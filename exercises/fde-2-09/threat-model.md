# Alder Creek Health Network — threat model of the running build

Fictional composite, continued from FDE 2.01 to 2.08. Written
from the engagement's notes for the security and privacy
review of the discharge-support system as it now stands:
the FDE 2.05 eval set, the FDE 2.06 gate, the FDE 2.07
observability build, and the FDE 2.08 prototype, all
running together on the customer's network.

## Where this phase starts

The system works, and that is exactly the problem this
topic exists for. A build that demos well and passes its
eval gate can still leak the data it was trusted with:
identifiers written into the traces that were only meant
to carry timings, a key sitting in a prototype's repo
history, a pasted note that talks the model out of its
own retrieval filter. Before the pilot widens, the ward
lead and the customer's security reviewer ask for one
artefact: a threat model of the running build, and a
hardening plan for its worst findings, inside a fixed
window.

`findings.json` holds the fourteen findings the review
produced. Each finding records its category — pii,
residency, secrets, injection, access, or logging — its
severity and likelihood (each 1 to 5), their product as
the recorded risk, whether a customer action blocks the
fix, the blocker text where one does, and the fix cost
in engineering hours.

## The hardening window (agreed before the review started)

- **Sixteen engineering hours** are available before the
  pilot decision. The window is a budget, not a target:
  hours left over are slack held for the pilot, not a
  reason to widen the fix list past the rules below.
- **Scores were frozen when the findings were filed.**
  Re-scoring a finding after the ranking is known — to
  promote a favourite fix or demote an awkward one — is
  the security form of moving a gate threshold after the
  numbers are in, and it is refused for the same reason
  as in FDE 2.06 and FDE 2.07.

## The fix rules (agreed before the review started)

Applied in this order, exactly as written:

1. **Deferred.** A blocked finding is deferred, however
   high its risk. Its fix waits on the customer action
   named in its blocker text — a contract amendment, an
   identity-team registration — and the plan names that
   action and its owner instead of working around it.
2. **Ranked.** The unblocked findings are ranked by risk
   descending, ties broken by finding id ascending.
3. **Fixed.** The first three findings in the ranking
   are fixed in this window — plus every other unblocked
   finding whose risk equals the third finding's risk.
   A tie at the cut line is fixed, not split: two
   findings the review scored as equally dangerous do
   not become unequal because one id sorts earlier.
4. **Backlog.** Every other unblocked finding is
   backlog: recorded with its risk, owned, and scheduled
   after the pilot decision — not deleted, not quietly
   re-scored down.

## The verdict

- **Hardened for pilot** is a verdict with a rule, not a
  feeling: the fixed findings' hours fit the sixteen-hour
  budget, and no backlog finding carries a risk of 20 or
  more. A verdict of hardened-for-pilot is a statement
  about the top of the ranking only — the residual risk
  (deferred plus backlog) is printed beside it, in the
  open, and the pilot decision is made with that number
  visible.
- Fixing a finding means the fix in its fix note, in
  full — rotating the key and purging the history, not
  one of the two. A half-fix recorded as fixed is the
  finding this exercise is really about.

## Ownership

- The customer's security reviewer owns the severity and
  likelihood scores; the ward lead owns the pilot
  decision; the engagement owns the fixes and the
  honesty of the record.
- Deferred findings leave this exercise with a named
  customer action and owner. A deferral without an owner
  is a backlog item wearing a costume.
