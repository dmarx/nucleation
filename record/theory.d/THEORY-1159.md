---
number: 1159
status: Proposed
formerly:
- THEORY-tmpz6ryi
promote_when: >-
  An ablation in which a joint multi-marginal coupling and independently
  fitted pairwise couplings share the same cost, the same anchors and the
  same search space, scored on held-out correspondences on two kinds of
  data: data whose true correspondences are transitive, and data where
  some are not, such as maps through an intermediate network that loses or
  merges distinctions. The account is supported if the joint fit wins on
  the first kind without losing pairwise accuracy on the second; it is
  weakened if it gains only where the truth is consistent by construction.
  A further comparison of HOT against other methods on consistent
  benchmarks does not settle it.
title: 'Aligning three networks jointly, through one multi-marginal fused Gromov–Wasserstein coupling with an anchor-based random-walk cost and a cluster decomposition, finds held-out correspondences better than pairwise and existing multi-network methods, in both pairwise and whole-tuple hits, on benchmarks whose true correspondences are consistent across the three networks by construction; whether the joint coupling itself is the cause is not separated from the new cost and the clustering'
version: 1
tags:
- network-science
- mathematics
date: '2026-10-29'
source:
- LIT-1814
summary: >-
  Zeng et al. (2024), [LIT-1814](../literature.d/LIT-1814.md), §5 and Appendix C, read in
  [NOTE-1334](../notes.d/NOTE-1334.md). Reported as plots against 13 baselines on ER, Douban,
  DBLP and ACM triples, with 10% anchors and 90% held out. Proposed: the
  result is empirical, its ground truth is a consistent set of node
  triples, and no ablation holds the cost and the clustering fixed while
  changing joint for pairwise fitting.
---

# THEORY-1159: Aligning three networks jointly, through one multi-marginal fused Gromov–Wasserstein coupling with an anchor-based random-walk cost and a cluster decomposition, finds held-out correspondences better than pairwise and existing multi-network methods, in both pairwise and whole-tuple hits, on benchmarks whose true correspondences are consistent across the three networks by construction; whether the joint coupling itself is the cause is not separated from the new cost and the clustering

## Source

Zeng et al. (2024), [LIT-1814](../literature.d/LIT-1814.md), §5 (pp. 5–7), Appendices C–D (pp.
12–15) of arXiv 2310.04470v2; read in [NOTE-1334](../notes.d/NOTE-1334.md).

## What was actually shown

**Design.** Three networks per benchmark: ER-500 (each a noisy permutation
of one base graph, p. 15), Douban-230, DBLP-500/1000 and, with 17
attributes, ACM(A) and DBLP(A) (Table 4, p. 14). Ten random splits, 10%
of the true node triples as anchors and 90% for testing (p. 5). Thirteen
baselines: consistency-, embedding- and OT-based; the pairwise ones are
combined into a tensor by multiplying their three alignment matrices
(p. 5). Metrics: pairwise Hits@K, high-order Hits@K (the whole triple in
the top K) and MRR (p. 5).

**Result.** HOT is reported best "in most cases" (p. 5), by "at least
12.0% on plain networks in terms of high-order Hits@10" (p. 1), with the
larger margins on plain networks and on high-order metrics (p. 5). Read
off the plots, roughly: on ER-500 pairwise Hits@K near 99% and high-order
near 80%. It also wins on pairwise hits, so on these data the joint fit
did not cost pairwise accuracy. Results for larger DBLP graphs (Tables
1–2) have no baseline.

**What could have failed.** The joint fit could have lost pairwise
accuracy to its consistency constraint, or a pairwise method with a good
cost could have matched it. Neither happened against these baselines.

## What this does not say

- **That joint fitting is the cause.** HOT introduces three things at once:
  the RWR cost from shared anchors, the cluster decomposition, and the
  joint coupling. The paper attributes the high-order gains to joint
  alignment (p. 5) without an ablation. On attributed DBLP the plain
  version does nearly as well, which it credits to the cost (p. 13).
- **That consistency never loses local distinctions.** Every benchmark's
  truth is a consistent set of triples, so a consistency constraint cannot
  be wrong there. The record's interest ([CLAIM-496](../claims.d/CLAIM-496.md),
  [QUESTION-319](../questions.d/QUESTION-319.md)) is in data where it can be.
- **Anything about independently fitted pairwise alignments composed and
  compared with direct ones.** The baselines' product rule never composes
  maps.
- **Exact values.** The main results are plots; numbers above are
  readings.
