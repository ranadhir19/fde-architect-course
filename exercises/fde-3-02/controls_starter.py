"""Starter for FDE 3.02. Copy to controls.py and complete it.

Compute every value from the delivered file at run time.
The grader imports RESULT from your controls.py; accuracy
is scored against SOLUTION.md with RUBRIC.md.

The mapping is specified exactly, so maps reproduce:
  - controls.json holds fourteen controls, each with its
    id, name, frameworks list, evidence artefact,
    evidence_present flag, evidence age in days (null
    when the artefact does not exist), maximum evidence
    age in days, owner (blank when nobody is named),
    is_gate flag, and a workshop note.
  - A control's status is the first failing check, in
    this order: "missing" when the evidence artefact
    does not exist; "stale" when its age in days is
    greater than the maximum evidence age; "unowned"
    when it exists and is fresh but no owner is named;
    otherwise "satisfied".
  - A control counts toward every framework in its
    frameworks list. soc2_total and hipaa_total are the
    numbers of controls tagged for each framework, and
    the per-framework satisfied counts are how many of
    those are satisfied.
  - gate_total is the number of controls whose is_gate
    flag is true; gate_satisfied_count is how many of
    those are satisfied; gate_gap_ids is the sorted list
    of gate controls in any gap status.
  - Verdict: "ready" when every control is satisfied;
    "not_ready" when at least one gate control is in a
    gap status; otherwise "ready_with_scheduled_gaps".
  - Id lists are sorted ascending.
"""
import json
from pathlib import Path

HERE = Path(__file__).parent


def load(name):
    return json.loads((HERE / name).read_text(encoding="utf-8"))


def build_result(controls):
    # Replace each placeholder with a computed value.
    return {
        "controls_total": 0,
        "satisfied_count": 0,
        "missing_count": 0,
        "stale_count": 0,
        "unowned_count": 0,
        "satisfied_ids": [],
        "missing_ids": [],
        "stale_ids": [],
        "unowned_ids": [],
        "gate_total": 0,
        "gate_satisfied_count": 0,
        "gate_gap_ids": [],
        "soc2_total": 0,
        "soc2_satisfied_count": 0,
        "hipaa_total": 0,
        "hipaa_satisfied_count": 0,
        "verdict": "",              # per the verdict rules
    }


RESULT = build_result(load("controls.json"))

if __name__ == "__main__":
    for key, value in RESULT.items():
        print(f"{key}: {value}")
