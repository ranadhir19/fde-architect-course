"""Starter for FDE 2.09. Copy to security.py and complete it.

Compute every value from the delivered file at run time.
The grader imports RESULT from your security.py; accuracy
is scored against SOLUTION.md with RUBRIC.md.

The hardening selection is specified exactly, so plans
reproduce:
  - findings.json holds fourteen findings, each with its
    id, finding text, category (pii, residency, secrets,
    injection, access, logging), severity (1 to 5),
    likelihood (1 to 5), risk (severity times likelihood,
    as recorded), a blocked flag, the blocker text (empty
    when unblocked), and the fix cost in hours.
  - Deferred: blocked findings. A blocked finding is
    deferred however high its risk scores; the fix waits
    on the customer action named in its blocker text.
  - Ranking: the unblocked findings, by risk descending,
    ties broken by id ascending.
  - Fixed: the first three findings in that ranking,
    plus every other unblocked finding whose risk equals
    the third finding's risk. A tie at the cut line is
    fixed, not split by the id tie-break.
  - Backlog: unblocked findings that are not fixed.
  - The fix budget is 16 hours. Slack is the budget
    minus the fixed findings' fix hours.
  - risk_reduction is the fixed risk divided by the
    total risk, rounded to 4 decimal places.
  - residual_risk is the total risk minus the fixed
    risk (deferred and backlog risk both remain).
  - max_residual_unblocked_risk is the highest risk
    among backlog findings, or 0 when the backlog is
    empty.
  - Hardened for pilot: the fixed hours fit the budget
    and no backlog finding carries a risk of 20 or
    more. The verdict string is "hardened_for_pilot"
    or "not_hardened".
  - Id lists are sorted ascending. Category counts are
    counts of findings in that category in the file.
"""
import json
from pathlib import Path

HERE = Path(__file__).parent

FIX_BUDGET_HOURS = 16


def load(name):
    return json.loads((HERE / name).read_text(encoding="utf-8"))


def build_result(findings):
    # Replace each placeholder with a computed value.
    return {
        "findings_total": 0,
        "risk_total": 0,
        "blocked_count": 0,
        "deferred_count": 0,
        "deferred_ids": [],
        "deferred_risk": 0,
        "fixed_count": 0,
        "fixed_ids": [],
        "fixed_hours": 0,
        "fix_budget_hours": FIX_BUDGET_HOURS,
        "slack_hours": 0,
        "fixed_risk": 0,
        "risk_reduction": 0.0,
        "backlog_count": 0,
        "backlog_ids": [],
        "backlog_risk": 0,
        "residual_risk": 0,
        "max_residual_unblocked_risk": 0,
        "pii_count": 0,
        "secrets_count": 0,
        "injection_count": 0,
        "residency_count": 0,
        "hardened": False,
        "verdict": "",              # "hardened_for_pilot" or "not_hardened"
    }


RESULT = build_result(load("findings.json"))

if __name__ == "__main__":
    for key, value in RESULT.items():
        print(f"{key}: {value}")
