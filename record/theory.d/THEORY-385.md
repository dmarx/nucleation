---
number: 385
status: Proposed
formerly:
- THEORY-tmpsdhw2
promote_when: >-
  A test by others than the authors, on clustered data with the cluster
  structure measured, that compares the two linking rules at matched degree
  and build cost and finds the nearest-neighbour rule losing recall at
  cluster boundaries while the pruning rule does not. More runs by the
  authors, or benchmark wins on unclustered data, cannot settle it.
title: "In a proximity-graph index over data in isolated clusters, linking each new item to its nearest neighbours leaves greedy search stuck at cluster boundaries and short of high recall, while linking a candidate only when it is nearer the new item than to any neighbour already chosen keeps the clusters connected and search fast; on uniform or very high-dimensional data the two rules differ little, and the evidence is the authors' own tests on synthetic and benchmark data"
version: 1
tags:
- databases
- information-retrieval
- network-science
date: '2026-10-15'
source:
- LIT-1098
summary: >-
  Malkov and Yashunin (2020), [LIT-1098](../literature.d/LIT-1098.md), read in [NOTE-916](../notes.d/NOTE-916.md). In HNSW,
  each new element's neighbours are chosen either as its M nearest
  candidates or by a pruning rule that keeps a candidate only if it is
  nearer the new element than to any neighbour already kept, a rule
  related to the relative neighbourhood graph. On 10M random d = 10
  vectors in 100 isolated clusters, nearest-neighbour links failed to
  reach high recall and the pruning rule did not. In every test reported,
  the rule was at least as good. Its gain was largest at low dimension,
  at high recall, and on clustered data, and small on uniform or very
  high-dimensional data. These are the authors' benchmarks: one clustered
  dataset, synthetic, with no independent replication in this reading.
---
<!-- inactive-ok-file: LIT-1098 — new filing, the source of this account -->

# THEORY-385: In a proximity-graph index over data in isolated clusters, linking each new item to its nearest neighbours leaves greedy search stuck at cluster boundaries and short of high recall, while linking a candidate only when it is nearer the new item than to any neighbour already chosen keeps the clusters connected and search fast; on uniform or very high-dimensional data the two rules differ little, and the evidence is the authors' own tests on synthetic and benchmark data

## Source

Malkov and Yashunin, IEEE TPAMI 42(4), 2020, [LIT-1098](../literature.d/LIT-1098.md), read in full
in [NOTE-916](../notes.d/NOTE-916.md) from arXiv v4: Section 3 (Fig. 2), Section 4 (Algorithm 4)
and Section 4.1 (Figs. 3–7).

## What was actually shown

**The rule.** Candidates are taken nearest first, and one is kept "only if
it is closer to the base (inserted) element compared to any of the already
connected candidates". Optionally, the candidate set is first extended by
the candidates' own neighbours, which is "useful only for extremely
clustered data". With enough candidates, the kept links contain the exact
relative neighbourhood graph. The rule keeps more edges than that graph so
that the degree can be controlled. In 1D it gives the exact Delaunay graph,
and the index becomes a skip list.

**Why it matters for clusters.** An element inserted at the edge of one
cluster has all its nearest neighbours in that cluster. Nearest-neighbour
linking then omits the edges that join the clusters. The rule keeps a link
to the nearest element of the other cluster when no kept neighbour is
closer to it (Fig. 2). Measured on 10M random d = 10 vectors, plain and in
100 isolated clusters (Fig. 7): with nearest-neighbour links "the
Hierarchical NSW algorithm fails to achieve a high recall for clustered
data because the search stucks at the clusters boundaries". With the rule
and candidate extension, "clustering leads to even higher performance".

**Where it matters less.** "For uniform and very high dimensional data
there is a little difference between the neighbors selecting methods". The
paper suggests this is because the rule then keeps nearly all the nearest
neighbours. On 5M SIFT the rule improved speed more than the hierarchy
did (Fig. 5). The paper reports it as never worse in any test.

## What this does not say

- **Not a connectivity guarantee.** The paper says the relative
  neighbourhood graph "allows easily keeping the global connected
  component". Nothing is proved about the pruned, degree-capped graph the
  index builds. Connectivity under deletion, which the index does not
  support, is untouched.
- **Not a general result about clustered data.** There is one clustered
  test: synthetic, with isolated clusters, at d = 10. Real clustered
  corpora were not separated out. That the Wiki-8 gain (about three
  orders of magnitude over NSW) comes from the rule is not isolated
  either: it compares whole methods.
- **The mechanism is the paper's reading.** That search sticks at
  cluster boundaries explains the low recall but was not measured directly, for instance by
  counting connected components or failed crossings.
- **Not that nearest is worst.** On uniform and very high-dimensional data
  the plain rule did about as well.

## Connections

- [CLAIM-310](../claims.d/CLAIM-310.md): the same items under the same distance can be findable or
  not, depending only on which links are kept. This is the claim's
  point that arrangements, not descriptions, decide retrieval, with links in place of bins, and with
  failure to find, not only extra cost.
- [THEORY-365](THEORY-365.md) is the paper's scaling claim. The rule is one of the
  approximations that stops the index's graphs being Delaunay graphs, which
  is why that bound is only derived, not proved, for what is built.
