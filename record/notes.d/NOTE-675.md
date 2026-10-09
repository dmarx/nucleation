---
number: 675
status: Read
formerly:
- NOTE-tmpki7xw
paper: 'LIT-870'
title: 'Hyperbolic Diffusion Embedding and Distance'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full from the arXiv PDF of v1 (arXiv:2305.18962, 30 May 2023,
    23 pp., the ICML 2023 camera-ready text with the PMLR 202 footer), text
    extracted with pdftotext. §§1–7 read; Appendix A (background), B (proof
    of Proposition 1) and C (proof of Theorem 1: C.1–C.4) read with every
    step followed; Appendices D–E (baselines, datasets, implementation,
    toy example, per-dataset tables, ablations, run times) read. Figures read
    from captions and text; Figure 2–4 and 6 values taken from the tables
    that repeat them. The lemmas the proof quotes (Leeb and Coifman 2016,
    Lemmas 3–4; the tree heat-kernel bounds of Lemmas C.4–C.6 from McKean,
    Grigor'yan and Noguchi, Frank and Kovarik, Zelditch) were not checked
    in their sources. The code was not run.
date: '2026-10-09'
summary: >-
  Embeds each point's diffusion densities at dyadic time scales in a
  product of Poincaré half-spaces and proves that the ℓ1 product distance,
  a scale-weighted Hellinger sum, is equivalent up to constants to a
  thresholded snowflake min{1, d_T^(2α)} of a latent tree metric when the
  diffusion operator behaves like the heat kernel on that tree. The tree
  heat-kernel bounds are cited rather than proved and one Hölder step holds
  only for d_T ≥ 1. Empirically it keeps tree neighbourhoods (best MAP) and
  not global distances (more distortion than hyperbolic MDS).
---
<!-- inactive-ok-file: THEORY-185 CLAIM-119 QUESTION-025 — Proposed or open; cited as the question and claim this reading bears on -->

# NOTE-675: Hyperbolic Diffusion Embedding and Distance

## Contribution

A non-learned construction that takes observations with a hidden
tree-like structure (or a graph) and returns a distance provably
comparable to a power of the hidden tree distance. Hyperbolic embedding
methods before it mostly needed the tree, or tree distances, as input
(Nickel and Kiela's Poincaré embeddings, Sala et al.'s combinatorial and
MDS methods, Sonthalia and Gilbert's TreeRep), or fitted an objective
without a recovery guarantee. Diffusion-geometry multiscale distances
before it (Leeb and Coifman 2016) recovered geodesic distance on
non-negatively curved manifolds, and the authors show (Appendix E,
referred to) that they fail on trees. The combination, densities at many
diffusion scales placed in hyperbolic space and summed in ℓ1, is new.

## Key insight

Scale in diffusion and height in the hyperbolic half-space are made the
same coordinate. A point's density after a short diffusion is local and
is placed high in the half-space, where hyperbolic distances are small;
after a long diffusion it is coarse and is placed low, where they are
large. Summing the per-scale hyperbolic distances therefore weights
coarse disagreement, two points that differ already at the level of big
branches, exponentially more than fine disagreement, which is how a tree
metric grows. The hierarchy is not stored in any coordinate; it is in how
the distance accumulates over scales.

## Assumptions

- **Data model.** Points x_i lie in a hidden "hierarchical metric space"
  (T, d_T); the kernel W(i, j) = exp(−d²(x_i, x_j)/ε) with a suitable
  ambient distance d, doubly normalised (S⁻¹WS⁻¹, then row-normalised),
  gives P, which is assumed to approximate pointwise the heat kernel
  a_t of T: P^t(i, j) ≈ a_t(x_i, x_j). The paper cites the manifold limits
  (n → ∞, ε → 0; Coifman and Lafon, Singer, Belkin and Niyogi) for this.
  Those limits are for manifolds; that a point cloud's P approximates the
  heat kernel of a *tree* is assumed, not shown.
- **Kernel conditions** (Appendix C.2), with d_T and a scaling exponent β:
  √a_t(x, x′) ≤ t^(−n/2β) f₁(d_T/t^(1/β)) (upper bound, f₁ decreasing with a
  moment condition); √a_t(x, x′) ≥ t^(−n/2β) g₁(d_T/t^(1/β)) for d_T < R
  (lower bound); and |√a_t(x, y) − √a_t(x′, y)|² ≤ (d_T(x, x′)/t^(1/β))^(2Θ)
  t^(−n/β) f₁(d_T(x, y)/t^(1/β)) when d_T(x, x′) ≤ t^(1/β) (Hölder). Here n
  is the dimension of the measure space, µ(B(x, r)) ≲ rⁿ, not the number of
  points, although the main text uses n for both and says "sufficiently
  large K and n".
- **The heat kernel on a tree** meets these with β = 2 and Θ = 1
  (Lemmas C.4–C.6, Gaussian bounds in d_T²/t). The lemmas are stated with
  citations and no proof.
- **Parameters.** 0 < α < min{1, Θ/β}, so α < 1/2 for the tree; K large
  enough that the omitted scales are negligible; dyadic times t = 2^−k ≤ 1.

## Key results

- **HDD** (Eq. 9): d_HDD(i, j) = Σ_{k=0}^{K} 2 sinh⁻¹(2^(−kα+1) ‖φ_i^k − φ_j^k‖₂),
  with φ_i^k = √(P^(2^−k) e_i). This is the ℓ1 product of the hyperbolic
  distances d_H(x, y) = 2 sinh⁻¹(‖x − y‖/(2√(x_(n) y_(n)))) between points at
  equal height 2^(kα−2).
- **Proposition 1.** For scales k₁ ≤ k₂ there is 0 < C < 1 with
  C 2^−(k₂−k₁)α ≤ d_k₂ / d_k₁ ≤ C⁻¹ 2^−(k₂−k₁)α. *Holds when:* the Hellinger
  distances between distinct points are bounded below by some c > 0 at
  every scale used, which the proof assumes; C = c/(2√2).
- **Proposition C.1** (upper bound). Under the Hölder condition and
  α < Θ/β: T̂_α(x, x′) ≲ min{1, d_T^(αβ)}.
- **Lemma C.1.** 2 sinh⁻¹(2^(−kα+1) ‖√p − √q‖₂) ≥ 2^(−kα) ‖p − q‖₁.
- **Propositions C.2–C.3** (lower bound, via Leeb and Coifman's Lemmas 3–4):
  T̂_α ≳ d_T^(αβ) for d_T < R, and T̂_α ≳ C for d_T > R; hence
  T̂_α ≳ min{1, d_T^(αβ)} (Corollary C.1).
- **Proposition C.4 / Theorem 1.** Under the three kernel conditions and
  µ(B(x, r)) ≲ rⁿ, T̂_α ≃ min{1, d_T^(αβ)}; for the tree heat kernel
  (β = 2) and 0 < α < 1/2, T̂_K ≃ d_T^(2α) "for sufficient K". *Holds when:*
  the operator is the heat kernel on the tree, or approximates it pointwise;
  "≃" is two-sided up to unspecified constants.
- **Experiments.** Graph benchmarks (balanced tree 40 nodes, phylogenetic
  tree 344, diseases 516, CS-PhD 1025, Gr-QC 4158): MAP 1.0, 1.0, 0.970,
  0.999, 0.930 — best or tied on all five; average distortion 0.144, 0.520,
  0.206, 0.274, 0.179 — better than Poincaré embeddings and hyperbolic
  hierarchical clustering, worse than hMDS, TreeRep or Sarkar's
  construction on most. scRNA-seq (Zeisel 3005 cells, CBMC 8617): MAP 0.996
  and 0.979, distortion second best, nearest-centroid accuracy 0.862 and
  0.832, best. UCI Zoo, Iris, Glass, ImaSeg: best accuracy on three of four.
  Ablation: Euclidean distance on the same embedding, MAP 0.12–0.23 and
  distortion about 0.69–0.78 against HDD's 0.93–1.0 and 0.14–0.52.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | For the heat kernel on a tree, the multiscale scaled-Hellinger distance is two-sided equivalent to the thresholded snowflake min{1, d_T^(2α)}, 0 < α < 1/2 | moderate (proof with gaps) | Appendix C; the tree kernel bounds are cited, and Proposition C.5's last inequality needs d_T ≥ 1 (see Limitations) |
| C2 | HDD recovers the hidden tree distance from observational data | weak as stated | Theorem 1 gives a snowflake up to constants, saturated beyond R, and assumes P approximates a tree heat kernel |
| C3 | Single-scale distances decay geometrically in the scale index | strong (proof) | Proposition 1, given a uniform lower bound on Hellinger distances |
| C4 | HDD keeps local tree neighbourhoods better than the compared hyperbolic methods, at the cost of global distortion | moderate | Tables 2 and 5, five graphs and two scRNA-seq sets, single seed |
| C5 | Multiscale, ℓ1 aggregation and hyperbolic distance are each needed | moderate | Ablations, Figure 6 and Table 4, on the five graphs only |
| C6 | As α → 1/2 the distance is approximately 0-hyperbolic | not supported here | asserted after Theorem 1; equivalence up to constants does not carry δ-hyperbolicity |

## Method

1. Kernel W = exp(−d²/ε) on the data (cosine distance for scRNA-seq and
   UCI data), or P = exp(−L) for a given graph.
2. Double normalisation W̃ = S⁻¹WS⁻¹, then P = D⁻¹W̃.
3. Eigendecompose P once; for k = 0, …, K form P^(2^−k) by powering the
   eigenvalues and take square roots of the rows: φ_i^k.
4. Embed (i, k) ↦ [φ_i^k, 2^(kα−2)] ∈ H^(n+1); the embedding of i is the
   (K + 1)-tuple, of dimension (n + 1)(K + 1).
5. Distance: Σ_k 2 sinh⁻¹(2^(−kα+1) ‖φ_i^k − φ_j^k‖₂); α = 1/2 in all
   experiments (outside the theorem's open range α < 1/2), K from 3 to 13.

## Concepts

- **multi-scale densities**: the rows P^(2^−k) e_i, the distribution of a
  random walk started at i after diffusion time 2^−k; the owner's
  "multiscale density geometry".
- **hyperbolic diffusion embedding (HDE)**: the map of a point to its
  tuple of per-scale points in a product of Poincaré half-spaces.
- **hyperbolic diffusion distance (HDD)**: the ℓ1 product distance
  between HDEs.
- **hierarchical metric space / hierarchical distance d_T**: a tree, or
  tree-like space, with its shortest-path metric; "0-hyperbolic metric"
  is defined as one equal to a tree's shortest-path metric (Definition
  A.3).
- **snowflake distance**: d^s for 0 < s < 1 (after Leeb).
- **hierarchical distance recovery**: the task of approximating a hidden
  d_T from observations only, as opposed to graph embedding, where the
  tree is given.

## Connections

The analysis is Leeb and Coifman's (2016) multiscale diffusion distance,
an ℓ1 sum of total-variation distances between diffused measures that is
equivalent to a snowflake of geodesic distance on non-negatively curved
manifolds, carried over to trees by replacing total variation with a
sinh⁻¹-scaled Hellinger distance and using heat-kernel bounds for
negatively curved spaces and metric trees. Diffusion maps (Coifman and
Lafon 2006) and diffusion wavelets (Coifman and Maggioni 2006) supply the
operator and the dyadic times. The hyperbolic side is Sarkar's
low-distortion tree embedding and Sala et al.'s benchmarks and baselines
(the latter filed in the same batch). Product manifolds of mixed curvature
(Gu et al. 2018) are the embedding space. The same group's later
Tree-Wasserstein distance with a latent feature hierarchy (2024) applies
the idea to features.

## Bearing on the record

- **[QUESTION-025](../questions.d/QUESTION-025.md).** Indirect. The question is whether hierarchical
  attributes keep linear directions in a co-occurrence embedding, after
  [THEORY-185](../theory.d/THEORY-185.md) ([LIT-863](../literature.d/LIT-863.md)), whose independent-attribute model makes the concept
  lattice Boolean. This paper does not touch attributes, co-occurrence or
  linear structure: its hierarchy is a tree metric among samples,
  recovered by distances across diffusion scales. Two things are of use to
  the question. First, a contrast: here hierarchy is carried by how a
  distance accumulates over scales, and one Euclidean distance on the same
  features loses most of it (Table 4), which is a reason to expect a
  single linear-spectral view not to show nesting by itself. That is my
  inference, not the paper's. Second, a candidate tool for the
  "measurement" answer [QUESTION-025](../questions.d/QUESTION-025.md) names: diffusion on a word
  co-occurrence graph, scored against a known hierarchy such as WordNet
  hypernymy, would test whether the hierarchy is present in the statistics
  at all, separately from whether it is linear. The paper does not do this.
- **[CLAIM-119](../claims.d/CLAIM-119.md).** The object recovered is a tree. A concept lattice with
  shared attributes (multiple inheritance) is not a tree metric, and
  nothing here would distinguish a lattice from a hierarchy; at most it is
  the hierarchy side of [CLAIM-119](../claims.d/CLAIM-119.md)'s contrast. No grounds proposed.
- **THEORY.** None filed. The theorem is a statement about one
  construction's metric under heat-kernel bounds, the bounds are cited
  rather than proved, and one step needs repair; the record has no account
  it would support or contradict.
- **ML practice.** It is a representation-learning method with benchmark
  comparisons, which the anthology's `graphs-and-networks` topic could
  hold; the LIT carries `anthology-candidate`.

## Limitations

- **The recovered quantity is a snowflake, thresholded.** Theorem 1 in the
  main text says d_HDD "is equivalent to d_T^(2α)"; Proposition C.4 proves
  equivalence to min{1, d_T^(αβ)} with unspecified constants. Pairs beyond
  the lower-bound radius R are only bounded below by a constant, so global
  tree distances are not recovered, which matches the higher average
  distortion the experiments report.
- **A gap in the Hölder step.** Proposition C.5 obtains
  |√h(x) − √h(x′)|² ≤ ‖∇h‖ d_T(x, x′) and then writes
  ≤ ‖∇h‖ d_T²(x, x′), which holds only for d_T ≥ 1, whereas it is applied to
  close points. With the first bound only, as I read it, the Hölder exponent
  halves (Θ = 1/2 rather than 1), the admissible range becomes α < 1/4, and
  the snowflake exponent 2α stays below 1/2. The mean-value step also
  replaces ∇h at an intermediate point y by ∇h at x′ without comment. The
  conclusion that some snowflake is recovered survives; the stated range
  does not as written.
- **Tree heat-kernel bounds cited, not proved** (Lemmas C.4–C.6), with a
  t^(n/2) volume factor whose n is the space's dimension; for a metric tree
  the appropriate local dimension is 1, and the main text conflates n with
  the sample size.
- **From data to the tree's heat kernel.** The only bridge offered is the
  manifold-limit convergence of diffusion maps; that a sampled point cloud
  with a "hidden hierarchy" yields an operator approximating a tree heat
  kernel is assumed. What kind of data-generating process has a tree as
  its diffusion geometry is not said.
- **α = 1/2 in every experiment**, outside the open interval the theorem
  covers.
- **0-hyperbolicity "as α → 1/2"** is claimed without proof, and two-sided
  equivalence up to constants does not imply it.
- **Evaluation.** MAP and distortion against a ground-truth tree exist
  only for the graphs and for the scRNA-seq cell-type trees (how cells are
  placed in the cell-type tree for d_T is not described). The UCI datasets
  have no ground-truth hierarchy and are scored by classification. One
  fixed seed; no variance over seeds for the graph tables.

## Open questions

- Does the theorem hold for α up to 1/2 once Proposition C.5 is repaired,
  for instance by a sharper Hölder bound on √a_t for the tree heat kernel
  directly?
- For which generative models of observations is the diffusion operator
  close to a tree heat kernel, and how does recovery degrade for tree-like
  but non-tree data (δ-hyperbolic with δ > 0, or a lattice with shared
  parents)?
- Can the threshold be removed, so that global tree distances, and not only
  neighbourhoods, are recovered, or is the local-over-global trade-off
  intrinsic to multiscale diffusion?
