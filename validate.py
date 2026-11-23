#!/usr/bin/env python3
"""Repo harness for fde-architect-course.

Checks the delivered structure, not sidecar claims:
  1. Required top-level files exist and are non-empty.
  2. Every topic in CURRICULUM.md appears exactly once, in order.
  3. Every capstone brief carries the required sections
     (customer, brief, deliverables, rubric).
  4. No placeholder markers left in shipped markdown.

Exit 0 = green. Run before every push.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
failures = []


def check(cond, msg):
    if not cond:
        failures.append(msg)


for name in ["README.md", "LICENSE", "CURRICULUM.md", "BENCHMARK.md"]:
    p = ROOT / name
    check(p.exists() and p.stat().st_size > 0, f"missing or empty: {name}")

curr = (ROOT / "CURRICULUM.md").read_text(encoding="utf-8")
topics = re.findall(r"FDE (\d\.\d\d)", curr)
check(len(topics) == 26, f"expected 26 topics in CURRICULUM.md, found {len(topics)}")
check(topics == sorted(topics), "topics out of order in CURRICULUM.md")
check(len(set(topics)) == len(topics), "duplicate topics in CURRICULUM.md")

cap_dir = ROOT / "capstones"
briefs = sorted(cap_dir.glob("0*.md"))
check(len(briefs) == 5, f"expected 5 capstone briefs, found {len(briefs)}")
for b in briefs:
    text = b.read_text(encoding="utf-8").lower()
    for section in ["customer", "deliverables", "rubric"]:
        check(section in text, f"{b.name}: missing section '{section}'")
    check("change injection" in text or "twist" in text,
          f"{b.name}: no change injection / twist")

for md in ROOT.rglob("*.md"):
    text = md.read_text(encoding="utf-8")
    check("TODO-PLACEHOLDER" not in text, f"{md.relative_to(ROOT)}: placeholder left")

if failures:
    print("VALIDATE: FAIL")
    for f in failures:
        print(" -", f)
    sys.exit(1)
print(f"VALIDATE: PASS ({len(topics)} topics, {len(briefs)} capstones)")
