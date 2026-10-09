---
status: Read
paper: 'LIT-tmp0u9c9'
title: 'Hyperbolic Geometry of Complex Networks'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full from the arXiv PDF of v2 (arXiv:1006.5169v2, 10 September
    2010, 18 pp.), text extracted with pdftotext. Sections I–XI read, with
    every derivation followed in the text (Eqs. 1–61), not re-derived; the
    exact intersection-area formula (11) and the clustering integral (59)
    were taken as stated. Figures 1–13 read from their captions and the
    text's account of them, the plotted values not checked. The reference
    list read. References [5] (the 2009 Rapid Communication), [12] (Serrano,
    Krioukov and Boguñá's S¹ model), [27] (on hyperbolicity of
    approximately tree-like spaces) and [56] (the Internet embedding), on
    which parts of the argument rest, were not read.
date: '2026-10-09'
summary: >-
  Shows, for a model in which nodes sit in a hyperbolic disk and connect
  with a Fermi–Dirac probability of their hyperbolic distance, that the
  degree distribution is a power law with γ = 2α/ζ + 1 and that clustering
  is set by a temperature, strongest at T = 0 and gone above T = 1; that a
  circle-similarity model with power-law hidden degrees is the same
  ensemble once degree is read as radial depth; and that the configuration
  model and Erdős–Rényi graphs are its limits with the angular, metric part
  of the distance removed. Greedy routing by the coordinates is
  near-optimal and robust in its networks. No real network is embedded.
---
<!-- inactive-ok-file: THEORY-tmp1y92d THEORY-185 QUESTION-025 CLAIM-119 CLAIM-042 — Proposed or Open; cited as the accounts this reading bears on -->

# NOTE-tmprhn7r: Hyperbolic Geometry of Complex Networks

## Contribution

Before this paper, power-law degrees and strong clustering in real networks
had separate explanations (growth with preferential attachment, hidden
variables, a hidden metric on a circle). This paper derives both from one
assumption, that nodes are points of a hyperbolic space and links depend on
distance in it: heterogeneity is curvature and clustering is metric
structure. It shows the hidden-metric S¹ model of Serrano et al. is the
same ensemble as the hyperbolic H² model, recasts the ensemble as fermions
whose energies are distances, places the configuration model and classical
random graphs inside it as degenerate limits, and shows greedy routing by
coordinates is near-optimal in the networks it generates.

## Key insight

Read degree as depth. A node near the centre of the hyperbolic disk is
close to almost everyone and has high degree; a node at the rim is close
only to its angular neighbours. Hyperbolic distance between two far-out
points is approximately r + r′ + (2/ζ) ln sin(Δθ/2): a sum of two
"popularity" terms, one per node, plus one term for how far apart they are
in similarity. Exponential growth of space turns the radial terms into a
power law; the angular term is what makes neighbours of neighbours
neighbours. Strip the angular term and only the per-node terms remain, the
configuration model.

## Assumptions

- **Space.** The hyperbolic plane H² of curvature K = −ζ², in the native
  polar representation (radius equals hyperbolic distance from the origin).
  Only two dimensions are treated; §V's S¹ model is the one-dimensional
  boundary.
- **Nodes.** N nodes, angles uniform on [0, 2π), radii in [0, R] with
  density ρ(r) = α sinh(αr)/(cosh(αR) − 1) ≈ αe^{α(r−R)} (quasi-uniform; exactly
  uniform when α = ζ). R grows as (2/ζ) ln(N/ν).
- **Links.** Independent, with probability p(x) depending only on the
  hyperbolic distance x: the step Θ(R − x) at T = 0 (§IV), the Fermi–Dirac
  1/(e^{β(ζ/2)(x−R)} + 1) in general (§VI).
- **Approximations.** Large R, r and r′, so that x ≈ r + r′ + (2/ζ) ln
  sin(Δθ/2) (Eq. 6, valid for Δθ above roughly 2√(e^{−2ζr} + e^{−2ζr′}));
  sparse networks, so the degree of a node with hidden variable r is
  Poisson with mean k̄(r).
- **§V, the converse,** assumes the network already has a metric
  structure (a circle in the worked case) and power-law hidden degrees
  κ ~ κ^{−γ}, γ > 2, with connection probability a function of
  d/(μκκ′). Tests for the presence of such a metric are cited to [12],
  not given.
- **§III's rationale,** that node similarity is organised by an
  approximately tree-like hierarchy, is an assumption illustrated by
  examples (social, citation, web, phylogenetic, autonomous systems), not
  measured.

## Key results

