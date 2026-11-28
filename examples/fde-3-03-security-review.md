# Worked example — FDE 3.03: the answer the artefact supports, annotated

Referenced by the FDE 3.03 learning session. The customer is
fictional; the pattern is a composite written for this course.
Annotations in brackets name the move being made. This example
uses a different customer from the exercise, on purpose: copy
the moves, not the words.

> **SECURITY QUESTIONNAIRE (excerpt) — Larkspur Freight
> quote-desk build, customer security review**
>
> **The "yes" that was a design.** Asked whether failed
> logins were alerted on, the draft said yes: the
> alerting rule was written, reviewed, and in the
> configuration file. Nobody had ever seen it fire, and
> a test login storm produced no alert — the rule
> pointed at a log stream the service had stopped
> writing to two releases earlier. The returned answer
> was a gap with a date: rule re-pointed, test storm
> re-run, alert received and timed. The reviewer marked
> the question closed on the strength of the correction,
> not the original answer.
>
> *[A configuration is a claim about intent. The artefact
> that carries an answer is the record of the thing
> happening — a test, a report, an exercise — never the
> setting that says it should.]*
>
> **The qualification that passed unchanged.** Asked
> whether all data stores were encrypted at rest, the
> team answered qualified: the attestation covered the
> quote store and the document index, and named the one
> legacy export bucket it did not cover, with the
> migration date. The reviewer's written response was
> two words: "accepted, noted". No follow-up questions
> were asked about any other answer on that page.
>
> *[A qualification that names its own boundary is
> evidence about the answerer, not just the answer: it
> tells the reviewer the unqualified answers can be
> taken at face value, because this team demonstrably
> says less than it could when less is true.]*
>
> **The gate named before the counts.** The return
> opened with its one blocking gap — the untested
> restore — and the exercise date already booked, and
> only then with its supported answers. The sponsor
> later said the ordering was why the review took one
> round instead of three: a team that leads with its
> own stop sign does not have to be audited for the
> others.
>
> *[Gate first is the same discipline as the evidence
> map's, one room further along: the verdict is the
> first thing the reader needs, and burying it costs
> more trust than the gap itself.]*

**The lesson:** a security review is survived in the
drafting, not in the meeting. Answer each question at
exactly the strength of the artefact behind it, correct
your own overclaims before the reviewer finds them, and
lead with the gate — the review then becomes a check of
your evidence, which you can pass, instead of a test of
your adjectives, which you cannot.
