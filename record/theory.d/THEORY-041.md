---
number: 41
status: Active
formerly:
- THEORY-tmpwitpu
title: 'Birkhoff and von Neumann proposed the modular law, not orthomodularity, and proved it fails for closed subspaces in infinite dimension; Husimi used the orthomodular identity only as an unnamed proof step'
version: 1
tags:
- logic
- quantum-foundations
- mathematics
date: '2026-09-30'
source:
- LIT-306
- LIT-357
summary: >-
  Birkhoff & von Neumann (1936), [LIT-306](../literature.d/LIT-306.md) — the lattice of closed subspaces
  is orthocomplemented and not distributive. They propose modularity (L5),
  motivated by a dimension function, and give an explicit
  infinite-dimensional pentagon that breaks it. The word "orthomodular"
  does not occur. Husimi (1937), [LIT-357](../literature.d/LIT-357.md), derives modularity as the
  parallelogram law under a finite-chain assumption and uses the
  orthomodular identity as a step without naming it. Citing either paper
  for "the orthomodular lattice of quantum logic" misattributes it.
---

# THEORY-041: Birkhoff and von Neumann proposed the modular law, not orthomodularity, and proved it fails for closed subspaces in infinite dimension; Husimi used the orthomodular identity only as an unnamed proof step

## Source

Birkhoff & von Neumann (1936), [LIT-306](../literature.d/LIT-306.md), §§6, 10–12, 15, fn. 33 ([NOTE-275](../notes.d/NOTE-275.md)). Husimi (1937), [LIT-357](../literature.d/LIT-357.md), pp. 773, 780–784 ([NOTE-312](../notes.d/NOTE-312.md)).

## What was actually shown

Birkhoff and von Neumann identify experimental propositions with closed subspaces. This rests on a stated Postulate (§6), not a theorem. Meet is intersection, join is closed span and negation is orthogonal complement. The lattice satisfies L1–L4 and the orthocomplement laws L71–L73. It fails distributivity L6, and the witness is a symmetric state and two half-space wave packets (§10). The replacement they propose is the modular law L5 (§11). They motivate it by a dimension function obeying d(a) + d(b) = d(a∩b) + d(a∪b), which "partially describe[s] the formal properties of probability". They show that finite-dimensional subspaces satisfy L5. They show that closed subspaces of infinite-dimensional Hilbert space do not, with an explicit construction that generates Dedekind's pentagon (§11, Fig. 1). With finite dimension and irreducibility added, the lattice is a projective geometry (§12). The Appendix proves that its orthocomplementations are the polarities of definite Hermitian forms. To keep L5 in infinite dimensions they prefer von Neumann's continuous geometries to Hilbert space (§15, fn. 33).

Husimi sets out to answer their open question: what physical reason is there for L5? Under Assumption F (chains of uniformly bounded length), he shows that the modular law is equivalent to the parallelogram law |P| + |Q| − |P∩Q| = |P∪Q|. That law is the addition law of probability in the uniform "virgin" state (p. 782). He then derives it from the covering property of points. The step that makes this work is "S + P∩Q = R" for R ⊃ P∩Q, justified as "traditional logic in any classical part" (p. 784). That step is the orthomodular identity. It is never stated as an axiom or named.

## What this does not say

- That the full lattice of closed subspaces is orthomodular. That is the standard modern fact, but no held reading proves it. Kalmbach and Piron, the usual sources, are not in the record.
- That modularity implies orthomodularity for ortholattices. That is also standard, and neither paper states it. So in finite dimension BvN's modular picture already contains orthomodularity, but only through a fact the record does not source.
- That BvN's identification of propositions with subspaces is derived. It is a Postulate, motivated by the conjecture that all Hermitian operators are observables, and superselection denies that conjecture (see the superselection claim in this group).
- That Husimi's derivation reaches actual quantum mechanics. Assumption F, by his own account, "does not hold in the more important cases" (p. 773).

## Connections

- [LIT-298](../literature.d/LIT-298.md) (Kochen–Specker) drops the total lattice for a partial Boolean algebra over commuting propositions. That is one answer to BvN's question about the experimental meaning of meets of incompatible propositions.
- [LIT-262](../literature.d/LIT-262.md) (van Rijsbergen, [NOTE-239](../notes.d/NOTE-239.md)) inherits the BvN dictionary for information retrieval. [LIT-340](../literature.d/LIT-340.md) (Aerts–Gabora) posits an orthocomplemented lattice of contexts.
- [THEORY-017](THEORY-017.md): BvN fn. 34 says the inclusion relation fixes dimensions but not complements. The orthocomplement, that is the inner product, is structure beyond the order.
