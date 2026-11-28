# FDE 3.01 Exercise — Deployment topologies in customer land: place the same application three ways

**Topic:** Deployment topologies in customer land (Layer 6).
**Part (d) of FDE 3.01.**
Attempt this before watching the tutorial half of the lesson.
**Prerequisite:** Phase 2 — the build works. This exercise
opens Phase 3 at a new customer, with the question every
working build eventually meets: where does it land?

## The task

Read `topology-design.md` first. It describes Northline
Logistics' shipment exception triage assistant, its twelve
components, the three candidate topologies — cloud VPC,
on-premises, air-gapped — and the placement rules the
customer's infrastructure and compliance leads agreed
before any placement was computed.

Then build the deployment design the customer can check
without you:

1. `topology.py`, built from `topology_starter.py`: read
   the twelve components in `components.json`, apply the
   placement rules for each topology exactly as written,
   and fill the `RESULT` dictionary the grader checks.
   Every value must be computed from the file at run time.
2. `DEPLOYMENT.md` from `design-template.md`: the design
   you would hand the infrastructure lead — the placement
   of every component in every topology, what each blocked
   component costs the customer, and the verdict for each
   topology with its rule stated.

The design rules, agreed with the customer before you build:

- **A topology is a set of prohibitions, not a location.**
  What changes between the three homes is what is forbidden:
  regulated data over a public surface, any data leaving the
  premises, any connection at all. Place against the
  prohibitions, not against the geography.
- **Adapt is a named change at a named cost.** A component
  is adapted only when the adaptation its note names
  genuinely exists — a self-hosted form, a private endpoint,
  an allowlisted proxy. Wishing a component self-hostable
  does not make it so.
- **Blocked is a finding, not an embarrassment.** A blocked
  core component refuses the topology for the design as
  built. The professional outputs are a priced replacement
  design or a refusal — never a table that hides the block.

## Done means

- Every RESULT value is computed from `components.json` at
  run time — for each topology: the as-is, adapt and blocked
  counts, the sorted adapt and blocked id lists, the adapt
  hours, the blocked core count, and the verdict.
- The partitions hold, per topology: as-is plus adapt plus
  blocked is the twelve components, and every component id
  appears exactly once across the three lists.
- The design names, for every blocked component, what the
  customer loses by the cut — and for a blocked core
  component, the replacement-or-refusal conversation the
  verdict obliges you to have.
- Graded with `RUBRIC.md`. `SOLUTION.md` is the reference
  answer, released after the attempt window.

## The habit this exercise is really testing

- The same application is three different systems in three
  topologies. The components did not change; the prohibitions
  did — and the placement table, computed honestly, is what
  tells you which system you are actually being asked to land.
- Model access is the component everyone assumes travels.
  In customer land it is usually the first thing that does
  not — and the design that discovers that on paper is
  cheaper than the deployment that discovers it on site.
