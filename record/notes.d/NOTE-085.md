---
number: 85
status: Read
formerly:
- NOTE-tmpz49bi
paper: LIT-068
title: 'Local separators and community structure'
version: 2
history:
- version: 2
  date: '2026-09-25'
  note: >-
    Read in full (full text of arXiv 2504.14501v1 (submitted 20 Apr 2025;
    title page dated 22 April 2025; the only version on arXiv as of
    2026-09-26), 15 pp. Covered §§1–6, Tables 1–2, Figs. 1–4 and references
    [1]–[28]. Nothing skipped. PDF from arxiv.org/pdf/2504.14501, extracted
    with PyMuPDF to raw4/2504.14501.txt. The results are almost entirely in
    Figs. 2–4, which are stacked bar charts, so I rendered pp. 2, 9, 10 and
    12 as images (raw4/c56_p*.png; NRW zoomed at 220 dpi). Bar heights below
    are read off those renders, ±~5% of the axis. I did not read the method
    papers [7] and [9], which hold the only definition of a local separator.
    No journal reference on arXiv, and no Crossref hit for the title.).
    Upgraded from `Skimmed` to `Read`: the claims table, assumptions and
    results are new, and the skim is corrected where the full text
    disagreed.
date: '2026-09-25'
summary: >-
  This is a comparison of the authors' local 1- and 2-separator
  decompositions against Infomap, Label Propagation, Leiden and Louvain
  (igraph) on five sparse graphs (62 to 9,133 nodes). Local separators
  score lower overlapping modularity than the modularity optimisers
  everywhere, and lower than Infomap on 3 of 5 graphs (Table 2). Their
  edge is confined to high density thresholds on the two road networks,
  where the best radius gives a handful more qualifying clusters: about 12
  against about 5 at β ≥ 1.25 on Euroroads, and about 50 against about 40
  for Infomap at β ≥ 1.5 on NRW (Figs. 3–4). On Netscience all methods are
  similar. At δ = 1 on both road networks, and at δ = 1.25 on NRW, Infomap
  yields more qualifying clusters than any local-separator setting.
---

<!-- inactive-ok-file: LIT-068 — Deferred: the paper is placed by this reading; the directive lapses when its status changes -->

# NOTE-085: Local separators and community structure

## Contribution

The paper is the first head-to-head empirical comparison, by its authors, of the local 1- and 2-separator decompositions from their earlier papers [7, 9] against four igraph community-detection methods. It uses five public sparse graphs. It proposes an "algorithm-independent" density function β(c) = (1/2|c|)Σ_{(i,j)∈P(c,c)} a_{i,c}a_{j,c}, with overlap-discounting belonging coefficients a_{i,c}. It frames community detection as maximising the number of communities with β ≥ δ. No new method or theorem is given.

## Key insight

The intended one: communities in sparse, near-planar graphs such as road networks are delimited by *local* bottlenecks, meaning small vertex sets that separate a ball around them. Global objectives like modularity miss these. Cutting at local 1-separators, then refining with local 2-separators, gives a two-level hierarchical decomposition. What the evidence supports is weaker: in road networks, local 1-separators produce a few more high-density clusters (β ≥ 1.25–1.5) than the baselines, and fewer clusters overall.

## Assumptions

- **Premise:** evaluation against modularity is biased by community count and size (§2.4). Two of the supporting statements are false; see corrections.
- **Density:** for sparse graphs, density is edges per vertex, e(c)/|c|, not e(c)/|c|². Overlap is handled by a_{i,c} = 1/|{d ∈ C : i ∈ d}| (§2.5).
- **Threshold:** no universal δ exists, since duplicating every vertex doubles β (Example 2.1). So δ is part of the problem instance.
- **Baselines:** igraph defaults for IM, LP, Leiden-modularity and Best Multi-Level (Louvain) (§2.2). Parameters and seeds are not stated.
- **Preprocessing (NRW only, §5):** degree-1 vertices removed and degree-2 vertices suppressed.
- **Unstated:** the definition of a local k-separator, the radius parameter R (the x-axis of Figs. 2–4; "d" in Table 2 is presumably the chosen R), how bags become overlapping communities, and how R is chosen for Table 2.

## Key results

- **Table 2 (overlapping modularity; local-separator values are overlapping modularity, baselines standard modularity, equal for partitions):**

  | Graph | 1-sep (R, clusters, Q) | 2-sep (R, clusters, Q) | IM | LP | BML | LM |
  |---|---|---|---|---|---|---|
  | Dolphins | 3, 4, 0.463 | 4, 16, 0.359 | 0.528 | 0.505 | 0.523 | 0.524 |
  | Euroroads | 6, 27, 0.536 | 9, 85, 0.370 | 0.788 | 0.812 | 0.880 | 0.886 |
  | Netscience | 5, 124, 0.878 | 7, 155, 0.812 | 0.930 | 0.910 | 0.959 | 0.959 |
  | Powergrid | 7, 95, 0.727 | 14, 145, 0.723 | 0.476 | 0.800 | 0.935 | 0.939 |
  | NRW | 10, 567, 0.900 | 17, 2246, 0.627 | 0.863 | 0.780 | 0.952 | 0.956 |

  Local 1-separators beat Infomap on Powergrid and NRW only. They are 0.25 lower on Euroroads, the road network the paper calls its strongest case.
