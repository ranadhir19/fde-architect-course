# FDE 2.06 Rubric — 24 points

| Section | Points | What earns them |
|---|---|---|
| Computed gate | 8 | All twenty-eight RESULT values computed from `runs.json` and `canary.json` and matching SOLUTION.md exactly (per-version counts and deltas, both candidates' largest category failure increases, critical counts and deltas, both gate verdicts, shadow and canary counts and rates, worst block rate, kill-switch state, promotion verdict). Hand-typed numbers score zero here even if correct — the program is the artefact. |
| Rules applied as written | 6 | The verdicts follow from G1, G2 and G3 applied in order to the computed counts, and the report names, for the failed candidate, each rule it failed and the margin. Reaching the right verdict by a different rule loses these points. |
| Slices over totals | 4 | The report shows the category failure changes behind each candidate's largest increase — in particular that v1.4's near-flat total is the sum of real improvements and two categories gaining two failures each — rather than reporting the total alone. |
| Promotion as its own decision | 3 | Shadow and canary are reported separately from the gate, the kill switch is tested on both of its conditions, and the promotion verdict checks all three of its conditions against the numbers. |
| Gate discipline | 3 | Nothing re-scored to make a verdict kinder: no rule threshold adjusted after the counts landed, no case dropped from a category, no critical flag removed. Any proposed rule change is recorded as a proposal for the next candidate, never applied to this one. |

**Automatic fails:** reporting a candidate's overall pass
count as its gate verdict; editing `runs.json` or
`canary.json`; promoting a candidate that failed the gate;
waiving the critical rule because the total improved.
