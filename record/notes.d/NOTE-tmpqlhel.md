---
status: Read
paper: 'LIT-tmp9eclr'
title: 'Emergent Hyperbolic Network Geometry'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full from the arXiv PDF of v2 (arXiv:1607.05710v2, 29 December
    2016, 19 pp.), text extracted with pdftotext. Abstract, Introduction,
    Results, Discussion and Methods read, every derivation followed (Eqs.
    1–21), the master-equation solution (Eqs. 14–19) checked for its
    exponent and its d + s = 1 case, not re-derived in full. Table I read;
    Figures 1–4 read from their captions and the text's account of them,
    the plotted values not checked. The reference list read. The authors'
    earlier papers on which the fitness and "quantum statistics" remarks
    rest (refs. 9–11, network geometry with flavor and complex quantum
    network manifolds) and the Apollonian-packing literature (refs.
    51–54) were not read. v1 (19 July 2016) was not read.
date: '2026-10-09'
summary: >-
  Shows that simplicial complexes grown by gluing d-simplices to
  (d − 1)-faces, by a rule with no geometry in it, have exponential or
  power-law degrees (γ = 2 + 1/(d + s − 1)) by a master equation, high
  clustering and modularity, and a tree as their dual; and draws them, with
  all links of equal length, as ideal simplices tiling the Poincaré ball.
  The hyperbolicity is that drawing, which the authors say depends on the
  equal-length assumption; it is not measured or proved. A fitness on faces
  gives a simulated transition to growth in one direction.
---
<!-- inactive-ok-file: THEORY-tmpp6w9v THEORY-tmp1y92d THEORY-tmpzw8vz THEORY-tmpzjtfu THEORY-185 THEORY-186 QUESTION-025 CLAIM-119 — Proposed or Open; cited as the accounts this reading bears on -->

# NOTE-tmpqlhel: Emergent Hyperbolic Network Geometry

## Contribution

Before this paper, the hyperbolic account of complex networks (Krioukov
et al., [LIT-tmp0u9c9](../literature.d/LIT-tmp0u9c9.md)) put the geometry first: nodes are placed in a
hyperbolic space and links follow from distance. This paper builds a
growth model in which the geometry comes last. Simplicial complexes grown
by a purely combinatorial attachment rule have the usual network
signatures together (small world, high clustering, high modularity, and
scale-free degrees above a dimension threshold), with the degree law
derived exactly, and their natural drawing with equal links is a tiling
of hyperbolic d-space by ideal simplices. It also extends the
growing-network family (Barabási–Albert, random recursive trees) to
higher dimension, with the flavor s and dimension d together setting the
degree exponent.

## Key insight

Glue each new simplex to exactly one face of the old complex and the
simplices form a tree. A tree's ball of radius D holds e^D nodes, which no
flat space can hold with equal edges, and a tree of ideal simplices is
exactly what tiles hyperbolic space. So "hyperbolic geometry emerges" here
because "a tree of equal simplices" is a tiling of H^d; the growth rule
need only make the dual a tree. What the rule adds is the statistics:
which faces are chosen, and so the degrees, clustering and communities.

## Assumptions

- **Growth by single-face gluing.** Each step adds one node and one
  d-simplex, glued along one existing (d − 1)-face; nothing is ever
  removed or rewired. This is what makes the dual a tree.
- **Attachment** with probability Π_α = (1 + s n_α)/Σ(1 + s n_α′),
  s ∈ {−1, 0, 1}, n_α the number of simplices on face α minus one; with
  fitness, Π_α ∝ η_α(1 + s n_α), η_α = e^{−βε_α}, ε_α the sum of node
  energies drawn from g(ε).
- **Equal link lengths.** The geometric conclusion assumes every link of
  the complex has the same length. The paper calls this a
  "proto-geometry" and says that without it the curvature is not
  determined.
- **The embedding** is chosen, not derived: ideal simplices in the
  Poincaré ball, initial nodes on the unit sphere with Σ r_i = 0, each new
  node at r_i = Σ_{j⊂α} r_j / |Σ_{j⊂α} r_j|. Its uniqueness as the
  space-filling embedding is asserted.
- **Mean-field rates.** The degree distribution is the stationary
  solution of the master equation for the average number of nodes of
  degree k, in the large-t limit.

## Key results

