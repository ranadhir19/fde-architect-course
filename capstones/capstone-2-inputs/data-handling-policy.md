# Alder Creek Health Network — Data-handling policy for suppliers

Issued to all suppliers processing network data. Version 3.1.
This policy is a fictional teaching artefact written for this
capstone; it models the shape of real hospital supplier
policies. Your build is assessed against it as written.

## 1. Classification

- **Patient-identifiable data (PID):** anything that carries,
  or can be combined to recover, a patient reference — the
  `patient_ref` field, and any note text that contains one.
- **Clinical content:** clinician note text and discharge
  records, whether or not they carry an identifier.
- Everything in the Capstone 2 input pack is PID or clinical
  content. Treat it accordingly, even though it is synthetic.

## 2. Handling rules

1. **Residency.** Network data is processed and stored only
   in the network's home region. Copies outside the region —
   including evaluation sets, exports, and backups — are a
   policy breach, however convenient.
2. **Logging.** Application and trace logs must never contain
   a patient reference or any note text. Log record ids,
   counts, timings, and outcome codes only. A log that can be
   read as a patient record is a patient record, and will be
   handled as one in an incident.
3. **Access.** Access to PID is role-based and named: ward
   staff see their own ward; nobody sees every ward by
   default. Bulk export of PID is not a read operation and
   requires separate approval.
4. **Retention.** Draft summaries and working copies are
   deleted 30 days after the encounter closes. Eval sets are
   reviewed at the same interval and re-justified or deleted.
5. **Sub-processors.** Only the sub-processors named in the
   engagement contract may touch network data. A new tool in
   the pipeline is a contract conversation first and an
   install second.
6. **Secrets.** Credentials for network systems are issued per
   environment, never shared, never committed to a repository,
   and rotated on any suspicion of exposure.

## 3. Incidents

- Suspected exposure of PID is reported to the network's
  compliance team within one working day of discovery, with
  what was exposed, whose data, for how long, and what now
  contains it.
- Containment comes before root-cause analysis. A contained
  leak with an honest timeline beats a diagnosed leak that is
  still running.
- The postmortem the network expects names the control that
  should have caught it — and states whether that control
  existed, was configured, or was only ever written down.

## 4. The compliance team's standing reminder

The network has veto power over go-live, and a long memory.
An artefact that demonstrates a control (a log sample with no
identifiers, a residency listing, a deletion record) is
evidence. A paragraph asserting a control is a claim. The
review grades evidence.
