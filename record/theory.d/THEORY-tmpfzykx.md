---
status: Active
title: 'In the time limit, sheaf diffusion on a graph projects node features onto the harmonic space of its sheaf Laplacian, and which labellings that space can linearly separate depends on the class of restriction maps: a weighted graph Laplacian cannot separate the sides of a balanced bipartite graph, signed one-dimensional maps separate any two classes and no one-dimensional sheaf separates three, while diagonal maps with d ≥ C and orthogonal bundles with C ≤ 2d (d = 2, 4 and, against the paper, 8) separate any labelling; every separating sheaf is built from the labels'
version: 1
tags:
- network-science
- mathematics
- representation-learning
date: '2026-10-29'
source:
- LIT-tmpgqc02
summary: >-
  Bodnar, Di Giovanni, Chamberlain, Liò and Bronstein (NeurIPS 2022),
  [LIT-tmpgqc02](../literature.d/LIT-tmpgqc02.md), §3.2 and Appendix B, read in [NOTE-tmpani5h](../notes.d/NOTE-tmpani5h.md) from the
  arXiv preprint v4. Active as mathematics: each separation result has a
  proof, and Propositions 9, 10 and 13 were checked numerically. The
  paper says the orthogonal construction exists only at d = 2 and 4; it
  exists at d = 8 as well, by the Hurwitz–Radon theorem, and was built.
  The results are existential: the separating sheaf is defined from the
  class labels, so they say what a sheaf can do, not that one can be
  found without the labels.
---

# THEORY-tmpfzykx: In the time limit, sheaf diffusion on a graph projects node features onto the harmonic space of its sheaf Laplacian, and which labellings that space can linearly separate depends on the class of restriction maps: a weighted graph Laplacian cannot separate the sides of a balanced bipartite graph, signed one-dimensional maps separate any two classes and no one-dimensional sheaf separates three, while diagonal maps with d ≥ C and orthogonal bundles with C ≤ 2d (d = 2, 4 and, against the paper, 8) separate any labelling; every separating sheaf is built from the labels

## Source

Bodnar et al. (2022), [LIT-tmpgqc02](../literature.d/LIT-tmpgqc02.md), §3 (pp. 3–6) and Appendices A–B
(pp. 15–21) of arXiv 2202.04579v4; read in [NOTE-tmpani5h](../notes.d/NOTE-tmpani5h.md).

## What was actually shown

**The setting.** A connected graph with stalks ℝᵈ, the normalised sheaf
Laplacian Δ_F, and diffusion Ẋ = −Δ_F X. In the limit the features are the
orthogonal projection of the initial features onto ker Δ_F (Lemma 21,
p. 16, from Hansen and Ghrist; [THEORY-1070](THEORY-1070.md)). A class of sheaves has
"linear separation power" over a family of graphs if for every labelled
graph in it some sheaf of the class makes the limit linearly separable for
almost every initial condition (Definition 7, p. 5).

**The harmonic space of an orthogonal bundle.** For O(d) restriction maps,
dim H⁰ ≤ d, with equality exactly when transport along paths is
path-independent (Lemma 6, p. 4). This is the O(d) counterpart of
[THEORY-1082](THEORY-1082.md)'s U(1) zero-mode criterion.

**The hierarchy.**

- Symmetric maps, d = 1, are the weighted graph Laplacians (Prop. 20). On
  a connected bipartite graph with |A| = |B| they cannot separate A from B
  for any initial condition (Prop. 9). The harmonic vector is the square
  root of the weighted degree, and with F_v = F_u on every edge the two
  sides' weighted degrees sum to the same total, so the A-values cannot all
  exceed the B-values (p. 17).
- Signed maps, d = 1: −α_e at the A end and +α_e at the B end of each edge
  separates any two classes on any connected graph; the transport is −1
  across classes and +1 within (Prop. 10). Same-signed maps fail on two
  nodes (Prop. 23).
- Any d = 1 sheaf fails for three classes: dim H⁰ ≤ 1, so the limiting
  features are multiples of one vector and some class lies in the convex
  hull of two others (Prop. 11). Feature channels do not help.
- Diagonal maps with d ≥ C separate C classes, one-versus-rest per
  coordinate (Prop. 12).
- Orthogonal bundles: if the transport from a base node to each class is a
  matrix from a set {±P₀, …, ±P_{d−1}} with P₀ = I, P_kᵀ = −P_k and P_kP_l
  = −P_lP_k (points (1)–(5), pp. 20–21), the classes' limits are mutually
  orthogonal or antipodal for every projection coefficient, and up to 2d
  classes separate (Prop. 13). On regular graphs, rotations by multiples
  of 2π/C separate any C (Prop. 28).

**The correction.** The paper says such matrices exist "only in dimensions
two and four" because the octonions are non-associative (p. 21). The
conditions are those of the Hurwitz–Radon theorem: d − 1 anticommuting
orthogonal complex structures on ℝᵈ, which exist exactly for d = 1, 2, 4
and 8. At d = 8 the left multiplications by the seven imaginary octonion
units satisfy all five points. I built them, checked each condition, built
the path-independent bundle on a random connected 60-node graph with 16
classes, and projected a random initial signal onto ker Δ_F (dimension 8,
as Lemma 6 says): every class separated from the rest. So Prop. 13 holds
for d ∈ {2, 4, 8}; what happens at other d is open.

**Numerical checks.** Prop. 9 and Prop. 10 on a 10-node balanced bipartite
graph (the symmetric harmonic vector did not separate; the signed one
gave opposite signs on the two sides). Prop. 3's bound λ₀ ≤ r²/2 held on
300 random O(2) bundles.

**What could have failed.** A symmetric sheaf could have had a harmonic
vector ordering the sides of a bipartite graph; the counting identity rules
it out. A one-dimensional sheaf could have had a two-dimensional harmonic
space; Lemma 6 rules it out on a connected graph with invertible maps.

## What this does not say

- **That a separating sheaf can be found without the labels.** Every
  construction (Props. 8, 10, 12, 13, 28) assigns maps by class. The
  results bound what a class of sheaves can express. The learning problem,
  recovering such a sheaf from features, is not addressed, and Prop. 18
  (an MLP can express any sheaf) does not address it either.
- **That the geometry found is the system's.** "The right sheaf" is the one
  that solves the task. In [QUESTION-282](../questions.d/QUESTION-282.md)'s terms the correspondence is
  fixed by the target, not discovered; in [QUESTION-130](../questions.d/QUESTION-130.md)'s, it is chosen.
- **Anything at finite depth.** The results are for the projection; the
  paper's remark that exponential convergence makes them "relevant" to
  finite layers (p. 4) gives no rate.
- **That linear separability is accuracy.** The authors note that a model
  that cannot perfectly fit can still score well, and that one-layer GCNs
  do well on bipartite graphs (p. 10).
- **Anything for d outside {1, 2, 4, 8} in the orthogonal case**, either
  way.
