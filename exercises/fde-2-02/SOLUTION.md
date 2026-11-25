# FDE 2.02 Reference solution

Released after the attempt window. All counts are of the files
as delivered and are reproduced by the reference `pipeline.py`.

## The counts

| Finding | Value |
|---|---|
| orders_raw | 400 |
| orders_unique | 376 |
| duplicate_order_rows | 24 |
| payments_raw | 360 |
| matched_exact | 320 |
| amount_mismatches | 20 |
| orphan_payments | 20 |
| unpaid_orders | 36 |
| matched_total_cents | 10696078 |

Both partitions hold, and a strong report shows them:
320 + 20 + 36 = 376 unique orders, and
320 + 20 + 20 = 360 payments.

## What the breaks mean

- **Duplicates (24).** The clerk's belief that duplicates cannot
  happen is refuted by the file: 24 rows are exact second copies
  of an order already in the drop, consistent with the vendor's
  whole-segment re-send on a retried transfer. De-duplication is
  by order id, the duplicate count is reported every night, and
  a night with zero duplicates is the surprising one.
- **Amount mismatches (20).** Every mismatched payment settles
  exactly 500 cents below its order amount — a pattern, not
  noise. The gateway-fee note in `legacy-systems.md` is the
  leading hypothesis. It stays a hypothesis in the report until
  finance confirms which payment types the fee applies to;
  neither file is adjusted in the meantime.
- **Orphan payments (20).** Payments carrying order ids that
  exist nowhere in the drop, with real money attached. The
  hand-typed phone-order path at the billing desk is the likely
  source — which would make some orphans the payments half of
  the excluded email channel, visible from the money side only.
  They are reported as orphans, owned by the billing desk, and
  never reclassified as orders.
- **Unpaid orders (36).** Unique orders with no payment at all.
  Owned by finance for a same-week answer: expected lag, or the
  first list the nightly reconciliation exists to produce.

## The manifest discrepancy

The manifest states 380 orders; the file delivers 400 raw rows
holding 376 unique orders. Neither stated number matches either
computed number, and that is the finding: the manifest counts
something nobody can currently define. The report carries both
numbers, names the IT team as owner, and asks one question:
"What does the manifest count — rows written, orders created
that day, or orders the clerk expects?" Until it is answered,
the pipeline's computed counts are the report of record.

## Certification

- Certified for the build: the payments export — one operator,
  one dialect, internally consistent; its breaks are all
  visible from the reconciliation itself.
- Refused, for now: the orders drop as a sole source of order
  volume, until the orders vendor, reached through procurement,
  answers in writing whether a retried transfer can re-send a
  segment. The pipeline defends against the answer being yes;
  certification waits for the vendor to say so.
