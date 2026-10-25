---
number: 940
status: Proposed
formerly:
- THEORY-tmpq0hjk
promote_when: >-
  A checked re-derivation recorded in this file, which the reading made
  (NOTE-1146) and which ADR-047 counts toward promotion. It is refuted
  by a finite symmetric zero-sum game with a Nash clustering in which some
  earlier cluster has negative relative population performance against a
  later one, or in which a strategy beating every member of a population
  containing a whole cluster C_i lies in C_i or a later cluster. Empirical
  results on cluster sizes or on the spinning-top shape neither promote
  nor refute it.
title: 'In a finite symmetric zero-sum game, successive Nash clusters are weakly ordered by relative population performance, and a strategy that beats every member of a population containing a whole cluster lies in a strictly earlier cluster'
version: 1
tags:
- game-theory
- mathematics
date: '2026-10-24'
source:
- LIT-1504
- LIT-1509
summary: >-
  Czarnecki et al. (2020), [LIT-1504](../literature.d/LIT-1504.md), Definition 3 and Theorems 2–3,
  read from arXiv v2 in [NOTE-1146](../notes.d/NOTE-1146.md), proofs followed and re-derived. RPP
  is the population value of Balduzzi et al. (2019), [LIT-1509](../literature.d/LIT-1509.md). It holds
  for any Nash clustering of any finite symmetric zero-sum game and does
  not depend on the spinning-top hypothesis. The order is weak, since
  clusters can tie, and cardinal, since RPP uses payoff magnitudes.
---
<!-- inactive-ok-file: NOTE-1146 — the reading this is filed from -->
<!-- inactive-ok-file: CLAIM-451 — Proposed; named in prose, nothing here rests on it -->

# THEORY-940: In a finite symmetric zero-sum game, successive Nash clusters are weakly ordered by relative population performance, and a strategy that beats every member of a population containing a whole cluster lies in a strictly earlier cluster

## Source

Czarnecki, Gidel, Tracey, Tuyls, Omidshafiei, Balduzzi & Jaderberg,
[LIT-1504](../literature.d/LIT-1504.md), read in [NOTE-1146](../notes.d/NOTE-1146.md) from arXiv:2004.09468v2: Definition 3
and Theorems 2–3 (p. 7, proofs pp. 13–14). RPP is Definition 3 of
Balduzzi et al., [LIT-1509](../literature.d/LIT-1509.md).

## What was actually shown

- **Nash clustering.** C₁ is the support of a Nash equilibrium of the
  whole game. C₂ is the support of a Nash of the game restricted to what
  remains, and so on until nothing remains. With maximum-entropy
  equilibria at each step the clustering is unique.
- **Theorem 2.** With X_i the strategies left at step i, and C_j ⊂ X_i
  for j > i: RPP(C_i, C_j) ≥ RPP(C_i, X_i), since a smaller opposing set
  cannot lower the value. RPP(C_i, X_i) = 0, because C_i can play the
  Nash of X_i and so holds X_i to zero, while X_i can mirror it.
- **Theorem 3.** Let the population contain C_i, and let π beat every
  member. If π lay in a later cluster C_k, then RPP(C_i, C_k) ≤
  max_{π_j ∈ C_i} f(π_j, π) < 0, contrary to Theorem 2. π is not in C_i,
  because f(π, π) = 0. So π lies in an earlier cluster.

The reader re-derived both. Each is a few lines on the value of a
zero-sum game.

## What this does not say

- **That every member of an earlier cluster beats every member of a later
  one.** The order is between clusters as populations.
- **That the order is strict.** Clusters can tie at RPP = 0.
- **Anything about real games.** Neither theorem uses the spinning-top
  shape. Both hold in rock-paper-scissors, which is one cluster, and in
  the disc game.
- **Anything ordinal.** Clusters are Nash supports, which depend on payoff
  magnitudes. A monotone transform of payoffs can change them.

## Connections

A cardinal layering of a cyclic record: the cycling stays inside clusters
and the order runs between them. That parallels the ordinal condensation
reading in [NOTE-1156](../notes.d/NOTE-1156.md). Theorem 3 is a sufficient condition for escaping
a cycle: beat its whole class, not its latest member. That bears on
[CLAIM-451](../claims.d/CLAIM-451.md)'s accommodation ([NOTE-1146](../notes.d/NOTE-1146.md)).
