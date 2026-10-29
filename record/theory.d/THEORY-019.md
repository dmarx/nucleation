---
number: 19
status: Active
formerly:
- THEORY-tmp1jea9
title: 'Symmetry forces spectral degeneracy but degeneracy does not identify a symmetry: an operator commuting with a group has eigenspaces built from its real irreducibles, so abelian rotation groups force pairs over ℝ, and the spectrum fixes neither the group nor a basis inside a multiplet'
version: 4
history:
- version: 2
  date: '2026-10-05'
  note: >-
    `extends: THEORY-017` re-filed as `presupposes: THEORY-017` (ADR-029).
    The claim that multiplicities are intrinsic and the basis inside a
    multiplet is not uses that account's sense of intrinsic; the claim about
    symmetry and degeneracy does not refine it.
- version: 3
  date: '2026-10-20'
  note: >-
    The result this account assembles, that symmetric commuting operators
    have eigenspaces built from real irreducibles, that SO(2) and ℤ/n for
    n ≥ 3 pair eigenvalues over ℝ, and that the spectrum fixes neither the
    group nor a basis inside a multiplet, is filed as the record's own
    demonstrated claim, CLAIM-385, under ADR-032 (promotion audit,
    batches 042 and 052). This account keeps the reading of the sources and
    its promote_when, which asks for a held source stating the real Schur
    corollary. Status stays Proposed. Title unchanged.
- version: 4
  date: '2026-10-29'
  note: >-
    Promoted by the twelfth status review (ADR-057; ADR-047's ruling on
    re-derivations, and the owner's ruling of the tenth pass that a
    re-derivation meets a promote_when asking for a source's own
    statement). The promote_when asked for "A held source that states and
    proves the Schur corollary over the reals, with the three real types
    ... The record holds none, and the pieces now come from LIT-329 §3,
    LIT-305 Lemma 6 and readers' numerical checks. More numerical examples
    cannot settle it." The reviewing session read its ask for a held text
    as an ask for a checked proof, which is what it was missing; the clause
    on numerical examples rules out examples, not a proof. The note of this
    date gives the proof, and the reviewing session checked it numerically
    for one group of each real type, with non-commuting controls, and
    recomputed the cube's levels under B₃ and S₃. The promote_when's two
    refutation conditions are CLAIM-385's defeat condition. Title
    unchanged.
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
summary: >-
  Peter & Weyl (1927), [LIT-329](../literature.d/LIT-329.md) §3, build representations as eigenspaces of an
  invariant kernel, and Kondor & Trivedi, [LIT-305](../literature.d/LIT-305.md) Lemma 6, show that
  intertwiners preserve isotypic components. Neither states the degeneracy
  corollary or its converse. This document puts that together from several
  readings, and that assembly, with its proof, is now the record's own
  claim, CLAIM-385; what stays here is the reading. It adds the real-scalar correction in [NOTE-282](../notes.d/NOTE-282.md), found in the
  reading of [LIT-362](../literature.d/LIT-362.md), and the counting in the reading of [LIT-346](../literature.d/LIT-346.md). It does not
  support "degeneracy detects symmetry": a spectrum is consistent with several
  groups and says nothing about the characters inside a multiplet.
extended_by:
- THEORY-084
presupposes:
- THEORY-017
supports:
- CLAIM-193
- CLAIM-269
---

# THEORY-019: Symmetry forces spectral degeneracy but degeneracy does not identify a symmetry: an operator commuting with a group has eigenspaces built from its real irreducibles, so abelian rotation groups force pairs over ℝ, and the spectrum fixes neither the group nor a basis inside a multiplet

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

Presupposes [THEORY-017](THEORY-017.md)'s sense of intrinsic: the multiplet is intrinsic, and the basis inside it is extra data.
[LIT-322](../literature.d/LIT-322.md)'s weekday circles are real ℤ/7 irreducibles ([NOTE-273](../notes.d/NOTE-273.md)). A degeneracy
test would see them as pairs only.
Wedderburn's structure theorem ([THEORY-652](THEORY-652.md)) gives the algebra-side half
of the real Schur corollary: each simple real
block is a full matrix algebra over a real division algebra. It does not give
the step from a representation's commutant to such a block; the note of
2026-10-29 gives it. Pontryagin
duality ([THEORY-645](THEORY-645.md)) is the abelian case, where the irreducibles over ℂ
are characters.

## Note of 2026-10-20: the assembled result is a claim

Promotion audit, batches 042 and 052. The forward direction, the pairing
over ℝ and the failure of the converse re-derive from Schur's lemma,
complete reducibility and Frobenius's theorem, and no held source states
them together, so they are the record's own result. They are filed as
[CLAIM-385](../claims.d/CLAIM-385.md), demonstrated, with the proof. This account keeps what the
sources say and do not say, the readers' real-scalar correction, and the
promote_when, which a held representation-theory text would meet.

## Note of 2026-10-29: the real Schur corollary, proved

The twelfth status review proved the corollary the promote_when asked a
held source for, and checked it numerically.

Let V be a real irreducible of G of dimension d, with a G-invariant inner
product, and let 𝔽 = End_G(V). By Schur's lemma every nonzero element of 𝔽
is invertible, so 𝔽 is a finite-dimensional real division algebra, and by
Frobenius's theorem it is ℝ, ℂ or ℍ. On an isotypic component W ≅ V^m an
intertwiner is an m × m array of intertwiners V → V, so End_G(W) = M_m(𝔽).
Transposition maps 𝔽 to itself, because ρ is orthogonal. A symmetric s in 𝔽
has a real eigenvalue λ, and s − λI is in 𝔽 and singular, so it is zero: the
symmetric elements of 𝔽 are the real scalars, and transposition is 𝔽's
conjugation. A symmetric operator commuting with ρ is therefore, on W, a
Hermitian matrix over 𝔽. Each of its eigenspaces in W is G-invariant, so it
is a sum of copies of V and has real dimension a multiple of d; generically
there are m eigenvalues, each of multiplicity exactly d.

The check (numpy, run by the reviewing session): for S₃ on three copies of
its 2-dimensional representation (ℝ type), ℤ/5 on three copies of a rotation
plane (ℂ type) and the quaternion group on two copies of ℍ (ℍ type), the
commutant has dimension 9, 18 and 16, which is m² dim 𝔽, and the symmetric
commutant 6, 9 and 6, the dimension of the Hermitian m × m matrices over 𝔽.
A group-averaged random symmetric matrix has multiplicities (2, 2, 2),
(2, 2, 2) and (4, 4), with G-invariant eigenspaces. As controls, a random
symmetric matrix, and an SO(2)-averaged one perturbed by 10⁻³ in a
non-commuting direction, have simple spectra. The 3-cube's Laplacian, with
spectrum 0, 2, 2, 2, 4, 4, 4, 6, commutes with the hyperoctahedral group B₃,
under which each level has a one-dimensional commutant, and with S₃, under
which levels 1 and 2 have a two-dimensional one: one spectrum, two groups.
