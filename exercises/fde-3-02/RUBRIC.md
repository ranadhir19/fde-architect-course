# FDE 3.02 Rubric — 24 points

| Section | Points | What earns them |
|---|---|---|
| Computed map | 8 | All seventeen RESULT values computed from `controls.json` and matching SOLUTION.md exactly (status counts and sorted id lists, gate totals and gate gap list, per-framework totals and satisfied counts, verdict). Hand-typed numbers score zero here even if correct — the program is the artefact. |
| Status by the rules | 5 | The map applies the precedence exactly as written — missing before stale before unowned — and can show, for any control, which check produced its status and what artefact fact decided it. |
| Gate honesty | 4 | The verdict is stated as not ready, the gate gaps are named before any satisfied count, and no gate gap is described as a scheduling detail. The landing consequence of each gate gap is stated as plainly as the gap. |
| Gap closure | 4 | Every gap — gate and scheduled alike — is named with the artefact or action that closes it. A gap listed without closing work scores nothing in this section. |
| Framework reading | 3 | The map states each framework's total and satisfied count separately, and notes where the two frameworks disagree about the same build (the HIPAA map carries a missing gate control the SOC 2 map does not), so each reader decides on their own numbers. |

**Automatic fails:** reporting the build ready while a
gate control is in a gap status; reclassifying a gap by
hand (marking stale evidence fresh, or a missing artefact
as present) to improve the map; editing `controls.json`
or a control's record to change a status; leading the
map with the satisfied count while a gate gap exists
anywhere in it.
