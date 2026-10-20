---
status: Proposed
promote_when: >-
  Level-ordering measured on hierarchies whose levels are known, for
  several hyperbolic architectures and seeds, with variance reported and
  with level decoupled from degree and centrality, before and after
  recentring the embedding on its centroid. The account is supported if
  task-trained embeddings order levels by radius only partly and
  recentring alone does not repair it, and refuted if recentring alone
  brings the ordering close to complete. Benchmark gains from an
  outward-push loss cannot settle it, since the paper's own largest gains
  are on its least tree-like graphs.
title: "Hyperbolic graph embedding models trained on task losses that never mention the hierarchy do not place a tree's root nearest the origin, and their distance from the origin orders hierarchical levels only partly"
version: 1
tags:
- representation-learning
- network-science
- anthology-candidate
date: '2026-10-20'
source:
- LIT-871
extends:
- THEORY-421
summary: >-
  Yang, Zhou, Ying, Chen & King (2023), [LIT-871](../literature.d/LIT-871.md), read in [NOTE-669](../notes.d/NOTE-669.md), assert
  for hyperbolic graph models in general what they measured for HGCN on two
  synthetic trees: the root is not innermost and radius reads level only
  partly. The general form was the lead clause of [THEORY-421](THEORY-421.md) until that
  account was narrowed to the measurement on 2026-10-20 ([ADR-047](../decisions.d/ADR-047.md) v4); it is
  filed here so that it stays a thesis evidence can confirm or reject.
---
<!-- inactive-ok-file: THEORY-196 — Proposed; the tree-embedding result this is set beside, named, not leaned on -->

# THEORY-tmp5lbcx: Hyperbolic graph embedding models trained on task losses that never mention the hierarchy do not place a tree's root nearest the origin, and their distance from the origin orders hierarchical levels only partly

## Source

Yang, Zhou, Ying, Chen & King (2023), [LIT-871](../literature.d/LIT-871.md) (ICML 2023), read in full in
[NOTE-669](../notes.d/NOTE-669.md). The general claim is the paper's: after Figure 2 it says that
"other hyperbolic models have demonstrated comparable results", without
showing them.

## What was actually shown

What supports it is [THEORY-421](THEORY-421.md): for HGCN trained for link prediction or
node classification on two synthetic 3-ary trees of eight levels, the root
sits at distance 1.8–3.3 from the origin against a minimum of 1.2–2.4, and
distance from the origin orders 69–75% of 5,000 random node pairs by level
(Figure 2; Table 9). One architecture, two trees, no variance. The general
thesis would have been in trouble if HGCN had put the root at the minimum
and ordered levels nearly completely; it did not.

A reason to expect it more widely is the record's own: a loss built only on
pairwise hyperbolic distances is unchanged by any isometry, so it does not
fix where the origin lies relative to the embedding ([THEORY-421](THEORY-421.md), re-derived
in the promotion audit). Losses that read features at the origin's tangent
space, as HGCN's classifier does, are not covered by that argument.

## What this does not say

- **That other hyperbolic models were measured.** The paper asserts it;
  none is shown. Poincaré embeddings, hyperbolic attention networks and
  entailment-cone models ([THEORY-189](THEORY-189.md)), which encode hierarchy by angle as
  well as radius, are untested here.
- **That recentring fails.** How much of the gap is only the arbitrary
  origin, which recentring on the centroid would remove, is not separated
  in the paper. The promotion condition asks for exactly that.
- **That the paper's fix recovers hierarchy.** Its outward-push loss gains
  most on the least tree-like benchmarks, and levels are never measured on
  the real graphs.

## Connections

- [THEORY-421](THEORY-421.md) is the measurement this generalizes, and is Active.
- [THEORY-196](THEORY-196.md) gives the near-isometric tree embedding the geometry allows;
  this thesis says task training does not realise it by itself.
- [QUESTION-025](../questions.d/QUESTION-025.md): a space suited to a hierarchy does not show that a trained
  representation in it holds the hierarchy.
