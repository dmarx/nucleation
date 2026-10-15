---
status: Active
status_note: >-
  read in full 2026-10-15 (NOTE for LIT-tmpllfsb) from the authors' arXiv preprint
  (arxiv.org/abs/2310.19126v1, the only version, which carries the NeurIPS 2023
  line and is the camera-ready text), including Appendices A–C. Worth reading as
  the first worst-case analysis of graph-based nearest neighbour indexes: DiskANN
  built by "slow preprocessing" (every point pruned against all others with α >
  1, naively O(n³)) is proved to give a ((α+1)/(α−1) + ε)-approximate neighbour
  in O(log_α(∆/((α−1)ε))) greedy steps of cost O((4α)^d log ∆), for doubling dimension
  d and aspect ratio ∆, with both the ratio and the ∆ dependence shown tight; for
  DiskANN as implemented, HNSW, NSG and seven others, two-dimensional constructed
  instances made recall@5 zero or near zero until the search queue held about 10%
  of the points, an empirical result with no theorem behind it for those algorithms.
  For [CLAIM-310](../claims.d/CLAIM-310.md), with [LIT-tmp7dffg](LIT-tmp7dffg.md), it shows on one fixed point set that the graph
  built over it, not the points, decides between finding the nearest neighbour in
  two steps and scanning a tenth of the collection, and that the guarantee rests
  on a stated property of the arrangement (from every point, some edge gets α times
  closer to any target); for [QUESTION-114](../questions.d/QUESTION-114.md) it is a case where an expensive build
  buys a worst-case guarantee, without a measured break-even or upkeep.
title: 'Worst-case Performance of Popular Approximate Nearest Neighbor Search Implementations:
  Guarantees and Limitations'
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Filed, not read. Citation checked on 2026-10-15: NeurIPS 2023. arXiv v1 submitted
    29 October 2023. Not held in the Anthology of the SOTA: a grep of its record/
    (clone of 2026-10-15, commit d1573d2) for the title and authors found nothing.
    Read the same day (NOTE-tmpak6ah).
tags:
- information-retrieval
- databases
- anthology-candidate
date: '2026-10-15'
published: '2023-10-29'
arxiv: '2310.19126'
first_author: Indyk
keywords: []
implementations: []
summary: >-
  Indyk and Xu (2023), NeurIPS 2023. For DiskANN's "slow preprocessing" graph (each
  point linked to the points that survive α-pruning of all other points, naively
  O(n³) time), greedy search from any start with no backtracking reaches a ((α+1)/(α−1)
  + ε)-approximate nearest neighbour in O(log_α(∆/((α−1)ε))) steps, each costing
  O((4α)^d log ∆) for doubling dimension d and aspect ratio ∆; the ratio is tight
  and the dependence on ∆ cannot be replaced by log n. For DiskANN with its practical
  "fast preprocessing", HNSW, NSG and seven other graph indexes, the paper constructs
  two-dimensional point sets (constant doubling dimension) on which, in experiments
  with the authors' code at the authors' recommended parameters, the search queue
  must hold about 10% of the points before recall@5 becomes non-zero or the approximation
  ratio becomes reasonable. The linear lower bounds are empirical, for one query
  per constructed instance, with an informal Ω(n/R) argument for fast-preprocessing
  DiskANN; no theorem bounds HNSW or NSG.
---

# LIT-tmpllfsb: Worst-case Performance of Popular Approximate Nearest Neighbor Search Implementations: Guarantees and Limitations

Indyk, P. and Xu, H. (2023). Worst-case performance of popular approximate nearest neighbor search implementations: guarantees and limitations. In *Advances in Neural Information Processing Systems 36*, pp. 66239–66256. DOI 10.52202/075280-2891

## Key takeaways

Read in full ([NOTE-tmpak6ah](../notes.d/NOTE-tmpak6ah.md)). For DiskANN's "slow preprocessing" graph (each point linked to the points that survive α-pruning of all other points, naively O(n³) time), greedy search from any start with no backtracking reaches a ((α+1)/(α−1) + ε)-approximate nearest neighbour in O(log_α(∆/((α−1)ε))) steps, each costing O((4α)^d log ∆) for doubling dimension d and aspect ratio ∆; the ratio is tight and the dependence on ∆ cannot be replaced by log n. For DiskANN with its practical "fast preprocessing", HNSW, NSG and seven other graph indexes, the paper constructs two-dimensional point sets (constant doubling dimension) on which, in experiments with the authors' code at the authors' recommended parameters, the search queue must hold about 10% of the points before recall@5 becomes non-zero or the approximation ratio becomes reasonable. The linear lower bounds are empirical, for one query per constructed instance, with an informal Ω(n/R) argument for fast-preprocessing DiskANN; no theorem bounds HNSW or NSG.

## Why this is here

[CLAIM-310](../claims.d/CLAIM-310.md), with [LIT-tmp7dffg](LIT-tmp7dffg.md) and [LIT-tmp08vve](LIT-tmp08vve.md): proves a guarantee only for the slow-preprocessing DiskANN graph, at about cubic build cost. For HNSW, NSG and the fast DiskANN build, linear-time behaviour is shown on constructed instances, not proved; the authors cannot prove guarantees for them.
