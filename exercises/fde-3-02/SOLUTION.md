# FDE 3.02 Reference solution

Released after the attempt window. All counts are of the
file as delivered and are reproduced by the reference
`controls.py`, built exactly to the starter's specification.

## The counts

| Finding | Value |
|---|---|
| controls_total | 14 |
| satisfied_count | 8 |
| missing_count | 2 |
| stale_count | 2 |
| unowned_count | 2 |
| satisfied_ids | K01, K02, K04, K08, K09, K11, K13, K14 |
| missing_ids | K07, K12 |
| stale_ids | K03, K05 |
| unowned_ids | K06, K10 |
| gate_total | 6 |
| gate_satisfied_count | 4 |
| gate_gap_ids | K05, K07 |
| soc2_total | 11 |
| soc2_satisfied_count | 6 |
| hipaa_total | 11 |
| hipaa_satisfied_count | 7 |
| verdict | not_ready |

## The verdict comes first

- Six controls are go-live gates. Four stand satisfied.
  Two do not, and either one alone decides the verdict:
  the map is **not_ready**, and the landing waits on two
  named pieces of work — not on a general programme of
  improvement.
- The satisfied count is eight of fourteen, and it is
  the least important number on this page. A map that
  led with it would invite exactly the misreading the
  compliance lead banned at the kickoff: a build that
  sounds mostly compliant and is, in the only sense that
  matters, not landable yet.

## The two gate gaps

- **K05, the quarterly access review — stale.** The
  review exists and was signed, 100 days ago, against a
  90-day maximum: it proves the restricted-document
  access list was right last quarter. The closing work
  is one review, re-run and re-signed — days of work,
  not weeks — and until it lands, nobody can say who
  can currently see restricted documents, which is the
  question the gate exists to answer.
- **K07, log retention enforcement — missing.** The
  retention is configured in the trace store; the
  enforcement report the control names as its evidence
  was never produced. This is the exercise's central
  shape: the control is probably operating and is
  nonetheless a gap, because the artefact is the
  evidence and the artefact does not exist. The closing
  work is to run the report against the live store —
  and if the report shows retention is not in fact
  enforced, the gap was worth more than the report.

## The scheduled gaps

- **K03, the TLS scan — stale** at 45 days against a
  30-day maximum, and stale for a reason that matters:
  the scan predates the retrieval service's move to a
  new internal endpoint, so it does not cover the path
  it is cited for. Re-scan after the move; scheduled,
  not gated, because no regulated path is claimed live
  until the landing this map governs.
- **K12, the vulnerability scan — missing.** Licensed
  and configured, never run. A configured scanner is a
  plan, and the map scores it exactly as it scores
  K07: the artefact is the evidence.
- **K06 and K10 — unowned.** The tabletop record (K06)
  names actions but no owner for the incident plan
  itself; the eval gate records (K10) exist for every
  change and belong to nobody. Both artefacts are fresh
  today. Both are already expiring, because freshness
  without an owner is a countdown nobody is watching.
  The closing work is a name, which is why unowned is
  the cheapest gap to close and the most embarrassing
  to be caught with twice.

## The two frameworks read the same build differently

- SOC 2 sees eleven controls, six satisfied — and both
  of its gap lists include the stale access review, so
  its gate is blocked too.
- HIPAA sees eleven controls, seven satisfied — one
  more satisfied than SOC 2, on the strength of the
  training list (K11) and the scoping review (K13) —
  and it is HIPAA that carries the missing gate control
  (K07 is HIPAA-only). The framework with the better
  satisfied count owns the worse gap. Any summary that
  averages the two frameworks into one score hides the
  only fact the landing decision turns on.

## Certification

- Certified: the evidence map as a runnable artefact
  (each status reproduces from the control's recorded
  facts without a human re-arguing a rule), and the
  not-ready verdict under the gate rule as written.
- Refused: softening a gate gap into a scheduled item,
  counting a configured-but-unrun report as evidence,
  treating stale evidence as a pass with an asterisk,
  and any headline that reports eight of fourteen
  without the two gate gaps in the same sentence.
