"""Starter for FDE 1.07. Copy to hunt.py and fill in ANSWERS.

Run the structural grader: python -m pytest test_hunt.py -q
Accuracy is scored against SOLUTION.md with RUBRIC.md (the answer
key is deliberately not in code, so attempting cannot leak it).
"""

ANSWERS = {
    # file where the bug's decisive comparison lives
    "bug_file": "",
    # the two mismatched priority values, exactly as written in
    # the code and the export: (value in the comparison, value
    # the export writes)
    "bug_values": ("", ""),
    # file that decides configuration
    "config_file": "",
    # environment variable that overrides the ticket data path
    "data_path_env_var": "",
    # retry limit the code will actually use (an int)
    "retry_limit": None,
    # the data path in order: function names from entry point
    # to queue count, e.g. ["main", "...", "..."]
    "data_path_functions": [],
}
