---
status: Proposed
title: "Baik and Silverstein's almost-sure limits carry the spiked threshold and outlier location to real samples, to more variables than samples, and to each of finitely many spikes, as the claims that apply them need"
version: 1
form: formal-application
grounds:
- THEORY-tmp0zr7o
concludes:
- CLAIM-tmp5y856
- CLAIM-tmp8mvx8
- CLAIM-tmpqbo50
- CLAIM-tmpk33au
tags:
- mathematical-statistics
- representation-learning
date: '2026-11-21'
line:
- learned-structure
summary: >-
  The record's spiked-matrix claims apply the threshold β > √(D/N) and the
  outlier (1 + β)(1 + γ/β) to real-valued data, to each of several spikes
  (CLAIM-tmp8mvx8), at D > N (CLAIM-tmpqbo50's γ = 4 row) and to a
  mean-field ordering mode (CLAIM-tmpk33au). Baik and Silverstein's
  theorem (THEORY-tmp0zr7o) is the result that covers those settings, for
  limits, with finitely many fixed spikes. The application holds in the
  sparse regime and fails, as CLAIM-tmp8mvx8 already finds, when the
  number of spikes grows with D. The wording is the assistant's (Claude,
  in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmp5y856 CLAIM-tmp8mvx8 CLAIM-tmpqbo50 CLAIM-tmpk33au THEORY-tmp0zr7o ARG-tmpe2vrk — Proposed; the claims, the reading and the neighbouring argument -->

# ARG-tmpvalfs: Baik and Silverstein's almost-sure limits carry the spiked threshold and outlier location to real samples, to more variables than samples, and to each of finitely many spikes, as the claims that apply them need

## The inference

Baik and Silverstein: samples T^(1/2)Z with i.i.d. standardized entries of
finite fourth moment, real or complex, p/n → c > 0, finitely many fixed
spikes; each spike α_j > 1 + √c gives sample eigenvalues tending almost
surely to α_j + cα_j/(α_j − 1) (1.10), and with one spike the top
eigenvalue tends to (1 + √c)² otherwise (1.14). With c = γ = D/N and
α = 1 + β, that is the threshold β > √γ and the outlier
(1 + β)(1 + γ/β), at every γ, for each spike.

## Critical questions (formal application)

**Does the mapping premise hold?** Yes: the notation maps one to one, and
the filer checked the algebra, α + cα/(α − 1) = (1 + β)(1 + γ/β).

**Are the model's assumptions met in the new domain?**
- *CLAIM-tmp5y856*: real Gaussian data with a covariance spike, Σ = I + βvvᵀ;
  met. (Its illustrating case, a ±1 mixture, is not of this form; see
  ARG-tmpe2vrk.)
- *CLAIM-tmp8mvx8*: orthogonal spikes β_j = Cj^(−α), each giving its own
  outlier; met while K is fixed as D grows. The claim's own row 5 (K/D =
  0.4, 84 outliers against 143 predicted) is where the assumption fails,
  and the claim already says "Sparse regime only".
- *CLAIM-tmpqbo50*: σ²I + ℓuuᵀ at γ = 4, 1, 0.25, 0.01; the γ = 4 row is
  D > N, which BBP excludes and this theorem covers (c > 1, same
  threshold 1 + √c). Its hidden-layer model h = bφu + σξ is T^(1/2)Z only
  if φ is Gaussian; otherwise it is the additive model of ARG-tmpe2vrk,
  with the same formulas.
- *CLAIM-tmpk33au*: the mean-field precursor treats the ordering mode below
  K = D as a covariance spike of strength θ² = γ(K/D)/(1 − K/D) in real
  Gaussian-approximated data; met within that approximation, which the
  claim states.

## Verdict

THEORY-tmp0zr7o goes into the grounds of all four claims. What it does not
supply is fluctuations, which only the claims' remarks about the
N^(−2/3) window near the edge need; those are BBP's, for complex data.
