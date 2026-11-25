"""Starter for FDE 2.01. Copy to audit.py and complete it.

Compute every value from discharges.csv at run time. The grader
imports FINDINGS from your audit.py; accuracy is scored against
SOLUTION.md with RUBRIC.md.
"""
import csv
from pathlib import Path

DATA = Path(__file__).with_name("discharges.csv")

SILENT_NULL_TOKENS = {"", "N/A", "null", "-"}


def load_rows():
    with DATA.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def build_findings(rows):
    # Replace each placeholder with a computed value.
    return {
        "rows": 0,
        "duplicate_extra_rows": 0,   # rows identical on every field except discharge_id, beyond the first copy
        "empty_discharge_date": 0,
        "empty_diagnosis_code": 0,
        "follow_up_silent_nulls": 0,  # follow_up values in SILENT_NULL_TOKENS
        "iso_admit_dates": 0,         # admit_date in YYYY-MM-DD form
        "us_admit_dates": 0,          # admit_date in MM/DD/YYYY form
        "first_us_format_row": 0,     # 1-based data row of the first non-ISO admit_date
        "first_undotted_diagnosis_row": 0,  # 1-based data row of the first diagnosis_code with no dot
        "status_distinct_raw": 0,     # distinct raw status spellings
        "ward_distinct_raw": 0,       # distinct raw ward spellings
    }


FINDINGS = build_findings(load_rows())

if __name__ == "__main__":
    for key, value in FINDINGS.items():
        print(f"{key}: {value}")
