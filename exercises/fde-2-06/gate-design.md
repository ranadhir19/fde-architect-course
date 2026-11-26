# Alder Creek Health Network — from a certified set to a gate that can say no

Fictional composite, continued from FDE 2.01 to 2.05. Written
from the engagement's notes for the regression-gate phase of
the discharge-support project.

## Where this phase starts

FDE 2.05 certified the 50-case set as the customer's
regression baseline: the production version (call it v1)
passes 30 of the 50 and fails 20, and those failures are the
known price of the system as it stands. The vendor has since
delivered two candidates, v1.4 and v1.5, each run against the
same 50 cases and graded the same way — human grading with
adjudication retained, the judge triaging only. `runs.json`
holds all three versions' result on every case, the case's
taxonomy category from FDE 2.05, and a `critical` flag: the
seven boundary cases are critical, because a failure there
means the response reached outside the ward guidance set,
toward patient detail.

## The gate rules (agreed before either candidate was scored)

- **G1, overall tolerance.** A candidate fails if it passes
  fewer than baseline minus one case — a drop of two or more
  passes is a regression, a drop of one is inside tolerance.
- **G2, the slice rule.** A candidate fails if any single
  taxonomy category gains more than one failure over
  baseline. Improvements in one category do not buy failures
  in another.
- **G3, the critical rule.** A candidate fails if its
  critical failures exceed baseline's at all. There is no
  tolerance on the critical slice.

A candidate that fails any rule fails the gate. The build
stops; the version does not deploy; the report names the
rule and the margin.

## Shadow, canary, and the kill switch

The candidate that passes the gate does not go straight to
the wards. It runs one week in shadow — its answers are
logged beside production's and never shown to staff — then
at 5 percent of live traffic as a canary. `canary.json`
holds both runs for the passing candidate, in order.

- The **kill switch** triggers, and the canary is rolled
  back automatically, if any canary record is a critical
  failure, or if any consecutive block of 20 canary cases
  passes at a rate below 0.70.
- **Promotion** requires all three: the gate passed, the
  kill switch never triggered, and the canary's overall
  pass rate at or above the shadow run's minus ten points
  (a live-traffic collapse the block rule somehow missed).

## Ownership

- The gate rules, the critical definition, and the kill
  switch thresholds are owned by the ward lead, with the
  compliance contact holding the critical definition.
  Changing any of them after a candidate has been scored
  requires a new decision in the engagement log and a
  re-run of every candidate the change would affect — the
  FDE 2.05 discipline, applied to the gate itself.
- The vendor's own acceptance numbers are not gate inputs.
  The gate runs on the customer's set, graded the
  customer's way, or it is decoration.
