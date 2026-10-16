---
number: 120
status: Open
formerly:
- QUESTION-tmpa0dq9
title: 'When the record meets a random linear map that keeps what a later stage needs, in random features for kernels, the compressed-sensing bound on superposition, and the expand-and-threshold codes of sparse distributed memory and the fly, is it one concentration-of-measure fact applied to different families, and does each threshold count the same thing?'
version: 4
history:
- version: 4
  date: '2026-10-16'
  note: >-
    Alon and Klartag read (NOTE-929): the distances thread now says
    how far the lower bound reaches and how their bit count realizes the
    proposed shape. The question itself stands.
- version: 3
  date: '2026-10-16'
  note: >-
    After main moved. The record now holds Indyk and Motwani (LIT-1106,
    NOTE-905), with a Gaussian JL-type proof and the LSH guarantee filed
    as THEORY-388, and it already held THEORY-261 on SDM recall, which the
    first survey missed. Both THEORY documents reach the expand-and-threshold
    thread, which nothing read for this question had, and "What would answer
    it" now names the fly hash's collision probabilities as the quantity to
    find. The question itself stands.
- version: 2
  date: '2026-10-14'
  note: >-
    Six of the seven anchor works were read the same day (the fly paper is
    Unavailable). The readings corrected five statements in version 1,
    listed under "Corrections"; a section on what the readings found was
    added and "What would answer it" rewritten. The question itself stands.
tags:
- mathematics
- learning-theory
- neuroscience
date: '2026-10-14'
line: formal-apparatus
summary: >-
  Filed when a survey of the record found random projections in three
  places and the Johnson–Lindenstrauss lemma in none. The three uses carry
  three thresholds: ε⁻² log n for distances, k log(n/k) for sparse
  recovery, and 2N = n for random-features regression. The question is
  whether these are one union bound over different families or different
  phenomena that share a tool. Six anchor works are now read. They show
  the distance and sparse-recovery thresholds share a sufficiency proof,
  but not a necessity proof, and give nothing that reaches the other two
  uses. For SDM and the fly, the record's SDM recall account and its LSH
  account offer candidate thresholds of a different shape.
answered_by:
- THEORY-390
- THEORY-391
- THEORY-395
- THEORY-397
- THEORY-393
- THEORY-399
---
<!-- inactive-ok-file: LIT-1158 — Unavailable; the fly paper, a lawful preprint this client could not fetch -->
<!-- inactive-ok-file: THEORY-106 THEORY-261 — Proposed; the accounts the random-features and SDM threads are set against -->

# QUESTION-120: When the record meets a random linear map that keeps what a later stage needs, in random features for kernels, the compressed-sensing bound on superposition, and the expand-and-threshold codes of sparse distributed memory and the fly, is it one concentration-of-measure fact applied to different families, and does each threshold count the same thing?

## The question

The record uses random projections in three places.

- **Random features.** Liao, Couillet and Mahoney ([LIT-679](../literature.d/LIT-679.md), [NOTE-519](../notes.d/NOTE-519.md))
  and [THEORY-106](../theory.d/THEORY-106.md) treat cos(WX), sin(WX) with W random. The threshold
  there is 2N = n, features against samples, and it is where the test error
  diverges.
- **Superposition.** Toy Models of Superposition proves m = Ω(k log(n/k))
  for recovering k-sparse features, assuming the restricted isometry
  property, and asks whether its phase changes are the Donoho–Tanner
  transition ([NOTE-278](../notes.d/NOTE-278.md)).
- **Expand and threshold.** Neuron-view sparse distributed memory is linear
  attention with thresholded random projections as its feature map
  ([NOTE-242](../notes.d/NOTE-242.md), [NOTE-779](../notes.d/NOTE-779.md)). The mushroom body makes a similar move in tissue
  ([NOTE-670](../notes.d/NOTE-670.md), [NOTE-165](../notes.d/NOTE-165.md)).

The Johnson–Lindenstrauss lemma keeps the pairwise distances of n points
in O(log n) dimensions, with ε⁻² log n as the order in its later proofs.
If one argument underlies all three uses, each threshold would be the log
of the size of the family a map must hold, divided by a squared tolerance.
The question is whether that is true of all three uses, or only of some.

## Why it is a question

Two things suggested from the start that the three are not one phenomenon.

