"""Starter for FDE 3.01. Copy to topology.py and complete it.

Compute every value from the delivered file at run time.
The grader imports RESULT from your topology.py; accuracy
is scored against SOLUTION.md with RUBRIC.md.

The placement is specified exactly, so designs reproduce:
  - components.json holds twelve components, each with its
    id, name, requires_internet flag, self_hostable flag,
    sends_regulated_data_out flag, is_core flag, adapt cost
    in hours, and a discovery note.
  - Cloud VPC: a component that sends regulated data out
    is "adapt" (re-pointed to the vendor private endpoint);
    every other component is "as_is". Nothing is blocked.
  - On-premises: a component that does not require the
    internet is "as_is". One that requires it and is
    self-hostable is "adapt". One that requires it, is not
    self-hostable, and sends no regulated data out is
    "adapt" (allowlisted proxy). One that requires it, is
    not self-hostable, and sends regulated data out is
    "blocked".
  - Air-gapped: a component that does not require the
    internet is "as_is". One that requires it and is
    self-hostable is "adapt". One that requires it and is
    not self-hostable is "blocked", whatever it carries.
  - adapt_hours for a topology is the sum of the adapt
    costs of its adapted components.
  - blocked_core_count is the number of blocked components
    whose is_core flag is true.
  - Verdict: "feasible" when nothing is blocked;
    "feasible_with_cuts" when blocked components exist and
    none is core; "not_feasible_as_designed" when a core
    component is blocked.
  - Id lists are sorted ascending.
"""
import json
from pathlib import Path

HERE = Path(__file__).parent


def load(name):
    return json.loads((HERE / name).read_text(encoding="utf-8"))


def build_result(components):
    # Replace each placeholder with a computed value.
    return {
        "components_total": 0,
        "cloud_as_is_count": 0,
        "cloud_adapt_count": 0,
        "cloud_blocked_count": 0,
        "cloud_adapt_ids": [],
        "cloud_blocked_ids": [],
        "cloud_adapt_hours": 0,
        "cloud_blocked_core_count": 0,
        "cloud_verdict": "",          # per the verdict rules
        "onprem_as_is_count": 0,
        "onprem_adapt_count": 0,
        "onprem_blocked_count": 0,
        "onprem_adapt_ids": [],
        "onprem_blocked_ids": [],
        "onprem_adapt_hours": 0,
        "onprem_blocked_core_count": 0,
        "onprem_verdict": "",         # per the verdict rules
        "airgap_as_is_count": 0,
        "airgap_adapt_count": 0,
        "airgap_blocked_count": 0,
        "airgap_adapt_ids": [],
        "airgap_blocked_ids": [],
        "airgap_adapt_hours": 0,
        "airgap_blocked_core_count": 0,
        "airgap_verdict": "",         # per the verdict rules
    }


RESULT = build_result(load("components.json"))

if __name__ == "__main__":
    for key, value in RESULT.items():
        print(f"{key}: {value}")
