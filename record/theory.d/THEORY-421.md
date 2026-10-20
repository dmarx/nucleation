---
number: 421
status: Active
formerly:
- THEORY-tmp2ngm5
title: "In HGCN embeddings of two synthetic 3-ary trees trained for link prediction or node classification, distance from the origin is only a partial reading of hierarchical level: the root is not innermost (distance 1.8–3.3 against a minimum of 1.2–2.4) and level order is recovered for 69–75% of node pairs; a loss built only on pairwise distances leaves the origin arbitrary"
version: 2
history:
- version: 2
  date: '2026-10-20'
  note: >-
    Narrowed and promoted, carrying out the promotion audit's decision for
    THEORY-421 (batch 073, ADR-047 v3 and v4): one study read in full in
    NOTE-669, with Figure 2's inset statistics and Table 9 re-checked
    against arXiv:2306.09118v1. The title names HGCN and the two trees,
    which is all that was measured; the pairwise-distance clause was
    re-derived in the decision file. The general claim for hyperbolic
    models, which the paper asserts without data, moves with the old
    promote_when to THEORY-825.
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
extended_by:
- THEORY-825
---
<!-- inactive-ok-file: THEORY-825 — Proposed; the general claim this measurement was narrowed from, filed to carry it -->
<!-- inactive-ok-file: THEORY-196 — Proposed; other encodings of hierarchy and the paper this one tests, named in Connections, not leaned on -->

# THEORY-421: In HGCN embeddings of two synthetic 3-ary trees trained for link prediction or node classification, distance from the origin is only a partial reading of hierarchical level: the root is not innermost (distance 1.8–3.3 against a minimum of 1.2–2.4) and level order is recovered for 69–75% of node pairs; a loss built only on pairwise distances leaves the origin arbitrary

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

## Note of 2026-10-20: narrowed and promoted

The promotion audit (batch 073) narrowed the title to what [LIT-871](../literature.d/LIT-871.md)
measured and promoted it on that one study, under [ADR-047](../decisions.d/ADR-047.md) v3. [NOTE-669](../notes.d/NOTE-669.md)
read it in full; the review re-checked Figure 2's inset statistics (ROOT
against MIN: 3.1/2.0, 1.8/1.2, 3.3/2.1, 2.7/2.4) and Table 9 (72.5%,
68.9%, 75.3%, 73.7%) against the arXiv PDF. The old title opened with
hyperbolic graph embeddings in general; the paper shows HGCN only and
asserts the rest ("other hyperbolic models have demonstrated comparable
results"). Under [ADR-047](../decisions.d/ADR-047.md) v4 that general claim is not dropped: it is filed
as the Proposed [THEORY-825](THEORY-825.md), which extends this account and inherits
its former promote_when. The pairwise-distance clause is the record's own
and was re-derived step by step: a loss that depends only on pairwise
hyperbolic distances is invariant under every isometry, the isometries act
transitively, so the loss does not fix where the origin lies. It covers
the link-prediction runs; HGCN's classifier reads the tangent space at the
origin and is not pairwise-only.
