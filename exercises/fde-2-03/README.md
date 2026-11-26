# FDE 2.03 Exercise — Build the retrieval system, guardrail first

**Topic:** LLM application engineering for one customer (Layer 4).
**Part (d) of FDE 2.03.**
Attempt this before watching the tutorial half of the lesson.
**Prerequisite:** FDE 2.02 (legacy integration) — the pipeline you
built there is what feeds a system like this one in production.

## The task

Read `corpus-and-queries.md` first. It describes the Alder Creek
Health Network discharge-guidance assistant as scoped: a retrieval
system over the network's own guidance documents, for ward staff,
with one hard guardrail fitted to this customer's risk — documents
marked restricted carry worked patient examples and must never be
returned to anyone, however well they match a query.

Then build it:

1. `retrieval.py`, built from `retrieval_starter.py`: index the
   documents in `documents.csv` that the guardrail allows, score
   them against each query in `queries.json` with the TF-IDF
   cosine method the starter specifies exactly, and fill the
   `RESULT` dictionary the grader checks. Every value must be
   computed from the files at run time.
2. `RETRIEVAL.md` from `retrieval-report-template.md`: the report
   you would hand the ward lead before this goes near a user —
   the measured recall against the stated target, the guardrail
   stated as a rule with its leak count, and the one failure you
   found that the headline number hides.

The measured target, agreed with the customer before you build:
**recall at 5 of at least 0.90, with zero restricted documents
returned.** Both halves are the target. A system that hits the
recall number and leaks fails; a system that leaks nothing and
misses the documents fails more quietly, and also fails.

## Done means

- The index contains only documents the guardrail allows, and
  the excluded count is reported, not silently dropped.
- Recall and precision at 5 are computed against the gold
  relevance sets in `queries.json` — not estimated, not sampled.
- The restricted-returned count is zero, and the report states
  what that count would have been without the filter, from your
  own measurement, not from intuition.
- The scoring method in your program is the one the starter
  specifies (tokenisation, stopwords, IDF formula, tie-break),
  so your numbers are reproducible by anyone who re-runs it.
- Graded with `RUBRIC.md`. `SOLUTION.md` is the reference
  answer, released after the attempt window.

## The habit this exercise is really testing

- A retrieval metric is a claim about one failure class only.
  Recall says nothing about leakage; the guardrail needs its
  own measurement, reported beside the headline, every time.
- Guardrails fitted to the customer's risk are engineering,
  not policy decoration: here the risk has a name (identifiable
  patient detail in worked examples), a location (eight
  documents), and a test (zero returned, counted).
