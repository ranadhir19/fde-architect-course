# FDE 3.01 Reference solution

Released after the attempt window. All counts are of the
file as delivered and are reproduced by the reference
`topology.py`, built exactly to the starter's specification.

## The counts

| Finding | Value |
|---|---|
| components_total | 12 |
| cloud_as_is_count | 9 |
| cloud_adapt_count | 3 |
| cloud_blocked_count | 0 |
| cloud_adapt_ids | C04, C07, C10 |
| cloud_blocked_ids | (none) |
| cloud_adapt_hours | 22 |
| cloud_blocked_core_count | 0 |
| cloud_verdict | feasible |
| onprem_as_is_count | 5 |
| onprem_adapt_count | 5 |
| onprem_blocked_count | 2 |
| onprem_adapt_ids | C04, C06, C08, C09, C11 |
| onprem_blocked_ids | C07, C10 |
| onprem_adapt_hours | 26 |
| onprem_blocked_core_count | 0 |
| onprem_verdict | feasible_with_cuts |
| airgap_as_is_count | 5 |
| airgap_adapt_count | 3 |
| airgap_blocked_count | 4 |
| airgap_adapt_ids | C04, C08, C09 |
| airgap_blocked_ids | C06, C07, C10, C11 |
| airgap_adapt_hours | 20 |
| airgap_blocked_core_count | 1 |
| airgap_verdict | not_feasible_as_designed |

## The cloud is the control case

- Nine components land unchanged. The three adaptations
  share one trigger and one shape: model inference (C04),
  bill-of-lading OCR (C07) and the eval benchmark API
  (C10) each send regulated data out, so each is re-pointed
  to its vendor's private endpoint inside the VPC — 22
  hours of adaptation, no cuts, verdict feasible.
- That is the cloud's real lesson: in a VPC the topology
  costs you endpoint plumbing, not capability. Every harder
  number below is the price of a prohibition the cloud does
  not impose.

## On-premises: two cuts, neither core

- Five components never needed the internet and land as
  they are. Five adapt: model inference, telemetry and
  identity go self-hosted (C04, C08, C09), and the carrier
  rate feed and the update service are reached through the
  allowlisted proxy (C06, C11) — permitted because neither
  sends customer data out; the proxy is a route for public
  data in, not a pipe for regulated data out.
- Two components block. Cloud OCR (C07) would send bills
  of lading — shipper, consignee and goods data — to a
  vendor with no self-hosted form: the customer loses
  automated bill-of-lading reading, and dispatchers key
  those fields by hand until a local OCR is built. The
  eval benchmark API (C10) would send eval cases built
  from real shipments: the customer loses the vendor
  benchmark, and the eval set runs locally against the
  self-hosted model instead — a worse yardstick, honestly
  labelled. Neither is core, so the verdict is
  feasible_with_cuts, at 26 adapt hours — the most
  adaptation work of the three topologies, because the
  proxy route and the self-hosting both live here.

## Air-gapped: the feed is the finding

- The same five local components land unchanged, and the
  same three self-hostable components adapt (C04, C08,
  C09), at 20 hours — fewer adapt hours than on-premises,
  which is precisely the trap in reading hours as cost.
- Four components block: the two on-premises cuts (C07,
  C10), the update service (C11 — a nuisance, priced as
  manual media updates in a replacement design), and the
  carrier rate feed (C06). The feed carries no regulated
  data and blocked nothing on-premises, where the proxy
  reached it. In the air gap there is no proxy. The feed
  only exists outside, so inside it does not exist — and
  the feed is core: exception triage prices its drafts
  against the current surcharge tables the feed delivers.
- One blocked core component makes the verdict
  not_feasible_as_designed. The design's honest outputs
  are a replacement — a scheduled, signed snapshot import
  of the published rate tables on physical media, priced
  separately, with its staleness stated on the page — or
  a refusal of the air-gapped topology for this system.
  What the design may not do is list C06 as adapted: the
  snapshot import is a different component, not an
  adaptation of the feed, and calling it one is how
  air-gapped deployments are promised and then discovered.

## The comparison

- Cloud VPC forbids regulated data on a public surface:
  3 adaptations, 0 blocked, feasible.
- On-premises additionally forbids data leaving the
  premises at all: 5 adaptations, 2 blocked, neither
  core, feasible with cuts.
- The air gap additionally forbids connection itself:
  3 adaptations, 4 blocked, one core, not feasible as
  designed. Each topology's table is the previous table
  plus one prohibition — and the last prohibition is the
  one that reaches a component nobody suspected, because
  it carried nothing sensitive at all.

## Certification

- Certified: the three placement tables as a runnable
  artefact (each placement reproduces from the component
  attributes without a human re-arguing a rule), and the
  three verdicts under the rules as written.
- Refused: adapting a blocked component on paper, editing
  a component's attributes to land it, a proxy in the air
  gap, and any summary that reports the air-gapped adapt
  hours (20, the lowest) without the blocked core
  component that makes the topology infeasible as designed.
