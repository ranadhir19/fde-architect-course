"""Grader for FDE 2.06. Run: python -m pytest test_gate.py -q

Checks structure, the partitions, and the gate computation
itself against runs.json and canary.json; accuracy is scored
against SOLUTION.md with RUBRIC.md (the answer key is
deliberately not in code, so attempting the exercise cannot
leak it).
"""
import json
from pathlib import Path

import gate

HERE = Path(__file__).parent

KEYS = {
    "records_total", "baseline_pass", "baseline_fail",
    "baseline_critical_fail",
    "v14_pass", "v14_fail", "v14_pass_delta",
    "v14_max_category_fail_increase", "v14_critical_fail",
    "v14_critical_delta", "v14_gate",
    "v15_pass", "v15_fail", "v15_pass_delta",
    "v15_max_category_fail_increase", "v15_critical_fail",
    "v15_critical_delta", "v15_gate",
    "shadow_records", "shadow_pass", "shadow_pass_rate",
    "canary_records", "canary_pass", "canary_pass_rate",
    "canary_critical_fail", "canary_worst_block_rate",
    "kill_switch_triggered", "promotion_verdict",
}

CATS = ["grounded", "omission", "fabrication", "boundary",
        "stale_guidance"]


def test_all_results_present():
    assert set(gate.RESULT) == KEYS


def test_version_partitions():
    r = gate.RESULT
    assert r["baseline_pass"] + r["baseline_fail"] == r["records_total"]
    assert r["v14_pass"] + r["v14_fail"] == r["records_total"]
    assert r["v15_pass"] + r["v15_fail"] == r["records_total"]


def test_record_partitions():
    r = gate.RESULT
    runs = json.loads((HERE / "runs.json").read_text(encoding="utf-8"))
    records = json.loads((HERE / "canary.json").read_text(encoding="utf-8"))
    assert r["records_total"] == len(runs)
    assert r["shadow_records"] + r["canary_records"] == len(records)


def test_slice_rule_matches_the_file():
    # Recompute v1.4's largest category failure increase from
    # runs.json: the reported value must be the file's value.
    runs = json.loads((HERE / "runs.json").read_text(encoding="utf-8"))

    def fails(ver, cat):
        return sum(1 for x in runs
                   if x[ver] == "fail" and x["category"] == cat)

    increase = max(fails("v14_candidate", c) - fails("v1_baseline", c)
                   for c in CATS)
    assert gate.RESULT["v14_max_category_fail_increase"] == increase


def test_gate_verdicts_follow_the_rules():
    # Recompute both verdicts from the reported counts by the
    # three rules in gate-design.md.
    r = gate.RESULT
    for prefix in ["v14", "v15"]:
        verdict = "pass"
        if r[f"{prefix}_pass"] < r["baseline_pass"] - 1:
            verdict = "fail"
        if r[f"{prefix}_max_category_fail_increase"] > 1:
            verdict = "fail"
        if r[f"{prefix}_critical_delta"] > 0:
            verdict = "fail"
        assert r[f"{prefix}_gate"] == verdict


def test_kill_switch_and_promotion_follow():
    # Recompute the worst canary block and the two verdicts
    # that depend on it.
    records = json.loads((HERE / "canary.json").read_text(encoding="utf-8"))
    canary = [x for x in records if x["mode"] == "canary"]
    blocks = [canary[i:i + 20] for i in range(0, len(canary), 20)]
    worst = min(sum(1 for x in b if x["result"] == "pass") / len(b)
                for b in blocks)
    r = gate.RESULT
    assert r["canary_worst_block_rate"] == round(worst, 4)
    triggered = any(x["critical_fail"] for x in canary) or worst < 0.70
    assert r["kill_switch_triggered"] == triggered
    promote = (r["v15_gate"] == "pass" and not triggered
               and r["canary_pass_rate"] >= r["shadow_pass_rate"] - 0.10)
    assert r["promotion_verdict"] == ("promote" if promote else "hold")
