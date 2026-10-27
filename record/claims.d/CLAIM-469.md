---
number: 469
status: Proposed
formerly:
- CLAIM-tmp0yhlm
title: 'Luria is an apparatus for a record''s objects in the operational sense: through its schemes, vocabularies, validators and generated views it realizes a system of distinctions that fixes what counts as a referable and governable object within the record, so that a split scheme makes one object two and a promoted vocabulary makes a value an entity; it keeps, enforces and propagates those distinctions; and its distinctions are revised through the record''s own use'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  A grammar change (a split scheme, a promoted vocabulary, a new relation)
  after which everything the record can refer to, check, relate and
  retire was already referable, checkable, relatable and retirable
  before, with the same consequences, so that the grammar only describes
  objects it does not fix. Or a record whose distinctions are fixed and
  enforced by something other than its grammar (its files, say, or
  conventions no tool reads), so that luria registers them without
  realizing them. Not defeated by Barad's ontology being false or
  inapplicable: this claim does not use it.
tags:
- design-rationale
- epistemology
date: '2026-10-27'
line:
- nucleating-argument
rests_on:
- CLAIM-479
- CLAIM-419
grounds:
- CASE-131
- CASE-178
uses:
- TERM-089
complements:
- CLAIM-470
summary: >-
  The operational half of [CLAIM-476](CLAIM-476.md), split from it at the owner's
  review of the pull request. In [TERM-089](../terms.d/TERM-089.md)'s sense, which needs no
  observer and no constitutive metaphysics, luria differentiates, retains,
  enforces and revises distinctions among a record's entries. That is
  established by how its grammar works ([CLAIM-479](CLAIM-479.md)) and by the
  record's own amendments ([CLAIM-419](CLAIM-419.md), [CASE-131](../cases.d/CASE-131.md), [CASE-178](../cases.d/CASE-178.md)). The
  further thesis that the record's objects are constituted in Barad's
  sense stays in [CLAIM-476](CLAIM-476.md), which now rests on this one. Split so
  that luria's evidential role does not depend on accepting Barad's
  ontology.
---
<!-- inactive-ok-file: CLAIM-476 CLAIM-419 CLAIM-470 TERM-089 CASE-178 — Proposed or new; the claim this was split from and the entries it rests on -->

# CLAIM-469: Luria is an apparatus for a record's objects in the operational sense: through its schemes, vocabularies, validators and generated views it realizes a system of distinctions that fixes what counts as a referable and governable object within the record, so that a split scheme makes one object two and a promoted vocabulary makes a value an entity; it keeps, enforces and propagates those distinctions; and its distinctions are revised through the record's own use

## The claim

The owner's review of the pull request, 2026-10-27, on [CLAIM-476](CLAIM-476.md): "There
are really two assertions. The operational claim: Luria realizes a system of
distinctions through its schemas, records, validators, and revision processes.
Those distinctions determine what counts as a referable and governable object
within the record. This is close to demonstrated. The constitutive claim:
Luria instantiates Barad's notion of an apparatus … This requires an
additional philosophical argument." And: "I would therefore avoid putting 'in
Barad's sense' into the title of the operational claim."

This is the operational claim, in [TERM-089](../terms.d/TERM-089.md)'s four functions:

- **Differentiation.** The grammar fixes what counts as a distinct object:
  whether two propositions are one entry or two, whether a work and a
  recommendation drawn from it carry different standing, and whether a
  word is a value or an entity. Promotion is the clearest case ([LU-ADR-124](https://github.com/dmarx/luria/blob/main/record/decisions.d/ADR-124.md)):
  a vocabulary that needs to say more becomes a scheme, and a value with a
  label becomes an entry with its own status, history and relations. A7 of
  the exchange: "The system has changed what kind of thing the value is
  permitted to be."
- **Retention.** Entries, their versions and their history are kept, and a
  retired entry keeps its code (CLAUDE.md: "Retire by status, never by
  deletion").
- **Enforcement.** A distinction the grammar holds is checked by the lint,
  propagated along declared relations and shown in generated views. A
  distinction held only in prose is not. A typed relation fixes the
  scheme at both ends and says what retiring its target leaves
  ([CLAIM-479](CLAIM-479.md)).
- **Revision.** Misfits met in filing are read as defects of the grammar
  and answered by amending it. [CLAIM-419](CLAIM-419.md) holds this as a finding about the
  record, with five amendments. [CASE-131](../cases.d/CASE-131.md) is the one in which a fixed
  relation misrepresented its relata. [CASE-178](../cases.d/CASE-178.md) measured how
  revisions arrive: in the pull request whose documents need them, nine
  times in ten with an ADR.

## Its warrant

Demonstrated for the first three functions, by construction. They are what
luria's grammar and machinery do, and can be checked against its code and
configuration. The fourth rests on [CLAIM-419](CLAIM-419.md) and the record's history, which is
why the claim rests on [CLAIM-419](CLAIM-419.md) and is Proposed while [CLAIM-419](CLAIM-419.md) is. The
owner's review: "close to demonstrated".

## What it does not claim

- **That the record's objects are constituted, in Barad's sense or any
  stronger sense than "made referable and governable".** That is
  [CLAIM-476](CLAIM-476.md).
- **That the distinctions are the right ones, or that every misfit is
  caught.** [CLAIM-419](CLAIM-419.md)'s limit stands: a move silently forced into the
  wrong shape leaves no decision behind. [TERM-089](../terms.d/TERM-089.md): "A self-modifying
  apparatus is not necessarily an epistemically self-correcting
  apparatus." A revision made only to make records pass, for instance by
  weakening a rule, would be revision without improvement ([CLAIM-342](CLAIM-342.md);
  A22 §10).
- **That luria maintains itself.** It depends on maintainers, computers and
  the repository it lives in ([CLAIM-195](CLAIM-195.md)).
