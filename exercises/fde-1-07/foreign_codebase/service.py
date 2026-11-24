"""Cedarbrook triage service — entry point.

Reads the ticket export named by the config, routes each
ticket to a queue, prints the queue counts.
"""
from config import load_config
from ingest import read_tickets

URGENT = "urgent"
STANDARD = "standard"
REVIEW = "review"


def triage(ticket):
    if ticket["category"] == "returns" and ticket["priority"] == "HIGH":
        return URGENT
    if ticket["category"] == "returns":
        return STANDARD
    return REVIEW


def main():
    config = load_config()
    counts = {URGENT: 0, STANDARD: 0, REVIEW: 0}
    for ticket in read_tickets(config["data_path"]):
        counts[triage(ticket)] += 1
    print(counts)


if __name__ == "__main__":
    main()
