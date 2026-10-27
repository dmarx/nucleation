---
status: Proposed
complements:
- TERM-tmpk211q
title: 'relational vocabulary, of a class of descriptions: the arities and kinds of relation it can state (pairwise or higher-order, among states or among histories, of which declared types), and so which constraints are expressible in it at all'
version: 1
tags:
- compositionality
- mathematics
- design-rationale
date: '2026-10-27'
line: nucleating-argument
summary: >-
  What [QUESTION-tmprr9yy](../questions.d/QUESTION-tmprr9yy.md) asks about: whether composition can force a
  description to adopt relations its parts never needed. A sheaf on a
  graph has a pairwise vocabulary. Eliminating an interior can leave a
  constraint outside it ([THEORY-tmpvecoh](../theory.d/THEORY-tmpvecoh.md)). A luria record's relational
  vocabulary is its declared relation types and fields, and amendments
  that add one ([ADR-043](../decisions.d/ADR-043.md), [ADR-044](../decisions.d/ADR-044.md)) enlarge it. The term lets the record say
  that a constraint is inexpressible in a vocabulary, which is different
  from saying that it is false or unknown. Proposed.
---
<!-- inactive-ok-file: QUESTION-tmprr9yy CLAIM-tmpose3y CLAIM-419 CLAIM-tmpoe0v5 CLAIM-tmp0yhlm — Proposed, Open or new; the entries this term serves -->

# TERM-tmpk6w4q: relational vocabulary, of a class of descriptions: the arities and kinds of relation it can state (pairwise or higher-order, among states or among histories, of which declared types), and so which constraints are expressible in it at all

## Definition

The **relational vocabulary** of a class of descriptions is the set of relations
it can state. It has three dimensions:

- **arity:** pairwise only, as in a sheaf on a graph, or higher-order, as in
  a hypergraph or a sheaf on a cell complex;
- **domain:** relations among states, or among histories (a memory kernel,
  a behaviour in Willems's sense);
- **type:** which declared kinds of relation exist. A luria record's
  vocabulary is its relation types and fields ([CLAIM-tmpoe0v5](../claims.d/CLAIM-tmpoe0v5.md)).

A constraint is **expressible** in a vocabulary if some description in the class
states exactly it. Hansen and Ghrist's reduced constraint v₁ = v₂ + v₃ is not
expressible in the pairwise vocabulary of sheaves on the boundary graph
([THEORY-tmpvecoh](../theory.d/THEORY-tmpvecoh.md)).

## The distinctions it draws

- **Inexpressible is not false or unknown.** A description can fail because
  it states a relation that does not hold, because it lacks evidence, or
  because no description in its class states the relation at all. The
  last is a fact about the vocabulary. The response to it is to enlarge
  the vocabulary, not to revise a value. In CEGAR's terms ([NOTE-tmpxgbdz](../notes.d/NOTE-tmpxgbdz.md))
  it is the case refinement within a fixed answer space cannot reach.
- **Forced by the composite or by the class.** A richer vocabulary may be
  needed because of what the composite does, or only because the class
  excluded what would have stated it, here the interior vertex. Telling
  these apart is part of [QUESTION-tmprr9yy](../questions.d/QUESTION-tmprr9yy.md).

## Why it is proposed

The owner's review called the higher-order reduction "a remarkably direct
mathematical analogue of the sort of event we keep encountering in Luria: the
existing relation scheme cannot express what the composed organization
requires." Stating that analogy needs a name for what the scheme can express.
[CLAIM-419](../claims.d/CLAIM-419.md) and [CLAIM-tmp0yhlm](../claims.d/CLAIM-tmp0yhlm.md) describe the record's amendments as revising the
grammar, and this term says what the revision enlarges. What would settle it:
adoption if [QUESTION-tmprr9yy](../questions.d/QUESTION-tmprr9yy.md)'s answer is stated in it; rejection if "grammar"
and "scheme" suffice.
