# Alder Creek Health Network — Supplier security questionnaire

Capstone 2 copy, issued blank. Complete every section. Each
answer must name its evidence artefact (a file in your
submission, a log sample, a listing, a test result) — answers
without artefacts are graded as unanswered. This questionnaire
is a fictional teaching artefact modelling real hospital
supplier reviews.

## A. Data inventory and flow

1. List every store your system creates that holds network
   data, including working copies, caches, and eval sets.
   *Evidence:* the inventory itself, with locations.
2. Draw the data flow from the file drop to the drafted
   summary. Name every component that touches note text.
   *Evidence:* the diagram or its written equivalent.
3. Which data leaves the network's home region, if any, at
   any point in the pipeline? *Evidence:* configuration or
   deployment listing.

## B. Access control

4. Which roles can read patient-identifiable data, and how
   is ward scoping enforced? *Evidence:* the permission
   configuration or the code that computes exposure.
5. Is bulk export possible through any interface you expose?
   If yes, who approved it? *Evidence:* the operation list.
6. How are service credentials issued, stored, and rotated?
   *Evidence:* the secrets handling description, with no
   secret values included.

## C. Logging and observability

7. What does your trace log record for one processed note?
   *Evidence:* one real (synthetic-data) log sample.
8. Can any log line contain a patient reference or note
   text? Answer for every logger in the system, not the
   main one. *Evidence:* the log sample set.
9. Who can read the logs, and how long are they kept?
   *Evidence:* retention configuration.

## D. Evaluation data

10. Where does your eval set live, and what identifiers does
    it contain? *Evidence:* the eval set's location listing
    and field list.
11. How was the eval set labelled, and who adjudicated
    disagreements? *Evidence:* the eval report.
12. What is your PHI-safety failure taxonomy, and what does
    the gate do when a critical failure appears?
    *Evidence:* the taxonomy and one gate result.

## E. Retention and deletion

13. How are drafts and working copies deleted at 30 days,
    and how would the network verify a deletion happened?
    *Evidence:* the deletion mechanism and one deletion
    record.
14. What happens to network data in your system if the
    engagement ends tomorrow? *Evidence:* the exit procedure.

## F. Incident readiness

15. Who is notified, in what order, when PID exposure is
    suspected — and within what time? *Evidence:* the
    incident runbook.
16. What is your containment step for a leak found in logs,
    specifically? *Evidence:* the runbook section.
17. Have you run an incident drill against this system? What
    did it find? *Evidence:* the drill record or postmortem.

## Declaration

18. Name the controls in the data-handling policy (v3.1)
    that your system does **not** yet meet, if any. An
    honest gap declared here is graded as a control working.
    A gap discovered by the reviewer instead is graded as
    two controls failing.
