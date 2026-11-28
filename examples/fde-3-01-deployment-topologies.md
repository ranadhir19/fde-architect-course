# Worked example — FDE 3.01: the topology nobody priced, annotated

Referenced by the FDE 3.01 learning session. The customer is
fictional; the pattern is a composite written for this course.
Annotations in brackets name the move being made. This example
uses a different customer from the exercise, on purpose: copy
the moves, not the words.

> **DEPLOYMENT DESIGN (excerpt) — Larkspur Freight
> quote-desk build, three-topology placement**
>
> **The cloud table took an afternoon.** The quote desk's
> drafting model and its document store both touched
> customer rate data, so both were re-pointed to private
> endpoints and the rest landed as built. The design
> review spent longer on the catering for the go-live
> than on the placements. That ease was recorded in the
> design as what it was: a property of the topology, not
> evidence the system was portable.
>
> *[A feasible cloud table certifies the cloud. It says
> nothing about any other land the customer owns.]*
>
> **On-premises cost the OCR, and that was the right
> price.** The terminal operator's site forbade data
> leaving the premises. The cloud OCR that read the
> terminal's paper gate passes had no local form, so it
> was cut, named as a capability — gate passes keyed by
> hand, four minutes a truck — and the quote desk landed
> without it. Nobody proposed sending the passes out
> "temporarily" until a local reader existed. Temporary
> is how a prohibition becomes a rumour.
>
> *[A blocked non-core component is a cut with a named
> cost. Pricing the cost is what makes the cut a design
> decision instead of a gap.]*
>
> **The air-gapped site refused the design, and the feed
> was why.** The bonded warehouse ran air-gapped. Its
> placement table blocked the live tariff feed — a core
> component carrying published data that had survived
> every other topology through a proxy that, in the air
> gap, did not exist. The verdict was written as not
> feasible as designed, and the replacement — a signed
> weekly snapshot of the tariff tables, carried in on
> media, its seven-day staleness printed on every quote
> the desk produced — was priced as its own design and
> chosen by the customer with its eyes open.
>
> *[The component that breaks an air gap is rarely the
> sensitive one. It is the public one everyone reached
> for without thinking, because reaching was free.]*
>
> **The sentence under all three tables.** Each topology
> forbade one more thing than the one before it, and the
> design printed the prohibitions, not the place names,
> at the head of each table — because the customer's
> fourth site, when it came, would be none of the three
> places and exactly one of the prohibition sets.
>
> *[Place against prohibitions and the next site is a
> recomputation. Place against place names and it is a
> new engagement.]*

**The lesson:** a deployment topology is a set of
prohibitions wearing a place name — compute the same
application against each set, let blocked components say
what they cost, and let a blocked core component refuse
the topology out loud, on paper, before anyone ships
hardware to a site that cannot run the design.
