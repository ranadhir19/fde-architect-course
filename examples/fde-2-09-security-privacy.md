# Worked example — FDE 2.09: the tie that would have left the door open, annotated

Referenced by the FDE 2.09 learning session. The customer is
fictional; the pattern is a composite written for this course.
Annotations in brackets name the move being made. This example
uses a different customer from the exercise, on purpose: copy
the moves, not the words.

> **HARDENING PLAN (excerpt) — Larkspur Freight
> quote-desk build, pre-pilot security review**
>
> **The worst finding was the dullest one.** The review's
> top score was not an exotic injection. It was the quote
> desk's debug logging, switched on during a latency hunt
> and never switched off, writing full customer rate cards
> into a log file the whole support team could read. It
> was fixed by deleting the payload from the log line and
> purging the stored logs — both halves, because a redacted
> future beside an unpurged past is a finding wearing a
> fix's clothes.
>
> *[In a running build, exposure is usually a leftover —
> a debug flag, a prototype key, a stand-in login — not an
> attacker's invention.]*
>
> **The tie at the cut line.** Three findings scored 20.
> The window's rule fixed the top three, ties whole, so
> all three were fixed: the rate-card logging, a carrier
> API key in a shared drive, and a rate-card document that
> could instruct the drafting model to quote below the
> floor rate. Splitting the tie by id would have left the
> injection open because its id sorted last — a sort order
> deciding a security posture, which the reviewer refused
> in one sentence.
>
> *[A tie-break orders work. It must never be allowed to
> decide which of two equally dangerous findings counts
> as dangerous.]*
>
> **Deferred, with an owner.** The sub-processor's log
> retention sat outside the engagement's power to change:
> it waited on a contract amendment, and the plan named
> the amendment, the procurement owner, and the date it
> would be chased. Nobody built a workaround and called
> the finding closed; the interim step — routing the
> desk's traffic away from that sub-processor — was
> recorded as a mitigation, in those words.
>
> *[A deferral with a named action and owner is a plan.
> A deferral without them is a hope, filed.]*
>
> **The number beside the verdict.** The plan's verdict
> was hardened for pilot, and printed directly under it
> was the residual: 96 points of risk still open, the
> highest single backlog item at 15. The desk lead signed
> the pilot with that number on the page — which is what
> made the signature worth having when, six weeks later,
> the backlog's top item fired and the record showed it
> had been seen, priced, and owned in advance.
>
> *[A verdict that hides its residual buys a quiet week
> and an expensive meeting later.]*

**The lesson:** security while building is a ranking with
owners and a printed residual — fix the top whole, defer
only behind a named customer action, and never let a
verdict say more than its rules earned.
