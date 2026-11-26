# FDE 2.08 Rubric — 24 points

| Section | Points | What earns them |
|---|---|---|
| Computed plan | 8 | All twenty-four RESULT values computed from `requests.json` and matching SOLUTION.md exactly (counts and sorted ids for deferred, faked, built and cut requests, hours, slack, value carried and coverage, harden list, verdict). Hand-typed numbers score zero here even if correct — the program is the artefact. |
| Selection by the rules | 5 | The demo plan applies the rules in their stated order — deferral before faking, faking before building, value-per-hour ranking with the id tie-break — and can show, for any request, which rule placed it where it is. |
| Safety and honesty of fakes | 4 | No safety-critical feature is built for real; every faked feature is labelled faked in the demo plan, with what the fake does and does not prove stated beside it. |
| Timebox discipline | 4 | The plan fits the sixteen hours with its slack named, and no request is re-scored, re-estimated, or quietly dropped mid-sprint to make the plan fit after the fact. |
| Harden list and throwaway call | 3 | Every prototype item with a harden note appears on the harden list with its note carried forward, and the plan declares the prototype throwaway — what carries forward is the learning and the list, not the code. |

**Automatic fails:** building a safety-critical feature
for real inside the timebox; showing a faked feature
without its label; editing `requests.json` or its value
scores; claiming the prototype code is production-ready.