- **Tree comparison (§II).** In H²_ζ circle length 2π sinh ζr and disk
  area 2π(cosh ζr − 1) both grow as e^{ζr}; in a b-ary tree the number of
  nodes at or within distance r grows as b^r. With ζ = ln b they are
  metrically alike. *Holds:* as growth rates; the paper calls trees
  "discrete hyperbolic spaces" informally and cites nearly isometric
  embeddings of trees into hyperbolic space.
- **Eq. 11–16 (uniform density, ζ = 1, step connection).** Exact k̄(r)
  (Eq. 11), approximately k̄(r) ≈ (4/π)N e^{−r/2}; k̄ ≈ (8/π)N e^{−R/2}, so
  R = 2 ln[8N/(πk̄)]; with N = νe^{R/2}, k̄(r) = (k̄/2)e^{(R−r)/2}; and
  P(k) = 2(k̄/2)² Γ(k − 2, k̄/2)/k! ~ k^{−3}. *Holds:* large R, sparse.
- **Eq. 29 (general α, ζ).** P(k) ~ k^{−γ} with γ = 2α/ζ + 1 when
  α/ζ ≥ ½ and γ = 2 when α/ζ ≤ ½. Average degree k̄ = 2νξ²/π with
  ξ = (γ − 1)/(γ − 2) (Eq. 31). *Holds:* large R; the control of k̄ by ν
  is poor as α → ζ/2, where k̄ grows polylogarithmically in N (Eq. 26).
- **§V equivalence.** Under κ = κ₀e^{ζ(R−r)/2} (Eq. 37), the S¹ model's
  argument χ = d/(μκκ′) becomes e^{ζ(x−R)/2} with x the approximation (6)
  (Eq. 39), node radii come out with α = ζ(γ − 1)/2, and k̄(r) agrees;
  so the two models generate statistically the same ensembles.
  *Holds:* under approximation (6), with R fixed as in (25) and
  ν = πμκ₀² (Eq. 38).
- **§VI.** With p(x) = 1/(e^{β(ζ/2)(x−R)} + 1), the ensemble is the
  exponential random graph with link fields ω_ij = β(ζ/2)(x_ij − R)
  (Eq. 45): fermions with energy x, chemical potential R, Boltzmann
  constant 2/ζ, temperature T = 1/β. The integral
  I = ∫₀^∞ p̃(χ)dχ = (π/β)/sin(π/β) is finite only for β > 1, and R
  diverges as −ln|β − 1| on either side of T = 1: a phase transition.
- **§VII.** Cold regime (T < 1): the same power law, γ = 2α/ζ + 1.
  Hot regime (T > 1): k̄(κ) ∝ κ^β and γ = 2αT/ζ + 1 (Eqs. 53–54), still
  above 2.
- **§VIII.** Cold regime: average clustering decreases from its maximum
  at T = 0, almost linearly, to zero at T = 1 (Fig. 6, simulation against
  numerical integration). Degree-dependent clustering c̄(κ) ~ κ^{−1} for
  large κ; at β = 2, γ = 3 it is given exactly by Eq. 60, with
  c̄(κ₀) = ln(27/16) ≈ 0.52 and c̄(κ) → (ln 4)κ₀/κ. Hot regime: clustering
  is zero in the thermodynamic limit.
- **§IX.** With ζ, T → ∞ and η = ζ/T fixed, x_ij = r_i + r_j, the fields
  decouple (ω_ij = ω_i + ω_j) and p_ij = k̄(r_i)k̄(r_j)/(k̄N): the
  configuration model. With α, ζ fixed and T → ∞, p → k̄/N: Erdős–Rényi
  G(N, p).
- **Fig. 8.** The Internet's autonomous-system graph (CAIDA Archipelago)
  against an H² network with α = 0.55, ζ = 1, β = 2 (γ = 2.1): the degree
  distribution, average neighbour degree and degree-dependent clustering
  match.
- **§X (simulation, N = 10⁴, k̄ = 6.5).** At T = 0, γ = 2.1, greedy
  forwarding succeeds for 99.92% (OGF) and 99.99% (MGF) of pairs, OGF's
  maximum hop stretch is 1, and success falls and stretch rises as γ grows
  toward 3 (Fig. 9). With up to 10% of links removed, MGF at γ = 2.1
  still succeeds for over 99% (Fig. 10). Efficiency falls with T (Fig. 11).
  In the configuration-model limit success never exceeds 40%; in
  Erdős–Rényi graphs it is 0.17% and 0.21%.
