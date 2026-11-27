# FDE 2.09 Reference solution

Released after the attempt window. All counts are of the
file as delivered and are reproduced by the reference
`security.py`, built exactly to the starter's specification.

## The counts

| Finding | Value |
|---|---|
| findings_total | 14 |
| risk_total | 196 |
| blocked_count | 2 |
| deferred_count | 2 |
| deferred_ids | F05, F06 |
| deferred_risk | 28 |
| fixed_count | 4 |
| fixed_ids | F01, F02, F03, F12 |
| fixed_hours | 14 |
| fix_budget_hours | 16 |
| slack_hours | 2 |
| fixed_risk | 85 |
| risk_reduction | 0.4337 |
| backlog_count | 8 |
| backlog_ids | F04, F07, F08, F09, F10, F11, F13, F14 |
| backlog_risk | 83 |
| residual_risk | 111 |
| max_residual_unblocked_risk | 16 |
| pii_count | 3 |
| secrets_count | 3 |
| injection_count | 3 |
| residency_count | 2 |
| hardened | True |
| verdict | hardened_for_pilot |

## The ranking, read through its rules

- Fourteen findings carry 196 points of risk between
  them: three each in pii, secrets and injection, two
  in residency, two in access, one in logging.
- Ranked by risk, the unblocked findings run: the
  identifier-logging traces (F03, risk 25) first, then
  a three-way tie at 20 — the committed API key (F01),
  the pasted-note injection (F02), and the
  unauthenticated prototype endpoints (F12).

## The tie is the exercise

- The fix rule names the top three — and the third seat
  sits inside the tie at 20. Splitting the tie by id
  would have fixed F01 and F02 and left F12, the
  finding with the joint-highest likelihood in the
  file, open on a sort order. The tie rule fixes all
  four findings: 85 points of risk, a reduction of
  0.4337, in 14 of the 16 hours.
- Each fix is its note in full: the key is rotated and
  purged from the repo history; pasted text is demoted
  to data with injection cases added to the FDE 2.05
  gate; identifiers are redacted before the trace write
  and the stored traces purged; every prototype
  endpoint goes behind the interim per-user token check
  — which is a bridge to F06's real fix, not a
  substitute for it, and the plan says so.

## Deferred is a customer action, not a shrug

- Two findings are blocked, carrying 28 points of risk:
  the sub-processor's ninety-day prompt retention
  (F05), which waits on a contract amendment the
  customer's procurement team owns, and the shared ward
  login (F06), which waits on the customer's identity
  team issuing the IdP registration. F06 is the
  FDE 2.08 faked single sign-on, still unfaked — the
  prototype's label said the real thing was owed, and
  this review is where the debt comes due.
- Neither is fixed by working around it. The interim
  token check under F12 narrows F06's exposure; it does
  not close the finding, and F06 stays deferred in the
  record until the IdP lands.

## The backlog, and the number beside the verdict

- Eight findings remain in the backlog with 83 points
  of risk: the out-of-zone eval copy (F04, 16) heads
  it, then the cross-patient retrieval injection
  (F07, 15), the laptop env file and the unreviewed
  feedback text (F08 and F11, 12 each), the editable
  audit log and the unvalidated tool arguments (F09
  and F13, 9 each), the cross-region backups (F10, 6)
  and the copied fixtures (F14, 4). The highest backlog
  risk is 16 — below the verdict's line of 20, and
  printed, not buried.
- Total residual risk is 111 of the original 196. The
  verdict below is a statement about the top of the
  ranking, made with that 111 on the page.

## The verdict, rule by rule

- Fix hours: 14, inside the sixteen-hour budget,
  with 2 hours of slack held for the pilot.
- Highest backlog risk: 16, below 20.
- **Verdict: hardened_for_pilot.** Hardened for the
  pilot as scoped — not secure in general, and the
  plan never confuses the two. The deferred pair and
  the 83-point backlog are the price of the pilot,
  named in advance, with owners.

## Certification

- Certified: the hardening plan as a runnable artefact
  (the selection reproduces from the findings without
  a human re-arguing the ranking), and the
  hardened-for-pilot verdict under the rules as written.
- Refused: splitting the tie at the cut line, fixing a
  blocked finding by substitution, re-scoring any
  finding after the ranking was known, and any claim
  that the verdict retires the residual 111 points.
