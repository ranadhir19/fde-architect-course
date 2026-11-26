# FDE 2.04 Rubric — 24 points

| Section | Points | What earns them |
|---|---|---|
| Computed exposure and evaluation | 8 | All nine RESULT values computed from the files and matching SOLUTION.md exactly (operations total, exposed, withheld; requests evaluated, allowed, denied; the three denial reasons). Hand-typed numbers score zero here even if correct — the program is the artefact. |
| Exposure by rule, not by list | 6 | The exposed set is computed from the rule (kind is read, data class is internal) applied to the registry — not written into the code as three names. A hard-coded list that happens to match loses these points: it silently stops being the rule the first time the registry changes. |
| Evaluation order | 4 | Requests are checked exposure first, role second, arguments last, and counted once under the first failed check. Checking arguments or roles for a tool that is not exposed loses half these points even when the totals agree, because the order is itself a disclosure decision. |
| Report: the withholding defended | 3 | The report groups the nine withheld operations by reason (patient-data reads, bulk export, writes, administration), names the owner who can reconsider each group, and states the veto that was exercised over the bulk extract. |
| Scope discipline | 3 | Nothing exposed beyond the rule: no write "just for the demo", no patient-data read reclassified as internal, no role quietly widened to make a denial count smaller. |

**Automatic fails:** any write, admin, patient-data, or bulk
operation in the exposed set; editing `operations.json` or
`requests.json`; reporting the allowed count without the
denial counts beside it.
