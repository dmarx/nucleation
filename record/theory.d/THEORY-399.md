---
number: 399
status: Active
formerly:
- THEORY-tmpup7x5
title: 'Storing every inner product of n points of the unit ball of R^k to additive error ε takes Θ(n log n/ε²) bits once k ≥ log n/ε² and Θ(nk log(2 + log n/(ε²k))) below, for 1/n^0.49 ≤ ε ≤ 0.1, and comparing these counts across dimensions shows that some n such points cannot be mapped into fewer than Ω(min{k, log(2 + ε²n)/ε²}) dimensions with additive error ε for every ε ≥ 2/√n; this is a worst-case lower bound with unstated constants, the small-ε bit count is open for k above that dimension, and no one-family embedding that small is proved'
version: 1
tags:
- mathematics
- information-theory
date: '2026-10-16'
source:
- LIT-1151
extends:
- THEORY-395
answers:
- QUESTION-251
summary: >-
  Alon and Klartag (2017), [LIT-1151](../literature.d/LIT-1151.md), read in [NOTE-929](../notes.d/NOTE-929.md) from arXiv v4.
  Theorem 1.1 gives the bits of an additive ε-distance sketch for every k
  when 1/n^0.49 ≤ ε ≤ 0.1, by a volume argument above and a packing of net
  points against random probes below. Since an embedding is a sketch,
  Corollary 2.1 re-proves Larsen and Nelson's bound in that range, and
  Corollary 2.3, using the Gaussian correlation inequality in place of a
  union bound, extends it to every ε ≥ 2/√n with log(2 + ε²n) in place of
  log n. The dimension statements are for additive error on squared
  distances of points of norm at most 1; the relative form for small ε
  follows but is not stated. The matching upper bound for one set is open.
---

# THEORY-399: Storing every inner product of n points of the unit ball of R^k to additive error ε takes Θ(n log n/ε²) bits once k ≥ log n/ε² and Θ(nk log(2 + log n/(ε²k))) below, for 1/n^0.49 ≤ ε ≤ 0.1, and comparing these counts across dimensions shows that some n such points cannot be mapped into fewer than Ω(min{k, log(2 + ε²n)/ε²}) dimensions with additive error ε for every ε ≥ 2/√n; this is a worst-case lower bound with unstated constants, the small-ε bit count is open for k above that dimension, and no one-family embedding that small is proved

## Source

Alon and Klartag (2017), [LIT-1151](../literature.d/LIT-1151.md), FOCS 2017, read in [NOTE-929](../notes.d/NOTE-929.md)
from arXiv 1610.00239v4 of 2 April 2017. Theorem numbers are that copy's.

## What was actually shown

**The problem.** X is n points of norm at most 1 in R^k, n ≥ k ≥ 1. An
ε-distance sketch recovers any pair's squared distance and inner product
to within an additive ε. f(n, k, ε) is the least number of bits of one.

**The bit count (Theorem 1.1).** For 1/n^0.49 ≤ ε ≤ 0.1, f(n, k, ε) is
Θ(n log n/ε²) for log n/ε² ≤ k ≤ n; Θ(nk log(2 + log n/(ε²k))) for
log n ≤ k ≤ log n/ε²; and Θ(nk log(1/ε)) for k ≤ log n. The upper bound
counts ε-separated Gram matrices by volume: random points near any
target configuration hit it with probability at least c^{nk}, and the
events are disjoint (Lemmas 3.1–3.2). The lower bound fixes n/2 random
probe points that tell apart any two points of a δ-separated net by their
inner products, and counts ordered choices of n/2 net points (Lemma 5.1).
Theorem 4.1 makes the upper bound algorithmic: JL into 40 log n/ε²
dimensions, unbiased randomized rounding of each coordinate, O(1) bits
per coordinate, correct with probability at least 1 − 2/n³.

**Small ε (Theorem 2.2).** For ε ≥ 2/√n and t = log(2 + ε²n)/ε²,
f(n, k, ε) = Θ(nk log(2 + t/k)) for log(2 + ε²n) ≤ k ≤ t and
Θ(nk log(1/ε)) below; for t ≤ k ≤ n only Ω(nt) ≤ f ≤ O(n log n/ε²) is
shown. The upper bound replaces the union bound over pairs with Lemma 6.2,
which multiplies slab probabilities by Hargé's inequality and the
Khatri–Šidák lemma.

**Dimension (Corollaries 2.1 and 2.3).** A map into ℓ dimensions with
additive error ε on squared distances is a sketch, so f must not drop by
more than the dimension allows. For 1/n^0.49 ≤ ε ≤ 0.1, a reduction into
ℓ ≤ ck dimensions exists only if ℓ = Ω(log n/ε²), and the same holds for
relative error (1 − ε)|x_i − x_j|² ≤ |y_i − y_j|² ≤ (1 + ε)|x_i − x_j|²
(Corollary 2.1). For every ε ≥ 2/√n, a reduction into ℓ ≤ ck dimensions
exists only if ℓ = Ω(log(2 + ε²n)/ε²) (Corollary 2.3, additive only). In
§1.2's words, no reduction below t is possible for n ≥ k ≥ t, and for
k < t or smaller ε no reduction by more than a constant factor. The maps
are arbitrary: the images may depend on the whole set.

**What could have come out otherwise.** A sketch of o(n log n/ε²) bits
for every n-point set at k = log n/ε², or an embedding of the hard set
into o(min{k, t}) dimensions, would refute it. The counting proofs are
short and were followed step by step; the step from bits to dimension is
a few lines of §7.

## What this does not say

- **That every set needs this many dimensions.** It is a worst case, shown
  by existence, with unstated constants.
- **The relative form for small ε, in the paper's words.** Corollary 2.3
  is additive. On points of norm at most 1 relative error ε implies
  additive error 4ε, so the relative lower bound follows ([NOTE-929](../notes.d/NOTE-929.md),
  my observation). The converse does not.
- **That log(2 + ε²n)/ε² dimensions suffice for one set.** The
  Johnson–Lindenstrauss lemma still needs log n/ε². Only a bipartite
  version reaches t ([THEORY-393](THEORY-393.md)), and its upper bound on bits for
  k ≥ t is open (Theorem 2.2, first bullet).
- **Anything about relative-error sketches**, beyond that these lower
  bounds hold for them; a log gap remains there (§7).
- **A bound on nearly orthogonal sets.** The hard set is probes plus net
  points, not an incoherent family.
- **Anything about maps into more dimensions**, where it is vacuous.

## Connections

- [THEORY-395](THEORY-395.md): it extends that account's lower bound from
  ε > lg^0.5001 n/√min{n, d} to every ε ≥ 2/√n, with log(2 + ε²n) in place
  of lg(ε²n), and gives a second proof in the range ε ≥ 1/n^0.49.
- [THEORY-397](THEORY-397.md): the upper bound it matches for ε ≥ 1/n^0.49, used here
  as the first step of the sketch.
- [QUESTION-120](../questions.d/QUESTION-120.md): on the distances thread the bit count is the log of a
  family's size, the ε-separated Gram matrices, and the dimension is that
  count per point over O(1) bits per coordinate. For small ε the log is of
  2 + ε²n, not of the n² pairs a union bound counts, because a product of
  slab probabilities replaces the union bound (my observation).
- [THEORY-393](THEORY-393.md): the paper's other result, the bipartite reduction to t
  dimensions.
