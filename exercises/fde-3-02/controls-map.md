# Alder Creek Health Network — the build, its controls, and the evidence each one stands on

Fictional composite, returning from Phase 2. Alder Creek's
discharge-guidance build — retrieval over ward guidance
(FDE 2.03), permission-scoped tools (2.04), a customer eval
set and gate (2.05, 2.06), production traces (2.07) and a
threat model with its top findings fixed (2.09) — is ready
to land in the topology FDE 3.01's rules chose for it.
Alder Creek is a health network: the build touches
discharge guidance and restricted worked examples carrying
patient references, so two frameworks govern the landing —
SOC 2 (the trust-services criteria its enterprise
customers and auditors ask for) and HIPAA (the health-data
rules its own compliance office answers to).

The compliance lead's position, stated at the kickoff and
recorded here because the exercise grades against it:
"Do not bring me a list of controls. Bring me, for each
control, the artefact that proves it, the date on the
artefact, and the person who owns refreshing it. Where
one of those three is missing, bring me the gap instead —
named, not softened."

`controls.json` holds the fourteen controls the two
frameworks resolve to for this build. Each records the
frameworks it serves, the evidence artefact named for it,
whether that artefact exists today, its age in days where
it exists, the maximum age the control allows, the named
owner (blank where nobody has been named), whether it is
a go-live gate control, and a note from the mapping
workshop.

## The mapping rules (agreed before any control was scored)

Applied per control, exactly as written, in this order —
the first failing check is the control's status:

1. **Missing.** The evidence artefact does not exist.
   There is nothing to check, so nothing later in the
   list can rescue the control.
2. **Stale.** The artefact exists but its age in days is
   greater than the control's maximum evidence age. It
   proves the control held at that date; it does not
   prove the control holds now.
3. **Unowned.** The artefact exists and is fresh, but no
   owner is named. Nobody refreshes unowned evidence, so
   the control is running on borrowed time.
4. **Satisfied.** The artefact exists, is within its
   maximum age, and has a named owner.

A control tagged for both frameworks counts toward both
frameworks' totals, with the same status in each. The
per-framework satisfied count is the number of that
framework's controls whose status is satisfied.

## The gate and the verdict

Six of the fourteen controls are marked as go-live gate
controls: the landing may not proceed while any of them
is in a gap status. One verdict for the map, by rule:

- **ready** — every control is satisfied.
- **ready_with_scheduled_gaps** — gaps exist, and none of
  them is on a gate control. The landing proceeds; the
  gaps are scheduled work with owners and dates.
- **not_ready** — at least one gate control is in a gap
  status. The honest outputs are the named gate gaps and
  the work that closes each — never a satisfied-count
  headline that lets a reader believe the landing is a
  scheduling question.

## Ownership

- Alder Creek's compliance lead owns the framework calls
  recorded in `controls.json`; the engagement owns the
  mapping and the honesty of the verdict.
- A status is a claim about an artefact as recorded. If
  the workshop recorded an artefact's age or owner wrong,
  the fix is to correct the file and recompute — never to
  adjust a status by hand until the map looks landable.