- **Fig. 1 (Dolphins):** the local-separator clusters cover the two known groups, with two boundary nodes in both. Roughly a quarter of the nodes, the peripheral low-degree ones, are in no cluster. Which method and which R produced the figure is not stated. The paper shows no modularity partition of Dolphins to support "only partially recover".
- **Figs. 2–4:** see the corrections for the bar heights. Summary: Netscience shows parity. On Euroroads, 1-separators are the only method with clusters at β ≥ 1.5 (about 1–3), but have fewer clusters at lower bands. On NRW, 1-separators at small R slightly exceed Infomap at β ≥ 1.5 and trail it at 1.25–1.5. 2-separators give few, low-density clusters on both road networks.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Local 1-separators "consistently identify the densest communities, outperforming modularity-based methods" | weak | Figs. 2–4 by eye; holds only at high thresholds on the road networks, by small counts; no δ or count reported; parity on Netscience |
| C2 | Local 2-separators reveal hierarchical structure but over-fragment small clusters | weak | assertion plus the low bars of Figs. 3c/4c; no hierarchy is shown or measured here (deferred to [8]) |
| C3 | Results are "particularly strong" on road networks | weak | Figs. 3–4; contradicted on modularity by Table 2 (Euroroads) |
| C4 | Local separators achieve modularity comparable to IM and LP | moderate | Table 2; true on 3 of 5 graphs, 0.25 lower on Euroroads |
| C5 | Modularity is maximal (= 1) for the single-community partition, and merging never lowers it | false as stated | §2.4; contradicted by the paper's own §2.1 formula (Q({V}) = 0) |
| C6 | No universal density threshold exists | strong | Example 2.1 (vertex duplication doubles β); a valid construction |
| C7 | The method is scalable | weak | assertion from locality (p. 2); no runtime or complexity given |
| C8 | On Dolphins the method recovers the ground-truth split up to two boundary nodes, where modularity methods "only partially" do | weak | Fig. 1 only; many nodes unassigned; no modularity comparison shown |

## Concepts

- **Local separator** — "a small set of vertices that separates its local neighbourhood into well-connected regions" (p. 1–2). The formal definition is in [7, 9], not here.
- **Bags** — the components that remain after cutting at local separators, used as (overlapping) communities.
- **Overlapping modularity Q_ov** — §2.1, after Chen et al. [10], with belonging coefficients a_{i,c}. It equals standard modularity for partitions.
- **Density β(c)** — (1/2|c|)Σ_{(i,j)∈P(c,c)} a_{i,c}a_{j,c} (§2.5).
- **Community detection problem (G, δ)** — maximise |C| subject to β(c) ≥ δ for all c ∈ C (§2.5).

## Connections

- **Method sources:** Carmesin (2022), "Local 2-separators", JCTB [7] (theory); Carmesin & Frenkel, arXiv:2312.12354 [9] (practical definition and first algorithm); Carmesin & Frenkel, "From tree decompositions to large-scale network structures" [8] (hierarchy). None is in this record.
- **[LIT-004](../literature.d/LIT-004.md) (Ni et al., Ricci-flow community detection, read in reads/59.md).** The paper does not cite it. The two share three baselines (Infomap, Label Propagation, Louvain/multilevel) and a relationship to modularity, but they use it in opposite ways. [LIT-004](../literature.d/LIT-004.md) uses modularity's "first plateau" as its label-free cutoff rule; reads/59.md found that rule validated on one graph. This paper argues against modularity as an evaluation criterion, on grounds that are partly false (C5). [LIT-004](../literature.d/LIT-004.md) evaluates against ground truth (ARI on LFR, SBM and labelled real networks). This paper has no ground-truth benchmark beyond a qualitative Dolphins figure, so the two cannot be compared on accuracy. Both methods are "local": curvature of an edge's neighbourhood against separators within a ball of radius R. Neither text makes that link.
- **[LIT-020](../literature.d/LIT-020.md) (Weber, Saucan & Jost, Forman–Ricci curvature, read in reads/12.md).** No textual connection. Forman curvature is a combinatorial, local edge quantity, and [LIT-020](../literature.d/LIT-020.md) only *proposes* curvature-based clustering. This paper supplies nothing that tests that proposal.

## Bearing on the record

