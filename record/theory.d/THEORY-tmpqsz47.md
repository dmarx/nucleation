---
status: Active
title: "In additive Gaussian noise independent of an input of finite power whose law does not depend on the signal-to-noise ratio, the derivative of mutual information with respect to that ratio is half the minimum mean-square error of the optimal noncausal estimator, so mutual information is accumulated estimation error over SNR; in continuous time the causal filtering error equals the noncausal error averaged over SNR, and the identity fails with feedback"
version: 1
tags:
- information-theory
- probabilistic-modeling
date: '2026-10-16'
source:
- LIT-058
summary: >-
  Guo, Shamai & Verdú (2004), [LIT-058](../literature.d/LIT-058.md), read in full in [NOTE-086](../notes.d/NOTE-086.md). Proved
  five ways for every finite-power input, in scalar, vector, discrete-time
  and continuous-time forms. It concerns the optimal, conditional-mean
  estimator; carrying it to a trained diffusion model's learned denoiser
  needs the mismatched version, which is later work. Theorems 3, 4 and 11
  are stated without proof.
---

# THEORY-tmpqsz47: In additive Gaussian noise independent of an input of finite power whose law does not depend on the signal-to-noise ratio, the derivative of mutual information with respect to that ratio is half the minimum mean-square error of the optimal noncausal estimator, so mutual information is accumulated estimation error over SNR; in continuous time the causal filtering error equals the noncausal error averaged over SNR, and the identity fails with feedback

## Source

Guo, Shamai & Verdú (2004), "Mutual Information and Minimum Mean-square
Error in Gaussian Channels", arXiv cs/0412108v1 (IEEE Trans. IT 51(4),
2005), [LIT-058](../literature.d/LIT-058.md), read in full in [NOTE-086](../notes.d/NOTE-086.md).

## What was actually shown

**Theorem 1.** For Y = √snr·X + N, N ~ N(0,1) independent of X, and any
P_X with E X² < ∞ (discrete, singular or heavy-tailed allowed):
d/dsnr I(X;Y) = ½·mmse(snr) in nats, equivalently I(snr) =
½∫₀^snr mmse(γ) dγ. Checks: a Gaussian input gives ½ log(1+snr) and
1/(1+snr); the ±1 input is verified in Appendix I.

**Why.** Gaussian noise is infinitely divisible, so the channel at snr is
a degraded version of the one at snr + δ. The information lost in the
step is a vanishing-SNR channel whose input law is the posterior, and at
vanishing SNR information is (δ/2)·variance. Averaging gives the MMSE.

**Theorem 2.** For Y = √snr·HX + N: d/dsnr I = ½·E‖HX − H·E[X|Y]‖². It is
equivalent to de Bruijn's identity.

**Continuous time (Theorems 6–8).** With Duncan's I = (snr/2)·cmmse,
cmmse(snr) = (1/snr)∫₀^snr mmse(γ) dγ: filtering error equals smoothing
error averaged over SNR uniform on [0, snr]. The authors know no
non-information-theoretic proof.

**Entropy as integrated MMSE (§VI).** H(X) = ½∫₀^∞ mmse(g(X) | √snr·g(X)
+ N) dsnr for any one-to-one g (Theorem 13), and the non-Gaussianness
D(P_X ‖ N(EX, σ²)) is an integral of the gap between the Gaussian and the
actual MMSE (Theorem 14).

What could have come out otherwise: the identity could have held only at
low SNR, as was known before. It holds at every SNR.

## What this does not say

- **That it holds with feedback.** If the input law depends on snr, the
  noncausal identity fails: §V-B's counterexample Z = X/√snr gives
  dI/dsnr = 0 with non-zero MMSE. Duncan's causal identity survives.
- **That filtering equals averaged smoothing in discrete time.** There
  only the sandwich (snr/2)·Σ cmmse ≤ I ≤ (snr/2)·Σ pmmse holds (Theorem
  9).
- **Anything for non-Gaussian noise.** Infinite divisibility and
  independent increments are essential.
- **That a diffusion model's likelihood bound is proved by it.** The
  identity concerns the optimal estimator. A learned denoiser needs the
  mismatched-estimation version, which is not in this paper ([NOTE-086](../notes.d/NOTE-086.md),
  Bearing).
- **Theorems 3, 4 and 11.** Stated without proof, or with the proof
  omitted.

## Connections

- [NOTE-086](../notes.d/NOTE-086.md) marks this as the root of the reading that diffusion-model
  likelihoods are integrals of denoising error over noise levels, which
  [ANTH-THEORY-027](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/theory.d/THEORY-027.md) and [ANTH-THEORY-107](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/theory.d/THEORY-107.md) rest on without citing it.
- The conditional Schrödinger bridge ([THEORY-tmpes2tv](THEORY-tmpes2tv.md)) trains with the
  denoising losses this Gaussian calculus underlies.
- The Gaussian-input check, ½ log(1+snr) = ½∫₀^snr dγ/(1+γ), is the
  per-dimension form of Shannon's white-noise capacity ([THEORY-tmpotoox](THEORY-tmpotoox.md)).
