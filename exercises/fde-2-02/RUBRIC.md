# FDE 2.02 Rubric — 24 points

| Section | Points | What earns them |
|---|---|---|
| Computed reconciliation | 8 | All nine RESULT values computed from the files and matching SOLUTION.md exactly (raw and unique orders, duplicates, payments, matched, mismatches, orphans, unpaid, matched total). Hand-typed numbers score zero here even if correct — the program is the artefact. |
| Partition discipline | 5 | Both partitions shown in the report and summing exactly: order classes to unique orders, payment classes to payments raw. A class invented to make the sums work scores zero. |
| Idempotency | 4 | The pipeline returns the identical RESULT on a second run over the same drop, and the report states the de-duplication key (order id) and why re-sending a segment cannot double-count. |
| Break ownership | 4 | Each break class carries a named next owner and a next action with a date or trigger — not "investigate further". The amount-mismatch class names the gateway-fee explanation as a hypothesis to confirm with finance, not as a settled fact. |
| Manifest and exclusion honesty | 3 | The manifest discrepancy reported with both numbers (380 stated, 400 delivered) and a named owner; phone-email orders named as excluded from v1 with the reason. |

**Automatic fails:** adjusting either file's amounts so the
reconciliation balances; silently dropping duplicate rows
without counting them; reporting an orphan payment as an unpaid
order (or the reverse); claiming the two files cover all orders
while the email channel exists.
