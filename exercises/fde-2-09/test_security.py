"""Grader for FDE 2.09. Run: python -m pytest test_security.py -q

Checks structure, the partitions, and the hardening
computation itself against findings.json; accuracy is
scored against SOLUTION.md with RUBRIC.md (the answer
key is deliberately not in code, so attempting the
exercise cannot leak it).
"""
import json
from pathlib import Path

import security

HERE = Path(__file__).parent

KEYS = {
    "findings_total", "risk_total", "blocked_count",
    "deferred_count", "deferred_ids", "deferred_risk",
    "fixed_count", "fixed_ids", "fixed_hours",
    "fix_budget_hours", "slack_hours", "fixed_risk",
    "risk_reduction", "backlog_count", "backlog_ids",
    "backlog_risk", "residual_risk",
    "max_residual_unblocked_risk", "pii_count",
    "secrets_count", "injection_count", "residency_count",
    "hardened", "verdict",
}


def load():
    return json.loads((HERE / "findings.json").read_text(encoding="utf-8"))


def expected():
    fs = load()
    deferred = [f for f in fs if f["blocked"]]
    rest = [f for f in fs if not f["blocked"]]
    ranked = sorted(rest, key=lambda f: (-f["risk"], f["id"]))
    cut_risk = ranked[2]["risk"]
    fixed = [f for f in ranked[:3]] + [
        f for f in ranked[3:] if f["risk"] == cut_risk]
    backlog = [f for f in rest if f not in fixed]
    return deferred, fixed, backlog


def test_all_results_present():
    assert set(security.RESULT) == KEYS


def test_risk_is_severity_times_likelihood():
    for f in load():
        assert f["risk"] == f["severity"] * f["likelihood"]


def test_partitions():
    r = security.RESULT
    fs = load()
    assert r["findings_total"] == len(fs)
    assert (r["deferred_count"] + r["fixed_count"]
            + r["backlog_count"]) == r["findings_total"]
    assert r["risk_total"] == sum(f["risk"] for f in fs)
    assert (r["fixed_risk"] + r["deferred_risk"]
            + r["backlog_risk"]) == r["risk_total"]
    assert r["residual_risk"] == r["risk_total"] - r["fixed_risk"]
    assert r["fixed_hours"] + r["slack_hours"] == r["fix_budget_hours"] == 16
    ids = r["deferred_ids"] + r["fixed_ids"] + r["backlog_ids"]
    assert sorted(ids) == sorted(f["id"] for f in fs)


def test_selection_matches_the_rules():
    deferred, fixed, backlog = expected()
    r = security.RESULT
    assert r["deferred_ids"] == sorted(f["id"] for f in deferred)
    assert r["fixed_ids"] == sorted(f["id"] for f in fixed)
    assert r["backlog_ids"] == sorted(f["id"] for f in backlog)
    assert r["fixed_hours"] == sum(f["fix_hours"] for f in fixed)
    assert r["fixed_risk"] == sum(f["risk"] for f in fixed)


def test_tie_at_the_cut_line_is_fixed_not_split():
    deferred, fixed, backlog = expected()
    r = security.RESULT
    cut_risk = sorted(
        (f for f in load() if not f["blocked"]),
        key=lambda f: (-f["risk"], f["id"]))[2]["risk"]
    tied = [f["id"] for f in backlog if f["risk"] == cut_risk]
    assert tied == []
    assert r["max_residual_unblocked_risk"] == max(
        (f["risk"] for f in backlog), default=0)


def test_blocked_findings_are_never_fixed():
    fs = {f["id"]: f for f in load()}
    r = security.RESULT
    assert all(fs[i]["blocked"] for i in r["deferred_ids"])
    assert all(not fs[i]["blocked"] for i in r["fixed_ids"] + r["backlog_ids"])


def test_categories_and_verdict():
    fs = load()
    r = security.RESULT
    for key, cat in [("pii_count", "pii"), ("secrets_count", "secrets"),
                     ("injection_count", "injection"),
                     ("residency_count", "residency")]:
        assert r[key] == sum(1 for f in fs if f["category"] == cat)
    assert r["risk_reduction"] == round(r["fixed_risk"] / r["risk_total"], 4)
    ready = r["fixed_hours"] <= 16 and r["max_residual_unblocked_risk"] < 20
    assert r["hardened"] == ready
    assert r["verdict"] == ("hardened_for_pilot" if ready else "not_hardened")
