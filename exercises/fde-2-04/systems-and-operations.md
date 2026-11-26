# Alder Creek Health Network — the legacy system, its operations, the proposal

Fictional composite, continued from FDE 2.01 to 2.03. Written
from the engagement's notes for the agent phase of the
discharge-support project.

## Where this phase starts

The discharge-guidance retrieval system (FDE 2.03) is live for
ward staff. The next request, from the ward lead, is modest: an
agent that can answer ward staff questions by calling the
legacy record system directly — bed state, checklists, follow-up
availability — instead of staff switching screens. The vendor
that maintains the legacy system supports an MCP-style tool
interface and has proposed exposing all twelve of the system's
operations through it, "so the agent is not limited later".

That sentence is the risk this exercise exists to refuse.
"Not limited later" means every operation the system can
perform becomes callable by software that takes instructions
from text — including text inside the customer's own documents
(FDE 2.09 takes up prompt injection directly). The exposure
decision is made now, by rule, with the compliance contact in
the room — not later, by accumulation.

## The operations (`operations.json`)

- Twelve operations. Each carries a `kind` (read, write, or
  admin), a `data_class` (internal, phi, phi_bulk, or
  financial), the caller roles the legacy system itself allows,
  and its required arguments.
- Three operations are read-only over internal data: aggregate
  bed counts, the discharge checklist, and follow-up slot
  availability. None of them returns patient detail.
- Two are reads over patient data: one record at a time, and a
  bulk monthly extract. Read-only is not the same as safe: a
  read is a disclosure, and the bulk read is a disclosure at
  scale.
- Six are writes — to patient records, to billing, to patients
  by email. One of them, merging two patient records, cannot
  be undone from the legacy interface at all.
- One is administration: granting system access. Its data
  class is internal, and it is still withheld — kind decides
  before data class is even considered.

## The exposure rule (this customer's risk, stated as a rule)

**Expose an operation only if its kind is read and its data
class is internal.** The rule is deliberately crude. A finer
rule — this read, for this role, on Tuesdays — is a rule
nobody can audit in a review meeting. Crude and checkable
beats precise and argued, at the boundary where software
starts calling a hospital's record system.

## The calls (`requests.json`)

- 24 calls, written from the pilot week's log shape: ward
  staff, bed managers, and booking clerks calling the exposed
  tools; callers reaching for tools that were never exposed,
  including one tool name that does not exist in the registry
  at all; callers using the wrong role; and calls missing a
  required argument.
- Evaluation order is part of the design: exposure first (a
  caller learns nothing about roles or arguments for a tool
  that is not exposed to anyone), role second, arguments last.
- The roles in the registry were assigned by the legacy
  vendor's default template and have never been reviewed by
  the network. The engagement accepts them for the pilot and
  records that as an open risk in the report — the same shape
  of risk as the unreviewed access levels in FDE 2.03, one
  layer up.

## Ownership

- The exposure decision is owned by the ward lead, with the
  compliance contact holding a veto — exercised in the scoping
  meeting, where the bulk extract was the only operation anyone
  argued for, and the veto held.
- Reconsidering a withheld operation is a new decision by the
  same owners, in the engagement log — never a configuration
  change made quietly because a demo went well.
