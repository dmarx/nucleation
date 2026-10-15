---
status: Active
title: "A nearest-neighbour graph built by pruning each point's links against all other points with a factor α > 1, so that from every point some link is α times closer to any other point, lets greedy search from any start reach a ((α+1)/(α−1) + ε)-approximate nearest neighbour in O(log_α(∆/((α−1)ε))) steps of cost O((4α)^d log ∆), for doubling dimension d and aspect ratio ∆; the ratio is tight and the dependence on ∆ cannot be replaced by one on n, and the build takes O(n³) time done naively"
version: 1
tags:
- databases
- information-retrieval
date: '2026-10-15'
source:
- LIT-tmpllfsb
summary: >-
  Indyk and Xu (2023), [LIT-tmpllfsb](../literature.d/LIT-tmpllfsb.md), read in [NOTE-tmpak6ah](../notes.d/NOTE-tmpak6ah.md). Proved for
  DiskANN's "slow preprocessing" build, not the build DiskANN implements.
  The guarantee rests on one property of the graph (α-shortcut
  reachability, α > 1), gives a constant approximation, not exact search,
  is logarithmic in the aspect ratio ∆, which can exceed n by far, and has
  a per-step cost exponential in the doubling dimension. HNSW and NSG
  prune with α = 1 and are not covered.
supports:
- CLAIM-310
---

# THEORY-tmpry4qh: A nearest-neighbour graph built by pruning each point's links against all other points with a factor α > 1, so that from every point some link is α times closer to any other point, lets greedy search from any start reach a ((α+1)/(α−1) + ε)-approximate nearest neighbour in O(log_α(∆/((α−1)ε))) steps of cost O((4α)^d log ∆), for doubling dimension d and aspect ratio ∆; the ratio is tight and the dependence on ∆ cannot be replaced by one on n, and the build takes O(n³) time done naively

## Source

Indyk and Xu (2023), [LIT-tmpllfsb](../literature.d/LIT-tmpllfsb.md), NeurIPS 2023 (arXiv 2310.19126v1),
read in full in [NOTE-tmpak6ah](../notes.d/NOTE-tmpak6ah.md): Section 3 (Lemmas 3.2–3.3, Theorems 3.4–3.6)
and Appendix B (proof of Theorem 3.5).

## What was actually shown

**The build.** For each point v, sort all other points by distance from
v; keep the nearest, delete every w that some kept u has α·D(u, w) <
D(v, w), and repeat. Linking v to what is kept makes the graph
α-shortcut reachable: for any p and q, either p links to q or p links to
some p′ with α·D(p′, q) ≤ D(p, q) (Lemma 3.2). In a set of doubling
dimension d, at most O((4α)^d log ∆) points survive (Lemma 3.3). The
paper notes that a naive implementation takes O(n³) time; in its
experiments the build took "several hundred hours" beyond 10⁵ points.

**The guarantee (Theorem 3.4).** Greedy search with no backtracking
(queue length 1), from any start, reaches a ((α+1)/(α−1) + ε)-approximate
nearest neighbour in O(log_α(∆/((α−1)ε))) steps. Each step shrinks the
distance by a factor α, up to an additive term in the true neighbour's
distance. For α = 2 the ratio is 3 + ε. When the true neighbour is much
closer to the query than the closest pair of data points, the exact
neighbour is reached in O(log_α ∆) steps.

**Tightness.** Theorem 3.6: for any α > 1, n + 2 points in the plane
under ℓ₁ on which search scans at least n vertices before beating ratio
(α+1)/(α−1). Theorem 3.5: n points on a line with ∆ = O(α^n) on which
search needs Ω(log ∆) steps, which there is Ω(n), so log ∆ cannot be
replaced by log n.

## What this does not say

- **That DiskANN as used has this guarantee.** DiskANN implements a
  "fast preprocessing" build that prunes only against points found by
  searching the graph under construction; it is not covered, and
  [THEORY-tmpc25xn](THEORY-tmpc25xn.md) describes instances on which it fails.
- **That HNSW or NSG have it.** They prune with α = 1. The paper says "we
  cannot prove query performance guarantees similar to the ones above";
  that is the absence of a proof, not a proof of failure.
- **That search is polylogarithmic in n.** It is logarithmic in the
  aspect ratio, and the two are incomparable. The paper reports ∆ near 20
  for MNIST, but Theorem 3.5's instance has ∆ exponential in n.
- **That high-dimensional data are covered.** The step cost grows as
  (4α)^d in the doubling dimension, and the result is an approximation
  ratio, not exact search, except in the near-query case.
- **That the expensive build is worth it.** No cost of building is
  weighed against query savings, and points are not inserted after the
  build.

## Connections

- [CLAIM-310](../claims.d/CLAIM-310.md) (arrangements, not descriptions): the guarantee is a property
  of how the points are linked, stated exactly, and on the instance of
  [THEORY-tmpc25xn](THEORY-tmpc25xn.md) this graph finds the exact neighbour in two steps where
  other builds over the same points scan a tenth of them.
- [THEORY-tmpdllj7](THEORY-tmpdllj7.md) (Kleinberg): both say local search is fast when, from
  every point, some link makes geometric progress toward any target.
  There the progress comes with probability about 1/log n per step from a
  link distribution; here it is guaranteed every step by construction.
- [QUESTION-114](../questions.d/QUESTION-114.md): an instance of an organizing cost (an O(n³) build)
  buying a worst-case query guarantee, without the break-even the
  question asks for.
