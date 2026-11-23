# FDE 1.01 Reference solution

Released after the attempt window.

| ID | Role | Deciding fact |
|---|---|---|
| 1 | sales-engineer | Pre-sale, standard product, no production code in customer systems. |
| 2 | fde | Post-sale, production code in the customer's systems, accountable for the metric moving. |
| 3 | solutions-architect | Design and hand over; does not deploy or stay accountable for adoption. |
| 4 | consultant | Advice and a document; leaves before anything runs in production. |
| 5 | product-engineer | One capability for many customers — the roadmap, not one customer's workflow. |
| 6 | fde | Discovery inside one customer's operation, aimed at a deployable slice. |
| 7 | sales-engineer | Pre-sale evaluation support; nothing is deployed. |
| 8 | fde | Stays after go-live and is measured on adoption and workflow impact. |
| 9 | consultant | Recommendation only; no system is built or operated. |
| 10 | solutions-architect | Platform-wide design standard, not one customer's deployment. |
| 11 | product-engineer | Shared product code serving all customers equally. |
| 12 | fde | Production integration inside one customer's stack, under that customer's constraints. |

The pattern: only tasks 2, 6, 8, and 12 are FDE work — post-sale, one customer, production code in their systems, accountability for adoption or the metric.
