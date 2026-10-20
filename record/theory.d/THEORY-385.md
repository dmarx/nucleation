---
number: 385
status: Active
formerly:
- THEORY-tmpsdhw2
title: 'In HNSW over 10-dimensional data in 100 isolated clusters, linking each new item to its nearest neighbours leaves part of the bottom layer unreachable from the entry point and caps recall well short of 1 however wide the query search, while linking a candidate only when it is nearer the new item than to any neighbour already kept keeps that layer connected and reaches recall near 1 with about half the links; on uniform data at 10 and 64 dimensions the two rules differ little; shown in Malkov and Yashunin''s own tests on 10 million points and in an independent re-run on 30,000, which found the nearest-neighbour rule capped at a recall@10 of 0.72 to 0.83 against 0.999, at matched build cost too'
version: 2
history:
- version: 2
  date: '2026-10-20'
  note: >-
    Narrowed and promoted, carrying out the promotion audit's decision for
    THEORY-385 (batch 063). The paper's clustered result is one figure
    with no numbers in its text, so the review re-ran it independently, as
    the promote_when asked: HNSW with both linking rules on 30,000 points
    in 100 isolated clusters, at degree above and below the pruning rule's
    and at matched build cost, plus uniform data at d = 10 and 64. The
    nearest-neighbour rule left layer 0 partly unreachable and capped
    recall@10 at 0.72–0.83; the pruning rule reached 0.999. The title
    narrows to HNSW and to what was measured; "search fast" and candidate
    extension, which did not help in the re-run, leave it.
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
  Re-run independently at smaller scale on promotion (2026-10-20), with the
  same result.
---

# THEORY-385: In HNSW over 10-dimensional data in 100 isolated clusters, linking each new item to its nearest neighbours leaves part of the bottom layer unreachable from the entry point and caps recall well short of 1 however wide the query search, while linking a candidate only when it is nearer the new item than to any neighbour already kept keeps that layer connected and reaches recall near 1 with about half the links; on uniform data at 10 and 64 dimensions the two rules differ little; shown in Malkov and Yashunin's own tests on 10 million points and in an independent re-run on 30,000, which found the nearest-neighbour rule capped at a recall@10 of 0.72 to 0.83 against 0.999, at matched build cost too

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

## Note of 2026-10-20: an independent re-run

The promotion audit (batch 063) re-ran the paper's clustered test,
because Fig. 7 gives it without numbers in the text. The full design and
every number are in the audit's decision for THEORY-385.

- **Setup.** An implementation of HNSW written for the review, in Python
  and NumPy, following the paper's Algorithms 1–4: M = 16, 2M links on
  layer 0, ef_construction 100, and overflowing lists re-selected by the
  same rule. The data were 30,000 points in d = 10 from 100 isolated
  clusters (centres uniform in the unit cube, Gaussian spread 0.01), with
  500 queries scored against exact top-10.
- **Nearest-neighbour linking.** Recall@10 reached only 0.72 (seed 1)
  and 0.76 (seed 2) at query ef = 320. On layer 0, 23,996 and 1,241 of the
  30,000 elements were reachable from the entry point. Matching the
  pruning rule's build cost (ef_construction 400) raised the ceiling only
  to 0.83. Cutting the degree below the pruning rule's (M = 5) lowered it
  to 0.53.
- **The pruning rule.** Recall@10 was 0.995 by ef = 20 and 0.999 at
  ef ≥ 80, with every element reachable and a mean layer-0 degree of 11.8,
  against 24.9 for nearest-neighbour linking.
- **Uniform data.** At d = 10 and d = 64 the two rules were within about
  0.02 of each other at every ef.
- **Candidate extension.** The paper calls it useful for extremely
  clustered data. Here it kept the layer connected but capped recall at
  about 0.97, below the rule without it. The title no longer relies on
  it.

**Limits.** One synthetic clustered distribution, two seeds, and about
1/300 of the paper's scale. Where searches stop was not traced, so "stuck
at cluster boundaries" is replaced by what was measured: unreachable
elements and a recall ceiling. The connectivity of the pruned graph is
still measured, not proved.
