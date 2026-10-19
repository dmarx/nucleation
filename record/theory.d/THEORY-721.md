---
number: 721
status: Active
formerly:
- THEORY-tmpa07hh
title: 'On a complex Hilbert space no orthonormal basis or tensor factorisation of given dimensions is distinguished by the space alone, and orthonormal bases correspond exactly to commutative special †-Frobenius algebras; over the reals that correspondence fails'
version: 1
history:
- version: 1
  date: '2026-10-19'
  note: >-
    Split from THEORY-017 and filed Active at the owner's direction,
    carrying out the promotion audit's decision
    (record/promotion-audit/decisions/THEORY-017.yaml, batch 005, ADR-047).
    THEORY-017's promote_when recorded the Coecke–Pavlovic–Vicary condition
    as met (LIT-274 read in NOTE-247, LIT-275 in NOTE-248), and held the
    whole entry Proposed only for a per-placement check of its cross-source
    table. This THEORY holds the mathematics. THEORY-017 keeps the table and
    its two inferences, and extends this one. The elementary parts and the
    real-scalar counterexample were checked again for the split.
tags:
- mathematics
- quantum-foundations
date: '2026-10-19'
source:
- LIT-274
- LIT-275
summary: >-
  Three results [THEORY-017](THEORY-017.md) rested on, held apart from its synthesis. (a) The
  unitary group acts transitively on the orthonormal bases of a
  finite-dimensional Hilbert space, and on its tensor factorisations of
  given dimensions, so neither is fixed by the space; a non-degenerate
  self-adjoint operator fixes a basis up to phases, and its invariant
  content is its spectrum. (b) Over ℂ, commutative special †-Frobenius
  algebras correspond exactly to orthonormal bases: Coecke, Pavlovic &
  Vicary, [LIT-274](../literature.d/LIT-274.md), Thm 5.1 and §6, in finite dimension; Abramsky & Heunen,
  [LIT-275](../literature.d/LIT-275.md), Thm 22, for the non-unital ones satisfying the H*-axiom, in any
  dimension. (c) Over ℝ it fails: ℂ as a real algebra, with multiplication
  scaled by 1/√2, is a commutative special †-Frobenius algebra with no
  nonzero copyable vector.
extended_by:
- THEORY-017
supports:
- CLAIM-148
---
<!-- inactive-ok-file: THEORY-017 — Proposed; the synthesis this core was split from and that extends it, cited as open -->

# THEORY-721: On a complex Hilbert space no orthonormal basis or tensor factorisation of given dimensions is distinguished by the space alone, and orthonormal bases correspond exactly to commutative special †-Frobenius algebras; over the reals that correspondence fails

## Source

- Coecke, Pavlovic & Vicary, [LIT-274](../literature.d/LIT-274.md), Thm 5.1 and §6, read in full in
  [NOTE-247](../notes.d/NOTE-247.md) (its claims C1 and C2, "strong (proof)").
- Abramsky & Heunen, [LIT-275](../literature.d/LIT-275.md), Lemma 3 and Thm 22, read in [NOTE-248](../notes.d/NOTE-248.md).
- Parts (a) and (c) are elementary and written out below.

## What was actually shown

**(a) No basis or factorisation is intrinsic.** Let H be a Hilbert space of
finite dimension n. If {e_i} and {f_i} are orthonormal bases, the map
U e_i = f_i is unitary, so the unitary group acts transitively on
orthonormal bases. If U₁, U₂ : H_A ⊗ H_B → H are two unitary
identifications with factors of fixed dimensions, U₂U₁⁻¹ is a unitary of
H that carries the first factorisation to the second. So nothing in H
alone picks out a basis or a factorisation. A non-degenerate self-adjoint
operator does fix a basis, its eigenbasis, up to a phase on each vector.
Under unitary conjugation, though, all that survives is its list of
eigenvalues.

**(b) Bases are commutative special †-Frobenius algebras, over ℂ.** On a
finite-dimensional complex Hilbert space, every commutative †-Frobenius
monoid determines an orthogonal basis, namely its copyable elements, and
is the copy-and-delete structure of that basis ([LIT-274](../literature.d/LIT-274.md), Thm 5.1). It is
special, m∘m† = id, exactly when the basis is orthonormal (§6). Without a
unit the correspondence extends to every dimension. On a complex Hilbert
space of any dimension, a commutative special †-Frobenius algebra comes
from an orthonormal basis exactly when it satisfies Ambrose's H*-axiom,
equivalently when it is semisimple ([LIT-275](../literature.d/LIT-275.md), Thm 22). A unital Frobenius
algebra exists in Hilb only in finite dimension (Lemma 3).

**(c) Over ℝ it fails.** Take ℂ as the real Hilbert space ℝ² with
orthonormal basis {1, i} and inner product ⟨a, b⟩ = Re(a b̄). Let m be
complex multiplication, so m(1⊗1) = 1, m(1⊗i) = m(i⊗1) = i and
m(i⊗i) = −1.

- **Special.** m m†(1) = ⟨1, 1⟩·1 + ⟨−1, 1⟩·(−1) = 2, and likewise
  m m†(i) = 2i. So μ = m/√2 satisfies μμ† = id.
- **Commutative and associative**, as complex multiplication is.
- **Frobenius.** m†(z) is the bilinear form (a, b) ↦ Re(ab z̄). Since the
  adjoint of multiplication by x is multiplication by x̄, the form
  attached to (x ⊗ 1)m†(z) is (a, b) ↦ Re(x̄a·b·z̄), which is
  Re(ab·conj(xz)), the form of m†(xz). So m† is a module map, which is the
  Frobenius law.
- **No copyable vector.** A vector x is copyable when μ†(x) = x ⊗ x. The
  form μ†(x) has matrix (1/√2)[[p, −q], [−q, −p]] in {1, i}, where
  x̄ = p + qi. Its determinant is −|x|²/2, so it has rank 2 for x ≠ 0,
  while x ⊗ x has rank 1. So no nonzero x is copyable.

So over the reals a basis still induces a commutative special
†-Frobenius algebra, but such an algebra need not come from a basis.
[NOTE-248](../notes.d/NOTE-248.md) adds that this ℂ, as a real algebra, satisfies the H*-axiom, so
the axiom does not rescue the real case in any dimension.

## What this does not say

- **That basis-dependent models are wrong**, or which basis a model should
  use. That, and where the record's Hilbert-space works get their basis,
  is [THEORY-017](THEORY-017.md)'s synthesis, which is Proposed.
- **Anything about continuous observables.** They have no eigenbasis and
  fall outside Thm 22 ([LIT-275](../literature.d/LIT-275.md), §6).
- **That a tensor factorisation is a basis.** It is coarser: many bases
  respect it. Part (a) treats both only as structure the space does not
  supply.
- **Whether the H*-axiom is automatic.** [LIT-275](../literature.d/LIT-275.md) leaves this open
  (Prop. 23).
