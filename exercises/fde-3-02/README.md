# FDE 3.02 Exercise — Regulated deployment: map the build's controls to the evidence an auditor can check

**Topic:** Regulated deployment (Layer 6).
**Part (d) of FDE 3.02.**
Attempt this before watching the tutorial half of the lesson.
**Prerequisite:** FDE 3.01 — the build has a topology.
This exercise returns to Alder Creek Health Network, the
Phase 2 build customer, with the question a regulated
landing adds: not "does the control exist?" but "what
artefact proves it, how fresh is the proof, and whose
name is on it?"

## The task

Read `controls-map.md` first. It describes the Alder Creek
discharge-guidance build as it now stands, the fourteen
controls its SOC 2 and HIPAA obligations resolve to, the
evidence artefact named for each control, and the mapping
rules the customer's compliance lead agreed before any
control was scored.

Then build the evidence map the auditor can check without
you:

1. `controls.py`, built from `controls_starter.py`: read
   the fourteen controls in `controls.json`, apply the
   mapping rules exactly as written, and fill the `RESULT`
   dictionary the grader checks. Every value must be
   computed from the file at run time.
2. `EVIDENCE.md` from `evidence-template.md`: the map you
   would hand the compliance lead — every control's status
   with its rule, every gap named as the work it obliges,
   and the go-live verdict with the gate gaps that decide
   it stated before the counts that merely describe it.

The mapping rules, agreed with the customer before you
build:

- **A control is its evidence, not its intention.** A
  control nobody can point to an artefact for is not a
  control that exists; it is a plan. The map scores the
  artefact: present, fresh enough, and owned — or it
  scores the gap.
- **Freshness is part of the claim.** Evidence older than
  its control's maximum age proves the control held once,
  not that it holds. Stale evidence is a gap with a date
  on it, not a pass with an asterisk.
- **An unowned control is an unrun control.** Evidence
  with no named owner has nobody who refreshes it, so its
  freshness is already expiring. Ownership is scored, not
  assumed from the org chart.
- **Gate gaps decide; other gaps schedule.** A gap on a
  go-live gate control stops the landing until it closes.
  A gap anywhere else is scheduled work with a date. The
  verdict reports the gate first — a map that leads with
  "eight of fourteen satisfied" while a gate control has
  no evidence is a map written to be misread.

## Done means

- Every RESULT value is computed from `controls.json` at
  run time — the satisfied, missing, stale and unowned
  counts and sorted id lists, the gate totals and gate
  gap list, the per-framework totals and satisfied
  counts, and the verdict.
- The partitions hold: satisfied plus missing plus stale
  plus unowned is the fourteen controls, and every control
  id appears in exactly one status list.
- The map names, for every gap, the artefact or action
  that closes it — and for a gate gap, the landing
  consequence stated as plainly as the gap itself.
- Graded with `RUBRIC.md`. `SOLUTION.md` is the reference
  answer, released after the attempt window.

## The habit this exercise is really testing

- Regulation reaches an FDE build as a list of artefacts
  with dates and owners, not as a mood of carefulness.
  The professional skill is the mapping: control to
  evidence, evidence to freshness, gap to the decision
  it forces.
- The most dangerous sentence in a regulated deployment
  is "we do that" with no artefact behind it. The map
  exists so that sentence is never the evidence.
