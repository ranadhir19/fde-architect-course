# Worked example — FDE 2.03: retrieval over one customer's documents, measured before it was believed, annotated

Referenced by the FDE 2.03 learning session. The customer is
fictional; the pattern is a composite written for this course.
Annotations in brackets name the move being made. This example
uses a different customer from the exercise, on purpose: copy
the moves, not the words.

> **RETRIEVAL NOTE (excerpt) — Larkspur Freight rate-card lookup**
>
> **The corpus as it actually was.** The sales desk wanted
> retrieval over "the rate cards". The corpus turned out to be
> 214 documents: current rate cards, three years of superseded
> cards still in the same folder, and a folder of quoted-rate
> emails containing named customer pricing. Nobody had lied;
> nobody had ever drawn the boundary. The first build decision
> was the corpus boundary, not the model: current cards only,
> superseded cards excluded by their own effective dates, and
> the quoted-rate emails excluded entirely — named customer
> pricing is this customer's restricted class.
>
> *[Every retrieval system has a guardrail, whether or not
> anyone wrote it down. The only choice is whether the boundary
> is a decision with a name on it, or an accident of which
> folder the export happened to point at.]*
>
> **The measurement.** Forty staff queries with gold sets agreed
> by the desk lead. First run, no exclusions: recall at 5 of
> 0.93 — and 11 of the 40 queries returning a superseded card or
> a pricing email in the top 5. The recall number was quoted in
> the project update that week. The leak count was not, because
> nobody had thought to count it. Both numbers are in every
> report since.
>
> *[A metric suite is a list of the failures you have decided
> to be able to see. Recall sees missed documents. Only a leak
> count sees returned documents that should never have been
> returnable — and in a customer system, that is usually the
> failure with a name and a contract attached.]*
>
> **After the boundary.** With the exclusions applied at index
> time, recall at 5 was 0.95 and the leak count was zero, on
> the same 40 queries, re-run unchanged. The two missed gold
> documents were both cards whose titles used a depot nickname
> the queries did not — recorded as a vocabulary gap for the
> customer to fix in the source titles, not tuned around.
>
> *[When the measurement and the target disagree, the honest
> moves are fix the corpus or re-open the scope — never edit
> the gold set. The gold set is the customer's statement of
> what correct means; tuning it to pass is grading your own
> homework.]*

**The lesson:** build for one customer means the corpus
boundary, the guardrail, and the gold set are all customer
decisions with names on them — and the report carries the leak
count beside the recall number, because the number that can
embarrass the project is the one that has to be in the room.
