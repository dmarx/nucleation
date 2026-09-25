---
number: 6
status: Read
formerly:
- NOTE-tmp6z978
paper: LIT-004
title: 'Community Detection on Networks with Ricci Flow'
version: 2
history:
- version: 2
  date: '2026-09-25'
  note: >-
    Read in full (full text of arXiv 1907.03993v1 (9 Jul 2019), 29 pp. The
    main text is pp. 1–13 (§§1–5, Figs. 1–8, Table 1). The Supplementary
    Information is pp. 14–26: §A theory, §B the 3-manifold motivation, §C
    Algorithm 1, §D evaluations with Figs. S9–S16, and §E the proof of
    Theorem 4.1 with Figs. S17–S18. The reference list is pp. 26–29.
    Extraction was with PyMuPDF. Fig. 5 was inspected as a page render, and
    the bar-chart values below are read off it (±~0.03). I checked Lemma E.1
    numerically by linear programming on G(3,2), G(5,3) and G(6,2)
    (scratchpad/lpcheck59.py). I did not compare the Sci. Rep. version, and
    I did not run the GraphRicciCurvature code.). Upgraded from `Skimmed` to
    `Read`: the claims table, assumptions and results are new, and the skim
    is corrected where the full text disagreed.
date: '2026-09-25'
summary: >-
  The paper runs Ollivier-Ricci flow w^{(k+1)}_{xy} = (1 −
  κ^{(k)}_{xy})·d^{(k)}(x,y) (= W(m_x, m_y)), then cuts edges above a
  weight threshold. On LFR (n = 500, avg. degree 20) this gives ARI ≈ 1 up
  to μ ≈ 0.6. On two-block SBM (n = 500, p_intra = 0.15) it gives ≈ 1 up
  to p_inter/p_intra = 0.5, but it collapses to ≈ 0.1 at 0.55, where
  Spinglass and Fast Greedy still score ≈ 0.9 and ≈ 0.8. Theorem 4.1 (α =
  p = 0, cliques G(a,b), a > b ≥ 2) proves in fact only that non-gateway
  intra-clique edges shrink as (1/a)ⁿ. Gateway intra-clique edges grow at
  the same rate λ₁ⁿ as inter-community edges, with ratio → k ∈ (0,1).
---

# NOTE-006: Community Detection on Networks with Ricci Flow

## Contribution

The paper introduces an iterated **Ollivier-Ricci flow on edge weights** for community detection. The update is w^{(k+1)}_{ij} = (1 − κ^{(k)}_{ij})·d^{(k)}(i,j) (SI Eq. 10), which is exactly the Wasserstein distance W(m_i, m_j) on the current metric graph. The neighbour measure is parameterised by laziness α and a distance discount p. After the flow, the method removes high-weight edges ("surgery") and reads communities off as connected components.

It adds three things:
- a proof for one symmetric family, G(a,b), under α = p = 0, that the flow separates the cliques (Theorem 4.1, SI §E);
- a benchmark on SBM, LFR, GNet and six labelled real networks against five iGraph baselines, scored by ARI;
- a label-free cutoff heuristic: cut where modularity "first hits the plateau".

Code was released as GraphRicciCurvature.

## Key insight

Ollivier curvature compares the cost of transporting one endpoint's neighbourhood to the other's with the edge length. Edges between communities have few shared neighbours, so the transport must use the edge itself: W > d and κ < 0. Edges inside a community have shared neighbours and shortcuts: W ≤ d and κ ≥ 0. Replace each edge weight by that transport cost and iterate. Bottleneck edges then lengthen and within-community edges contract, so a single weight threshold separates them. This is the discrete analogue of Ricci flow with surgery pinching necks in a 3-manifold (Fig. 1, SI §B).

## Assumptions

- **Graph and metric.** The graph is undirected and connected, with positive edge weights. Starting weights are 1, and d is the shortest-path metric induced by the current weights (SI Eq. 3).
- **Neighbour measure (§3, SI Eq. 7):**
  - m^{α,p}_x(x) = α;
  - m^{α,p}_x(xᵢ) = (1 − α)/C · exp(−d(x,xᵢ)^p) for neighbours xᵢ;
  - zero elsewhere.
  - Experiments use **α = ½ and p = 2** "in most cases" (SI §A.4), with base e (SI §D.2).
  - **Theorem 4.1 uses α = 0, p = 0**, the uniform neighbour measure of Lin–Lu–Yau. The SI says: "we are not able to prove the similar result for other Ollivier-Ricci curvatures when p > 0" (§E).