- **Degree rate** (Eq. 14). A node of degree k gains a link at rate
  m̃(k) = [d + (d − 1 + s)(k − d)]/((d + s)t), for (d, s) ≠ (1, −1).
- **Degree distribution** (Eqs. 16–19). For d + s = 1, P(k) =
  (d/(d+1))^{k−d}/(d+1), k ≥ d. For d + s > 1, P(k) = [(d+s)/(2d+s)]
  Γ[1 + (2d+s)/(d+s−1)]/Γ[d/(d+s−1)] · Γ[k − d + d/(d+s−1)]/Γ[k − d + 1
  + (2d+s)/(d+s−1)], with tail exponent γ = 2 + 1/(d + s − 1) ≤ 3. So the
  complex is scale-free exactly when d > 1 − s. For d + s = 0 it is a
  chain. Checked against single runs of N = 10⁵ (Fig. 2).
- **Clustering and modularity** (Table I, N = 10⁴, 20 realisations,
  generalised Louvain). Modularity 0.97/0.94/0.90 for d = 2 and
  0.91/0.85/0.80 for d = 3 (s = −1/0/1); clustering 0.65/0.74/0.79 and
  0.77/0.81/0.84. Modularity falls and clustering rises with s.
- **Small world.** Stated for every (d, s) except the chain, N ≃ e^D; not
  shown with data in the text.
- **Hyperbolic embedding.** The dual is a tree (immediate from the rule).
  The ideal-simplex drawing in the Poincaré ball is given (Eqs. 2–4,
  Fig. 1); for d = 3 the projection on the boundary is a random
  Apollonian network, and for s = −1, d = 3 the complexes are stacked
  polytopes whose symmetry group is a noncompact discrete subgroup of
  SO(3,1) (cited, refs. 51–54).
- **Geometric transition with fitness** (Figs. 3–4). For s = −1, d = 2, 3,
  as β grows the norm R of the mean node position tends to 1 and the
  spread σ shrinks with N: the complex grows in one preferred direction.
  For d = 3 the maximum degree peaks at the transition, for d = 2 it does
  not. Similar transitions are reported, not shown, for s = 0, 1.
  Simulation only (N = 2500–10⁴, 500 realisations).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The degree distribution of a growing simplicial complex of dimension d and flavor s is geometric for d + s = 1 and power-law with γ = 2 + 1/(d + s − 1) for d + s > 1 | strong (derivation, mean field) | Methods, Eqs. 14–19; Fig. 2 |
| C2 | For d ≥ 2 these complexes have high clustering and high modularity, varying with d and s | moderate (simulation) | Table I |
| C3 | The dual of the complex is a tree | strong (immediate from the rule) | Results |
| C4 | With equal link lengths, the complex's natural geometry is hyperbolic d-space, filled by ideal simplices | weak (a construction and an argument) | Eqs. 2–4, Fig. 1; small-world argument; no proof of uniqueness or of hyperbolicity of the graph metric |
| C5 | The hyperbolicity depends on the equal-length assumption; with unequal lengths the complex embeds in a sphere | moderate (stated with a one-line construction) | Results, first observation |
| C6 | Hyperbolic network geometry can arise from combinatorial growth that ignores any hidden metric | weak to moderate | follows from C3–C4, conditional on C5's assumption |
| C7 | Face fitness drives a phase transition to directional growth in the hyperbolic embedding | moderate (simulation, finite-size scaling by eye) | Figs. 3–4 |

## Method

A growth process and its mean-field master equation for degrees;
simulation for clustering, modularity (generalised Louvain, a lower bound
on maximum modularity) and the fitness transition; a geometric
construction for the embedding.

## Concepts

- **flavor s**: the parameter in Π_α ∝ 1 + s n_α; −1 forces a discrete
  manifold (each face on at most two simplices), 0 is uniform, 1 is
  preferential attachment to faces.
- **incidence number n_α**: the number of d-simplices on the
  (d − 1)-face α, minus one.
- **dual network**: simplices as nodes, linked when they share a
  (d − 1)-face; a tree for these complexes.
- **ideal simplex**: a simplex of the Poincaré ball with every vertex on
  the boundary sphere, so all its edges are equal (and infinite).
- **emergent geometry**: here, geometry as the outcome of network
  dynamics rather than as the space in which the dynamics happens.

## Connections

