---
number: 4
status: Active
formerly:
- THEORY-tmpcawyi
title: 'A representation is determined by its centred kernel up to a translation and an orthogonal transformation, and the rotation-aligned distance between two representations equals the Bures distance between their kernels'
version: 8
history:
- version: 2
  date: '2026-10-14'
  note: >-
    After the close readings NOTE-753 (LIT-250) and NOTE-743
    (LIT-254). The title and body now say that a centred kernel fixes the
    representation up to a translation as well as an orthogonal map. "NBS
    is the cosine of the Riemannian shape distance" is re-credited from
    Lemma 2 to Thm 1, eq. 15; Lemma 2 is F = ‖Σ_XY‖_*. "Centred kernels are
    equal iff Procrustes distance is zero" is no longer cited to §2.2,
    which says it of RDMs; for kernels it follows from Thm 1. LIT-254 §2.2
    is marked as an argument, not a theorem, and its App. D.2 is added as
    the closer support for the Procrustes–Bures half. The promote_when
    records the Harvey half as done and the Jorgensen & Tian half as
    outstanding, so the status stays Proposed. Stale Deferred comments for
    LIT-250 and LIT-254 removed.
- version: 3
  date: '2026-10-14'
  note: >-
    A Connections section added: THEORY-236 (LIT-254, Thm 1), filed
    today, says why the invariant is not taken under the general linear
    group, where comparison is degenerate.
- version: 4
  date: '2026-10-14'
  note: >-
    After the close reading of LIT-259 (NOTE-829). The book states,
    not proves, Cor. 1.35 (proof left as an exercise); summary and body
    corrected. The (1.24) typo noted, and that the corollary is complex
    and unitary, so the real or non-spanning case needs an unstated step.
    promote_when records the LIT-259 reading as done and the Cor. 1.35
    clause as not met by the book but met by Thm 4.35's argument
    transferred; whether that suffices is left as an open call for the
    owner, and the status stays Proposed. The Deferred comment on LIT-259
    removed.
- version: 5
  date: '2026-10-14'
  note: >-
    The citation of the GNS article (LIT-241, read in NOTE-857) narrowed to the C*-algebraic statement; the kernel form rests on LIT-259 alone.
- version: 6
  date: '2026-10-14'
  note: >-
    Promoted from Proposed to Active at the owner's direction. Both clauses
    of promote_when are met. The Harvey, Larsen & Williams clause: NOTE-753
    (LIT-250, Read) read the proof of Lemma 2 in App. A.2, from which Thm 1
    follows, and found it correct. The Jorgensen & Tian clause: NOTE-829
    (LIT-259) read Remark 1.34 and Cor. 1.35 closely, and the book leaves
    the corollary's proof entirely as an exercise, so the confirmation is
    the record's own. The NOTE supplies the uniqueness argument, the book's
    proved argument for Thm 4.35 transferred: U defined on finite sums by
    Σc_xΦ₁(x) ↦ Σc_xΦ₂(x) preserves norms because both equal Σc̄_xc_yϕ(x,y),
    so it is well defined and isometric, extends to H₁ by minimality, and
    is onto because its range is closed and contains the dense span of the
    Φ₂(x). Checked again for this promotion; the argument is unchanged over
    real scalars. The body's caveat stands: applying the corollary to
    representation matrices whose rows do not span R^d needs the isometry
    extended across the complement, which LIT-250 §5.3 states as known.
    The promote_when is removed. The claim is unchanged.
- version: 7
  date: '2026-10-14'
  note: >-
    The record's own steps behind the promotion are filed with their proofs
    as CLAIM-290: Cor. 1.35's uniqueness of minimal realizations, and
    the finite case LIT-250 §5.3 states as known, including the extension
    across the complement that version 6 flagged. Cited where the finite
    step is made. The claim is unchanged.
- version: 8
  date: '2026-10-16'
  note: >-
    The "does not say" parenthetical claimed the Platonic-convergence
    claim disputes orthogonal equivalence. NOTE-286 shows LIT-302 adopts
    it by defining a representation by its kernel; corrected. The claim is
    unchanged.
tags:
- representation-learning
- mathematics
date: '2026-09-26'
source:
- LIT-250
- LIT-259
- LIT-254
- LIT-241
summary: >-
  Harvey, Larsen & Williams (2023), [LIT-250](../literature.d/LIT-250.md), Thm 1; Jorgensen & Tian,
  [LIT-259](../literature.d/LIT-259.md), Remark 1.34 and Cor. 1.35, which name the
  kernel-to-Hilbert-space construction as GNS and state its minimal
  realizations unique up to a unitary (proof left as an exercise). This is the GNS connection the owner
  asked about, stated.
