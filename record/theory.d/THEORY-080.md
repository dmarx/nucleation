---
number: 80
status: Proposed
formerly:
- THEORY-tmp84ynr
promote_when: >-
  A held source and a computation. The source would state the Bayesian
  evidence of a linearised network, or of a Gaussian process with the NTK
  as covariance, in the kernel's eigenbasis. The record holds no such
  paper, and each step here is assembled from sources about other things.
  The computation would take a wide fully connected ReLU network on
  uniform data on S^(d−1), linearise it at initialisation, and evaluate the
  log-determinant term of its evidence over a range of n. It would check
  that this term matches Σ_k N(d, k)·½ log(1 + βnµ_k/α) up to the error of
  approximating the Gram spectrum by nµ_k. It would also check that the
  effective number of parameters γ grows about as n^((d−1)/d). The account
  is refuted if the log-determinant departs from the per-degree sum by more
  than that approximation error, or if γ grows at a clearly different
  rate. Evidence computed for networks outside the kernel regime cannot
  settle it, since the account is about the linearised model.
title: "In a linearised network with a Gaussian prior on its parameters, the Occam factor is a sum over the NTK's eigenvalues, so on spherical data each harmonic pays ½ log(1 + βnµ_k/α) and the kernel's eigenvalue decay schedules the complexity penalty across frequencies"
version: 1
tags:
- model-comparison
- information-geometry
- learning-theory
- anthology-candidate
date: '2026-10-03'
source:
- LIT-623
- LIT-608
- LIT-612
summary: >-
  The filer's synthesis, stated by no source. A network linearised at
  initialisation, with an isotropic Gaussian prior on its parameters and
  Gaussian noise, is MacKay's linear-in-parameters model ([LIT-623](../literature.d/LIT-623.md)).
  Its Occam factor is −½ Σ log(1 + βλ_a/α) over the eigenvalues of JᵀJ.
  These are the empirical NTK's, which on uniform spherical data form
  Bietti & Bach's degree blocks, nµ_k with multiplicity N(d, k)
  ([LIT-608](../literature.d/LIT-608.md)). Degrees whose βnµ_k exceeds α pay about ½ log n per
  harmonic, and degrees below pay almost nothing. With µ_k ~ k^(−d), the
  number of paid directions γ grows as n^((d−1)/d), not as the parameter
  count. Basri et al.'s bound ([LIT-612](../literature.d/LIT-612.md), Eq. 14) is the matching
  data-fit term. The kernel's decay exponent is the schedule of the
  penalty.
---
<!-- inactive-ok-file: THEORY-087 THEORY-084 — Proposed; THEORY-087 is extended in its regular half, which is derived, and THEORY-084 is named in Connections -->

# THEORY-080: In a linearised network with a Gaussian prior on its parameters, the Occam factor is a sum over the NTK's eigenvalues, so on spherical data each harmonic pays ½ log(1 + βnµ_k/α) and the kernel's eigenvalue decay schedules the complexity penalty across frequencies

## Source

- MacKay (1992), [LIT-623](../literature.d/LIT-623.md), read in [NOTE-471](../notes.d/NOTE-471.md): the linear model
  and quadratic regulariser (Eqs. 7–11), the log evidence (Eq. 20) and γ
  (Eq. 23).
- Bietti & Bach (2021), [LIT-608](../literature.d/LIT-608.md), read in [NOTE-475](../notes.d/NOTE-475.md): the Mercer
  decomposition on the sphere (Eqs. 8–9) and Corollary 3.
- Basri et al. (2019), [LIT-612](../literature.d/LIT-612.md), read in [NOTE-481](../notes.d/NOTE-481.md): the
  generalisation bound, Eq. 14.

## The derivation

**The model.** Linearise a network at θ0, f(x; θ) ≈ f(x; θ0) + J(x)(θ − θ0).
Put a Gaussian prior of precision α on θ − θ0, and let the targets carry
Gaussian noise of precision β. This is exactly MacKay's interpolation
model. It is linear in its parameters, with a quadratic regulariser
E_W = ½|θ − θ0|² and a quadratic misfit ([LIT-623](../literature.d/LIT-623.md), Eqs. 7–11). The
basis functions are the components of the gradient J(x). For such models
MacKay's Gaussian evidence is exact, not an approximation.

