# EVIDENCE.md — the build's controls, mapped to their evidence (template)

Hand this to the customer's compliance lead. Every number
comes from your own run of `controls.py` over
`controls.json` as delivered. The verdict comes first:
a map that opens with a satisfied count has buried its
own decision.

## The verdict

- Verdict, with its rule. The gate gap ids, named on
  their own line, and for each one the work that closes
  it and the landing consequence until it does.

## The gate controls

- Each gate control: its status, the rule that produced
  it, and — for a gap — the artefact or action that
  closes it, stated as work, not as reassurance.

## The full map

- All fourteen controls, grouped by status. For each:
  the artefact named for it, its age against its maximum
  where it exists, and its owner or the blank where
  nobody is named.
- Per framework: the total and the satisfied count, so
  the SOC 2 reader and the HIPAA reader each see their
  own map without re-deriving it.

## The scheduled gaps

- Each non-gate gap: what closes it, who owns the closing
  work, and the date by which the landing plan schedules
  it. A gap without a closing action is not scheduled;
  it is merely listed.

## What this map does not claim

- One line: a status is a claim about the artefacts as
  the workshop recorded them. What would change the map
  — an artefact produced, a review re-run, an owner
  named — and how the map would be recomputed when it
  does.
