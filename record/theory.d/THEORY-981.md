---
number: 981
status: Active
formerly:
- THEORY-tmpdxhxm
title: 'When a data distribution is unchanged by a group of orthogonal transformations under which a network is equivariant, the weights fixed by that group form a subspace that population gradient descent never leaves; for attention-only transformers on block-list inductive tasks, with fixed orthogonal write maps, Musat, Pimentel, Zucchet and Hofmann compute this subspace as the span of a few elementary token and position actions composed through the heads, and an elementwise optimizer such as sign descent keeps it only when those actions are aligned with the parameter coordinates'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed Active from NOTE-1177. The confinement is the paper's Theorem
    1 and Corollary 1. Its general form, the fixed-point argument, is
    re-derived below step by step, and the one-layer token and position
    commutants were checked numerically, which meets the condition for
    Active under ADR-047 v2. The explicit multi-layer basis is the paper's
    computation, followed in its proof and not independently re-derived.
    The optimizer clause is the record's, checked numerically; the paper
    does not discuss it.
tags:
- learning-theory
- mathematics
date: '2026-10-26'
source:
- LIT-1530
summary: >-
  Musat et al. (2026), [LIT-1530](../literature.d/LIT-1530.md), read in [NOTE-1177](../notes.d/NOTE-1177.md). Symmetries of
  the data confine population gradient descent to the weights those
  symmetries fix; for their task class and idealized architecture this is
  a subspace whose coordinates are interpretable head actions. It does not
  say the subspace is attractive (the paper proves only invariance), and
  it does not cover minibatch noise beyond expectation, learnable value
  maps (a sketch in the paper), or adaptive optimizers, which keep it only
  when the basis is coordinate-aligned.
---
<!-- inactive-ok-file: THEORY-783 THEORY-802 CLAIM-263 — Proposed; accounts and claims this one is set beside, cited as open -->

# THEORY-981: When a data distribution is unchanged by a group of orthogonal transformations under which a network is equivariant, the weights fixed by that group form a subspace that population gradient descent never leaves; for attention-only transformers on block-list inductive tasks, with fixed orthogonal write maps, Musat, Pimentel, Zucchet and Hofmann compute this subspace as the span of a few elementary token and position actions composed through the heads, and an elementwise optimizer such as sign descent keeps it only when those actions are aligned with the parameter coordinates

## Source

Musat, Pimentel, Zucchet and Hofmann (2026), arXiv:2607.11875,
[LIT-1530](../literature.d/LIT-1530.md), read in full in [NOTE-1177](../notes.d/NOTE-1177.md): §3 (Theorem 1, Corollary 1)
and Appendix A.3 (the proof), with Appendix B for general relations. The
general statement and the optimizer check below are the record's.

## What was actually shown

**The general argument.** Let a group G act orthogonally on the weights,
W ↦ g·W, and suppose the expected loss is invariant:
F(g·W) = F(W) for all g, with F(W) = E_x L(W; x). Differentiating,
∇F(g·W) = g·∇F(W), since g is orthogonal. If W is fixed by every g, then
∇F(W) = ∇F(g·W) = g·∇F(W), so the gradient is fixed too. The fixed set
Fix(G) is a linear subspace, so a step W − η∇F(W) stays in it, and so does
the flow. Nothing in this needs the loss to be convex or the dynamics to be
slow.

**Where the invariance comes from in the paper.** Two transformations of
the input leave the data distribution unchanged: an association-preserving
permutation of the common tokens (E^(t)) and a shift of every block's
positional offsets (E^(p)), Assumptions 1–2. With fixed orthogonal write
maps V^(ℓ) (Assumption 6), the paper defines layer rotations
Λ^(ℓ) = Λ^(ℓ−1) + V^(ℓ)Λ^(ℓ−1)V^(ℓ)ᵀ, under which the network is
equivariant: transforming the input and conjugating each W^(ℓ) by
Λ^(ℓ−1) leaves attention scores, and so the loss, unchanged ((33)–(38)).
Together with distributional invariance this is F(g·W) = F(W) above. The
paper's S is then the commutant: the matrices commuting with every
Λ^(ℓ−1).

