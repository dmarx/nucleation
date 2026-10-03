---
number: 519
status: Read
formerly:
- NOTE-tmp61xwr
paper: 'LIT-679'
title: 'A Random Matrix Analysis of Random Fourier Features: Beyond the Gaussian Kernel, a Precise Phase Transition, and the Corresponding Double Descent'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read from arXiv v2 (31 pages, text layer). Sections 1–5 read in full,
    with the theorem statements checked against the extracted equations.
    Appendix A (proof of Theorem 1 through an intermediate resolvent and
    Lemma 1's integration tricks) followed in outline; Appendices B–D
    (proofs of Theorems 2–3 and the lemmas, including Lemma 5 on det(Ω⁻¹)
    and Lemma 7 on monotonicity of δ) skimmed. Equations (16)–(17) for the
    ridgeless limits did not survive text extraction and are described from
    the surrounding prose, not quoted.
date: '2026-10-03'
summary: >-
  Q̄ = ((N/n)(Kcos/(1+δcos) + Ksin/(1+δsin)) + λI)⁻¹ with δσ = (1/n) tr KσQ̄
  is a deterministic equivalent for E_W[(ΣXᵀΣX/n + λI)⁻¹] (Theorem 1); Ē_train
  and Ē_test follow (Theorems 2–3). As λ → 0, δ ~ 1/λ for 2N < n and O(1)
  for 2N > n; det(Ω⁻¹) ~ λ, so Ē_test → ∞ at 2N = n unless the test set is
  within σ² ≲ λ of the training set. N/n → ∞ recovers Gaussian kernel
  regression. Theory matches MNIST, Fashion- and Kannada-MNIST.
---

<!-- inactive-ok-file: THEORY-080 — Proposed; named for its use of the effective number of parameters, with no relation claimed -->

# NOTE-519: A Random Matrix Analysis of Random Fourier Features: Beyond the Gaussian Kernel, a Precise Phase Transition, and the Corresponding Double Descent

## Contribution

An exact asymptotic description of random Fourier feature ridge regression
in the proportional regime, where sample size, input dimension and number
of features grow together. Before it, RFF analyses either let N → ∞ (and so
used the Gaussian kernel) or bounded the number of features needed. Double
descent analyses of random features (Mei and Montanari) assumed Gaussian
data. After it, the training and test errors are given by a fixed-point
equation on two data kernels, valid for concentrated data, and the
double-descent peak is located and explained as the boundary between two
regimes of that fixed point.

## Key insight

With finitely many random features, the cosine and sine parts of the
feature map do not stay orthogonal: their kernel eigenspaces "intersect",
and two scalars δcos and δsin measure by how much. Those scalars act like
a data-dependent extra regularization. When there are fewer than n/2
features and the explicit ridge goes to zero, they blow up like 1/λ. With
more, they stay bounded. The test error's peak at 2N = n is where the
system passes from one behaviour to the other, and it is only a peak when
nothing regularizes it.

## Assumptions

- **Proportional regime** (Assumption 1): 0 < lim inf min(p/n, N/n) ≤ lim
  sup max(p/n, N/n) < ∞; ‖X‖ and ‖y‖∞ bounded, so the data are normalized
  with respect to n.
- **Features**: W ∈ ℝ^{N×p} with i.i.d. N(0, 1) entries, drawn once;
  ΣXᵀ = [cos(WX)ᵀ, sin(WX)ᵀ], so the feature dimension is 2N.
- **Ridge regressor** (Eq. 5): β = (1/n)ΣX((1/n)ΣXᵀΣX + λIn)⁻¹y, λ > 0
  for the theorems.
- **Test data** (Assumption 2): training points drawn independently from
  one of K classes, each a concentrated random vector,
  P(|f(xi) − E f(xi)| ≥ t) ≤ C e^{−(t/η)^q} for 1-Lipschitz f. Test points
  may depend on the training data, subject to ‖E[σ(WX) − σ(WX̂)]‖ = O(√n).
  This allows X̂ = X and X̂ = X + noise.

## Key results

- **Warm-up (Section 1.1).** For the sample covariance with C = I and
  n = 100p, ‖Ĉ − C‖/‖C‖ ≈ 20%, and the Marčenko–Pastur support has width
  4√c = 0.4 (Eq. 3). Bilinear forms of the resolvent follow m(λ) solving
  cλm² + (1 + λ − c)m − 1 = 0 (Eq. 4), not (C + λI)⁻¹ (Figure 2).
- **Theorem 1.** ‖E_W[Q] − Q̄‖ → 0 with Q̄ as in the summary. The
  equivalent is computable by fixed-point iteration on Kcos and Ksin.
  Remark 3 reads δcos, δsin as an eigenvalue-weighted "angle" between the
  eigenspaces of Kcos, Ksin and of their weighted sum.
- **Theorem 2 (training MSE).** Ē_train = (λ²/n)‖Q̄y‖² plus a second-order
  term through Ω⁻¹ = I₂ − (N/n)[(1/n)tr(Q̄KσQ̄Kσ′)/(1+δ)²] (Eqs. 10–11). As
  N/n → ∞ it goes to 0 and the model interpolates (Remark 4). Ē_train falls
  with N and rises with λ (Remark 5).
- **Theorem 3 (test MSE).** Ē_test = (1/n̂)‖ŷ − (N/n)Φ̂Q̄y‖² plus a
  second-order term weighted by Θσ (Eqs. 13–14). Setting (X̂, ŷ) = (X, y)
  recovers Ē_train (Remark 6). As N/n → ∞ it becomes the Gaussian kernel
  test error ‖ŷ − K(X̂, X)K⁻¹y‖²/n̂, which is not zero and does not depend
  on λ (Remark 7).
- **Empirics.** On MNIST 3 versus 7 (p = 784, n = 1,000), the Gaussian
  kernel mispredicts training MSE for N/n < 1 while the theory fits
  (Figure 4). The δ decrease in λ and in N (Lemma 7). The test MSE has a
  singular peak at 2N = n for λ = 10⁻⁷ and 10⁻³ and is smooth and
  decreasing for λ = 0.2 and 10 (Figure 7, n = 500).
- **Ridgeless phases (Section 4.1).** For 2N < n the scaled γσ and λQ̄
  stay O(1) and go to 0 as 2N − n ↑ 0, so the training error tends to a
  nonzero limit and then to 0 at the threshold. For 2N > n, δ and ‖Q̄‖
  diverge as 2N − n ↓ 0 and vanish as N/n → ∞. det(Ω⁻¹) scales as λ, so
  Ē_test diverges at 2N = n (Lemma 5, Figure 9).
- **Training–test similarity (Section 4.2).** For X̂ = X + σε at N = 512,
  n = 1,024: below σ² = λ the test error equals the training error and is
  near zero; above it, the test error grows linearly in σ² (Figure 10).
- **Other data.** Fashion-MNIST and Kannada-MNIST show the same fit, the
  same jump in δ at 2N = n and the same double-descent curves (Figures
  11–13).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | In the proportional regime the RFF Gram matrix is not close to the Gaussian kernel in spectral norm, and its resolvent has the deterministic equivalent Q̄ | strong (theorem) | Theorem 1, Appendix A |
| C2 | Training and test MSE of RFF ridge regression converge almost surely to the closed forms | strong (theorems) under Assumptions 1–2 and λ > 0 | Theorems 2–3 |
| C3 | Ridgeless RFF regression has two phases, 2N < n and 2N > n, with a sharp transition in δ at 2N = n | strong for the limit; shown numerically at λ = 10⁻⁷ | Section 4.1, Figures 6, 8 |
| C4 | The double-descent peak is the divergence of the test error at that transition, and it needs the test data to be dissimilar from the training data | strong for this model | Section 4.1–4.2, Figure 10 |
| C5 | The results hold without Gaussian data | moderate: concentrated random vectors are a broad class, and three image datasets agree | Assumption 2, Figures 11–13 |
| C6 | Double descent is "presumably" a consequence of a phase transition in many other models | weak: an aside | Remark 9 |

## Concepts

- **deterministic equivalent**: a deterministic matrix Q̄ such that
  bilinear forms and normalized traces of the random resolvent Q are close
  to those of Q̄.
- **δcos, δsin**: the correction pair solving the fixed point in Theorem 1,
  read as an "angle" between kernel eigenspaces.
- **concentrated random vector**: one for which every 1-Lipschitz function
  concentrates with tail Ce^{−(t/η)^q}.
- **under- and over-parameterized phase**: 2N < n and 2N > n. The threshold
  is 2N, not N, because cos and sin double the feature dimension.

## Connections

- **Martin and Mahoney ([LIT-672](../literature.d/LIT-672.md))** for the thermodynamic limit and the
  phase reading of double descent (Remark 9).
- **Mei and Montanari (2019)**: random-features double descent for Gaussian
  data, which this paper extends to RFF and concentrated data.
- **Louart, Liao and Couillet (2018)**: the earlier random-matrix approach
  to single-layer random networks that this builds on.
- **Rahimi and Recht (2008)**: RFF and the Gaussian-kernel limit.
- **Dereziński et al. ([LIT-683](../literature.d/LIT-683.md))**: in the reference list; it and this
  paper both obtain an implicit regularization from a self-consistent trace
  equation.

## Bearing on the record

- **The record's kernel-regime theories ([THEORY-086](../theory.d/THEORY-086.md) and the NTK readings
  [LIT-608](../literature.d/LIT-608.md), [LIT-612](../literature.d/LIT-612.md), [LIT-624](../literature.d/LIT-624.md))** are infinite-width statements. This paper is
  the finite-ratio correction for the simplest random-feature model: as long
  as N/n is finite, kernel predictions are biased, worst below N/n = 1/2.
