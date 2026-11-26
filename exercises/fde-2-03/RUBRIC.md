# FDE 2.03 Rubric — 24 points

| Section | Points | What earns them |
|---|---|---|
| Computed retrieval | 8 | All eight RESULT values computed from the files and matching SOLUTION.md exactly (corpus counts, indexed and excluded, queries, hits, recall and precision at 5, restricted returned). Hand-typed numbers score zero here even if correct — the program is the artefact. |
| Guardrail as engineering | 6 | The restricted filter is applied before ranking, the excluded count is reported, and restricted-returned is zero — with the unfiltered leak count measured and stated in the report. Filtering the output list after ranking, instead of the index, loses half these points even at zero leaks, because a filtered-out slot is a document a user never saw. |
| Specified method, reproduced | 4 | The scoring follows the starter's specification exactly (tokenisation, stopwords, IDF formula over the indexed set, cosine, doc_id tie-break), so a re-run by anyone reproduces the same numbers. A different method that happens to score well earns the retrieval points only if its numbers still match and the report names the deviation. |
| Report honesty | 3 | The report states recall and the leak count side by side, names the failure recall cannot see, and carries the unreviewed-access-levels risk as an accepted risk with an owner — not as a footnote. |
| Scope discipline | 3 | Retrieval only, as scoped: no generated answer layer, no gold set quietly edited to raise recall, no restricted document reclassified to make the leak count easier. |

**Automatic fails:** any restricted document returned in any
top 5; editing `queries.json` or a gold set; reclassifying a
restricted document as internal; reporting recall without the
leak count beside it.
