"""Grader for FDE 1.01. Run: python -m pytest test_classify.py -q

Checks structure automatically; classification accuracy is scored against
SOLUTION.md with RUBRIC.md (the answer key is deliberately not in code,
so attempting the exercise cannot leak it).
"""
import classify

def test_all_twelve_answered():
    assert len(classify.ANSWERS) == 12, "answer all 12 tasks"

def test_roles_valid_and_reasons_present():
    for tid, (role, why) in classify.ANSWERS.items():
        assert role in classify.ROLES, f"task {tid}: unknown role {role}"
        assert len(why.strip()) >= 20, f"task {tid}: defence too short"

def test_task_ids_are_1_to_12():
    assert sorted(classify.ANSWERS) == list(range(1, 13))