extended_by:
- THEORY-008
- THEORY-017
presupposed_by:
- THEORY-002
supports:
- CLAIM-148
---
<!-- inactive-ok-file: THEORY-236 — Proposed; named in Connections for why GL-invariant comparison is degenerate, not leaned on -->

# THEORY-004: A representation is determined by its centred kernel up to a translation and an orthogonal transformation, and the rotation-aligned distance between two representations equals the Bures distance between their kernels

## Source

Harvey, Larsen & Williams (2023), [LIT-250](../literature.d/LIT-250.md), §2.2, §5.3, Thm 1 (eqs. 14–15), Lemma 2, eq. 25, as read in [NOTE-753](../notes.d/NOTE-753.md). Jorgensen & Tian, [LIT-259](../literature.d/LIT-259.md), Remark 1.34, Cor. 1.35, Ex. 4.28. Supporting: Kornblith et al. (2019), [LIT-254](../literature.d/LIT-254.md), as read in [NOTE-743](../notes.d/NOTE-743.md): App. D.2 (the Procrustes optimum is ‖YᵀX‖_*) and §2.2 (an argument, not a theorem, for orthogonal invariance); the C*-algebraic GNS statement, [LIT-241](../literature.d/LIT-241.md), of which [LIT-259](../literature.d/LIT-259.md)'s kernel form is the analogue; the article says nothing about kernels, real scalars or orthogonal maps.

## What was actually shown

Jorgensen & Tian call the construction of a Hilbert space from a positive-definite kernel "the GNS construction" (Remark 1.34) and state that a kernel's minimal realizations k(x,y) = ⟨Φ(x), Φ(y)⟩ are unique up to a unitary (Cor. 1.35). The proof is "left as an exercise"; the argument the book proves for Thm 4.35 transfers to it ([NOTE-829](../notes.d/NOTE-829.md)). Eq. (1.24) as printed, "UΦ₁(x) = Φ₂(x) U", is a typo for UΦ₁(x) = Φ₂(x). The corollary is over complex Hilbert spaces with a unitary; applying it to real representation matrices with an orthogonal map, or to representations whose rows do not span R^d and so are not minimal, needs a step the book does not state. They also note that commutative states are measures (Ex. 4.28). On a finite sample, two representation matrices with the same number of columns and the same Gram matrix differ by an orthogonal transformation ([LIT-250](../literature.d/LIT-250.md) §5.3, stated there as known, without proof; proved in [CLAIM-290](../claims.d/CLAIM-290.md), with no assumption that the rows span R^d). Since the centring removes column means, two representations with the same centred kernel differ by a translation and an orthogonal transformation. Harvey, Larsen & Williams prove that the Procrustes distance equals the Bures distance between the centred linear kernels (Thm 1, eq. 14), and that normalized Bures similarity is the cosine of the Riemannian shape distance (Thm 1, eq. 15); both follow from Lemma 2, F(K_X, K_Y) = ‖Σ_XY‖_*. So centred kernels are equal iff the Procrustes distance is zero, by Thm 1 and the metric property of B; §2.2 says the like of RDMs, not of kernels. Kornblith et al. had already noted that the orthogonal Procrustes optimum is ‖YᵀX‖_* (App. D.2), without linking it to the Bures fidelity. Their §2.2 case that a similarity index should be invariant to orthogonal maps (and isotropic scaling) is argued from training dynamics and symmetry, not proved. Their eq. 25 applies Uhlmann's theorem: the fidelity is the maximal overlap over all representations consistent with the kernels.

So the kernel is the invariant and the representation is one realization of it — the GNS picture, stated for representations.

## What this does not say

- That orthogonal equivalence is the right notion of sameness for learned models. The Platonic-convergence paper (LIT-302, NOTE-286) adopts it rather than disputing it, by defining a representation by its kernel (§2), and its alignment metric is invariant to more; adopting a notion is not an argument that it is right.
- Anything for nonlinear kernels on the representation, where what is determined is the kernel's feature map, not the representation itself.
- That a model's kernel is determined by anything short of the model; the uniqueness is of realizations of a given kernel.

## Connections

- **[THEORY-236](THEORY-236.md).** Why the orthogonal group, and not the general linear
  group. Kornblith et al. ([LIT-254](../literature.d/LIT-254.md), Thm 1) prove that a similarity index
  invariant to every invertible linear map takes the same value on all
  representations whose rank equals the number of examples. A comparison
  under that larger group is degenerate once the representation is wide
  enough, so the kernel is not traded for an invertible-linear invariant.
