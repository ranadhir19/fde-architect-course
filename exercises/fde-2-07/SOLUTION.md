# FDE 2.07 Reference solution

Released after the attempt window. All counts are of the
file as delivered and are reproduced by the reference
`trace.py`, built exactly to the starter's specification.

## The counts

| Finding | Value |
|---|---|
| traces_total | 280 |
| days | 7 |
| pass | 232 |
| fail | 48 |
| pass_rate | 0.8286 |
| early_records | 160 |
| early_pass | 138 |
| early_pass_rate | 0.8625 |
| late_records | 120 |
| late_pass | 94 |
| late_pass_rate | 0.7833 |
| late_pass_delta | -0.0792 |
| critical_failures | 3 |
| medication_records | 57 |
| medication_pass | 39 |
| medication_pass_rate | 0.6842 |
| medication_share_early | 0.0813 |
| medication_share_late | 0.3667 |
| medication_share_delta | 0.2854 |
| drift_detected | True |
| mean_latency_ms | 1194.12 |
| max_latency_ms | 2412 |
| latency_breaches | 11 |
| latency_breach_rate | 0.0393 |
| total_cost_cents | 6585.03 |
| mean_cost_cents | 23.52 |
| cost_breaches (above 30 cents) | 22 |
| alert_triggered | True |
| verdict | alert |

## The week, read through its windows

- Overall, the promoted system passes 232 of
  280 traces, a rate of 0.8286 —
  a number that, reported alone, reads as a good first
  week. The windows say what the average hides.
- Early (days 1 to 4): 138 of
  160, a rate of 0.8625.
  Late (days 5 to 7): 94 of
  120, a rate of 0.7833.
  The delta is -0.0792 — a drop of about
  eight percentage points, past the five-point A1 line.

## The drift that explains the shape, without proving the cause

- Medication questions were 0.0813
  of early traces and 0.3667 of
  late traces — a rise of 0.2854,
  far past the ten-point drift rule. Drift is declared.
- Medication is also the weakest topic in the record:
  39 passes from
  57 traces, a rate of
  0.6842 against the week's
  0.8286. A rising share of the weakest topic
  is consistent with the late drop; the report states
  that as consistency, not proof — the late window also
  contains every other topic, and their rates are part
  of the same record.
- The operational meaning is the gate's blind spot made
  visible: the 50-case set of FDE 2.05 and 2.06 barely
  covers medication, so a version can pass the gate and
  still be thin exactly where live traffic is growing.
  The corrective is a bigger medication slice in the
  gate set — proposed for next week, not backdated.

## Budgets and critical failures

- Latency: mean 1194.12 ms, maximum
  2412 ms, with 11
  traces over the 2,000 ms budget — a breach rate of
  0.0393, under the five-percent A4
  line. The mean alone would have hidden all eleven.
- Cost: 6585.03 cents across the week, a
  mean of 23.52 cents per trace, with
  22 traces over the 30-cent budget —
  the long medication documents of FDE 2.03, priced.
- Critical failures: 3. Three is
  a small number and a large fact: each one is a failure
  that reached outside the ward guidance set, and A3
  needs only one.

## The verdict, rule by rule

- A1 (window drop): fired — the delta of
  -0.0792 is past the minus-five-point line.
- A2 (drift): fired — the share delta of
  0.2854 is past ten points.
- A3 (critical failure): fired — 3
  occurred, and the rule needs one.
- A4 (latency breaches): not fired — the rate of
  0.0393 is under five percent.
- **Verdict: ALERT.** Three of the four pre-agreed
  conditions hold. The report to the ward lead says the
  system is live, useful, and drifting into its weakest
  topic — and that the gate set, not only the model, is
  part of what gets fixed next.

## Certification

- Certified: the weekly report as a runnable artefact
  (the numbers reproduce from the traces without a human
  re-counting), and the alert verdict under the rules as
  written.
- Refused: calling the week healthy on its overall rate,
  attributing the whole late drop to drift without the
  per-topic record, and any retroactive threshold change
  that would turn this week's alert into last week's
  comfort.
