"""Grader for FDE 2.07. Run: python -m pytest test_trace.py -q

Checks structure, the partitions, and the observability
computation itself against traces.json; accuracy is scored
against SOLUTION.md with RUBRIC.md (the answer key is
deliberately not in code, so attempting the exercise cannot
leak it).
"""
import json
from pathlib import Path

import trace

HERE = Path(__file__).parent

KEYS = {
    "traces_total", "days", "pass", "fail", "pass_rate",
    "early_records", "early_pass", "early_pass_rate",
    "late_records", "late_pass", "late_pass_rate",
    "late_pass_delta", "critical_failures",
    "medication_records", "medication_pass",
    "medication_pass_rate", "medication_share_early",
    "medication_share_late", "medication_share_delta",
    "drift_detected", "mean_latency_ms", "max_latency_ms",
    "latency_breaches", "latency_breach_rate",
    "total_cost_cents", "mean_cost_cents", "cost_breaches",
    "alert_triggered", "verdict",
}


def load():
    return json.loads((HERE / "traces.json").read_text(encoding="utf-8"))


def test_all_results_present():
    assert set(trace.RESULT) == KEYS


def test_partitions():
    r = trace.RESULT
    traces = load()
    assert r["pass"] + r["fail"] == r["traces_total"] == len(traces)
    assert r["early_records"] + r["late_records"] == r["traces_total"]
    assert r["days"] == len({t["day"] for t in traces})


def test_window_rates_match_the_file():
    traces = load()
    early = [t for t in traces if t["day"] in (1, 2, 3, 4)]
    late = [t for t in traces if t["day"] in (5, 6, 7)]
    er = round(sum(1 for t in early if t["result"] == "pass") / len(early), 4)
    lr = round(sum(1 for t in late if t["result"] == "pass") / len(late), 4)
    r = trace.RESULT
    assert r["early_pass_rate"] == er
    assert r["late_pass_rate"] == lr
    assert r["late_pass_delta"] == round(lr - er, 4)


def test_drift_matches_the_file():
    traces = load()
    early = [t for t in traces if t["day"] in (1, 2, 3, 4)]
    late = [t for t in traces if t["day"] in (5, 6, 7)]
    se = sum(1 for t in early if t["topic"] == "medication") / len(early)
    sl = sum(1 for t in late if t["topic"] == "medication") / len(late)
    r = trace.RESULT
    assert r["medication_share_early"] == round(se, 4)
    assert r["medication_share_late"] == round(sl, 4)
    assert r["medication_share_delta"] == round(round(sl, 4) - round(se, 4), 4) or r["medication_share_delta"] == round(sl - se, 4)
    assert r["drift_detected"] == (sl - se > 0.10)


def test_budgets_match_the_file():
    traces = load()
    r = trace.RESULT
    breaches = sum(1 for t in traces if t["latency_ms"] > 2000)
    assert r["latency_breaches"] == breaches
    assert r["latency_breach_rate"] == round(breaches / len(traces), 4)
    assert r["max_latency_ms"] == max(t["latency_ms"] for t in traces)
    assert r["cost_breaches"] == sum(1 for t in traces if t["cost_cents"] > 30)


def test_alert_follows_the_rules():
    r = trace.RESULT
    alert = (r["late_pass_delta"] <= -0.05 or r["drift_detected"]
             or r["critical_failures"] >= 1 or r["latency_breach_rate"] > 0.05)
    assert r["alert_triggered"] == alert
    assert r["verdict"] == ("alert" if alert else "healthy")
