---
number: 1906
status: Proposed
formerly:
- THEORY-tmpw4lo5
promote_when: >-
  Mallat's "Group Invariant Scattering" is read and gives, under the
  conditions stated here, the deformation bound ‖S_J L_τ x − S_J x‖ ≤
  C m_max ‖x‖ (2^−J ‖τ‖∞ + ‖∇τ‖∞), the contraction and the translation
  invariance below 2^J; the dependence of second-order coefficients on
  moments up to order four is checked; and the reported error rates (0.43%
  on MNIST with an SVM, 0.2% on CUReT with PCA) are reproduced with the
  authors' released software or an independent implementation.
title: 'Bruna and Mallat define a windowed scattering transform, a cascade of fixed wavelet convolutions, complex modulus and local averaging, which is contractive, translation invariant below the scale 2^J and Lipschitz-stable to small deformations, whose second-order coefficients depend on moments up to order four, and which with fixed filters gave 0.43% error on MNIST with an SVM and 0.2% on CUReT with a PCA classifier'
version: 1
tags:
- representation-learning
- mathematics
date: '2026-11-15'
source:
- LIT-2632
bears_on:
- QUESTION-058
summary: >-
  Bruna & Mallat (2013), [LIT-2632](../literature.d/LIT-2632.md), read in [NOTE-1957](../notes.d/NOTE-1957.md) from arXiv
  v2. The stability, contraction and energy theorems are stated here and
  proved in Mallat's "Group Invariant Scattering", unread, so they hold
  here only by citation. Bears on [QUESTION-058](../questions.d/QUESTION-058.md), invariance from
  architecture alone; and it is the contrast to [THEORY-758](THEORY-758.md), a linear
  multiscale decomposition giving covariance only. The wording is the
  reader's; adopting it is the owner's call.
---

# THEORY-1906: Bruna and Mallat define a windowed scattering transform, a cascade of fixed wavelet convolutions, complex modulus and local averaging, which is contractive, translation invariant below the scale 2^J and Lipschitz-stable to small deformations, whose second-order coefficients depend on moments up to order four, and which with fixed filters gave 0.43% error on MNIST with an SVM and 0.2% on CUReT with a PCA classifier

Bruna & Mallat (2013), [LIT-2632](../literature.d/LIT-2632.md); read in [NOTE-1957](../notes.d/NOTE-1957.md).

## The result

S_J[p]x = |||x ⋆ ψλ1| ⋆ ψλ2| … ⋆ ψλm| ⋆ φ_2J, along paths p of wavelet
indices, with Morlet wavelets satisfying a Littlewood–Paley bound. The
argument for the modulus is in the paper: a linear invariant of a wavelet
output is zero, and a non-linearity that commutes with deformations and is
L²-stable must be a modulus. The properties are stated with proofs cited
to [22]: contraction, ‖S_J x − S_J y‖ ≤ ‖x − y‖; energy conservation for a
unitary wavelet transform; and, for compactly supported signals,
‖S_J(L_τ x) − S_J x‖ ≤ C m_max ‖x‖ (2^−J ‖τ‖∞ + ‖∇τ‖∞). On Caltech-101
less than 1% of the energy lies beyond three layers. Second-order
coefficients depend on moments up to order four, so they separate
textures of equal power spectrum. Experimentally, with fixed filters,
second-order scattering gave 0.43% error on MNIST with a Gaussian SVM
(convolution network 0.53%), beat the convolution network below 5 · 10³
training samples with a PCA classifier, and gave 0.2% on CUReT. These
error rates could have come out worse than learned networks.

## What it does not show

- The theorems themselves: they are proved in Mallat's "Group Invariant
  Scattering", not read.
- That trained CNNs work this way: the paper's explanation of deep
  networks is by architectural analogy, not by analysis of trained
  filters.
- Anything beyond small benchmarks (MNIST, USPS, CUReT, and rotated or
  scaled MNIST).
- That multiscale linear coarse-graining is invariant: the paper's point is
  the reverse, which is why it bears on [THEORY-758](THEORY-758.md) as a contrast, not as
  support.