- **The random-features threshold counts something else.** 2N = n compares
  features with training samples. Its divergence comes from the ridgeless
  resolvent near interpolation ([THEORY-106](../theory.d/THEORY-106.md)), not from failing to keep
  distances. A random map can keep every distance and still interpolate
  badly.
- **The biological and SDM maps go up in dimension.** The fly projects
  about 50 glomeruli onto about 2,000 Kenyon cells and keeps the top 5%
  ([LIT-1158](../literature.d/LIT-1158.md), unread). Johnson–Lindenstrauss is about going down.
  What expansion followed by sparsification keeps is similarity rank under
  a hash, which is a different guarantee.

## What the readings found

**Distances.** The original lemma ([LIT-1153](../literature.d/LIT-1153.md), [NOTE-930](../notes.d/NOTE-930.md)) states
k = [K(τ) log n] for a bound (1+τ)/(1−τ) on distortion. The τ⁻² appears
only in its proof (K ≥ (10/τ)² suffices), which concentrates the norm about
its median by Lévy's isoperimetric inequality. Dasgupta and Gupta
([LIT-1157](../literature.d/LIT-1157.md), [NOTE-932](../notes.d/NOTE-932.md)) give the explicit
k ≥ 4(ε²/2 − ε³/3)⁻¹ ln n for squared distances: a per-pair tail of 2/n²
and a union bound over the pairs. Larsen and Nelson ([LIT-1154](../literature.d/LIT-1154.md),
[NOTE-925](../notes.d/NOTE-925.md)) show Ω(ε⁻² lg(ε²n)) is needed for some n-point set,
for any map, when ε is above about 1/√min{n, d}. Indyk and Motwani
also prove a JL-type lemma with Gaussian projections ([LIT-1106](../literature.d/LIT-1106.md), [NOTE-905](../notes.d/NOTE-905.md),
Appendix A), read for nearest-neighbour search. [NOTE-905](../notes.d/NOTE-905.md) does not give
its constants, so it is not compared here. Their STOC text also shows the
lemma fails for ℓ∞. So for distances the
proposed shape holds on both sides, up to a constant, for the worst set.
It is not a sharp threshold in the Donoho–Tanner sense.

