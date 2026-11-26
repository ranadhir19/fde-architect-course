"""Grader for FDE 2.03. Run: python -m pytest test_retrieval.py -q

Checks structure and the two target conditions automatically;
accuracy is scored against SOLUTION.md with RUBRIC.md (the
answer key is deliberately not in code, so attempting the
exercise cannot leak it).
"""
import retrieval

KEYS = {
    "documents_total", "documents_indexed", "restricted_excluded",
    "queries_evaluated", "hits_at_5", "recall_at_5",
    "precision_at_5", "restricted_returned",
}


def test_all_results_present():
    assert set(retrieval.RESULT) == KEYS


def test_document_partition():
    r = retrieval.RESULT
    assert r["documents_indexed"] + r["restricted_excluded"] == r["documents_total"]


def test_recall_target_met():
    # The target agreed with the customer: recall at 5 of at least 0.90.
    assert retrieval.RESULT["recall_at_5"] >= 0.90


def test_guardrail_holds():
    # The other half of the target: zero restricted documents returned.
    assert retrieval.RESULT["restricted_returned"] == 0


def test_hits_consistent_with_recall():
    r = retrieval.RESULT
    # Each query has a gold set of two, so total possible hits
    # are twice the query count, and recall is hits over that.
    possible = 2 * r["queries_evaluated"]
    assert abs(r["recall_at_5"] - round(r["hits_at_5"] / possible, 4)) < 0.001


def test_precision_consistent_with_hits():
    r = retrieval.RESULT
    expected = round(r["hits_at_5"] / (5 * r["queries_evaluated"]), 4)
    assert abs(r["precision_at_5"] - expected) < 0.001
