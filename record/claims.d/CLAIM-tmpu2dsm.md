---
status: Active
title: 'For a symmetric positive-pair distribution with marginal p, the conditional-expectation operator on L²(p) has the density ratio K⁺ as its kernel, and it is Hilbert–Schmidt exactly when the χ²-divergence of the pair from the product of its marginals is finite, in which case it is compact and self-adjoint with an orthonormal eigenbasis'
version: 1
history:
- version: 1
  date: '2026-10-19'
  note: >-
    Split from THEORY-005 and filed Active at the owner's direction, from
    the second pass of the owner's promotion audit of 2026-10-19.
    THEORY-005 is a reading, and its operator identity with the finite-χ²
    condition is, by its own account, "the record's own": no source it
    holds states it. A record-own result belongs in a CLAIM (ADR-032).
    The proof is self-contained, so it does not wait on THEORY-005's
    promote_when, which asks for a published statement and stays as it
    is. THEORY-005 keeps its reading of the sources, and what
    trained features do.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the proof below: a symmetric positive-pair distribution on a
  standard Borel space for which the conditional-expectation operator is
  Hilbert–Schmidt while the χ²-divergence is infinite, or the reverse, or
  for which the operator fails to be self-adjoint or to have K⁺ as its
  kernel.
tags:
- mathematics
- representation-learning
- information-theory
date: '2026-10-19'
line: formal-apparatus
grounds:
- LIT-258
- LIT-249
summary: >-
  [THEORY-005](../theory.d/THEORY-005.md)'s derivation, stated as the record's own and with its proof.
  Johnson et al. ([LIT-258](../literature.d/LIT-258.md)) write the operator on a finite space without an
  integrability condition. HaoChen et al. ([LIT-249](../literature.d/LIT-249.md)) reach the Hilbert–
  Schmidt property from a uniform bound, which is stronger. Here the
  condition is exact: Hilbert–Schmidt if and only if finite χ². It says
  nothing about what trained features span.
---
<!-- inactive-ok-file: THEORY-005 THEORY-001 — Proposed; the reading this was split from, and the InfoNCE account, cited as open, not leaned on -->

# CLAIM-tmpu2dsm: For a symmetric positive-pair distribution with marginal p, the conditional-expectation operator on L²(p) has the density ratio K⁺ as its kernel, and it is Hilbert–Schmidt exactly when the χ²-divergence of the pair from the product of its marginals is finite, in which case it is compact and self-adjoint with an orthonormal eigenbasis

## The claim

Let (A, A′) take values in a standard Borel space X, with joint
distribution P⁺ symmetric under exchange of the two views and marginal p.
Define T on L²(p) by (Tf)(a) = E[f(A′) | A = a].

1. **Kernel.** If P⁺ ≪ p⊗p, with density K⁺ = dP⁺/d(p⊗p), then
   (Tf)(a) = ∫ K⁺(a, b) f(b) p(db).
2. **The exact condition.** T is Hilbert–Schmidt if and only if P⁺ ≪ p⊗p
   and χ²(P⁺‖p⊗p) < ∞, and then ‖T‖²_HS = ∫∫ K⁺² d(p⊗p) = 1 + χ²(P⁺‖p⊗p).
3. **Spectrum.** T is self-adjoint and a contraction. When it is
   Hilbert–Schmidt it is compact, so L²(p) has an orthonormal basis of
   eigenfunctions of T together with its kernel. The eigenvalues are real,
   lie in [−1, 1] and accumulate only at 0, and the constants are an
   eigenfunction with eigenvalue 1.

## Proof

(1) For bounded g, E[g(A)f(A′)] = ∫∫ g(a)f(b)K⁺(a,b) p(da)p(db), and this
identifies the conditional expectation as the stated integral.

(2) Hilbert–Schmidt operators on L²(p) are exactly the integral operators
with a kernel in L²(p⊗p). If K⁺ ∈ L²(p⊗p), then (1) shows that T is one.
Conversely, let T be Hilbert–Schmidt with kernel k. For measurable E and
F, P⁺(E × F) = ⟨1_E, T1_F⟩ = ∫∫ 1_E(a)1_F(b)k(a,b) p(da)p(db). Measures that
agree on rectangles agree, so P⁺ = k·(p⊗p) and k = K⁺. In both directions,
∫∫ K⁺² d(p⊗p) = ∫ (dP⁺/d(p⊗p))² d(p⊗p) = 1 + χ²(P⁺‖p⊗p), by the
definition of χ².

(3) ⟨g, Tf⟩ = E[g(A)f(A′)], which is symmetric in f and g because P⁺ is.
By Jensen, (Tf)² ≤ T(f²), so ‖Tf‖² ≤ E[f(A′)²] = ‖f‖²; T1 = 1. A compact
self-adjoint operator has the stated spectral decomposition (the spectral
theorem).

## What it does not say

- **That trained features span T's top eigenfunctions.** That is about
  optimization and capacity. [THEORY-005](../theory.d/THEORY-005.md)'s promote_when keeps it.
- **That InfoNCE features are eigenfunctions.** InfoNCE fits log K⁺, not
  K⁺ ([THEORY-001](../theory.d/THEORY-001.md)).
- **Anything when χ² is infinite**, for instance when two views of a
  continuous input are nearly deterministic functions of each other. Then
  T need not be compact. In the limit A′ = A, T is the identity.
- **That a source states it.** Johnson et al. ([LIT-258](../literature.d/LIT-258.md), App. E.2) write
  (1) on a finite space, where (2) is automatic. HaoChen et al. ([LIT-249](../literature.d/LIT-249.md),
  Assumption F.1, eq. 70) get the Hilbert–Schmidt property from K⁺ ≤ B,
  which is sufficient and strictly stronger.
