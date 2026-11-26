# FDE 2.03 Reference solution

Released after the attempt window. All counts are of the files
as delivered and are reproduced by the reference `retrieval.py`,
built exactly to the starter's specification.

## The counts

| Finding | Value |
|---|---|
| documents_total | 48 |
| documents_indexed | 40 |
| restricted_excluded | 8 |
| queries_evaluated | 20 |
| hits_at_5 | 40 |
| recall_at_5 | 1.0 |
| precision_at_5 | 0.4 |
| restricted_returned | 0 |

## What the numbers mean

- **Recall 1.0, precision 0.4 — read both.** Every query's two
  gold documents are inside its top 5, so the recall target
  (at least 0.90) is met with room. Precision at 5 is 0.4 by
  arithmetic, not by failure: two gold documents in a list of
  five is the most precision this gold design can show. A
  report that apologises for 0.4 has not understood its own
  measurement; a report that hides it has understood and
  chosen not to say.
- **The leak the headline hides.** Measured without the
  guardrail filter — same scoring, all 48 documents indexed —
  a restricted worked example reaches the top 5 on **every one
  of the 20 queries (20 restricted returns)**, while recall
  stays at 1.0. The restricted documents match so well because
  they repeat each topic's whole vocabulary around a real case.
  That is the exercise's central fact: the unfiltered system
  passes the recall target and leaks on every query. Recall
  certifies relevance; it certifies nothing else.
- **Why filter before ranking.** With post-ranking filtering,
  each query's leaked document would silently consume a top-5
  slot and then be removed, showing the user four documents
  and hiding that a fifth existed. Filtering the index keeps
  the top 5 honest: five allowed documents, and an exclusion
  count (8) that can be audited against the corpus.

## Certification

- Certified for the build: the guidance corpus as indexed —
  eight topics, gold sets with two reviewers behind them, a
  measured target met on both halves.
- Refused, for now: any use of the restricted worked examples
  in this system, and any generated-answer layer on top of the
  retrieval, until the training group reviews the access levels
  it assigned and the ward lead re-opens the v1 scope decision
  in the engagement log. The open risk carried in the report:
  the access levels have never been reviewed, so the guardrail
  is only as good as labels nobody has checked since they were
  written — the filter is verified; the labels are trusted.
