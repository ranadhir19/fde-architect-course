# FDE 2.08 Exercise — Prototype at deployment speed: the 48-hour handoff brief

**Topic:** Prototyping at deployment speed (Layer 4).
**Part (d) of FDE 2.08.**
Attempt this before watching the tutorial half of the lesson.
**Prerequisite:** FDE 2.07 — the first production week
ended in an alert. This exercise is the prototype sprint
that follows it, at the same customer.

## The task

Read `prototype-design.md` first. It describes the twelve
features the room asked for, the sixteen prototype hours
available inside the 48-hour window, and the selection
rules the ward lead agreed before the sprint started:
defer what is blocked or un-fakeable safety work, fake
what is safety-critical and fakeable, build the rest for
real in value-per-hour order while the hours last.

Then build the sprint plan the customer can check
without you:

1. `prototype.py`, built from `prototype_starter.py`:
   read the twelve requests in `requests.json`, apply
   the selection rules exactly as written, and fill the
   `RESULT` dictionary the grader checks. Every value
   must be computed from the file at run time.
2. `DEMO.md` from `report-template.md`: the demo plan you
   would hand the ward lead — what is built, what is
   faked and labelled faked, what is deferred or cut and
   why, the hours against the timebox, and the harden
   list the prototype leaves behind.

The design rules, agreed with the customer before you build:

- **Speed is a selection problem, not a typing problem.**
  The sprint is won by what the rules leave out, in the
  open, before the clock starts — not by working the
  timebox's edges.
- **Safety is never prototyped for real.** A
  safety-critical feature is faked with a label, or it
  waits for production time and its proper review.
- **Throwaway is declared, not discovered later.** The
  prototype's code answers the demo question only. The
  harden list — not the code — is what carries forward.

## Done means

- Every RESULT value is computed from `requests.json` at
  run time — counts and ids for deferred, faked, built
  and cut requests, the hours and the slack, the demo
  value carried and its coverage, the harden list, and
  the demo-ready verdict.
- The partitions hold: deferred plus faked plus built
  plus cut is the twelve requests; prototype hours plus
  slack is the sixteen-hour timebox.
- The demo plan labels every shown feature built or
  faked, and names every absent feature deferred or cut
  with its rule.
- Graded with `RUBRIC.md`. `SOLUTION.md` is the reference
  answer, released after the attempt window.

## The habit this exercise is really testing

- A prototype is a question with a deadline. Building the
  most impressive thing in 48 hours and learning nothing
  decidable from the demo is the expensive failure.
- The features you refuse, fake honestly, or defer with a
  named reason are the evidence that the speed was
  judgement, not panic.
