---
number: 4
status: Proposed
formerly:
- THEORY-tmpcawyi
promote_when: >-
  A close reading of Harvey, Larsen & Williams's Thm 1 proof (App. A.2) and of
  Jorgensen & Tian's Cor. 1.35, which the book leaves partly as an exercise.
  The first half is done: NOTE-tmpx7mtu read the proof of Lemma 2 in App.
  A.2, from which Thm 1 follows, and found it correct. What remains is the
  close reading of Jorgensen & Tian (LIT-259), which this record has so far
  only skimmed.
title: 'A representation is determined by its centred kernel up to a translation and an orthogonal transformation, and the rotation-aligned distance between two representations equals the Bures distance between their kernels'
version: 2
history:
- version: 2
  date: '2026-10-14'
  note: >-
    After the close readings NOTE-tmpx7mtu (LIT-250) and NOTE-tmph96lt
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
  kernel-to-Hilbert-space construction as GNS and prove its minimal
  realizations unique up to a unitary. This is the GNS connection the owner
  asked about, stated.
extended_by:
- THEORY-008
- THEORY-017
presupposed_by:
- THEORY-002
supports:
- CLAIM-148
---
<!-- inactive-ok-file: LIT-259 — Deferred: filed and skimmed on 2026-09-26 while pursuing the owner's Riesz/Radon–Nikodym/GNS question; the theories citing it are Proposed until it is read closely -->

# THEORY-004: A representation is determined by its centred kernel up to a translation and an orthogonal transformation, and the rotation-aligned distance between two representations equals the Bures distance between their kernels

## Source

Harvey, Larsen & Williams (2023), [LIT-250](../literature.d/LIT-250.md), §2.2, §5.3, Thm 1 (eqs. 14–15), Lemma 2, eq. 25, as read in [NOTE-tmpx7mtu](../notes.d/NOTE-tmpx7mtu.md). Jorgensen & Tian, [LIT-259](../literature.d/LIT-259.md), Remark 1.34, Cor. 1.35, Ex. 4.28. Supporting: Kornblith et al. (2019), [LIT-254](../literature.d/LIT-254.md), as read in [NOTE-tmph96lt](../notes.d/NOTE-tmph96lt.md): App. D.2 (the Procrustes optimum is ‖YᵀX‖_*) and §2.2 (an argument, not a theorem, for orthogonal invariance); the GNS statement, [LIT-241](../literature.d/LIT-241.md).

## What was actually shown

Jorgensen & Tian call the construction of a Hilbert space from a positive-definite kernel "the GNS construction" (Remark 1.34) and prove that a kernel's minimal realizations k(x,y) = ⟨Φ(x), Φ(y)⟩ are unique up to a unitary (Cor. 1.35); they also note that commutative states are measures (Ex. 4.28). On a finite sample, two representation matrices with the same number of columns and the same Gram matrix differ by an orthogonal transformation ([LIT-250](../literature.d/LIT-250.md) §5.3, stated there as known, without proof). Since the centring removes column means, two representations with the same centred kernel differ by a translation and an orthogonal transformation. Harvey, Larsen & Williams prove that the Procrustes distance equals the Bures distance between the centred linear kernels (Thm 1, eq. 14), and that normalized Bures similarity is the cosine of the Riemannian shape distance (Thm 1, eq. 15); both follow from Lemma 2, F(K_X, K_Y) = ‖Σ_XY‖_*. So centred kernels are equal iff the Procrustes distance is zero, by Thm 1 and the metric property of B; §2.2 says the like of RDMs, not of kernels. Kornblith et al. had already noted that the orthogonal Procrustes optimum is ‖YᵀX‖_* (App. D.2), without linking it to the Bures fidelity. Their §2.2 case that a similarity index should be invariant to orthogonal maps (and isotropic scaling) is argued from training dynamics and symmetry, not proved. Their eq. 25 applies Uhlmann's theorem: the fidelity is the maximal overlap over all representations consistent with the kernels.

So the kernel is the invariant and the representation is one realization of it — the GNS picture, stated for representations.

## What this does not say

- That orthogonal equivalence is the right notion of sameness for learned models (see the Platonic-convergence claim, which disputes it).
- Anything for nonlinear kernels on the representation, where what is determined is the kernel's feature map, not the representation itself.
- That a model's kernel is determined by anything short of the model; the uniqueness is of realizations of a given kernel.
