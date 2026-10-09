---
status: Proposed
promote_when: >-
  What would settle it is the proof checked independently of this reading,
  or the same result found stated and proved in the literature on
  symmetry-induced constraints or equivariant dynamics, together with a
  check of the local form: that two neurons can coincide after one step
  only when η times the update's Lipschitz ratio across their swap is at
  least 1. It is refuted by a permutation-equivariant update with ηK < 1
  under which two distinct neurons coincide after one step. Experiments
  that track Betti numbers or other scale-dependent shape summaries of the
  neuron cloud cannot settle it either way, since the claim says nothing
  about them.
title: 'Under a permutation-equivariant update whose map is K-Lipschitz, coincident neurons stay coincident at every step size, and at step size below 1/K distinct neurons cannot merge in finitely many steps'
version: 1
tags:
- loss-landscapes
- mathematics
date: '2026-10-09'
source:
- LIT-tmpacvdl
summary: >-
  Yang, Poggio, Chuang and Ziyin (2025), [LIT-tmpacvdl](../literature.d/LIT-tmpacvdl.md), read in
  [NOTE-tmp571ty](../notes.d/NOTE-tmp571ty.md). If an update commutes with permuting neurons (GD, SGD or
  Adam on a permutation-symmetric loss) and its map is K-Lipschitz, one
  step of size η changes every pairwise neuron distance by a factor in
  [1 − ηK, 1 + ηK]. This is a proved constraint on trajectories. It does
  not say that training simplifies above 1/K, that neurons never merge in
  the limit, or that any scale-dependent shape of the neuron cloud is
  preserved.
---

<!-- inactive-ok-file: THEORY-039 — Proposed; the record's account of later training phases, named for what this does not settle -->

# THEORY-tmpmh1ao: Under a permutation-equivariant update whose map is K-Lipschitz, coincident neurons stay coincident at every step size, and at step size below 1/K distinct neurons cannot merge in finitely many steps

## Source

Yang, Poggio, Chuang and Ziyin (2025), [LIT-tmpacvdl](../literature.d/LIT-tmpacvdl.md), Lemmas 1–4, Theorem 1
and Propositions 1–3, as read in [NOTE-tmp571ty](../notes.d/NOTE-tmp571ty.md).

## What was actually shown

The setting is a collection of neuron vectors xᵢ ∈ ℝᴰ, updated by
xᵢ′ = xᵢ + ηUᵢ(X). The update is equivariant, PU(X) = U(PX) for every
finitary permutation P. For gradient descent and for Adam, the paper proves
this follows from a permutation-symmetric loss. Two consequences are proved
in a few lines each, and the proofs were followed here:

- **No splitting, at any step size.** If xᵢ = xⱼ, the swap of i and j fixes
  X, so Uᵢ(X) = Uⱼ(X) and the two stay equal (Lemma 1).
- **Bounded relative motion.** If ‖U(X) − U(Y)‖ ≤ K‖X − Y‖, apply it to Y
  = PX with P the swap of i and j. This gives
  ‖Uᵢ − Uⱼ‖ ≤ K‖xᵢ − xⱼ‖, hence
  (1 − ηK)‖xᵢ − xⱼ‖ ≤ ‖xᵢ′ − xⱼ′‖ ≤ (1 + ηK)‖xᵢ − xⱼ‖ (Lemma 2). For ηK < 1,
  distinct neurons stay distinct after any finite number of steps, and the
  induced map on the neuron set is a bi-Lipschitz homeomorphism
  (Theorem 1(iii)).

The proof uses K only through the one pair (X, PX). So the reader's local
form also holds: neurons i and j can coincide after a step only if
η‖U(X) − U(PX)‖/‖X − PX‖ ≥ 1. For gradient descent this ratio is the
averaged Hessian acting on the antisymmetric direction that moves i and j
oppositely, and it is bounded by, but can be far below, λ_max. Equivalently,
X ↦ X + ηU(X) is injective when ηK < 1. Equivariance turns injectivity on
the weights into injectivity on the neurons.

What could have come out otherwise: an equivariant, K-Lipschitz rule with
ηK < 1 that maps two distinct neurons to one point. The argument rules it
out.

## What this does not say

- **That training simplifies above 1/K.** Above the threshold the guarantee
  lapses. Nothing shows that neurons then merge, or that the network loses
  expressivity. The paper's "topological breakdown" and its two-phase
  picture with the edge of stability are interpretation. [THEORY-039](THEORY-039.md), on
  later training phases, is not settled by it.
- **That neurons never merge at small step sizes.** The lower bound
  compounds to (1 − ηK)ᵗ. Neurons may converge to each other as t → ∞ at
  any step size. Only coincidence after finitely many steps is excluded.
- **That the shape of the neuron cloud is preserved.** For finitely many
  neurons a homeomorphism of the neuron set is just a bijection. Genus,
  loops and the Betti numbers of a point cloud at a fixed scale can all
  change under bi-Lipschitz steps whose distortion compounds. The paper's
  experiments measure exactly such quantities. The changes they report at
  large step sizes are fragmentation, which this result does not predict.
- **That 1/λ_max is where a network's neurons start to merge.** A global K
  does not exist for typical networks. The local constant that matters is
  the curvature across a particular swap, not the top Hessian eigenvalue.
  For Adam no K has been derived.
- **Anything about the weights within a neuron.** The result constrains
  distances between neurons. It does not constrain how far each one
  travels, or the function the network computes.
