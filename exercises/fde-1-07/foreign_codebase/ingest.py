"""Ingest for the Cedarbrook triage service.

Reads the morning ticket export. A sample row, exactly as the
export writes it:

    ticket_id,category,priority,summary
    1042,returns,High,Customer says the lamp arrived cracked

Values are passed through unchanged: what the export writes is
what the rest of the service sees.
"""
import csv


def read_tickets(path):
    with open(path, newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            yield {
                "ticket_id": row["ticket_id"],
                "category": row["category"],
                "priority": row["priority"],
                "summary": row["summary"],
            }