- In this record it is [LIT-068](../literature.d/LIT-068.md). Its summary overstates the finding ("denser than modularity-based methods produce … especially road networks"). It should say that local 1-separators yield a few more clusters at high density thresholds on road networks, with lower modularity than Infomap on Euroroads and no scored density criterion. Status should move from Deferred to Rejected. The dossier's hope that the §2.4 critique of modularity "applies to any community-detection comparison" should be withdrawn: the critique's concrete statements are wrong. The sound version of the point, the resolution limit and modularity's dependence on community count and size, should be cited to Fortunato & Barthélemy (2007) [14], not to this paper.
- It is not a useful comparison partner for [LIT-004](../literature.d/LIT-004.md): there is no shared benchmark or metric.
- **For the Anthology of the SOTA:** no ML content and no instruction for ML practice.

## Limitations

- No definition of the method, no pseudo-code, no code, no runtime.
- No ground-truth evaluation apart from one qualitative figure.
- The baselines are single igraph-default runs, while the local-separator results sweep R and are read at their best. There are no seeds or variance for the stochastic baselines (LP, Infomap, Leiden).
- The density problem of §2.5 is posed but not solved or scored. The δ at which "densest" is claimed is never stated.
- The Powergrid edge count appears doubled (unverified), and Powergrid is dropped from the discussion.
- 2-separator results on road networks are poor (few, low-density clusters). The hierarchical-refinement claim is deferred to [8].

## Open questions

- Score §2.5 properly: for a grid of δ, report the maximum number of β ≥ δ clusters for each method, with baselines given the same tuning budget as R.
- Evaluate against ground truth (LFR/SBM with overlapping communities, as in [LIT-004](../literature.d/LIT-004.md)'s benchmarks) to see whether local separators recover planted structure.
- Report runtime and scaling against Leiden and Infomap on graphs of 10⁶ nodes or more to support "scalable".

## Corrections to the seeded skim

- The dossier summary says local 1-separators find "denser than modularity-based methods produce" communities, "especially road networks". The figures support something narrower.
  - **Euroroads (Fig. 3):** LM/BML give about 21 clusters (about 16–17 at 1 ≤ β < 1.25, about 4–5 at 1.25–1.5). Infomap gives about 55 (50 + 5), and LP about 40. The best local 1-separator radius (R = 5) gives about 25, with about 2 at 1.5 ≤ β < 2. So the 1-separator method is the only one with any clusters above β = 1.5. At δ = 1.25 its best radius (R = 6, about 9 + 3 = 12) beats IM and LM (about 5 each). At δ = 1 it has fewer qualifying clusters than Infomap (about 25 against 55) at every R.
  - **NRW (Fig. 4):** Infomap has about 920 clusters (about 700 at 1.25–1.5, about 40 at ≥ 1.5). The best 1-separator setting (R = 2) has about 975 (about 580 at 1.25–1.5, about 50 at ≥ 1.5). At δ = 1.25, Infomap's about 740 qualifying clusters beat 1-separators' about 630.
  - **Netscience (Fig. 2):** local 1- and 2-separators (about 99–105 clusters) match IM/LP (about 102/107), and the ≥ 3 band is about 10 for every method.
  - So "densest" holds only at high thresholds on road networks and by small counts. The baselines are single runs, while the local-separator bars are a sweep over R and the best is quoted.
- The dossier treats §2.4 as a useful argument against modularity. Two of its statements are false.
  - "If all nodes are placed in a single community (C = {G}), modularity reaches its maximum possible value of one." For C = {V}, Q = |E|/|E| − (2|E|/2|E|)² = 0 by the paper's own formula (§2.1).
  - Merging two communities "is not smaller" in modularity. This is false: ΔQ = e₁₂/|E| − 2·(d₁/2|E|)(d₂/2|E|), which is negative whenever the two communities share few edges. Merging two disconnected communities always lowers Q.
  - The follow-on claim that a community containing nearly all vertices "artificially inflate[s]" modularity "often approaching one" is wrong for the same reason.
  - The resolution-limit point it cites [14] is real, but the paper's own statement of it is wrong.
- The dossier asked whether the density criterion (§2.5) "may favour their method". The more basic finding is that the criterion is never used as defined. §2.5 poses the problem "find C as large as possible with β(c) ≥ δ for all c ∈ C", but no δ is fixed and no count is reported. The figures show histograms of β over each method's clusters, and the text reads "densest" off them informally.
- The dossier notes runtime is "not obviously reported". It is not reported at all, and neither is the algorithm. "Scalable" (abstract, §1, §6) is asserted from "neighbourhood-level computations" (p. 2), with no timing, complexity statement or code.
- New, not in the dossier: Table 1 gives Powergrid m = 13,188. The standard US power-grid graph (4,941 nodes) has 6,594 edges, exactly half. The graph was probably loaded with both arc directions. This is unverified, but if true the Powergrid modularities in Table 2 are for a doubled multigraph. Powergrid is not discussed anywhere in the text beyond Tables 1–2.
- New, not in the dossier: the §3 text says local separators "find a comparable number of clusters to IM and LP". Table 2 gives 124 and 155 against 314 and 330 on Netscience. The figures, which count only clusters with β ≥ 1.5, show comparable counts. The text conflates the two.
- The dossier's point that the paper never mentions Ricci flow is confirmed.
