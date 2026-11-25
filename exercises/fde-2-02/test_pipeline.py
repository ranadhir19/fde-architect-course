"""Grader for FDE 2.02. Run: python -m pytest test_pipeline.py -q

Checks structure automatically; accuracy is scored against
SOLUTION.md with RUBRIC.md (the answer key is deliberately not
in code, so attempting the exercise cannot leak it).
"""
import pipeline

KEYS = {
    "orders_raw", "orders_unique", "duplicate_order_rows",
    "payments_raw", "matched_exact", "amount_mismatches",
    "orphan_payments", "unpaid_orders", "matched_total_cents",
}


def test_all_results_present():
    assert set(pipeline.RESULT) == KEYS


def test_all_results_are_positive_ints():
    for key in KEYS:
        value = pipeline.RESULT[key]
        assert isinstance(value, int) and value > 0, f"{key}: {value!r}"


def test_orders_partition():
    r = pipeline.RESULT
    assert r["orders_unique"] + r["duplicate_order_rows"] == r["orders_raw"]


def test_unique_orders_partition():
    r = pipeline.RESULT
    assert (
        r["matched_exact"] + r["amount_mismatches"] + r["unpaid_orders"]
        == r["orders_unique"]
    )


def test_payments_partition():
    r = pipeline.RESULT
    assert (
        r["matched_exact"] + r["amount_mismatches"] + r["orphan_payments"]
        == r["payments_raw"]
    )


def test_idempotent_second_run():
    again = pipeline.build_result(pipeline.load_orders(), pipeline.load_payments())
    assert again == pipeline.RESULT
