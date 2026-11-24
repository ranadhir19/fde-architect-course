"""Grader for FDE 1.07. Run: python -m pytest test_hunt.py -q

Checks structure automatically; accuracy is scored against
SOLUTION.md with RUBRIC.md (the answer key is deliberately not
in code, so attempting the exercise cannot leak it).
"""
import hunt


def test_all_six_answers_present():
    assert set(hunt.ANSWERS) == {
        "bug_file", "bug_values", "config_file",
        "data_path_env_var", "retry_limit", "data_path_functions",
    }


def test_text_answers_filled():
    for key in ["bug_file", "config_file", "data_path_env_var"]:
        assert len(hunt.ANSWERS[key].strip()) >= 5, f"{key}: too short"


def test_bug_values_are_a_mismatched_pair():
    a, b = hunt.ANSWERS["bug_values"]
    assert a and b and a != b, "the two values must differ — that is the bug"


def test_retry_limit_is_a_positive_int():
    assert isinstance(hunt.ANSWERS["retry_limit"], int)
    assert hunt.ANSWERS["retry_limit"] > 0


def test_data_path_has_at_least_four_steps():
    steps = hunt.ANSWERS["data_path_functions"]
    assert len(steps) >= 4, "trace the ticket through at least four functions"
    assert all(isinstance(s, str) and s.strip() for s in steps)
