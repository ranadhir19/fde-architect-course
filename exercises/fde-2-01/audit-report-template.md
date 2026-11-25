# Data-audit report — template

Copy this file to `AUDIT.md` and fill every section. Counts come
from running your `audit.py`; if a section has no finding, write
"none found" and the check you ran — an unchecked section left
blank reads as a finding you missed.

## 1. The file as delivered

Rows, columns, the extract's stated provenance, and the
provenance you could actually verify.

## 2. Defect register

One row per defect: what it is, the computed count, an example
row id, and its class — *blocks the build*, *shapes the build*,
or *cosmetic* — with the build consequence that earns the class.

## 3. Drift

Each format or vocabulary that changes inside the file: the
first row where the new form appears, the two forms, and your
hypothesis for why (checked against `data-reality.md`).

## 4. Silent nulls

Per column: the null tokens present, the count for each, and
whether the column can be trusted as complete.

## 5. Access and ownership

Per source: who owns it, who granted your access, what access
you still do not have, and every vacancy (a source nobody owns).

## 6. Where the documents and the data disagree

Each contradiction between `data-reality.md`, the policy claims,
and what the file itself proves.

## 7. The refusal

The one source you will not build on yet, the named person who
can clear it, and the exact question they must answer.
