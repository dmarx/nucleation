---
status: Active
status_note: 'read 2026-10-09 ([NOTE-tmpki7xw](../notes.d/NOTE-tmpki7xw.md)); worth reading as a construction that recovers a latent tree from unlabelled data by distances alone, with a proof of what is recovered. Each point is represented by its diffusion densities P^(2^−k) e_i at dyadic times, each density is placed in a Poincaré half-space at a height set by its scale, and the hyperbolic diffusion distance is the ℓ1 sum over scales of the hyperbolic distances, 2 sinh⁻¹(2^(1−kα)‖φ_i^k − φ_j^k‖) with φ the square roots of the densities, a scale-weighted Hellinger distance. Theorem 1 (Appendix C, after Leeb and Coifman) says that for the heat kernel on a tree this is equivalent up to constants to min{1, d_T^(2α)}, 0 < α < 1/2: a thresholded snowflake of the tree metric, not the tree metric, and saturated beyond a fixed radius; the main text states it without the threshold. The tree heat-kernel bounds are stated, not proved, and one step of the Hölder bound (Proposition C.5) holds only for tree distances of at least 1, so the admissible range of α is not secured. Empirically it gives the best mean average precision on five graph benchmarks and two single-cell datasets and worse average distortion than hyperbolic MDS or Sarkar''s construction: local neighbourhoods are kept, global distances are not. Nothing in it concerns attributes or linear directions.'
title: 'Hyperbolic Diffusion Embedding and Distance for Hierarchical Representation Learning'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Filed at the owner's request on 2026-10-09, one of a batch of six works
    on hierarchy and hyperbolic geometry. The owner's description was "Lin
    et al. (2023) — multiscale density geometry recovering latent
    hierarchy". Identified as this paper: its abstract says "using diffusion
    geometry, we build multi-scale densities on the data, aimed to reveal
    their hierarchical structure", and proves the recovery. arXiv API
    searches for 2023 papers with a first author Lin and abstracts
    combining hierarchy with multiscale, density, diffusion, hyperbolic,
    "latent hierarchy" or geometry returned no other candidate. The nearest
    other work, by the same first author and group, is "Tree-Wasserstein
    Distance for High Dimensional Data with a Latent Feature Hierarchy"
    (arXiv:2410.21107, posted 28 October 2024), which is 2024 and recovers a
    hierarchy of features rather than of samples. Read in full the same day
    (NOTE-tmpki7xw) from the arXiv PDF of v1 (30 May 2023, 23 pp., the only
    version), text extracted with pdftotext: §§1–7 and Appendices A–E,
    every proof followed. Checked against the arXiv abstract page
    (arXiv:2305.18962, v1 submitted 30 May 2023; authors Ya-Wei Eileen Lin,
    Ronald R. Coifman, Gal Mishne, Ronen Talmon) and the PMLR index for
    volume 202: Proceedings of the 40th International Conference on Machine
    Learning (ICML 2023), PMLR 202:21003–21025, same title and authors,
    proceedings dated 3 July 2023; no DOI was found (Crossref returns none
    for the title). `published:` is the arXiv v1 date, 30 May 2023, the
    earlier of the two (ADR-002). Not held in nucleation before this
    filing: a grep of record/ for the identifier, the title and the four
    authors found nothing. Not held in the Anthology of the SOTA as far as
    its clone shows: a grep of its record/ (clone at commit d8b5ba5, 9
    October 2026, possibly stale) for the identifier, the title, the
    authors, "diffusion maps" and "Poincaré" found nothing relevant. Its
    `graphs-and-networks` topic could hold it (graph embedding and
    hyperbolic representation), hence `anthology-candidate`. Code at
    github.com/Ya-Wei0/HyperbolicDiffusionDistance (not inspected).
