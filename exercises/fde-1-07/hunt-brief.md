# Provided input — the hunt brief (fictional)

**Cedarbrook Home Goods** is the fictional Capstone 1 customer
from FDE 1.02 to FDE 1.06. Everything below is invented for this
course.

## The situation

A previous contractor built a small triage service for the
support team: it reads the morning ticket export, sorts each
ticket into a queue, and prints the queue counts. The support
lead reports one symptom, in her words:

> "Urgent returns never show up in the urgent queue. The counts
> add up — every ticket lands somewhere — but the urgent queue
> has been zero all week, and agents are finding urgent returns
> sitting in the standard queue."

No other symptom is reported. The contractor is unreachable.
There is no documentation beyond the code in `foreign_codebase/`
(three Python files, no tests, no README).

## The rules of the hunt

- **Timebox: 45 minutes.** Set a timer before you open the code.
- **Read-only.** Do not edit anything in `foreign_codebase/`.
  Your fix proposal goes in the hunt report, as prose, with the
  smallest change that would prove the diagnosis.
- **No running the service against real data** — there is none
  here, and on site there would be, which is why the habit is
  formed now: diagnose from reading, confirm from the smallest
  possible synthetic input, in that order.
- **Record your route.** The hunt report template asks what you
  opened first and why. "I read everything" is not a route.

## What you hand in

`hunt.py` (the six answers) and `hunt-report.md` (the trace, the
evidence, the proposed smallest fix, and your reading route).
