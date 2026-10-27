---
number: 91
status: Proposed
formerly:
- TERM-tmpk6w4q
complements:
- TERM-090
title: 'relational vocabulary, of a class of descriptions: the arities and kinds of relation it can state (pairwise or higher-order, among states or among histories, of which declared types), and so which constraints are expressible in it at all'
version: 1
tags:
- compositionality
- mathematics
- design-rationale
date: '2026-10-27'
line: nucleating-argument
summary: >-
  What [QUESTION-283](../questions.d/QUESTION-283.md) asks about: whether composition can force a
  description to adopt relations its parts never needed. A sheaf on a
  graph has a pairwise vocabulary. Eliminating an interior can leave a
  constraint outside it ([THEORY-1090](../theory.d/THEORY-1090.md)). A luria record's relational
  vocabulary is its declared relation types and fields, and amendments
  that add one ([ADR-043](../decisions.d/ADR-043.md), [ADR-044](../decisions.d/ADR-044.md)) enlarge it. The term lets the record say
  that a constraint is inexpressible in a vocabulary, which is different
  from saying that it is false or unknown. Proposed.
---
<!-- inactive-ok-file: QUESTION-283 CLAIM-480 CLAIM-419 CLAIM-479 CLAIM-469 — Proposed, Open or new; the entries this term serves -->

# TERM-091: relational vocabulary, of a class of descriptions: the arities and kinds of relation it can state (pairwise or higher-order, among states or among histories, of which declared types), and so which constraints are expressible in it at all

## Definition

The **relational vocabulary** of a class of descriptions is the set of relations
it can state. It has three dimensions:

- **arity:** pairwise only, as in a sheaf on a graph, or higher-order, as in
  a hypergraph or a sheaf on a cell complex;
- **domain:** relations among states, or among histories (a memory kernel,
  a behaviour in Willems's sense);
- **type:** which declared kinds of relation exist. A luria record's
  vocabulary is its relation types and fields ([CLAIM-479](../claims.d/CLAIM-479.md)).

A constraint is **expressible** in a vocabulary if some description in the class
states exactly it. Hansen and Ghrist's reduced constraint v₁ = v₂ + v₃ is not
expressible in the pairwise vocabulary of sheaves on the boundary graph
([THEORY-1090](../theory.d/THEORY-1090.md)).

## The distinctions it draws

- **Inexpressible is not false or unknown.** A description can fail because
  it states a relation that does not hold, because it lacks evidence, or
  because no description in its class states the relation at all. The
  last is a fact about the vocabulary. The response to it is to enlarge
  the vocabulary, not to revise a value. In CEGAR's terms ([NOTE-1231](../notes.d/NOTE-1231.md))
  it is the case refinement within a fixed answer space cannot reach.
- **Forced by the composite or by the class.** A richer vocabulary may be
  needed because of what the composite does, or only because the class
  excluded what would have stated it, here the interior vertex. Telling
  these apart is part of [QUESTION-283](../questions.d/QUESTION-283.md).

## Why it is proposed

The owner's review called the higher-order reduction "a remarkably direct
mathematical analogue of the sort of event we keep encountering in Luria: the
existing relation scheme cannot express what the composed organization
requires." Stating that analogy needs a name for what the scheme can express.
[CLAIM-419](../claims.d/CLAIM-419.md) and [CLAIM-469](../claims.d/CLAIM-469.md) describe the record's amendments as revising the
grammar, and this term says what the revision enlarges. What would settle it:
adoption if [QUESTION-283](../questions.d/QUESTION-283.md)'s answer is stated in it; rejection if "grammar"
and "scheme" suffice.
