# Worked example — FDE 2.04: three tools exposed on a legacy system, nine withheld, annotated

Referenced by the FDE 2.04 learning session. The customer is
fictional; the pattern is a composite written for this course.
Annotations in brackets name the move being made. This example
uses a different customer from the exercise, on purpose: copy
the moves, not the words.

> **TOOL EXPOSURE NOTE (excerpt) — Larkspur Freight legacy
> booking system**
>
> **The proposal as it arrived.** The integration vendor
> offered the agent project "full MCP coverage" of the booking
> system: fourteen operations, one switch. The list included
> creating and cancelling bookings, editing rates, and issuing
> refunds. Full coverage was presented as a saving — no return
> visits to wire up more tools later.
>
> *[A vendor's coverage list is a sales artefact. It counts
> what the system can do, not what the agent should be able
> to do. The exposure decision belongs to the customer, made
> against the customer's risk — and the price of wiring a
> tool later is a meeting; the price of unwiring one after
> an incident is a postmortem.]*
>
> **The rule the customer chose.** Expose reads over data the
> desk already treats as shared: booking status lookup, dock
> schedule, and the current rate-card check. Three of
> fourteen. Everything that changes state — bookings, rates,
> refunds — stayed human-operated for the pilot, and the one
> read over named customer pricing was withheld with them:
> a read is a disclosure, and pricing by customer name is
> this firm's restricted class, the same call the rate-card
> corpus boundary made in the retrieval work.
>
> *[State the rule before you apply it, in words a review
> meeting can test: kind and data class, both required. A
> rule stated afterwards, around a list somebody already
> liked, is not a rule — it is a caption.]*
>
> **The first month's log.** Of 310 agent calls, 121 were
> denied: 84 for tools never exposed (most of them the agent
> reaching, from wording in a booking email, for the cancel
> operation it did not have), 29 for role, 8 for malformed
> calls. The denial log was the pilot's most useful artefact:
> it showed exactly which capability the desk actually wanted
> next — a supervised cancel flow, proposed as a new decision
> with a human confirmation step, not switched on from the
> vendor's list.
>
> *[Count denials by reason and read them as demand evidence.
> A denial is the system working; a pattern of denials is
> the scoping conversation for the next phase, held with
> evidence instead of enthusiasm.]*

**The lesson:** building agents in customer systems starts
with the withholding decision — the exposed set is what is
left after the rule has refused everything it cannot defend,
and the denial log, not the vendor's coverage list, is what
earns the next tool.
