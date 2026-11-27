# FDE 2.09 Rubric — 24 points

| Section | Points | What earns them |
|---|---|---|
| Computed plan | 8 | All twenty-four RESULT values computed from `findings.json` and matching SOLUTION.md exactly (counts and sorted ids for deferred, fixed and backlog findings, the risk in each partition, hours, slack, reduction, residual risks, category counts, verdict). Hand-typed numbers score zero here even if correct — the program is the artefact. |
| Selection by the rules | 5 | The hardening plan applies the rules in their stated order — deferral of blocked findings before ranking, ranking by risk with the id tie-break, the tie at the cut line fixed whole — and can show, for any finding, which rule placed it where it is. |
| Privacy and secrets substance | 4 | Each fixed finding's fix is its fix note in full (rotation and purge, redaction and purge, demotion of pasted text to data, authentication on every endpoint) — a half-fix recorded as fixed earns nothing here. |
| Deferral honesty | 4 | Every deferred finding leaves with its blocker text, the customer action that unblocks it, and its owner named; no blocked finding is fixed by substitution, and interim mitigations are labelled as mitigations, not closures. |
| Residual risk reporting | 3 | The plan prints the residual risk and the highest backlog risk beside the verdict, and states what hardened-for-pilot does and does not claim. |

**Automatic fails:** splitting the tie at the cut line
by id; fixing a blocked finding by building a substitute;
editing `findings.json` or its severity, likelihood or
risk scores; claiming the build is secure in general on
the strength of the pilot verdict.
