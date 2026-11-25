# FDE 2.01 Reference solution

Released after the attempt window. All counts are of the file
as delivered, duplicates included, and are reproduced by the
reference `audit.py`.

## The counts

| Finding | Value |
|---|---|
| rows | 600 |
| duplicate_extra_rows | 24 |
| empty_discharge_date | 19 |
| empty_diagnosis_code | 16 |
| follow_up_silent_nulls | 31 |
| iso_admit_dates | 401 |
| us_admit_dates | 199 |
| first_us_format_row | 385 |
| first_undotted_diagnosis_row | 289 |
| status_distinct_raw | 6 |
| ward_distinct_raw | 10 |

Notes a strong audit states out loud:

- 18 discharge dates were emptied in the source rows; the
  delivered count is 19 because one duplicated row carried an
  empty discharge date with it (the same duplication lifts the
  silent-null count from 30 planted to 31 delivered). The 16
  empty diagnosis codes are 16 in both the source rows and the
  delivered file. An audit that reports 18 discharge dates has
  de-duplicated before counting — the first automatic fail.
- The silent-null tokens in `follow_up` are the empty string
  (8), `N/A` (8), `null` (8), and `-` (7). The column is never
  honestly empty and is unusable as delivered.
- Status has 6 raw spellings for 3 meanings: `discharged`
  appears as `discharged` (103), `Discharged` (112),
  `DISCHARGED` (92), and `dc` (93); `transferred` (142) and
  `deceased` (58) are spelled consistently.
- Ward has 10 raw spellings for 4 wards: Ward 4 as `Ward 4`,
  `W4`, `4`; Ward 7 as `Ward 7`, `W7`, `7`; Step-Down as
  `Step-Down`, `SDU`, `SD`; ICU is `ICU` throughout (150).

## The drift

- **Admit dates:** rows 1–384 are ISO; row 385 is the first in
  MM/DD/YYYY form, and 199 rows follow it (401 ISO rows in
  total, because 17 of the 24 duplicate rows carry ISO dates).
  A parser that assumes one format silently misreads a third
  of the file — and a US-format date such as 03/04/2026 does
  not even fail loudly.
- **Diagnosis codes:** dotted through row 288; row 289 is the
  first undotted code. 293 rows are dotted, 291 undotted, 16
  empty — 8 distinct raw values for 4 codes. The cause is in
  `data-reality.md`: two coders, two habits, no standard. The
  fix is a standard and an owner, not a cleaning script; a
  script alone re-drifts within a month.

## Classification

- **Blocks the build:** the 24 duplicate rows (every volume
  figure is inflated until they are resolved); the
  re-identifiable `patient_ref` (the build may not join on it
  until compliance rules on the de-identification claim).
- **Shapes the build:** both drifts and both vocabularies (the
  ingestion layer must normalise with the raw value preserved);
  the silent nulls in `follow_up` (that workflow step is
  designed out of v1 or rebuilt on a fixed pick-list).
- **Cosmetic:** none. An audit of a 600-row extract that finds
  a merely cosmetic defect has usually misjudged it.

## Access, ownership, and the refusal

- Vacancies: the bed board (no owner since the senior clerk
  retired), the coding standard (believed to exist, does not),
  and the standing extract (the nightly job is unverified and
  the access request for it is unfiled).
- Contradictions: the policy names the EHR the single source
  of truth for ward, while the bed board feeds the EHR by hand;
  the policy calls the extract de-identified, while one lookup
  in the discharge lounge reverses it.
- **The refusal:** do not build the ward-grouped reporting on
  the EHR ward field until the head nurse and the medical
  records lead jointly answer one question: "Which artefact —
  the bed board or the EHR — is corrected when the two
  disagree, and who corrects it?" Until that is answered, every
  ward figure the build produces has two authors and no owner.
