---
number: 2188
status: Proposed
formerly:
- THEORY-tmpvwv5n
title: 'InfoNCE converges to a convex free energy'
statement: >-
  Cai, Zhang, Liu and Shi show that as the number of negatives grows InfoNCE
  and its gradient converge to a deterministic energy over the
  representation's distribution on a compact embedding manifold, which for
  one modality is a strictly convex free energy, alignment potential over
  temperature minus entropy, with a unique Gibbs minimizer, and for
  symmetric two-modality InfoNCE carries a negative symmetric KL divergence
  between the modalities that makes each one's density a barrier for the
  other
promote_when: >-
  A second reading or an independent derivation confirms, under the stated
  assumptions (i.i.d. negatives, constant kernel volume, density floors),
  the large-batch value and gradient consistency of Theorem 3.1, the strict
  convexity and Gibbs minimizer of Proposition 3.1, and the negative
  symmetric-KL term and concave coordinate map of Definition 4.3 and
  Proposition 4.1.
version: 1
tags:
- representation-learning
- learning-theory
- information-theory
date: '2026-11-22'
source:
- LIT-2975
summary: >-
  Cai and colleagues, [LIT-2975](../literature.d/LIT-2975.md), read in [NOTE-2277](../notes.d/NOTE-2277.md). InfoNCE's
  large-batch limit is a passive, variational energy over the
  representation's law: one free energy with a Gibbs equilibrium for one
  modality, one joint energy with a repulsive cross-modal term for two.
  Grounds [CLAIM-798](../claims.d/CLAIM-798.md)'s weak reading and gives nothing toward its strong one
  ([ARG-189](../arguments.d/ARG-189.md)).
---
<!-- inactive-ok-file: CLAIM-798 ARG-189 — Proposed or new; the claim this reading grounds and the argument for it -->

# THEORY-2188: InfoNCE converges to a convex free energy

## Source

Yichao Cai, Zhen Zhang, Yuhang Liu and Javen Qinfeng Shi, "The Geometric
Mechanics of Contrastive Representation Learning: Alignment Potentials,
Entropic Dispersion, and Cross-modal Divergence", ICML 2026, arXiv
2601.19597, [LIT-2975](../literature.d/LIT-2975.md), read in [NOTE-2277](../notes.d/NOTE-2277.md).

## What was actually shown

- Theorem 3.1: large-batch consistency in value (up to log(N V_κ(τ))) and
  in gradient.
- Proposition 3.1: the unimodal intrinsic energy "is strictly convex on
  its effective domain and has the unique Gibbs-form minimizer".
- §1: "uniformity" is "not ... a global force opposing alignment, but ...
  entropy-driven spreading inside the alignment basin."
- Definition 4.3, Proposition 4.1, Theorem 4.2: the symmetric multimodal
  energy subtracts a symmetric KL divergence between the modalities'
  densities; its coordinate map is concave; the divergence survives τ → 0+
  as "an explicit separation-inducing contribution".

What could have failed: the large-batch limit could have depended on the
batch's composition, or the multimodal objective could have reduced to two
independent unimodal ones.

## What this does not say

- Nothing about training trajectories: it is "the geometry of the
  objective rather than the trajectory of a specific optimization
  algorithm".
- Not an attraction–repulsion energy for one modality; repulsion is
  population-level and only between modalities.
- No collapse regime: singular measures are set aside.
- Its "bifurcation" is a difference between two objectives, not a
  transition in a control parameter.
