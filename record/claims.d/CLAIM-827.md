---
number: 827
status: Proposed
formerly:
- CLAIM-tmpk33au
title: 'The occupancy threshold of a cone holding a fixed share of random directions, the BBP threshold and the alignment bifurcation are three different thresholds on one scale of alignment strength: the first at κ of order √D, the second at κ = √D·(D/N)^(1/4), the third at a coupling of order D; only the last is a transition of the system, and in the mean-field alignment model the ordering mode becomes BBP-detectable at coupling D/(1 + √(D/N)), an early warning before the bifurcation at D'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivations below: a von Mises–Fisher tilt κ = c√D whose
  effect on sample PCA is not that of a spike β = c², so that the BBP
  threshold does not fall at κ = √D·(D/N)^(1/4); a mean-field alignment
  model whose isotropic state loses stability at a coupling other than D;
  or exact samples of that model, at growing D and N with D/N fixed, in
  which the top eigenvalue leaves the bulk at a coupling that does not
  tend to D/(1 + √(D/N)). Not met by trained networks whose alignment is
  not of this form; the claim is about the models the exchange used.
tags:
- representation-learning
- mathematics
- complex-systems
date: '2026-11-21'
line:
- learned-structure
rests_on:
- CLAIM-838
- CLAIM-799
bears_on:
- QUESTION-515
- QUESTION-512
summary: >-
  Fills a gap the ledgers of the exchange "Rich Get Richer Power Laws"
  flagged across A32, A33 and A35 (answering U19 and U21): an entailment
  cone's aperture scaling with √D, the BBP threshold and an alignment
  bifurcation are each called a threshold, and the exchange never says
  whether they are one. They are three, on one scale: two detectability
  thresholds and one transition. When the alignment is self-generated, the
  ordering mode becomes spectrally visible before the bifurcation, an early
  warning. The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call.
grounds:
- THEORY-2152
- THEORY-2149
---
<!-- inactive-ok-file: ARG-tmps8aog THEORY-tmphbp5a — Proposed, Deferred or new; the readings of 2026-11-22 and the entries they bear on -->
<!-- inactive-ok-file: CLAIM-838 CLAIM-799 ARG-153 — new and Proposed, filed from the exchange "Rich Get Richer Power Laws" on 2026-11-21 -->
<!-- inactive-ok-file: THEORY-2152 THEORY-2149 THEORY-2148 ARG-135 ARG-151 ARG-145 — Proposed; the readings and arguments of 2026-11-21 -->

# CLAIM-827: The occupancy threshold of a cone holding a fixed share of random directions, the BBP threshold and the alignment bifurcation are three different thresholds on one scale of alignment strength: the first at κ of order √D, the second at κ = √D·(D/N)^(1/4), the third at a coupling of order D; only the last is a transition of the system, and in the mean-field alignment model the ordering mode becomes BBP-detectable at coupling D/(1 + √(D/N)), an early warning before the bifurcation at D

## The claim

**Which gap.** The exchange names several thresholds: a cone's half-angle
tracking π/2 − a/√D, with a bias κ of order √D changing its occupancy
([CLAIM-838](CLAIM-838.md), A35 §1); the BBP threshold √(D/N) at which a covariance spike
separates from the bulk ([CLAIM-799](CLAIM-799.md), A32 §2); and the ordering of a mean-field
O(D) alignment model at J/T = D (A32 §7). A33 §9 lists them as "a hierarchy
of geometric thresholds" that "need not occur simultaneously", without
relating them. They can be put on one axis, the alignment strength.

**One scale.** Let unit vectors be tilted toward μ by a von Mises–Fisher
bias κ, and write x = √D·u, so the null is near N(0, I) and the tilt shifts
x along μ by c = κ/√D (A35 §1).

[CLAIM-838](CLAIM-838.md), on which this claim rests, gives two of the scales: a
fixed-share cone changes occupancy smoothly once c is of order one, κ ∼ √D,
and an order-one cosine or a cone of fixed angle needs κ ∼ D, a factor √D
beyond. This claim adds the spectral one:

