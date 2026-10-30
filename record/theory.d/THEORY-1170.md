---
number: 1170
status: Proposed
formerly:
- THEORY-tmph50qc
promote_when: >-
  A proof of the adaptive analogue, read or re-derived and checked;
  refuted by a map some non-contextual adaptive hom model induces and no
  adaptive procedure does.
title: 'A convex map between two scenarios'' model sets is induced by a classical adaptive procedure exactly when some non-contextual model of the corresponding adaptive hom scenario induces it'
version: 1
tags:
- contextuality
- mathematics
- quantum-foundations
date: '2026-10-29'
source:
- LIT-845
extends:
- THEORY-174
summary: >-
  The adaptive analogue of Theorem 44 that Barbosa, Karvonen and Mansfield
  assert in Closing Bell ([LIT-845](../literature.d/LIT-845.md), §6.2) without proof, split from
  [THEORY-174](THEORY-174.md) when the fifteenth status review narrowed that entry to the
  non-adaptive procedures its re-derivation covers and promoted it
  ([ADR-047](../decisions.d/ADR-047.md), kind 1: a dropped clause the source asserts). The non-adaptive
  route does not transfer as it stands, since Lemma 39 fails for adaptive
  procedures. Proposed until a proof is read or re-derived.
---

# THEORY-1170: A convex map between two scenarios' model sets is induced by a classical adaptive procedure exactly when some non-contextual model of the corresponding adaptive hom scenario induces it

## Source

Barbosa, Karvonen and Mansfield, *Closing Bell* ([LIT-845](../literature.d/LIT-845.md), arXiv v2),
§6.2, as read in [NOTE-650](../notes.d/NOTE-650.md). The paper states the adaptive analogue of its
Theorem 44 and gives no proof.

## What is asserted

[THEORY-174](THEORY-174.md) holds the non-adaptive statement, re-derived: a convex map
between model sets is induced by a mixture of non-adaptive procedures
exactly when some non-contextual model of the hom scenario [S, T] that
satisfies its predicate induces it. §6.2 asserts the same for adaptive
procedures, in which the source measurements an agent makes may depend on
outcomes already seen, as in the comonadic simulations of [LIT-847](../literature.d/LIT-847.md).

## What this does not say

- **That the non-adaptive proof carries over.** Theorem 40, the
  characterisation of deterministic procedures, does not transfer to
  adaptive ones, because its key lemma (Lemma 39, least supports) fails
  for them (§6.2). Whether the short argument for Theorem 44 survives
  depends on how the adaptive hom scenario is defined, which the paper
  sketches without detail.
- **Anything about the preorder.** [LIT-847](../literature.d/LIT-847.md) Theorem 20 shows adaptive
  simulation is the same preorder as convertibility by free operations
  ([THEORY-720](THEORY-720.md)). That orders models; it does not say which maps are
  simulations.
