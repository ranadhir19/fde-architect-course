"""Grader for FDE 2.05. Run: python -m pytest test_eval.py -q

Checks structure, the partitions, and the inter-rater
computation itself against cases.json; accuracy is scored
against SOLUTION.md with RUBRIC.md (the answer key is
deliberately not in code, so attempting the exercise cannot
leak it).
"""
import json
from pathlib import Path

import evalset

HERE = Path(__file__).parent

KEYS = {
    "cases_total", "gold_pass", "gold_fail",
    "cat_grounded", "cat_omission", "cat_fabrication",
    "cat_boundary", "cat_stale_guidance",
    "rater_agreements", "rater_disagreements",
    "rater_agreement_rate", "cohens_kappa",
    "judge_correct", "judge_accuracy",
    "judge_false_pass", "judge_false_fail",
}


def test_all_results_present():
    assert set(evalset.RESULT) == KEYS


def test_gold_partition():
    r = evalset.RESULT
    assert r["gold_pass"] + r["gold_fail"] == r["cases_total"]


def test_taxonomy_partition():
    r = evalset.RESULT
    cats = (r["cat_grounded"] + r["cat_omission"] + r["cat_fabrication"]
            + r["cat_boundary"] + r["cat_stale_guidance"])
    assert cats == r["cases_total"]


def test_rater_partition():
    r = evalset.RESULT
    assert r["rater_agreements"] + r["rater_disagreements"] == r["cases_total"]


def test_judge_partition():
    r = evalset.RESULT
    parts = r["judge_correct"] + r["judge_false_pass"] + r["judge_false_fail"]
    assert parts == r["cases_total"]


def test_kappa_matches_the_file():
    # Recompute agreement and kappa from cases.json: the
    # reported values must be the file's values, computed by
    # the formula in the starter, not typed in.
    cases = json.loads((HERE / "cases.json").read_text(encoding="utf-8"))
    n = len(cases)
    agree = sum(1 for c in cases if c["rater_a"] == c["rater_b"])
    po = agree / n
    pa = sum(1 for c in cases if c["rater_a"] == "pass") / n
    pb = sum(1 for c in cases if c["rater_b"] == "pass") / n
    pe = pa * pb + (1 - pa) * (1 - pb)
    kappa = round((po - pe) / (1 - pe), 4)
    assert evalset.RESULT["rater_agreements"] == agree
    assert evalset.RESULT["cohens_kappa"] == kappa
