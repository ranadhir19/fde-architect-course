# FDE 2.05 Reference solution

Released after the attempt window. All counts are of the
files as delivered and are reproduced by the reference
`evalset.py`, built exactly to the starter's specification.

## The counts

| Finding | Value |
|---|---|
| cases_total | 50 |
| gold_pass | 30 |
| gold_fail | 20 |
| cat_grounded | 18 |
| cat_omission | 10 |
| cat_fabrication | 8 |
| cat_boundary | 7 |
| cat_stale_guidance | 7 |
| rater_agreements | 45 |
| rater_disagreements | 5 |
| rater_agreement_rate | 0.9 |
| cohens_kappa | 0.7967 |
| judge_correct | 42 |
| judge_accuracy | 0.84 |
| judge_false_pass | 5 |
| judge_false_fail | 3 |

## Where the gold failures live

- **Grounded: 0 of 18 fail.** The taxonomy's clean class is
  clean — the set's control group behaves like one.
- **Omission: 7 of 10 fail; fabrication: 6 of 8 fail.** These
  two categories carry 13 of the 20 failures: the assistant's
  real weaknesses are leaving steps out and adding details
  in, in that order.
- **Boundary: 3 of 7 fail; stale guidance: 4 of 7 fail.** The
  other boundary and stale cases pass — they refuse and
  redirect, or follow the current version after all. Category
  is the shape of the attempt, never the verdict.

## The raters: 90 percent agreement, kappa 0.7967

- The raters agree on 45 of 50 cases. The 5 disagreements —
  C03, C36, C41, C44, C48 — were adjudicated by the ward lead
  against the current guidance, and those settled labels are
  gold.
- Kappa corrects the 0.90 for chance: rater A passed 30 of
  50 and rater B passed 27 of 50, so their marginals alone
  predict agreement of 0.508, and kappa lands at 0.7967.
- **The verdict applies the threshold as set: 0.7967 is
  below 0.80, so adjudication stays.** The honest sentence
  is "strong agreement, adjudication retained" — not
  "basically 0.80". The disagreement cases go into rubric
  training for the next grading round; that is what they
  are for.

## The judge: 84 percent accurate, and not a grader

- The judge matches gold on 42 of 50. Split by direction,
  the 8 errors are 5 false passes and 3 false fails.
- The 5 false passes are a quarter of the 20 gold failures:
  one failure in four would have shipped under judge-only
  grading. Under the pre-set rule — any false pass ends a
  grade-alone application — **the judge is certified for
  triage only**: it may order cases for human review, where
  its false fails cost reviewer time and its false passes
  are still caught, because a human grades every case that
  matters.
- The 3 false fails are not harmless either; they are the
  price of triage, paid in reviewer attention, and the
  report states them so the ward lead can price the judge's
  help honestly.

## Certification

- Certified: the 50-case set as the customer's regression
  baseline (FDE 2.06 builds the gate on it), human grading
  with adjudication retained, the judge as triage only.
- Refused: judge-only grading, dropping adjudication on the
  strength of the raw agreement rate, and any use of the
  vendor's 96 percent figure for this system — it was
  measured on a different customer's argument about failure.
