# Alder Creek Health Network — the corpus, the queries, the risk

Fictional composite, continued from FDE 2.01 and 2.02. Written
from the engagement's scoping notes for the discharge-guidance
assistant.

## What is being built, and for whom

Ward staff preparing a discharge lose time hunting the network's
own guidance: which summary instructions go home, how the
follow-up gets booked, what the medication list must be checked
against. The v1 system retrieves the relevant guidance document
from the network's corpus and shows it to the staff member, who
remains the author of anything the patient receives. Retrieval
only — no generated answers in v1, by the ward lead's decision,
recorded in the engagement log.

## The corpus (`documents.csv`)

- 48 documents: guidance across eight topics (discharge summary,
  follow-up scheduling, medication reconciliation, ward transfer,
  billing and coding, infection control, nutrition and diet,
  physiotherapy referral), five guidance documents per topic,
  plus one worked-example document per topic.
- Each document carries an `access_level`. Guidance documents
  are `internal`: written for staff, no patient detail.
- The eight worked-example documents are `restricted`: they were
  written around real cases, carry a `patient_ref` and
  identifiable detail, and exist for a small training group.
  They were included in the export the IT team sent — nobody
  filtered the export, because nobody had been asked to.

## The guardrail (this customer's risk, stated as a rule)

**A document with `access_level` equal to `restricted` is never
indexed and never returned, whatever its score.** The filter is
applied before ranking, not after: a restricted document must
not be able to displace an allowed one, and the report counts
exclusions so the filter itself is auditable.

The reason is not abstract. A worked example returned to a ward
screen carries one patient's detail into another patient's
discharge. Recall cannot see that failure; only the leak count
can.

## The queries (`queries.json`)

- 20 queries, written with ward staff from real lookups during
  discovery, each with a gold relevance set of two document ids
  agreed by two reviewers.
- The gold sets name allowed documents only — by design, because
  the restricted documents are never a correct answer, however
  similar their wording.
- One vocabulary trap is planted on purpose: the word for a
  food-and-drug reaction appears in both the medication and the
  nutrition guidance. A query about one is not a query about
  the other, and the gold sets say which.

## Access and ownership

- The corpus export is owned by the network's IT team; the
  access levels were assigned by the training group and have
  never been reviewed since. The engagement accepts them as
  given for v1 and records that as an open risk in the report.
- The gold relevance sets are owned by the ward lead. A dispute
  about a gold set is a customer conversation, not a tuning
  opportunity: you do not move the target to hit it.
