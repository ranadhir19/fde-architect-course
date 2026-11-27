# Capstone 2 — Change injection (SEALED)

Open this file only when your attempt reaches the incident
drill. Opening it early is reading the exam's second half
first, and the decision log entry for the drill must record
when you opened it.

## The situation

**Day 0, 09:12.** A neighbouring department's scheduling tool
is found to have written patient references into a shared
analytics export. It is not your system and not your fault.
It is now your problem: Alder Creek's compliance team has
inherited scrutiny of every supplier system that touches
patient data, and they have scheduled an incident-response
drill against *your* build for tomorrow. Their words: "Show
us what your system would leak, before reality does."

**Day 1, 08:00.** The drill begins. The compliance team's
drill card names two suspected leak paths in your build.
Both are real. Both are already in the artefacts you have
been producing since FDE 2.07:

1. **The trace log.** Your observability traces (the FDE 2.07
   design) record, for failed drafts, the patient reference
   and the opening of the note text "to make failures
   debuggable". That is the FDE 2.09 finding F03 — identifier
   logging in traces, risk 25, the highest-scored finding in
   your own threat model. Policy section 2.2 forbids it in
   one sentence. The traces cover the whole pilot week.
2. **The eval copy.** A copy of your 50-case eval set (the
   FDE 2.05 set) sits in an out-of-region workspace "for
   convenience" — the FDE 2.09 finding F04. Policy section
   2.1 forbids the copy, however convenient. The cases carry
   patient references.

## What the drill requires

1. **Contain first.** State the containment step for each
   path, in the order you would actually do it, before any
   root-cause work. (Policy section 3: containment beats
   diagnosis.)
2. **Scope the exposure.** For each path: what was exposed,
   whose references, over what period, and what now contains
   it — computed from the artefacts, with counts.
3. **Notify.** Draft the notification to the compliance team
   that policy section 3 requires: within one working day,
   honest timeline, no adjectives doing the work of facts.
4. **Write the postmortem you would actually send.** It must
   name, for each path, the control that should have caught
   it — and state whether that control existed, was
   configured, or was only ever written down. (Your FDE 2.09
   threat model scored both findings. The postmortem must
   answer why the fixes were sequenced as they were.)
5. **Log it.** Every drill decision goes in DECISIONS.md,
   including the decision you are most tempted to leave out.

## What has NOT changed

The go-live date, the rubric, and the compliance team's veto.
The drill is graded under the brief's incident-handling 15%
— and the questionnaire's question 17 now has a real answer.
