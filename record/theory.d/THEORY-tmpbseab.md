---
status: Active
title: 'Every n-point metric space embeds in Euclidean space of O(log n) dimensions with distortion O(log n), by distances to random sets of every scale followed by Johnson–Lindenstrauss, and constant-degree expanders need distortion Ω(log n) in every ℓ_p with 1 ≤ p ≤ 2, of any dimension, so O(log n) is tight in the worst case; the constants are unspecified, the lower bound rests on Leighton and Rao''s flow–cut gap, and nothing is shown for trees or for p > 2'
version: 1
tags:
- mathematics
date: '2026-10-16'
source:
- LIT-tmp9g20z
- LIT-tmpwy0he
presupposes:
- THEORY-tmpns5kz
summary: >-
  Linial, London and Rabinovich (1995), [LIT-tmp9g20z](../literature.d/LIT-tmp9g20z.md), read in [NOTE-tmpetxcq](../notes.d/NOTE-tmpetxcq.md)
  from the authors' February 1995 manuscript. Theorem 3.2(1) states
  Bourgain's theorem ([LIT-tmpwy0he](../literature.d/LIT-tmpwy0he.md), unread): every n-point metric embeds in
  O(log n)-dimensional Euclidean space with distortion O(log n). The paper
  reproves the distortion with a randomized map into ℓ_p^{O(log² n)} built
  from distances to O(log n) random sets of each size 2ˡ, and gets the
  dimension from Johnson–Lindenstrauss. Proposition 4.2 shows that every
  embedding of a constant-degree expander into ℓ_p, 1 ≤ p ≤ 2, has
  distortion Ω(log n), from the expander's Ω(log n) gap between flow and
  cut. Together these answer Johnson and Lindenstrauss's Problem 4 in the
  negative, which the paper does not say.
---
<!-- inactive-ok-file: LIT-tmpwy0he — Unavailable; Bourgain's paper, whose theorem this account takes as Linial, London and Rabinovich state it -->

# THEORY-tmpbseab: Every n-point metric space embeds in Euclidean space of O(log n) dimensions with distortion O(log n), by distances to random sets of every scale followed by Johnson–Lindenstrauss, and constant-degree expanders need distortion Ω(log n) in every ℓ_p with 1 ≤ p ≤ 2, of any dimension, so O(log n) is tight in the worst case; the constants are unspecified, the lower bound rests on Leighton and Rao's flow–cut gap, and nothing is shown for trees or for p > 2

## Source

Linial, London and Rabinovich (1995), [LIT-tmp9g20z](../literature.d/LIT-tmp9g20z.md), *Combinatorica*
15(2): 215–245, read in [NOTE-tmpetxcq](../notes.d/NOTE-tmpetxcq.md) from the authors' 26-page
manuscript, "the final version of February 1995". Page and theorem
numbers are the manuscript's. Bourgain (1985), [LIT-tmpwy0he](../literature.d/LIT-tmpwy0he.md), is the
second source because Theorem 3.2(1) states his theorem. The record has
no copy of his paper and reads the theorem only as stated here. Filed for
later use. It answers JL's Problem 4, which the record holds in
[NOTE-tmpmv42v](../notes.d/NOTE-tmpmv42v.md), and no question of the record's yet.

## What was actually shown

**The measure.** An embedding φ has distortion ≤ c if d(x, y) ≥
‖φ(x) − φ(y)‖ ≥ d(x, y)/c for every pair (Definition 2.1). c_p(X) is the
least such c into ℓ_p of any dimension.

