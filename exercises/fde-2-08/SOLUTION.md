# FDE 2.08 Reference solution

Released after the attempt window. All counts are of the
file as delivered and are reproduced by the reference
`prototype.py`, built exactly to the starter's specification.

## The counts

| Finding | Value |
|---|---|
| requests_total | 12 |
| value_total | 41 |
| blocked_count | 2 |
| deferred_count | 3 |
| deferred_ids | R03, R06, R12 |
| fake_count | 3 |
| fake_ids | R02, R05, R10 |
| fake_hours | 3 |
| real_count | 4 |
| real_ids | R01, R04, R07, R09 |
| real_hours | 10 |
| cut_count | 2 |
| cut_ids | R08, R11 |
| prototype_items | 7 |
| prototype_hours | 13 |
| timebox_hours | 16 |
| slack_hours | 3 |
| prototype_value | 24 |
| value_coverage | 0.5854 |
| harden_count | 5 |
| harden_ids | R01, R02, R05, R09, R10 |
| demo_ready | True |
| verdict | demo_ready |

## The sprint, read through its rules

- The room asked for twelve features worth 41 demo
  points. The prototype carries seven of them, worth
  24 points — a coverage of 0.5854 — in
  13 of the sixteen hours, with
  3 hours of slack held for rehearsal
  and one failure.
- Ranked for real building, the queue ran: feedback
  thumbs (R07, value 2 in 1 hour), PDF export (R04,
  3 in 2), the night-shift handoff summary (R09, 4 in
  3), and the discharge brief itself (R01, 5 in 4) —
  10 hours in total. The multilingual brief
  (R11, 5 hours) and voice input (R08, 4 hours) were
  each tried in their turn and neither fit the 13
  hours left after faking; both are cut, by the rule,
  not by preference.

## Deferred is a decision, not a delay tactic

- The live bed-board integration (R03) and offline
  ward mode (R12) are blocked — 2 requests
  whose dependencies sit outside the sprint. Their
  combined 9 demo points are the price of honesty
  about what a weekend cannot move.
- The patient reference redaction check (R06) is the
  sprint's sharpest call: worth 5 points, the joint
  highest score in the file, and deferred anyway —
  safety-critical, not fakeable, and therefore not
  buildable for real inside a demo timebox. A sprint
  that rushes exactly this feature has misunderstood
  what the timebox is for.

## Faked, labelled, and worth less than they look

- Three safety-critical features are faked at one hour
  each: the medication guardrail banner (R02), single
  sign-on (R05), and the audit log viewer (R10). The
  demo shows their placement and shape; it proves
  nothing about their behaviour under real data, real
  credentials, or a real audit — and the demo script
  says so while they are on screen.
- Their 10 demo points count toward demo-readiness
  because the ward lead's question — is a brief worth
  attention at handover — can be judged with the
  safety surfaces visible but stubbed. They would not
  count toward a production decision, and the plan
  does not ask them to.

## The harden list is the real deliverable

- Five of the seven prototype items leave named
  production work behind: R01, R02, R05, R09, R10.
  The faked three carry the heaviest notes — real
  banner logic with its eval, real authentication,
  a tamper-evident audit trail — and the built brief
  and handoff summary carry their corpus and wording
  reviews.
- The prototype code itself is throwaway by
  declaration. If the Monday verdict is to proceed,
  production starts from the harden list and the
  FDE 2.03 to 2.07 artefacts, not from the sprint's
  shortcuts.

## The verdict, rule by rule

- Value carried: 24, at or above the
  pre-agreed line of 20.
- Hours used: 13, inside the sixteen-hour
  timebox.
- **Verdict: demo_ready.** Ready means the demo can
  answer its stated question on Monday — not that the
  system is ready, and the plan never confuses the two.

## Certification

- Certified: the sprint plan as a runnable artefact
  (the selection reproduces from the requests without
  a human re-arguing it), and the demo-ready verdict
  under the rules as written.
- Refused: building the redaction check to chase its
  five points, presenting any fake without its label,
  and any claim that demo-ready shortens the production
  work named on the harden list.
