# FDE 2.01 Exercise — Audit the data before anyone builds a model on it

**Topic:** Data before models (Layer 3). **Part (d) of FDE 2.01.**
Attempt this before watching the tutorial half of the lesson.
**Prerequisite:** Phase 1 complete — in particular the Capstone 1
decision-log discipline (FDE 1.08). This exercise opens Phase 2
and the Capstone 2 engagement.

## The task

Read `data-reality.md` first. It describes the Alder Creek Health
Network (a fictional composite, and the Capstone 2 customer) as
its data actually is: who owns each source, who can grant access
to it, which document runs the ward, and where the written policy
and the lived reality disagree.

Then audit `discharges.csv` — 600 synthetic discharge records,
the exact extract the network's IT team would hand you on day
one. The file looks clean. It is not. It contains exact
duplicates filed under new ids, silent nulls wearing four
different costumes, a date format that changes partway down the
file, a diagnosis code that loses its dot partway down the file,
and two vocabularies (status, ward) that spell the same thing
several ways.

Produce two artefacts:

1. `audit.py`, built from `audit_starter.py`: a small program
   that computes the audit counts from the file itself — never
   typed in by hand — and fills the `FINDINGS` dictionary the
   grader checks. If a number in your report cannot be
   reproduced by running your program, it does not belong in
   the report.
2. `AUDIT.md` from `audit-report-template.md`: the data-audit
   report you would hand the customer before any build starts.
   Every count from your program, each defect classified as
   *blocks the build*, *shapes the build*, or *cosmetic*, the
   access and ownership findings from `data-reality.md`, and
   the one source you refuse to build on until its owner answers
   a named question.

## Done means

- Every count in `FINDINGS` is computed, and the counts are the
  counts of the file as delivered — duplicates included. An
  audit that silently de-duplicates before counting has hidden
  the first defect it was hired to find.
- Both drift points are located by row, not described as
  "somewhere in the middle": the first row whose admit date is
  not in ISO format, and the first row whose diagnosis code has
  lost its dot.
- Silent nulls are counted as one class with its tokens named.
  A column that is never empty can still be full of nulls.
- The report separates what the file proves from what
  `data-reality.md` claims, and flags every place the two
  disagree.
- Graded with `RUBRIC.md`. `SOLUTION.md` is the reference
  answer, released after the attempt window.

## The habit this exercise is really testing

- Data before models is not a slogan about cleanliness. It is
  the discipline of refusing to let a model's first failure be
  a defect a two-hour audit would have caught on day one.
- Ownership is a data property. A field nobody owns will drift
  again the week after you clean it; the audit names the owner
  or names the vacancy.
