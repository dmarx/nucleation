---
number: 910
status: Read
formerly:
- NOTE-tmpak6ah
paper: LIT-1112
title: Indyk & Xu — Worst-case performance of popular approximate nearest neighbor
  search implementations
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Read in full from the authors' arXiv preprint, arXiv:2310.19126v1 (29 October
    2023, the only version; arxiv.org/pdf/2310.19126, fetched 2026-10-15, saved
    here as 2310.19126.pdf), 17 pages: 10 pages of paper, references, and Appendices
    A–C. Its first page carries the line "37th Conference on Neural Information
    Processing Systems (NeurIPS 2023)", so it is the camera-ready text; the proceedings
    PDF on the NeurIPS site was not fetched and compared. Text extracted with pdftotext
    -layout; the extraction renders mathematical symbols in a substitute font (=
    as “, ∈ as P, parentheses as p q), so every formula below was transcribed by
    reading the extraction against the PDF's structure, and the theorem statements
    were checked against it line by line. Figures 2–10 are images; what they show
    is taken from their captions and the text, and no plotted value was read off
    a figure. Read: abstract, Sections 1–5, Appendix A (the DiskANN pseudocode),
    Appendix B (proof of Theorem 3.5) and Appendix C (the KD-tree hard instance
    and the seven further algorithms). The hard-instance code on GitHub was not
    run or read. Every quotation below was checked against the extracted text by
    script, with whitespace normalised; phrases quoted from the record are marked
    as such.
date: '2026-10-15'
summary: >-
  For DiskANN's "slow preprocessing" graph (each point linked to the points that
  survive α-pruning of all other points, naively O(n³) time), greedy search from
  any start with no backtracking reaches a ((α+1)/(α−1) + ε)-approximate nearest
  neighbour in O(log_α(∆/((α−1)ε))) steps, each costing O((4α)^d log ∆) for doubling
  dimension d and aspect ratio ∆; the ratio is tight and the dependence on ∆ cannot
  be replaced by log n. For DiskANN with its practical "fast preprocessing", HNSW,
  NSG and seven other graph indexes, the paper constructs two-dimensional point
  sets (constant doubling dimension) on which, in experiments with the authors'
  code at the authors' recommended parameters, the search queue must hold about
  10% of the points before recall@5 becomes non-zero or the approximation ratio
  becomes reasonable. The linear lower bounds are empirical, for one query per constructed
  instance, with an informal Ω(n/R) argument for fast-preprocessing DiskANN; no
  theorem bounds HNSW or NSG.
---

# NOTE-910: Indyk & Xu — Worst-case performance of popular approximate nearest neighbor search implementations

## Contribution

Graph-based nearest neighbour indexes (HNSW, NSG, DiskANN) are, in the authors' words, "widely used in practice" and have "limited theoretical guarantees", unlike older divide-and-conquer structures that have near-linear space and logarithmic query time when the data have low doubling dimension. The paper gives the first worst-case upper and lower bounds for these graph indexes. It proves a guarantee for one variant, DiskANN built by slow preprocessing, with matching lower-bound instances for its approximation ratio and its dependence on the aspect ratio. For the variants used in practice it builds hard instances and measures the query effort they need. The authors state that "our results do not contradict the empirical evaluations given in the original papers".

## Key insight

The guarantee comes from one property of the graph, which the paper calls α-shortcut reachability: from every point p, every other point q is either a neighbour of p or is at least α times closer to some neighbour of p than to p, with α > 1. Pruning each point's candidate list against all n points (slow preprocessing) gives this property by construction. With it, each greedy step shrinks the distance to the query's nearest neighbour by a factor α, up to an additive term, so the number of steps is logarithmic in the aspect ratio. Doubling dimension bounds how many neighbours survive pruning per distance scale, so the degree is O((4α)^d log ∆). Fast preprocessing prunes only against points found by searching the graph under construction, and HNSW and NSG prune with α = 1; neither guarantees the property, and the hard instances exploit that: a large cluster of points that are all closer to the query than the gateway to its true neighbour, with no edges from the cluster to that neighbour.

