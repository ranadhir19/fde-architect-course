# Alder Creek Health Network — the legacy systems, as they are

Fictional composite, continued from FDE 2.01. Written from the
network's own systems register and two weeks of shadowing the
night clerk who actually moves the files.

## The orders system (the SFTP drop)

- A stock-and-orders system with no API, no webhooks, and no
  vendor roadmap for either. Its one integration surface is a
  CSV file written to an SFTP folder at about 02:00 each night.
- The file is semicolon-delimited. Dates are DD/MM/YYYY. Amounts
  are integer cents. The header is stable; the row order is not.
- The drop manifest — a line the night clerk pastes into a shared
  log — states this delivery contains 380 orders. The delivered
  file, `orders_drop.csv`, is the exact file from that night.
  Nobody has yet explained the difference, and the clerk's log
  is the only manifest there is.
- When a night's transfer is interrupted, the vendor's retry
  re-sends the whole file segment it was in the middle of. The
  clerk believes duplicates "cannot happen". The file is the
  authority on whether he is right.

## The billing system (the export)

- A separate billing system, bought a decade later, that has
  never spoken to the orders system directly. A finance analyst
  exports `payments_export.csv` each morning: comma-delimited,
  dates as YYYY-MM-DD, amounts in integer cents.
- Payments reference orders by order id — typed by hand at the
  billing desk for phone orders, which is how an id that exists
  in no orders file can appear in the payments file with real
  money attached to it.
- A payment gateway deducts its fee before settlement on some
  payment types. The export shows the settled amount, not the
  charged amount. Finance knows this; the export's one-line
  header note does not mention it.

## The third channel (out of scope, on purpose)

- A small number of orders are taken by phone and arrive as
  emails to a shared inbox, where a clerk re-keys them into the
  orders system the next day. They are real orders. They are
  also, for v1, explicitly out of scope: no automated feed
  exists, and pretending the two files cover them would invent
  a completeness the engagement does not have. The v1 report
  names them as excluded.

## Access and ownership

- The SFTP folder is owned by the network's IT team; the orders
  vendor answers questions only through a support contract held
  by procurement, with a five-working-day response norm.
- The billing export is owned by the finance analyst who runs
  it. She is also its only documented operator.
- Nobody owns the join between the two systems. Until this
  engagement, nobody had ever reconciled them nightly; month-end
  reconciliation was a spreadsheet, a sampling check, and a
  difference written off below a threshold nobody can now find
  in writing.
