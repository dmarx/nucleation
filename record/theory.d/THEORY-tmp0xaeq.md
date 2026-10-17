---
status: Active
title: "For jointly Gaussian stationary processes, Granger causality in Geweke's generalized-variance form is exactly twice the transfer entropy, conditional and multivariate, at the regressions' lags, because least-squares residual covariance is the partial covariance and a Gaussian's conditional entropy is half its log-determinant plus a constant"
version: 1
tags:
- information-theory
- causality
date: '2026-10-16'
source:
- LIT-tmpmi22s
summary: >-
  Barnett, Barrett & Seth (2009), [LIT-tmpmi22s](../literature.d/LIT-tmpmi22s.md), read in full in [NOTE-tmp2veo7](../notes.d/NOTE-tmp2veo7.md).
  F_{Y→X|Z} = 2T_{Y→X|Z}, exactly, for population quantities. The proof
  is two identities and was checked. Sample agreement depends on the
  entropy estimator. Both quantities are predictive; the authors keep
  them apart from physical causation.
extended_by:
- THEORY-641
---

# THEORY-tmp0xaeq: For jointly Gaussian stationary processes, Granger causality in Geweke's generalized-variance form is exactly twice the transfer entropy, conditional and multivariate, at the regressions' lags, because least-squares residual covariance is the partial covariance and a Gaussian's conditional entropy is half its log-determinant plus a constant

## Source

Barnett, Barrett & Seth (2009), "Granger causality and transfer entropy
are equivalent for Gaussian variables", arXiv 0910.4514v2 (Phys. Rev.
Lett. 103, 238701), [LIT-tmpmi22s](../literature.d/LIT-tmpmi22s.md), read in full in [NOTE-tmp2veo7](../notes.d/NOTE-tmp2veo7.md). The PRL
version was not compared.

## What was actually shown

**The setting.** X_t, Y_t, Z_t jointly Gaussian and stationary, any
dimensions, lags p, q, r fixed. G-causality is Geweke's
F_{Y→X|Z} = ln(|Σ(X|X⁻⊕Z⁻)|/|Σ(X|X⁻⊕Y⁻⊕Z⁻)|) (Eq. 9). Transfer entropy is
T_{Y→X|Z} = H(X|X⁻⊕Z⁻) − H(X|X⁻⊕Y⁻⊕Z⁻) (Eq. 10).

**Two identities.** The OLS residual covariance of X on Y is the partial
covariance Σ(X|Y) (Eq. 3). For jointly Gaussian X, Y,
H(X|Y) = ½ln|Σ(X|Y)| + ½n ln(2πe), by |Σ(X⊕Y)| = |Σ(Y)|·|Σ(X|Y)| (Eq.
11). Both were checked.

**The result.** F_{Y→X|Z} = 2T_{Y→X|Z} (Eq. 13). With a univariate
predictee it is the standard log variance ratio (Eq. 8).

What could have come out otherwise: the identity needs the determinant.
With the trace (total variance) in place of the generalized variance, a
multivariate predictee would not give twice the transfer entropy. That
is the Letter's argument for Geweke's form.

## What this does not say

- **That either quantity measures causation in the interventional sense.**
  The authors say a G-causality interaction is not a physically
  instantiated one (p. 2). When it is, is [THEORY-tmp4g68i](THEORY-tmp4g68i.md)'s question.
- **That estimates agree in sample.** Covariance-based entropy estimates
  agree by construction. Partition, kernel and nearest-neighbour
  estimators need not (p. 7).
- **Anything outside Gaussianity.** That nonzero G-causality implies
  nonzero transfer entropy in general is cited, not shown. That nonlinear
  G-causality adds nothing for Gaussian AR processes rests on unpublished
  work.
- **That the regressions model the process.** They are predictive fits and
  may omit latent variables (fn. 31).

## Connections

- [THEORY-641](THEORY-641.md) generalizes this result: transfer entropy is the limit of a
  log-likelihood ratio under any well-specified parametric Markov model,
  and the linear Gaussian VAR is its case "half the Granger statistic".
- Geweke (1982, [LIT-tmpj9yuo](../literature.d/LIT-tmpj9yuo.md), Unavailable) is the source of Eq. 9 and of
  the frequency decomposition the authors propose to carry over to
  transfer entropy.
- [TERM-tmpq0ms2](../terms.d/TERM-tmpq0ms2.md) defines Granger causality in the record's own words.
