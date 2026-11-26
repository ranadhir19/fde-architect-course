# FDE 2.04 Exercise — Expose three operations, withhold the rest

**Topic:** Agents and MCP in customer systems (Layer 4).
**Part (d) of FDE 2.04.**
Attempt this before watching the tutorial half of the lesson.
**Prerequisite:** FDE 2.03 (LLM application engineering for one
customer) — the retrieval system you built there is read-only by
design; this exercise is where other operations ask for access,
and where the answer is mostly no.

## The task

Read `systems-and-operations.md` first. It describes the Alder
Creek Health Network legacy record system as the agent project
found it: twelve operations the system can perform, and a
proposal — from the vendor, not from the customer — to expose
all twelve to an agent over an MCP-style tool interface.

Then build the server that exposes three of them:

1. `server.py`, built from `server_starter.py`: apply the
   exposure rule from the brief to `operations.json`, then
   evaluate every call in `requests.json` against the exposed
   set in the decision order the starter specifies, and fill
   the `RESULT` dictionary the grader checks. Every value must
   be computed from the files at run time.
2. `SERVER.md` from `server-report-template.md`: the report you
   would hand the ward lead and the compliance contact together
   — the three exposed tools with the rule that admitted them,
   the nine withheld operations grouped by the reason each was
   withheld, and the denial counts from your own run.

The exposure rule, agreed with the customer before you build:
**an operation is exposed only if it is read-only and its data
class is internal.** Both halves are the rule. A read over
patient detail is still a disclosure channel; a write over
internal data is still a write. Three of the twelve operations
meet the rule. The other nine are not backlog — they are the
withholding decision, and the report defends each group.

## Done means

- The exposed set is exactly the operations that meet the rule,
  computed from `operations.json` at run time — never typed in
  as a list of names.
- Every request is evaluated in the stated order: not exposed
  first, then caller role, then required arguments. A request
  is counted once, under the first check it fails.
- Denied calls are counted by reason, and the three denial
  counts sum to the denied total.
- The report groups the nine withheld operations by reason
  (writes, patient-data reads, bulk export, administration)
  and states what would have to change — a new decision by a
  named owner — before any of them is reconsidered.
- Graded with `RUBRIC.md`. `SOLUTION.md` is the reference
  answer, released after the attempt window.

## The habit this exercise is really testing

- An agent's tool list is a permission decision, not a feature
  list. Every exposed operation is attack surface and accident
  surface the customer now carries; every withheld one costs a
  conversation, once, instead of an incident, later.
- Permission scoping is applied in layers, in order: what
  exists for the agent at all, who may call it, and whether
  this call is well formed. A server that checks arguments
  before exposure has already told an attacker which tools
  exist.
