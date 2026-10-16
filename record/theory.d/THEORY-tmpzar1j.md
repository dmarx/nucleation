---
status: Active
title: "Sparse distributed memory's read weights each stored pattern by the number of hard locations within the read radius of both query and pattern, a ball-intersection count that falls roughly exponentially in Hamming distance over a local window, so softmax attention over cosine similarity of unit-norm queries and keys, with a fitted inverse temperature, approximates the SDM read there; the approximation cannot hold globally, since the binary count vanishes beyond twice the radius, and its inverse temperature comes from a regression, not from the paper's analytic bound"
version: 1
tags:
- neuroscience
- information-retrieval
- mathematics
date: '2026-10-16'
source:
- LIT-269
summary: >-
  Bricken & Pehlevan (2021), [LIT-269](../literature.d/LIT-269.md), read in full in [NOTE-242](../notes.d/NOTE-242.md), which
  re-evaluated the intersection formula and the fit. The exact
  intersection (Eq. 2) is checked against Kanerva's lune formula and
  simulation; eight SDM and fitted-softmax variants retrieve almost
  identically on random patterns, MNIST and CIFAR-10, with three named
  exceptions. The intersection is a staircase in distance, the fit holds to
  about dv = 20 for d = 15, the analytic β of App. B.2 is about 2–2.5 times
  too small, and every optimal radius assumes random patterns and
  addresses. The GPT-2 "confirmation" and the cerebellar implementation of
  attention are argument, not demonstration.
supports:
- CLAIM-298
---
<!-- inactive-ok-file: THEORY-261 THEORY-272 — Proposed; neighbouring memory accounts named in Connections, nothing here rests on them -->
<!-- inactive-ok-file: CLAIM-180 CLAIM-298 — Proposed; the record's own claims that use this reading, named in Connections -->
<!-- inactive-ok-file: LIT-928 — Unavailable; Kanerva's book, named as the source of the critical distance, unread -->

# THEORY-tmpzar1j: Sparse distributed memory's read weights each stored pattern by the number of hard locations within the read radius of both query and pattern, a ball-intersection count that falls roughly exponentially in Hamming distance over a local window, so softmax attention over cosine similarity of unit-norm queries and keys, with a fitted inverse temperature, approximates the SDM read there; the approximation cannot hold globally, since the binary count vanishes beyond twice the radius, and its inverse temperature comes from a regression, not from the paper's analytic bound

## Source

Bricken and Pehlevan (2021), "Attention Approximates Sparse
Distributed Memory", NeurIPS 2021, [LIT-269](../literature.d/LIT-269.md), read in full in [NOTE-242](../notes.d/NOTE-242.md).

## What was actually shown

**The correspondence (Eqs. 1, 4–9).** An SDM read is a normalised
weighted sum of stored pointers; a pattern's weight is the number of
neurons that both stored it and are read by the query, the size of the
intersection of two radius-d Hamming balls. Attention is a normalised,
softmax-weighted sum of values. Map binary vectors to unit vectors with
d(a, b) = ⌊n/2 (1 − âᵀb̂)⌋ (exact for the bipolar rescaling), and if the
intersection is c₁exp(−c₂ d), the SDM weights are softmax(β âᵀξ̂) with β
set by c₂.

**The exact count (Eq. 2/12, App. B.1).** I(dv, d, n) is a closed double
sum of binomials, zero for dv > 2d, checked against Kanerva's lune
formula and simulation (n = 100, r = 10⁴, d = 35).

**How exponential it is.** The paper says "for the closest, most important
patterns where d(pa, ξ) ≤ 2d" (§1.1); its own App. B.2 says the log-linear
fit holds "until around dv = 20" for d = 15 and the curve is
super-exponential beyond. [NOTE-242](../notes.d/NOTE-242.md)'s recomputation: I(2k−1) = I(2k)
exactly, so the exponential fits an envelope of a staircase; over
distances below d the fit has R² 0.89–0.98 at n = 64 (≥ 0.998 on even
distances) and 0.99 at n = 1000; the fitted β moves with the window (14.4
on dv < d, 19.3 on dv ≤ 2d, at n = 64, d = 11).

**Retrieval agrees (App. B.7).** Eight SDM and softmax variants on random
patterns (n = 64 and 1000, m = 1024), MNIST and CIFAR-10 converge "in close
agreement", by plot, with exceptions at d = 5 under large perturbation, at
d = 19 for one variant, and at the canonical d = 447, where the true
intersection beats every fitted softmax and the authors "cannot explain
this difference".

**What could have come out otherwise.** The intersection could have fallen
in a way no exponential fits locally; or retrieval under the two weightings
could have diverged. Neither happened over the local window and on these
tests.

## What this does not say

- **That the analytic derivation gives β.** App. B.2's Gaussian
  approximation of a far-tail binomial gives β = (n − 2d)²/(4n), which
  [NOTE-242](../notes.d/NOTE-242.md) finds 2–2.5 times smaller than the regression (11.4, 6.9, 4.5
  against 28.4, 14.4, 9.4 at n = 64, d = 5, 11, 15). The authors call it
  "moderate success".
- **That far patterns get no weight.** With m = 1024 random patterns near
  the orthogonal distance, softmax gives them a total weight of about 0.07
  at β ≈ 9.4, where SDM gives exactly 0 ([NOTE-242](../notes.d/NOTE-242.md)'s calculation). On random
  patterns this did not change retrieval.
- **That trained Transformers implement SDM.** QK-norm heads learn
  β in [10, 25], from private correspondence; the optima it is compared
  with assume random patterns, which the authors call "only a weak
  reference", and the memory-optimal β lies outside the band. GPT-2 does
  not normalise queries and keys, and its "effective β", the largest
  softmax input over eight prompts, is mostly 3–12. The abstract's
  "confirm" outruns App. A.2.
- **That the cerebellum implements attention.** The mapping is Kanerva's
  for SDM. The attention instance needs r = 2⁶⁴ neurons, which the paper
  calls implausible, and per-token writes are not addressed.
- **That Hopfield networks are a parameter setting of SDM.** The reduction
  replaces the threshold by a raw dot product, a change of rule.

## Connections

- **Kanerva's capacity analysis** ([THEORY-261](THEORY-261.md), from [LIT-921](../literature.d/LIT-921.md)) gives the load
  side of SDM for exact cues. This account concerns the weighting by
  distance that both the read and its critical distance depend on, which
  [THEORY-261](THEORY-261.md) leaves to this paper and to Kanerva's book ([LIT-928](../literature.d/LIT-928.md)).
- **Hopfield's attractor memory** ([THEORY-272](THEORY-272.md), from [LIT-918](../literature.d/LIT-918.md)) is the zero
  write-radius neighbour, by the change of rule above.
- **A kernel reading.** [NOTE-242](../notes.d/NOTE-242.md) restates the correspondence as one between
  two zonal positive-definite kernels used as normalised kernel-smoother
  weights, and observes that neuron-view SDM is linear attention with a
  thresholded random-projection feature map. Neither is the paper's.
- [CLAIM-180](../claims.d/CLAIM-180.md) uses the critical distance as its picture of drift, and
  [CLAIM-298](../claims.d/CLAIM-298.md) the reach of a query into stored distinctions; [QUESTION-096](../questions.d/QUESTION-096.md)
  asks when a cue changes what an unchanged memory yields.
- The anthology holds the paper's reading for practice ([ANTH-LIT-641](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-641.md),
  [ANTH-THEORY-097](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/theory.d/THEORY-097.md), on query–key normalisation); [NOTE-242](../notes.d/NOTE-242.md) corrects two of
  its statements.
