# Worked example — FDE 2.05: a 60-case eval set that demoted its own judge, annotated

Referenced by the FDE 2.05 learning session. The customer is
fictional; the pattern is a composite written for this course.
Annotations in brackets name the move being made. This example
uses a different customer from the exercise, on purpose: copy
the moves, not the words.

> **EVAL CALIBRATION NOTE (excerpt) — Larkspur Freight
> rate-quote assistant**
>
> **Why a local set at all.** The vendor reported 94 percent
> on a logistics benchmark of 2,000 cases. Larkspur's desk
> lead accepted the number as evidence about some other
> firm's freight: none of the benchmark cases involved
> Larkspur's rate cards, its two superseded tariff versions,
> or its rule that named-customer pricing is never quoted by
> the assistant. The engagement built 60 cases from the
> desk's own tickets instead — fewer cases, all of them
> about the failures this firm can actually have.
>
> *[An eval set is an argument about what failure looks
> here. Sample size serves the argument; it does not replace
> it. Sixty argued-over local cases outrank two thousand
> generic ones for every decision the desk lead owns.]*
>
> **The graders, measured.** Two dispatchers graded the 60
> independently and agreed on 53 — 88 percent, which the
> vendor's slide called excellent. Their marginals predicted
> 55 percent agreement by chance, putting kappa at 0.74,
> below the 0.80 line the desk had set before grading. The
> 7 disagreements went to the desk lead for adjudication,
> and adjudication stayed in the process for the next round.
>
> *[Report agreement and kappa together, and let the
> pre-set threshold decide. The number that flatters the
> process is the raw rate; the number that governs it is
> the one corrected for chance.]*
>
> **The judge, demoted by its own errors.** The LLM judge
> scored 88 percent overall — and passed 4 of the 17 real
> failures, three of them responses that quoted superseded
> tariffs with complete confidence. Under the rule set
> before grading, that ended its application to grade alone.
> It still triages the weekly case intake, ordering likely
> failures first for the dispatchers, where being wrong
> costs minutes instead of a wrong quote reaching a customer.
>
> *[Overall accuracy is the average of two very different
> errors. A judge that fails toward the customer is a
> different instrument from one that fails toward the
> reviewer, whatever the shared percentage says.]*

**The lesson:** a customer-specific eval set is built from
the customer's failures, graded by graders who have
themselves been measured, and judged by a judge that has
been certified per error direction — or it is a vendor
number wearing the customer's name.
