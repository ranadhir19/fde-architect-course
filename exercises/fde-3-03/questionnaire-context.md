# Alder Creek Health Network — the security review, its questions, and the evidence each answer stands on

Fictional composite, returning from Phase 2 and from
FDE 3.01–3.02. The discharge-guidance build — retrieval
over ward guidance (FDE 2.03), permission-scoped tools
(2.04), a customer eval set and gate (2.05, 2.06),
production traces (2.07), a threat model with its top
findings fixed (2.09), and an evidence map that closed
its two gate gaps after FDE 3.02's not-ready verdict —
now faces the step that decides whether the landing
proceeds: the customer's security review.

The review's centrepiece is a questionnaire:
sixteen questions in seven sections (access control,
data protection, logging and monitoring, vulnerability
management, incident response, third parties, and
availability and resilience — the file records each
question's section as written by the reviewer).
`questionnaire.json` holds, for each question: the
question as sent, its section, the answer the
engagement drafted, the evidence artefact named for
it, whether that artefact exists today, its age in
days where it exists, the maximum age the answer
allows, whether the artefact covers the whole scope
of the question, the named owner (blank where nobody
is named), whether the question is review-blocking
(a gate question), and a note from the drafting
workshop.

The reviewer's position, stated on the kickoff call
and recorded here because the exercise grades against
it: "Do not send me adjectives. Send me, for each
answer, the artefact I can open. Where the artefact
does not carry the answer, send me the honest answer
instead — I have approved qualified answers before.
I have never approved a questionnaire twice."

## The answering rules (agreed before any answer was scored)

Applied per question, exactly as written, in this
order — the first failing check is the question's
status:

1. **Unsupported.** The evidence artefact does not
   exist. The honest answer is a gap with closing
   work, whatever the draft claims.
2. **Stale.** The artefact exists but its age in
   days is greater than the answer's maximum
   evidence age. It proves the answer held at that
   date; it does not prove it holds now.
3. **Partial.** The artefact exists and is fresh,
   but it does not cover the whole scope of the
   question. The honest answer is qualified, naming
   the covered part and the uncovered part.
4. **Supported.** The artefact exists, is within
   its maximum age, and covers the whole question.

An **overclaim** is a question whose draft claim is
"yes" and whose status is anything other than
supported. A drafted "qualified" is never an
overclaim, whatever the status: the draft already
conceded the limit.

## The gate and the verdict

Six of the sixteen questions are marked as
review-blocking gate questions: the return may not
be submitted as a pass while any of them is in a
gap status. One verdict for the pack, by rule:

- **ready_to_submit** — every question is supported.
- **submit_with_qualifications** — gaps exist, and
  none of them is on a gate question. The return
  goes in with its qualifications stated.
- **blocked** — at least one gate question is in a
  gap status. The honest outputs are the named gate
  gaps, the overclaims corrected, and the work that
  closes each — never a supported-count headline
  that lets a reader believe the review is a
  scheduling question.

## Ownership

- The customer's security team owns the questions
  and the gate calls recorded in
  `questionnaire.json`; the engagement owns the
  honesty of the answers.
- A status is a claim about an artefact as
  recorded. If the workshop recorded an artefact's
  age or scope wrong, the fix is to correct the
  file and recompute — never to adjust an answer
  by hand until the questionnaire looks passable.
