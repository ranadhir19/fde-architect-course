"""Starter for FDE 2.02. Copy to pipeline.py and complete it.

Compute every value from the two delivered files at run time.
The grader imports RESULT from your pipeline.py; accuracy is
scored against SOLUTION.md with RUBRIC.md. The pipeline must be
idempotent: a second run over the same files returns the same
RESULT.
"""
import csv
from pathlib import Path

HERE = Path(__file__).parent
ORDERS = HERE / "orders_drop.csv"
PAYMENTS = HERE / "payments_export.csv"


def load_orders():
    # The drop is semicolon-delimited; dates are DD/MM/YYYY.
    with ORDERS.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter=";"))


def load_payments():
    with PAYMENTS.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def build_result(orders, payments):
    # Replace each placeholder with a computed value.
    return {
        "orders_raw": 0,
        "orders_unique": 0,        # distinct order_id values in the drop
        "duplicate_order_rows": 0,  # raw rows beyond the first copy of each order_id
        "payments_raw": 0,
        "matched_exact": 0,         # unique orders whose payment amount equals the order amount
        "amount_mismatches": 0,     # unique orders with a payment for a different amount
        "orphan_payments": 0,       # payments whose order_id is not in the drop
        "unpaid_orders": 0,         # unique orders with no payment
        "matched_total_cents": 0,   # sum of order amounts over matched_exact orders
    }


RESULT = build_result(load_orders(), load_payments())

if __name__ == "__main__":
    for key, value in RESULT.items():
        print(f"{key}: {value}")
