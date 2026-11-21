---
status: Skimmed
paper: LIT-tmp1q78e
title: 'Benaych-Georges and Nadakuditi, The singular values and vectors of low rank perturbations of large rectangular random matrices, read for the Gaussian matrix with a non-zero mean'
version: 1
history:
- version: 1
  date: '2026-11-21'
  note: >-
    Read on 2026-11-21 by a delegated reader, as a supplement to the BBP
    paper (NOTE-tmpggv08), from arXiv 1103.2221v2 (26 Jan 2012), the
    authors' PDF: the abstract and §3.1 (pp. 9–10), with equations (9)
    to (11). The general theorems of §2 and their proofs were not read,
    hence Skimmed. Running notes on the branch claude/readers/lit-tmpipm3o.
    The section heading and equations (9) and (10) rechecked by the filer
    against the downloaded text, and the change of notation by hand.
date: '2026-11-21'
summary: >-
  An n × m Gaussian matrix with entries of variance 1/m, plus a
  deterministic perturbation of fixed rank with singular values θ_i, at
  n/m → c ∈ (0, 1]: the top singular values leave the bulk edge 1 + √c
  exactly for θ_i > c^(1/4), at √((1 + θ²)(c + θ²)/θ²), and the left
  singular vector's squared overlap tends to 1 − c(1 + θ²)/(θ²(θ² + c)).
  In the record's notation these are the spiked formulas, for an additive
  signal-plus-noise model.
---
<!-- inactive-ok-file: THEORY-tmp4zojc THEORY-tmp0covn THEORY-tmp0zr7o THEORY-tmp6808g CASE-tmp59xy5 CLAIM-tmpk33au CLAIM-tmp5y856 CLAIM-tmpqbo50 ARG-tmpe2vrk ARG-tmpnwmcr — Proposed; the reading and the entries it bears on -->

# NOTE-tmpor0h4: Benaych-Georges and Nadakuditi, The singular values and vectors of low rank perturbations of large rectangular random matrices, read for the Gaussian matrix with a non-zero mean

## Contribution

A general theory, through a free-probability integral transform, of when a
low-rank perturbation of a large rectangular random matrix shows in its
extreme singular values and vectors. The abstract: the extreme singular
values move "if and only if the singular values of the perturbing matrix
are above a certain critical threshold". The reading is THEORY-tmp4zojc.

## Key results

- **The example the record uses** (§3.1, "Gaussian rectangular random
  matrices with non-zero mean", p. 9). X_n is n × m with independent
  zero-mean normal entries of variance 1/m, real or complex; P_n is
  deterministic, of fixed rank r, with singular values θ_i; n/m → c ∈ (0, 1].
- **Singular values** (9): σ_i(X_n + P_n) → √((1 + θ_i²)(c + θ_i²)/θ_i²)
  almost surely if θ_i > c^(1/4), and → 1 + √c otherwise.
- **Singular vectors** (10), r = 1, P_n = θuv*: |⟨ũ, u⟩|² →
  1 − c(1 + θ²)/(θ²(θ² + c)) if θ ≥ c^(1/4), and → 0 otherwise; (11)
  gives the right singular vector, 1 − (c + θ²)/(θ²(θ² + 1)).

## Assumptions

Gaussian noise of independent entries; a deterministic perturbation (or
one independent of the noise) of fixed rank; c ≤ 1 in §3.1, the other case
following by transposition.

## Concepts

Information-plus-noise (signal-plus-noise) matrix; low-rank additive
perturbation; the singular value phase transition; the D-transform.

## Connections

In the record's notation, n = D, m = N, c = γ = D/N and β = θ²: the
threshold is β > √γ, the top eigenvalue of the uncentred second moment
(1/N)ZZᵀ is σ² = (1 + β)(1 + γ/β), and the squared overlap is
1 − γ(1 + β)/(β(β + γ)) = (1 − γ/β²)/(1 + γ/β). These are the spiked
formulas of BBP (THEORY-tmp0covn), Baik and Silverstein (THEORY-tmp0zr7o)
and Paul (THEORY-tmp6808g), for a different model: a signal added to the
data matrix rather than a covariance acting on the samples.

## Bearing on the record

- **CASE-tmp59xy5** (gives its model). z = √β·s·v + ε with s = ±1 is the
  data matrix √β·vsᵀ + E; scaled by 1/√N it is X_n + P_n with
  P_n = √β·v(s/√N)ᵀ, a rank-one perturbation of singular value θ = √β. So
  the case's threshold, outlier and overlap are (9) and (10), not BBP's,
  whose samples are Gaussian. ARG-tmpe2vrk.
- **CLAIM-tmpk33au** (gives the mean-shift step). N samples of
  N(cμ, I), seen by PCA on the uncentred second moment, are
  cμ1ᵀ + E, a rank-one perturbation of singular value θ = c; the threshold
  θ > γ^(1/4) gives κ_BBP = √D·(D/N)^(1/4). ARG-tmpe2vrk.
- **CLAIM-tmp5y856** (corroborates the eigenvector clause, for the
  additive model). ARG-tmpnwmcr.
- **CLAIM-tmpqbo50** (fits its hidden-layer model). With φ independent of
  ξ, h = bφu + σξ is again an additive rank-one model.
- **NOTE-666, LIT-862, NOTE-659** (already cite it): Saxe and colleagues'
  coherence threshold is its Theorem 2.9, θ > c^(1/4).

## Limitations

Only §3.1 was read: the general theorems, the fluctuations and the
conditions for non-Gaussian noise were not. §3.1 states c ≤ 1.
