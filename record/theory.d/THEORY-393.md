---
number: 393
status: Active
formerly:
- THEORY-tmpbh0v2
title: 'Any two families of n vectors of norm at most 1 have images in ⌊C log(2 + ε²n)/ε²⌋ dimensions whose cross inner products ⟨x_i, y_j⟩ are each within an additive ε of the originals, found by a randomized polynomial-time algorithm, which for small ε is below the log n/ε² of the Johnson–Lindenstrauss lemma; only cross products are kept, the new vectors'' norms are not bounded, and whether one set can be embedded that small is open'
version: 1
tags:
- mathematics
date: '2026-10-16'
source:
- LIT-1151
summary: >-
  Alon and Klartag (2017), [LIT-1151](../literature.d/LIT-1151.md), read in [NOTE-929](../notes.d/NOTE-929.md) from arXiv v4.
  Theorem 1.2 answers, in a bipartite form, Larsen and Nelson's question
  whether log n can become log(2 + ε²n) in the JL lemma. The proof is
  convex geometry: Khatri–Šidák bounds the Gaussian measure of a body of
  slabs, and a weakened low M*-estimate puts a random t-dimensional
  subspace close to every scaled a_i. Conjecture 2.4, the same with norms
  O(1), is proved only for t of order n (Theorem 2.5). It is not an
  embedding of one point set and says nothing about distances.
bears_on:
- QUESTION-120
---

# THEORY-393: Any two families of n vectors of norm at most 1 have images in ⌊C log(2 + ε²n)/ε²⌋ dimensions whose cross inner products ⟨x_i, y_j⟩ are each within an additive ε of the originals, found by a randomized polynomial-time algorithm, which for small ε is below the log n/ε² of the Johnson–Lindenstrauss lemma; only cross products are kept, the new vectors' norms are not bounded, and whether one set can be embedded that small is open

## Source

Alon and Klartag (2017), [LIT-1151](../literature.d/LIT-1151.md), FOCS 2017, read in [NOTE-929](../notes.d/NOTE-929.md)
from arXiv 1610.00239v4 of 2 April 2017. Theorem numbers are that copy's.

## What was actually shown

**The statement (Theorem 1.2).** There is an absolute C such that for any
a₁ … a_n, b₁ … b_n ∈ R^n of Euclidean norm at most 1, any 0 < ε < 1 and
t = ⌊C log(2 + ε²n)/ε²⌋, there are x₁ … x_n, y₁ … y_n ∈ R^t with
|⟨x_i, y_j⟩ − ⟨a_i, b_j⟩| ≤ ε for all i, j. For ε ≥ 1/n^0.49 this is the
JL order; for smaller ε it is below it, and for ε below about 1/√n it is
trivial, since t exceeds n.

**The proof (§6.4).** The body K of x with |⟨x/√t, b_j⟩| ≤ c₀ε for every
j has Gaussian measure at least e^{−c₀t}, by the Khatri–Šidák lemma, at
this t. Theorem 6.8 weakens the low M*-estimate's hypothesis from measure
1/2 to that, so a random t-dimensional subspace E meets v + CK for every
|v| ≤ √t (Corollary 6.9). With U a rotation taking R^t onto E, each x_i
is found by linear programming so that Ux_i lies in E and in √t a_i + CK,
and each y_j is the first t coordinates of U⁻¹b_j, scaled. A random
rotation works with probability 1 − C exp(−ct), so the algorithm is
randomized and polynomial.

**Toward bounded norms.** Conjecture 2.4 asks for ‖x_i‖, ‖y_i‖ ≤ O(1).
Theorem 2.5 proves it when t is of order n: m ≥ n vectors of each family in
R^{2n} are matched within ε by scaled Gaussian vectors in R^n with
|X̄_i| + |Ȳ_i| ≤ C₃, with probability at least exp(−C₂nm), when
n ≥ C₁ log(2 + ε²m)/ε². It is tight for m = 2n, ε = C/√n and an
orthonormal basis, because a matrix within 1/(2√n) of the 2n × 2n
identity in each entry has rank above n. Iterating it fails because the
norms grow (§7).

**What could have come out otherwise.** Two families of n vectors whose
cross Gram matrix cannot be matched to ε by any rank-t factorization
would refute it. The proof rests on cited theorems of asymptotic convex
geometry, read in outline in [NOTE-929](../notes.d/NOTE-929.md).

## What this does not say

- **A Johnson–Lindenstrauss lemma for one set.** It keeps ⟨x_i, y_j⟩
  between two families, not the inner products within one family and not
  distances. Setting b = a does not give x_i = y_i.
- **Bounded norms.** That is Conjecture 2.4, open except at t of order n.
  With unbounded norms the vectors are not points of a ball, and the
  paper's sketch argument cannot use them.
- **Relative error.** The error is additive.
- **That log(2 + ε²n)/ε² is necessary for this bipartite problem.** The
  matching lower bound, [THEORY-399](THEORY-399.md), is for one family's squared
  distances, though §7's perturbed-identity remark gives tightness at
  ε of order 1/√n.
- **A bound on superposition.** With a_i = b_i = e_i it gives n
  nearly orthogonal write and read pairs in t dimensions, below log n/ε²
  for small ε (my observation), but not unit vectors, so not superposition
  as [NOTE-278](../notes.d/NOTE-278.md) describes it.

## Connections

- [THEORY-397](THEORY-397.md): the JL upper bound, log n/ε² for one set, which this
  beats for small ε only in bipartite form and by a different mechanism,
  convex geometry rather than concentration and a union bound.
- [THEORY-399](THEORY-399.md): the lower bound from the same paper; together they
  bracket t for small ε, the lower bound for one set and the upper bound
  for two.
- [QUESTION-120](../questions.d/QUESTION-120.md): on the distances thread it suggests that for small ε
  the right threshold is log(2 + ε²n)/ε², not the union bound's log n/ε².
  On superposition, see above.
