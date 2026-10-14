---
number: 297
status: Proposed
formerly:
- THEORY-tmp11baf
promote_when: >-
  An independent statement and proof of Theorem 5.1 and of the
  eigenspace-preservation consequence for smooth manifolds, with the
  conditions under which the truncated matrix C_{n×n} of an exact isometry
  stays orthogonal (a spectral gap at n). It is refuted by a
  volume-preserving bijection whose functional matrix in orthonormal bases
  is not orthogonal, or an isometry whose matrix mixes eigenspaces with
  different eigenvalues. What cannot settle it: shape-matching benchmark
  results, which test the method, not the theorem.
title: "A bijection between shapes is equivalent to the linear operator it induces on functions; in orthonormal bases a volume-preserving bijection's matrix is orthogonal, and an isometry's commutes with the Laplace–Beltrami operator, so it maps each eigenspace to the matching eigenspace"
version: 1
tags:
- mathematics
date: '2026-10-14'
source:
- LIT-993
summary: >-
  Ovsjanikov, Ben-Chen, Solomon, Butscher & Guibas (2012), [LIT-993](../literature.d/LIT-993.md),
  Remarks 4.1–4.3, Theorem 5.1 with App. A, and §5.1, read in
  [NOTE-822](../notes.d/NOTE-822.md). Orthogonality was checked; commutation with the
  Laplacian is cited as well known. All of it assumes a bijection. The
  operator runs between two different spaces, but the paper gives no
  structure for a non-invertible or one-way map, and the stability of
  truncated eigenspaces is cited to Kato, not shown.
---
<!-- inactive-ok-file: THEORY-009 THEORY-239 — Proposed; accounts this one sits beside, open -->

# THEORY-297: A bijection between shapes is equivalent to the linear operator it induces on functions; in orthonormal bases a volume-preserving bijection's matrix is orthogonal, and an isometry's commutes with the Laplace–Beltrami operator, so it maps each eigenspace to the matching eigenspace

## Source

Ovsjanikov, Ben-Chen, Solomon, Butscher & Guibas (2012), [LIT-993](../literature.d/LIT-993.md),
Remarks 4.1–4.3, Theorem 5.1 and its proof (App. A), and §5.1, as read in
[NOTE-822](../notes.d/NOTE-822.md).

## What was actually shown

**Equivalence.** A bijection T: M → N induces T_F(f) = f∘T⁻¹, which is
linear, and T is recovered from T_F because indicator functions go to
indicator functions (Remarks 4.1–4.2). In bases, T_F is a matrix C
(Remark 4.3).

**Orthogonality (Theorem 5.1(1), checked).** If T preserves volume, the
integral defining C_ij and the one defining the matrix D of T⁻¹ have the
same integrand after a change of variables, so C = Dᵀ. Since CD = I, C is
orthogonal and T⁻¹ is represented by Cᵀ. The same holds when the discrete
bases are orthonormal in the standard inner product.

**Eigenspaces (Theorem 5.1(2) and §5.1).** An isometry commutes with the
Laplace–Beltrami operator, so C_ij ≠ 0 only between eigenfunctions of the
same eigenvalue; C is block-diagonal, and diagonal if no eigenvalue
repeats. The individual eigenvectors are not preserved (signs and bases
within a repeated eigenvalue can change); the eigenspaces are.

What could have failed: the orthogonality argument needs only the volume
condition; a volume-changing bijection gives a non-orthogonal C, which is
why the paper uses an unweighted Laplacian where it helps compactness.

## What this does not say

- **Nothing about maps that are not bijections.** The operator runs
  between two spaces, but every structural result assumes T is
  invertible. Inverting a truncated matrix for a non-bijective map is a
  numerical step without guarantee.
- **Not that truncation is stable.** That the span of the first n
  eigenfunctions survives a near-isometry is cited to Kato (1995), with a
  gap between the nth and (n + 1)st eigenvalues; it is not shown.
- **Not which matrices come from point maps.** The paper calls that "a
  difficult open problem" (§5.5).
- **Not that near-isometries are nearly diagonal in general.** The 94%
  sparsity is measured on TOSCA cats, and the paper says C stops being
  diagonal quickly under non-isometric deformation.

## Connections

- [QUESTION-052](../questions.d/QUESTION-052.md) asks for a signature stable under a kind's admissible
  transformations. For isometries, this gives one: the Laplacian
  eigenspaces, as spaces, not as bases, which is [CLAIM-164](../claims.d/CLAIM-164.md)'s point. It
  gives nothing for the directed case the question asks about, so it is
  not filed as an answer.
- [THEORY-239](THEORY-239.md) obtains singular functions of an operator between two
  spaces from a joint law. Functional maps are another operator between
  two spaces, whose structure comes from a bijection and an intrinsic
  Laplacian, not from a pair distribution.
- [THEORY-009](THEORY-009.md) says self-adjointness in spectral self-supervised learning
  comes from a symmetric pair distribution. Here the analogue of symmetry
  is volume preservation, which makes the inverse the adjoint.
