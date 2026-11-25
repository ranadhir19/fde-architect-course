# FDE 2.01 Rubric — 24 points

| Section | Points | What earns them |
|---|---|---|
| Computed counts | 8 | All eleven FINDINGS values computed from the file and matching SOLUTION.md exactly (rows, duplicates, both empty counts, silent nulls, both date-format counts). Hand-typed numbers score zero here even if correct — the program is the artefact. |
| Drift located | 5 | Both drift points given as exact 1-based data rows (first non-ISO admit date; first undotted diagnosis code), each with the two forms named. |
| Defect classification | 5 | Every defect in the register classified blocks / shapes / cosmetic with a build consequence; duplicates and the re-identifiable patient_ref are classed as blocking, with reasons. |
| Access and ownership | 4 | All three vacancies named: the unowned bed board, the coding standard that does not exist, and the unfiled request for the standing extract. The nightly-extract claim is flagged as unverified, not repeated as fact. |
| The refusal | 2 | One source refused, a named person who can clear it, and one exact question — not a general request for "clarification". |

**Automatic fails:** de-duplicating or cleaning the file before
counting (the counts must describe the file as delivered);
reporting a count the program does not produce; calling
`patient_ref` de-identified without raising the one-lookup
re-identification path; inventing an owner for the bed board.
