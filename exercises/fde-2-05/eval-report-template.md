# EVAL.md — eval set and calibration report (template)

Hand this to the ward lead. Every number comes from your own
run of `evalset.py` over `cases.json` as delivered.

## The set

- Cases: (total), drawn from (the pilot wards and period).
- Taxonomy counts: grounded (n), omission (n), fabrication
  (n), boundary (n), stale_guidance (n) — and one line on why
  the taxonomy is the customer's, not the vendor's.
- Gold split: pass (n), fail (n). Gold is adjudicated: state
  how disagreements were settled and by whom.

## The human graders

- Agreements (n of total), disagreements (n), agreement rate.
- Kappa, with the computation shown: observed agreement, the
  chance agreement predicted by the two raters' marginal pass
  rates, and the result.
- Verdict against the pre-set 0.80 threshold: does
  adjudication stay in the loop? Name the disagreement cases
  and what training or rubric change they point to.

## The judge

- Accuracy overall (correct n of total).
- False passes (n) and false fails (n), stated separately,
  with the false passes also expressed as a share of the
  gold failures.
- Verdict against the pre-set rule (any false pass ends a
  grade-alone application): grader, triage only, or neither —
  with the false-pass count as the evidence.

## What this set cannot yet say

- One line each: the categories with too few cases to grade
  a change against, and what FDE 2.06's regression gate will
  need that a one-off calibration does not.
