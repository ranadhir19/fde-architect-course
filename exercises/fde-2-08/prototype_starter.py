"""Starter for FDE 2.08. Copy to prototype.py and complete it.

Compute every value from the delivered file at run time.
The grader imports RESULT from your prototype.py; accuracy
is scored against SOLUTION.md with RUBRIC.md.

The selection is specified exactly, so plans reproduce:
  - requests.json holds twelve requests, each with its
    id, prototype build time in hours (proto_hours), the
    ward lead's demo value (value, 1 to 5), a blocked
    flag, a safety flag, a fakeable flag, and a
    harden_note (empty when the shortcut leaves no
    named production work behind).
  - The timebox is 16 prototype hours. Faking one
    feature costs 1 hour.
  - Deferred: blocked requests, plus safety-critical
    requests that are not fakeable.
  - Faked: safety-critical, fakeable, unblocked
    requests. Faked hours are paid first.
  - Built for real: the remaining requests, ranked by
    value divided by proto_hours, highest first, ties
    broken by id ascending. Take a request while its
    proto_hours fit the hours left; a request that does
    not fit is cut, and later requests are still tried.
  - Cut: a remaining request the hours could not fit.
  - The harden list is every prototype item (built or
    faked) whose harden_note is non-empty.
  - Demo-ready: the demo value carried by built plus
    faked items is at least 20, inside the timebox.
    The verdict string is "demo_ready" or "not_ready".
  - Id lists are sorted ascending. Coverage is the
    prototype value divided by the total value,
    rounded to 4 decimal places.
"""
import json
from pathlib import Path

HERE = Path(__file__).parent

TIMEBOX_HOURS = 16
FAKE_HOURS = 1


def load(name):
    return json.loads((HERE / name).read_text(encoding="utf-8"))


def build_result(requests):
    # Replace each placeholder with a computed value.
    return {
        "requests_total": 0,
        "value_total": 0,
        "blocked_count": 0,
        "deferred_count": 0,
        "deferred_ids": [],
        "fake_count": 0,
        "fake_ids": [],
        "fake_hours": 0,
        "real_count": 0,
        "real_ids": [],
        "real_hours": 0,
        "cut_count": 0,
        "cut_ids": [],
        "prototype_items": 0,
        "prototype_hours": 0,
        "timebox_hours": TIMEBOX_HOURS,
        "slack_hours": 0,
        "prototype_value": 0,
        "value_coverage": 0.0,
        "harden_count": 0,
        "harden_ids": [],
        "demo_ready": False,
        "verdict": "",              # "demo_ready" or "not_ready"
    }


RESULT = build_result(load("requests.json"))

if __name__ == "__main__":
    for key, value in RESULT.items():
        print(f"{key}: {value}")
