---
number: 837
status: Proposed
formerly:
- CLAIM-tmpqbo50
title: 'In the factored-feature model a feature switches on, and its regularized loss is singular, at the same point s = λ, but sample PCA detects the feature only further on: in the hidden layer once s − λ exceeds σ²√(D/N), and in its contribution to the output once (s − λ)² does, so over a window that narrows as the sample grows the feature is active and improves the fit while it stays inside the noise bulk'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation below: a minimizer of
  L(a, b) = ½(ab − s)² + (λ/2)(a² + b²) above threshold that is not
  balanced, a² = b² = s − λ; a spiked covariance σ²I + ℓuuᵀ whose sample
  PCA, from N samples in D dimensions, gives an outlier and an informative
  top eigenvector at a spike ℓ other than σ²√(D/N) as D and N grow with
  D/N fixed; or a gain in fit inside the window that is not positive. That
  the hidden-layer window depends on the balance weight decay imposes, and
  that the isotropic noise is stipulated, do not defeat it; the claim says
  both.
tags:
- learning-theory
- representation-learning
- mathematical-statistics
date: '2026-11-21'
line:
- learned-structure
rests_on:
- CLAIM-807
- CLAIM-799
grounds:
- CASE-301
- THEORY-2149
bears_on:
- QUESTION-511
uses:
- TERM-137
summary: >-
  From the synthesis audit of the exchange "Rich Get Richer Power Laws":
  the narrower sentence that passes where A41 §8's revised synthesis
  ("the developmental onset of a new semantic distinction may first appear
  as a change in task sensitivity within a spectrally quiet subspace,
  potentially preceding a visible change in variance or an identifiable
  transition in local singularity structure") does not. Put on one axis,
  the factored feature's threshold and the BBP threshold give it a
  derivation in a stated model: onset and the singular point coincide at
  s = λ, and sample PCA sees the feature only after a window that narrows
  as N/D grows. So A's sentence holds in this model for variance and fails
  for the singular transition. Checked with python3 -I. The wording is
  the assistant's (Claude, in this session); adopting it is the owner's
  call.
---
<!-- inactive-ok-file: THEORY-2149 THEORY-2148 THEORY-2152 ARG-151 — Proposed; the readings and argument of 2026-11-21 -->
<!-- inactive-ok-file: CLAIM-807 CLAIM-799 CASE-301 TERM-137 CLAIM-828 CLAIM-827 — new and Proposed or Open; filed from the exchange "Rich Get Richer Power Laws" on 2026-11-21 -->

# CLAIM-837: In the factored-feature model a feature switches on, and its regularized loss is singular, at the same point s = λ, but sample PCA detects the feature only further on: in the hidden layer once s − λ exceeds σ²√(D/N), and in its contribution to the output once (s − λ)² does, so over a window that narrows as the sample grows the feature is active and improves the fit while it stays inside the noise bulk

## The claim

Two thresholds the record holds separately are put on one axis, the
feature's signal strength s at fixed weight decay λ.

**The feature's threshold** ([CLAIM-807](CLAIM-807.md), A42 §§1–5). For
L(a, b) = ½(ab − s)² + (λ/2)(a² + b²), the strength is q* = (s − λ)₊.
Above threshold the minima are balanced, a = b = ±√(s − λ). Write
ε = s − λ. Then:

- the hidden activation bφ has variance b² = ε;
- the contribution abφ to the output has variance ε²;
- the fit improves by sε − ε²/2 = λε + ε²/2 ([CLAIM-807](CLAIM-807.md));
- the local coefficient of the regularized loss goes 1 → 3/4 → 1 across
  s = λ ([CLAIM-807](CLAIM-807.md)), so the singular point is the threshold itself.

**The detectability threshold** ([CLAIM-799](CLAIM-799.md), [CASE-301](../cases.d/CASE-301.md)). Stipulate
that the layer in which PCA is run carries the feature along a unit
direction u against isotropic noise: h = bφu + σξ, ξ ∼ N(0, I_D), as in
[CASE-301](../cases.d/CASE-301.md)'s z = √β·s·v + ε. Its covariance is σ²I + b²uuᵀ, a spike of
relative strength ℓ = b²/σ². Sample PCA from N samples gives an outlier
eigenvalue, and a top eigenvector correlated with u, only when
ℓ > √γ, γ = D/N (the BBP threshold the record holds in [CLAIM-799](CLAIM-799.md)).
Below it the top eigenvalue sits at the bulk edge σ²(1 + √γ)²; above it
the outlier is at σ²(1 + ℓ)(1 + γ/ℓ).

**Together.**

- Hidden layer: ℓ = ε/σ², detected when ε > σ²√γ.
- Output contribution, with noise σ in that representation: ℓ = ε²/σ²,
  detected when ε > σ·γ^(1/4).
- On 0 < ε below either bound, the feature is switched on and the fit
  gains about λε, while sample PCA returns a top eigenvalue at the bulk
  edge and an eigenvector unrelated to u.

With σ = 1 the windows are:

| γ = D/N | hidden layer, ε below | output contribution, ε below |
|---|---|---|
| 4 | 2.000 | 1.414 |
| 1 | 1.000 | 1.000 |
| 0.25 | 0.500 | 0.707 |
| 0.01 | 0.100 | 0.316 |

At fixed D, the hidden-layer window narrows as N^(−1/2) and the
output-contribution window as N^(−1/4). With abundant samples,
detection nearly coincides with onset. The two windows are in different
units, since σ in the two representations need not be equal.

**Checks** (python3 -I, this session).

- Gradient descent on L(a, b) with λ = 1, from 41 starts, gives
  ab = 0.0500, 0.2000 and 0.5000 at s = 1.05, 1.2 and 1.5, with
  a² = b² = ε each time.
- Sampled spiked covariances, mean of four or five draws:
  - D = N = 1,500 (γ = 1, bulk edge 4). Spikes 0.3, 0.6 and 0.9 give top
    eigenvalues 3.978, 3.998 and 3.994, at the edge. Spikes 1.5, 2.0 and
    3.0 give 4.169, 4.500 and 5.259, against 4.167, 4.500 and 5.333
    predicted.
  - D = 600, N = 2,400 (γ = 0.25, threshold 0.5, edge 2.25). Spikes 0.3
    and 0.45 give 2.234 and 2.243, at the edge. Spikes 0.6, 0.8 and 1.2
    give 2.265, 2.379 and 2.692, against 2.267, 2.363 and 2.658.

## Admission

From the audit of the syntheses in the exchange "Rich Get Richer Power
Laws" ([ADR-075](../decisions.d/ADR-075.md), step 5; [ADR-131](../decisions.d/ADR-131.md)). The learning thesis's revised synthesis,
A41 §8, adds one integrating sentence: a new distinction's onset "may
first appear as a change in task sensitivity within a spectrally quiet
subspace, potentially preceding a visible change in variance or an
identifiable transition in local singularity structure". As stated, it
holds only as a candidate answer in [QUESTION-511](../questions.d/QUESTION-511.md), and "may" leaves no
outcome that would defeat it.

The narrower sentence passes by **derivation**. It is a valid inference
from [CLAIM-807](CLAIM-807.md) and [CLAIM-799](CLAIM-799.md), together with the stipulated noise
of [CASE-301](../cases.d/CASE-301.md)'s construction. It is not trivial: it fixes the order of
three events and the width of the gap between two of them. No claim holds
it.

- [CLAIM-807](CLAIM-807.md) says a newly active feature is quiet, with variance of
  order ε², but does not set that against a detection threshold.
- [CLAIM-799](CLAIM-799.md) and [CLAIM-827](CLAIM-827.md) place the BBP threshold against
  decodability and alignment, not against a feature's onset.
- [CLAIM-828](CLAIM-828.md)'s three times (encoded, stable, expressed) separate
  onset from expression by dynamics. This window is static.

It also gives a dependency the components leave open: the lag between
onset and detection in s scales as √(D/N) in the hidden layer. In
[LEAD-207](../leads.d/LEAD-207.md)'s or [LEAD-210](../leads.d/LEAD-210.md)'s design, varying the probe set's
sample count at fixed width should move the detection time and not the
onset time.

**What this does to A41's sentence.** In this model the onset precedes a
visible change in variance, as A says. It does not precede the singular
transition: the coefficient's dip is at the onset itself. [QUESTION-511](../questions.d/QUESTION-511.md)
notes that events 1 and 2 coincide at s = λ. This claim adds that event 1
(the weak direction becoming informative) and sample-PCA visibility are
separated by a window of stated width.

## What it does not say

- **Nothing about trained networks.** The model has one feature, one
  direction and isotropic noise, all stipulated.
- **Nothing dynamic.** With a parent gate drifting through the threshold,
  the observed onset lags the crossing ([CLAIM-828](CLAIM-828.md)), and the feature
  can grow past the detection bound faster than equilibrium would. The
  window is a statement about equilibria at fixed s.
- **The hidden-layer window is not gauge-free.** Without weight decay,
  a → ca, b → b/c leaves the predictor fixed and moves the hidden
  variance by 1/c², so that window is set by the balance weight decay
  imposes. The output-contribution window does not depend on the
  balance. This is [TERM-137](../terms.d/TERM-137.md)'s point that "weak" needs a named
  spectrum.
- **Not that the feature cannot be decoded in the window.** A population
  readout along u has R² = ε/(ε + σ²) > 0. Whether a probe trained on N
  samples finds it is a further threshold, not derived here.
- **Not a phase transition of the predictor.** The predictor only kinks at
  s = λ ([CLAIM-807](CLAIM-807.md)).

## Note of 2026-11-21: Baik, Ben Arous and Péché, read

The BBP paper ([LIT-2986](../literature.d/LIT-2986.md), read in [NOTE-2241](../notes.d/NOTE-2241.md); [THEORY-2148](../theory.d/THEORY-2148.md))
**supports the formulas** and **qualifies the range**.

- The outlier σ²(1 + ℓ)(1 + γ/ℓ) and the edge σ²(1 + √γ)² are BBP's
  Corollary 1.1 rescaled by σ².
- **The γ = 4 row is outside BBP**, which needs at least as many samples
  as variables (γ ≤ 1). It is inside Baik and Silverstein's theorem
  ([LIT-2988](../literature.d/LIT-2988.md), [THEORY-2149](../theory.d/THEORY-2149.md)), which holds at any ratio with the same
  threshold 1 + √γ and location, for real samples ([ARG-151](../arguments.d/ARG-151.md)). The row
  stands on that theorem.
- With φ independent of ξ and not Gaussian, h = bφu + σξ is an additive
  rank-one model, Benaych-Georges and Nadakuditi's ([THEORY-2152](../theory.d/THEORY-2152.md)), with
  the same formulas.
- The window's lower end, an outlier within about N^(−2/3) of the edge, is
  BBP's edge scale (Theorem 1.1(a)).

[THEORY-2149](../theory.d/THEORY-2149.md) joins `grounds`; [THEORY-2148](../theory.d/THEORY-2148.md) corroborates.
