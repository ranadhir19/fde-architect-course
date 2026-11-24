# FDE 1.07 Reference solution

Released after the attempt window. One defensible hunt:

## The bug

`foreign_codebase/ingest.py` preserves the export's priority
value exactly as written: the sample export writes it as
`High` (capital H, rest lower case), and `read_tickets` passes
the string through unchanged. `foreign_codebase/service.py`
routes a ticket to the urgent queue only when the priority
equals `HIGH` — all capitals. `High` never equals `HIGH`, so
no ticket ever takes the urgent branch; every urgent returns
ticket falls through to the standard queue. That is exactly
the reported symptom: the counts still add up, because nothing
is dropped — it is misrouted, which is why a dropped-ticket
theory fails the support lead's own evidence.

## The config

Configuration is decided in `foreign_codebase/config.py`:
defaults are declared there and environment variables override
them. The ticket data path is overridden by the environment
variable `TRIAGE_DATA_PATH`. The retry limit the code will
actually use is 3 — the default in `config.py`, overridable by
`TRIAGE_RETRY_LIMIT`, with no other value set anywhere in the
codebase.

## The data path

1. `service.py` — `main()` is the entry point; it asks
   `config.py` for the resolved configuration first.
2. `config.py` — `load_config()` returns the data path
   (default `data/tickets_export.csv`, or the
   `TRIAGE_DATA_PATH` override).
3. `ingest.py` — `read_tickets(path)` opens that file and
   yields one dict per CSV row, values unchanged.
4. `service.py` — `triage(ticket)` compares the row's priority
   and returns a queue name: `urgent`, `standard`, or `review`.
5. `service.py` — `main()` counts the returned queue names and
   prints the counts. A ticket's journey ends as one increment
   in exactly one queue count.

## Smallest fix

Normalise on one side only: in `ingest.py`, upper-case the
priority value as the row is parsed, so every downstream
comparison sees the form the rest of the code was written
against. The losing side is changing the comparison in
`service.py` to match the export's mixed case: the export's
casing is one writer's habit, while `HIGH` is the form the
service's other priority checks also use — fix the boundary
where untrusted input enters, not every place it is consumed.
The proof is one synthetic row with priority `High` landing in
the urgent count — run after the fix is approved, not during
the hunt.

## Reading route (reference)

Entry point first (`service.py` `main`), then the two files it
touches in the order it touches them: `config.py` for where
the path comes from, `ingest.py` for what a ticket looks like
when it arrives. The symptom (misrouting, not loss) pointed at
the comparison in `triage` before any other line was read;
the hunt was confirming or killing that hypothesis in the
ingest code, which is where it was proved.
