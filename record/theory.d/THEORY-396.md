---
number: 396
status: Active
formerly:
- THEORY-tmpi8kfq
title: 'Every Lipschitz map from an n-point metric space into any Banach space extends to any containing space with Lipschitz constant at most C log n/log log n times its own, by averaging over random partitions at every scale, and every n-point subset of L₂ extends into any Banach space at C√(log n) after Johnson–Lindenstrauss dimension reduction; for maps into Hilbert space this is no improvement on K√(log n), and whether √(log n) suffices for every target is left open'
version: 1
tags:
- mathematics
date: '2026-10-16'
source:
- LIT-1152
presupposes:
- THEORY-397
summary: >-
  Lee and Naor (2005), [LIT-1152](../literature.d/LIT-1152.md), read in [NOTE-927](../notes.d/NOTE-927.md) from the authors'
  January 2004 preprint. Theorem 1.10 (Theorem 5.1(4)): ae(X) ≤ C log n/log log n
  for every n-point metric space X, bounding the extension constant over every
  superspace and every Banach target at once, improving Johnson, Lindenstrauss
  and Schechtman's C log n. Theorem 1.12: eₙ(L_p, Z) ≤ C(p)(log n)^{1/p} for
  1 < p ≤ 2, C√(log n) at p = 2, through the Johnson–Lindenstrauss lemma and
  e(ℓ₂ᵈ, Z) ≤ C√d. For Hilbert targets Johnson and Lindenstrauss's K√(log n)
  ([THEORY-392](THEORY-392.md)) stays the better bound, and the paper states as open
  whether O(√(log n)) holds for every metric domain and normed target.
---

# THEORY-396: Every Lipschitz map from an n-point metric space into any Banach space extends to any containing space with Lipschitz constant at most C log n/log log n times its own, by averaging over random partitions at every scale, and every n-point subset of L₂ extends into any Banach space at C√(log n) after Johnson–Lindenstrauss dimension reduction; for maps into Hilbert space this is no improvement on K√(log n), and whether √(log n) suffices for every target is left open

## Source

