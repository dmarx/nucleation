---
status: Deferred
status_note: seeded from the abstract and a skim on 2026-09-25; not read in full
title: 'Mutual Information and Minimum Mean-square Error in Gaussian Channels'
version: 1
tags:
- information-theory
- probabilistic-modeling
date: '2026-09-25'
published: '2004-12-23'
arxiv: 'cs/0412108'
doi: '10.1109/TIT.2005.844072'
first_author: 'Guo'
keywords:
- 'Gaussian channel'
- 'minimum mean-square error (MMSE)'
- 'mutual information'
- 'nonlinear filtering'
- 'optimal estimation'
- 'smoothing'
- 'Wiener process'
implementations: []
summary: >-
  Guo et al. (2004), [arXiv:cs/0412108](https://arxiv.org/abs/cs/0412108). For any finite-power input observed in additive Gaussian noise, the derivative of the input–output mutual information (in nats) with respect to SNR equals half the MMSE, whatever the input distribution (the I-MMSE identity). A consequence is that the causal filtering MMSE equals the average of the non-causal smoothing MMSE over SNRs uniform on [0, snr].
---

# LIT-tmpe1irs: Mutual Information and Minimum Mean-square Error in Gaussian Channels

Dongning Guo, Shlomo Shamai (Shitz), Sergio Verdú (2004), *IEEE Transactions on Information Theory 51(4):1261–1282 (April 2005)* — [arXiv:cs/0412108](https://arxiv.org/abs/cs/0412108)

## Key takeaways

- For any finite-power input observed in additive Gaussian noise, the derivative of the input–output mutual information (in nats) with respect to SNR equals half the MMSE, whatever the input distribution (the I-MMSE identity). A consequence is that the causal filtering MMSE equals the average of the non-causal smoothing MMSE over SNRs uniform on [0, snr].

*Seeded from the abstract and a skim, not a reading. What follows is what the work says about itself.*

The paper considers arbitrarily distributed, finite-power inputs sent through an additive Gaussian noise channel and proves a formula linking the mutual information to the MMSE of the optimal estimator of the input given the output: dI/dsnr = mmse/2, independent of input statistics. The identity holds for scalar and vector channels and for discrete-time and continuous-time non-causal estimation. In continuous time it gives an unexpected result for nonlinear filtering: the causal (filtering) MMSE at a given SNR equals the non-causal (smoothing) MMSE averaged over SNR uniform between 0 and that SNR.

## Standing in the record

Filed from the survey of 2026-09-25 of work the anthology set aside as out of scope (tier C): 330 seconds of active reading over 2 sessions in the papers-feed tracker. `Deferred` because nobody has read it closely here yet, not on merit.

**Priority for a deeper reading: medium — A foundational result with a live ML descendant (diffusion likelihoods). The owner's time is moderate (t=330 s). The skim captures the theorem, but the proofs and conditions deserve a proper read if this becomes a cited source.**

What a deeper reading should check:

- I-MMSE is the identity behind information-theoretic readings of diffusion models, where likelihoods and entropies are written as integrals of denoising MSE over noise levels. That makes it the probable root citation for such a note in the anthology. A deeper reading should confirm which later ML papers build directly on it.
- Check the regularity conditions (finite power, and what exactly "arbitrary input" allows) before citing it as unconditional.

Access when seeded: I read the arXiv abstract page (v1 23 Dec 2004) and the full arXiv PDF (22 pp., marked "IEEE Trans. Inform. Theory, 2005, to appear"). I read §I, §II-D, §V headings, §VI and §VII, and skimmed the rest by section heads. Crossref confirms the IEEE DOI, the April 2005 issue and pp. 1261–1282. Crossref capitalizes "Mean-Square" where arXiv has "Mean-square"; the title above is arXiv's. A same-titled ISIT 2004 conference version is plausible but unverified.
