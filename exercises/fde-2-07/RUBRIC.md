# FDE 2.07 Rubric — 24 points

| Section | Points | What earns them |
|---|---|---|
| Computed summary | 8 | All twenty-nine RESULT values computed from `traces.json` and matching SOLUTION.md exactly (counts, window rates and delta, critical count, medication counts, shares and drift, latency and cost means, maxima and breach counts, alert and verdict). Hand-typed numbers score zero here even if correct — the program is the artefact. |
| Windows over totals | 5 | The report leads with the early-versus-late comparison and reads the overall rate through it, rather than reporting the week as its average. |
| Drift measured, not asserted | 4 | The medication share change is computed from the traces in both windows and judged against the pre-agreed ten-point rule; the report connects the drift to the pass-rate movement without claiming the drift alone proves causation. |
| Budgets and criticals | 4 | Latency and cost are each reported as a mean beside a breach count against the pre-agreed budget, and critical failures are reported as a count of their own, never folded into the fail total alone. |
| Alert discipline | 3 | The verdict follows the four rules as written, each rule's state is named, and no threshold is adjusted after the numbers are known. Any proposed change is recorded for next week, never applied to this one. |

**Automatic fails:** reporting the overall pass rate as
the week's verdict; editing `traces.json`; declaring the
week healthy while any alert condition holds; averaging
the critical failures into the overall fail rate and
reporting nothing separately.