**The upper bound (Theorem 3.2(1), p. 6).** "Every n-point metric space
(X, d) can be embedded in an O(log n)-dimensional Euclidean space with an
O(log n) distortion", attributed to Bourgain, "see also" Johnson,
Lindenstrauss and Schechtman and Matoušek. The paper proves the
distortion itself (Claim 5's proof, pp. 7–8). For each power of two 2ˡ
below n, take O(log n) random subsets of that size, Q = O(log² n) in
all, and send x to (d(x, Aᵢ)/Q^{1/p}). Each coordinate is 1-Lipschitz, so
nothing expands. For a pair x, y, balls around x and y of growing
cardinality 2ᵗ give radii ρ_t up to d(x, y)/4. At each scale a set of
size about n/2ᵗ separates the radii ρ_{t−1} and ρ_t with constant
probability, so a tenth of the O(log n) sets do, for all pairs, with
high probability. Summed over scales, Σᵢ |d(x, Aᵢ) − d(y, Aᵢ)| ≥
log n·d(x, y)/40, against at most C·log² n·d(x, y). That gives distortion
O(log n) into ℓ_p^{O(log² n)} for every p ≥ 1, although Claim 5 is stated
for p > 2. With p = 2, Johnson–Lindenstrauss (Theorem 3.1, quoted with
t = O(log n/ε²)) reduces the dimension to O(log n), using
[THEORY-tmpns5kz](THEORY-tmpns5kz.md). The paper calls Claim 1 "an immediate corollary".

**The lower bound (Proposition 4.2, p. 12; Theorem 3.2(6)).** "Every
embedding of an n-vertex constant degree expander into an l_p space,
2 ≥ p ≥ 1, of any dimension, has distortion Ω(log n)." Let Φ(d) =
Σ_{edges} d_{i,j} / Σ_{i≠j} d_{i,j}. For the expander's own metric,
Φ = Θ(1/(n log n)). For any cut metric, and so for any ℓ₁ metric, which
is a nonnegative combination of cuts, Φ = Ω(1/n). An embedding of
distortion c changes Φ by at most a factor c, so c = Ω(log n) in ℓ₁. ℓ_p
for 1 ≤ p ≤ 2 embeds in ℓ₁ with constant distortion, which carries the
bound to ℓ₂. The same proposition says constant distortion needs
Ω(log² n) dimensions in any normed space, since a d-dimensional norm is
within √d of Euclidean.

**Together.** For ℓ₂, and for ℓ₁ (since c₁ ≤ c₂), the worst-case least
distortion over n-point metrics is Θ(log n). The paper says the expander
result "is tight, and closes a gap left open by Bourgain". The
consequence for Johnson and Lindenstrauss's Problem 4 is the record's
inference, not the paper's: a distortion of K√(log n) for every n-point
metric is impossible, because expanders need Ω(log n).

**What could have come out otherwise.** A family of n-point metrics
whose least Euclidean distortion grows faster than log n would refute the
upper bound, and a constant-degree expander family embedding in ℓ₂ with
distortion o(log n) would refute the lower bound. The lower bound's
argument is short given its cited inputs. The upper bound's probability
estimates are asserted rather than computed.

## What this does not say

- **Anything about trees.** The lower bound is for expanders. The paper's
  only tree result is that trees embed isometrically in ℓ∞^{O(log n)}
  (Theorem 5.3). It does not support the claim, cited to it by Sala et
  al. ([NOTE-679](../notes.d/NOTE-679.md)), that Euclidean space cannot embed trees with low
  distortion.
- **The constants**, in either bound, or in the dimension.
- **That the dimension O(log n) comes from Bourgain's construction.** In
  this paper's argument the construction uses O(log² n) coordinates, and
  the reduction is Johnson–Lindenstrauss's. Whether Bourgain's own paper
  states O(log n) dimensions cannot be checked without it.
- **Anything about p > 2.** Claim 5 gives O(log n) there, with no lower
  bound.
- **Anything about Lipschitz extension.** L(X, n) and [THEORY-tmp7nqd6](THEORY-tmp7nqd6.md)'s
  √(log n) are a different problem, and the paper does not address them.
- **That typical metrics or graphs need log n.** The bound is worst case.
  Particular families embed better, and Theorem 3.2(2) computes c₂(X) for
  any given X.

## Connections

- [THEORY-tmpns5kz](THEORY-tmpns5kz.md): the dimension half uses its random projection as a
  second stage, after a non-linear random map.
- [THEORY-tmp7nqd6](THEORY-tmp7nqd6.md): the account filed from Johnson and Lindenstrauss's
  paper. That paper's Problem 4, about embedding rather than extension,
  is answered here by inference. Its extension bound is untouched.
- [QUESTION-tmpa0dq9](../questions.d/QUESTION-tmpa0dq9.md): the upper bound's count, O(log n) random sets per
  scale so that a constant per-pair probability holds for all n² pairs, is
  a union bound over pairs, like the lemma's. Its tolerance is a factor
  O(log n), not 1 ± ε, and the map is not linear.
