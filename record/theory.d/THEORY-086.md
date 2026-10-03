---
number: 86
status: Active
formerly:
- THEORY-tmpo9r23
title: 'In the kernel regime gradient descent fits the target eigenspace by eigenspace of the neural tangent kernel, at rates set by their eigenvalues; on uniform spherical data the eigenspaces are the harmonic degrees, and for fully connected ReLU networks the non-zero eigenvalues decay as k^(−d) at every depth'
version: 1
tags:
- learning-theory
- representation-learning
- mathematics
- anthology-candidate
date: '2026-10-03'
source:
- LIT-624
- LIT-612
- LIT-608
summary: >-
  Three derived results that compose. Cao et al. (2019), [LIT-624](../literature.d/LIT-624.md),
  Theorem 4.2: for a wide two-layer ReLU network, the training residual's
  component in the top-r_k NTK eigenspace falls as (1 − λ_{r_k})^T, for
  any target. Basri et al. (2019), [LIT-612](../literature.d/LIT-612.md): on uniform spherical data
  the Gram matrix is a convolution, so its eigenvectors are harmonics,
  with closed-form eigenvalues per frequency. The bias-free kernel is zero
  on odd frequencies k ≥ 3, and a bias restores them. Bietti & Bach (2021),
  [LIT-608](../literature.d/LIT-608.md), Corollary 3: the L-layer ReLU NTK decays as k^(−d) on
  S^(d−1), the same exponent at every depth. Active for the kernel regime
  on uniform spherical data, where every step is proved. It says nothing
  about networks whose kernel moves.
extended_by:
- THEORY-084
---
<!-- inactive-ok-file: THEORY-019 THEORY-084 THEORY-080 — Proposed; named in Connections, nothing here rests on them -->

# THEORY-086: In the kernel regime gradient descent fits the target eigenspace by eigenspace of the neural tangent kernel, at rates set by their eigenvalues; on uniform spherical data the eigenspaces are the harmonic degrees, and for fully connected ReLU networks the non-zero eigenvalues decay as k^(−d) at every depth

## Source

- Cao, Fang, Wu, Zhou & Gu (2019; IJCAI 2021), [LIT-624](../literature.d/LIT-624.md), read in
  [NOTE-483](../notes.d/NOTE-483.md): Lemma 4.1, Theorems 4.2–4.3, Corollaries 4.6–4.7, §5 and
  Appendix F.
- Basri, Jacobs, Kasten & Kritchman (2019), [LIT-612](../literature.d/LIT-612.md), read in
  [NOTE-481](../notes.d/NOTE-481.md): Theorems 1–4, Eqs. 5 and 11–13, Figures 4, 6 and 7.
- Bietti & Bach (2021), [LIT-608](../literature.d/LIT-608.md), read in [NOTE-475](../notes.d/NOTE-475.md): Eqs. 8–9,
  Theorem 1, Corollaries 2–3, §3.3.

## The claim, assembled

**Eigenspace by eigenspace.** In the linearised dynamics of a wide
network trained by gradient descent on squared loss, the residual along
each eigenvector of the Gram matrix decays as (1 − ηλ_i)^t ([LIT-612](../literature.d/LIT-612.md),
Eq. 5, from Arora et al.). So an eigenvalue is a learning rate. Cao et al.
prove a finite-width version for a two-layer ReLU network with both
layers trained ([LIT-624](../literature.d/LIT-624.md), Theorem 4.2). The residual's component in
the span of the first r_k eigenfunctions of the NTK integral operator
satisfies n^(−1/2)‖V_{r_k}ᵀ(y − ŷ(T))‖ ≤ 2(1 − λ_{r_k})^T n^(−1/2)‖V_{r_k}ᵀ y‖ + ε.
This holds once n ≥ Ω̃(ε^(−2) max{(λ_{r_k} − λ_{r_k+1})^(−2), M⁴r_k²}) and
the width is polynomial in T, λ_{r_k}^(−1) and ε^(−1). It assumes nothing
about the target. Here r_k counts the multiplicities of the first k
distinct eigenvalues, so the theorem is stated only for whole eigenspaces.
Larger eigenvalues are fitted faster, with fewer samples and narrower
networks.

