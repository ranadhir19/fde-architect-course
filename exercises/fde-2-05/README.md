# FDE 2.05 Exercise — A 50-case eval set, graded twice, judged once

**Topic:** Evals I — customer-specific eval design (Layer 4).
**Part (d) of FDE 2.05.**
Attempt this before watching the tutorial half of the lesson.
**Prerequisite:** FDE 2.03 and FDE 2.04 — the discharge-guidance
system whose answers this eval set grades, and the permission
boundary its failures must respect.

## The task

Read `eval-design.md` first. It describes the Alder Creek
discharge-guidance assistant as the engagement found it: a
system the vendor scored at 96 percent on the vendor's own
test set, and a ward lead who does not believe the number,
because none of the vendor's cases came from her wards.

Then build the measurement the customer can believe:

1. `evalset.py`, built from `eval_starter.py`: read the 50 graded
   cases in `cases.json` — each with an adjudicated gold label,
   two independent human grades, and one LLM-judge grade — and
   fill the `RESULT` dictionary the grader checks. Every value
   must be computed from the file at run time.
2. `EVAL.md` from `eval-report-template.md`: the report you
   would hand the ward lead — the taxonomy counts, the
   inter-rater numbers with the kappa computation shown, the
   judge's accuracy split into false passes and false fails,
   and the calibration verdict the numbers support.

The design rules, agreed with the customer before you build:

- **The gold label is adjudicated, not voted.** Where the two
  raters disagreed, a third reviewer settled the label against
  the current guidance. Gold is the standard; raters and the
  judge are measured against it, never averaged into it.
- **Agreement is not accuracy.** Two raters can agree at 90
  percent and still leave a kappa below the 0.80 line the
  engagement set for "grade without adjudication" — the report
  shows both numbers and says which one governs.
- **A judge is certified per error direction, not overall.**
  An 84 percent accurate judge that passes a quarter of the
  real failures is a triage tool, not a grader. False passes
  and false fails are reported separately, always.

## Done means

- Every RESULT value is computed from `cases.json` at run
  time — the taxonomy counts, the gold split, the inter-rater
  agreement and kappa, and the judge's two error counts.
- The partitions hold: taxonomy counts sum to 50, gold pass
  plus gold fail is 50, agreements plus disagreements is 50,
  and judge correct plus false pass plus false fail is 50.
- Kappa is computed by the formula in the starter (observed
  agreement corrected for the agreement the two raters'
  marginal pass rates predict by chance), rounded to four
  decimal places — not quoted from a library call whose
  convention you cannot state.
- The report states the calibration verdict the numbers
  support for both instruments: the raters (adjudication
  stays) and the judge (triage only, or grader — with the
  false-pass count as the evidence).
- Graded with `RUBRIC.md`. `SOLUTION.md` is the reference
  answer, released after the attempt window.

## The habit this exercise is really testing

- An eval set is a customer's argument about what failure
  looks like, written as cases. A vendor benchmark measures
  the vendor's argument. The 50 cases here are few, local,
  and argued over — which is exactly why the ward lead can
  act on them.
- Calibration is a verdict with a threshold set in advance.
  Deciding after the numbers land what would have been good
  enough is how a 0.79 becomes "basically 0.80" in a slide.
