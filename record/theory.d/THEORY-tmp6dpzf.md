---
status: Proposed
promote_when: >-
  A held derivation of the same divergence in a second random-feature
  model, by a different route: Mei and Montanari's random-features
  regression on Gaussian data, or Hastie et al.'s ridgeless asymptotics,
  read in the record and found to put the peak at the interpolation
  threshold as a ridgeless divergence that a positive ridge bounds. A
  line-by-line reading of Liao et al.'s Lemma 5 (det(Ω⁻¹) scales as λ)
  would also serve, since the record has followed that proof only in
  outline. The account is refuted by a random-feature model, inside the
  proportional regime and with test data not within the ridge scale of
  the training data, whose ridgeless test error stays bounded at the
  threshold, or whose peak sits away from the threshold, or survives a
  ridge of the size that minimizes the test error. More agreement between
  Liao et al.'s closed forms and MNIST-like data cannot settle it: that
  checks the formulas, not that the peak is the divergence.
title: 'In random-features ridge regression the double-descent peak is a divergence of the test error at the interpolation threshold 2N = n as the ridge goes to zero, which a positive ridge keeps finite and a ridge of the tuned size removes; minimum-norm linear regression has the same peak at n = d in exact finite-sample form'
version: 1
tags:
- learning-theory
- mathematics
- anthology-candidate
date: '2026-10-03'
source:
- LIT-tmpufwlh
- LIT-tmpzk7ci
summary: >-
  Liao, Couillet & Mahoney (2020), [LIT-tmpufwlh](../literature.d/LIT-tmpufwlh.md): for random Fourier
  features with n, p and N large together, the test MSE has a closed form
  through a deterministic equivalent of the resolvent. As λ → 0 its
  corrections jump from O(1) to order 1/λ across 2N = n, det(Ω⁻¹) scales
  as λ, and the test error diverges at 2N = n unless the test data lie
  within about λ of the training data. At λ = 10⁻⁷ and 10⁻³ the curve has
  a singular peak; at the tuned λ ≈ 0.2 and at 10 it has none. Dereziński,
  Liang & Mahoney (2019), [LIT-tmpzk7ci](../literature.d/LIT-tmpzk7ci.md): exact MSE of the minimum-norm
  estimator under a surrogate design, peaking at n = d with value
  σ² tr(Σ⁻¹), and below the threshold equal in expectation to ridge
  regression at the λn that makes the ridge effective dimension n.
  Proportional-limit theorems for one shallow model each; nothing here
  reaches trained deep networks.
---

# THEORY-tmp6dpzf: In random-features ridge regression the double-descent peak is a divergence of the test error at the interpolation threshold 2N = n as the ridge goes to zero, which a positive ridge keeps finite and a ridge of the tuned size removes; minimum-norm linear regression has the same peak at n = d in exact finite-sample form

## Source

- Liao, Couillet & Mahoney (2020), [LIT-tmpufwlh](../literature.d/LIT-tmpufwlh.md), read in [NOTE-tmp61xwr](../notes.d/NOTE-tmp61xwr.md):
  Theorems 1–3, Section 3.3 (Figure 7, Remarks 8–9), Section 4.1 (Lemma 5,
  Figures 8–9) and Section 4.2 (Figure 10).
- Dereziński, Liang & Mahoney (2019), [LIT-tmpzk7ci](../literature.d/LIT-tmpzk7ci.md), read in
  [NOTE-tmp55ipv](../notes.d/NOTE-tmp55ipv.md): Theorems 1–3 and Figure 1.

## The claim

**Random features: the peak is where the ridgeless test error diverges.**
Liao, Couillet and Mahoney ([LIT-tmpufwlh](../literature.d/LIT-tmpufwlh.md)) treat ridge regression on N
random Fourier features, cos(WX) and sin(WX), so 2N features in all, with
sample size n, input dimension p and N growing together. They show that
the expected resolvent of the feature Gram matrix has a deterministic
equivalent built from two data kernels and a pair of scalars δcos, δsin
that solve a fixed point (Theorem 1), and that training and test MSE
converge to closed forms built from it (Theorems 2–3). In the ridgeless
limit the system has two regimes. For 2N < n the δ grow as 1/λ; for
2N > n they stay O(1). At λ = 10⁻⁷ "the values of δcos and δsin 'jumps'"
across the threshold (Figure 6). The test error carries a 2 × 2 matrix Ω
whose determinant det(Ω⁻¹) scales as λ (Lemma 5). So when the test inputs
differ from the training inputs, Ē_test → ∞ as 2N → n with λ → 0
(Section 4.1). The training error stays at zero there, because a
prefactor λ² cancels the divergence. The double-descent peak is that
divergence. The paper's Remark 9 puts it in the words this claim uses:
double descent is "a natural consequence of the phase transition between
two qualitatively different phases of learning".

**A positive ridge keeps it finite; a tuned one removes it.** For any
fixed λ > 0 the theorems give a finite test error. Whether a peak is
still visible depends on the size of λ. On MNIST 3 against 7 with n = 500,
the test MSE has "a singularity at 2N = n" at λ = 10⁻⁷ and λ = 10⁻³, and
is smooth and monotonically decreasing in N at λ = 0.2 and λ = 10 (Figure
7). A grid search over λ finds λopt ≈ 0.2, and "for this choice of λ ...
no singular peak at 2N = n is observed" (Remark 8). At every fixed λ > 0
the minimum test error is at 2N > n, and the global optimum over N and λ
is a heavily over-parameterized model with non-vanishing λ.

