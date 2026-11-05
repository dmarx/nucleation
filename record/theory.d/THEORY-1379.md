---
number: 1379
status: Proposed
formerly:
- THEORY-tmp8atfa
promote_when: >-
  The Basic Theorem (that the concepts of any formal context form a
  complete lattice and that every complete lattice is isomorphic to some
  concept lattice) is checked against a proof, in Ganter & Wille or
  re-derived in the record, since the tutorial states it without one. The
  other parts of the title are re-derived in this reading.
title: 'Wille''s formal concept analysis, as restated by Ignatov: for any relation between objects and attributes, the two derivation operators form an antitone Galois connection whose closed pairs form a complete lattice, every complete lattice arises so, and an attribute implication A → B holds exactly when every object with all of A has all of B, that is, when B lies in the closure of A'
version: 1
tags:
- mathematics
date: '2026-11-05'
source:
- LIT-2083
summary: >-
  Ignatov (2015), [LIT-2083](../literature.d/LIT-2083.md), read in part in [NOTE-1593](../notes.d/NOTE-1593.md) (the theory
  sections and conclusion), restating Wille 1982 and Ganter & Wille
  ([LIT-344](../literature.d/LIT-344.md)). Proposed: the tutorial gives the Basic Theorem without proof;
  the Galois property and the closure form of implications were re-derived
  for this reading. Implications hold relative to the given objects, not by
  logical entailment, and include vacuous ones. It does not say that a
  concept lattice's existence tells anything about the system it describes:
  every relation has one.
---
<!-- inactive-ok-file: NOTE-1593 LIT-344 CLAIM-586 — Skimmed and new, Unavailable, or Proposed; cited from the reading of Ignatov (2015) as open -->

# THEORY-1379: Wille's formal concept analysis, as restated by Ignatov: for any relation between objects and attributes, the two derivation operators form an antitone Galois connection whose closed pairs form a complete lattice, every complete lattice arises so, and an attribute implication A → B holds exactly when every object with all of A has all of B, that is, when B lies in the closure of A

## Source

Ignatov (2015), [LIT-2083](../literature.d/LIT-2083.md); read in [NOTE-1593](../notes.d/NOTE-1593.md). The canonical source,
[LIT-344](../literature.d/LIT-344.md) (Ganter & Wille), is held Unavailable.

## What was actually shown

- **The Galois connection** (Proposition 1, p. 7): A ⊆ B′ ⇔ B ⊆ A′ ⇔ A × B
  ⊆ I. Immediate from Definition 8: each side says every object in A has
  every attribute in B.
- **Closures** (Exercise 4, p. 7): both composites (·)′′ "are closure
  operators"; standard for any antitone Galois connection.
- **The Basic Theorem** (Theorem 1, p. 9): "Concept lattice B(G, M, I) is a
  complete lattice." and "In particular, L is isomorphic to B(L, L, ≤)."
  Stated with credit to Wille 1982 and Ganter & Wille; no proof given.
- **Implications** (Definition 17, p. 15): A → B holds when A′ ⊆ B′, "i.e.,
  each object having all attributes from A also has all attributes from
  B." That this is B ⊆ A′′ was re-derived: if A′ ⊆ B′ then B ⊆ B′′ ⊆ A′′;
  if B ⊆ A′′ then A′ = A′′′ ⊆ B′.

## What this does not say

- That an implication is a logical entailment: it holds over the objects
  given. With fewer objects more implications hold, so restricting a
  context to a subset of its objects (A's budget-affordable
  configurations) can only add implications, the opposite direction to
  [CLAIM-586](../claims.d/CLAIM-586.md)'s growing complex. That is the reader's derivation, not
  the tutorial's.
- That a set of attributes no object has is excluded: its closure is every
  attribute, a vacuous implication.
- That the lattice's existence is a finding about anything: it exists for
  every relation whatever; only its shape carries information.
- Anything beyond the core: no structure theory, and nothing of Wille's
  Boolean concept logic.
