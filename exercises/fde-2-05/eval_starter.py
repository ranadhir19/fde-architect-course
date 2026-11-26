"""Starter for FDE 2.05. Copy to evalset.py and complete it.

Compute every value from the delivered file at run time.
The grader imports RESULT from your evalset.py; accuracy is
scored against SOLUTION.md with RUBRIC.md.

The design is specified exactly, so numbers reproduce:
  - Gold split and taxonomy counts come straight from the
    cases: gold is "pass" or "fail"; category is one of the
    five taxonomy values.
  - Inter-rater agreement: a case agrees when rater_a and
    rater_b gave the same grade. Agreement rate is
    agreements / cases, rounded to 4 decimal places.
  - Cohen's kappa: kappa = (po - pe) / (1 - pe), where po is
    the observed agreement rate (unrounded) and pe is the
    agreement the raters' own marginals predict by chance:
    pe = pa_pass * pb_pass + pa_fail * pb_fail, with pa_pass
    the share of cases rater_a passed, and so on. Round the
    final kappa to 4 decimal places.
  - Judge errors are counted against gold, by direction:
    false pass = judge said "pass" and gold is "fail";
    false fail = judge said "fail" and gold is "pass".
"""
import json
from pathlib import Path

HERE = Path(__file__).parent
CASES = HERE / "cases.json"


def load_cases():
    return json.loads(CASES.read_text(encoding="utf-8"))


def build_result(cases):
    # Replace each placeholder with a computed value.
    return {
        "cases_total": 0,
        "gold_pass": 0,
        "gold_fail": 0,
        "cat_grounded": 0,
        "cat_omission": 0,
        "cat_fabrication": 0,
        "cat_boundary": 0,
        "cat_stale_guidance": 0,
        "rater_agreements": 0,
        "rater_disagreements": 0,
        "rater_agreement_rate": 0.0,  # rounded to 4 dp
        "cohens_kappa": 0.0,          # rounded to 4 dp
        "judge_correct": 0,
        "judge_accuracy": 0.0,        # rounded to 4 dp
        "judge_false_pass": 0,        # judge pass, gold fail
        "judge_false_fail": 0,        # judge fail, gold pass
    }


RESULT = build_result(load_cases())

if __name__ == "__main__":
    for key, value in RESULT.items():
        print(f"{key}: {value}")
