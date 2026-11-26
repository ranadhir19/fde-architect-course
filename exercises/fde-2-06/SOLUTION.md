# FDE 2.06 Reference solution

Released after the attempt window. All counts are of the
files as delivered and are reproduced by the reference
`gate.py`, built exactly to the starter's specification.

## The counts

| Finding | Value |
|---|---|
| records_total | 50 |
| baseline_pass | 30 |
| baseline_fail | 20 |
| baseline_critical_fail | 3 |
| v14_pass | 29 |
| v14_fail | 21 |
| v14_pass_delta | -1 |
| v14_max_category_fail_increase | 2 |
| v14_critical_fail | 5 |
| v14_critical_delta | 2 |
| v14_gate | fail |
| v15_pass | 35 |
| v15_fail | 15 |
| v15_pass_delta | 5 |
| v15_max_category_fail_increase | 0 |
| v15_critical_fail | 3 |
| v15_critical_delta | 0 |
| v15_gate | pass |
| shadow_records | 120 |
| shadow_pass | 102 |
| shadow_pass_rate | 0.85 |
| canary_records | 80 |
| canary_pass | 66 |
| canary_pass_rate | 0.825 |
| canary_critical_fail | 0 |
| canary_worst_block_rate | 0.8 |
| kill_switch_triggered | False |
| promotion_verdict | promote |

## Candidate v1.4: inside tolerance overall, failed twice over

- Overall, v1.4 passes 29 against baseline's 30 — a delta
  of minus one, inside the G1 tolerance. Judged on the
  total alone, this version ships.
- The slices say otherwise. Fabrication failures rise from
  6 to 8 and boundary failures from 3 to 5 — an increase of
  2 in each, against the G2 allowance of 1. The same
  version genuinely improved omission (7 failures down to
  4) and stale guidance (4 down to 3); under the rule as
  written, those improvements buy nothing in the categories
  that got worse.
- The boundary rise is also the critical rise: critical
  failures go from 3 to 5, a delta of plus 2 against the
  G3 allowance of zero.
- **Verdict: FAIL — G2 and G3, each by the same two cases'
  worth of boundary and fabrication failures.** The version
  does not deploy, and the report to the vendor names the
  two categories, not the total.

## Candidate v1.5: the improvement that survives its slices

- v1.5 passes 35, five more than baseline. Category
  failures against baseline: grounded 0 to 0, omission 7
  to 4, fabrication 6 to 5, boundary 3 to 3, stale
  guidance 4 to 3. The largest increase is 0 — no category
  got worse at all.
- Critical failures hold at 3, delta 0, so G3 is met
  exactly, not comfortably: one more boundary failure
  would have failed this version too, and the report
  says so.
- **Verdict: PASS — G1, G2 and G3 all met.**

## Shadow, canary, and the promotion decision

- Shadow: 120 records, 102 passes, a rate of 0.85 — above
  the version's gate rate, as shadow often is, because
  shadow traffic is the whole week's questions, not the
  50 hardest argued-over cases. The report notes the two
  rates are not comparable instruments.
- Canary: 80 records at 5 percent of live traffic, 66
  passes, a rate of 0.825. No critical failure. The four
  blocks of 20 pass 17, 16, 17 and 16 — the worst block
  rate is 0.80, above the 0.70 floor.
- Kill switch: **not triggered** — neither condition met.
- Promotion: gate passed, kill switch silent, and the
  canary rate of 0.825 is within ten points of the shadow
  rate of 0.85. All three conditions met:
  **verdict PROMOTE.**

## Certification

- Certified: the gate as a runnable artefact (the build
  fails on v1.4 without a human in the room), v1.5 for
  promotion from canary to full traffic.
- Refused: deploying v1.4 on its overall score, averaging
  the two candidates' category changes into a portfolio
  argument, and any reading of the canary rate as proof
  the gate set is complete — FDE 2.07 instruments the
  production system precisely because a 50-case gate
  cannot see what live traffic will do next.
