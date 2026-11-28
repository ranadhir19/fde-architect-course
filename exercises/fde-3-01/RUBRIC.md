# FDE 3.01 Rubric — 24 points

| Section | Points | What earns them |
|---|---|---|
| Computed placements | 8 | All twenty-five RESULT values computed from `components.json` and matching SOLUTION.md exactly (per topology: counts, sorted adapt and blocked ids, adapt hours, blocked core counts, verdicts). Hand-typed numbers score zero here even if correct — the program is the artefact. |
| Placement by the rules | 5 | The design applies each topology's rules as written — private-endpoint adaptation in the cloud, the proxy only for components carrying no regulated data on-premises, no proxy fiction in the air gap — and can show, for any component in any topology, which rule placed it there. |
| Blocked-component honesty | 4 | Every blocked component is named with the capability the customer loses; no blocked component is relabelled as adapted, and no component's attributes are edited to make a placement landable. |
| The core verdict | 4 | The air-gapped verdict is stated as not feasible as designed, with the blocked core component named and the replacement-or-refusal conversation set out — priced separately, in the open, before the topology is chosen. |
| Topology comparison | 3 | The design states, per topology, what it forbids that the previous one allowed, and puts the adapt hours and blocked counts side by side so the infrastructure lead decides on the comparison, not on three separate tables. |

**Automatic fails:** listing a blocked component as
adapted in any topology; editing `components.json` or a
component's attributes to change a placement; claiming
the air-gapped design is feasible while a core component
is blocked; reaching a component through the proxy in
the air-gapped topology, where no proxy exists.
