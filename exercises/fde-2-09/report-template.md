# HARDENING.md — the running build's hardening plan (template)

Hand this to the customer's security reviewer before the
pilot decision. Every number comes from your own run of
`security.py` over `findings.json` as delivered.

## The review in one line

- Findings (n), total risk (n). Fixed (n) findings
  carrying risk (n) — a reduction as a share of the
  total. Verdict: hardened for pilot or not, by the
  stated rule, with the residual risk printed beside it.

## Fixed in this window

- Each fixed finding: its id, its risk, its fix hours,
  and the fix as its fix note states it, in full. Where
  a fix bridges a deferred finding, say so and name the
  deferred finding it bridges.

## Deferred, with the unblocking action

- Each deferred finding: its id, its risk, its blocker
  text, the customer action that unblocks it, and the
  owner of that action. Interim mitigations, labelled
  as mitigations.

## The backlog

- Each backlog finding: its id, its risk, and the one
  line that schedules it after the pilot decision.
- The highest backlog risk, stated on its own line.

## The window

- Fix hours, the sixteen-hour budget, and the slack.
  What the slack is held for.

## The residual risk

- Deferred risk, backlog risk, and the total residual,
  printed beside the verdict — and one line on what
  the verdict does not claim.
