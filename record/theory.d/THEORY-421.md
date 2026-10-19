---
number: 421
status: Proposed
formerly:
- THEORY-tmp2ngm5
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
title: "In hyperbolic graph embeddings trained on link-prediction or classification losses, distance from the origin is only a partial reading of hierarchical level: on synthetic trees the root is not innermost and level order is recovered for 69–75% of node pairs, and a loss built on pairwise distances leaves the origin arbitrary"
version: 1
tags:
- representation-learning
- network-science
- anthology-candidate
date: '2026-10-16'
source:
- LIT-871
summary: >-
  Yang, Zhou, Ying, Chen & King (2023), [LIT-871](../literature.d/LIT-871.md), read in [NOTE-669](../notes.d/NOTE-669.md). On two
  synthetic 3-ary trees of eight levels, HGCN leaves the root at hyperbolic
  distance 1.8–3.3 from the origin where the minimum is 1.2–2.4, the
  distances are roughly normal rather than leaf-heavy, and radius orders
  true levels for 69–75% of 5,000 random pairs. Recentring on the
  centroid plus an outward push raises that to 75–84%. The diagnosis rests
  on one architecture, two synthetic trees and one table without variance,
  and the paper does not separate a real failure to order levels from the
  origin's arbitrariness under losses that see only pairwise distances.
---
<!-- inactive-ok-file: THEORY-189 THEORY-196 — Proposed; other encodings of hierarchy and the paper this one tests, named in Connections, not leaned on -->

# THEORY-421: In hyperbolic graph embeddings trained on link-prediction or classification losses, distance from the origin is only a partial reading of hierarchical level: on synthetic trees the root is not innermost and level order is recovered for 69–75% of node pairs, and a loss built on pairwise distances leaves the origin arbitrary

## Source

Yang, Zhou, Ying, Chen & King (2023), [LIT-871](../literature.d/LIT-871.md) (ICML 2023), read in full in
[NOTE-669](../notes.d/NOTE-669.md).

## What was actually shown

**The assumption tested.** Hyperbolic embedding methods train on losses
that never mention the hierarchy: a softmax over hyperbolic distances, a
cross-entropy for node classes, a Fermi–Dirac link likelihood. A
hierarchy's root near the origin and its levels further out is expected
to arise by itself, after Krioukov et al.'s placement of level r at radius
proportional to r. The paper measures it with the hyperbolic distance of
each node to the origin (HDO), read as level.

**The trees.** Two synthetic 3-ary trees, eight levels, 1,093 nodes, with
labels following the tree two ways (by top-level subtree, homophily 0.998;
by level, homophily 0.018).

**Position (§3.2, Fig. 2).** HGCN for link prediction or node
classification puts the root at HDO 1.8–3.3 while the minimum is 1.2–2.4.
The HDO distribution is roughly normal, where a tree's level counts would
put most nodes far out.

**Level order (Table 9).** Of 5,000 random node pairs, the fraction whose
HDO order matches their true level order is 72.5% and 68.9% at dimension
16 and 75.3% and 73.7% at 256. With recentring on the hyperbolic centroid
and a loss rewarding a large HDO-weighted mean HDO, it is 75.4–83.5%.

**What could have come out otherwise.** The root could have sat at the
minimum and the order could have been near complete. Neither held.

## What this does not say

- **Why the root is off-centre.** A translation of the whole embedding
  changes no pairwise distance, so under a loss built only on pairwise
  hyperbolic distances the origin is arbitrary ([NOTE-669](../notes.d/NOTE-669.md), Key insight).
  How much of the diagnosis survives recentring alone is not separated.
  The ablation's alignment-only column hints that on the most tree-like
  data recentring is most of it.
- **That the fix recovers hierarchy.** The outward push uses each node's
  own current HDO as its weight, and the root is the centroid, so it
  amplifies whatever radial order training produced. Its largest
  benchmark gains are on Citeseer and Cora, the least tree-like graphs,
  which the authors credit to class separation. On the real graphs levels
  are never measured.
- **That other hyperbolic models behave alike.** Asserted, not shown;
  Fig. 2 is HGCN only.
- **That radius is the only encoding of hierarchy.** Angular containment
  and entailment cones ([THEORY-189](THEORY-189.md)) are not considered.
- **Anything about attribute lattices.** The hierarchies are graph trees,
  not implication among attributes.

## Connections

- **[QUESTION-025](../questions.d/QUESTION-025.md).** Not an answer. The caution it carries applies to any
  answer: a space suited to a hierarchy does not show that a trained
  representation in it holds the hierarchy, which has to be measured on
  data with known levels.
- **Ganea et al. ([LIT-879](../literature.d/LIT-879.md), [THEORY-566](THEORY-566.md))** is among the works this paper
  says assumed the radial layout would arise by itself.
- **[THEORY-196](THEORY-196.md)** gives the near-isometric tree embedding the geometry makes
  possible. This account says task training realises it only partly.
