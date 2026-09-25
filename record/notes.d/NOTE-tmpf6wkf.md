---
status: Skimmed
paper: LIT-tmp8ahjz
title: 'Transfer entropy as a log-likelihood ratio'
version: 1
date: '2026-09-25'
summary: >-
  For a broad class of Markov predictive models, the log-likelihood-ratio statistic for "zero transfer entropy" is a consistent estimator of the transfer entropy itself, with a standard asymptotic χ² null distribution. This generalizes the Gaussian equivalence of transfer entropy and Granger causality.
---

<!-- inactive-ok-file: LIT-tmp8ahjz — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-25 -->

# NOTE-tmpf6wkf: Transfer entropy as a log-likelihood ratio

## Contribution

Transfer entropy measures time-directed information flow between processes and is widely used in neuroscience, ecology, climatology and econometrics, but it is hard to estimate. The authors show that, for a wide class of parametric predictive models, the likelihood-ratio test statistic for the null of zero transfer entropy, suitably normalized, converges to the transfer entropy. For finite-state Markov chains no explicit model is needed, because the plug-in estimator is already of this form. In general the estimator is asymptotically χ²-distributed, which permits significance tests. The result extends the known Gaussian equivalence of transfer entropy and Granger causality, and ties Schreiber-style information transfer to Wiener–Granger causality.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- Setup (eqs 1–5): the authors define k-lag transfer entropy T_{Y→X} as a difference of conditional entropies. They use a deliberately misspecified "extended" full model, in which Y is independent of X given the joint history, and show this is harmless.
- Props 1–2 (eqs 11–13): under an ergodicity assumption, the average log-likelihood converges to minus the conditional entropy, and the ML estimator stays consistent for the partial-model parameters despite the misspecification.
- Theorem 1 (eq. 16 onward): T̂ = −(1/(n−k)) log Λ converges almost surely to T. Under the null, 2(n−k)T̂ is asymptotically χ²(d). Under the alternative it is non-central χ² with λ = 2(n−k)T. The estimator is consistent but generally biased.
- Special cases (pp. 5–6): for a linear Gaussian VAR the estimator is half the Granger causality, recovering Barnett, Barrett & Seth (2009). The result extends to conditional transfer entropy. In the discrete case it coincides with the standard plug-in estimator (eq. 21).
- Closing (p. 7): the stated payoff is χ² significance testing and confidence intervals without surrogate or subsampling methods. The authors anticipate an extension to point processes and spiking neurons.

## Open questions

- It is a clean bridge between an information-theoretic quantity and standard likelihood inference. That is useful background for any causal or directed-information analysis of time series, including analysis of learned systems.
- A deeper reading should check the ergodicity condition (eq. 10) and how slowly the non-central χ² converges in practice (the authors flag it). Also check how the result compares with the later literature on transfer-entropy estimator bias.
