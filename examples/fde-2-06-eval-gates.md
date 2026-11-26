# Worked example — FDE 2.06: the version the total would have shipped, annotated

Referenced by the FDE 2.06 learning session. The customer is
fictional; the pattern is a composite written for this course.
Annotations in brackets name the move being made. This example
uses a different customer from the exercise, on purpose: copy
the moves, not the words.

> **GATE REPORT (excerpt) — Larkspur Freight rate-quote
> assistant, candidate v2.2**
>
> **The total, first — because it is the trap.** V2.2 passes
> 44 of the desk's 60 local cases against the production
> version's 41. On the vendor's slide that is the whole
> story: three cases better, ship it. The gate report prints
> the total on the first line and then refuses to stop there.
>
> *[Print the total. Then judge the slices. A gate that hides
> the flattering number looks rigged; a gate that stops at
> it is rigged.]*
>
> **The slice that decided it.** Failures on superseded
> tariffs — the category the desk lead named as the one that
> reaches a customer as a wrong price — rose from 2 to 5.
> The gate's slice rule allows an increase of one. The
> version's real gains sat in formatting and in follow-up
> phrasing, categories whose failures cost a dispatcher a
> correction, not a customer a wrong quote. The gate failed
> v2.2 on the slice rule, and the report named the category
> and the margin: three failures over baseline, two over
> the allowance.
>
> *[Improvements do not average away a regression in the
> category that carries the risk. That is not strictness;
> it is what the categories were for.]*
>
> **What happened next.** The vendor fixed the tariff-version
> lookup and resubmitted as v2.3: same 44 passes overall,
> superseded-tariff failures back at 2. The gate passed it
> without a meeting — the on-call dispatcher ran it at 06:10
> and the build went green. In its canary week the third
> block of 20 dipped to a 0.75 pass rate, above the 0.70
> kill-switch floor, so the canary held and the version
> promoted. The dip is in the log with its cause (a holiday
> rota the desk had not modelled), because a block that
> nearly trips the switch is evidence, not embarrassment.
>
> *[A gate earns trust twice: once by stopping the version
> the room wanted to ship, and once by passing the fixed
> version without needing the room at all.]*

**The lesson:** a regression gate is the eval set with
authority — pre-agreed rules over slices and critical cases,
applied by a program, whose verdict stands when the
champion of the new version is standing right there with
a better-looking total.
