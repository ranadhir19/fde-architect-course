# FDE 2.07 Exercise — Instrument the system: the weekly report the ward lead actually reads

**Topic:** Observability in production (Layer 5).
**Part (d) of FDE 2.07.**
Attempt this before watching the tutorial half of the lesson.
**Prerequisite:** FDE 2.06 — v1.5 passed the gate and was
promoted. This exercise covers its first full week in
production at Alder Creek.

## The task

Read `observability-design.md` first. It describes the
trace record the promoted system emits, the budgets and
alert rules agreed with the ward lead before the week
started, and the question the weekly report must answer:
is the system healthy, drifting, or quietly getting worse
in a slice the overall rate hides?

Then build the instrumentation summary the customer can
run without you:

1. `trace.py`, built from `trace_starter.py`: read the
   280 production traces in `traces.json` and fill the
   `RESULT` dictionary the grader checks. Every value
   must be computed from the file at run time.
2. `WEEK.md` from `report-template.md`: the weekly quality
   report you would hand the ward lead — the overall rate,
   the early-versus-late comparison, the topic drift, the
   budget breaches, and the alert verdict with the rules
   that produced it.

The design rules, agreed with the customer before you build:

- **Averages are reported with their slices.** The overall
  pass rate is printed, and so are the early window
  (days 1 to 4), the late window (days 5 to 7), and the
  medication topic on its own. A healthy total over a
  deteriorating slice is not a healthy report.
- **Drift is a measured change in the input mix, not a
  feeling.** The medication topic's share of traces is
  compared between the two windows; a rise of more than
  ten percentage points is drift, by the pre-agreed rule.
- **The alert verdict follows the rules, not the mood.**
  Any one of the four pre-agreed conditions raises the
  alert. Reporting the numbers and then calling the week
  healthy anyway is the failure this exercise exists to
  catch.

## Done means

- Every RESULT value is computed from `traces.json` at
  run time — counts, window rates and their delta, the
  critical count, the medication counts, share and drift,
  latency and cost means, maxima and breach counts, and
  the alert verdict.
- The partitions hold: pass plus fail is the trace total;
  early plus late records is the trace total.
- The report names which alert conditions fired and which
  did not — a verdict without its rules is an opinion.
- Graded with `RUBRIC.md`. `SOLUTION.md` is the reference
  answer, released after the attempt window.

## The habit this exercise is really testing

- Observability is not a dashboard; it is the ability to
  answer, from records, whether the system the customer
  is running today is the system that passed the gate.
- Drift in what users ask is a production event. The model
  did not change this week; the questions did — and the
  traces are the only place that shows up before the
  complaints do.
