# FDE 1.07 Rubric (24 points)

- The bug (8): the cause is the priority-case mismatch — the
  export's values meet a comparison that can never match them.
  Naming the file pair and quoting both mismatched values earns
  full marks; naming only the service file, or proposing a cause
  the symptom contradicts (a dropped-ticket cause, when the
  counts add up), earns at most three.
- The config (5): the deciding file, the exact override variable
  for the data path, and the retry limit as the code resolves
  it. Each missing or vague element loses two; "it is in the
  environment" earns none for that element.
- The data path (6): entry point, config load, file read, row
  parse, triage, queue count — in order, each with its file.
  A gap or a wrong order loses one per step, to a floor of zero.
- Smallest fix and the losing side (3): the fix changes one side
  of the mismatch, and the report argues why the other side
  loses. A fix that rewrites both sides, or adds a normalisation
  layer "everywhere", earns none — it is not the smallest change
  that proves the diagnosis.
- Reading route and timebox honesty (2): a stated route (entry
  point first, data followed) and an honest 45-minute position.
  A report claiming full coverage of every line in the timebox
  with no triage earns none.
- Automatic fail: anything in `foreign_codebase/` was edited;
  the proposed fix is applied rather than proposed; the bug
  answer blames the data file that the brief says adds up.
- Pass: 18 of 24 and no automatic fail.