## Assumptions

- **Metric and dimension.** Points in a metric space; the guarantee needs the triangle inequality, finite doubling dimension d (log₂ of the smallest C such that any ball of radius 2r is covered by C balls of radius r) and aspect ratio ∆ = D_max/D_min. The paper notes that bounds in log ∆ and in log n are incomparable, and that ∆ is typically low: MNIST, with n = 60,000, has ∆ around 20.
- **Slow preprocessing.** For each vertex v, RobustPruning(v, V, α, R) on the whole point set: sort all points by distance from v, keep the nearest, delete every w with α·D(u, w) < D(v, w) for a kept u, repeat. The analysis takes R = n and then states that R = O((4α)^d log ∆) gives the same result. The paper notes that a naive implementation takes O(n³) time.
- **Fast preprocessing.** The method DiskANN actually implements: start from a random R-regular graph, make two passes in random order, and prune each point against the candidates returned by GreedySearch on the current graph, adding back-edges and re-pruning when a degree exceeds R.
- **Search.** GreedySearch(s, q, L) is best-first search with a queue of length L, from a fixed start vertex (DiskANN uses the point nearest the centroid). L lower-bounds the number of vertices scanned. The upper bound uses L = 1, no backtracking, and holds from any start vertex.
- **Experiments.** Two-dimensional Euclidean instances (one six-dimensional instance for the KD-tree-seeded methods), n from 10⁵ to 2·10⁶ in 20 sizes, one query per instance, L = pn for p from 1% to 50%, recall@5 and average approximation ratio, averaged over 5 or 10 runs with fresh random seeds. Parameters are those the original authors used or recommend (DiskANN R = 70, L = 125 at build, α = 2; HNSW efConstruction = 200, M = 64; NSG as for GIST1M). Running time is counted as vertices scanned, not wall-clock.

## Key results

- **Lemma 3.2.** Connecting each p to the output of RobustPruning(p, V, α) makes the graph α-shortcut reachable.
- **Lemma 3.3 (sparsity).** That output has at most O((4α)^d log ∆) vertices.
- **Theorem 3.4 (upper bound).** On an α-shortcut reachable graph built by slow preprocessing, GreedySearch(s, q, 1) from any s finds a ((α+1)/(α−1) + ε)-approximate nearest neighbour in O(log_α(∆/((α−1)ε))) steps; with step cost O((4α)^d log ∆), the total is polylogarithmic in ∆ for constant d. Case 3 of the proof adds that when the nearest neighbour is very close to the query (D(a, q) < (α−1)/(4(α+1))·D_min), the exact nearest neighbour is reached in O(log_α ∆) steps. For α = 2, the paper's typical setting, the ratio is 3 + ε.
- **Why not HNSW and NSG.** "we cannot prove query performance guarantees similar to the ones above", because those algorithms prune with α = 1.
- **Theorem 3.5 (the ∆ dependence is necessary).** For any α > 1 there are n points on a line with ∆ = O(α^n) and a query such that, after slow preprocessing, greedy search must scan Ω(log ∆) (equivalently Ω(n), on this instance) vertices before reaching an O(1)-approximate nearest neighbour. So log ∆ cannot be replaced by log n.
- **Theorem 3.6 (the ratio is tight).** For any α > 1 there are n + 2 points in the plane under ℓ₁ such that slow-preprocessing DiskANN scans at least n vertices before reaching a point better than (α+1)/(α−1)-approximate; with L ≤ n, search stops without one.
- **Hard instance for DiskANN, fast preprocessing (Section 4.1).** In the plane: grids M (0.8n points, containing the start), P (0.1n) and P′ (0.1n), and a target a with four points near it. The build leaves edges to a only from P′ and from P's random initial edges, and search exhausts P first. "the query procedure can take at least 0.1n steps on instances of size n before it encounters any of the 5 nearest neighbors of the query." In Figure 3, recall@5 is mostly zero until L is about 10% of n. The informal argument gives Ω(n/R) expected scans. On the same instance the slow-preprocessing graph is very sparse and "finds the exact nearest neighbor in only 2 steps!", measured only up to n = 10⁵ because "the slow preprocessing algorithm takes several hundred hours for larger values of n."
- **Hard instance for NSG and HNSW (Section 4.2).** The same layout with 4,400 points (0.44%) added in chains so that k-NN graphs are connected. "for most values of n, both NSG and HNSW algorithms cannot achieve good Recall@5 unless scanning at least 10% of the vertex set." Swapping the instances between algorithms at n = 10⁶ gave the same result. Average approximation ratios on rescaled versions are, in the paper's words, very high unless L ≥ 0.1n.
- **Ten algorithms (Table 1, L = 0.1n).** Average recall@5: DiskANN 0.0, NSG 0.27, HNSW 0.1, NGT 0.05, SSG 0.16, KGraph 0.42, DPG 0.37, NSW 0.02, SPTAG-KDT 0.02, EFANNA 0.12.
- **Scope the authors give.** "We demonstrate empirically that almost all of them suffer from linear query times on carefully constructed instances, despite being fast on benchmark data sets". Open: a fast-preprocessing index with worst-case guarantees, and "whether it is possible to replicate our findings for real data sets, using adversarially selected queries."

