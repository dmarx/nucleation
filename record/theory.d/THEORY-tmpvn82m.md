---
status: Active
title: 'Co-optimal transport between two data matrices of equal shape with uniform weights vanishes exactly when one is the other with its rows and its columns separately permuted, and its objective is unchanged when a pair of optimal plans is composed with any joint relabelling of rows and columns that leaves a matrix unchanged; its sample and feature couplings are therefore identified at best up to that joint symmetry group, which can exchange a block of samples together with its block of features though neither exchange alone is a symmetry, and the paper proves no uniqueness beyond it'
version: 1
tags:
- mathematics
- representation-learning
date: '2026-10-29'
source:
- LIT-tmpbnbe3
summary: >-
  Redko, Vayer, Flamary and Courty (2020), [LIT-tmpbnbe3](../literature.d/LIT-tmpbnbe3.md), Proposition 1,
  read in [NOTE-tmpghx1t](../notes.d/NOTE-tmpghx1t.md); the composition step is elementary and was
  checked by enumeration on small matrices, including a two-community
  block matrix with 32 tied optimal plan pairs. Active. It does not say
  real response matrices have exact symmetries; noisy ones give
  near-ties, which is the practical form of the threat.
---

# THEORY-tmpvn82m: Co-optimal transport between two data matrices of equal shape with uniform weights vanishes exactly when one is the other with its rows and its columns separately permuted, and its objective is unchanged when a pair of optimal plans is composed with any joint relabelling of rows and columns that leaves a matrix unchanged; its sample and feature couplings are therefore identified at best up to that joint symmetry group, which can exchange a block of samples together with its block of features though neither exchange alone is a symmetry, and the paper proves no uniqueness beyond it

## Source

Redko, Vayer, Flamary and Courty (2020), [LIT-tmpbnbe3](../literature.d/LIT-tmpbnbe3.md), Proposition 1, p. 4,
proof pp. 11–13 of arXiv 2002.03731v3; read in [NOTE-tmpghx1t](../notes.d/NOTE-tmpghx1t.md).

## What was actually shown

**The paper's result.** For L = |·|^p, n = n′, d = d′ and uniform weights,
"COOT(X, X′) = 0 iff there exists a permutation of the samples σ1 ∈ Sn and
of the features σ2 ∈ Sd, s.t, ∀i, k Xi,k = X′σ1(i),σ2(k)" (p. 4). The proof
uses the fact that a bilinear program over two Birkhoff polytopes has an
optimal pair of permutations (pp. 3–4, 13).

**The step that follows.** The objective Σ L(X_{i,k}, X′_{j,l}) π^s_{i,j}
π^v_{k,l} depends on the plans only through which entries they pair. Let
P, Q be permutations of the rows and columns of X′ with X′ = P X′ Qᵀ. Then
(π^s Pᵀ, π^v Qᵀ) pairs X_{i,k} with entries equal to those (π^s, π^v)
paired, so it costs the same. The same holds for symmetries of X. Every
optimal pair therefore comes with its orbit under the joint symmetry group
{(P, Q): P X′ Qᵀ = X′}. That group can contain (P, Q) with neither (P, I)
nor (I, Q) in it.

**Checked by enumeration** (all permutation pairs, which is exact for these
sizes and weights):

- A generic random 4 × 3 matrix against a row- and column-permuted copy:
  one optimal pair, cost 0.
- The matrix with rows e₁, e₂, e₃ and (½, ½, ½) against itself: six optimal
  pairs, each permuting rows and columns together. Swapping two rows alone
  costs 1/3.
- A 4 × 4 matrix of two communities, each of two samples answering its own
  two features, against itself: 32 zero-cost pairs of 576, that is 4 ×
  4 × 2. The factor 2 is the exchange of one community's samples and
  features together with the other's.
- The same matrix with noise of sd 0.05: one optimal pair, but the next
  best costs only 5.4 × 10⁻⁴ more.

**What could have failed.** COOT's raw-feature cost could have made the
plans unique whenever the matrices are generic. It does for a generic
matrix, but any exact joint block symmetry leaves a tie the objective
cannot break.

## What this does not say

- **That a row is ever matched with a column.** π^s couples samples with
  samples, π^v features with features. The "joint swap" is a relabelling
  inside each side, carried out on both sides together.
- **That COOT is as ambiguous as GW.** On squared distances GW cannot
  separate a configuration from its rotations and reflections. COOT on raw
  features can ("not invariant neither to feature rotations nor to the
  change of signs", pp. 5–6). Its ambiguity is the generally smaller
  permutation-symmetry group of the matrix itself (compare [THEORY-tmpa43ta](THEORY-tmpa43ta.md)).
- **That the optimum can be found.** Exact COOT is NP-hard in general (p.
  4), and block coordinate descent reaches block-wise optima. In a check
  on a random 5 × 4 pair, 12% of 200 random starts reached the global value.
- **A stability bound.** Near-symmetries give near-ties. How far noise
  must move a plan before it changes is not studied in the paper.
- **That it holds for unequal sizes or non-uniform weights as stated.** The
  zero case is proved only for equal sizes and uniform weights. The
  paper's claim that COOT is otherwise "always strictly positive" (p. 13)
  is false when rows or columns are duplicated ([NOTE-tmpghx1t](../notes.d/NOTE-tmpghx1t.md)).
