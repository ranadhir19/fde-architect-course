# FDE 3.03 Exercise — Surviving the security review: answer the questionnaire with artefacts, not adjectives

**Topic:** Surviving the security review (Layer 6).
**Part (d) of FDE 3.03.**
Attempt this before watching the tutorial half of the lesson.
**Prerequisite:** FDE 3.02 — the build has an evidence map.
This exercise returns to Alder Creek Health Network, the
Phase 2 build customer, now facing the review its landing
depends on: a customer security questionnaire of sixteen
questions in seven sections, sent by the customer's security
team, due back as answers a reviewer can check.

## The task

Read `questionnaire-context.md` first. It describes the
review, the sixteen questions in `questionnaire.json`,
what the engagement drafted for each one, the evidence
each answer stands on, and the answering rules the
reviewer and the engagement agreed before any answer
was scored.

Then build the review pack the security team can check
without you:

1. `review.py`, built from `review_starter.py`: read the
   sixteen questions in `questionnaire.json`, apply the
   answering rules exactly as written, and fill the
   `RESULT` dictionary the grader checks. Every value
   must be computed from the file at run time.
2. `REVIEW.md` from `review-template.md`: the answers
   you would return — every question's honest answer
   with its rule, every overclaim in the draft corrected
   in place, and the submission verdict with the gate
   gaps that decide it stated before any count.

The answering rules, agreed with the reviewer before
you build:

- **An answer is its evidence, not its adjectives.**
  "Yes" is a claim that an artefact exists, is fresh,
  and covers the whole question. An answer whose
  artefact fails any of those three checks is a
  different answer, and the pack must say which.
- **The draft is not the answer.** The engagement's
  draft claims are recorded in the file so the review
  can find them: a drafted "yes" that the evidence does
  not support is an overclaim, and an overclaim left in
  a returned questionnaire is the finding the reviewer
  remembers.
- **A qualification is an answer, not a failure.**
  Partial evidence earns a qualified answer that names
  exactly what is covered and what is not. Reviewers
  trust qualifications they can check; they discount
  every other answer on the page once one unqualified
  claim proves soft.
- **Gate questions decide the submission.** A gap on a
  review-blocking question stops the return until it
  closes or the answer is returned honestly as a gap.
  The verdict reports the gate first.

## Done means

- Every RESULT value is computed from
  `questionnaire.json` at run time — the supported,
  partial, stale and unsupported counts and sorted id
  lists, the gate totals and gate gap list, the
  overclaim count and list, the section count, and the
  verdict.
- The partitions hold: supported plus partial plus
  stale plus unsupported is the sixteen questions, and
  every question id appears in exactly one status list.
- The returned pack names, for every gap, the artefact
  or action that closes it — and for every overclaim,
  the corrected answer that replaces the draft.
- Graded with `RUBRIC.md`. `SOLUTION.md` is the
  reference answer, released after the attempt window.

## The habit this exercise is really testing

- A security review is not an exam to be passed with
  confident prose; it is an audit the customer runs on
  your honesty, with your build as the evidence. The
  professional skill is answering each question at
  exactly the strength its artefact supports — no
  stronger, and no weaker either.
- The answer that survives a review is rarely the
  most impressive one. It is the one the reviewer can
  verify in the room, from an artefact, without having
  to take your word for anything.