- **Effective dimension.** δσ = (1/n) tr(KσQ̄) is a regularized trace of the
  same kind as MacKay's number of well-determined parameters γ =
  Σ λa/(λa + α) ([LIT-623](../literature.d/LIT-623.md)) and its NTK form in [THEORY-080](../theory.d/THEORY-080.md). The paper does not
  draw this connection. A reading that wanted to tie the evidence framework
  to random features would start here.
- **THEORY candidate (not filed):** "In proportional-limit ridge regression
  on random features, the double-descent peak is the divergence of the test
  error at the interpolation threshold, where the resolvent's
  self-consistent corrections pass from order 1/λ to order 1; it vanishes
  under a positive ridge and when test points lie within the ridge scale of
  the training points." Source this paper, with [LIT-683](../literature.d/LIT-683.md) for the linear
  case; promote when a second model's exact analysis (Mei and Montanari, or
  Hastie et al.) is read.
- **Anthology.** Belkin et al.'s double descent ([ANTH-LIT-297](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-297.md)) is the
  empirical phenomenon this paper explains for one model.

## Limitations

- **One shallow model.** A single random layer with cos and sin and a
  trained linear readout. The extension to deep networks is named as future
  work, through Fan and Wang's conjugate-kernel spectra.
- **λ > 0 throughout the theorems.** The ridgeless phases are derived as a
  limit of the λ > 0 results, and the paper warns that the λ = 10 "transition"
  in γσ is potentially misleading, because those quantities are not
  fixed-point solutions there.
- **Experiments are binary MNIST-like tasks** with n up to about 1,000.
- **The theorems give expectations over W** and almost-sure limits. The
  finite-size error is not bounded.

## Open questions

- Does the same structure, a self-consistent correction that changes order
  at a threshold, describe the double-descent peaks of trained deep
  networks, as Yang et al. ([LIT-663](../literature.d/LIT-663.md)) suggest empirically?
- How do the δ relate to the effective number of parameters of the
  evidence framework?

## Corrections

- none (there was no seed)
