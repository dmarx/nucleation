---
status: Proposed
title: "A mean shift seen by PCA on the uncentred second moment, and a two-class mixture along one direction, are low-rank additive perturbations of a Gaussian matrix, so Benaych-Georges and Nadakuditi's theorem, not the spiked-covariance one, gives their threshold and formulas"
version: 1
form: formal-application
grounds:
- THEORY-tmp4zojc
concludes:
- CLAIM-tmpk33au
tags:
- mathematical-statistics
- representation-learning
date: '2026-11-21'
line:
- learned-structure
summary: >-
  [CLAIM-tmpk33au](../claims.d/CLAIM-tmpk33au.md) says PCA sees a mean shift c along μ "as a spike β = c² in
  the uncentred second moment", and puts the BBP threshold at
  κ = √D·(D/N)^(1/4); [CASE-tmp59xy5](../cases.d/CASE-tmp59xy5.md) applies BBP to z = √β·s·v + ε with
  s = ±1. Neither model is a spiked covariance sample: BBP centres by the
  sample mean, which removes a shift, and the mixture is not Gaussian. Both
  are rank-one additive perturbations, X + P, and Benaych-Georges and
  Nadakuditi's §3.1 gives the threshold θ > γ^(1/4) and the same formulas.
  The claim's result stands, on that theorem. The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmpk33au CASE-tmp59xy5 THEORY-tmp4zojc ARG-tmpvalfs — Proposed; the claim, case, reading and neighbouring argument -->

# ARG-tmpe2vrk: A mean shift seen by PCA on the uncentred second moment, and a two-class mixture along one direction, are low-rank additive perturbations of a Gaussian matrix, so Benaych-Georges and Nadakuditi's theorem, not the spiked-covariance one, gives their threshold and formulas

## The inference

Benaych-Georges and Nadakuditi, §3.1: X_n n × m with N(0, 1/m) entries,
n/m → c ∈ (0, 1], P_n deterministic of rank one with singular value θ; the
top singular value leaves 1 + √c for θ > c^(1/4), at
√((1 + θ²)(c + θ²)/θ²) (9), with overlap (10).

## Critical questions (formal application)

**Does the mapping premise hold?**
- *Mean shift ([CLAIM-tmpk33au](../claims.d/CLAIM-tmpk33au.md)).* N samples x_i ∼ N(cμ, I_D) form the
  D × N matrix cμ1ᵀ + E. Divided by √N: X_n = E/√N (n = D, m = N, entries
  of variance 1/N) and P_n = cμ(1/√N)ᵀ, of singular value θ = c. The
  eigenvalues of the uncentred second moment (1/N)Σxᵢxᵢᵀ that PCA uses are the
  squared singular values. So the outlier appears for c > γ^(1/4), at
  (1 + c²)(1 + γ/c²): the claim's "spike β = c²", threshold
  κ_BBP = √D·(D/N)^(1/4), and its simulated values (3.56 against 3.61 at
  γ = 0.25, c = 1.5) are this formula.
- *Mixture ([CASE-tmp59xy5](../cases.d/CASE-tmp59xy5.md)).* z = √β·s·v + ε gives √β·vsᵀ + E; divided by
  √N, P_n = √β·v(s/√N)ᵀ with ‖s/√N‖ = 1, so θ = √β, threshold
  β > √γ, outlier (1 + β)(1 + γ/β), overlap (1 − γ/β²)/(1 + γ/β): the
  case's formulas.

**Are the model's assumptions met?** Gaussian noise, yes. P_n must be
deterministic or independent of the noise: conditioning on the labels s,
or on μ, makes it so. §3.1 states c ≤ 1, D ≤ N; the claim's N ≪ D remark
("later when N ≪ D") lies outside what was read, though the theorem's
general form covers it by transposition. A centred covariance would remove
the mean shift entirely, so the claim must be read, as it says, of the
uncentred second moment.

## Verdict

[THEORY-tmp4zojc](../theory.d/THEORY-tmp4zojc.md) goes into [CLAIM-tmpk33au](../claims.d/CLAIM-tmpk33au.md)'s grounds and [CASE-tmp59xy5](../cases.d/CASE-tmp59xy5.md) draws
on it. The claim's numbers stand; the attribution changes from BBP to this
theorem for the mean-shift step. Its mean-field precursor, a covariance
spike, rests on Baik and Silverstein instead ([ARG-tmpvalfs](ARG-tmpvalfs.md)).
