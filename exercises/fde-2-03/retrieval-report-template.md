# Retrieval report — discharge-guidance assistant (template)

Copy this file to `RETRIEVAL.md` and complete every section
from your program's computed output. A number that does not
come from running the program does not belong in the report.

## Coverage

- Corpus as delivered: ___ documents.
- Indexed after the guardrail: ___ documents.
- Excluded by the guardrail: ___ documents, named by rule: ___.

## The measured target

- Recall at 5: ___ against the agreed target of at least 0.90.
- Precision at 5: ___.
- Queries evaluated: ___ , gold documents found in the top 5: ___.

## The guardrail

- Restricted documents returned across all queries: ___.
- The same system measured without the filter returns ___
  restricted documents in the top 5 (measure it; do not guess).
- The failure the recall number cannot see, in one sentence: ___.

## Open risks and refusals

- The access levels were assigned by ___ and last reviewed ___.
  The risk the engagement accepts for v1 is: ___.
- The one thing this system must not be used for yet: ___.
