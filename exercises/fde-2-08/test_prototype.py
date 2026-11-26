"""Grader for FDE 2.08. Run: python -m pytest test_prototype.py -q

Checks structure, the partitions, and the selection
computation itself against requests.json; accuracy is
scored against SOLUTION.md with RUBRIC.md (the answer
key is deliberately not in code, so attempting the
exercise cannot leak it).
"""
import json
from pathlib import Path

import prototype

HERE = Path(__file__).parent

KEYS = {
    "requests_total", "value_total", "blocked_count",
    "deferred_count", "deferred_ids", "fake_count",
    "fake_ids", "fake_hours", "real_count", "real_ids",
    "real_hours", "cut_count", "cut_ids",
    "prototype_items", "prototype_hours", "timebox_hours",
    "slack_hours", "prototype_value", "value_coverage",
    "harden_count", "harden_ids", "demo_ready", "verdict",
}


def load():
    return json.loads((HERE / "requests.json").read_text(encoding="utf-8"))


def expected():
    reqs = load()
    deferred = [r for r in reqs
                if r["blocked"] or (r["safety"] and not r["fakeable"])]
    fake = [r for r in reqs
            if not r["blocked"] and r["safety"] and r["fakeable"]]
    rest = [r for r in reqs if r not in deferred and r not in fake]
    ranked = sorted(rest, key=lambda r: (-(r["value"] / r["proto_hours"]), r["id"]))
    budget = 16 - len(fake) * 1
    real, cut, used = [], [], 0
    for r in ranked:
        if used + r["proto_hours"] <= budget:
            real.append(r)
            used += r["proto_hours"]
        else:
            cut.append(r)
    return deferred, fake, real, cut, used


def test_all_results_present():
    assert set(prototype.RESULT) == KEYS


def test_partitions():
    r = prototype.RESULT
    reqs = load()
    assert r["requests_total"] == len(reqs)
    assert (r["deferred_count"] + r["fake_count"]
            + r["real_count"] + r["cut_count"]) == r["requests_total"]
    assert r["prototype_items"] == r["fake_count"] + r["real_count"]
    assert r["prototype_hours"] + r["slack_hours"] == r["timebox_hours"] == 16
    ids = (r["deferred_ids"] + r["fake_ids"]
           + r["real_ids"] + r["cut_ids"])
    assert sorted(ids) == sorted(x["id"] for x in reqs)


def test_selection_matches_the_rules():
    deferred, fake, real, cut, used = expected()
    r = prototype.RESULT
    assert r["deferred_ids"] == sorted(x["id"] for x in deferred)
    assert r["fake_ids"] == sorted(x["id"] for x in fake)
    assert r["real_ids"] == sorted(x["id"] for x in real)
    assert r["cut_ids"] == sorted(x["id"] for x in cut)
    assert r["real_hours"] == used
    assert r["fake_hours"] == len(fake)


def test_no_safety_feature_is_built_for_real():
    reqs = {x["id"]: x for x in load()}
    r = prototype.RESULT
    assert all(not reqs[i]["safety"] for i in r["real_ids"])
    assert all(not reqs[i]["blocked"] for i in r["real_ids"] + r["fake_ids"])


def test_value_and_harden_match_the_file():
    deferred, fake, real, cut, used = expected()
    proto_items = real + fake
    r = prototype.RESULT
    assert r["prototype_value"] == sum(x["value"] for x in proto_items)
    assert r["value_coverage"] == round(
        r["prototype_value"] / r["value_total"], 4)
    harden = sorted(x["id"] for x in proto_items if x["harden_note"])
    assert r["harden_ids"] == harden
    assert r["harden_count"] == len(harden)


def test_verdict_follows_the_rule():
    r = prototype.RESULT
    ready = r["prototype_value"] >= 20 and r["prototype_hours"] <= 16
    assert r["demo_ready"] == ready
    assert r["verdict"] == ("demo_ready" if ready else "not_ready")