**The divergence needs the test data to be away from the training data.**
If the test inputs are within the ridge scale of the training inputs, the
divergence cancels. With X̂ = X + σε at N = 512 and n = 1,024, the test
error equals the training error below σ² ≈ λ and grows linearly in σ²
above it (Section 4.2, Figure 10). The peak is a statement about
generalization to new points, not about fitting.

**Linear regression: the same threshold, in exact finite-sample form.**
Dereziński, Liang and Mahoney ([LIT-tmpzk7ci](../literature.d/LIT-tmpzk7ci.md)) give the exact MSE of the
minimum-norm estimator X⁺y for d features and n samples, under a
determinantal surrogate of the i.i.d. design (Theorem 1). Below the
threshold it is σ² tr((Σ + λnI)⁻¹)(1 − αn)/(d − n) plus a bias term; at
n = d it is σ² tr(Σ⁻¹); above, σ² tr(Σ⁻¹)(1 − e^{d−n})/(n − d). Their
Figure 1a shows the peak at n = d, matching i.i.d. Gaussian simulations.
At finite size the peak is finite. Reading Theorem 1 at n = 2d, the
variance there is σ² tr(Σ⁻¹)(1 − e^{−d})/d, so the peak is about d times
its value at twice the threshold, and it grows without bound as the
dimension does. That arithmetic is this account's, not the paper's.

**The implicit ridge of the minimum-norm solution.** Below the threshold,
the expected minimum-norm solution is the population ridge solution
(Σ + λnI)⁻¹E[y(x)x], at the λn for which the ridge effective dimension
tr(Σ(Σ + λnI)⁻¹) equals n (Theorem 2). This is the paper's statement of
implicit regularization: over-parameterization acts as a ridge whose
strength makes n the effective number of degrees of freedom. As n rises
to d, that equation forces λn down to 0, so the implicit ridge vanishes
exactly at the threshold where the peak sits. That last step follows from
the definition of λn; the paper does not draw it as an account of the
peak.

## What this does not say

- **It does not say the peak is a divergence at finite size.** In both
  papers the divergence is a statement about the proportional limit, or
  the ridgeless limit within it. Dereziński et al.'s finite-sample peak is
  σ² tr(Σ⁻¹), finite. Their Theorem 3, which ties the surrogate to the
  i.i.d. design, excludes n/d → 1, the peak itself.
- **It does not say any positive ridge removes the peak.** λ = 10⁻³ leaves
  a singular-looking peak in Liao et al.'s Figure 7. The ridge that removes
  it is of the size that minimizes the test error, problem-dependent, and
  0.2 in that experiment.
- **It does not say the two papers' mechanisms are one.** Liao et al.'s
  δ are corrections in a resolvent that blow up on the under-parameterized
  side; Dereziński et al.'s λn is an implicit ridge on the
  over-parameterized side. Both are fixed by a self-consistent trace
  equation, and Dereziński et al. thank Liao for the resolvent connection,
  but neither paper compares itself with the other.
- **It does not reach deep networks.** One random layer with a trained
  linear readout, and well-specified linear regression. Yang et al.
  ([LIT-tmpf3sak](../literature.d/LIT-tmpf3sak.md)) cite both papers for the double-descent band they see in
  ResNets trained on noisy labels, and claim only that their observation
  "corroborates" them.
- **It is checked on small tasks only.** Liao et al. need only
  concentrated random vectors, which is wider than Gaussian data, but
  their experiments are binary MNIST-like tasks with n up to about 1,000.

## Connections

- **The kernel regime.** Liao et al.'s N/n → ∞ limit is Gaussian kernel
  regression, whose test error is not zero and does not depend on λ
  (Remark 7). The record's kernel-regime account ([THEORY-086](THEORY-086.md)) works in
  that infinite-feature limit: Cao et al. ([LIT-624](../literature.d/LIT-624.md)) prove that gradient
  descent fits the target eigenspace by eigenspace of the NTK, Basri et al.
  ([LIT-612](../literature.d/LIT-612.md)) show the eigenspaces on spherical data are the harmonic
  degrees, and Bietti and Bach ([LIT-608](../literature.d/LIT-608.md)) show the ReLU NTK's eigenvalues
  decay as k^(−d) at every depth. This account is the finite-ratio side
  those results do not have. While N/n is finite the kernel prediction is
  biased, and Liao et al.'s Figure 4 shows it missing the training error
  badly for N/n < 1. No relation is declared: the two accounts
  are about different limits, and neither builds on the other.
- **MacKay's γ.** The agent who filed Dereziński et al. identified the
  equation n = tr(Σ(Σ + λnI)⁻¹) with MacKay's number of well-determined
  parameters, γ = Σ λa/(λa + α) ([LIT-623](../literature.d/LIT-623.md)), with the population covariance
  in place of the data Hessian. The identification is that agent's, in the
  LIT's standing and the NOTE, not the paper's, and it is not part of this
  claim. [NOTE-tmp55ipv](../notes.d/NOTE-tmp55ipv.md) records that MacKay's evidence maximum sets α by a
  different condition, so the two regularizers differ in general.
- **Anthology.** The double-descent curve itself is held there as Belkin
  et al. ([ANTH-LIT-297](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-297.md)), the empirical signature that Liao et al. cite and
  explain for one model.
