# Northline Logistics — the same application, three places to land it

Fictional composite, opening Phase 3. Northline Logistics is a
regional freight and warehousing operator. The engagement built a
shipment exception triage assistant: it reads exception events,
retrieves the carrier documents that govern them, drafts the
response a dispatcher approves, and logs every decision. The build
works. Phase 3 starts with the question the build never answered:
where, exactly, does it run — in whose land, under whose rules?

Northline has three candidate homes for the system, and they are
not three sizes of the same thing:

- **Cloud VPC.** A virtual private cloud in the customer's own
  cloud account. Outbound internet is available. Contracted
  vendors may receive regulated data only over private endpoints
  inside the VPC boundary — never over the public API surface.
- **On-premises.** Northline's own data centre. No customer data
  of any kind may leave the premises. Outbound internet exists
  through a customer proxy with an allowlist, and services that
  receive no customer data may be reached through it.
- **Air-gapped.** A segregated network segment with no internet
  connection in either direction. Nothing reaches out, nothing
  is reached. Updates and imports arrive on physical media, on
  a schedule, carried by a person.

`components.json` holds the twelve components the system is
actually made of. Each records whether it requires the internet
as built, whether a self-hosted form of it genuinely exists,
whether its external dependency would receive regulated data
(shipment, shipper and consignee data), whether it is core —
the triage workflow fails without it — its adaptation cost in
engineering hours where adaptation is needed, and a note from
discovery.

## The placement rules (agreed before any placement was computed)

Applied per topology, exactly as written. A component's
disposition is one of: **as_is** (it lands unchanged),
**adapt** (it lands after the adaptation its note names, at
its recorded adapt hours), or **blocked** (it cannot land in
this topology as designed — it is cut, replaced by a different
design, or the topology is refused; it is never quietly
assumed away).

1. **Cloud VPC.** A component that sends regulated data out is
   **adapt**: it is re-pointed to the vendor's private endpoint
   inside the VPC before it may run. Every other component is
   **as_is**. Nothing is blocked in the cloud topology — which
   is a fact about the cloud, not a virtue of the design.
2. **On-premises.** A component that does not require the
   internet is **as_is**. A component that requires the
   internet and is self-hostable is **adapt**: the self-hosted
   form replaces the external call. A component that requires
   the internet, is not self-hostable, and sends no regulated
   data out is **adapt**: it is reached through the customer's
   allowlisted proxy. A component that requires the internet,
   is not self-hostable, and sends regulated data out is
   **blocked**: the data may not leave, and there is no local
   form to land.
3. **Air-gapped.** A component that does not require the
   internet is **as_is**. A component that requires the
   internet and is self-hostable is **adapt**. A component
   that requires the internet and is not self-hostable is
   **blocked**, whatever data it carries: in an air gap there
   is no proxy, and a feed that only exists outside does not
   exist inside.

## The verdicts

One verdict per topology, by rule, not by optimism:

- **feasible** — nothing is blocked.
- **feasible_with_cuts** — something is blocked, and nothing
  blocked is core. The cuts are named in the design, with what
  the customer loses by each one.
- **not_feasible_as_designed** — a core component is blocked.
  The design as built cannot run there. The honest outputs are
  a replacement design for the blocked core component, priced
  separately, or a refusal of the topology — never a placement
  table that lists the core component as adapted when the
  adaptation does not exist.

## Ownership

- Northline's infrastructure lead owns the topology choice;
  its compliance lead owns the regulated-data calls recorded
  in `components.json`; the engagement owns the placements
  and the honesty of the verdicts.
- A disposition is a claim about a real dependency. If
  discovery got a component's attributes wrong, the fix is
  to correct the file and recompute — never to adjust a
  placement by hand until the table looks landable.
