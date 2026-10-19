---
number: 297
status: Active
formerly:
- THEORY-tmp11baf
title: "A bijection between shapes is equivalent, up to null sets, to the linear operator it induces on functions; in orthonormal bases a volume-preserving bijection's matrix is orthogonal, and an isometry's commutes with the Laplace–Beltrami operator, so it maps each eigenspace to the matching eigenspace"
version: 2
history:
- version: 2
  date: '2026-10-19'
  note: >-
    Narrowed and promoted from Proposed to Active at the owner's direction,
    carrying out the promotion audit's decision
    (record/promotion-audit/decisions/THEORY-297.yaml, batch 007, ADR-047).
    The promote_when's first clause asked for an independent statement and
    proof of Theorem 5.1 and of eigenspace preservation. The record does
    not hold a second source. The owner ruled on 2026-10-19 that a checked
    step-by-step re-derivation recorded in the decision file meets such a
    clause, and the three statements were re-derived there by change of
    variables and the metric naturality of the Laplacian. The note of
    2026-10-19 below gives them. "Equivalent" now carries "up to null sets",
    which a merely measurable bijection needs. The clause on truncation and
    near-isometries, which the THEORY already disclaimed, moves unchanged to
    QUESTION-138, and the promote_when is removed.
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

# THEORY-297: A bijection between shapes is equivalent, up to null sets, to the linear operator it induces on functions; in orthonormal bases a volume-preserving bijection's matrix is orthogonal, and an isometry's commutes with the Laplace–Beltrami operator, so it maps each eigenspace to the matching eigenspace

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
  gap between the nth and (n + 1)st eigenvalues; it is not shown. When the
  truncated block of an exact or near isometry stays orthogonal is
  [QUESTION-138](../questions.d/QUESTION-138.md).
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

## Note of 2026-10-19: the three statements, re-derived

For a measurable bijection T: M → N between compact Riemannian manifolds,
with T_F(f) = f∘T⁻¹:

1. **Equivalence.** T_F is linear and sends 1_A to 1_(T(A)), so it fixes
   T(A) for every measurable A, and with it T up to null sets. If T is
   continuous, it fixes T pointwise.
2. **Orthogonality.** If T preserves volume, change of variables gives
   ‖f∘T⁻¹‖²_N = ∫_N |f(T⁻¹y)|² dy = ∫_M |f|² dx, so T_F is unitary from
   L²(M) to L²(N). In orthonormal bases its matrix C satisfies CᵀC = I, and
   its inverse is the matrix D of T⁻¹, so C = Dᵀ. That is Theorem 5.1(1),
   which [NOTE-822](../notes.d/NOTE-822.md) checked.
3. **Eigenspaces.** A Riemannian isometry pulls back the metric, and the
   Laplace–Beltrami operator is built from the metric alone, so
   Δ_N(f∘T⁻¹) = (Δ_M f)∘T⁻¹. So T_F maps the λ-eigenspace of M onto the
   λ-eigenspace of N, and C_ij = 0 whenever λ_i ≠ λ_j, since eigenspaces of
   distinct eigenvalues are orthogonal. The paper cites this as well known.
   It is the naturality of the Laplacian under isometries.

For an exact isometry the truncation question is easy when n ends at a
spectral gap. C is block-diagonal by eigenspace, so its leading n × n block
is a direct sum of orthogonal blocks. The open part is the near-isometric
case, which is [QUESTION-138](../questions.d/QUESTION-138.md).
