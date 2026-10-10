---
number: 4
status: Proposed
formerly:
- THEORY-tmpcawyi
promote_when: >-
  A close reading of Harvey, Larsen & Williams's Thm 1 proof (App. A.2) and of
  Jorgensen & Tian's Cor. 1.35, which the book leaves partly as an exercise.
  Both are proved in the sources; this record has so far only skimmed them.
title: 'A representation is determined by its kernel up to an orthogonal transformation, and the rotation-aligned distance between two representations equals the Bures distance between their kernels'
version: 1
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
- CLAIM-tmpro4wi
---
<!-- inactive-ok-file: LIT-259 — Deferred: filed and skimmed on 2026-09-26 while pursuing the owner's Riesz/Radon–Nikodym/GNS question; the theories citing it are Proposed until it is read closely -->
<!-- inactive-ok-file: LIT-250 — Deferred: filed and skimmed on 2026-09-26 while pursuing the owner's Riesz/Radon–Nikodym/GNS question; the theories citing it are Proposed until it is read closely -->
<!-- inactive-ok-file: LIT-254 — Deferred: filed and skimmed on 2026-09-26 while pursuing the owner's Riesz/Radon–Nikodym/GNS question; the theories citing it are Proposed until it is read closely -->

# THEORY-004: A representation is determined by its kernel up to an orthogonal transformation, and the rotation-aligned distance between two representations equals the Bures distance between their kernels

## Source

Harvey, Larsen & Williams (2023), [LIT-250](../literature.d/LIT-250.md), §2.2, §5.3, Thm 1, Lemma 2, eq. 25. Jorgensen & Tian, [LIT-259](../literature.d/LIT-259.md), Remark 1.34, Cor. 1.35, Ex. 4.28. Supporting: Kornblith et al. (2019), [LIT-254](../literature.d/LIT-254.md), §2.2 (the case for orthogonal invariance); the GNS statement, [LIT-241](../literature.d/LIT-241.md).

## What was actually shown

Jorgensen & Tian call the construction of a Hilbert space from a positive-definite kernel "the GNS construction" (Remark 1.34) and prove that a kernel's minimal realizations k(x,y) = ⟨Φ(x), Φ(y)⟩ are unique up to a unitary (Cor. 1.35); they also note that commutative states are measures (Ex. 4.28). On a finite sample, two representation matrices with the same Gram matrix differ by an orthogonal transformation, and their centred kernels are equal iff their Procrustes distance is zero ([LIT-250](../literature.d/LIT-250.md) §5.3, §2.2). Harvey, Larsen & Williams prove that the Procrustes distance equals the Bures distance between the centred linear kernels (Thm 1), and that normalized Bures similarity is the cosine of the Riemannian shape distance (Lemma 2). Their eq. 25 applies Uhlmann's theorem: the fidelity is the maximal overlap over all representations consistent with the kernels.

So the kernel is the invariant and the representation is one realization of it — the GNS picture, stated for representations.

## What this does not say

- That orthogonal equivalence is the right notion of sameness for learned models (see the Platonic-convergence claim, which disputes it).
- Anything for nonlinear kernels on the representation, where what is determined is the kernel's feature map, not the representation itself.
- That a model's kernel is determined by anything short of the model; the uniqueness is of realizations of a given kernel.
