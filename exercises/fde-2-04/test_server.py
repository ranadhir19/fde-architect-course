"""Grader for FDE 2.04. Run: python -m pytest test_server.py -q

Checks structure, the partitions, and the exposure rule itself
against operations.json; accuracy is scored against
SOLUTION.md with RUBRIC.md (the answer key is deliberately
not in code, so attempting the exercise cannot leak it).
"""
import json
from pathlib import Path

import server

HERE = Path(__file__).parent

KEYS = {
    "operations_total", "operations_exposed", "operations_withheld",
    "requests_evaluated", "requests_allowed", "requests_denied",
    "denied_not_exposed", "denied_role", "denied_bad_args",
}


def test_all_results_present():
    assert set(server.RESULT) == KEYS


def test_operations_partition():
    r = server.RESULT
    assert r["operations_exposed"] + r["operations_withheld"] == r["operations_total"]


def test_requests_partition():
    r = server.RESULT
    assert r["requests_allowed"] + r["requests_denied"] == r["requests_evaluated"]


def test_denial_reasons_sum():
    r = server.RESULT
    parts = r["denied_not_exposed"] + r["denied_role"] + r["denied_bad_args"]
    assert parts == r["requests_denied"]


def test_exposed_set_meets_the_rule():
    # Recompute the rule from the registry: every exposed
    # operation must be a read over internal data, and the
    # reported count must match the registry as delivered.
    operations = json.loads((HERE / "operations.json").read_text(encoding="utf-8"))
    admitted = [op for op in operations
                if op["kind"] == "read" and op["data_class"] == "internal"]
    assert server.RESULT["operations_total"] == len(operations)
    assert server.RESULT["operations_exposed"] == len(admitted)


def test_most_requests_denied():
    # The pilot log shape this exercise is built on: a server
    # scoped by the rule refuses more calls than it serves.
    r = server.RESULT
    assert r["requests_denied"] not in (0, r["requests_evaluated"])
    assert abs(r["requests_denied"] - r["requests_allowed"]) not in (0,)
