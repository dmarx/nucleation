---
number: 301
status: Proposed
formerly:
- CASE-tmp59xy5
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
- CLAIM-799
bears_on:
- QUESTION-515
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
- THEORY-2152
- THEORY-2153
---
<!-- inactive-ok-file: THEORY-2152 THEORY-2153 THEORY-2148 ARG-135 ARG-143 — Proposed; the readings and arguments of 2026-11-21 -->
<!-- inactive-ok-file: THEORY-2186 — Proposed, Deferred or new; the readings of 2026-11-22 (Wang, Wu and Fan; Yang, Steinhardt and Hu; Ansuini and colleagues; Cai and colleagues; Martínez-Sánchez and colleagues), their arguments, and the entries they bear on -->

# CASE-301: A two-class Gaussian mixture along a hidden direction, whose same-class cosines vanish with dimension while a readout along the direction stays 84 per cent accurate and PCA recovers the direction only above the BBP threshold

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
Baik, Ben Arous and Péché, [LIT-2986](../literature.d/LIT-2986.md), read 2026-11-21; for this
mixture the theorem that applies is Benaych-Georges and Nadakuditi's,
[LIT-2964](../literature.d/LIT-2964.md), and the overlap is also Paul's, [LIT-3006](../literature.d/LIT-3006.md); see the note
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

The BBP paper ([LIT-2986](../literature.d/LIT-2986.md), read in [NOTE-2241](../notes.d/NOTE-2241.md); [THEORY-2148](../theory.d/THEORY-2148.md))
**qualifies** the case's attribution; its numbers stand.

- The formulas are exact after the change of notation, but z = √β·s·v + ε
  with s = ±1 is a real, non-Gaussian mixture, not BBP's complex Gaussian
  samples, and not Baik and Silverstein's T^(1/2)Z with identically
  distributed entries either (the coordinate along v differs).
- It is exactly Benaych-Georges and Nadakuditi's additive rank-one model
  (§3.1; [LIT-2964](../literature.d/LIT-2964.md), [THEORY-2152](../theory.d/THEORY-2152.md)): the data matrix √β·vsᵀ + E,
  divided by √N, is a Gaussian matrix plus a perturbation of singular
  value θ = √β, so the threshold θ > γ^(1/4) is β > √γ, the outlier is
  (1 + β)(1 + γ/β) and the overlap (1 − γ/β²)/(1 + γ/β) ([ARG-135](../arguments.d/ARG-135.md)).
- The overlap is also Paul's Theorem 4 for the covariance-spike reading
  ([LIT-3006](../literature.d/LIT-3006.md), [THEORY-2153](../theory.d/THEORY-2153.md); [ARG-143](../arguments.d/ARG-143.md)).

The case `draws_on` [THEORY-2152](../theory.d/THEORY-2152.md) and [THEORY-2153](../theory.d/THEORY-2153.md) for its check of
the PCA column. The "Deferred: registered, not read" parenthesis above is
updated.

## Note of 2026-11-22: Wang, Wu and Fan, read

Wang, Wu and Fan ([LIT-2984](../literature.d/LIT-2984.md), [NOTE-2274](../notes.d/NOTE-2274.md), [THEORY-2186](../theory.d/THEORY-2186.md)): **extends the
construction through L random layers.** Their Corollary 4 takes a
signal-plus-noise input X = Σθᵢaᵢbᵢᵀ + Z, this case's mixture when the
bᵢ are class-label vectors, and pushes it through a network with random
Gaussian weights. The input threshold has this case's form in their
normalization (noise entries of variance 1/d, γ0 the limit of n/d): a
spike for θᵢ "if and only if θᵢ > γ0^(1/4) and i ∈ Iℓ", where Iℓ is the set
that has passed a further BBP-type test at every layer up to ℓ. The
alignment with the labels is multiplied by a factor below one at each
layer, so the spectral column of this case can only get worse with depth at
random weights. The decodability column is not studied there. A note, no
relation: the case does not use the reading.
