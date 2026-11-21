---
status: Proposed
title: 'A two-class Gaussian mixture along a hidden direction, whose same-class cosines vanish with dimension while a readout along the direction stays 84 per cent accurate and PCA recovers the direction only above the BBP threshold'
version: 1
standing: stipulated
kind: construction
tags:
- representation-learning
- mathematical-statistics
- probabilistic-modeling
date: '2026-11-21'
line:
- learned-structure
illustrates:
- CLAIM-tmp5y856
bears_on:
- QUESTION-tmpvu6cb
summary: >-
  A32 §4 of the exchange "Rich Get Richer Power Laws" (2026-11-21): labels
  s = ±1 and z = √β·s·v + ε with ε ∼ N(0, I_D). The covariance is the
  spiked I + βvvᵀ; same-class cosines are about β/(D + β); a readout along v
  is right with probability Φ(√β); PCA on N samples finds v only when
  β > √(D/N). One construction in which geometric separation, decodability
  and spectral detectability all differ. The construction is A's (the
  other assistant in the exchange "Rich Get Richer Power Laws", A32);
  adopting it is the owner's call.
draws_on:
- THEORY-tmp4zojc
- THEORY-tmp6808g
---
<!-- inactive-ok-file: THEORY-tmp4zojc THEORY-tmp6808g THEORY-tmp0covn ARG-tmpe2vrk ARG-tmpnwmcr — Proposed; the readings and arguments of 2026-11-21 -->

# CASE-tmp59xy5: A two-class Gaussian mixture along a hidden direction, whose same-class cosines vanish with dimension while a readout along the direction stays 84 per cent accurate and PCA recovers the direction only above the BBP threshold

## The case

A32 §4. Two equally likely classes s equal to −1 or +1, an unknown unit vector v,
and

z = √β·s·v + ε, ε ∼ N(0, I_D),

so that Σ = I_D + βvvᵀ, a rank-one spiked covariance. Three descriptions of
the same cloud:

- **Radial**: ‖z‖ ≈ √(D + β), a Gaussian annulus.
- **Pairwise**: E[zᵢᵀzⱼ | sᵢ = sⱼ] = β, so the expected same-class cosine is
  about β/(D + β), which tends to zero at fixed β: "even two semantically
  related points can become almost orthogonal".
- **Semantic**: projected on v, y = √β·s + η with η ∼ N(0, 1), so the
  Bayes-optimal readout along a known v is right with probability Φ(√β),
  about 84% at β = 1, whatever D is.

Finding v without labels is a separate matter. In the limit D, N → ∞ with
γ = D/N fixed, the top eigenvalue of the sample covariance leaves the
Marchenko–Pastur edge (1 + √γ)² only when β > √γ, at
(1 + β)(1 + γ/β), with squared eigenvector overlap
(1 − γ/β²)/(1 + γ/β); below, the overlap tends to zero (the BBP transition,
Baik, Ben Arous and Péché, [LIT-tmpipm3o](../literature.d/LIT-tmpipm3o.md), read 2026-11-21; for this
mixture the theorem that applies is Benaych-Georges and Nadakuditi's,
[LIT-tmp1q78e](../literature.d/LIT-tmp1q78e.md), and the overlap is also Paul's, [LIT-tmpxru3g](../literature.d/LIT-tmpxru3g.md); see the note
of 2026-11-21 below).

"Semantically informative structure can exist in an embedding cloud whose
generic pairwise geometry looks almost completely random."

## Checked

Simulated in this session (python3 -I, D = 400, one draw each):

| N | β | top eigenvalue (predicted) | overlap (predicted) | same-class cosine (β/(D+β)) | accuracy along v (Φ(√β)) |
|---|---|---|---|---|---|
| 1,600 | 1.0 | 2.41 (2.50) | 0.62 (0.60) | 0.0024 (0.0025) | 0.83 (0.84) |
| 1,600 | 0.4 | 2.22 (edge 2.25) | 0.00 (0) | 0.0012 (0.0010) | 0.76 (0.74) |
| 400 | 2.0 | 4.44 (4.50) | 0.48 (0.50) | 0.0045 (0.0050) | 0.90 (0.92) |

The second row is the separating instance: at β = 0.4, below the threshold
√γ = 0.5, PCA finds nothing while a readout along v is right three times in
four. The ledger of the exchange also checked A32's chart (β = 0.6 gives
2.2667 and β = 2 gives 3.375 at γ = 0.25) and Φ(1) = 0.841.

## What it shows and does not

It shows the three qualities can come apart in one coherent model. It does
not show that trained representations are such mixtures, or that a
supervised learner faces the BBP threshold: with labels the estimation
problem is different, as A32 says.

## Note of 2026-11-21: Baik, Ben Arous and Péché, read

The BBP paper ([LIT-tmpipm3o](../literature.d/LIT-tmpipm3o.md), read in [NOTE-tmpggv08](../notes.d/NOTE-tmpggv08.md); [THEORY-tmp0covn](../theory.d/THEORY-tmp0covn.md))
**qualifies** the case's attribution; its numbers stand.

- The formulas are exact after the change of notation, but z = √β·s·v + ε
  with s = ±1 is a real, non-Gaussian mixture, not BBP's complex Gaussian
  samples, and not Baik and Silverstein's T^(1/2)Z with identically
  distributed entries either (the coordinate along v differs).
- It is exactly Benaych-Georges and Nadakuditi's additive rank-one model
  (§3.1; [LIT-tmp1q78e](../literature.d/LIT-tmp1q78e.md), [THEORY-tmp4zojc](../theory.d/THEORY-tmp4zojc.md)): the data matrix √β·vsᵀ + E,
  divided by √N, is a Gaussian matrix plus a perturbation of singular
  value θ = √β, so the threshold θ > γ^(1/4) is β > √γ, the outlier is
  (1 + β)(1 + γ/β) and the overlap (1 − γ/β²)/(1 + γ/β) ([ARG-tmpe2vrk](../arguments.d/ARG-tmpe2vrk.md)).
- The overlap is also Paul's Theorem 4 for the covariance-spike reading
  ([LIT-tmpxru3g](../literature.d/LIT-tmpxru3g.md), [THEORY-tmp6808g](../theory.d/THEORY-tmp6808g.md); [ARG-tmpnwmcr](../arguments.d/ARG-tmpnwmcr.md)).

The case `draws_on` [THEORY-tmp4zojc](../theory.d/THEORY-tmp4zojc.md) and [THEORY-tmp6808g](../theory.d/THEORY-tmp6808g.md) for its check of
the PCA column. The "Deferred: registered, not read" parenthesis above is
updated.
