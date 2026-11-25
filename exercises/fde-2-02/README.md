# FDE 2.02 Exercise — Build the ingestion and reconciliation pipeline

**Topic:** Legacy integration as the main event (Layer 3). **Part (d) of FDE 2.02.**
Attempt this before watching the tutorial half of the lesson.
**Prerequisite:** FDE 2.01 (data before models) — the audit discipline
carries straight into the build.

## The task

Read `legacy-systems.md` first. It describes Alder Creek Health
Network's two feeds as they actually arrive: a stock-and-orders
system that speaks only in a nightly SFTP file drop, and a billing
system that exports a different dialect entirely. There is no API
to call. The file drop is the interface.

Then build the pipeline that joins them:

1. `pipeline.py`, built from `pipeline_starter.py`: ingest
   `orders_drop.csv` (semicolon-delimited, dates as DD/MM/YYYY)
   and `payments_export.csv` (comma-delimited, dates as
   YYYY-MM-DD), de-duplicate the orders drop by order id without
   losing the duplicate count, and reconcile orders against
   payments. Every value in the `RESULT` dictionary the grader
   checks must be computed from the files at run time.
2. `RECONCILIATION.md` from `reconciliation-template.md`: the
   report you would send on the first morning the pipeline runs —
   every count, every break class with its named next owner, the
   manifest discrepancy, and the one feed you refuse to certify
   until its owner answers a named question.

Idempotency is part of the task, not an extra: running the
pipeline twice over the same drop must produce the same result.
A pipeline that double-counts on a re-run will double-count in
production on the first retried night.

## Done means

- Orders are counted twice over, honestly: raw rows as delivered,
  and unique orders after de-duplication — with the duplicate
  count stated, never silently absorbed.
- Every payment lands in exactly one class: matched exactly,
  amount mismatch, or orphan (no such order). Every unique order
  lands in exactly one class: matched exactly, amount mismatch,
  or unpaid. The classes partition both files; if your classes
  do not sum to the file totals, the reconciliation is not done.
- Amount mismatches are reported as a class with a size, not
  fixed by adjusting either side. Reconciliation reports breaks;
  it does not heal them.
- The manifest discrepancy in `legacy-systems.md` is named in
  the report with both numbers, not resolved by picking one.
- Phone orders arriving by email are named as excluded from v1,
  with the reason — never presented as missing data.
- Graded with `RUBRIC.md`. `SOLUTION.md` is the reference
  answer, released after the attempt window.

## The habit this exercise is really testing

- Legacy integration is the main event, not the warm-up. The
  model is the easy part; the drop that arrives late, twice, or
  in a new dialect is where deployments actually fail.
- Reconciliation is a promise: two systems that disagree produce
  a named break with a named owner, every night, in writing.
