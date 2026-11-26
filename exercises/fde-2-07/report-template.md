# WEEK.md — weekly quality report (template)

Hand this to the ward lead. Every number comes from your
own run of `trace.py` over `traces.json` as delivered.

## The week in one line

- Traces (n) over (n) days; pass (n), fail (n), overall
  pass rate. Verdict: alert or healthy.

## The windows

- Early (days 1 to 4): records (n), pass rate.
- Late (days 5 to 7): records (n), pass rate.
- Delta (late minus early), in percentage points, with
  one line on what a delta of this size does and does not
  prove on samples of this size.

## The slice under watch

- Medication topic: records (n), pass rate against the
  overall rate.
- Medication share, early window and late window, and the
  delta. Drift: declared or not, by the pre-agreed rule.

## Budgets and critical failures

- Latency: mean, maximum, breaches of the 2,000 ms budget
  (n and rate).
- Cost: total and mean in cents, breaches of the 30-cent
  budget (n).
- Critical failures (n), with the days they fell on if
  your run records them.

## The verdict, rule by rule

- A1 window drop: fired or not, with the margin.
- A2 drift: fired or not, with the margin.
- A3 critical failure: fired or not.
- A4 latency breaches: fired or not, with the margin.
- The verdict that follows from the rules as written.

## What the traces cannot say

- One line each: what a graded trace sample cannot detect
  (an ungraded failure mode, a topic nobody routed yet),
  and what FDE 2.08's prototype work must not assume from
  this week's numbers.
