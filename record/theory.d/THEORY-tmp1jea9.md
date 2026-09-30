---
status: Proposed
promote_when: >-
  A held source that states and proves the Schur corollary over the reals,
  with the three real types. On an isotypic component made of m copies of a
  real irreducible of real dimension d, the commutant is M_m(𝔽), with 𝔽 = ℝ,
  ℂ or ℍ. A symmetric commuting operator is then a Hermitian matrix over 𝔽,
  so each of its eigenvalues has a real multiplicity that is a multiple of d.
  A representation-theory text such as Serre would do it. The record holds none,
  and the pieces now come from LIT-329 §3, LIT-305 Lemma 6 and readers'
  numerical checks. More numerical examples cannot settle it. The account would
  be refuted by an operator commuting with ρ(G) that has an eigenspace that is
  not G-invariant. Its converse half would be refuted by a procedure that
  recovers a unique group from one operator's eigenvalue multiplicities.
title: 'Symmetry forces spectral degeneracy but degeneracy does not identify a symmetry: an operator commuting with a group has eigenspaces built from its real irreducibles, so abelian rotation groups force pairs over ℝ, and the spectrum fixes neither the group nor a basis inside a multiplet'
version: 1
tags:
- mathematics
- representation-learning
date: '2026-09-30'
source:
- LIT-329
- LIT-305
- LIT-352
- LIT-362
- LIT-346
- LIT-319
extends:
- THEORY-017
summary: >-
  Peter & Weyl (1927), [LIT-329](../literature.d/LIT-329.md) §3, build representations as eigenspaces of an
  invariant kernel, and Kondor & Trivedi, [LIT-305](../literature.d/LIT-305.md) Lemma 6, show that
  intertwiners preserve isotypic components. Neither states the degeneracy
  corollary or its converse. This document puts that together from several
  readings. It adds the real-scalar correction in [NOTE-282](../notes.d/NOTE-282.md), found in the
  reading of [LIT-362](../literature.d/LIT-362.md), and the counting in the reading of [LIT-346](../literature.d/LIT-346.md). It does not
  support "degeneracy detects symmetry": a spectrum is consistent with several
  groups and says nothing about the characters inside a multiplet.
---

# THEORY-tmp1jea9: Symmetry forces spectral degeneracy but degeneracy does not identify a symmetry: an operator commuting with a group has eigenspaces built from its real irreducibles, so abelian rotation groups force pairs over ℝ, and the spectrum fixes neither the group nor a basis inside a multiplet

## Source

- Peter & Weyl (1927), [LIT-329](../literature.d/LIT-329.md), §§3–4, as read in [NOTE-305](../notes.d/NOTE-305.md).
- Kondor & Trivedi (2018), [LIT-305](../literature.d/LIT-305.md), Lemmas 3–10, as read in [NOTE-282](../notes.d/NOTE-282.md), including its dated correction.
- Murota, Kanno, Kojima & Kojima, [LIT-352](../literature.d/LIT-352.md), Props 3.2–3.5 and Thm 3.1(C), as read in [NOTE-276](../notes.d/NOTE-276.md).
- Cohen & Welling (2014), [LIT-362](../literature.d/LIT-362.md), §2.2 and §3.3, as read in [NOTE-307](../notes.d/NOTE-307.md).
- O'Donnell, [LIT-346](../literature.d/LIT-346.md), Props 2.37 and 2.47 and Ex. 1.30, as read in [NOTE-291](../notes.d/NOTE-291.md).
- Bronstein et al., [LIT-319](../literature.d/LIT-319.md), pp. 37 and 54, as read in [NOTE-274](../notes.d/NOTE-274.md).

## What was actually shown

**Forward direction.** Peter–Weyl prove that the eigenspaces of an invariant
Hermitian kernel z(st⁻¹) carry representations of the group (§3). They then
split those representations into irreducibles (§4). So an eigenvalue's
multiplicity is at least the dimension of an irreducible, and it can be more
when several copies occur ([NOTE-305](../notes.d/NOTE-305.md)). Kondor & Trivedi's Lemma 6 is the
general form: an equivariant linear map preserves isotypic components.
Neither paper states "symmetric commuting operator ⇒ multiplicities are sums
of irrep dimensions". That step, from Lemma 6 plus Schur II, is the readers'
([NOTE-282](../notes.d/NOTE-282.md)).

