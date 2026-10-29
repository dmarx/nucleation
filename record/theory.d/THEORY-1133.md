---
number: 1133
status: Active
formerly:
- THEORY-tmpa43ta
title: 'The Gromov–Wasserstein objective between two spaces depends on each only through its within-space similarity matrix and weights, so every transformation of a space that preserves them, a single orthogonal map or per-vector rescaling under cosine similarity, leaves every coupling''s cost unchanged, and any coupling composed with a symmetry of either structure costs exactly what it did; GW can therefore identify a correspondence only up to the automorphisms of the two similarity structures, and on symmetric data it cannot choose between branches or categories that the symmetry exchanges'
version: 1
tags:
- mathematics
- representation-learning
date: '2026-10-29'
source:
- LIT-1818
- LIT-1805
summary: >-
  Alvarez-Melis and Jaakkola (2018), [LIT-1818](../literature.d/LIT-1818.md), use the GW objective
  (their eq. 8) for word translation and do not state its ambiguity;
  read in [NOTE-1336](../notes.d/NOTE-1336.md). The invariance follows in two lines from the
  objective's form and was checked numerically, including a symmetric
  tree on which a branch-swapping coupling costs exactly what the true
  one does. Active: elementary and checked. It does not say how large
  the symmetry group of real embedding spaces is, and exact symmetries
  are rare in noisy data; near-symmetries give near-ties instead.
---
<!-- inactive-ok-file: CLAIM-135 LIT-1813 LIT-1804 — Proposed, Open or Deferred; the entries this reading bears on, cited as open -->

# THEORY-1133: The Gromov–Wasserstein objective between two spaces depends on each only through its within-space similarity matrix and weights, so every transformation of a space that preserves them, a single orthogonal map or per-vector rescaling under cosine similarity, leaves every coupling's cost unchanged, and any coupling composed with a symmetry of either structure costs exactly what it did; GW can therefore identify a correspondence only up to the automorphisms of the two similarity structures, and on symmetric data it cannot choose between branches or categories that the symmetry exchanges

## Source

Alvarez-Melis and Jaakkola (2018), [LIT-1818](../literature.d/LIT-1818.md), §3.1, eq. (8) and
Algorithm 1, pp. 3–5 of arXiv 1809.00013v1; read in [NOTE-1336](../notes.d/NOTE-1336.md). The
equivalence with a global-invariance OT problem is from Alvarez-Melis,
Jegelka and Jaakkola (2019), [LIT-1805](../literature.d/LIT-1805.md), Lemma 4.3 ([NOTE-1333](../notes.d/NOTE-1333.md)).

## What was actually shown

**The objective.** For within-space matrices C (n × n) and C′ (m × m),
weights p, q and a loss L, GW(C, C′, p, q) = min over couplings Γ with
marginals p, q of E(Γ) = Σ_{ijkl} L(C_ik, C′_jl) Γ_ij Γ_kl (eq. 8).

**Invariance to re-embedding.** E depends on the embeddings only through
C and C′. Any map of a space that leaves its matrix unchanged leaves E(Γ)
unchanged for every Γ. With C = cos(X, X), as in the paper's Algorithm 1,
that includes every orthogonal Q and every positive diagonal rescaling S
of the vectors: cos(QYS, QYS) = cos(Y, Y). A numerical check over five
random couplings (d = 10, n = 40) gave |ΔE| ≤ 3 × 10⁻¹⁷ for QY, YS and
QYS, and 0.07 for a generic linear map AY.

**Invariance to symmetries of the data.** Let σ be a permutation of the
target points with C′_{σ(j)σ(l)} = C′_jl and q_{σ(j)} = q_j, an
automorphism of (C′, q). Define Γ^σ_ij = Γ_{iσ(j)}. Then Γ^σ has the same
marginals, and E(Γ^σ) = Σ L(C_ik, C′_jl) Γ_{iσ(j)} Γ_{kσ(l)} = E(Γ) after
substituting j ↦ σ⁻¹(j), l ↦ σ⁻¹(l). The same holds on the source side.
So the set of minimisers is closed under Aut(C, p) × Aut(C′, q), and
nothing in the objective prefers one member of an orbit. The entropic
version used in practice adds −λH(Γ), which is also unchanged by
permuting columns, so it inherits the same symmetry.

**A worked case.** The tree with a root and three identical branches, each
a node with two leaves (ten nodes), has 3! · 2³ = 48 automorphisms. Under
shortest-path distances and squared loss, the identity coupling and the
coupling that swaps two branches both cost 1.3 × 10⁻¹⁵, zero to rounding.
Entropic GW on a randomly relabelled copy, from 20 random starts, ended 7
times at an automorphism of the tree and never at the true labelling. The
other 13 ended at local optima. Without symmetry, entropic GW recovered a
hidden permutation of a randomly rotated 60-point cloud in ℝ¹⁰ exactly.

**What could have failed.** The objective could have depended on the
embeddings by some route other than C, C′, p and q. Or the entropy term
could have broken the tie between members of an orbit. Neither happens.

## What this does not say

- **That real embedding spaces have exact symmetries.** Noisy data rarely
  do. What they have are near-symmetries, and these give near-ties, so
  the coupling is chosen by noise, the subset or the initialisation. How
  much of a real alignment is decided this way is not measured here, or
  in the paper.
- **That GW is worse than methods that estimate a registration.**
  Orthogonal Procrustes with OT has the same blind spot wherever the
  symmetry is a rotation of the cloud ([LIT-1805](../literature.d/LIT-1805.md)). Only information
  from outside the structure breaks it: anchors, frequency ranks, labels,
  or a feature cost as in fused GW ([LIT-1813](../literature.d/LIT-1813.md)).
- **That anchors solve the problem.** An anchor set breaks the tie only if
  no non-trivial symmetry fixes it. Anchors drawn from the symmetric part
  can leave it intact.
- **Anything about per-entity frames.** The arbitrary choice GW removes is
  a single transformation of each whole space. Its data are scalar
  relations, and those do not change under a change of frame at any node.
  It therefore cannot represent a connection between frames, or its
  holonomy (contrast [THEORY-1140](THEORY-1140.md)).
- **That a GW minimum is a correspondence of kinds.** The cost measures
  relational resemblance under the similarity chosen. Whether matched
  items are the same kind is a further question ([CLAIM-135](../claims.d/CLAIM-135.md)).
