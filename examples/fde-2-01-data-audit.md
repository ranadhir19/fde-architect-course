# Worked example — FDE 2.01: a data audit that stopped a build for one day and saved it, annotated

Referenced by the FDE 2.01 learning session. The customer is
fictional; the audit is a composite written for this course.
Annotations in brackets name the move being made. This example
uses a different customer from the exercise, on purpose: copy
the moves, not the words.

> **AUDIT.md (excerpt) — Larkspur Freight job-history export**
>
> **The file as delivered.** 4,812 rows, one CSV, exported from
> the depot system by the operations analyst "the way we always
> send it". Stated coverage: all completed jobs, last two years.
> Verified coverage: the export stops eleven weeks ago — the
> analyst's saved query still ends at the date it was first
> written. Every recency claim in the engagement plan was
> quietly eleven weeks stale.
>
> *[The first audit finding is rarely in the data. It is in the
> gap between what the file claims to be and what it is. Check
> coverage — first row, last row, row count against a number
> the customer already trusts — before you check a single
> value.]*
>
> **Defect register (excerpt).**
>
> | Defect | Count | Class |
> |---|---|---|
> | Jobs present twice, second copy with the depot suffix dropped from the job id | 211 | blocks |
> | `completed_at` empty, completion recorded in the free-text notes instead | 96 | shapes |
> | Weight unit changes from kilograms to pounds at the row where the partner depot's feed joins | 1 boundary | blocks |
>
> *[The unit change is one boundary and zero ambiguity, and it
> outranks every other row in the register: a model trained
> across that boundary learns that partner-depot jobs weigh
> 2.2 times more. Count is not severity. The audit ranks by
> what the defect does to the build, not by how often it
> occurs.]*
>
> **Ownership.** The export is owned by the operations analyst;
> the query behind it is owned by nobody — it predates him. The
> partner feed's unit is owned by the partner depot's IT, who
> confirmed in writing, the same day, that pounds is their
> permanent convention.
>
> *[One question, sent to the named owner, answered in writing
> the same day. That is what an ownership section is for: not
> an org chart, a list of questions that now have names
> attached.]*
>
> **The refusal.** No training run on this export until the
> analyst re-runs the query with the end date removed and the
> job-id duplicates resolved at source. One day. The build
> started a day late and on data that deserved it.

**The lesson:** the audit is not a cleaning pass. Cleaning
produces a tidy file and no memory; an audit produces a
register, a set of named owners, and — where it matters — a
refusal with a date on it. The build inherits all three.
