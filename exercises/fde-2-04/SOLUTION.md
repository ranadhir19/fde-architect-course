# FDE 2.04 Reference solution

Released after the attempt window. All counts are of the files
as delivered and are reproduced by the reference `server.py`,
built exactly to the starter's specification.

## The counts

| Finding | Value |
|---|---|
| operations_total | 12 |
| operations_exposed | 3 |
| operations_withheld | 9 |
| requests_evaluated | 24 |
| requests_allowed | 9 |
| requests_denied | 15 |
| denied_not_exposed | 7 |
| denied_role | 5 |
| denied_bad_args | 3 |

## The exposed three, and why these three

- `get_ward_bed_board` — read, internal: aggregate bed counts
  by ward. No patient detail exists in its output to leak.
- `get_discharge_checklist` — read, internal: the standard
  checklist text. Guidance, already written for every ward.
- `check_followup_availability` — read, internal: open slots
  by clinic and date — counts and times, no patient names.

Each passes both halves of the rule. That is the whole of the
argument for each of them, and it is enough: the report does
not add "and they are useful" as a permission reason, because
usefulness is why the other nine were proposed too.

## The withheld nine, grouped by reason

- **Patient-data reads (2):** `get_patient_record` and
  `download_discharge_extract`. Read-only, and withheld
  anyway: a read is a disclosure, and the extract is a
  disclosure of a month of discharges at once. The extract is
  the one operation anyone argued for in the scoping meeting;
  the compliance veto held, and the log records it.
- **Writes (6):** `update_discharge_date`,
  `record_medication_change`, `approve_billing_charge`,
  `send_patient_email`, `merge_patient_records`,
  `delete_ward_note`. An agent that can write to a record
  system on the strength of text it has read is a different
  risk class from one that can look things up — and
  `merge_patient_records` cannot be undone from the legacy
  interface, so a mistaken call is a permanent record event.
- **Administration (1):** `grant_system_access`. Its data
  class is internal; its kind decides first. A tool that can
  widen access can retire every other withholding decision
  on this page, which is exactly why it is never agent-held.

## What the request counts mean

- **Denied is the normal outcome, by design.** 15 of 24 pilot
  calls are refused. Seven reach for tools that are not
  exposed — including one name, `get_lab_results`, that is
  not in the registry at all, which the server treats
  identically: not exposed is not exposed, and the caller
  learns nothing about what does exist.
- **Role denials (5) are the second layer working.** Booking
  clerks and bed managers reach for exposed tools outside
  their roles, and one call arrives under a role,
  `external_auditor`, that no exposed tool allows. The server
  refuses before it ever looks at the arguments.
- **Bad-argument denials (3) are the smallest count, and
  that ordering is the point.** Only a call that has passed
  exposure and role is told what it is missing.

## Certification

- Certified for the pilot: the three exposed operations,
  under the registry's roles as delivered, for ward staff,
  bed managers, and booking clerks as listed per tool.
- Refused, for now: every withheld operation, and any change
  to the exposed set made by configuration rather than by a
  new decision in the engagement log. The open risk carried
  in the report: the registry's role assignments came from
  the vendor's default template and have never been reviewed
  by the network — the rule is verified; the roles are
  trusted, exactly the shape of risk FDE 2.03 left behind on
  access levels, one layer up.
