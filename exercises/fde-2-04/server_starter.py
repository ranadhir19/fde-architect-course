"""Starter for FDE 2.04. Copy to server.py and complete it.

Compute every value from the two delivered files at run time.
The grader imports RESULT from your server.py; accuracy is
scored against SOLUTION.md with RUBRIC.md.

The design is specified exactly, so numbers reproduce:
  - Exposure rule: an operation is exposed only if its kind
    is "read" and its data_class is "internal". Compute the
    exposed set from operations.json; never type the names.
  - Evaluation order for each request in requests.json:
    1. Tool not in the exposed set (including tool names that
       are not in the registry at all): denied_not_exposed.
    2. Caller role not in the operation's allowed_roles:
       denied_role.
    3. A required argument missing from the call's args:
       denied_bad_args.
    4. Otherwise: allowed.
  - Each request is counted once, under the first check it
    fails.
"""
import json
from pathlib import Path

HERE = Path(__file__).parent
OPERATIONS = HERE / "operations.json"
REQUESTS = HERE / "requests.json"


def load_operations():
    return json.loads(OPERATIONS.read_text(encoding="utf-8"))


def load_requests():
    return json.loads(REQUESTS.read_text(encoding="utf-8"))


def build_result(operations, requests):
    # Replace each placeholder with a computed value.
    return {
        "operations_total": 0,
        "operations_exposed": 0,    # operations the exposure rule admits
        "operations_withheld": 0,   # operations the rule keeps from the agent
        "requests_evaluated": 0,
        "requests_allowed": 0,
        "requests_denied": 0,
        "denied_not_exposed": 0,    # tool not exposed, or not in the registry
        "denied_role": 0,           # exposed tool, caller role not allowed
        "denied_bad_args": 0,       # exposed tool, allowed role, argument missing
    }


RESULT = build_result(load_operations(), load_requests())

if __name__ == "__main__":
    for key, value in RESULT.items():
        print(f"{key}: {value}")
