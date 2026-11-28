"""Grader for FDE 3.02. Run: python -m pytest test_controls.py -q

Checks structure, the partitions, and the mapping
computation itself against controls.json; accuracy is
scored against SOLUTION.md with RUBRIC.md (the answer
key is deliberately not in code, so attempting the
exercise cannot leak it).
"""
import json
from pathlib import Path

import controls

HERE = Path(__file__).parent

KEYS = {
    "controls_total",
    "satisfied_count", "missing_count", "stale_count", "unowned_count",
    "satisfied_ids", "missing_ids", "stale_ids", "unowned_ids",
    "gate_total", "gate_satisfied_count", "gate_gap_ids",
    "soc2_total", "soc2_satisfied_count",
    "hipaa_total", "hipaa_satisfied_count",
    "verdict",
}

STATUSES = ["satisfied", "missing", "stale", "unowned"]


def load():
    return json.loads((HERE / "controls.json").read_text(encoding="utf-8"))


def status(c):
    if not c["evidence_present"]:
        return "missing"
    if c["evidence_age_days"] > c["max_evidence_age_days"]:
        return "stale"
    if not c["owner"]:
        return "unowned"
    return "satisfied"


def expected_status(s):
    return sorted(c["id"] for c in load() if status(c) == s)


def test_all_results_present():
    assert set(controls.RESULT) == KEYS


def test_partitions_hold():
    r = controls.RESULT
    comps = load()
    assert r["controls_total"] == len(comps)
    total = sum(r[f"{s}_count"] for s in STATUSES)
    assert total == r["controls_total"]
    seen = []
    for s in STATUSES:
        assert r[f"{s}_ids"] == expected_status(s), s
        assert r[f"{s}_count"] == len(r[f"{s}_ids"]), s
        seen += r[f"{s}_ids"]
    assert sorted(seen) == sorted(c["id"] for c in comps)


def test_status_precedence():
    # The first failing check decides: a control that is
    # both stale and unowned reports as stale, and a
    # missing artefact reports as missing whatever else
    # the record says.
    r = controls.RESULT
    for c in load():
        assert c["id"] in r[f"{status(c)}_ids"], c["id"]


def test_gate_counts():
    r = controls.RESULT
    gates = [c for c in load() if c["is_gate"]]
    assert r["gate_total"] == len(gates)
    assert r["gate_satisfied_count"] == sum(
        1 for c in gates if status(c) == "satisfied")
    assert r["gate_gap_ids"] == sorted(
        c["id"] for c in gates if status(c) != "satisfied")


def test_framework_counts():
    r = controls.RESULT
    for key, tag in [("soc2", "SOC2"), ("hipaa", "HIPAA")]:
        sel = [c for c in load() if tag in c["frameworks"]]
        assert r[f"{key}_total"] == len(sel), key
        assert r[f"{key}_satisfied_count"] == sum(
            1 for c in sel if status(c) == "satisfied"), key


def test_verdict_follows_the_gate():
    r = controls.RESULT
    if all(status(c) == "satisfied" for c in load()):
        assert r["verdict"] == "ready"
    elif r["gate_gap_ids"]:
        assert r["verdict"] == "not_ready"
    else:
        assert r["verdict"] == "ready_with_scheduled_gaps"


def test_a_gate_gap_means_not_ready_here():
    # The delivered file carries gate gaps by design; a
    # map that reports this build ready has misread it.
    r = controls.RESULT
    assert r["gate_gap_ids"], "expected gate gaps in the delivered file"
    assert r["verdict"] == "not_ready"