## Bearing on the record

**On [CLAIM-310](../claims.d/CLAIM-310.md) (arrangements, not descriptions, do the work in retrieval), with [LIT-1103](../literature.d/LIT-1103.md).** It supports the claim and sharpens the owner's reading in one respect.

- Supports: on one point set, the graph built over it decides whether greedy search reaches the nearest neighbour in two steps or only after scanning a tenth of the points (Section 4.1, both builds on the instance of Figure 2). The contents and the metric are fixed; the arrangement, which edges exist, does the work. This is [CLAIM-310](../claims.d/CLAIM-310.md)'s "as arrangements" half in a measured case.
- Sharpens: what the guarantee needs is a stated structural property, α-shortcut reachability with α > 1, which is a cousin of Kleinberg's condition: from any point, some link makes geometric progress toward any target. Kleinberg's r = 2 gives that progress with probability about 1/log n per step; slow-preprocessing DiskANN gives a factor α every step, deterministically.
- Narrows the owner's summary in three places. (1) The filing's "can need time linear in the collection on some inputs" is shown by experiment, not proved, for HNSW, NSG and fast DiskANN: one query per constructed instance, the authors' code and parameters, recall measured against queue length. No theorem lower-bounds those algorithms. (2) The hard instances are two-dimensional, so the failure is not a high-dimensional effect; low intrinsic dimension does not protect these builds. (3) The guarantee is not polylogarithmic in n: it is logarithmic in the aspect ratio ∆, which can be far larger than n (Theorem 3.5), with a constant approximation ratio, not exact search, and a degree exponential in the doubling dimension. "Slow preprocessing" is pruning every point against all others, O(n³) naively and hundreds of hours past 10⁵ points.

**On [QUESTION-114](../questions.d/QUESTION-114.md) (sorting as amortized search).** It is a clean case of the trade the question names. An O(n³) build buys a worst-case query guarantee; a near-linear heuristic build keeps queries fast on benchmarks and loses the guarantee. The paper measures neither build time systematically nor the break-even, and has no upkeep: points are not inserted after the build in the analysis. So it shows that the organizing cost buys something definite (a guarantee), not how much of it is worth paying.

**On [CLAIM-309](../claims.d/CLAIM-309.md) (goodness vs discriminability).** No bearing.

**On [THEORY-358](../theory.d/THEORY-358.md) (Treisman and Gelade search slopes).** A formal parallel only: an arrangement that leaves the target distinguishable from its neighbours by a guaranteed margin (the α factor) gives logarithmic search, and one that surrounds it with a cluster of nearer-looking candidates forces a scan proportional to the cluster. The mechanisms are unrelated, and the paper says nothing about perception.
