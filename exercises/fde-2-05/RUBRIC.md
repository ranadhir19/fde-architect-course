# FDE 2.05 Rubric — 24 points

| Section | Points | What earns them |
|---|---|---|
| Computed measurement | 8 | All sixteen RESULT values computed from `cases.json` and matching SOLUTION.md exactly (gold split, five taxonomy counts, rater agreement counts and rate, kappa, judge correct/accuracy and both error counts). Hand-typed numbers score zero here even if correct — the program is the artefact. |
| Kappa done honestly | 6 | Kappa computed by the stated formula from the raters' own marginals, rounded as specified, and reported beside — never instead of — the raw agreement rate. Quoting agreement alone as reliability, or importing a kappa whose convention you cannot state, loses these points. |
| Judge certified per direction | 4 | The judge's errors are split into false passes and false fails, the false passes are expressed against the gold failures, and the verdict applies the pre-set rule (any false pass ends grade-alone use) rather than the overall accuracy. |
| Report: thresholds applied as set | 3 | The report applies the 0.80 kappa threshold and the false-pass rule exactly as agreed before grading, names the disagreement cases, and records adjudication's fate from the numbers — no threshold is renegotiated in the report. |
| Set discipline | 3 | Nothing re-labelled to make the numbers kinder: no case moved between categories after grading, no gold label edited to raise agreement, no disagreement case dropped from the set. |

**Automatic fails:** reporting the judge's accuracy without
its false-pass count; editing `cases.json`; moving the 0.80
threshold after seeing the kappa; treating the majority vote
of raters plus judge as the gold label.
