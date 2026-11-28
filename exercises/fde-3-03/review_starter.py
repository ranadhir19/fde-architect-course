"""Starter for FDE 3.03. Copy to review.py and complete it.

Compute every value from the delivered file at run time.
The grader imports RESULT from your review.py; accuracy
is scored against SOLUTION.md with RUBRIC.md.

The answering is specified exactly, so packs reproduce:
  - questionnaire.json holds sixteen questions, each
    with its id, section, question text, draft_claim
    ("yes" or "qualified"), evidence artefact,
    evidence_present flag, evidence age in days (null
    when the artefact does not exist), maximum evidence
    age in days, scope_covers flag, owner (blank when
    nobody is named), is_gate flag, and a workshop note.
  - A question's status is the first failing check, in
    this order: "unsupported" when the evidence
    artefact does not exist; "stale" when its age in
    days is greater than the maximum evidence age;
    "partial" when it exists and is fresh but does not
    cover the whole scope of the question; otherwise
    "supported".
  - An overclaim is a question whose draft_claim is
    "yes" and whose status is not "supported".
    overclaim_ids is the sorted list of those ids.
  - gate_total is the number of questions whose
    is_gate flag is true; gate_supported_count is how
    many of those are supported; gate_gap_ids is the
    sorted list of gate questions in any gap status.
  - sections_count is the number of distinct section
    values across the file.
  - Verdict: "ready_to_submit" when every question is
    supported; "blocked" when at least one gate
    question is in a gap status; otherwise
    "submit_with_qualifications".
  - Id lists are sorted ascending.
"""
import json
from pathlib import Path

HERE = Path(__file__).parent


def load(name):
    return json.loads((HERE / name).read_text(encoding="utf-8"))


def build_result(questions):
    # Replace each placeholder with a computed value.
    return {
        "questions_total": 0,
        "supported_count": 0,
        "partial_count": 0,
        "stale_count": 0,
        "unsupported_count": 0,
        "supported_ids": [],
        "partial_ids": [],
        "stale_ids": [],
        "unsupported_ids": [],
        "gate_total": 0,
        "gate_supported_count": 0,
        "gate_gap_ids": [],
        "overclaim_count": 0,
        "overclaim_ids": [],
        "sections_count": 0,
        "verdict": "",              # per the verdict rules
    }


RESULT = build_result(load("questionnaire.json"))

if __name__ == "__main__":
    for key, value in RESULT.items():
        print(f"{key}: {value}")
