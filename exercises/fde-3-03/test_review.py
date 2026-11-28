"""Grader for FDE 3.03. Run: python -m pytest test_review.py -q

Checks structure, the partitions, and the answering
computation itself against questionnaire.json; accuracy
is scored against SOLUTION.md with RUBRIC.md (the
answer key is deliberately not in code, so attempting
the exercise cannot leak it).
"""
import json
from pathlib import Path

import review

HERE = Path(__file__).parent

KEYS = {
    "questions_total",
    "supported_count", "partial_count", "stale_count", "unsupported_count",
    "supported_ids", "partial_ids", "stale_ids", "unsupported_ids",
    "gate_total", "gate_supported_count", "gate_gap_ids",
    "overclaim_count", "overclaim_ids",
    "sections_count", "verdict",
}

STATUSES = ["supported", "partial", "stale", "unsupported"]


def load():
    return json.loads((HERE / "questionnaire.json").read_text(encoding="utf-8"))


def status(q):
    if not q["evidence_present"]:
        return "unsupported"
    if q["evidence_age_days"] > q["max_evidence_age_days"]:
        return "stale"
    if not q["scope_covers"]:
        return "partial"
    return "supported"


def expected_status(s):
    return sorted(q["id"] for q in load() if status(q) == s)


def test_all_results_present():
    assert set(review.RESULT) == KEYS


def test_partitions_hold():
    r = review.RESULT
    qs = load()
    assert r["questions_total"] == len(qs)
    total = sum(r[f"{s}_count"] for s in STATUSES)
    assert total == r["questions_total"]
    seen = []
    for s in STATUSES:
        assert r[f"{s}_ids"] == expected_status(s), s
        assert r[f"{s}_count"] == len(r[f"{s}_ids"]), s
        seen += r[f"{s}_ids"]
    assert sorted(seen) == sorted(q["id"] for q in qs)


def test_status_precedence():
    # The first failing check decides: a question with
    # no artefact reports as unsupported whatever else
    # the record says, and a stale artefact reports as
    # stale even when its scope is also partial.
    r = review.RESULT
    for q in load():
        assert q["id"] in r[f"{status(q)}_ids"], q["id"]


def test_gate_counts():
    r = review.RESULT
    gates = [q for q in load() if q["is_gate"]]
    assert r["gate_total"] == len(gates)
    assert r["gate_supported_count"] == sum(
        1 for q in gates if status(q) == "supported")
    assert r["gate_gap_ids"] == sorted(
        q["id"] for q in gates if status(q) != "supported")


def test_overclaims():
    r = review.RESULT
    expected = sorted(q["id"] for q in load()
                      if q["draft_claim"] == "yes"
                      and status(q) != "supported")
    assert r["overclaim_ids"] == expected
    assert r["overclaim_count"] == len(expected)


def test_sections_and_verdict():
    r = review.RESULT
    assert r["sections_count"] == len({q["section"] for q in load()})
    if all(status(q) == "supported" for q in load()):
        assert r["verdict"] == "ready_to_submit"
    elif r["gate_gap_ids"]:
        assert r["verdict"] == "blocked"
    else:
        assert r["verdict"] == "submit_with_qualifications"


def test_gate_gaps_block_this_return():
    # The delivered file carries gate gaps and
    # overclaims by design; a pack that reports this
    # return ready has misread it.
    r = review.RESULT
    assert r["gate_gap_ids"], "expected gate gaps in the delivered file"
    assert r["overclaim_ids"], "expected overclaims in the delivered file"
    assert r["verdict"] == "blocked"