Alon and Klartag ([LIT-1151](../literature.d/LIT-1151.md), [NOTE-929](../notes.d/NOTE-929.md), [THEORY-399](../theory.d/THEORY-399.md)) carry the
lower bound down to every ε ≥ 2/√n, as Ω(log(2 + ε²n)/ε²), for additive
error on points of norm at most 1. Their proof makes the proposed shape
literal: the bits needed are the log of the number of ε-separated Gram
matrices, and the dimension is that count per point over O(1) bits per
coordinate. For small ε the log is of 2 + ε²n, not of the n² pairs a
union bound counts (the reader's observation in [NOTE-929](../notes.d/NOTE-929.md)). Their
bipartite lemma ([THEORY-393](../theory.d/THEORY-393.md)) gives n nearly orthogonal pairs of
write and read vectors in that many dimensions, but with unbounded norms,
so it does not bound superposition as [NOTE-278](../notes.d/NOTE-278.md) defines it.

**Sparse recovery.** Baraniuk et al. ([LIT-1156](../literature.d/LIT-1156.md), [NOTE-931](../notes.d/NOTE-931.md))
derive the restricted isometry property from the JL concentration
inequality, in Achlioptas's form. They use a union bound over the points of
a δ/4-net on each k-sparse support, (eN/k)^k(12/δ)^k in all, and then a
step from the net to the whole subspace. That is the proposed shape, but
only for sufficiency. The paper rests necessity of k log(N/k) on
Garnaev–Gluskin's Gelfand widths of the ℓ₁ ball, which is geometry, not
concentration. The [NOTE-278](../notes.d/NOTE-278.md) bound is a necessity bound that takes the RIP
as a hypothesis. So this paper supplies its hypothesis for random matrices
and does not explain it.

Larsen and Nelson's proof points the other way: its hard instance is a
family of k-sparse vectors with k ≈ ε⁻², and the count it ends on is
m = Ω(k lg(d/k)) (my reading in [NOTE-925](../notes.d/NOTE-925.md)). There the JL order arises
as a sparse-support count. The same paper notes that ε-incoherent sets, the
almost-orthogonal directions superposition is about, fit in
o(ε⁻² lg n) dimensions for small enough ε. The JL lower bound is
therefore not a bound on superposition capacity.

Donoho and Tanner ([LIT-1160](../literature.d/LIT-1160.md), [NOTE-933](../notes.d/NOTE-933.md)) give the transition as an
exact limiting location from counting the faces of projected polytopes,
for ℓ₁ decoding. It is not a union bound of any shape. Its universality
across eight ensembles is observed and asymptotic only. At finite N the
location depends on the ensemble by O(N^(−1/2)), and by about one
transition width for sparse and Hadamard matrices at small N.

**Expand and threshold.** Nothing read reaches it. Achlioptas
([LIT-1159](../literature.d/LIT-1159.md), [NOTE-926](../notes.d/NOTE-926.md)) proves JL for independent, zero-mean, unit-variance
entries: dense ±1, or √3·{+1, 0, −1} with two thirds zeros. He says,
without proof, that more zeros than that breaks it. The fly's matrix is {0, 1}, nonnegative
and about 12% nonzero, so it falls outside both. SDM's address matrix is
dense ±1, which is inside, but no paper read says anything about the
threshold that follows the projection. Larsen and Nelson's bound is
vacuous once the map goes up in dimension.

Two accounts the record already holds do reach this thread, though
neither came from these readings. [THEORY-261](../theory.d/THEORY-261.md) treats SDM recall as a
signal-to-noise problem: the optimum activates about (2MT)^(−1/3) of the
hard locations, and capacity grows with their number, not with the word
length. That is a threshold for an expand-and-threshold map, and it is not
of the proposed shape. [THEORY-388](../theory.d/THEORY-388.md), filed upstream from Indyk and Motwani,
gives locality-sensitive hashing's guarantee as query cost n^ρ, with
ρ = ln(1/p₁)/ln(1/p₂) set by the collision probabilities of near and far
pairs. If the fly's tag is a hash family, as its paper claims, its guarantee
would take that form. That too is a ratio of logs, but of probabilities,
not of a family's size.

## Corrections

Version 1 said five things the readings do not support.

- "ε⁻² log n" was attributed to the lemma. The lemma states K(τ) log n;
  the ε⁻² order and the squared-distance form are from later proofs.
- "The bound is tight" holds only up to a constant, for ε above about
  1/√min{n, d}, and for a worst-case set.
- The RIP proof was described as a union bound "over sparse supports
  instead of point pairs". It is over net points on each support, plus a
  bootstrap step.
- "The sparse binary matrices of the fly and of SDM are the ensembles
  Achlioptas shows keep the JL guarantee." This is wrong. His ensembles are
  signed and zero-mean. The fly's is not, and SDM's is dense.
- "Donoho and Tanner observe that the sparse-recovery transition does not
  depend on the ensemble." That holds only as N → ∞, for the eight
  ensembles tested.

## What would answer it

- **For superposition.** Set the toy model's necessary m beside Baraniuk
  et al.'s sufficient n at the same k and N, and its phase change beside
  the Donoho–Tanner curve at the same (δ, ρ). They agree in order. Whether
  they agree in location needs the record's own computation. Then ask
  whether superposition is limited by recovery, as [NOTE-278](../notes.d/NOTE-278.md)'s bound
  assumes, or by incoherence, which Larsen and Nelson show can pack more.
- **For random features.** A statement of what a random-features map keeps
  that the lemma does not mention. One candidate is that a kernel's Gram
  matrix converges entrywise but not in spectral norm ([LIT-679](../literature.d/LIT-679.md)). Or a
  derivation of the 2N = n transition that goes through concentration, if
  one exists. Nothing read supplies either.
- **For expand-and-threshold.** The collision probabilities p₁ and p₂ of
  the fly's hash, a nonnegative sparse {0, 1} projection followed by top-k,
  so that its ρ can be set beside [THEORY-388](../theory.d/THEORY-388.md)'s for random-projection LSH.
  The fly paper is said to prove that the first two steps keep ℓ₂ distances
  in expectation, and it is the next reading once a copy is supplied. Then
  ask whether [THEORY-261](../theory.d/THEORY-261.md)'s activation optimum and ρ measure the same
  thing for SDM.

The readings so far answer the question for the first two uses only, and
only on the side of sufficiency. For the third, the record holds two
candidate forms, an SDM signal-to-noise optimum and an LSH exponent, and
neither is the proposed shape.
