---
number: 478
status: Proposed
formerly:
- THEORY-tmpa223w
promote_when: >-
  A complete proof that the heat kernel on a metric tree meets the
  Gaussian upper, lower and Hölder bounds the theorem uses, with the
  Hölder step of Proposition C.5 repaired for close points, and a stated
  condition under which the diffusion operator of sampled data
  approximates a tree's heat kernel. The equivalence to a thresholded
  snowflake would then be a theorem on its stated range of α, and the
  bridge from data to it an assumption with content. Better benchmark
  scores, or more datasets where the method has the best mean average
  precision, cannot settle it; neither can the experiments at α = 1/2,
  which lie outside the theorem's range.
title: "When a data set's diffusion operator behaves like the heat kernel of a latent tree, summing scale-weighted hyperbolic distances between diffusion densities over dyadic times gives a distance equivalent, up to constants, to a thresholded snowflake of the tree metric: it keeps the tree's neighbourhoods and not its global distances"
version: 1
tags:
- representation-learning
- mathematics
date: '2026-10-16'
source:
- LIT-870
answers:
- QUESTION-025
summary: >-
  Lin, Coifman, Mishne & Talmon (2023), [LIT-870](../literature.d/LIT-870.md), read in [NOTE-675](../notes.d/NOTE-675.md). The
  hyperbolic diffusion distance is equivalent to min{1, d_T^(2α)} for
  0 < α < 1/2 (Proposition C.4), under heat-kernel bounds on the tree that
  are cited rather than proved; one Hölder step holds only for d_T ≥ 1,
  and repaired, the reader finds the admissible range halves. Pairs beyond
  a radius are only known to be far, which matches the method's best mean
  average precision and its higher distortion than hyperbolic MDS on five
  graph benchmarks. A Euclidean distance on the same multiscale features
  does far worse.
---
<!-- inactive-ok-file: CLAIM-119 THEORY-196 — Proposed; the lattice claim and the tree-embedding account set beside this one, not leaned on -->

# THEORY-478: When a data set's diffusion operator behaves like the heat kernel of a latent tree, summing scale-weighted hyperbolic distances between diffusion densities over dyadic times gives a distance equivalent, up to constants, to a thresholded snowflake of the tree metric: it keeps the tree's neighbourhoods and not its global distances

## Source

Lin, Coifman, Mishne & Talmon (2023), [LIT-870](../literature.d/LIT-870.md) (ICML 2023), read in full
in [NOTE-675](../notes.d/NOTE-675.md), Appendix C's proofs included.

## What was actually shown

**The construction.** A kernel W = exp(−d²/ε) is doubly normalised into a
Markov matrix P (for a given graph, P = exp(−L)). Each point i gets
densities φ_i^k = √(P^(2^−k) e_i) at times 2^−k, k = 0, …, K, each placed in
the half-space at height 2^(kα−2), so fine scales sit high and coarse ones
low. The distance is the ℓ1 sum of per-scale hyperbolic distances,
Σ_k 2 sinh⁻¹(2^(1−kα) ‖φ_i^k − φ_j^k‖₂) (Eq. 9). No training, and no tree
is given.

**The theorem.** Proposition 1: single-scale distances shrink
geometrically with k, within constants, given a uniform lower bound on
Hellinger distances. Proposition C.4 (Theorem 1 in the main text): if the
kernel meets Gaussian-type upper and lower bounds and a Hölder bound in
the tree distance d_T, the distance is two-sided equivalent to
min{1, d_T^(αβ)}; for the tree heat kernel β = 2 and 0 < α < 1/2. The
argument adapts Leeb and Coifman's multiscale diffusion distance, which
recovers geodesic distance on non-negatively curved manifolds and which
the authors show fails on trees.

**The experiments.** On five graph benchmarks the method has the best or
tied mean average precision (1.0 on the balanced and phylogenetic trees)
but higher average distortion than hyperbolic MDS, TreeRep or Sarkar's
construction on most. On two single-cell RNA data sets, with the cell-type
tree held out, it has the best mean average precision and nearest-centroid
accuracy. A Euclidean distance on the same multiscale embedding gives mean
average precision 0.12–0.23 against 0.93–1.0 (Table 4).

**What could have come out otherwise.** The method could have recovered
global distances too. Its distortion, as the threshold predicts, shows it
does not.

## What this does not say

- **That the tree metric itself is recovered.** A snowflake d_T^(2α) with
  2α < 1 keeps the order of distances but not the metric, and beyond the
  radius R points are only known to be far. The main text's "equivalent to
  d_T^(2α)" drops the threshold.
- **That the theorem's range is as stated.** Proposition C.5 obtains a
  bound in d_T and then writes d_T², which holds only for d_T ≥ 1. With the
  first bound only, the reader finds the Hölder exponent halves and the
  admissible range becomes α < 1/4. Some snowflake is still recovered.
- **That data yield a tree heat kernel.** The bridge offered is the
  manifold limit of diffusion maps. That a sampled point cloud with a
  hidden hierarchy gives an operator close to a tree's heat kernel is
  assumed, and the tree heat-kernel bounds (Lemmas C.4–C.6) are cited, not
  proved.
- **That the distance is 0-hyperbolic as α → 1/2.** Asserted after Theorem
  1; equivalence up to constants does not carry δ-hyperbolicity. Every
  experiment uses α = 1/2, outside the theorem's open range.
- **Anything about lattices.** The object recovered is a tree. A concept
  lattice with shared parents is not a tree metric.

## Connections

- **[QUESTION-025](../questions.d/QUESTION-025.md)** asks whether hierarchical attributes keep linear
  directions in a co-occurrence embedding. This account constrains it from
  the side [NOTE-675](../notes.d/NOTE-675.md) names: here hierarchy is carried by how a distance
  accumulates over scales, and one Euclidean distance on the same features
  loses most of it. That is reason to expect a single linear view not to
  show nesting by itself, the reader's inference and not the paper's. It
  also supplies a measurement: diffusion on a co-occurrence graph scored
  against a known hierarchy would test whether the hierarchy is in the
  statistics at all.
- **[THEORY-196](THEORY-196.md)** (Sala et al.) gives a tree's near-isometric embedding in
  the hyperbolic plane and its bit cost. This construction gives up global
  distances for neighbourhoods, which is the trade-off its distortion
  numbers show.
- **[CLAIM-119](../claims.d/CLAIM-119.md)** concerns concept lattices, which a tree metric cannot
  distinguish from a hierarchy.
