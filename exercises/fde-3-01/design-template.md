# DEPLOYMENT.md — the same application in three topologies (template)

Hand this to the customer's infrastructure lead. Every
number comes from your own run of `topology.py` over
`components.json` as delivered.

## The application in one line

- Twelve components, of which (n) are core. The three
  topologies differ in what they prohibit, and the
  placements below are computed against those prohibitions
  by the agreed rules — not negotiated per component.

## Cloud VPC

- As-is (n), adapt (n) at (n) hours, blocked (n).
  Verdict, with its rule.
- Each adapted component: the private-endpoint change it
  needs, and why regulated data is the trigger.

## On-premises

- As-is (n), adapt (n) at (n) hours, blocked (n).
  Verdict, with its rule.
- Each adapted component: the self-hosted form or the
  proxy route that lands it.
- Each blocked component: what the customer loses by the
  cut, stated as a capability, not a component name.

## Air-gapped

- As-is (n), adapt (n) at (n) hours, blocked (n), of
  which (n) core. Verdict, with its rule.
- The blocked core component, named on its own line:
  the replacement design conversation or the refusal
  this verdict obliges, and what each would cost the
  customer to hear late instead of now.

## The comparison the decision is actually made on

- Adapt hours per topology, blocked counts per topology,
  and the one sentence that separates the three: what
  each topology forbids that the one before it allowed.

## What this design does not claim

- One line: a placement is a claim about the components
  as discovery recorded them. What would change the
  table — a component attribute corrected, a self-hosted
  form that turns out not to exist — and how the design
  would be recomputed when it does.
