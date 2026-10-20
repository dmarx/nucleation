---
number: 394
status: Active
formerly:
- CLAIM-tmpho867
title: 'In a stationary linear Gaussian VAR(1) that is time-reversible (AΠ = ΠAᵀ, Π the stationary covariance), every slow-feature direction is a left eigenvector of A, so any span of slow features is an exactly dynamically independent coarse-graining; off reversibility a slow feature is in general neither independent nor free of memory'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation: a stable VAR(1) with AΠ = ΠAᵀ and a
  solution w of the slow-feature generalized eigenproblem
  ½(AΠ + ΠAᵀ)w = μΠw, with distinct μ, for which Aᵀw is not a multiple
  of w.
tags:
- complex-systems
- representation-learning
- mathematics
date: '2026-10-20'
line:
- distributed-agency
- formal-apparatus
answers:
- QUESTION-217
grounds:
- THEORY-733
- THEORY-746
- LIT-1296
summary: >-
  Derived in the reading of Schüler and Wiskott (2025), [NOTE-1015](../notes.d/NOTE-1015.md),
  and re-checked here. It says when slowness, the criterion of slow
  feature analysis ([THEORY-746](../theory.d/THEORY-746.md)), picks out a closed coarse-graining in
  [THEORY-733](../theory.d/THEORY-733.md)'s sense: always in the reversible linear Gaussian VAR(1),
  which is the class of noise-free square mixtures of independent AR(1)
  processes, and not in general otherwise. Linear features, linear
  Gaussian dynamics, lag one.
---
<!-- inactive-ok-file: NOTE-1015 — new reading, cited as where the result was derived -->

# CLAIM-394: In a stationary linear Gaussian VAR(1) that is time-reversible (AΠ = ΠAᵀ, Π the stationary covariance), every slow-feature direction is a left eigenvector of A, so any span of slow features is an exactly dynamically independent coarse-graining; off reversibility a slow feature is in general neither independent nor free of memory

## The claim

Take X_t = AX_{t−1} + ε_t, stable, with stationary covariance Π and
lag-one covariance Cov(X_t, X_{t−1}) = AΠ. Linear slow feature analysis
minimizes E(wᵀX_t − wᵀX_{t−1})² at unit variance wᵀΠw = 1, which is
2(1 − wᵀAΠw). Its directions solve the generalized eigenproblem
½(AΠ + ΠAᵀ)w = μΠw, slowest first by largest μ.

**Reversible case.** If AΠ = ΠAᵀ, the symmetrization is AΠ itself, so
AΠw = μΠw. Substituting ΠAᵀ for AΠ gives ΠAᵀw = μΠw, and since Π ≻ 0,
Aᵀw = μw: w is a left eigenvector of A. A span L of such directions then
satisfies LA = BL with B diagonal, which is [THEORY-733](../theory.d/THEORY-733.md)'s condition for
exact dynamical independence. By [CLAIM-389](CLAIM-389.md) it then also has no
Mori–Zwanzig memory.

**Off reversibility.** The symmetrization differs from AΠ and the step
fails. In a random irreversible 4-dimensional example the largest
residual ‖wᵀA − (wᵀAw/wᵀw)wᵀ‖/‖w‖ was 0.71. In a reversible one built as
A = Π^{1/2}SΠ^{−1/2} with S symmetric, it was 8 × 10⁻¹⁶, and
‖AΠ − ΠAᵀ‖ was 1 × 10⁻¹⁴. The reader of Schüler and Wiskott found the
same contrast (0.26 against 0.0015 in their examples).

The reversible stationary Gaussian VAR(1)s are exactly the noise-free
square mixtures of independent AR(1)s: A = Π^{1/2}SΠ^{−1/2} with S
symmetric diagonalizes as a mixing of independent AR(1)s with S's
eigenvalues as coefficients. In that class the reader also found that
maximum likelihood recovers the slow-feature directions exactly, with no
limit taken ([NOTE-1015](../notes.d/NOTE-1015.md)).

## What it does not say

- **Not for Markov chains as stated.** There a slow eigenfunction closes
  only in conditional mean; closing the whole law needs eigenvectors
  constant on the blocks, that is strong lumpability ([THEORY-tmpz4ja2](../theory.d/THEORY-tmpz4ja2.md)).
  Slowness then gives metastability, not exact closure.
- **Not that slowness finds closure in general.** In irreversible
  linear dynamics, in nonlinear dynamics, or at lags above one, a slow
  feature can be dynamically dependent and carry memory.
- **Not that every closed coarse-graining is slow.** Any span of left
  eigenvectors is closed. Slowness picks one order among them.
- **Not that the features are individually identified.** With repeated
  μ only the eigenspace is fixed.
- **Not a reading of Turner and Sahani** ([LIT-1287](../literature.d/LIT-1287.md), Unavailable),
  though its noise-free mixing model is of their kind.
