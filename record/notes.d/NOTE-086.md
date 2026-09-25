---
number: 86
status: Skimmed
formerly:
- NOTE-tmpzg69x
paper: LIT-058
title: 'I-MMSE: mutual information and MMSE in Gaussian channels'
version: 1
date: '2026-09-25'
summary: >-
  For any finite-power input observed in additive Gaussian noise, the derivative of the input–output mutual information (in nats) with respect to SNR equals half the MMSE, whatever the input distribution (the I-MMSE identity). A consequence is that the causal filtering MMSE equals the average of the non-causal smoothing MMSE over SNRs uniform on [0, snr].
---

<!-- inactive-ok-file: LIT-058 — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-25 -->

# NOTE-086: I-MMSE: mutual information and MMSE in Gaussian channels

## Contribution

The paper considers arbitrarily distributed, finite-power inputs sent through an additive Gaussian noise channel and proves a formula linking the mutual information to the MMSE of the optimal estimator of the input given the output: dI/dsnr = mmse/2, independent of input statistics. The identity holds for scalar and vector channels and for discrete-time and continuous-time non-causal estimation. In continuous time it gives an unexpected result for nonlinear filtering: the causal (filtering) MMSE at a given SNR equals the non-causal (smoothing) MMSE averaged over SNR uniform between 0 and that SNR.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- Main identity (§I eq. 1; §II-A scalar, §II-B vector): I′(snr) = ½ mmse(snr) for every input with finite second moment. The authors call it simple yet previously unknown.
- Proof technique (§II-C, "incremental channels"): add an infinitesimal amount of extra Gaussian noise and read the resulting drop in mutual information as a low-SNR channel whose information is linear in the estimation error. Five proofs are given in total (§II-E, §III-E).
- Applications (§II-D): CDMA spectral efficiency under joint vs. separate decoding, and a one-line equivalence between "Gaussian inputs maximize I" and "Gaussian inputs maximize MMSE". GEXIT and the area property for sparse-graph codes reduce to MMSE statements.
- Continuous time (§III) and discrete time (§IV): the filtering-smoothing relation, derived via SNR- and time-incremental channels. Generalizations (§V) cover arbitrary preprocessing, feedback (via Kadota–Zakai–Ziv / Duncan), vector and complex channels.
- New representations (§VI): entropy and divergence written as integrals of MMSE, e.g. H(X) = lim_{snr→∞} I(X; √snr X + N) for discrete X.

## Open questions

- I-MMSE is the identity behind information-theoretic readings of diffusion models, where likelihoods and entropies are written as integrals of denoising MSE over noise levels. That makes it the probable root citation for such a note in the anthology. A deeper reading should confirm which later ML papers build directly on it.
- Check the regularity conditions (finite power, and what exactly "arbitrary input" allows) before citing it as unconditional.
