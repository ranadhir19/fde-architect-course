# Alder Creek Health Network — the first production week of the promoted system

Fictional composite, continued from FDE 2.01 to 2.06. Written
from the engagement's notes for the observability phase of
the discharge-support project.

## Where this phase starts

FDE 2.06 ended with candidate v1.5 promoted from canary to
full traffic. The gate proved the version against 50 argued-
over cases; it said nothing about what live ward traffic
would do over a week. This phase instruments that week.
`traces.json` holds 280 traces, 40 per day for seven days.
Each trace records its day, its query topic (discharge
steps, medication, follow-up, or wound care), its graded
result, a critical-failure flag (a failure that reached
outside the ward guidance set, as defined in FDE 2.06), its
latency in milliseconds, and its cost in cents.

Two things changed during the week, and the traces are
expected to show both. The wards began routing a new class
of medication questions to the system mid-week — questions
the 50-case gate set barely covers — and those questions
run longer, because the medication guidance documents are
the longest in the corpus FDE 2.03 indexed.

## The budgets (agreed before the week started)

- **Latency budget:** a trace should complete within
  2,000 milliseconds. Breaches are counted, not averaged
  away; the mean is reported beside the breach count.
- **Cost budget:** a trace should cost at most 30 cents.
  Breaches are counted the same way.

## Windows and drift

- The **early window** is days 1 to 4; the **late window**
  is days 5 to 7. The comparison is late minus early.
- **Drift** is declared when a topic's share of traces
  rises by more than ten percentage points between the
  windows. The medication topic is the one under watch,
  because it is the topic the gate set covers thinnest.

## The alert rules (agreed before the week started)

The weekly verdict is **alert** if any one condition holds:

- **A1:** the late pass rate is at least five percentage
  points below the early pass rate.
- **A2:** drift is declared on the watched topic.
- **A3:** at least one critical failure occurred.
- **A4:** latency breaches exceed five percent of traces.

Otherwise the verdict is **healthy**. The rules are owned
by the ward lead. Changing a threshold after the week's
numbers are known requires a decision in the engagement
log and applies from the next week, never retroactively —
the FDE 2.06 gate discipline, applied to operations.

## Ownership

- The weekly report goes to the ward lead every Monday,
  whether the verdict is healthy or alert. A week with no
  report is itself reported, as a gap in the record.
- The vendor's uptime figure is not an input. Uptime says
  the system answered; the traces say what the answers
  were worth.
