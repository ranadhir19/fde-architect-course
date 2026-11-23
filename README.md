# Forward Deployed Engineer — The Complete Course

Companion repository for the free **Forward Deployed Engineer (FDE)** course on
[The Architect's AI Workshop](https://www.youtube.com/@TheArchitectsAIWorkshop) (YouTube).

The course teaches the FDE role from first principles — discovery, scoping, data and
legacy integration, LLM application engineering, customer-specific evals, deployment
into real customer environments (cloud VPC, on-prem, air-gapped, regulated), rollout,
and dollar-denominated value proof — through simulated customer engagements, not toy
examples.

## How this repo is organised

| Path | What it holds |
|---|---|
| `CURRICULUM.md` | The full course map: 3 phases, 26 topics, lesson numbering (FDE P.TT) |
| `BENCHMARK.md` | The 10-dimension quality scorecard this course is measured against, with published scores |
| `exercises/` | One folder per topic: starter code, tests, and (after the attempt window) reference solutions |
| `capstones/` | Five simulated customer engagements — briefs, messy inputs, deliverable rubrics |
| `examples/` | Worked examples referenced by the whiteboard and coding sessions |

## The format

Every topic is taught in four parts on the channel: a **learning session**, a
**whiteboard explanation**, a **coding session**, and a **tutorial + exercise**.
Exercises here are the fourth part: do them, don't just watch.

## Capstones

1. **Retail support, messy data** — triage automation; the returns policy changes mid-project.
2. **Regulated deployment** — an LLM workflow under PHI constraints, a security review, and a leak incident.
3. **Prove it paid** — a logistics deployment judged only on honest ROI: baseline, canary, control.
4. **The rescue** — inherit a broken, distrusted deployment; audit, decide, repair or rebuild.
5. **The take-home simulation** — a timed FDE hiring simulation: brief → build → eval → walkthrough.

Every capstone is graded on the artefacts a real FDE produces: a running system,
`DECISIONS.md`, an eval report, a rollout plan, and a 5-minute walkthrough.
A documented 70% beats an undocumented 100%.

## Licence

MIT — see `LICENSE`. Course videos are free to watch; this repo's code and briefs
are free to use for learning. Customer scenarios are fictional composites written
for this course.
