# Alder Creek Health Network — the assistant, the vendor number, the eval design

Fictional composite, continued from FDE 2.01 to 2.04. Written
from the engagement's notes for the evaluation phase of the
discharge-support project.

## Where this phase starts

The discharge-guidance assistant (retrieval from FDE 2.03,
tools scoped in FDE 2.04) answers ward staff questions from
the network's own guidance. The vendor's acceptance report
scores it at 96 percent — on the vendor's generic test set,
built from published discharge literature, graded by the
vendor's own rubric. The ward lead's objection is not that
the number is fabricated. It is that the number is about a
different hospital: none of the vendor's cases involve this
network's checklist order, its superseded guidance versions
still circulating on paper, or its boundary between ward
guidance and patient detail.

So the engagement builds the customer's own eval set first,
before any further feature work. FDE 2.06 turns the set into
a regression gate; this exercise builds the set and certifies
the graders.

## The cases (`cases.json`)

- 50 cases, drawn from the pilot wards' real question shapes
  (rewritten as fictional composites; no patient data). Each
  case carries a staff query, the assistant's candidate
  response as a one-line summary of what it did, and its
  failure-taxonomy category.
- The taxonomy is the customer's, fixed before grading:
  **grounded** (follows current guidance, adds nothing),
  **omission** (a required checklist step missing),
  **fabrication** (a detail no held document supports),
  **boundary** (reaches outside the ward guidance set), and
  **stale_guidance** (follows a superseded version). A case's
  category describes the response's shape; its gold label
  says whether it passes.
- Not every non-grounded response fails, and the set is
  built that way on purpose: a boundary-reaching response
  that refuses and redirects passes; an omission of an
  optional step passes. Category is not verdict — grading
  against the current guidance is.

## The grading

- Two ward reviewers graded all 50 cases independently,
  pass or fail, against the current guidance pack. Neither
  saw the other's grades.
- The 5 cases they disagreed on went to adjudication: the
  ward lead settled each against the guidance text, and
  that settled label is the case's gold label. Gold labels
  for agreed cases are the agreed grade.
- An LLM judge then graded the same 50 cases from the same
  rubric text the humans used, as a candidate for cheap
  grading at scale. Its grades are in the file beside the
  humans', so its calibration can be measured against gold
  before anyone lets it grade alone.

## The thresholds (set before the numbers landed)

- Raters grade without adjudication only at kappa at or
  above 0.80. Below it, adjudication stays in the loop and
  the disagreement cases are training material, not noise.
- The judge may grade alone only if it passes no real
  failure: a single false pass ends that application,
  whatever its overall accuracy. At a false-pass count
  above zero it may still triage — ordering cases for human
  review — where its errors cost time, not correctness.

## Ownership

- The taxonomy and thresholds are owned by the ward lead,
  with the compliance contact holding the boundary category
  definition. Changing either after scores land requires a
  new decision in the engagement log — the same discipline
  as the exposure rule in FDE 2.04, applied to measurement.
