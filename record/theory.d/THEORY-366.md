---
number: 366
status: Active
formerly:
- THEORY-tmpazpbe
title: "With a fixed number of data points and a query drawn independently of them, if the variance of the p-th power of the query-to-point distance divided by its mean tends to zero, the farthest point comes within any factor 1 + ε of the nearest with probability tending to one; independent coordinates meet this condition, while data on a low-dimensional subspace, or queries that fall inside well-separated clusters, escape it"
version: 1
tags:
- information-retrieval
- mathematics
- probabilistic-modeling
date: '2026-10-15'
source:
- LIT-1099
summary: >-
  Beyer, Goldstein, Ramakrishnan and Shaft (1999), [LIT-1099](../literature.d/LIT-1099.md), read in
  [NOTE-917](../notes.d/NOTE-917.md) from the authors' 1998 technical report. Theorem 1: for n fixed
  data points and an independent query, var(d^p / E[d^p]) → 0 implies
  P[DMAX ≤ (1+ε)DMIN] → 1 for every ε > 0. The index m is arbitrary, so
  dimension enters only through the workload's distance distributions. IID
  coordinates and several correlated or non-identical workloads satisfy the
  condition; a diagonal line, two latent degrees of freedom and queries
  inside clusters do not. The condition is sufficient, not necessary. The
  result concerns the ratio of distances at fixed n, and does not show that
  real high-dimensional data loses contrast, or that indexes fail.
supports:
- CLAIM-310
- CLAIM-311
---

# THEORY-366: With a fixed number of data points and a query drawn independently of them, if the variance of the p-th power of the query-to-point distance divided by its mean tends to zero, the farthest point comes within any factor 1 + ε of the nearest with probability tending to one; independent coordinates meet this condition, while data on a low-dimensional subspace, or queries that fall inside well-separated clusters, escape it

## Source

Beyer, Goldstein, Ramakrishnan and Shaft (1999), [LIT-1099](../literature.d/LIT-1099.md), "When is
'nearest neighbor' meaningful?", ICDT '99. Read in full in [NOTE-917](../notes.d/NOTE-917.md), from
University of Wisconsin–Madison CS Technical Report [#1377](https://github.com/dmarx/nucleation/issues/1377) (June 1998), the
authors' report of the same title. The published chapter was not seen.

## What was actually shown

**The theorem.** For each m there are a data distribution and a query
distribution, n data points drawn independently from the first, a query
drawn from the second independently of them, a constant 0 < p < ∞, and any
non-negative function d_m (not necessarily a metric). If
lim var(d_m(P, Q)^p / E[d_m(P, Q)^p]) = 0, then for every ε > 0,
lim P[DMAX_m ≤ (1+ε)DMIN_m] = 1. The proof is short: the normalised
distance converges in probability to 1, so the max and min of n copies
converge to 1 too, and so does their ratio. Nothing in it uses m as
dimension. The paper says "nowhere in the following proof do we rely on
that interpretation".

**Which workloads satisfy it** (L_p distance, m as dimension), each by
computing the moments:

- IID coordinates with finite moments up to the 2p-th, query independent
  of the data. The paper calls this "not original".
- Every pair of coordinates correlated, with variance growing per
  coordinate (X_i = U_i + X_{i−1}/2).
- Independent coordinates whose variance shrinks as 1/i.
- Data and queries uniform on the boundary of the cube, where the
  marginals change with m.

**Which escape it.** Data and queries on the diagonal, where the problem
stays one-dimensional. Coordinates that are linear in two latent
uniforms, which in simulation kept the contrast of two-dimensional data at
every m. Queries required to land in one of several tight clusters, where
the nearest cluster is distinct but the nearest point within it is not.
Exact or near-exact matches. With the same clustered data and uniform
queries, the theorem applies again, to the choice of cluster.

**How fast.** No rate is proved. In simulation with IID uniform, normal and
exponential coordinates and 50 thousand to 10 million points, DMAX/DMIN
fell from about 10^8 at m = 1 by seven orders of magnitude at m = 10, and
data set size had little effect. Two real image-feature sets (64 and 324
dimensions, about 13,500 images) showed weak contrast: for 1-NN, 15% of
queries had half the data within three times the nearest distance.

**What could have come out otherwise.** The moment calculations are
explicit and checkable. A workload meeting the condition whose nearest
and farthest points stayed apart in ratio would refute the theorem. (The
NOTE found one arithmetic slip in a worked example, a variance of 12/i²
that should be 8/i²; the conclusion is unaffected.)

## What this does not say

- **That nearest neighbour is meaningless in high dimension.** Only under
  the variance condition, which is sufficient and not shown necessary.
  The paper's own escapes are the cases that matter in practice: low
  intrinsic dimension and queries that land in clusters.
- **That real data loses contrast.** Two real feature sets from one image
  system did. Real data of low intrinsic dimension was not analysed. The
  paper names it as an escape, and offers only a synthetic two-factor
  case.
- **Anything as the number of points grows with dimension.** n is fixed.
  The paper notes that for 2^m points on the cube's vertices queries
  become stable again.
- **Anything about absolute gaps.** The result concerns DMAX/DMIN. The
  difference between them is not addressed.
- **That indexes fail, or that ten to fifteen dimensions is a threshold.**
  No index is measured. The 10–15 figure is the simulations' summary for
  IID-like data, and the theorem has no rate.
- **That arrangement by similarity cannot discriminate.** The theorem is
  about one query against a set of points. Where it holds, no arrangement
  helps, because there is nothing to find. Where it fails, as with
  clustered queries, the paper's answer is retrieval of the whole nearest
  cluster.

## Connections

- [THEORY-369](THEORY-369.md) is the cost-side companion. Weber, Schek and Blott
  ([LIT-1107](../literature.d/LIT-1107.md)) show, under uniform independent data, that partitioned
  indexes come to read every block. This theorem says that in the same
  setting the answer they seek carries no contrast.
- [CLAIM-310](../claims.d/CLAIM-310.md): the theorem's condition is on the workload, data and queries
  jointly, so the same collection serves one query distribution and not
  another, the claim's dependence on the query mix. The paper's remedy
  for clustered data, to return the whole nearest cluster, is retrieval
  by bin.
- [QUESTION-114](../questions.d/QUESTION-114.md): a precondition rather than an answer. When the condition
  holds, organizing cannot pay, because no nearest neighbour is worth
  finding.
- [THEORY-340](THEORY-340.md): Yao's exact-membership setting always has a meaningful
  answer. This is the other end, where similarity search over
  concentrated distances may have none.
