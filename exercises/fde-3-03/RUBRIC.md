# FDE 3.03 Rubric — 24 points

| Section | Points | What earns them |
|---|---|---|
| Computed pack | 8 | All sixteen RESULT values computed from `questionnaire.json` and matching SOLUTION.md exactly (status counts and sorted id lists, gate totals and gate gap list, overclaim count and list, section count, verdict). Hand-typed numbers score zero here even if correct — the program is the artefact. |
| Status by the rules | 5 | The pack applies the precedence exactly as written — unsupported before stale before partial — and can show, for any question, which check produced its status and what artefact fact decided it. |
| Gate honesty | 4 | The verdict is stated as blocked, the gate gaps are named before any supported count, and no gate gap is described as a qualification or a scheduling detail. The submission consequence of each gate gap is stated as plainly as the gap. |
| Overclaims corrected | 4 | Every drafted "yes" the evidence does not support is found, named as an overclaim, and replaced in the returned pack with the honest answer. An overclaim the pack repeats, or one it quietly deletes instead of correcting, scores nothing in this section. |
| Qualified answers | 3 | Each partial or stale non-gate answer is returned as a qualification that names exactly what the evidence covers and what it does not, with the closing work for each. A qualification vaguer than its evidence scores nothing here. |

**Automatic fails:** submitting or recommending
submission of the questionnaire while a gate question
is in a gap status; reclassifying an answer by hand
(marking a missing artefact as present, a stale one as
fresh, or partial scope as full) to improve the pack;
editing `questionnaire.json` or a question's record to
change a status; leading the pack with the supported
count while a gate gap exists anywhere in it.
