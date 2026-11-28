"""Grader for FDE 3.01. Run: python -m pytest test_topology.py -q

Checks structure, the partitions, and the placement
computation itself against components.json; accuracy is
scored against SOLUTION.md with RUBRIC.md (the answer
key is deliberately not in code, so attempting the
exercise cannot leak it).
"""
import json
from pathlib import Path

import topology

HERE = Path(__file__).parent

KEYS = {
    "components_total",
    "cloud_as_is_count", "cloud_adapt_count", "cloud_blocked_count",
    "cloud_adapt_ids", "cloud_blocked_ids", "cloud_adapt_hours",
    "cloud_blocked_core_count", "cloud_verdict",
    "onprem_as_is_count", "onprem_adapt_count", "onprem_blocked_count",
    "onprem_adapt_ids", "onprem_blocked_ids", "onprem_adapt_hours",
    "onprem_blocked_core_count", "onprem_verdict",
    "airgap_as_is_count", "airgap_adapt_count", "airgap_blocked_count",
    "airgap_adapt_ids", "airgap_blocked_ids", "airgap_adapt_hours",
    "airgap_blocked_core_count", "airgap_verdict",
}

TOPOS = ["cloud", "onprem", "airgap"]


def load():
    return json.loads((HERE / "components.json").read_text(encoding="utf-8"))


def place(c, topo):
    if topo == "cloud":
        return "adapt" if c["sends_regulated_data_out"] else "as_is"
    if topo == "onprem":
        if not c["requires_internet"]:
            return "as_is"
        if c["self_hostable"]:
            return "adapt"
        return "blocked" if c["sends_regulated_data_out"] else "adapt"
    if not c["requires_internet"]:
        return "as_is"
    return "adapt" if c["self_hostable"] else "blocked"


def expected(topo):
    groups = {"as_is": [], "adapt": [], "blocked": []}
    for c in load():
        groups[place(c, topo)].append(c)
    return groups


def verdict(blocked):
    if not blocked:
        return "feasible"
    if any(c["is_core"] for c in blocked):
        return "not_feasible_as_designed"
    return "feasible_with_cuts"


def test_all_results_present():
    assert set(topology.RESULT) == KEYS


def test_partitions_hold_per_topology():
    r = topology.RESULT
    comps = load()
    assert r["components_total"] == len(comps)
    for topo in TOPOS:
        total = (r[f"{topo}_as_is_count"] + r[f"{topo}_adapt_count"]
                 + r[f"{topo}_blocked_count"])
        assert total == r["components_total"], topo


def test_placements_match_the_rules():
    r = topology.RESULT
    for topo in TOPOS:
        groups = expected(topo)
        assert r[f"{topo}_adapt_ids"] == sorted(
            c["id"] for c in groups["adapt"]), topo
        assert r[f"{topo}_blocked_ids"] == sorted(
            c["id"] for c in groups["blocked"]), topo
        assert r[f"{topo}_as_is_count"] == len(groups["as_is"]), topo
        assert r[f"{topo}_adapt_count"] == len(groups["adapt"]), topo
        assert r[f"{topo}_blocked_count"] == len(groups["blocked"]), topo


def test_hours_and_core_counts():
    r = topology.RESULT
    for topo in TOPOS:
        groups = expected(topo)
        assert r[f"{topo}_adapt_hours"] == sum(
            c["adapt_hours"] for c in groups["adapt"]), topo
        assert r[f"{topo}_blocked_core_count"] == sum(
            1 for c in groups["blocked"] if c["is_core"]), topo


def test_cloud_blocks_nothing():
    r = topology.RESULT
    assert r["cloud_blocked_count"] == 0
    assert r["cloud_blocked_ids"] == []
    assert r["cloud_verdict"] == "feasible"


def test_verdicts_follow_the_rules():
    r = topology.RESULT
    for topo in TOPOS:
        groups = expected(topo)
        assert r[f"{topo}_verdict"] == verdict(groups["blocked"]), topo


def test_airgap_blocks_at_least_the_onprem_blocks():
    r = topology.RESULT
    assert set(r["onprem_blocked_ids"]) <= set(r["airgap_blocked_ids"])
    assert r["airgap_blocked_count"] >= r["onprem_blocked_count"]
