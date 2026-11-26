# Alder Creek Health Network — the 48-hour prototype: a discharge handoff brief

Fictional composite, continued from FDE 2.01 to 2.07. Written
from the engagement's notes for the prototyping phase of the
discharge-support project.

## Where this phase starts

FDE 2.07 ended in an alert: live traffic drifted into the
medication topic, the system's weakest slice. Before anyone
commits to a larger build, the ward lead asks for a different
artefact on a short clock: a prototype of a discharge
handoff brief for night-shift nurses, demonstrated live at
Monday's 09:00 ward meeting — 48 hours after the Friday
16:00 request. The demo's job is narrow and stated in
advance: prove that a brief assembled from the FDE 2.03
retrieval system is worth a nurse's attention at handover,
or kill the idea cheaply while it is still a prototype.

`requests.json` holds the twelve features the room asked
for. Each request records its prototype build time in
hours, the demo value the ward lead scored it (1 to 5)
before the sprint started, whether an outside dependency
blocks it, whether it is safety-critical, whether it can
be faked convincingly for a demo, and — where the
prototype shortcut leaves real work behind — a harden note
naming that work.

## The timebox (agreed before the sprint started)

- **Sixteen prototype hours** are available inside the
  48-hour window. The other hours are sleep, the existing
  system's support rota, and the demo itself. A plan that
  needs seventeen hours is not a plan; it is a hope.
- **Faking a feature costs one hour**, whatever its real
  build time is: canned data, a stand-in screen, a fixed
  example. Faked features are labelled faked in the demo,
  on the record — a fake the audience cannot tell from
  the real thing is a lie, not a prototype technique.

## The selection rules (agreed before the sprint started)

Applied in this order, exactly as written:

1. **Deferred.** A blocked request is deferred, however
   valuable. So is a safety-critical request that cannot
   be faked: safety work is never rushed into a real
   build inside a demo timebox.
2. **Faked.** A safety-critical request that can be faked
   is faked, and only faked. Its real build belongs to
   production time, with its eval and review, not to the
   sprint.
3. **Built for real.** The remaining requests are ranked
   by demo value per prototype hour, highest first, ties
   broken by request id in ascending order. Requests are
   taken in that order while their build time fits the
   hours left after the faked features are paid for.
   A request that does not fit is cut, and later, smaller
   requests are still considered — the ranking is a
   queue, not a wall.
4. **Cut.** A request that is neither deferred, faked,
   nor built is cut from this prototype. Cut is a
   decision with a reason (it did not fit), recorded —
   not a promise that it will be built later.

## Throwaway, and the harden list

- The prototype is **throwaway by declaration**: its code
  is written to answer the demo question, and none of it
  is promoted to production by default. What survives is
  the learning, the demo record, and the harden list.
- The **harden list** is every prototype item — built or
  faked — that carries a harden note. Each note names the
  production work the shortcut skipped. A prototype with
  no harden list is claiming its shortcuts were free;
  at a customer site, they never are.
- **Demo-ready** is a verdict with a rule, not a feeling:
  the prototype is demo-ready when the demo value it
  carries (built plus faked) reaches at least 20 of the
  41 points the room asked for, inside the sixteen-hour
  timebox. Below that line, the honest Monday report is
  that the demo is not ready, and why.

## Ownership

- The ward lead owns the value scores and the timebox.
  Re-scoring a request mid-sprint to make a favourite
  feature fit is the prototyping form of moving a gate
  threshold after the numbers are known, and it is
  refused for the same reason (FDE 2.06, FDE 2.07).
- The demo script names, for each feature shown, whether
  it is built, faked, or absent. The audience decides
  with the labels visible.
