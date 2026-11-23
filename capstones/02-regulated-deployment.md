# Capstone 2 — Regulated deployment

**The customer.** A regional health network (fictional composite). They want an
LLM assistant that drafts discharge-summary first passes from clinician notes.
PHI is in scope. Their compliance team has veto power and a long memory.

**The brief.** Integrate with the provided legacy record system (no modern API:
scheduled file drops plus a read-only database view), build the drafting
workflow, and get it through a simulated security review.

**Provided inputs.** Synthetic clinician notes and discharge records, the file
-drop stand-in, the network's security questionnaire, and their data-handling
policy.

**Change injection.** Mid-engagement, a neighbouring department's tool leaks
PHI in an unrelated incident. Your engagement inherits the scrutiny: an
incident-response drill is run against *your* system, including a planted
leak path you must find, contain, and write up.

**Deliverables.** The running system; the ingestion + reconciliation pipeline;
a customer-specific eval set with a PHI-safety failure taxonomy; the completed
security questionnaire with evidence artefacts; a control-evidence pack; the
incident postmortem you would actually send the customer.

**Rubric.** Integration 20% · eval & safety 30% · compliance artefacts 25% ·
incident handling 15% · decision log 10%.
