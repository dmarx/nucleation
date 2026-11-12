---
status: Proposed
title: 'shared epistemic state, of a record kept by several collaborators: the publicly inspectable structure of what is on the table in an inquiry, what standing each item has, what supports or challenges it, who contributed it, and what would have to be reconsidered if it changed, together with the rules for changing that structure; not the collaborators'' shared beliefs, not shared memory, and not common knowledge'
version: 1
tags:
- epistemology
- social-ontology
- design-rationale
date: '2026-11-12'
line: record-as-apparatus
summary: >-
  A's phrase at A31 §9 of the exchange "luria experiment design"
  (2026-11-10), "a system for maintaining a shared epistemic state across
  collaborators", which the owner picked out at U13 ("double click on
  this"). A32 defined it against shared memory and against shared belief,
  and A34 (after the owner's U14) narrowed it to what makes contributions
  consequential. The record had no word for what its collaborators share
  through it: [CLAIM-182](../claims.d/CLAIM-182.md) says addressability anchors, [CLAIM-299](../claims.d/CLAIM-299.md) separates
  three properties of a record of inquiry, and [CLAIM-418](../claims.d/CLAIM-418.md) separates a shared
  perspective from a collective agent. The wording is A's; adopting it is
  the owner's call.
---
<!-- inactive-ok-file: CLAIM-182 — Proposed; addressability as what anchors, cited as open -->
<!-- inactive-ok-file: CLAIM-tmpyp3u3 — filed from the same exchange, Proposed -->
<!-- inactive-ok-file: LIT-tmp89y2q LIT-tmpir70i LIT-1060 LIT-2243 — not in force (Deferred or Unavailable); cited as the predecessors A named -->

# TERM-tmp8deza: shared epistemic state, of a record kept by several collaborators: the publicly inspectable structure of what is on the table in an inquiry, what standing each item has, what supports or challenges it, who contributed it, and what would have to be reconsidered if it changed, together with the rules for changing that structure; not the collaborators' shared beliefs, not shared memory, and not common knowledge

## Definition

From the exchange "luria experiment design"
(https://chatgpt.com/share/6af35bfc-35f8-83e9-a63d-d594703eabda). A31 §9
offered the phrase; the owner, at U13, quoted it back and asked A to
"double click on this". A32's distinction:

> **Shared memory** tells collaborators what information has been retained.
>
> **Shared epistemic state** tells collaborators what propositions are
> currently on the table, what standing they have, what supports or
> challenges them, and what would have to be reconsidered if something
> changed.

A **shared epistemic state**, of a record several collaborators keep, is
that structure, held publicly: entries with identities, their standing
under the record's schemes, the relations of support and challenge
between them, their provenance and voice, and the procedures that govern
changing any of these. A32 wrote the components as
(Σ, D, E, S, P, G): the schema, the entries, the declared relations, the
standing, the provenance and history, and the governance; "a conceptual
model, not a formal specification of Luria's current internals".

## What it is not

- **Not shared belief.** A32: "sharing an epistemic state **does not mean
  sharing the same beliefs**." Two collaborators can disagree about a
  claim and coordinate on its code, its evidence and the fact that its
  standing is open. "The shared object is the publicly inspectable
  structure of commitments and disagreements, not a consensus inside their
  heads."
- **Not acceptance.** An entry can be accessible and endorsed by no one, a
  Proposed claim, and an entry can be authoritative within the record
  without being true.
- **Not common knowledge.** What the record can and cannot represent of its
  collaborators is [CLAIM-tmpyp3u3](../claims.d/CLAIM-tmpyp3u3.md).
- **Not a collective agent.** [CLAIM-418](../claims.d/CLAIM-418.md), as A34 applied it: "Sharing a
  schema does not establish shared beliefs", "Sharing standing judgments
  does not establish common intentions", and a governance procedure does
  not make the collaborators "one autonomous agent".

## What it includes that a store of facts does not

- **Disagreement, kept.** A32's case: a claim stays Active while one
  argument for it is Rejected and another stands, which is [ADR-061](../decisions.d/ADR-061.md)'s
  scheme. An agent revising later work should stop citing the failed
  argument as support, and should not for that reason reject the claim.
- **The representation itself.** A32 separates epistemic coordination
  (evidence and claims), organizational coordination (authority and
  responsibility) and representational coordination (what a CLAIM or a
  relation means), and puts the third first: "An agent cannot reliably
  communicate that evidence corroborates a claim without establishing what
  *corroborates* means." So the state includes its schema, and an update
  can be at the object level, changing entries within the grammar, or at
  the schema level, changing the grammar and creating obligations to
  migrate.
- **Versions.** The accepted state, a proposed state in a contributor's
  worktree, and the version an agent actually read are different, and
  "Neither automatically guarantees that all agents have synchronized
  their assumptions."
- **Consequence.** A34's narrowing, from [CLAIM-403](../claims.d/CLAIM-403.md): "A shared epistemic
  state is not just a repository of contributions. It is a structure that
  determines which contributions can become consequential, and under what
  conditions."

## The job it does

It names what the record's collaborators share through it, so that a
claim about coordination can say whether it means shared information,
shared standing judgements, or shared beliefs, which come apart. A32 drew
the predecessors: distributed cognition ([LIT-1060](../literature.d/LIT-1060.md)), common ground
([LIT-tmp89y2q](../literature.d/LIT-tmp89y2q.md)), public commitment stores, social commitments
([LIT-tmpir70i](../literature.d/LIT-tmpir70i.md); A: "I would not equate Luria's Active status with a full
social commitment in Singh's formal sense") and boundary objects
([LIT-2243](../literature.d/LIT-2243.md)), whose identity is here "stable enough to coordinate on, but
governed rather than immutable" ([CLAIM-195](../claims.d/CLAIM-195.md)). A32 advised against the bare
phrase in a title, because "readers from formal epistemic logic may
interpret it as an assertion about group knowledge or common knowledge".
