---
status: Active
title: 'A positive-definite kernel''s minimal realizations are unique up to a unitary, and two finite representation matrices with the same centred Gram matrix differ by a translation and an orthogonal map'
version: 1
role: thesis
defeated_if: >-
  A step of the argument below that fails under its stated hypotheses.
  Examples: a well-defined, isometric U whose range is not dense in a
  minimal H₂, or finite matrices X and Y with XXᵀ = YYᵀ whose row spaces
  differ in dimension. A realization that is not minimal does not defeat
  part (a), which is stated for minimal ones only.
tags:
- mathematics
- representation-learning
date: '2026-10-14'
line:
- learned-structure
- formal-apparatus
grounds:
- LIT-259
- LIT-250
summary: >-
  The record's own proofs of two steps that [THEORY-004](../theory.d/THEORY-004.md) rests on and that
  its sources state without proof. (a) Jorgensen & Tian's Cor. 1.35:
  minimal realizations of a positive-definite kernel are unique up to a
  unitary. The book leaves this "as an exercise", and [NOTE-829](../notes.d/NOTE-829.md) supplied
  the book's own proof of Thm 4.35, transferred. (b) The finite case that
  [LIT-250](../literature.d/LIT-250.md) §5.3 states as known: XXᵀ = YYᵀ implies Y = XQ with Q
  orthogonal, with no assumption that the rows span R^d. With centring
  this becomes a translation and an orthogonal map. It does not say Q is
  unique, which fails when the rank is below d.
---

# CLAIM-tmpds763: A positive-definite kernel's minimal realizations are unique up to a unitary, and two finite representation matrices with the same centred Gram matrix differ by a translation and an orthogonal map

## The claim

**(a) Minimal realizations.** Let k : S × S → F, F = ℝ or ℂ, be
positive definite. For i = 1, 2 let Φᵢ : S → Hᵢ satisfy
k(s,t) = ⟨Φᵢ(s), Φᵢ(t)⟩, with the Φᵢ(s) spanning a dense subspace of Hᵢ.
Then there is exactly one unitary U : H₁ → H₂ with UΦ₁(s) = Φ₂(s) for every
s. Over ℝ it is an orthogonal isomorphism.

**(b) Finite matrices.** Let X, Y ∈ ℝ^(n×d), whose rows are two
representations of the same n inputs. If XXᵀ = YYᵀ, then Y = XQ for some
Q ∈ O(d).

**(c) Centred.** Let C = I − (1/n)11ᵀ. If CXXᵀC = CYYᵀC, then
Y = XQ + 1bᵀ for some Q ∈ O(d) and b ∈ ℝ^d.

## The argument

**(a)** This is [NOTE-829](../notes.d/NOTE-829.md)'s argument, the book's proof of Thm 4.35 with
π_i(A)u_i replaced by Φᵢ(s).

1. Define U on finite combinations by U Σ c_s Φ₁(s) := Σ c_s Φ₂(s).
2. For both i, ‖Σ c_s Φᵢ(s)‖² = Σ_(s,t) c̄_s c_t k(s,t), the same number.
3. So a combination that vanishes in H₁ also vanishes in H₂. Hence U is
   well defined, linear and isometric on span Φ₁(S).
4. An isometry on a dense subspace extends uniquely to an isometry on
   H₁. Its range is complete, hence closed. It contains span Φ₂(S), which
   is dense in H₂, so the range is H₂ and U is unitary.
5. U is unique because any unitary with UΦ₁(s) = Φ₂(s) is fixed on the
   dense set span Φ₁(S).

Nothing here uses complex scalars, so over ℝ it gives an orthogonal
isomorphism.

**(b)**
1. Let xⱼ and yⱼ be the rows. Apply (a) with S = {1, …, n},
   k(j,l) = (XXᵀ)_(jl), H₁ = row space of X and H₂ = row space of Y. This
   gives an orthogonal isomorphism U : H₁ → H₂ with Uxⱼ = yⱼ.
2. dim H₁ = rank X = rank XXᵀ = rank YYᵀ = dim H₂ = r.
3. The orthogonal complements H₁^⊥ and H₂^⊥ in ℝ^d therefore both have
   dimension d − r. Choose any orthogonal isomorphism V between them.
4. Then Q′ = U ⊕ V is orthogonal on ℝ^d with Q′xⱼ = yⱼ for every j.
   Q = Q′ᵀ gives Y = XQ.

When r < d, V is arbitrary, so Q is not unique.

**(c)** Apply (b) to CX and CY, whose Gram matrices are equal by
hypothesis. Then CY = CXQ. Write Y = CY + 1ȳᵀ and X = CX + 1x̄ᵀ, where x̄
and ȳ are the column means. Then Y = XQ + 1(ȳ − Qᵀx̄)ᵀ.

## Where it is used

- **[THEORY-004](../theory.d/THEORY-004.md).** Its clause that a representation is determined by its
  centred kernel up to a translation and an orthogonal map is (c). The
  promotion history (version 6) took Cor. 1.35's confirmation as the
  record's own. It also flagged that representation matrices whose rows do
  not span ℝ^d need the isometry extended across the complement. That is
  step (b)3.
- **[LIT-250](../literature.d/LIT-250.md) §5.3** states (b) as known, without proof.

## What it does not say

- Nothing about kernels estimated from data, or about approximate
  equality. If CXXᵀC and CYYᵀC are only close, (c) says nothing; that is
  what the Procrustes–Bures identity in [THEORY-004](../theory.d/THEORY-004.md) measures.
- Nothing about realizations that are not minimal. In infinite dimensions,
  a non-minimal realization gives U only as an isometry onto a closed
  subspace.
