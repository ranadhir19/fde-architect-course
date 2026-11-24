# FDE 1.07 Exercise — Timed treasure hunt in a foreign codebase

**Topic:** Engineering fluency for deployment (Layer 0). **Part (d) of FDE 1.07.**
Attempt this before watching the tutorial half of the lesson.

## The task

Read `hunt-brief.md`, then work only in `foreign_codebase/` — a small
returns-triage service a previous contractor left at Cedarbrook Home
Goods (the fictional Capstone 1 customer). You have never seen this
code. That is the point: an FDE's first engineering job on site is
rarely writing new code; it is reading someone else's, fast, in an
environment you do not control, and answering three questions under
time pressure:

1. **The bug** — why are urgent returns tickets not reaching the
   urgent queue? Name the file, the line-level cause, and the
   evidence that proves it (not a guess about what looks odd).
2. **The config** — where is the service's configuration decided,
   which environment variable overrides the ticket data path, and
   what is the retry limit the code will actually use?
3. **The data path** — trace one ticket from the file on disk to
   the queue it lands in: every function it passes through, in
   order, with the file each function lives in.

Work to the timebox in the brief: 45 minutes. Record where you were
at 45 minutes even if you finish early — the timebox is part of
the exercise, because on site the meeting is at a fixed time
whether your reading is finished or not.

Write your answers in `hunt.py`, copied from `hunt_starter.py`,
and your working notes in `hunt-report.md` from
`hunt-report-template.md`. Run the structural grader with
`python -m pytest test_hunt.py -q`.

## Done means

- The bug answer names a cause the code proves, with the two
  mismatched values quoted from the two files that disagree.
- The config answer names the deciding file and the exact
  environment variable — not "environment variables are used".
- The data path has no gaps: a reader could follow your trace
  from the CSV row to the queue name without opening the code.
- The hunt report states what you read first, what you skipped,
  and what you would read next with another hour. Fluency is
  triage, and the triage is graded too.
- Graded with `RUBRIC.md`. `SOLUTION.md` is the reference answer,
  released after the attempt window.

## Production habits this exercise is really testing

- Read the entry point first, then follow the data — never read
  a foreign codebase alphabetically or top to bottom.
- Form a hypothesis from the symptom, then go and prove or kill
  it in the code. Do not fix anything during the hunt: the
  deliverable is the diagnosis, and an unproven fix in a
  customer's system is how deployments break on day one.
- Write the trace down as you go. Memory of code you read once,
  in a building you arrived in yesterday, is not a plan.
