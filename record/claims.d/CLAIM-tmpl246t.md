---
status: Active
title: 'The adjoint of a square-integrable integral operator is the integral operator with the conjugate-transposed kernel'
version: 1
role: thesis
defeated_if: >-
  A step of the Fubini argument below that fails for a kernel in
  L²(μ⊗ν), for example a square-integrable kernel whose integrand
  k(x,y)f(y)ḡ(x) is not integrable. A kernel outside L²(μ⊗ν) does not
  defeat it, since the claim is not made there. Nor does a general
  bounded operator with no kernel, whose adjoint the Riesz theorem
  supplies without this formula.
tags:
- mathematics
- representation-learning
date: '2026-10-14'
line:
- learned-structure
- formal-apparatus
grounds:
- LIT-230
summary: >-
  The record's own step, written down in [THEORY-009](../theory.d/THEORY-009.md) and marked there as
  not the Riesz article's, which covers matrices and bounded operators
  only. For a kernel k in L²(μ⊗ν), the operator (Tf)(x) = ∫ k(x,y) f(y)
  dν(y) from L²(ν) to L²(μ) has adjoint (T*g)(y) = ∫ k̄(x,y) g(x) dμ(x),
  by Cauchy–Schwarz and Fubini. So T is self-adjoint, when μ = ν, exactly
  when k(x,y) = k̄(y,x) almost everywhere. It does not say where the
  symmetry of k comes from, which is [THEORY-009](../theory.d/THEORY-009.md)'s question, and it is not
  claimed for kernels that are not square-integrable.
---

# CLAIM-tmpl246t: The adjoint of a square-integrable integral operator is the integral operator with the conjugate-transposed kernel

## The claim

Let (X, μ) and (Y, ν) be σ-finite measure spaces and let k ∈ L²(μ⊗ν). The
operator T : L²(ν) → L²(μ), (Tf)(x) = ∫ k(x,y) f(y) dν(y), is bounded with
‖T‖ ≤ ‖k‖₂. Its adjoint T* : L²(μ) → L²(ν) is

  (T*g)(y) = ∫ k̄(x,y) g(x) dμ(x),

the integral operator with kernel k*(y,x) = k̄(x,y). For real kernels this is
the transpose. When X = Y and μ = ν, T is self-adjoint if and only if
k(x,y) = k̄(y,x) for μ⊗μ-almost every (x,y).

## The argument

1. **Integrability.** For f ∈ L²(ν) and g ∈ L²(μ), Cauchy–Schwarz on
   X × Y gives
   ∫∫ |k(x,y)| |f(y)| |g(x)| dμ dν ≤ ‖k‖₂ ‖g ⊗ f‖₂ = ‖k‖₂ ‖f‖ ‖g‖ < ∞.
   The same bound with g ranging over the unit ball gives ‖T‖ ≤ ‖k‖₂.
2. **Exchange.** The integrand is therefore integrable, so Fubini applies:
   ⟨Tf, g⟩ = ∫ (∫ k(x,y) f(y) dν(y)) ḡ(x) dμ(x)
   = ∫ f(y) · conj(∫ k̄(x,y) g(x) dμ(x)) dν(y) = ⟨f, Sg⟩,
   with S the integral operator in the claim. S is bounded by step 1
   applied to the kernel k̄(x,y) on Y × X.
3. **Uniqueness.** The adjoint is the unique operator with
   ⟨Tf, g⟩ = ⟨f, T*g⟩ for all f and g. Its existence for a bounded T is what
   the Riesz theorem supplies ([LIT-230](../literature.d/LIT-230.md)). Here it is exhibited directly. Two
   operators that satisfy the identity agree, because ⟨f, (S − S′)g⟩ = 0
   for every f forces (S − S′)g = 0. So S = T*.
4. **Self-adjointness.** With μ = ν, T = T* means the two kernels k and
   (x,y) ↦ k̄(y,x) define the same operator. The map from L²(μ⊗μ) kernels to
   Hilbert–Schmidt operators is an isometry, so it is injective, and the
   kernels agree almost everywhere.

This is the textbook fact for Hilbert–Schmidt operators. The record holds no
reading of a textbook that proves it, so the proof above is the record's own.

## Where it is used

- **[THEORY-009](../theory.d/THEORY-009.md).** It says HaoChen et al. apply the spectral theorem to a
  square-integrable kernel k(u,v) = w(u,v)/√(w(u)w(v)). By step 4 that
  operator is self-adjoint because w(u,v) = w(v,u). This claim is the
  step [THEORY-009](../theory.d/THEORY-009.md) marks as not the Riesz article's.
- **The X ≠ A case.** With two spaces (Zhai's thesis, [LIT-975](../literature.d/LIT-975.md), Theorem 2.11)
  the formula still gives the adjoint. T*T and TT* are then self-adjoint
  whatever k is. That is the composition [THEORY-009](../theory.d/THEORY-009.md) records as the thesis's
  source of self-adjointness.

## What it does not say

- Nothing about kernels outside L²(μ⊗ν). For a bounded but not
  Hilbert–Schmidt kernel operator the same formula holds when the integrand
  is integrable, for instance under a Schur test. That case is not argued
  here.
- Nothing about whether a self-supervised pair distribution makes k
  symmetric. That is [THEORY-009](../theory.d/THEORY-009.md)'s claim, and it rests on the readings it
  cites, not on this one.