Lee and Naor (2005), [LIT-1152](../literature.d/LIT-1152.md), *Inventiones Mathematicae* 160(1):
59–95, read in [NOTE-927](../notes.d/NOTE-927.md) from the authors' preprint of January 2004
(30 pages, posted on Lee's page). Theorem numbers are the preprint's.
Filed for later use; it answers no question of the record's yet.

## What was actually shown

**The quantities.** e(X, Y, Z) is the least K such that every Lipschitz
f: X → Z extends to Y with ‖f̃‖_Lip ≤ K‖f‖_Lip. eₙ(Y, Z) is its sup over
|X| ≤ n. ae(X), the absolute extendability constant, is its sup over every
Y ⊇ X and every Banach space Z. So ae(X) ≤ c for all n-point X implies
eₙ(Y, Z) ≤ c for every Y and Z.

**The mechanism (Lemma 2.1, Theorem 4.1).** A K-gentle partition of unity
Ψ with selector γ into X, one with
∫ d(γ(ω), x)|Ψ(ω, x) − Ψ(ω, y)| dμ(ω) ≤ K d(x, y), gives the extension
f̃(x) = ∫ f(γ(ω)) Ψ(ω, x) dμ(ω) with ‖f̃‖_Lip ≤ 3K‖f‖_Lip, into any closed
convex subset of a Banach space. Random partitions of Y at every scale,
weighted by a bump in d(x, X) and normalized, give such a Ψ.

**n-point domains (Theorems 3.17 and 4.3, Theorem 1.10).** For finite X,
a random-ball partition at scale ∆ (centres drawn by counting measure on
X, radius uniform in [2∆, 4∆]) splits x and y with probability at most
(2d(x, y)/∆)[1 + log(|B_X(x, 5∆)|/|B_X(x, ∆)|)]. Spreading the bump over
M scales makes those logarithms telescope to at most log m, at a cost
5^{2M}/M²; Corollary 4.5 gives O(5^{2M}/M² + (log m)/M), and M ≈ log log m
gives a C(log m/log log m)-gentle partition of unity. Hence
ae(X) ≤ C log n/log log n for every n-point metric space X. The paper
calls this "an asymptotic improvement over" eₙ(Y, Z) ≤ C log n of
Johnson, Lindenstrauss and Schechtman. It holds for Banach targets only;
the paper says the proof does not transfer to barycentric ones.

**Hilbert domains (Theorem 1.12).** For 1 < p ≤ 2 and every Banach space
Z, eₙ(L_p, Z) ≤ C(p)(log n)^{1/p}. At p = 2: random rank-d operators T_ω
from the Johnson–Lindenstrauss proof, d ≈ (4/c) log n, keep every
pairwise distance of X from shrinking by more than ½ with probability at
least ½. On each such ω, f ∘ T_ω⁻¹ is extended from T_ω(X) into Z by
e(ℓ₂ᵈ, Z) ≤ C√d (Theorem 1.11, from Lemma 3.16's (ε, 1/(2√d))-separating
partitions), at (4C/√c)√(log n)‖f‖_Lip; averaging over ω needs only
∫‖T_ω z‖ dP = O(‖z‖₂). For 1 < p < 2, Marcus and Pisier's p-stable maps
into L₂ lose a further (log n)^{1/p−1/2}.

**A lower bound for other targets (Lemma 1.13, sketched in Remark 5.3).**
For 2 < p < ∞, eₙ(L₂, L_p) ≥ C(log n/log log n)^{(p−2)/p²}. So
supₙ eₙ(L₂, Z) is infinite for some Banach Z, answering a question of
Johnson–Lindenstrauss and Johnson–Lindenstrauss–Schechtman. The exponent
is at most 1/8.

**What could have come out otherwise.** An n-point metric space X, a
superspace Y and a Banach target Z with no extension of constant
O(log n/log log n) would refute Theorem 1.10; an n-point subset of L₂ and
a Banach Z with no extension of constant O(√(log n)) would refute
Theorem 1.12. Both proofs were read in full in the reading.

## What this does not say

- **Anything better than K√(log n) for maps into Hilbert space.** For
  Z = L₂, Theorem 1.10's C log n/log log n is weaker than Johnson and
  Lindenstrauss's bound ([THEORY-392](THEORY-392.md)) by a factor of order
  √(log n)/log log n. The paper cites that bound (as 2√(log n)) and does
  not improve it.
- **That √(log n) is sharp, or that it is not.** The paper states as open
  whether eₙ(X, Z) = O(√(log n)) for every metric space X and normed space
  Z, and says "All known lower bounds fail to beat the '√(log n)
  barrier.'" It adds no lower bound for Hilbert targets; the
  (log n/log log n)^{1/2} of Johnson and Lindenstrauss is the one it
  cites. For Hilbert targets their (log log n)^{1/2} gap stands.
- **That log n/log log n is the right order for Banach targets.** No lower
  bound above √(log n) is given.
- **Anything about separated domains.** The bound in D/ε of
  [THEORY-398](THEORY-398.md) is neither cited nor implied; the two are incomparable
  (an equilateral set has D/ε = 1).
- **Explicit constants.** C is universal and not computed; the
  Johnson–Lindenstrauss constant 2 in the paper's Theorem 1.2 is the
  paper's citation, not something it proves.

## Connections

- [THEORY-392](THEORY-392.md): the same quantity for Hilbert targets, by dimension
  reduction, Kirszbraun and the non-linear Hahn–Banach theorem. This
  account widens the target to every Banach space with a different
  mechanism, at a worse rate, and leaves that account's open question
  where it was. Not filed as `extends`, because the mechanism of
  Theorem 1.10 is not a refinement of that one, and not as a rival,
  because both bounds hold.
- [THEORY-397](THEORY-397.md): Theorem 1.12 takes the dimension-reduction lemma as a
  premise, as Johnson and Lindenstrauss's Theorem 1 did, needing only its
  lower side for every pair and its upper side on average.
- [THEORY-400](THEORY-400.md): the paper's bounds for doubling, minor-free and
  Euclidean domains, by the same partitions.
- [THEORY-398](THEORY-398.md): the bound by diameter over separation, which this
  paper does not address.