- **§X E.** At T = 0 a node of expected degree κ covers the angular
  sector θ(κ, κ′) = 4πμκκ′/N of nodes of degree κ′; "bridges", nodes
  linked to every node above a degree threshold, exist in large networks
  only when γ < 3. Greedy paths zoom out to the core, turn, and zoom in.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Distance-thresholded random graphs on a hyperbolic disk with quasi-uniform node density have power-law degrees with γ = 2α/ζ + 1 (α/ζ ≥ ½) | strong for the model (asymptotic derivation, confirmed by simulation in Fig. 4) | §IV, Eqs. 11–29 |
| C2 | The S¹ hidden-metric model with power-law hidden degrees and the H² model are the same ensemble under κ = κ₀e^{ζ(R−r)/2} | moderate (a change of variables exact only under the large-distance approximation (6); "one can confirm in simulations", not shown) | §V, Eqs. 37–40 |
| C3 | Any heterogeneous network with some metric structure has an effective hyperbolic geometry | weak as stated (it is C2 generalised: argued for a boundary ∂X other than S¹ by analogy, and the presence of the metric is assumed) | §V's last paragraph, §XI |
| C4 | With Fermi–Dirac connection the ensemble has a phase transition at T = 1; clustering is positive and decreasing below it and zero above it | moderate (the divergence of R and the hot-regime zero are derived; the cold-regime curve is numerical) | §§VI, VIII, Fig. 6 |
| C5 | The configuration model and Erdős–Rényi graphs are limits of the ensemble in which the metric (angular) term of the distance vanishes | strong (derivation) | §IX, Eq. 61 |
| C6 | Complex networks are hyperbolic because similarity among their nodes is organised by an approximately tree-like hierarchy | weak (informal argument with examples) | §III, Fig. 2 |
| C7 | Greedy routing by hyperbolic coordinates is near-optimal and robust to link failure in the model's networks at small γ and T, and fails in the degenerate limits | moderate (simulation on 10⁴-node networks, five instances per γ) | §X, Figs. 9–12 |
| C8 | Real networks such as the Internet "have the optimal structure" for routing | weak (inferred from C7 and from a fit of three statistics in Fig. 8; no real network is embedded or routed here) | §XI |

## Method

A latent-space random-graph model, analysed by the hidden-variable
formalism of Boguñá and Pastor-Satorras: compute the expected degree
k̄(r) of a node at radius r as the node density integrated over the
intersection of its distance-R disk with the disk holding all nodes,
then mix the Poisson propagator over the radial density. Clustering is the
probability two neighbours of a node are adjacent, an integral over two
rescaled angular distances. The statistical-mechanics reading identifies
the connection probability with the Fermi–Dirac occupation of the
exponential random graph with link-coupled fields. Navigation is
simulated.

## Concepts

- **native representation**: polar coordinates on H² in which the radial
  coordinate is the true hyperbolic distance from the origin.
- **quasi-uniform density**: radial density ∝ sinh(αr), α > 0; uniform
  when α equals ζ. The paper reads e^α as the average branching factor of
  the hidden hierarchy.
- **hidden variable**: a node property (here r, or κ in S¹) on which the
  node's link probabilities depend; the degree is drawn conditionally on
  it.
- **effective hyperbolic geometry**: the result of §V; the radial
  coordinate obtained from a node's expected degree and the similarity
  coordinate on the boundary together form a hyperbolic space.
- **temperature** T = 1/β: the parameter of the Fermi–Dirac connection
  probability that controls clustering; not a physical temperature.
- **greedy forwarding**: pass the message to the neighbour hyperbolically
  closest to the destination; OGF drops at a local minimum, MGF excludes
  the current node and drops only on returning to the previous one.
- **stretch**: hop stretch (greedy hops over shortest hops), and
  hyperbolic stretch (summed hyperbolic length of a path over the
  source–destination distance).
- **bridge**: a node linked to every node above some expected degree.

## Connections

It extends the authors' own Rapid Communication of 2009 (ref. [5]) and the
S¹ model of Serrano, Krioukov and Boguñá (2008, ref. [12]), which it shows
equivalent to H². The degree calculation uses the hidden-variable
formalism of Boguñá and Pastor-Satorras (2003); the statistical mechanics
is Park and Newman's exponential random graphs (2004); the dendrogram view
of hidden hierarchies is Clauset, Moore and Newman (2008); degree-dependent
clustering as a signature of hierarchy is Ravasz and Barabási. Hierarchical
paths are Trusina et al. (2004). The tree–hyperbolic correspondence and the
disk-to-H³ map are cited to the metric-geometry literature (refs. [21–27]),
and the AdS/CFT analogy for the radial dimension is offered as an analogy.
The actual embedding of the Internet into H² is deferred to ref. [56].

## Bearing on the record

