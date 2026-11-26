"""Starter for FDE 2.03. Copy to retrieval.py and complete it.

Compute every value from the two delivered files at run time.
The grader imports RESULT from your retrieval.py; accuracy is
scored against SOLUTION.md with RUBRIC.md.

The scoring method is specified exactly, so numbers reproduce:
  - Tokenise: lowercase, take runs of [a-z0-9]+, drop STOPWORDS.
  - Document text is the title and the text field, joined.
  - Guardrail first: documents whose access_level is restricted
    are never indexed. N is the count of indexed documents.
  - Term weight: raw count times idf, where
    idf(t) = ln((N + 1) / (df(t) + 1)) + 1 and df counts indexed
    documents containing t. The query uses the same weights.
  - Score: cosine similarity. Rank by score descending, then
    doc_id ascending. Take the top 5 per query.
"""
import csv
import json
from pathlib import Path

HERE = Path(__file__).parent
DOCUMENTS = HERE / "documents.csv"
QUERIES = HERE / "queries.json"

STOPWORDS = {
    "the", "a", "an", "and", "or", "of", "to", "in", "on", "for",
    "with", "this", "that", "is", "are", "be", "by", "at", "from",
    "it", "its", "as", "do", "not",
}


def load_documents():
    with DOCUMENTS.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def load_queries():
    return json.loads(QUERIES.read_text(encoding="utf-8"))


def build_result(documents, queries):
    # Replace each placeholder with a computed value.
    return {
        "documents_total": 0,
        "documents_indexed": 0,     # documents the guardrail allows into the index
        "restricted_excluded": 0,   # documents the guardrail keeps out
        "queries_evaluated": 0,
        "hits_at_5": 0,             # gold documents found in the top 5, summed over queries
        "recall_at_5": 0.0,         # mean over queries of hits / gold set size, rounded to 4 places
        "precision_at_5": 0.0,      # mean over queries of hits / 5, rounded to 4 places
        "restricted_returned": 0,   # restricted documents in any top 5 (must be zero)
    }


RESULT = build_result(load_documents(), load_queries())

if __name__ == "__main__":
    for key, value in RESULT.items():
        print(f"{key}: {value}")
