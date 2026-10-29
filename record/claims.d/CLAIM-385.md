---
number: 385
status: Active
formerly:
- CLAIM-tmpjqb3e
title: 'If a symmetric operator on ℝⁿ commutes with an orthogonal representation of a compact group, each eigenspace is a sum of real irreducibles and each multiplicity a sum of multiples of their dimensions, so SO(2) and ℤ/n for n ≥ 3 force paired eigenvalues; conversely the spectrum fixes neither the group nor a basis inside an eigenspace'
version: 2
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Filed from THEORY-019 under ADR-032 (promotion audit, batches 042 and
    052). THEORY-019's summary says its sources state neither the
    degeneracy corollary nor its converse and that the document "puts that
    together from several readings": the result is the record's own. A
    result the record itself proves belongs in a CLAIM, as THEORY-005's
    became CLAIM-370 and THEORY-080's became CLAIM-384. The proof below
    needs only Schur's lemma, complete reducibility and Frobenius's
    theorem, so the claim is filed Active, demonstrated. THEORY-019 keeps
    the reading of the sources and its promote_when, which asks for a held
    source, and stays Proposed.
- version: 2
  date: '2026-10-29'
  note: >-
    THEORY-019 promoted by the twelfth status review (ADR-057); the bullet
    on what the sources state no longer calls it Proposed, and it leaves
    this entry's inactive-ok acknowledgement, with THEORY-017, which is
    Active. The claim is unchanged.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the proof below: a symmetric operator commuting with an
  orthogonal representation of a compact group that has an eigenspace
  which is not invariant under the group, or an eigenvalue whose
  multiplicity is not a sum of multiples of real-irreducible dimensions;
  or a procedure that recovers a unique group, or a unique basis inside a
  degenerate eigenspace, from the spectrum of one operator.
tags:
- mathematics
- representation-learning
date: '2026-10-20'
line:
- formal-apparatus
grounds:
- LIT-305
- LIT-329
- LIT-346
- LIT-362
---
<!-- inactive-ok-file: THEORY-005 — Proposed; the precedent named in the history, not leaned on -->

# CLAIM-385: If a symmetric operator on ℝⁿ commutes with an orthogonal representation of a compact group, each eigenspace is a sum of real irreducibles and each multiplicity a sum of multiples of their dimensions, so SO(2) and ℤ/n for n ≥ 3 force paired eigenvalues; conversely the spectrum fixes neither the group nor a basis inside an eigenspace

## The claim

Let G be a compact group (finite groups included) and ρ a real
representation of G on ℝⁿ, orthogonal for some inner product (any real
representation of a compact group is, for the averaged inner product).
Let A be symmetric for that inner product, with Aρ(g) = ρ(g)A for every g.
Then:

1. **Eigenspaces are G-invariant** and split into real irreducibles.
2. **Multiplicities count irreducible dimensions.** On an isotypic
   component W ≅ V^m, with V irreducible of real dimension d, every
   eigenspace of A meets W in a subspace of dimension kd for some k. So
   each multiplicity is a sum of multiples of the real-irreducible
   dimensions.
3. **Rotation groups pair eigenvalues over ℝ.** For SO(2), and for ℤ/n
   with n ≥ 3, every real irreducible that is not one-dimensional is a
   rotation plane, and A is a scalar on each such plane, so its
   eigenvalue there is at least doubled.
4. **The converse fails.** The spectrum of A determines neither G nor a
   basis inside a degenerate eigenspace.

## Proof

(1) If Av = λv then Aρ(g)v = ρ(g)Av = λρ(g)v, so the λ-eigenspace E_λ is
invariant. ρ is orthogonal, so the orthogonal complement of an invariant
subspace is invariant; induction on dimension splits E_λ into irreducibles
(complete reducibility).

(2) Decompose ℝⁿ into isotypic components W_i, the sums of all
irreducible subspaces isomorphic to V_i. For non-isomorphic irreducibles
V, V′, Schur's lemma gives Hom_G(V, V′) = 0. A commutes with ρ, so its
restriction to an irreducible subspace of W_i is an intertwiner into ℝⁿ,
whose components in the other W_j vanish; hence A W_i ⊆ W_i (Kondor &
Trivedi's Lemma 6 is this step, [LIT-305](../literature.d/LIT-305.md)). E_λ ∩ W_i is invariant, so by
(1) it is a direct sum of irreducibles, each in W_i and so isomorphic to
V_i: its dimension is k·d_i. The multiplicity of λ is Σ_i k_i d_i.
(End_G(V_i) is a real division algebra, ℝ, ℂ or ℍ, by Schur and
Frobenius; the count above does not need which.)

(3) The real irreducibles of SO(2) are the trivial representation and the
planes on which θ acts by rotation through jθ, j ≥ 1. For ℤ/n they are the
trivial and, for even n, the sign character, and the planes on which the
generator rotates by 2πj/n with 0 < j < n/2. On a rotation plane P with
generator J (J² = −I, Jᵀ = −J), the commutant is {aI + bJ}, since a
matrix commuting with every rotation of the plane is a rotation-scaling.
If the plane occurs once, A restricted to P lies in that commutant and is
symmetric, so b = 0 and A = aI on P, a doubled eigenvalue. If it occurs m
times, (2) gives multiplicities that are multiples of 2. The record's
checks agree: a symmetric 7 × 7 circulant has three pairs and one
singleton, and a symmetric matrix averaged over SO(2) acting with weights
(1, 1, 2, 3) on ℝ⁸ has four pairs.

(4) Let A have distinct eigenvalues with multiplicities m_1, …, m_r. A
commutes with every orthogonal map preserving each eigenspace, that is,
with O(m_1) × … × O(m_r) acting block-wise, and so with every subgroup of
that product. The spectrum is therefore consistent with every one of those
groups, and no procedure that reads only the spectrum can return a unique
group. O'Donnell's cube gives a concrete pair ([LIT-346](../literature.d/LIT-346.md)): the Laplacian of
the n-cube has an eigenvalue proportional to k with multiplicity C(n, k), for k = 0, …, n, and each level is
irreducible under the hyperoctahedral group but splits under the symmetric
group S_n (level 1 is the trivial representation plus the standard one).
Within a degenerate eigenspace every orthonormal basis is an eigenbasis,
so the spectrum fixes no basis there: the Walsh characters of a level are
one choice among many, and a degeneracy test finds the pairs of [LIT-362](../literature.d/LIT-362.md)'s
rotation planes but not their frequencies.

## What it does not say

- **That degeneracy detects symmetry.** (4) says the reverse. What a
  spectrum carries is the isotypic dimension count of whatever group is
  present, not the group.
- **That the sources state it.** Peter & Weyl build representations as
  eigenspaces of an invariant kernel ([LIT-329](../literature.d/LIT-329.md)), and Kondor & Trivedi
  prove that intertwiners preserve isotypic components ([LIT-305](../literature.d/LIT-305.md));
  neither states (2)–(4). The reading of the sources, with the
  real-scalar correction from [LIT-362](../literature.d/LIT-362.md), stays in [THEORY-019](../theory.d/THEORY-019.md).
- **Anything about noisy operators.** The statement is exact. Near-
  degeneracy and the thresholds a test on estimated operators would need
  are open.
- **That multiplicities are intrinsic in a further sense.** They are
  unitarily invariant, which is [THEORY-017](../theory.d/THEORY-017.md)'s sense of intrinsic; the
  basis inside a multiplet is extra data.
