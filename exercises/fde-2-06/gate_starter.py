"""Starter for FDE 2.06. Copy to gate.py and complete it.

Compute every value from the delivered files at run time.
The grader imports RESULT from your gate.py; accuracy is
scored against SOLUTION.md with RUBRIC.md.

The gate is specified exactly, so verdicts reproduce:
  - runs.json holds one record per gold case: its category,
    a critical flag (True for the boundary cases), and each
    version's result, "pass" or "fail".
  - A category's failure increase for a candidate is its
    fail count in that category minus baseline's fail count
    in the same category. The reported increase is the
    maximum over the five categories (it may be negative
    when every category improved or held).
  - Gate rules, applied as written in gate-design.md:
    G1 fails a candidate passing fewer than baseline
    passes minus 1; G2 fails a candidate whose maximum
    category failure increase exceeds 1; G3 fails a
    candidate whose critical failures exceed baseline's.
    The verdict is "pass" only if no rule fails it.
  - canary.json holds the passing candidate's shadow and
    canary records in order. Canary blocks are consecutive
    groups of 20 canary records, in file order. The worst
    block rate is the lowest block pass rate.
  - The kill switch triggers if any canary record has
    critical_fail set, or the worst block rate is below
    0.70. Promotion is "promote" only if v1.5 passed the
    gate, the kill switch did not trigger, and the canary
    pass rate is at least the shadow pass rate minus 0.10;
    otherwise it is "hold".
  - Rates are rounded to 4 decimal places.
"""
import json
from pathlib import Path

HERE = Path(__file__).parent
RUNS = HERE / "runs.json"
CANARY = HERE / "canary.json"

CATEGORIES = ["grounded", "omission", "fabrication",
              "boundary", "stale_guidance"]


def load(name):
    return json.loads((HERE / name).read_text(encoding="utf-8"))


def build_result(runs, records):
    # Replace each placeholder with a computed value.
    return {
        "records_total": 0,
        "baseline_pass": 0,
        "baseline_fail": 0,
        "baseline_critical_fail": 0,
        "v14_pass": 0,
        "v14_fail": 0,
        "v14_pass_delta": 0,            # v1.4 passes minus baseline
        "v14_max_category_fail_increase": 0,
        "v14_critical_fail": 0,
        "v14_critical_delta": 0,        # v1.4 critical minus baseline
        "v14_gate": "",                 # "pass" or "fail"
        "v15_pass": 0,
        "v15_fail": 0,
        "v15_pass_delta": 0,
        "v15_max_category_fail_increase": 0,
        "v15_critical_fail": 0,
        "v15_critical_delta": 0,
        "v15_gate": "",                 # "pass" or "fail"
        "shadow_records": 0,
        "shadow_pass": 0,
        "shadow_pass_rate": 0.0,        # rounded to 4 dp
        "canary_records": 0,
        "canary_pass": 0,
        "canary_pass_rate": 0.0,        # rounded to 4 dp
        "canary_critical_fail": 0,      # canary records flagged critical
        "canary_worst_block_rate": 0.0,  # blocks of 20, rounded to 4 dp
        "kill_switch_triggered": False,
        "promotion_verdict": "",        # "promote" or "hold"
    }


RESULT = build_result(load("runs.json"), load("canary.json"))

if __name__ == "__main__":
    for key, value in RESULT.items():
        print(f"{key}: {value}")