- **PCA on N such vectors** sees a mean shift c along μ as a spike
  β = c² in the uncentred second moment, so the BBP threshold β > √γ,
  γ = D/N, falls at c = γ^(1/4), that is κ_BBP = √D·(D/N)^(1/4). It is
  the same order as the cone threshold when N is proportional to D, earlier
  by γ^(1/4) when N ≫ D, later when N ≪ D. It is a non-analytic change in
  what the estimator returns, not in the population.

None of these is a transition of the system: the population changes
smoothly in κ in each. When κ is imposed by a task (one direction given by
labels), the cone threshold and the BBP threshold are detectability
thresholds of one smooth family, and the scale κ ∼ D is where alignment
becomes visible to the eye.

**When the tilt is self-generated.** In A32 §7's model,
H = −(J/2N)‖Σ_i u_i‖² at temperature T, write K = J/T. The mean-field
self-consistency m = A_D(Km), with A_D the mean cosine of a von Mises–Fisher
law, A_D(κ) ≈ κ/D for small κ, makes the isotropic state lose stability at
K = D, a pitchfork bifurcation, the one genuine transition in the set. Above
it m ≈ √(1 − D/K) at large D, and the effective tilt on each vector is
κ_eff = Km ≈ D√ε for K = D(1 + ε). So:

- the fixed-share cone threshold, κ_eff ∼ √D, is passed at ε ∼ 1/D, right
  after the bifurcation: in this model the √D threshold and the
  bifurcation coincide as D grows;
- the BBP threshold comes before it. Below K = D the ordering mode is the
  population mean, whose variance is enhanced by 1/(1 − K/D). In the
  Gaussian approximation that adds to the N × D data matrix a rank-one term
  of strength θ² = γ(K/D)/(1 − K/D) along a random direction, which
  separates from the bulk when θ² > √γ, that is at

  K_BBP = D/(1 + √γ).

  With N = D the ordering mode is spectrally detectable at half the
  bifurcation coupling; with N = 4D at two thirds; as N/D → ∞ the precursor
  merges with the bifurcation. A detached top eigenvalue of the
  representation's second moment, growing as K approaches D, is an early
  warning of the alignment bifurcation, in the sense of critical slowing:
  the variance of the mode that will order diverges before it orders.

**Answer to the gap.** The aperture threshold, the BBP threshold and the
bifurcation are different thresholds. Two are detectability thresholds on
the same √D scale, which agree in order when the probe sample grows with
width; one is a transition, at a coupling of order D. Whether they coincide
depends on whether the alignment is imposed or self-generated: imposed, they
are separated by a factor √D; self-generated, the cone threshold falls just
after the bifurcation and the spectral one before it.

## Checked

Computed in this session (python3 -I, numpy, scipy):

- **Tilt as spike.** Gaussian vectors with mean c along μ, D = 400: the top
  eigenvalue and overlap of the uncentred second moment follow the spiked
  formulas with β = c². At γ = 0.25, c = 1.5: 3.56 (predicted 3.61) and
  overlap 0.855 (0.856); at γ = 1, c = 2: 6.14 (6.25) and 0.739 (0.750);
  below c = γ^(1/4) no outlier.
- **The tilt in x.** For a von Mises–Fisher law at D = 768 with κ = c√D, the
  mean of √D·uᵀμ is 0.4998, 0.9987 and 1.990 for c = ½, 1, 2.
- **The bifurcation.** Solving m = A_D(Km) at D = 768 with A_D from the
  exact cosine density: m = 0 for K/D = 0.9 and 0.99; m = 0.100, 0.302,
  0.578, 0.707 and 0.866 for K/D = 1.01, 1.1, 1.5, 2 and 4, against
  √(1 − D/K) = 0.099, 0.302, 0.577, 0.707 and 0.866.
- **The precursor, by exact sampling.** The mean-field model at D = 200 was
  sampled exactly (a Hubbard–Stratonovich field drawn from its radial
  marginal, then the vectors independently from the von Mises–Fisher law it
  sets), twenty populations per coupling. Mean top eigenvalue of
  (D/N)Σ uᵢuᵢᵀ:

  | K/D | N = 200 (γ = 1; null 3.91) | N = 800 (γ = 0.25; null 2.20) |
  |---|---|---|
  | 0.5 | 3.87 | 2.20 |
  | 0.6 | 4.11 | 2.21 |
  | 0.7 | 4.63 | 2.24 |
  | 0.8 | 5.72 | 2.46 |
  | 0.9 | 8.44 | 3.35 |
  | 0.95 | 10.99 | 4.81 |

  Predicted onsets K/D = 0.50 and 0.67; the outlier is seen from 0.6 and
  from 0.7 to 0.8, later by the finite-size margin at the edge. The Gaussian
  approximation's outlier values match away from K = D (4.76 against 4.63
  at 0.7, γ = 1) and overshoot near it (11.1 against 8.4 at 0.9), where
  the unit-norm constraint saturates the mode. The onset, not the
  magnitude near the bifurcation, is what the claim uses.

