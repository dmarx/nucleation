---
status: Proposed
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
- LIT-tmpdc8x2
- LIT-tmpy9oi9
- LIT-tmpmford
- LIT-241
summary: >-
  Harvey, Larsen & Williams (2023), [LIT-tmpdc8x2](../literature.d/LIT-tmpdc8x2.md), Thm 1; Jorgensen & Tian,
  [LIT-tmpy9oi9](../literature.d/LIT-tmpy9oi9.md), Remark 1.34 and Cor. 1.35, which name the
  kernel-to-Hilbert-space construction as GNS and prove its minimal
  realizations unique up to a unitary. This is the GNS connection the owner
  asked about, stated.
extended_by:
- THEORY-tmp4sf4k
- THEORY-tmpqq4es
---
<!-- inactive-ok-file: LIT-tmpy9oi9 — Deferred: filed and skimmed on 2026-09-26 while pursuing the owner's Riesz/Radon–Nikodym/GNS question; the theories citing it are Proposed until it is read closely -->
<!-- inactive-ok-file: LIT-tmpdc8x2 — Deferred: filed and skimmed on 2026-09-26 while pursuing the owner's Riesz/Radon–Nikodym/GNS question; the theories citing it are Proposed until it is read closely -->
<!-- inactive-ok-file: LIT-tmpmford — Deferred: filed and skimmed on 2026-09-26 while pursuing the owner's Riesz/Radon–Nikodym/GNS question; the theories citing it are Proposed until it is read closely -->

# THEORY-tmpcawyi: A representation is determined by its kernel up to an orthogonal transformation, and the rotation-aligned distance between two representations equals the Bures distance between their kernels

## Source

Harvey, Larsen & Williams (2023), [LIT-tmpdc8x2](../literature.d/LIT-tmpdc8x2.md), §2.2, §5.3, Thm 1, Lemma 2, eq. 25. Jorgensen & Tian, [LIT-tmpy9oi9](../literature.d/LIT-tmpy9oi9.md), Remark 1.34, Cor. 1.35, Ex. 4.28. Supporting: Kornblith et al. (2019), [LIT-tmpmford](../literature.d/LIT-tmpmford.md), §2.2 (the case for orthogonal invariance); the GNS statement, [LIT-241](../literature.d/LIT-241.md).

## What was actually shown

Jorgensen & Tian call the construction of a Hilbert space from a positive-definite kernel "the GNS construction" (Remark 1.34) and prove that a kernel's minimal realizations k(x,y) = ⟨Φ(x), Φ(y)⟩ are unique up to a unitary (Cor. 1.35); they also note that commutative states are measures (Ex. 4.28). On a finite sample, two representation matrices with the same Gram matrix differ by an orthogonal transformation, and their centred kernels are equal iff their Procrustes distance is zero ([LIT-tmpdc8x2](../literature.d/LIT-tmpdc8x2.md) §5.3, §2.2). Harvey, Larsen & Williams prove that the Procrustes distance equals the Bures distance between the centred linear kernels (Thm 1), and that normalized Bures similarity is the cosine of the Riemannian shape distance (Lemma 2). Their eq. 25 applies Uhlmann's theorem: the fidelity is the maximal overlap over all representations consistent with the kernels.

So the kernel is the invariant and the representation is one realization of it — the GNS picture, stated for representations.

## What this does not say

- That orthogonal equivalence is the right notion of sameness for learned models (see the Platonic-convergence claim, which disputes it).
- Anything for nonlinear kernels on the representation, where what is determined is the kernel's feature map, not the representation itself.
- That a model's kernel is determined by anything short of the model; the uniqueness is of realizations of a given kernel.