**The commutant, checked at one layer.**
- Tokens: the matrices commuting with every pairing-preserving
  permutation of 2k tokens. The record solved WP = PW over the group for
  k = 4 and found a three-dimensional solution space, span{I, C, 11ᵀ}, the
  paper's c₁11ᵀ + c₂I + c₃C. With centred embeddings 11ᵀ acts as zero on
  the token subspace.
- Positions: the matrices commuting with independent rotations in m
  frequency planes. The solution space had dimension 2m, a scaled rotation
  aI + bJ in each plane, which the paper further reduces to polynomials in
  M using the structure of sinusoidal embeddings.
- A generic invariant loss averaged over the token group had its gradient
  at W = 0.7I + 0.3C inside span{I, C, 11ᵀ} to a residual of 3.5 × 10⁻⁹
  against a norm of 2.1.

**The optimizer clause (the record's).** The argument uses only that the
update is equivariant, (g·W) ↦ g·(update of W). Gradient descent is
equivariant under every orthogonal g. An elementwise update, such as sign
descent or Adam's m/√v, is equivariant only under signed permutations of
the coordinates. Checked: with token embeddings aligned with the
coordinates, sign(G) stayed in span{I, C, 11ᵀ} to 2 × 10⁻¹⁶; with random
orthonormal embeddings, G stayed in the rotated span to 1.7 × 10⁻⁹ but
sign(G) had a relative residual of 0.69. A scaled rotation in a
coordinate-aligned position plane kept its form under sign, while the same
plane embedded in a randomly rotated 8-dimensional stream did not
(relative residual 0.62).

**What could have failed.** The gradient at a symmetric point could have
had a symmetric-breaking component if the loss were not invariant for
every W, or if the network were equivariant only at points of S. Neither
happens with fixed orthogonal write maps. With learnable ones it is open.

## What this does not say

- **Not that the subspace attracts.** Trajectories that begin off it are
  not shown to approach it. The paper says so ("We do not prove the
  stronger property that the IMIR is attractive"), and shows alignment
  only empirically.
- **Not for each minibatch.** A single batch is not symmetric, so SGD is
  confined only in expectation.
- **Not for Adam or AdamW in general.** By the clause above, an adaptive
  optimizer leaves the subspace unless its basis is coordinate-aligned. The
  paper's own §5 trains with AdamW and finds the projection faithful, so
  the departure may be small there; it is not measured.
- **Not for real transformers.** Learnable value maps are "a sketch rather
  than a proven claim" (A.4); the residual width must grow as Θ(H^L); the
  embeddings are fixed and orthonormal.
- **Not that the subspace is small at depth.** It has (H + 1)^ℓ action
  products per layer: 28 directions for two layers, 1428 for five.

## Connections

- **[THEORY-253](THEORY-253.md) and [THEORY-783](THEORY-783.md).** The optimizer clause is the rotated
  quadratic's lesson in another setting: whether a sign-based optimizer
  changes the dynamics depends on whether the relevant directions are
  aligned with the coordinates.
- **[THEORY-802](THEORY-802.md).** Here the decomposition into units is fixed by the
  data's symmetry group, which is one way of choosing the decomposition
  [THEORY-802](THEORY-802.md) says interchange interventions alone do not fix.
- **[THEORY-018](THEORY-018.md) and [CLAIM-263](../claims.d/CLAIM-263.md).** Those concern what training leaves
  undetermined: a final-layer representation only up to an invertible
  linear map, and an architecture's parameter symmetries, which a
  comparison must quotient. Here the data's symmetries do the opposite
  work, and fix a basis for the weights, but only inside the paper's
  idealization, where Assumption 5 has already removed the key–query
  gauge.
- **[LIT-1534](../literature.d/LIT-1534.md).** Elhage et al.'s mathematical framework is where the
  two-layer attention-only setting and the QK/OV reading of heads of the
  paper's models come from; its path expansion is [THEORY-988](THEORY-988.md).
