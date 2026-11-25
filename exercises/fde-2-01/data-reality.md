# Data reality — Alder Creek Health Network (fictional composite)

What you are told in the kickoff meeting, written down. Some of
it is true. Your audit decides which parts.

## The sources

1. **The EHR discharge extract** (`discharges.csv`, this folder).
   Produced by the network's electronic health record. IT says
   the extract is generated nightly and covers "all discharges".
   The file you received was generated once, by hand, by an
   analyst who has since left. Nobody has confirmed the nightly
   job exists.
2. **The ward bed board.** A spreadsheet maintained by the ward
   clerks on a shared drive. It is, in practice, the source of
   truth for which ward a patient is in: the EHR ward field is
   updated from it, by hand, "most days". The spreadsheet has no
   owner since the senior clerk retired; three clerks edit it,
   none of them checks the others' rows.
3. **The coding sheet.** Diagnosis codes are assigned by two
   part-time coders working from paper notes. One coder writes
   codes with the dot, one without. Neither has been told this
   matters. There is no coding standard document.

## Access and ownership

- **EHR extract:** owned by IT. Read access for the engagement
  was granted in the kickoff meeting by the IT manager — for
  the analyst's hand-made file. The standing nightly extract,
  if it exists, needs a separate request nobody has filed.
- **Bed board:** owned by nobody (see above). The head nurse can
  describe how it is used; she cannot authorise changes to it,
  and says so.
- **Coding:** owned, on paper, by the medical records lead. She
  believes both coders follow the same written standard. There
  is no written standard (see above).
- **Follow-up field:** populated by the discharge lounge team
  from a pick-list in their own tool, which allows free text.
  The pick-list values and the values in the extract are not
  the same list.

## The policy claims

- The network's data-handling policy says extracts are
  de-identified before leaving the EHR. The extract's
  `patient_ref` column is a sequential reference that the
  discharge lounge can map back to a named patient in one
  lookup. Whether that counts as de-identified is a question
  for the compliance team, not for you — but your report must
  raise it, because Capstone 2 puts this data in scope.
- The policy says the EHR is the single source of truth for
  ward assignment. The bed board's existence contradicts it
  (see above).

## What the build will need

Capstone 2 drafts discharge summaries from clinician notes. The
drafting workflow will join notes to this extract on
`patient_ref`, group by `ward`, and report volumes by `status`
and `diagnosis_code`. Every defect you find in those columns
lands in the build. That is why the audit comes first.