**The eigenspaces are the harmonic degrees.** On uniform data on the
sphere, a kernel that depends only on xᵀx′ commutes with rotations. Basri
et al. show that the Gram matrix is then a convolution, and Funk–Hecke
makes its eigenvectors the spherical harmonics ([LIT-612](../literature.d/LIT-612.md), Theorems 1
and 3). Bietti & Bach state the Mercer form. Every harmonic of degree k
shares one eigenvalue µ_k, and there are N(d, k) of them, growing as
k^(d−2) on S^(d−1) ([LIT-608](../literature.d/LIT-608.md), Eq. 8). The RKHS is the set of functions
whose coefficients satisfy Σ a²_{k,j}/µ_k < ∞ (Eq. 9).

**The decay is set by architecture, not depth.** Bietti & Bach's
Theorem 1 reads the decay of µ_k off the kernel's expansion at t = ±1. A
non-integer exponent ν there gives µ_k ~ k^(−d−2ν+1). The ReLU arc-cosine
kernels have ν = 1/2 and 3/2, and composing them keeps these exponents.
So the L-layer ReLU NTK decays as k^(−d) for every L ≥ 3 (Corollary 3).
Its constant depends on the parity of k and grows with L. Two-layer
kernels have the same exponent.

**The one exception is a structural zero.** The bias-free two-layer ReLU
NTK has µ_k = 0 for every odd k ≥ 3. A single unit max(wᵀx, 0) is ½wᵀx
plus an even function, so it has no odd harmonic above degree 1
([LIT-612](../literature.d/LIT-612.md), Theorems 2 and 4; [LIT-624](../literature.d/LIT-624.md), Theorem 4.3). A
zero-initialised bias restores every frequency ([LIT-612](../literature.d/LIT-612.md), Eq. 13).
For L ≥ 3 both parities are non-zero ([LIT-608](../literature.d/LIT-608.md), Corollary 3).

**Conventions.** Bietti & Bach's d is the ambient dimension, inputs on
S^(d−1). Cao et al. and Basri et al. write S^d, where the same decay reads
k^(−d−1). On the circle (d = 2 here) Basri et al.'s closed form falls as
1/k², and on S² as about k^(−3). Their measured learning times in real
5-layer and 10-layer residual networks grow as k^1.94 and k^2.11 on the
circle and k^3.13 on S² (Figures 6–7). This is a check outside the
theorems, consistent with them.

## What this does not say

- **It does not reach outside the kernel regime.** Every result is about
  linearised dynamics or infinite-width kernels, and the authors say so.
  Nanda et al.'s modular-addition network ([LIT-345](../literature.d/LIT-345.md)) ends up using a few
  mid-range Fourier frequencies under weight decay and long training. Its
  kernel moved.
- **"First" means faster, not one at a time.** All eigenspaces are fitted
  at once, each at its own rate. The order is by eigenvalue, not by degree.
  Because the constants differ by parity, the two can disagree.
- **It does not say depth is useless.** It says depth buys no
  approximation power in this regime for fully connected ReLU networks.
  Bietti & Bach read it as a limit of the kernel view. Convolutional
  kernels are open.
- **It is for uniform data on the sphere.** A different input density
  changes the eigenbasis. Cao et al.'s experiments on three non-uniform
  distributions keep the ordering, but no theorem covers them.
- **Fitting is not generalising.** In Cao et al.'s Appendix F, the
  degree-4 component of the training residual falls while its test
  counterpart does not.
- **The eigengap condition is sufficient, not shown necessary.**

## Connections

- **[THEORY-019](THEORY-019.md).** The degree blocks are the case that account describes,
  an operator commuting with a group whose eigenspaces are built from its
  irreducibles. Here the group is the rotation group and the multiplicities
  are N(d, k). O'Donnell's hypercube ([LIT-346](../literature.d/LIT-346.md)) is the discrete twin. No
  relation is declared, since this account does not build on that one.
- **[THEORY-084](THEORY-084.md)** extends this account to the Fisher of the same
  networks and to spectral thresholds.
- **[THEORY-080](THEORY-080.md)** reads the same spectrum as a prior and computes the
  Occam factor it implies.
