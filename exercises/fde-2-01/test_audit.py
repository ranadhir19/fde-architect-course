"""Grader for FDE 2.01. Run: python -m pytest test_audit.py -q

Checks structure automatically; accuracy is scored against
SOLUTION.md with RUBRIC.md (the answer key is deliberately not
in code, so attempting the exercise cannot leak it).
"""
import audit

KEYS = {
    "rows", "duplicate_extra_rows", "empty_discharge_date",
    "empty_diagnosis_code", "follow_up_silent_nulls",
    "iso_admit_dates", "us_admit_dates", "first_us_format_row",
    "first_undotted_diagnosis_row", "status_distinct_raw",
    "ward_distinct_raw",
}


def test_all_findings_present():
    assert set(audit.FINDINGS) == KEYS


def test_all_findings_are_positive_ints():
    for key in KEYS:
        value = audit.FINDINGS[key]
        assert isinstance(value, int) and value > 0, f"{key}: {value!r}"


def test_date_formats_partition_the_rows():
    f = audit.FINDINGS
    assert f["iso_admit_dates"] + f["us_admit_dates"] == f["rows"]


def test_drift_rows_are_inside_the_file():
    f = audit.FINDINGS
    assert 1 < f["first_us_format_row"] <= f["rows"]
    assert 1 < f["first_undotted_diagnosis_row"] <= f["rows"]


def test_duplicates_are_a_minority():
    f = audit.FINDINGS
    assert f["duplicate_extra_rows"] < f["rows"] // 10
