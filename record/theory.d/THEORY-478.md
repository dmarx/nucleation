---
number: 478
status: Active
formerly:
- THEORY-tmpa223w
title: "If the diffusion densities' Hellinger distances obey a Hölder bound with exponent θ in d_T / t^(1/β) and are bounded below once d_T exceeds a multiple of t^(1/β), then for 0 < α < θ/β summing scale-weighted hyperbolic distances between diffusion densities over dyadic times gives a distance two-sided equivalent, up to constants, to min{1, d_T^(αβ)} for pairs above the finest scale: it keeps the tree's neighbourhoods and not its global distances; whether a tree's heat kernel, or sampled data, meets the bounds, and with which θ, is not shown"
version: 2
history:
- version: 2
  date: '2026-10-19'
  note: >-
    Narrowed and promoted under ADR-047 v2, carrying out the promotion
    audit's batch 026 decision for THEORY-478. The hypothesis "behaves
    like the heat kernel of a latent tree" is replaced by the two
    Hellinger bounds the proof uses, and the admissible range becomes
    α < θ/β. LIT-870's 0 < α < 1/2 is the case β = 2, θ = 1, and
    NOTE-675's repaired Proposition C.5 gives θ = 1/2, so α < 1/4. The
    equivalence holds for pairs above the finest scale. The re-derivation
    is in the dated note below. The promote_when, the tree heat-kernel
    bounds and the bridge from sampled data, moves unchanged to
    QUESTION-tmpeikcb.
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

# THEORY-478: If the diffusion densities' Hellinger distances obey a Hölder bound with exponent θ in d_T / t^(1/β) and are bounded below once d_T exceeds a multiple of t^(1/β), then for 0 < α < θ/β summing scale-weighted hyperbolic distances between diffusion densities over dyadic times gives a distance two-sided equivalent, up to constants, to min{1, d_T^(αβ)} for pairs above the finest scale: it keeps the tree's neighbourhoods and not its global distances; whether a tree's heat kernel, or sampled data, meets the bounds, and with which θ, is not shown

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
- **[QUESTION-tmpeikcb](../questions.d/QUESTION-tmpeikcb.md)** carries the former promotion condition: whether a
  metric tree's heat kernel meets the two bounds, with which Hölder
  exponent, and when sampled data yield such a kernel.

## Note of 2026-10-19: the equivalence re-derived

From the promotion audit (batch 026, [ADR-047](../decisions.d/ADR-047.md) v2). Let d = d_T(i, j),
t_k = 2^(−k) for k = 0, …, K, and h_k = ‖φ_i^k − φ_j^k‖₂, a Hellinger
distance, so 0 ≤ h_k ≤ √2. The distance is
D = Σ_k 2 sinh⁻¹(2^(1−kα) h_k). Assume, uniformly:

- **(H1)** h_k ≤ C₁ (d / t_k^(1/β))^θ;
- **(H2)** h_k ≥ c whenever d ≥ c₀ t_k^(1/β).

Each argument 2^(1−kα) h_k lies in [0, 2√2], where concave sinh⁻¹ is
within constant factors of the identity, so D ≍ S = Σ_k 2^(−kα) h_k.
Let k* be the least k with c₀ t_k^(1/β) ≤ d. Then 2^(−k*) ≍ (d/c₀)^β,
and k* ≤ K when d ≥ c₀ 2^(−K/β).

- **Fine scales, k ≥ k*.** h_k ≤ √2 bounds their sum by a constant times
  2^(−k*α) ≍ d^(αβ). (H2) gives h_{k*} ≥ c, so the sum is also at least a
  constant times d^(αβ).
- **Coarse scales, k < k*.** By (H1), 2^(−kα) h_k ≤ C₁ d^θ 2^(k(θ/β − α)).
  For α < θ/β this geometric sum is dominated by its last term,
  ≍ d^θ (c₀/d)^θ d^(αβ) ≍ d^(αβ). This is the only use of α < θ/β.
- **Threshold.** If d ≥ c₀, every scale is separated, so S ≥ c. In all
  cases S ≤ √2/(1 − 2^(−α)). So D ≍ 1.

Hence D ≍ min{1, d^(αβ)}, with constants depending on α, β, θ, C₁, c
and c₀. Below the finest scale only the upper bound holds. With β = 2,
the source's θ = 1 gives α < 1/2. The repaired Proposition C.5's
θ = 1/2 gives α < 1/4.
