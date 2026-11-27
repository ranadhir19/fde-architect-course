# FDE 2.09 Exercise — Security & privacy while building: threat-model the running build

**Topic:** Security & privacy while building (Layer 6).
**Part (d) of FDE 2.09.**
Attempt this before watching the tutorial half of the lesson.
**Prerequisite:** FDE 2.08 — the prototype sprint ended
demo-ready. This exercise reviews the whole running
build the sprint left behind, at the same customer.

## The task

Read `threat-model.md` first. It describes the fourteen
findings the security review produced, the sixteen-hour
hardening window, and the fix rules the ward lead and
the customer's security reviewer agreed before the
ranking was computed: blocked findings are deferred,
the rest are ranked by risk, the top three are fixed —
and a tie at the cut line is fixed, not split.

Then build the hardening plan the customer can check
without you:

1. `security.py`, built from `security_starter.py`:
   read the fourteen findings in `findings.json`, apply
   the fix rules exactly as written, and fill the
   `RESULT` dictionary the grader checks. Every value
   must be computed from the file at run time.
2. `HARDENING.md` from `report-template.md`: the plan
   you would hand the security reviewer — what is fixed
   and how, what is deferred and whose action unblocks
   it, what sits in the backlog with its risk, and the
   residual risk the pilot decision is being made under.

The design rules, agreed with the customer before you build:

- **Risk is a product, not an adjective.** Severity
  times likelihood, computed the same way for every
  finding, frozen when the finding was filed.
- **Blocked means deferred, not worked around.** A fix
  that needs a customer signature or a customer system
  waits for it, named and owned. Building a substitute
  in the meantime is how a prototype's stand-in screen
  becomes a production control nobody reviewed.
- **A tie at the cut line is fixed, not split.** The
  ranking's tie-break orders the work; it does not
  declare one equally-scored finding safe to leave.

## Done means

- Every RESULT value is computed from `findings.json` at
  run time — counts and ids for deferred, fixed and
  backlog findings, the risk in each partition, the fix
  hours against the budget and the slack, the risk
  reduction, the residual and maximum residual risks,
  the category counts, and the verdict.
- The partitions hold: deferred plus fixed plus backlog
  is the fourteen findings; fixed risk plus deferred
  risk plus backlog risk is the total risk; fix hours
  plus slack is the sixteen-hour budget.
- The hardening plan names, for every deferred finding,
  the customer action and owner that unblocks it, and
  prints the residual risk beside the verdict.
- Graded with `RUBRIC.md`. `SOLUTION.md` is the reference
  answer, released after the attempt window.

## The habit this exercise is really testing

- A threat model is a ranking with owners, not a list of
  worries. The findings you defer with a named blocker,
  and the residual risk you print next to your own
  verdict, are the evidence the review was real.
- The most dangerous finding in a customer build is
  rarely exotic. It is the ordinary one — a key in a
  repo, identifiers in a log — that everyone walked past
  because the demo worked.