The paper sets itself against the hidden-metric models of Krioukov et al.
([LIT-tmp0u9c9](../literature.d/LIT-tmp0u9c9.md)) and their "popularity versus similarity" growth model:
those place nodes in a hyperbolic space and link by distance, so the
geometry causes the network. Here the geometry is read off the network.
The degree-rate equation is the standard master-equation treatment of
growing networks (Dorogovtsev and Mendes; Krapivsky, Redner and
Leyvraz), and the fitness is Bianconi and Barabási's. The model is the
authors' "network geometry with flavor" of refs. 9–10, of which this paper
is the hyperbolic reading. The Battiston et al. review ([LIT-091](../literature.d/LIT-091.md), [NOTE-057](NOTE-057.md))
cites this school for the spectral dimension of the complexes. The
quantum-gravity motivation (causal dynamical triangulations, causal sets,
quantum graphity) is stated, not developed.

## Bearing on the record

- **[THEORY-tmp1y92d](../theory.d/THEORY-tmp1y92d.md)** (Krioukov et al.). The two are converses in framing
  only. Krioukov et al. derive network statistics from a given hyperbolic
  geometry; this paper derives network statistics from growth and then
  supplies a hyperbolic drawing. It does not show that its complexes have
  the statistics of the hyperbolic random graph, nor fit them to it, so
  it neither supports nor challenges [THEORY-tmp1y92d](../theory.d/THEORY-tmp1y92d.md)'s mechanism. Its
  power-law exponents, γ = 2 + 1/(d + s − 1), lie in (2, 3], the range
  the hyperbolic model also reaches, but by a different route.
- **[THEORY-tmpzw8vz](../theory.d/THEORY-tmpzw8vz.md)** (Sala et al.) holds that trees embed in the
  hyperbolic plane with distortion near 1. This paper is a higher-order
  case of the same fact: a complex whose dual is a tree has a hyperbolic
  drawing. Neither paper says the equal-link drawing here has bounded
  distortion; in the ideal drawing the distances are infinite, so it is a
  tiling, not a metric embedding of the graph.
- **[QUESTION-025](../questions.d/QUESTION-025.md).** No co-occurrence, no attributes, no embedding learned
  from data, so it does not answer the question. It offers one thing: a
  construction in which a node's position is the normalised sum of its
  parent face's positions, Eq. 4, so a descendant's vector is an additive
  combination of its ancestors' directions and the hierarchy is carried in
  directions on the sphere as well as in the tree of simplices. That is a
  placement rule chosen by the authors, not a derivation from statistics,
  and it says nothing about whether a learned embedding does the same.
  The paper also bears on the record's reading of "hyperbolic geometry as
  evidence of hierarchy": here the curvature is set by the equal-length
  convention, and with unequal lengths the same combinatorial hierarchy
  fits a sphere, a caution to set beside Yang et al. ([LIT-tmpocqly](../literature.d/LIT-tmpocqly.md)).
- **[THEORY-tmpzjtfu](../theory.d/THEORY-tmpzjtfu.md)** (random hierarchy model) is a different generative
  hierarchy, of symbols rather than simplices; the two share only the tree.
- No instruction for machine-learning practice; nothing for the anthology.

The reading is the source of [THEORY-tmpp6w9v](../theory.d/THEORY-tmpp6w9v.md).

## Limitations

- Hyperbolicity is not measured on the graph: no Gromov δ, no curvature
  (Ollivier or Forman, both cited), no distortion of a finite-length
  embedding. It is a drawing plus the small-world argument, which the
  paper admits is not sufficient.
- The ideal-simplex embedding puts every node at infinite distance from
  every other, and for s = 0, 1 maps sibling nodes to one point, so it is
  a picture of the dual tree more than a metric for the nodes.
- "Only one embedding can fill the entire space" and the link to Farey
  sequences are asserted without proof.
- The fitness transition is from simulations at N ≤ 10⁴; its order, its
  critical β, and the analytic link to the authors' earlier
  Bose–Einstein-type transitions are not given.
- The real-network signatures are compared qualitatively ("as most complex
  networks"); no real network is fitted.

## Open questions

- Is the 1-skeleton's graph metric Gromov-hyperbolic with δ bounded
  uniformly in N, for each flavor? That would make the hyperbolicity a
  property of the network rather than of the chosen drawing.
- Does the equal-length complex admit a finite-length embedding in H^d
  of bounded distortion, and how does the distortion scale with d and s?
- Is the fitness transition the face-level analogue of Bose–Einstein
  condensation in the fitness model, and what is its order?