The spiked-covariance threshold and formulas are Baik, Ben Arous and
Péché's ([LIT-2986](../literature.d/LIT-2986.md)), read on 2026-11-21; for the mean-shift step the
theorem that applies is Benaych-Georges and Nadakuditi's ([LIT-2964](../literature.d/LIT-2964.md)), and
for the precursor Baik and Silverstein's ([LIT-2988](../literature.d/LIT-2988.md)): see the note of
2026-11-21 below. The checks
above compare simulated outliers with the formulas directly, so they do not
depend on the work.

## What it does not say

- Not that training is a mean-field alignment model. A trained
  representation's order is rarely polar: several clusters pointing apart
  give m ≈ 0, as A30 §7 notes, so the order parameter for "onset of
  learning as symmetry breaking" (A30 §10) is still to be named. The claim
  is about the models the exchange used.
- Not that the hyperbolic entailment cones of [THEORY-189](../theory.d/THEORY-189.md) have the √D
  aperture threshold: the cone here is a spherical cap about the origin
  ([ARG-153](../arguments.d/ARG-153.md)).

## Note of 2026-11-21: Baik, Ben Arous and Péché, read

The BBP paper ([LIT-2986](../literature.d/LIT-2986.md), read in [NOTE-2241](../notes.d/NOTE-2241.md); [THEORY-2148](../theory.d/THEORY-2148.md))
**qualifies** this claim's attribution; its result stands.

- **The mean-shift step is not BBP's.** BBP centres the sample covariance
  by the sample mean ("the (centered) N × M sample matrix"), which would
  remove a mean shift, and its samples are complex Gaussian. PCA on the
  uncentred second moment of N samples of N(cμ, I) sees cμ1ᵀ + E, a
  rank-one additive perturbation of singular value θ = c (after dividing
  by √N). Benaych-Georges and Nadakuditi's §3.1 ([LIT-2964](../literature.d/LIT-2964.md),
  [THEORY-2152](../theory.d/THEORY-2152.md)) gives the threshold θ > γ^(1/4), so
  **κ_BBP = √D·(D/N)^(1/4) stands, on that theorem**, and the outlier
  (1 + c²)(1 + γ/c²) matches the check above ([ARG-135](../arguments.d/ARG-135.md)). The name "BBP
  threshold" is the field's and can stay.
- **The precursor** treats the ordering mode below K = D as a covariance
  spike in real data, which is Baik and Silverstein's real-case theorem
  ([LIT-2988](../literature.d/LIT-2988.md), [THEORY-2149](../theory.d/THEORY-2149.md); [ARG-151](../arguments.d/ARG-151.md)).
- **Scope.** §3.1 states D ≤ N; the claim's "later when N ≪ D" lies beyond
  what was read.

[LIT-2986](../literature.d/LIT-2986.md) leaves `grounds` for [THEORY-2152](../theory.d/THEORY-2152.md) and [THEORY-2149](../theory.d/THEORY-2149.md)
([ARG-145](../arguments.d/ARG-145.md)); [THEORY-2148](../theory.d/THEORY-2148.md) corroborates.

## Note of 2026-11-22: Park and colleagues, read

Park and colleagues ([LIT-2990](../literature.d/LIT-2990.md), [NOTE-tmpzethm](../notes.d/NOTE-tmpzethm.md), [THEORY-tmphbp5a](../theory.d/THEORY-tmphbp5a.md)): **a
parallel.** In their linear model the student converges toward the teacher
from the first step while the weight spectrum's outlier appears only at a
critical time: one more case of learning preceding spectral detection,
with the weight matrix as the estimator. No relation; [CLAIM-799](CLAIM-799.md) carries
the support ([ARG-tmps8aog](../arguments.d/ARG-tmps8aog.md)).
