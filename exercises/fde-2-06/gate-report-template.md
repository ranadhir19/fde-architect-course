# GATE.md — regression gate and promotion report (template)

Hand this to the ward lead. Every number comes from your own
run of `gate.py` over `runs.json` and `canary.json` as
delivered.

## The baseline

- The set: (total) gold cases, graded as in FDE 2.05.
- Baseline (v1, in production): pass (n), fail (n), of which
  critical failures (n). One line on what the baseline's
  failures are the known price of.

## Candidate v1.4

- Pass (n), fail (n), pass delta against baseline (n).
- Largest category failure increase (n) — name the category
  or categories that produced it.
- Critical failures (n), delta against baseline (n).
- Verdict, rule by rule: G1 (result), G2 (result), G3
  (result). The gate verdict follows; name every rule the
  candidate failed and by how much.

## Candidate v1.5

- Pass (n), fail (n), pass delta against baseline (n).
- Largest category failure increase (n).
- Critical failures (n), delta against baseline (n).
- Verdict, rule by rule, as above.

## Shadow, canary, promotion (passing candidate only)

- Shadow: records (n), pass (n), pass rate.
- Canary: records (n), pass (n), pass rate, critical
  failures (n), worst block of 20 (rate).
- Kill switch: triggered or not, with the two tests stated.
- Promotion verdict, with each of its three conditions
  checked against the numbers above.

## What this gate cannot yet say

- One line each: what a 50-case gate cannot detect (small
  regressions inside a category, failures the set has no
  case for), and what FDE 2.07's production observability
  must watch that a pre-deployment gate never sees.