- **No account in the record covered this.** It produces [THEORY-tmp1y92d](../theory.d/THEORY-tmp1y92d.md),
  stating the model result with its scope: what the geometry produces in
  the model, the S¹ equivalence, and the degenerate limits, and not the
  claim that real networks are hyperbolic.
- **[QUESTION-025](../questions.d/QUESTION-025.md).** It does not answer the question, which is about
  whether linear attribute directions survive hierarchical attributes in
  co-occurrence embeddings. Three points bear on it, and all three are my
  connections, not the paper's.
  - *Additivity is the degenerate case here too.* In the sparse cold
    regime, by Eqs. 6 and 41, ln p_ij ≈ −β(ζ/2)(r_i + r_j − R) −
    β ln sin(Δθ_ij/2). The log link probability is a per-node sum (the
    analogue of [THEORY-185](../theory.d/THEORY-185.md)'s independent, multiplicative factors) plus a
    pairwise term that does not factor. §IX shows that removing the
    pairwise term leaves the configuration model and destroys the metric
    and clustering. So in this model the structure lives in exactly the
    part of the log co-occurrence that [THEORY-185](../theory.d/THEORY-185.md)'s independence assumption
    sets to zero.
  - *What a spectral embedding would find.* The pairwise term is a
    translation-invariant kernel on the circle, so its eigenvectors are
    Fourier modes in θ, not directions for attributes. A spectral embedding
    of this model's log link probabilities would recover the radial term
    and circular harmonics. I have not worked this through: it is a
    prediction, not a result.
  - *Its "hierarchy" is not a lattice of attributes.* The radial
    coordinate ranks nodes by expected degree (popularity), and the tree is
    a dendrogram of similarity groups. No attribute implies another.
    §III's Fig. 2, where each node is a disk of attributes in ℝ² and nested
    or overlapping disks become points in H³, is the nearest the paper
    comes to attributes; it represents overlap of attribute regions as
    distance and gives no meet or join. So it offers a generative model of
    the kind [QUESTION-025](../questions.d/QUESTION-025.md)'s "derivation" asks for only in part: a stated
    hierarchy, with a non-additive interaction term, but not an implication
    structure among binary attributes.
- **[CLAIM-119](../claims.d/CLAIM-119.md) and [CLAIM-042](../claims.d/CLAIM-042.md).** Fig. 2's picture, objects as regions of an
  attribute space at several scales, with containment giving a tree and
  partial overlap adding cycles that keep the structure "not strictly a
  tree, but hyperbolic", is close to [CLAIM-042](../claims.d/CLAIM-042.md)'s "an object is the
  intersection of constraint regions at several levels". It is evidence
  that such structure has a geometric home in negatively curved space; it
  says nothing about whether it forms a concept lattice ([CLAIM-119](../claims.d/CLAIM-119.md)), since
  the H³ representation keeps distance and loses intersections. The
  bearing is weak and is my reading, not the paper's.
- **[LIT-004](../literature.d/LIT-004.md) and [LIT-020](../literature.d/LIT-020.md)** treat network curvature as a discrete
  edge-level quantity (Ollivier–Ricci, Forman–Ricci); this paper's
  curvature is of a latent continuous space. The two are related in later
  literature, not here.
- No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- Everything proved is about the model. The fit to the Internet in Fig. 8
  matches three summary statistics with three parameters; no real network
  is embedded, no coordinates are inferred, and routing on a real network
  is not tested here.
- §V's converse holds under approximation (6) and assumes a metric
  structure is present; it shows a model equivalence, not that a given
  heterogeneous network has a hyperbolic geometry.
- §III's argument that hierarchy implies hyperbolicity is informal; the
  paper says the hierarchy need only be "approximately a tree" and cites
  [27] for its negative curvature, without stating the condition.
- Only H² is analysed. Higher-dimensional hyperbolic spaces, and the
  disk-to-H³ example of Fig. 2, are mentioned, not worked.
- Clustering below T = 1 is obtained numerically except at β = 2, γ = 3.
- The routing results are simulations at one size (N = 10⁴) and one
  average degree, averaged over five instances per γ.

## Open questions

- Whether real networks have this geometry: settled only by inferring
  coordinates for a real network and showing they predict its links and
  routing better than degree plus a flat similarity space. The paper names
  constructive mapping as open and points to its own inference work [56].
- What dimension the similarity space needs, and how results change in
  Hᵈ for d > 2.
- The spectral question raised above for [QUESTION-025](../questions.d/QUESTION-025.md): what the spectrum of
  ln p_ij in this model is, and whether any attribute-like linear
  structure survives in it.