- **Community definition.** A community is a connected component left after removing a set of edges (SI §A). The partitions are non-overlapping. For FB-Ego, overlapping circles were merged into new circles (p. 9).
- **Hand-set knobs, per network:** the number of iterations, the surgery schedule and fraction, and the final cutoff. The authors defend this by analogy: "the cutoff number of iterations and threshold value for surgery … depend on individual networks", as in Hamilton–Perelman (p. 7).
- **The 3-manifold analogy is heuristic.** The authors call it "our heuristic thinking" (p. 7) and "roughly justify" it through Seifert–van Kampen (SI §B). No discrete statement links the two.

## Key results

- **Theorem 4.1 (p. 8; proof SI §E).** "The Ricci flow associated to the Ollivier K₀-Ricci curvature detects the community structure on G(a,b) if a > b ≥ 2, namely, the weight of the intra-community edges shrink asymptotically faster than the weight of the inter-community edges."
  - **Lemma E.1.** D₁ = (a−1)/(a+b)·d₁ + 2a/(a+b)·d₂; D₂ = b/(a+b)·d₁ + (ab−a−b)/(a(a+b))·d₂ + 1/(a+b)·d₃; D₃ = d₃/a. If d₁ ≥ d₂ ≥ d₃, then D₁ ≥ D₂ ≥ D₃. *I verified this by exact LP on three graphs over five iterations.*
  - **Lemma E.2 (via Maple).** The matrix A has real eigenvalues λ₁ > λ₂ = 1/a ≥ 0 > λ₃. The λ₁ eigenvector is [1, k, 0]ᵗ with k ∈ (0,1).
  - **What the proof establishes:**
    - d₁ ~ a₁λ₁ⁿ;
    - d₂ ~ k·a₁λ₁ⁿ, so d₂/d₁ → k (the proof's "o(λ₁ⁿ)" for d₂ is an error);
    - d₃ = (1/a)ⁿ → 0.
  - λ₁ can be < 1: 0.946 for (3,2), but 1.041 for (5,3). In that case every weight → 0 without normalisation, and only the ratios separate the communities.
- **SBM, Fig. 5a** (two equal blocks, n = 500, caption p_intra = 0.15, 10 graphs per point).
  - Ricci flow scores ARI ≈ 1 for p_inter/p_intra ≤ 0.5, ≈ 0.12 at 0.55 and ≈ 0 by 0.6.
  - Spinglass and Fast Greedy stay above it from 0.5 to ≈ 0.65.
  - Label Propagation and Infomap fail from ≈ 0.2.
  - §4.2.3 itself says "most of the algorithms perform well when the mixing ratio is below 0.5".
- **LFR, Fig. 5b** (n = 500, avg. degree 20, "38 communities").
  - Ricci flow scores ARI ≈ 1 up to μ = 0.6, ≈ 0.8 at 0.65 and ≈ 0.2 at 0.7.
  - Spinglass is ≈ 0.93–0.97 over μ = 0.45–0.6 and higher than Ricci flow at μ ≥ 0.7.
- **Real networks, Fig. 5c** (ARI read off the bars):

  | network | Ricci flow | best other |
  |---|---|---|
  | Karate | ≈ 0.77 | ≈ 0.60 (Label Propagation) |
  | Football | ≈ 0.89 | Infomap ≈ 0.90 |
  | Polbooks | ≈ 0.67 | Edge Betweenness ≈ 0.68 |
  | Polblogs | ≈ 0.72 | Fast Greedy ≈ 0.79, Spinglass ≈ 0.78 |
  | FB-Ego | ≈ 0.68 | Infomap ≈ 0.68 |
  | Email-EU-core | ≈ 0.46 | Infomap ≈ 0.30 |

  So Ricci flow is best on 2 of the 6 networks, tied on 3 and behind on Polblogs. The text counts Polblogs among the "competitive or better" cases and does not mention Email-EU-core. No run-to-run variation is shown for Ricci flow.
- **Cutoff and modularity (Fig. 6a).** The graph is LFR, n = 1000, 30 communities, μ = 0.4, after 50 iterations. ARI = 1 for any cutoff in [0.47, 1]. Modularity peaks at cutoff 0.275, which gives **290** communities. The "first plateau of modularity" rule is proposed from this one instance and then applied to GNet (Fig. 6b, cutoff 3.2 → 38 communities), where there is no ground truth.
- **SI §D.2–D.4.**
  - p = 2 or 3 works better than p = 0 or 1 on one LFR graph (μ = 0.5, Fig. S10).
  - Base e is the most stable at high μ (Fig. S11).
  - Sinkhorn (regularisation 0.1) matches exact OT on LFR n = 300. Mean time per iteration is 1.607 s against 6.417 s, which the paper calls "time complexity … reduced by four times" (Fig. S12).
  - Surgery raises ARI from 0.3 to 0.8 on LFR n = 1000, μ = 0.6 (Fig. S14).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Inter-community edges tend to be negatively and intra-community edges positively Ollivier-curved | informal argument + illustration | §3, Fig. 2a (Karate), Fig. S9b |
| C2 | Iterating w ← (1−κ)d stretches inter- and shrinks intra-community edges | experiment (illustrative) | Figs. 2, 3, S9, S13 |
| C3 | On G(a,b), a > b ≥ 2, α = p = 0, intra-community edges shrink asymptotically faster than inter-community edges | **proof, partly wrong** | SI §E. Correct for non-gateway edges (1/a)ⁿ. False for gateway–non-gateway edges, where the ratio → k ∈ (0,1). k ∈ (0,1) is from Maple, not proved. |
| C4 | The flow "provides nearly perfect clustering result when community structures exist" | experiment, overstated | Fig. 5. True where every method succeeds; fails on SBM where Spinglass and Fast Greedy succeed |
| C5 | The SBM collapse at p_inter/p_intra ≈ 0.55 marks "the non-existence of community structure" | **assertion, contradicted** | p. 9. Fig. 5a shows other methods at ARI 0.8–0.9 there. The two-block KS threshold is ≈ 0.78 for c_in = 75 (my calculation) |
| C6 | On LFR, Ricci flow is the most accurate and more stable than Spinglass | experiment | Fig. 5b, μ ≤ 0.65 only; 10 graphs per point |
| C7 | On real networks, Ricci flow is competitive or better in Karate, Football, Polbooks, Polblogs | experiment | Fig. 5c. Behind on Polblogs; single runs; how the final cutoff was chosen is not stated |
| C8 | Modularity's first plateau is a good label-free cutoff | experiment (n = 1 labelled graph) | Fig. 6a; applied unvalidated to GNet (Figs. 6b, S15–S16) |
| C9 | Varying the cutoff reveals hierarchical communities | illustration | Figs. 7, S16; no ground truth |
| C10 | Surgery every 5 iterations improves accuracy on mixed graphs | experiment | Fig. S14 (ARI 0.3 → 0.8 at μ = 0.6) |
| C11 | Sinkhorn with regularisation 0.1 performs "equally well" as exact OT and is ~4× faster | experiment | Fig. S12, LFR n = 300, 5-iteration average |
| C12 | Forman curvature gave "less satisfying" community-detection results | assertion | §1.2; no data shown |
| C13 | Ricci flow is "easier to implement in practice" than Girvan–Newman because betweenness needs global information | assertion | SI §A.4. The flow also recomputes shortest-path distances every iteration and solves one OT per edge; no timing comparison is given |
| C14 | "Similar results have been observed with modularity" | assertion | §4.2.2; no modularity results for Fig. 5 shown |

The most citable sentence is the abstract's "experimentally confirmed the effectiveness of this geometric approach", together with §1.1's "nearly perfect clustering result when community structures exist". That sentence has the least support. It holds on the benchmarks where most baselines also succeed. It fails, per the paper's own Fig. 5a, on the one benchmark that has a known detectability threshold.

## Method

**Algorithm 1 (SI §C).** The input is G with all weights 1. Repeat until every |κ⁽ⁱ⁾ − κ⁽ⁱ⁻¹⁾| < δ:
1. Normalise w ← d·|E| / Σd.
2. Compute κ_xy = 1 − W(m^{α,p}_x, m^{α,p}_y)/d(x,y) on every edge, with exact LP (CVXPY/ECOS) or Sinkhorn (POT).
3. Update w_xy ← d(x,y) − ε·κ_xy·d(x,y), and recompute shortest paths.

**Surgery.** Every 5 iterations, remove the edges in the top 5% by weight (SI §D.4). At the end, remove edges above a final cutoff and take the connected components as communities. For unlabelled graphs, choose the cutoff at the first plateau of modularity against cutoff (SI §D.4, Fig. 6). For hierarchies, use several cutoffs, or repeated rounds of flow and surgery.

**Stated parameters:** α = ½, p = 2, base e, and 20–50 iterations ("LFR with 1000 nodes … takes around 50 iterations to fully stabilized"). The values of ε and δ, and the Fig. 5 final cutoffs, are not given.

## Concepts

- **Ollivier-Ricci curvature** — κ_xy = 1 − W(m_x, m_y)/d(x,y), with W the 1-Wasserstein (earth mover's) distance under cost d (Eq. 2 / SI Eq. 8).
- **m^{α,p}_x** — the neighbour measure: laziness α at x itself, with the rest spread over neighbours ∝ exp(−d^p). p = 0 is Lin–Lu–Yau's uniform measure.
- **K₀** — the curvature with α = 0 and p = 0. It is the only one the theorem covers.
- **Discrete Ricci flow** — here w^{(k+1)} = (1 − κ^{(k)})d^{(k)} = W. It is the discrete form of Ollivier's suggested flow d/dt d_ij = −κ_ij d_ij (SI Eq. 9), and SI Algorithm 1 adds step size ε and renormalisation.
- **Surgery** — removing edges whose weights exceed a threshold, the analogue of excising a neck-pinch singularity.
- **G(a,b)** — b+1 cliques K_{a+1}, one "gateway" vertex per clique, and the gateways joined into K_{b+1}.
- **ARI** — adjusted Rand index against ground truth, 1 = identical partition (SI Eq. 11).
- **Modularity Q** — the Newman–Girvan quality function (SI §D).

## Connections

- **Reading 12 ([LIT-020](../literature.d/LIT-020.md); Weber, Saucan & Jost, Forman–Ricci curvature and flows).** Ni et al. cite it as [44], for Forman–Ricci flow in anomaly detection, and cite Samal et al. [23] for the strong correlation between Forman and Ollivier curvature on many networks. Both papers use a flow of the same form, weight change ∝ −curvature × weight:
  - Weber et al.'s Eq. 36 is γ̃ − γ = −Ric_F·γ;
  - Ni et al.'s is w ← d − ε·κ·d.

  The two readings are complementary. reads/12 found that Weber et al. only "theoretically proposed" their flow applications on a small example. Ni et al. is where a curvature flow is actually benchmarked, with Ollivier curvature. Ni et al. also report, without data, that Forman curvature did worse for community detection (C12). So neither paper tests Forman-flow community detection.
- **Methodological kin.** The paper itself compares the approach to Girvan–Newman edge-betweenness removal (SI §A.4): both iteratively remove "heavily traveled" edges. The Ollivier transport cost here is a local stand-in for global betweenness.
- **Own prior work.** Ni et al. 2015 (Ricci curvature of Internet topology, INFOCOM) and Ni et al. 2018 (network alignment by discrete Ollivier-Ricci flow) are the direct predecessors.
- **Not in this text.** Later work used Ollivier and Forman curvature to diagnose over-squashing in graph neural networks and to guide graph rewiring. This paper predates that line and does not anticipate it.

## Bearing on the record

- In nucleation this is [LIT-004](../literature.d/LIT-004.md). Its summary should be amended in three places:
  - drop "competitive with or better than" for SBM;
  - note that Theorem 4.1 is proved only for α = p = 0 and establishes separation by a constant factor for gateway edges;
  - note that the iteration count, surgery schedule and cutoff are hand-set per network.
- reads/12 names [LIT-004](../literature.d/LIT-004.md) as "the place where a Ricci flow is actually benchmarked". That stands, with the caveats above.
- It supports and contradicts no THEORY document in the Anthology of the SOTA.
- For ML practice, it carries no instruction. Community detection by curvature flow is a network-science method, not a training or evaluation practice. The anthology's GNN notes (e.g. [ANTH-LIT-580](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-580.md), [ANTH-LIT-582](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-582.md)) contain no curvature-based rewiring practice. If one were filed, its sources would be the later over-squashing papers, not this one. Nothing here warrants an ANTH- document.

## Limitations

- **The theorem** covers one highly symmetric family under a curvature variant (α = p = 0) that the experiments do not use. It overstates what its own proof shows for gateway edges, and it rests on a Maple-derived eigenvector property.
- **No guarantee for SBM or LFR**, and no analysis of when the flow converges or whether the fixed point depends on ε. The main-text flow (no ε, no normalisation) and SI Algorithm 1 differ, and the paper does not say which produced which figure.
- **Benchmarks.**
  - The two synthetic benchmarks use 10 graphs per point at n = 500. There is one SBM configuration and one LFR configuration.
  - The text and the caption disagree on SBM parameters. §4.2.3 says "fixed P_inter = 0.15 and tested the mixing ratio P_intra/P_inter"; the caption says P_intra = 0.15. The stated "500 nodes, 6800 edges" is below the ≈ 9,340 intra-block edges expected at p_intra = 0.15 alone (my arithmetic).
  - The number of LFR communities is given as 38 in the Fig. 5 caption and SI §D.1, but 30 in the Fig. S9 title.
- **Unreported selection.** How the final cutoff for the Fig. 5 ARI scores was chosen, whether with or without labels, is not stated. Fig. 6a shows ARI = 1 over a cutoff band that modularity's maximum misses.
- **Real networks.** There are six small networks (≤ 1,222 nodes) and no timing against the baselines. The only runtime figures are for Sinkhorn against exact OT at n = 300.
- **Some claims are asserted without data:** that Forman curvature performed worse (C12), that modularity gives "similar results" (C14), and that the method is easier to implement than betweenness (C13).

## Open questions

- Does the flow with α = ½ and p = 2 provably separate communities on SBM, and how close to the Kesten–Stigum threshold (≈ 0.78 here) can it get? Fig. 5a says it stops near 0.5, well short of both the threshold and Spinglass. A sweep over α, p, iterations and cutoff at fixed SBM parameters would show whether that gap is the method or the tuning.
- Is k ∈ (0,1) in Lemma E.2 true for all a > b ≥ 2? A symbolic proof would settle it; the numerics above agree for the four cases I tried.
- Is the "first modularity plateau" cutoff reliable across labelled benchmarks, or was Fig. 6a a favourable instance? A study over many LFR and SBM graphs, reporting ARI at the heuristic cutoff, would settle it.
- Does Forman-Ricci flow really underperform for community detection (C12)? The paper shows no data, and reading 12's paper shows no benchmark.

## Corrections to the seeded skim

- The dossier says the method is "competitive with or better than standard methods on SBM, LFR and several labelled real networks". On SBM (Fig. 5a), Ricci flow falls to ARI ≈ 0.12 at p_inter/p_intra = 0.55. At the same ratio Spinglass is ≈ 0.9 and Fast Greedy ≈ 0.8, and both stay above Ricci flow to ≈ 0.65. The paper interprets the collapse as "the non-existence of community structure" (p. 9). Its own figure contradicts that: other methods still recover the blocks. So does the two-block Kesten–Stigum threshold, (c_in − c_out)² > 2(c_in + c_out) with c_in = n·p_intra = 75. That places the detectability limit near p_inter/p_intra ≈ 0.78 (my calculation, from ref. [52]'s theory).
- The dossier restates Theorem 4.1 as intra-community edges shrinking "asymptotically faster than inter-community edges". The SI proof (§E) shows that only non-gateway–non-gateway edges shrink (d₃ = (1/a)ⁿ). The gateway–non-gateway intra-community edges satisfy wₙ₂ = k·a₁λ₁ⁿ + o(λ₁ⁿ), the same order as the inter-community edges wₙ₁ = a₁λ₁ⁿ + o(λ₁ⁿ). The proof's closing line, "the distance at the edges ui and ij grows at rate o(λ₁ⁿ)", is wrong for ui. I iterated the paper's matrix A and found d₂/d₁ → 0.455 for (a,b) = (3,2), 0.433 for (5,3), 0.172 for (10,2) and 0.625 for (10,9). Detection still follows by thresholding, because k < 1. But that is separation by a constant factor, not asymptotic. k ∈ (0,1) is asserted from a "Maple calculation" (Lemma E.2), not proved. For the record, Lemma E.1's three transport costs match an exact LP for every case I checked.
- The dossier says "surgery typically after ~10–15 iterations". That is the main text's remark (p. 7). The experiments differ:
  - Fig. 5 runs 50 iterations, with "surgery … every 5 iterations" (p. 9);
  - SI §D.4 says each surgery removes the edges whose weights "rank among the top 5%";
  - Fig. 2 uses 100 iterations, Fig. 3 uses 20, and GNet uses 20.
- The dossier gives the flow as w ← d − κd. That is the main-text form (p. 7). SI Algorithm 1 adds a step size ε (w ← d − ε·κ·d). It also renormalises the weights to sum to |E| at every iteration and stops when all |κ⁽ⁱ⁾ − κ⁽ⁱ⁻¹⁾| < δ. The paper never reports ε or δ. The theorem's matrix iteration uses neither ε nor normalisation.
- The dossier says LFR accuracy is "the most accurate and more stable than Spinglass". In Fig. 5b that holds for μ ≤ 0.65. At μ = 0.7–0.75 Spinglass is higher, roughly 0.35 against 0.2 at μ = 0.7.
- The dossier says it did not check the SI proofs. They have now been read and checked; see above.
