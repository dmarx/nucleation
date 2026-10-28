---
number: 55
status: Open
formerly:
- QUESTION-tmpgy8la
title: 'If communicative categories form a non-Boolean lattice, what structure fixes the negation of a category: a presheaf over contexts, and if so over which base category, an orthocomplemented lattice, or sectors that no probe connects?'
version: 3
history:
- version: 2
  date: '2026-10-16'
  note: >-
    THEORY-516, filed from Butterfield and Isham's part II, answers it
    in part and is added to "What the record holds": over a presheaf of
    contexts the truth values are sieves whose negation the base category
    fixes.
- version: 3
  date: '2026-10-21'
  note: >-
    Split under ADR-049. Which negation a presheaf over contexts gives is
    QUESTION-247, Answered by THEORY-516 and THEORY-037: the Heyting
    pseudo-complement the base category fixes. This question is reworded
    to what is left: whether the communicative object is such a presheaf,
    over which base, and whether probes split it into sectors. Version
    2's title was 'If communicative categories form a non-Boolean
    lattice, what is the negation of a category, an orthocomplement, a
    Heyting pseudo-complement over contexts, or a complement within
    sectors that no probe connects, and does the context-indexed form of
    the communicative object settle which?' THEORY-037's entry in "What
    the record holds" no longer says its Heyting laws are unchecked.
tags:
- logic
- quantum-foundations
- mathematics
date: '2026-10-12'
line: 'pragmatic-transport'
summary: >-
  Filed in the fourth synthesis pass to give readings no question asked
  for a place in the argument. It bears on [CLAIM-119](../claims.d/CLAIM-119.md), [CLAIM-038](../claims.d/CLAIM-038.md),
  [CLAIM-044](../claims.d/CLAIM-044.md), [QUESTION-025](QUESTION-025.md) and [QUESTION-031](QUESTION-031.md). Given a presheaf over
  contexts, the negation is the Heyting pseudo-complement, and that part
  is [QUESTION-247](QUESTION-247.md), Answered. Which structure the communicative
  object has is open. [THEORY-041](../theory.d/THEORY-041.md) and [THEORY-042](../theory.d/THEORY-042.md) bear on it; the body
  gives each one's limit.
refined_by:
- QUESTION-247
bearing:
- THEORY-042
- THEORY-041
---

# QUESTION-055: If communicative categories form a non-Boolean lattice, what structure fixes the negation of a category: a presheaf over contexts, and if so over which base category, an orthocomplemented lattice, or sectors that no probe connects?

## The question

[CLAIM-119](../claims.d/CLAIM-119.md) holds that communicative categories form a concept lattice and are told apart by "a few social-relational constraints". To say that affectionate teasing is not sarcastic condemnation, the lattice needs a negation. Non-Boolean lattices of propositions offer three: an orthocomplement, a pseudo-complement under which excluded middle fails, or a product of Boolean sectors. The question is which one the record's own model gives.

## Why the record needs it

The mechanism is structural identity, not analogy. [CLAIM-038](../claims.d/CLAIM-038.md) makes a communicative object a system of constraints indexed by a cover of contexts, which is a presheaf. The topos programme builds the logic of propositions about a presheaf over contexts. So if [CLAIM-038](../claims.d/CLAIM-038.md) holds, its result applies to the same kind of object. Superselection applies whenever no observable connects two blocks. In the record's terms, that is when no probe in the family has cross terms between two categories ([QUESTION-031](QUESTION-031.md)). A blend across them is then a mixture, and that is [CLAIM-044](../claims.d/CLAIM-044.md)'s ambiguity. [QUESTION-025](QUESTION-025.md) asks whether embeddings carry a non-Boolean lattice. It cannot be scored until the lattice's operations are fixed.

## What the record holds

- [THEORY-037](../theory.d/THEORY-037.md): over contexts, propositions form "a distributive Heyting algebra, not an orthocomplemented lattice", and "the negation of δ(P) is not δ(1 − P)". The source sketches the Heyting laws, and the record re-derives them ([THEORY-037](../theory.d/THEORY-037.md), note of 2026-10-19).
- [THEORY-041](../theory.d/THEORY-041.md): the order does not fix the complement. Birkhoff and von Neumann proposed modularity from a probability-like dimension function, and it fails in infinite dimension. Limit: it is mainly an attribution, and orthomodularity is unsourced.
- [THEORY-042](../theory.d/THEORY-042.md): under a superselection rule "a coherent superposition across sectors is operationally a mixture", and the lattice becomes a product of sector lattices. Limit: proved for one case only, and it is an idealisation.
- [THEORY-516](../theory.d/THEORY-516.md): for any presheaf of propositions over a category of contexts, valuations obeying functional composition are sieve-valued subobjects, and the logic of the truth values, negation included, is fixed by the base category, not by global sections. Limit: it says which negation once a base is chosen, not which base the communicative object has.

## What would answer it

A derivation of the sub-object logic of the communicative object as [CLAIM-038](../claims.d/CLAIM-038.md) defines it, with its negation written out. Or a probe family shown to be block-diagonal across a pair of categories, which would make their lattice a product of sectors.

**Split, 2026-10-21 ([ADR-049](../decisions.d/ADR-049.md)).** [THEORY-516](../theory.d/THEORY-516.md) and [THEORY-037](../theory.d/THEORY-037.md) answer the
conditional part: over a presheaf of contexts, the negation is the
Heyting pseudo-complement the base fixes, not an orthocomplement. That is
[QUESTION-247](QUESTION-247.md), Answered. This question keeps what they leave: whether
the communicative object is such a presheaf ([CLAIM-038](../claims.d/CLAIM-038.md) is Proposed), which
base category it has, and whether some probe family splits it into
sectors ([THEORY-042](../theory.d/THEORY-042.md)).