tags:
- representation-learning
- mathematics
- anthology-candidate
date: '2026-10-09'
published: '2023-05-30'
arxiv: '2305.18962'
first_author: 'Lin'
keywords:
- 'hyperbolic geometry'
- 'diffusion geometry'
- 'diffusion maps'
- 'hierarchical representation learning'
- 'Poincaré half-space'
- 'product manifold'
- 'heat kernel on trees'
- 'Hellinger distance'
- 'snowflake metric'
- 'single-cell RNA sequencing'
implementations: []
summary: >-
  Lin, Coifman, Mishne and Talmon (2023), ICML 2023 (PMLR 202),
  [ARXIV-2305.18962](https://arxiv.org/abs/2305.18962). Recovers a latent tree from point-cloud or graph
  data without learning: diffusion densities at dyadic time scales are
  embedded in a product of Poincaré half-spaces, and the ℓ1 product
  distance, a scale-weighted Hellinger sum, is proved equivalent up to
  constants to a thresholded snowflake min{1, d_T^(2α)} of the tree
  metric when the operator behaves like the heat kernel on a tree. It
  keeps local tree neighbourhoods (best MAP on the benchmarks) but not
  global distances (higher distortion than hyperbolic MDS).
---
<!-- inactive-ok-file: THEORY-185 CLAIM-119 QUESTION-025 — Proposed or open; cited as the question and claim this reading bears on -->

# LIT-tmpjwrpt: Hyperbolic Diffusion Embedding and Distance for Hierarchical Representation Learning

Ya-Wei Eileen Lin, Ronald R. Coifman, Gal Mishne and Ronen Talmon (2023),
*Proceedings of the 40th International Conference on Machine Learning*,
PMLR 202:21003–21025 — [ARXIV-2305.18962](https://arxiv.org/abs/2305.18962)

## Key takeaways

- **The construction.** From a kernel W = exp(−d²/ε), doubly normalised
  into a Markov matrix P (for a given graph, P = exp(−L)), each point i
  gets densities φ_i^k = √(P^(2^−k) e_i) at times 2^−k, k = 0, …, K. Each
  is a point [φ_i^k, 2^(kα−2)] of the half-space H^(n+1), so fine scales sit
  high and coarse scales low. The hyperbolic diffusion embedding is the
  tuple of K + 1 such points; the hyperbolic diffusion distance (HDD) is the
  ℓ1 sum of their hyperbolic distances, which reduces to
  Σ_k 2 sinh⁻¹(2^(1−kα) ‖φ_i^k − φ_j^k‖₂). No training and no tree is
  given; the hierarchy is read off the distance.
- **What is proved.** Proposition 1: the single-scale distances shrink
  geometrically with k, within constants, as 2^−(k₂−k₁)α. Theorem 1, in
  the form the appendix proves (Proposition C.4 with β = 2): if the kernel
  obeys Gaussian-type upper and lower bounds and a Hölder bound in the tree
  distance d_T, the multiscale distance is equivalent up to constants to
  min{1, d_T^(2α)} for 0 < α < 1/2. The heat kernel on a tree is asserted to
  meet the bounds (Lemmas C.4–C.6, stated with citations, not proved). The
  argument adapts Leeb and Coifman's multiscale diffusion distance, which
  recovers geodesic distance on non-negatively curved manifolds, to trees.
- **What the theorem does not give.** A snowflake d_T^(2α) with 2α < 1
  preserves the order of distances but not the tree metric itself, and the
  threshold means points farther apart than a fixed radius are only known
  to be far. The main text drops the threshold and says the result is
  "approximately 0-hyperbolic" as α → 1/2, which is not proved.
- **What the experiments show.** On Sala et al.'s five graph benchmarks HDD
  has the best mean average precision (1.0 on the balanced and
  phylogenetic trees) but higher average distortion than tree
  representation, hyperbolic MDS, the SGD method and Sarkar's construction;
  the authors call it a local-over-global trade-off. On two scRNA-seq
  datasets, with the cell-type tree held out for evaluation, it has the
  best MAP and nearest-centroid accuracy. Ablations: the ℓ2 product
  distance, any single scale, and a Euclidean distance on the same
  multiscale embedding all do worse, the last by a wide margin.

## Standing in the record

Filed at the owner's request on 2026-10-09, in a batch of six works on
hierarchy and hyperbolic geometry asked for after the record opened
[QUESTION-025](../questions.d/QUESTION-025.md). Read the same day ([NOTE-tmpki7xw](../notes.d/NOTE-tmpki7xw.md)).

It bears on that question only at a distance. [QUESTION-025](../questions.d/QUESTION-025.md) asks whether
attributes that imply each other keep linear directions in a co-occurrence
embedding ([THEORY-185](../theory.d/THEORY-185.md), [LIT-863](LIT-863.md)). This paper has no attributes and no
directions. It represents a hierarchy as a metric, recovered across scales
of diffusion, and it finds a Euclidean distance on the same multiscale
features far worse at it. What it supplies is a second, metric route to a
latent hierarchy against which a linear-direction account could be
compared, not an answer. Its object is also a tree, which is narrower than
the concept lattice of [CLAIM-119](../claims.d/CLAIM-119.md).