**Over the reals, abelian groups still pair eigenvalues.** [NOTE-282](../notes.d/NOTE-282.md) first said
that abelian symmetries give no degeneracy. The reading of [LIT-362](../literature.d/LIT-362.md) corrected
this ([NOTE-307](../notes.d/NOTE-307.md)). The real irreducibles of SO(2), and of ℤ/n for n ≥ 3, are
2-D rotation planes. Their commutant is {aI + bJ}, whose only symmetric
members are scalars, so each plane carries a doubled eigenvalue. The claim
holds over ℂ and for groups with real characters, such as (ℤ/2)ⁿ. Murota et
al.'s Thm 3.1(C) fails for the same reason: it assumes every real irreducible
is of real type ([NOTE-276](../notes.d/NOTE-276.md)).

I re-checked this when filing. A symmetric 7 × 7 circulant has three pairs and
one singleton. Averaging a random symmetric 8 × 8 matrix over SO(2) with
weights (1, 1, 2, 3) gives four pairs. Averaging a 4 × 4 matrix over the
quaternion group acting on ℝ⁴ gives one fourfold eigenvalue, the ℍ-type case.

**The converse fails in three ways.**

- *The group is not identified.* The cube's Laplacian has eigenvalue k with
  multiplicity C(n,k). Each level is irreducible under the hyperoctahedral
  group but reducible under S_n ([NOTE-291](../notes.d/NOTE-291.md)). One spectrum is consistent with
  both groups.
- *The pieces inside a multiplet are invisible.* The Walsh characters in a
  level form one basis of the eigenspace among many ([NOTE-291](../notes.d/NOTE-291.md)). A degeneracy
  test finds the pairs but not their frequencies ([NOTE-307](../notes.d/NOTE-307.md)). GDL assumes
  degeneracy away so that the Fourier basis is well defined, and notes that
  eigenvectors are unstable ([LIT-319](../literature.d/LIT-319.md), pp. 37, 54).
- *Degeneracy can be accidental* ([NOTE-305](../notes.d/NOTE-305.md)).

For a single operator, degeneracy is a symmetry only in a trivial sense. Any
k-fold eigenspace is rotated by O(k) while the operator stays fixed, so the
multiplicity says nothing about a group acting on the data. Structure beyond
that needs several operators and the joint commutant. Murota et al. compute
it without a group supplied, and it gives central projectors and
multiplicities, not a group ([NOTE-276](../notes.d/NOTE-276.md)). This paragraph is the filer's own
inference.

## What this does not say

- That spectral degeneracy is useless as a diagnostic. Eigenvalue
  multiplicities are unitarily invariant, and so intrinsic in [THEORY-017](THEORY-017.md)'s
  sense. What they carry is the isotypic dimension count, not a group.
- That any of these papers detects an unknown symmetry. [LIT-305](../literature.d/LIT-305.md), [LIT-314](../literature.d/LIT-314.md) and
  [LIT-319](../literature.d/LIT-319.md) impose G, and [LIT-362](../literature.d/LIT-362.md) and [LIT-363](../literature.d/LIT-363.md) need paired inputs and an assumed
  group or transformation (record/curation.d/2026/09/29/233704.md).
- Anything about noisy operators. Every source is exact-arithmetic. Near-
  degeneracy and the thresholds a test would need are open ([NOTE-276](../notes.d/NOTE-276.md),
  [NOTE-274](../notes.d/NOTE-274.md)).

## Connections

[THEORY-017](THEORY-017.md): the multiplet is intrinsic, and the basis inside it is extra data.
[LIT-322](../literature.d/LIT-322.md)'s weekday circles are real ℤ/7 irreducibles ([NOTE-273](../notes.d/NOTE-273.md)). A degeneracy
test would see them as pairs only.
