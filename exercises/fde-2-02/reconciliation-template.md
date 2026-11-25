# Reconciliation report — first morning (template)

Copy this file to `RECONCILIATION.md` and complete every section
from your pipeline's computed output. A number that does not come
from running the pipeline does not belong in the report.

## Coverage

- Orders drop as delivered: ___ raw rows, ___ unique orders,
  ___ duplicate rows.
- Payments export as delivered: ___ rows.
- Excluded from v1, named: ___ (the channel, and why).

## The breaks

| Break class | Count | Next owner | Next action |
|---|---|---|---|
| Amount mismatch | ___ | ___ | ___ |
| Orphan payment (no such order) | ___ | ___ | ___ |
| Unpaid order | ___ | ___ | ___ |

## The manifest discrepancy

- The manifest states ___; the file contains ___. Both numbers
  are reported. The discrepancy is owned by ___ and the question
  put to them is: ___

## Certification

- The feed I certify for the build: ___.
- The feed I refuse to certify until ___ answers ___: ___.
- What runs tonight, unchanged, so tomorrow's report is
  comparable to today's: ___.
