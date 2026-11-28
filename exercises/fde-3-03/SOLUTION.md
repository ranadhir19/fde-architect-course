# FDE 3.03 Reference solution

Released after the attempt window. All counts are of the
file as delivered and are reproduced by the reference
`review.py`, built exactly to the starter's specification.

## The counts

| Finding | Value |
|---|---|
| questions_total | 16 |
| supported_count | 8 |
| partial_count | 3 |
| stale_count | 2 |
| unsupported_count | 3 |
| supported_ids | Q01, Q02, Q05, Q07, Q10, Q12, Q14, Q15 |
| partial_ids | Q03, Q08, Q13 |
| stale_ids | Q04, Q09 |
| unsupported_ids | Q06, Q11, Q16 |
| gate_total | 6 |
| gate_supported_count | 3 |
| gate_gap_ids | Q04, Q11, Q16 |
| overclaim_count | 4 |
| overclaim_ids | Q04, Q06, Q11, Q16 |
| sections_count | 7 |
| verdict | blocked |

## The verdict comes first

- Six questions are review-blocking gates. Three stand
  supported. Three do not, and any one of them alone
  decides the verdict: the return is **blocked**, and
  it stays blocked until each gate answer can be
  returned at the strength its artefact supports — or
  returned honestly as a gap the customer accepts in
  writing.
- The supported count is eight of sixteen, and it is
  the least important number on this page. A return
  that led with it would invite exactly the misreading
  the reviewer banned on the kickoff call: a build that
  sounds half-passing, when the only question that
  matters — can this return be submitted as a pass —
  has a one-word answer, and the word is no.

## The three gate gaps

- **Q04, the sub-processor register — stale, and an
  overclaim.** The register is 130 days old against a
  90-day maximum, and it predates two changes it exists
  to record: the retrieval service's endpoint move and
  a replacement transcription sub-processor. The draft
  said "yes". The closing work is to rebuild the
  register from the current architecture and contracts
  and have it re-approved — and the stale register is
  also why Q13's contract answer is only partial: the
  replacement party was onboarded ahead of its
  countersigned amendment.
- **Q11, the regulated-data tabletop — unsupported,
  and an overclaim.** A tabletop was run, and its
  record is real — for a service-outage scenario. The
  question asks about regulated data, no such exercise
  record exists, and the incident plan the exercise
  would test still has no named owner (the same blank
  FDE 3.02 recorded against K06). The closing work is
  an owner, then the exercise, then the record — in
  that order.
- **Q16, the failover exercise — unsupported, and an
  overclaim.** Failover is designed, documented, and
  untested: scheduled twice, postponed twice, no
  exercise record. The draft's "yes" confused a design
  with a result. The closing work is the exercise
  itself, run and recorded with timings.

## The overclaim that is not a gate

- **Q06, deletion verification — unsupported.** The
  draft said "yes" because retention is configured.
  Configuration is not verification: no deletion report
  has ever been run, and backup deletion has never been
  tested at all. This is FDE 3.02's K07 lesson arriving
  in questionnaire form — the artefact is the evidence,
  and here there is no artefact. Not a gate question,
  so it does not block the return; left uncorrected, it
  would still be the answer the reviewer checks first,
  because it is the easiest one on the page to test.

## The honest qualifications

- **Q03, service accounts — partial.** The inventory
  covers the team's two services and not the vendor
  gateway's accounts. The qualified answer names both
  halves; the closing work is the vendor's inventory,
  obtained or the question stays qualified.
- **Q08, logs free of identifiers — partial.** The
  scrubbing check covers retrieval traces; eval-service
  logs have not been re-checked since the FDE 2.09
  F03 fix. A fresh check is days of work, and until it
  lands the answer covers one service, not the build.
- **Q13, third-party contracts — partial**, for the
  reason Q04 records: one party onboarded ahead of
  its countersigned amendment. The closing work is
  the signature, not a better sentence.
- **Q09, vulnerability scanning — stale, drafted
  honestly as "qualified".** The scanner ran once,
  75 days ago, against a monthly claim. The draft
  conceded the limit, so it is not an overclaim; the
  closing work is a cadence that holds, evidenced by
  the next two monthly reports, not by a promise.

## What the supported eight are worth

- The eight supported answers are not filler around
  the gaps. Each names an artefact the reviewer can
  open in the room — including two that were gaps in
  earlier topics and closed properly: the re-run
  access review (Q02, closing FDE 3.02's stale K05)
  and the region export showing the out-of-zone eval
  copy moved (Q14, closing FDE 2.09's F04). A review
  pack that shows its closed gaps beside its open
  ones gives the reviewer a reason to believe the
  open ones will close too. That belief, earned with
  artefacts, is what surviving a security review
  actually consists of.

## Certification

- Certified: the review pack as a runnable artefact
  (each status reproduces from the question's
  recorded facts without a human re-arguing a rule),
  the four overclaims corrected in place, and the
  blocked verdict under the gate rule as written.
- Refused: submitting the draft as written, softening
  a gate gap into a qualification, counting a design
  or a configuration as a tested result, and any
  headline that reports eight of sixteen without the
  three gate gaps in the same sentence.
