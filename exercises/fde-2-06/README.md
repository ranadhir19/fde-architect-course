# FDE 2.06 Exercise — Wire the gate: a bad version must fail the build

**Topic:** Evals II — gates and regression (Layer 5).
**Part (d) of FDE 2.06.**
Attempt this before watching the tutorial half of the lesson.
**Prerequisite:** FDE 2.05 — the 50-case Alder Creek eval set,
its taxonomy, and its adjudicated gold labels. This exercise
runs new versions of the same system against that same set.

## The task

Read `gate-design.md` first. It describes where the
engagement stands: the FDE 2.05 set is certified as the
regression baseline, the vendor has delivered two candidate
versions, and the gate rules were agreed with the ward lead
before either candidate was scored.

Then build the gate the customer can run without you:

1. `gate.py`, built from `gate_starter.py`: read the three
   versions' results on the 50 gold cases in `runs.json` and
   the shadow and canary records in `canary.json`, and fill
   the `RESULT` dictionary the grader checks. Every value
   must be computed from the files at run time.
2. `GATE.md` from `gate-report-template.md`: the report you
   would hand the ward lead — each candidate's verdict with
   the rule that decided it, and the promotion verdict for
   the candidate that passed, with the kill-switch evidence.

The design rules, agreed with the customer before you build:

- **The gate judges slices, not only totals.** A candidate
  whose overall score sits inside the agreed tolerance can
  still fail: no taxonomy category may gain more than one
  failure over baseline, and critical failures may not
  increase at all.
- **The rules are applied as written, in order.** Overall
  tolerance, then the slice rule, then the critical rule.
  A candidate that fails any rule fails the gate, and the
  report names the rule — "the numbers looked fine overall"
  is not a verdict.
- **Promotion is a second decision, not the gate repeated.**
  The passing candidate earns a shadow run and a 5 percent
  canary. It promotes only if the kill switch never triggers:
  no canary critical failure, and no block of 20 canary cases
  below the agreed pass-rate floor.

## Done means

- Every RESULT value is computed from `runs.json` and
  `canary.json` at run time — the per-version pass and fail
  counts, the largest category failure increase for each
  candidate, the critical failure counts and deltas, both
  gate verdicts, the shadow and canary rates, the worst
  canary block rate, the kill-switch state, and the
  promotion verdict.
- The partitions hold: for each version, pass plus fail is
  50; shadow plus canary records is 200.
- The gate verdicts follow from the three rules in
  `gate-design.md` applied to the computed counts — a
  verdict typed in to match the expected answer, with the
  counts computed some other way, is not a gate.
- The report states, for the failed candidate, which rule
  or rules it failed and by how much — not merely that it
  failed.
- Graded with `RUBRIC.md`. `SOLUTION.md` is the reference
  answer, released after the attempt window.

## The habit this exercise is really testing

- A regression gate exists so that a worse version fails
  while its champion is out of the room. If the verdict
  needs a meeting, it is not a gate.
- An overall score is an average over slices that do not
  matter equally. The failures a gate exists to catch are
  the ones the average hides: a category quietly doubling
  its failures while the total moves by one case.
