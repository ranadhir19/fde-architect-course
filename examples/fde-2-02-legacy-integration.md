# Worked example — FDE 2.02: the Oracle system with no API, integrated anyway, annotated

Referenced by the FDE 2.02 learning session. The customer is
fictional; the pattern is a composite written for this course.
Annotations in brackets name the move being made. This example
uses a different customer from the exercise, on purpose: copy
the moves, not the words.

> **INTEGRATION NOTE (excerpt) — Larkspur Freight depot system**
>
> **The constraint.** The depot system is an on-premise Oracle
> install whose vendor contract forbids direct database writes
> and offers no API at any price the customer will pay this
> year. The integration surface we negotiated instead: a nightly
> export the system already produces for its own reporting,
> written to a folder we control, plus a read-only database
> view for the one lookup the export cannot answer.
>
> *[No-API does not mean no integration. It means the interface
> is a file, a schedule, and a person who knows where both
> live. The engineering is the same; the failure modes move
> from HTTP status codes to silence — a file that simply does
> not arrive — so the pipeline alarms on absence first.]*
>
> **The reconciliation.** Every morning the export is joined
> against the dispatch ledger. On the first morning: 1,204
> export rows, 1,187 ledger jobs, 31 breaks in three classes —
> 14 jobs in the ledger with no export row (all traced to one
> depot whose export job had been paused for a holiday nobody
> logged), 11 export rows with no ledger job (test jobs from a
> training week, identifiable and now excluded by a named rule),
> and 6 weight mismatches, every one a kilograms-to-pounds
> boundary at the partner depot.
>
> *[Three classes, three owners, three different fixes — and
> none of them is "clean the data". The paused job is an
> operations fix, the test jobs are a rule, and the unit
> boundary is a conversion owned by the partner. A single
> "data quality issue" line would have hidden all three.]*
>
> **Idempotency, learned once.** In week two the export arrived
> twice — the folder sync retried after a network drop. Because
> ingestion keys on the job id and the run writes a manifest of
> what it consumed, the second arrival changed nothing and the
> morning report said so in one line. The incident review took
> four minutes.
>
> *[Design for the retry on day one. File-based integrations do
> not fail with an error you can catch; they fail by arriving
> twice, late, or not at all. All three are normal events with
> a designed answer, or production incidents without one.]*

**The lesson:** the pattern generalises — file drop plus
reconciliation plus an alarm on absence is a complete
integration strategy for a system that will never have an API.
What makes it production-grade is not the parser; it is the
break classes, the named owners, and the refusal to let a
silent night pass as a successful one.