**The Occam factor.** MacKay's log evidence (Eq. 20) contains
−½ log det A − log Z_W(α) + (k/2) log 2π, with A = αI + βJᵀJ. Since
Z_W = (2π/α)^{k/2}, these terms add up to −½ log det(I + (β/α)JᵀJ), which
is −½ Σ_a log(1 + βλ_a/α) over the eigenvalues λ_a of JᵀJ. Together with
−αE_W at the most probable parameters, this is the log Occam factor.
Directions with λ_a = 0 cost nothing. The number of well-determined
parameters is γ = Σ_a βλ_a/(βλ_a + α) (Eq. 23). The non-zero eigenvalues
of JᵀJ are those of the empirical NTK Gram matrix JJᵀ, so the Occam factor
is a function of the NTK spectrum alone. At most n directions are priced,
however many parameters the network has.

**On the sphere.** In the kernel regime on uniform data on S^(d−1), the
Gram eigenvalues are close to nµ_k with multiplicity N(d, k) ~ k^(d−2), and
µ_k ~ k^(−d) for ReLU networks of any depth ([LIT-608](../literature.d/LIT-608.md), Eq. 8 and
Corollary 3; [THEORY-086](THEORY-086.md)). So the log Occam factor is about
−Σ_k N(d, k)·½ log(1 + βnµ_k/α). Each harmonic of degree k pays
½ log(1 + βnµ_k/α). Degrees with βnµ_k ≫ α pay about ½ log n each, the
BIC rate. Degrees with βnµ_k ≪ α pay almost nothing and are not
determined. The crossover degree K satisfies βnµ_K ≈ α, so K grows as
n^(1/d), and γ ≈ Σ_{k<K} N(d, k) grows as K^(d−1), that is, as
n^((d−1)/d). These rates are the filer's, from the asymptotic forms, and
ignore the parity-dependent constants.

**The data-fit term.** Integrating out θ makes y Gaussian with covariance
α⁻¹K + β⁻¹I, where K is the Gram matrix. The quadratic form in the
resulting log evidence is, at small noise, α·yᵀK⁻¹y. In the harmonic basis
that is α Σ a²_{k,j}/µ_k, which is α times Bietti & Bach's RKHS norm
(Eq. 9). It is also the quadratic form in Basri et al.'s generalisation
bound, √(2yᵀ(H∞)⁻¹y/n) ([LIT-612](../literature.d/LIT-612.md), Eq. 14), which for a band-limited
target on the circle weights frequency k by k². The kernel charges high
frequencies twice: once in the fit, through 1/µ_k, and once in the Occam
factor, through which degrees are determined at all.

## What this does not say

- **It is about the linearised model.** The network itself may be
  singular, in which case its evidence is governed by an RLCT
  ([THEORY-087](THEORY-087.md)). Linearisation removes that question rather than
  answering it.
- **The kernel here is the NTK, as a prior on the parameter displacement.**
  It is not the random-feature (NNGP) kernel that a Bayesian network with
  Gaussian weights converges to at infinite width. That is a different
  prior with a faster decay, k^(−d−2) ([LIT-608](../literature.d/LIT-608.md), Corollary 2), and the
  record holds no source for the convergence.
- **It does not say the evidence picks good networks.** MacKay's own §6
  lists five reasons evidence and test error can disagree.
- **No source states it.** MacKay knows nothing of tangent kernels. Bietti
  & Bach and Basri et al. say nothing of priors or evidence. Every step is
  checkable, but the whole is assembled.

## Connections

- **Extends [THEORY-087](THEORY-087.md)** in its regular half. There the penalty is
  set by curvature and reaches (d/2) log n when every direction is well
  determined. Here the curvature is the NTK spectrum. When the parameters
  far outnumber the samples, the right count is γ, which grows as
  n^((d−1)/d), not d/2.
- **Gradient descent is the same filter.** This observation is the
  filer's. The posterior mean shrinks the least-squares coefficient along
  eigendirection a by βλ_a/(βλ_a + α). After T steps of gradient descent
  that coefficient has been fitted to 1 − (1 − ηλ_a)^T ([THEORY-086](THEORY-086.md)).
  Both pass directions above a cut-off, α/β for one and about 1/(ηT) for
  the other. This is the precise form of MacKay's weakly supported remark
  that early stopping resembles stronger regularisation ([LIT-623](../literature.d/LIT-623.md),
  §6).
- **[THEORY-084](THEORY-084.md)** reads the same spectrum as the Fisher and asks where
  a hard threshold on it is well posed. The Occam factor needs no
  threshold, since it prices every direction smoothly.
