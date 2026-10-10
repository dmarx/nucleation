---
number: 180
status: Proposed
formerly:
- THEORY-tmpjhj8u
promote_when: >-
  A proof of the spectral law for a trained attention layer with T ≥ 2
  tokens, or a held, independent derivation of it by another route, read
  in the record: for instance the multi-token Gaussian-universality and
  AMP bound arguments the paper says are still missing, or the T = 1
  linear case (Erba et al. 2025) read and found to prove the same
  thresholded law, together with a check that the softmax and the extra
  tokens change only the order parameters. The account is refuted by
  simulations of this model at growing d, in the stated limit and where the
  replicon condition holds, whose global-minimum spectrum does not
  converge to η·ReLU(S0 + δZ − ε): outliers that do not track the target's
  eigenvalues, or a bulk that is not a thresholded semicircle deformation.
  More qualitative resemblance between these spectra and those of trained
  transformers cannot settle it: that tests an analogy, not the law.
title: 'In a tied single-head attention layer trained by ridge-penalized empirical risk minimization on high-dimensional Gaussian sequences, weight decay is a nuclear-norm penalty on the query–key map, and the learned map is a soft-thresholded noisy copy of the target: its outliers are recovered target directions and its bulk is finite-sample noise'
version: 1
tags:
- learning-theory
- mathematics
- anthology-candidate
date: '2026-10-09'
source:
- LIT-857
summary: >-
  Boncoraglio, Erba, Troiani, Xu, Krzakala & Zdeborová (2025), [LIT-857](../literature.d/LIT-857.md):
  with S = WWᵀ, λ‖W‖²_F is exactly λ‖S‖_* (Appendix A), and in the limit
  n/d², p/d fixed the trained WᵀW/√(pd) has the law η·ReLU(S0 + δZ − εI),
  Z ∼ GOE, with δ a noise level that falls with the data and ε a threshold
  set by λ (Claim 4.1, replica/AMP, checked against Adam at d ≤ 400). It does
  not say that real transformers' spectra arise this way: the data are
  isotropic Gaussian, the target is inside the model class, and the
  agreement with measured spectra is qualitative.
supports:
- CLAIM-148
---

<!-- inactive-ok-file: THEORY-106 — Proposed; compared in scope below -->

# THEORY-180: In a tied single-head attention layer trained by ridge-penalized empirical risk minimization on high-dimensional Gaussian sequences, weight decay is a nuclear-norm penalty on the query–key map, and the learned map is a soft-thresholded noisy copy of the target: its outliers are recovered target directions and its bulk is finite-sample noise

## Source

Boncoraglio, Erba, Troiani, Xu, Krzakala & Zdeborová (2025), [LIT-857](../literature.d/LIT-857.md),
read in [NOTE-661](../notes.d/NOTE-661.md): Appendix A, Claims 3.1 and 4.1, Section 4 and
Figures 1, 4 and 8.

## What was actually shown

Two things of different strength.

**An identity, proved.** For tied weights, ‖W‖²_F = Tr(WᵀW) = ‖WᵀW‖_*,
so square-penalized training of W is nuclear-norm-penalized training of
the PSD map S = WWᵀ; for untied factors the balanced SVD factorization
makes min (‖U‖²_F + ‖V‖²_F)/2 over UVᵀ = M equal to ‖M‖_*. This holds for
any loss that depends on the weights only through the product.

**A spectral law, derived non-rigorously.** The layer is
softmax_β((x WWᵀ xᵀ − centring)/√(dp)) x, trained on square loss plus
λ‖W‖²_F, with T i.i.d. N(0, I_d) tokens and a target of the same form
with a rank-κ₀d matrix S0 and Gaussian noise on its pre-activations. As
d, n, p → ∞ with n/d² and p/d fixed, an AMP algorithm whose matrix step is
a spectral soft-threshold, analysed by state evolution, gives the global
minimizer's spectrum as η·ReLU(S0 + δZ − εI), with (η, δ, ε) from a
six-parameter variational problem. δ shrinks as samples grow; ε grows
with λ. Eigenvalues of S0 strong enough to separate from the noise bulk,
and above the threshold, come out as outliers; the rest, and the noise,
form a bulk or are cut to zero. The
derivation is a claim with a proof sketch, valid under a replicon
condition checked numerically. Adam runs at d = 100–400 reproduce the
predicted histograms, including the delta at zero and the split into two
bulks, and could have failed to (a non-convex loss with spurious minima
would have).

Under a further conjecture (validity for any large n, d), the excess
error splits into an overfitting term carried by the bulk, an
underfitting term for target directions still inside it, and an
approximation term along the outliers.

## What this does not say

- **Not that trained transformers' spectra come from this.** Real
  attention has untied, multi-head weights, non-Gaussian correlated tokens
  and targets outside any bilinear class. The paper claims only
  qualitative agreement with measured spectra, and none is quantified.
- **Not proved.** The identity is; the spectral law is not. Gaussian
  universality for T ≥ 2 and the AMP bounds are stated as remaining work.
- **Not about training dynamics.** It characterizes global minima. That
  gradient methods reach them is shown only by simulation; the paper's
  account of emergence is a sequence of minima as n or λ change, not a
  claim about plateaus in time.
- **Not that low rank is free in general.** "Every width above a
  threshold attains the same error" is a statement about this model's
  global minimum under weight decay, where the penalty already enforces
  the low rank.
- **Not that heavy tails mean self-regularization.** In this model, heavy
  tails in the learned spectrum appear only when the target's spectrum is a
  power law: they are the target's tail recovered mode by mode.
- **Not [THEORY-106](THEORY-106.md)'s case.** That account is for random features, whose
  features are not learned. This model's interpolation peak is not shown
  to diverge; Appendix G's simulations suggest a large but finite one.
