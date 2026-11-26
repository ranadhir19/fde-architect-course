"""Starter for FDE 2.07. Copy to trace.py and complete it.

Compute every value from the delivered file at run time.
The grader imports RESULT from your trace.py; accuracy is
scored against SOLUTION.md with RUBRIC.md.

The summary is specified exactly, so reports reproduce:
  - traces.json holds one record per production trace:
    its day (1 to 7), topic, result ("pass" or "fail"),
    a critical_fail flag, latency_ms and cost_cents.
  - The early window is days 1 to 4 and the late window
    is days 5 to 7. late_pass_delta is the late pass rate
    minus the early pass rate, rounded to 4 dp.
  - The watched topic is "medication". Its share in a
    window is its record count divided by the window's
    record count. drift_detected is True when the late
    share minus the early share exceeds 0.10.
  - A latency breach is a trace above 2,000 ms; a cost
    breach is a trace above 30 cents.
  - The alert verdict follows observability-design.md:
    alert when the late delta is at most -0.05, or drift
    is detected, or any critical failure occurred, or the
    latency breach rate exceeds 0.05; otherwise healthy.
    The verdict string is "alert" or "healthy".
  - Rates are rounded to 4 decimal places; means to 2.
"""
import json
from pathlib import Path

HERE = Path(__file__).parent


def load(name):
    return json.loads((HERE / name).read_text(encoding="utf-8"))


def build_result(traces):
    # Replace each placeholder with a computed value.
    return {
        "traces_total": 0,
        "days": 0,
        "pass": 0,
        "fail": 0,
        "pass_rate": 0.0,
        "early_records": 0,
        "early_pass": 0,
        "early_pass_rate": 0.0,
        "late_records": 0,
        "late_pass": 0,
        "late_pass_rate": 0.0,
        "late_pass_delta": 0.0,          # late minus early
        "critical_failures": 0,
        "medication_records": 0,
        "medication_pass": 0,
        "medication_pass_rate": 0.0,
        "medication_share_early": 0.0,
        "medication_share_late": 0.0,
        "medication_share_delta": 0.0,  # late minus early
        "drift_detected": False,
        "mean_latency_ms": 0.0,
        "max_latency_ms": 0,
        "latency_breaches": 0,
        "latency_breach_rate": 0.0,
        "total_cost_cents": 0.0,
        "mean_cost_cents": 0.0,
        "cost_breaches": 0,             # traces above 30 cents
        "alert_triggered": False,
        "verdict": "",                  # "alert" or "healthy"
    }


RESULT = build_result(load("traces.json"))

if __name__ == "__main__":
    for key, value in RESULT.items():
        print(f"{key}: {value}")
