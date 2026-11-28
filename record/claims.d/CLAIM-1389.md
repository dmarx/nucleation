---
number: 1389
status: Proposed
formerly:
- CLAIM-tmpby6hz
title: 'Retention requirements join over an entry''s uses'
statement: >-
  Instead of scoring entries by relevance, a record can let each use of an
  entry impose a minimum retention requirement, a pair of an availability
  (cold below warm below hot) and a fidelity (stub below capsule below
  full), set by the kind of relation through which it is used, and take an
  entry's requirement as the componentwise join of the requirements its
  uses impose, propagated over the relation graph to a fixed point with
  pins as lower bounds and unclassified relations defaulting to
  conservative retention; the result states the least the declared
  organization obliges the record to keep and prescribes no deletion
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  A requirement the record's own relations impose that is not monotone in
  the order (for instance, one that is met by keeping one of two entries
  but not both), so that no join gives the least requirement; or a showing
  that the requirements per relation kind cannot be fixed without
  deciding entry by entry, so that the propagation saves no judgment.
tags:
- databases
- software-engineering
- logic
date: '2026-11-26'
line:
- record-as-apparatus
- records-of-inquiry
bears_on:
- QUESTION-552
uses:
- TERM-186
summary: >-
  A29 §§2 and 15 of the exchange "Alignment consequences brainstorm"
  (ChatGPT, 2026-11-26). From weak references and ephemerons: "not every
  reference must keep its target alive", and the record's typed relations
  could carry "references that specify retention requirements", so that
  "Connectivity and retention pressure become separate properties". The
  join, r(e) = ⋁ over uses u of r_u(e), is "a small abstract
  interpretation over the record's relation graph". [CLAIM-1448](CLAIM-1448.md), the
  assistant's, shows it cannot express alternative support (A29 §16), so
  the defeated_if is met for that case and the claim stands for
  conjunctive requirements. The wording is A's (ChatGPT, in the exchange
  of 2026-11-26); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-1448 — Proposed; filed from the same exchange on 2026-11-26 -->

# CLAIM-1389: Retention requirements join over an entry's uses

## Retention semantics per relation

A29 §2 proposes defaults for the relations the record's `luria.yaml`
declares (all of which exist):

| Existing relation | Candidate retention semantics |
|---|---|
| `rests_on` | Preserve the load-bearing content and grounds needed for reconsideration |
| `grounds` | Preserve evidence and its relevant provenance |
| `uses` | Preserve the definition or capability actually used |
| `corroborates` | Retain according to the independent evidential contribution |
| `complements` | Weak association; does not necessarily require hot availability |
| `bears_on` | Weak or conditional relevance to an inquiry |
| `integrates` | Potential consolidation opportunity |
| `superseded_by` | Historical continuity and navigation to the successor |
| `objects_to` | Preserve the challenge and its relationship to the challenged position |

"These would be candidate defaults, not universal semantics." A `rests_on`
need not make its whole target hot: "It might require only a specific
proposition to remain cheaply accessible, while its complete justification
remains recoverable."

## The join

A29 §15. With fidelity ordered stub ⪯ capsule ⪯ full and availability
cold ⪯ warm ⪯ hot, an entry's minimum requirement is

  r(e) = ⋁_{u ∈ Uses(e)} r_u(e),

componentwise. "Each edge would propagate an availability or fidelity
constraint. Cycles could be evaluated to a fixed point. An explicit pin
would impose a lower bound. An unresolved classification could default to
conservative retention." The fixed point exists: the lattice is finite and
the propagation, if each edge's requirement is monotone in its source's,
is monotone, so iteration from the bottom reaches the least fixed point
(the assistant's note; textbook).

"The result would not prescribe what must be deleted. It would describe the
minimum maintenance obligations imposed by the declared organization. That
is an attractive separation between mechanical inference and institutional
judgment."

A's own caveat, in the widget's caption: the model "assumes one common
representation. Separate hot capsules and recoverable full archives can
satisfy some combinations more cheaply."

## Where it fails

A29 §16: "An argument may depend on two premises jointly, or it may have
two independently sufficient grounds. Those structures are not
equivalent." [CLAIM-1448](CLAIM-1448.md) shows the second has no least requirement, so
no join computes it.
