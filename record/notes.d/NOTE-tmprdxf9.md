---
status: Read
paper: 'LIT-tmpt10fk'
title: 'Representation Tradeoffs for Hyperbolic Embeddings'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full from the arXiv PDF of v2 (arXiv:1804.03329v2, 24 April
    2018, 31 pp.), text extracted with pdftotext and kept as paper.txt in
    the scratchpad download directory (dl/reg-hyp-sala): abstract, §§1–6,
    the reference list and Appendices A–H. The precision argument of §3.2,
    the lower-bound proof of Lemma D.1 (both the star case and the chain
    case), the proof of Proposition 3.1 with its Hadamard-code placement,
    Proposition D.2, the h-MDS derivation (§4.1, Lemmas 4.1, E.3–E.5), the
    perturbation proof of Lemma F.1 and the convexity proof of Lemma 4.3
    (Appendix G) were followed step by step; the identity
    cosh d_H = x_0y_0 − x⃗ᵀy⃗ and Yu = ‖u‖²u under Xᵀu = 0 were re-derived.
    Tables were read; figures from captions and text. The ICML version
    (PMLR 80:4460–4469, 10 pp., from proceedings.mlr.press) was compared
    by its section headings, statements, tables and experiments: the
    same sections and results without the appendices, plus a Table 4
    (WordNet relation triples) that v2 lacks. The authors' code was not
    inspected, and Sarkar's paper, on which §3.1 rests, was not read.
date: '2026-10-09'
summary: >-
  Trees embed in the hyperbolic plane with worst-case distortion 1 + ε, but
  because a hyperbolic distance d takes about d bits to write, the
  coordinates need Θ((ℓ/ε) log deg_max) bits in the plane: cheap in
  branching, expensive in depth. More dimensions divide the upper bound by
  r for bushy trees. For general metrics, an exact hyperbolic MDS by PCA on
  cosh of the distances after centring at a new mean, with a perturbation
  bound growing as sinh² of the diameter; hyperbolic PGA has spurious local
  minima and only a local-convexity guarantee.
---
<!-- inactive-ok-file: THEORY-tmpzw8vz THEORY-185 QUESTION-025 CLAIM-119 LIT-267 — Proposed or open; cited as what this reading produced and the accounts it bears on -->

# NOTE-tmprdxf9: Representation Tradeoffs for Hyperbolic Embeddings

## Contribution

Before this paper, hyperbolic embeddings of hierarchies were learned by
gradient descent (Nickel and Kiela; Chamberlain et al.), and the fact that
trees embed in the hyperbolic plane with arbitrarily low distortion was
Sarkar's. This paper puts a price on that fact. Hyperbolic coordinates
need precision linear in distance, so a distortion-(1 + ε) embedding of a
tree needs Θ((ℓ/ε) log deg_max) bits per coordinate in H². The upper bound
comes from Sarkar's construction, and a matching lower bound from an
explicit tree. Higher dimensions, using error-correcting codes, reduce the
upper bound by a factor r. It also gives the first exact, closed-form
hyperbolic multidimensional scaling, with a perturbation bound, and shows
that hyperbolic PGA, unlike PCA, has spurious local minima.

## Key insight

Hyperbolic space is tree-like because volume grows exponentially with
radius, as the number of nodes in a tree does with depth. The same growth
makes it expensive: telling apart the points of a hyperbolic ball of radius
d takes on the order of d bits, not log d. Branching is paid for once, in
the logarithm of the degree, which sets how far apart siblings must sit
before they separate. Depth is paid for linearly, because every level adds
τ to the distance from the root. So the representation is economical for
short, bushy hierarchies and loses its advantage on long chains.

## Assumptions

- **Input**: a finite, unweighted (or, after Steiner nodes, weighted) tree,
  or a graph first embedded into a tree. A graph is mapped to a tree with
  Steiner nodes (Abraham et al.), which costs distortion
  (1 + δ)^(c₁ log n) under their δ-4-points condition; the end-to-end bound
  is that times (1 + ε).
- **Fidelity measures**: worst-case distortion D_wc (max expansion over
  min contraction) for the theory; average distortion D and MAP of graph
  neighbours for the experiments. Sarkar's construction is Delaunay, so its
  MAP on a tree is 1 at any τ that separates children into disjoint cones.
- **Precision model**: bits are counted as −log(1 − ‖x‖) for a point x of
  the Poincaré ball, the bits needed so that 1 − ‖x‖ does not round to
  zero in fixed point. Appendix D's covering argument makes "distance d
  costs Θ(d) bits" model-independent, but only for representing every
  point of a ball to a fixed tolerance.
- **Lemma D.1** is stated for embeddings into H², of one family of graphs
  (a root with deg_max chains of length m), with worst-case distortion
  1 + ε.
- **h-MDS** assumes the distances come exactly from points in H^r; the
  perturbation analysis is second order in ‖ΔH‖_∞ and assumes
  ‖ΔH‖_∞ ≤ ‖H‖_∞.
- **Lemma 4.3** concerns a geodesic through the (Karcher) mean, after
  reflecting the mean to the origin, in H² for exposition.

## Key results

- **Tree-likeness (§2, Figure 1).** For ‖x‖ = ‖y‖ = t → 1,
  d_H(x, y)/(d_H(x, 0) + d_H(0, y)) → 1 at any fixed angle, while the
  Euclidean ratio stays constant.
- **Sarkar's construction (§3.1–3.2).** Edge scaling
  τ = ((1 + ε)/ε)·2 log(deg_max/(π/2)) gives D_wc ≤ 1 + ε; linear time.
  The largest distance is O((ℓ/ε) log deg_max), hence that many bits.
- **Bits per distance (§3.2, App. D).** d = acosh(1 + 2‖z‖²/(1 − ‖z‖²))
  gives (cosh d + 1)/2 = 1/(1 − ‖z‖²) ≥ (1/2)/(1 − ‖z‖), so representing
  distance d needs about log(cosh d + 1) ≈ d bits. Covering: at least
  log(V(d)/V(ε)) bits, n log(d/ε) in ℝⁿ, Θ(d) in hyperbolic space.
- **Lemma D.1 (lower bound).** Any embedding of the chain graph G_m into
  H² with D_wc ≤ 1 + ε needs −log(1 − ‖x‖) = Ω((ℓ/ε) log deg_max) bits,
  ℓ = 2m. Proof: some pair of children subtends an angle at most
  2π/deg_max; equalising the children's radii is without loss; bounding
  the hyperbolic distance with the small-angle substitution
  √(2(1 − cos θ)) = θ gives −log(1 − v) ≥ ((1 + ε)/ε)(log deg_max −
  log((2 + √6)π)) for the star; the chain case uses the contraction along
  a path of length m + 1 through the root.
- **Proposition 3.1 (H^r).** Distortion at most 1 + ε with
  O((1/ε)(ℓ/r) log deg_max) bits per component for r ≤ log deg_max + 1,
  and O(ℓ/ε) for larger r. Proof: a spherical-code lower bound
  A(r, θ) ≥ (1 + o(1))√(2πr) cos θ/(sin θ)^(r−1) lets deg_max cones of
  half-angle θ/2 with θ = asin(deg_max^(−1/(r−1))) fit around a node, and
  τ = −log tan(θ/4) = O((1/r) log deg_max). Placement in practice: the
  vertices of the hypercube with components ±1/√r indexed by a Hadamard
  code [2^k, k, 2^(k−1)], which puts up to r children at pairwise
  Euclidean distance √2. Beyond r ≈ log deg_max no dimension helps,
  since the minimum pairwise angle tends to π/2 and τ = Ω(1).
- **Proposition D.2 (transitive closure).** Weighting each edge from a
  node at depth s to its children by 2^s makes every ancestor nearer than
  any non-ancestor: d(a, ancestor) ≤ 2^s − 1 < 2^s ≤ d(a, non-ancestor).
- **Lemma 4.1 and Algorithm 2 (exact h-MDS).** With Ψ(z) = Σ sinh²
  d_H(x_i, z), ∇Ψ at z = origin is −2Xᵀu. At a pseudo-Euclidean mean
  Xᵀu = 0, so Y = cosh(D) = uuᵀ − XXᵀ has u as its single positive
  eigenvector, and PCA on −Y recovers X up to rotation.
- **Lemma 4.2 / E.4–E.5.** If the points lie in a k-dimensional geodesic
  submanifold, both the Karcher and the pseudo-Euclidean mean lie in it,
  by the hyperbolic Pythagorean theorem. So centring at either preserves
  the dimension of an exact embedding.
- **Lemma F.1 (perturbation).** To second order,
  D_E(X, X̂) ≤ (2n²/λ_min) sinh²(‖H‖_∞)‖ΔH‖²_∞, λ_min the smallest
  nonzero eigenvalue of XXᵀ; the same bound holds after projection to the
  Poincaré ball (Lemma F.2) and, up to a 10⁻¹⁰ slack, for the hyperbolic
  gap. Via cosh's difference formula and Sibson's perturbation theorem for
  classical MDS.
- **PGA (§4.2, Lemma 4.3).** The PGA loss reduces to
  f(γ) = ¼ Σ acosh²(1 + d_E(γ, w_i)²) with w_i = √8 x_i/(1 − ‖x_i‖²); it
  has non-global stable minima (Figure 3). f is locally convex at γ if
  acosh²(1 + d_E(γ, w_i)²) < min(1, ‖w_i‖²/3) for every i.
- **Experiments (§5, App. H).** Combinatorial H² embedding: distortion
  0.013 and 0.006 on a balanced and a phylogenetic tree, MAP 1.0 on both,
  0.991 on the CS PhD graph, falling to 0.822 (Diseases) and 0.696 (Gr-QC)
  as graphs become less tree-like. WordNet hypernyms in two dimensions:
  MAP 0.989, against Nickel and Kiela's published 0.87 in 200. h-MDS
  gives the lowest distortion of h-MDS, PCA and Nickel and Kiela on every
  dataset but has poor MAP in floating point; a 512-bit solver reached MAP
  1.0 (Table 9: MAP 0.347 at 128 bits, 0.986 at 256). Bits per coordinate
  for the combinatorial construction at ε = 0.1 range from 102 (40-node
  balanced tree) to 2,877 (WordNet, deg_max 404); at ε = 1.0, 18 to 495.
  A learned scale and exponential distance weighting improve MAP of the
  SGD embedding on the PhD graph (Table 5).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Any finite tree embeds in H² with worst-case distortion at most 1 + ε | strong (cited proof) | Sarkar's construction, §3.1–3.2; proved in Sarkar, not here |
| C2 | Representing hyperbolic distance d to fixed tolerance needs Θ(d) bits, in any model | moderate | §3.2 computation in the Poincaré model; App. D covering sketch |
| C3 | Distortion 1 + ε in H² costs Θ((ℓ/ε) log deg_max) bits: logarithmic in degree, linear in longest path | moderate | upper bound from Sarkar's τ; Lemma D.1 lower bound, proved with a small-angle approximation used as an equality |
| C4 | In H^r the cost falls to O((ℓ/(εr)) log deg_max) for r ≤ log deg_max + 1, and dimension cannot help beyond that | moderate (upper bound only) | Proposition 3.1 via a spherical-code bound; the "cannot be improved" remark is a footnote argument, and no lower bound in H^r is proved |
| C5 | A weighted tree embedding keeps every ancestor nearer than any non-ancestor | strong (proof) | Proposition D.2 |
| C6 | Points in H^r are recovered exactly from their distances by PCA on −cosh(D) after pseudo-Euclidean centring, preserving their geodesic dimension | strong (proof) | Lemmas 4.1–4.2, E.3–E.5, Algorithm 2 |
| C7 | h-MDS error under distance perturbations grows as sinh² of the diameter | moderate | Lemma F.1, second order only, through Sibson |
| C8 | Gradient descent on hyperbolic PGA recovers the low-dimensional submanifold under bounded noise | weak | Lemma 4.3 is a local-convexity condition; the existence of a convex region around the optimum is asserted, not proved |
| C9 | Combinatorial embeddings beat optimisation-based ones on tree-like data (WordNet MAP 0.989 in 2-D vs 0.87 in 200-D) | moderate | Tables 2–4; the WordNet comparison is against published numbers on a differently prepared graph (BFS tree or weighted transitive closure vs transitive closure) |

## Method

Two routes. For trees, a combinatorial construction with no loss function:
place the root at the origin, then recursively reflect each node to the
origin by a circle inversion, put its children evenly on a hyperbolic
circle of radius τ (in H^r, at code-selected hypercube vertices rotated so
one sits at the parent), and reflect back. General graphs go through a
Steiner tree first. For metrics, an h-MDS: take cosh of the distance
matrix, eigendecompose, project from the hyperboloid to the Poincaré ball,
optionally recentre at the Karcher mean. Dimensionality is then reduced by
hyperbolic PGA, optimised by gradient descent in PyTorch on the squared
hyperbolic distance, which, unlike the distance itself, has a continuous
derivative at coincident points. The PyTorch implementation adds a learned
scale τ.

## Concepts

- **distortion D(f)**: the mean over pairs of |d_V(f(u), f(v)) − d_U(u, v)|/d_U(u, v).
- **worst-case distortion D_wc(f)**: maximum expansion over minimum
  contraction of pairwise distances; 1 is perfect and is scale-free.
- **MAP**: mean, over nodes, of average precision in retrieving each
  graph neighbour by embedded distance; local and rank-based.
- **Delaunay embedding**: one whose Voronoi cells for two nodes touch only
  if the nodes are adjacent; neighbourhoods are preserved.
- **combinatorial construction**: graph to tree (with Steiner nodes),
  then tree to Poincaré ball by Sarkar's construction or its H^r version.
- **pseudo-Euclidean mean**: a local minimiser of Σ sinh² d_H(x_i, z); the
  paper's new centre, under which h-MDS reduces to PCA.
- **h-MDS**: recovering hyperbolic points from their pairwise distances.
- **PGA**: principal geodesic analysis, the manifold generalisation of PCA
  to geodesic submanifolds through the mean.

## Connections

The construction is Sarkar's (Graph Drawing 2011). The Euclidean contrast
is cited to Linial, London and Rabinovich, as "Bourgain's theorem". The
graph-to-tree step is Abraham et al.'s Steiner-tree reconstruction of tree
metrics. The work is motivated by Nickel and Kiela's Poincaré embeddings
and Chamberlain et al.'s, and set against Ganea et al.'s entailment cones.
Krioukov et al. (2009, 2010), Verbeek and Suri, and Gromov's hyperbolic
groups are cited for the hyperbolicity of real networks; the 2010 paper is
in the same batch of filings. The h-MDS builds on Sibson's perturbation
analysis of classical scaling and differs from Wilson et al. and
Cvetkovski and Crovella, who optimise. PGA is Fletcher et al.'s, and the
loss is the one in Huckemann et al.'s geodesic PCA. The bit-cost
observation has a precedent in Eppstein and Goodrich's succinct greedy
routing in the hyperbolic plane.

## Bearing on the record

- **[QUESTION-025](../questions.d/QUESTION-025.md)** (do hierarchical attributes in co-occurrence still give
  linear attribute directions, and a non-Boolean concept lattice?). Not
  answered here. The paper has no co-occurrence model, no attributes and
  no linear directions. What it supplies is a contrast in what
  "representing a hierarchy" means. [THEORY-185](../theory.d/THEORY-185.md)'s independent binary
  attributes give a hypercube, whose concept lattice is Boolean. This
  paper represents a tree, exactly the structure independence excludes,
  by distances. Proposition D.2 makes every ancestor nearer than every
  non-ancestor, so the full ancestor relation, a non-Boolean order, is
  read off by nearest neighbours, in two curved dimensions. A hierarchy
  therefore has a faithful geometry that is not a family of half-spaces.
  An answer to [QUESTION-025](../questions.d/QUESTION-025.md) that finds linear directions failing for
  hierarchical attributes would not show that the hierarchy is absent
  from an embedding. This is my connection, not the paper's.
- **One structural point for [QUESTION-025](../questions.d/QUESTION-025.md)'s derivation arm.** Proposition
  3.1 places a node's children at hypercube vertices ±1/√r chosen by a
  binary code. Locally, siblings are coded as binary vectors with large
  Hamming separation. Whether such an embedding has linear attribute
  directions is an open question the paper does not raise.
- **[LIT-267](../literature.d/LIT-267.md)** (the Lattice Representation Hypothesis) and **[CLAIM-119](../claims.d/CLAIM-119.md)**
  (communicative categories form a concept lattice rather than a
  hierarchy). The paper's results are for trees, and degrade with
  distance from a tree. A structure in which categories share attributes
  and differ in a few constraints is not a tree. Embedding it through a
  Steiner tree costs distortion (1 + δ)^(c₁ log n), and the combinatorial
  MAP falls from about 1.0 on trees to 0.70–0.82 on less tree-like graphs.
  If [CLAIM-119](../claims.d/CLAIM-119.md) is right, the advantage this paper establishes for
  hyperbolic space is the advantage that applies least to communicative
  categories. My inference, not tested anywhere.
- **Produces [THEORY-tmpzw8vz](../theory.d/THEORY-tmpzw8vz.md)**: the precision cost of tree embeddings in
  hyperbolic space, with its scope. The record held nothing on hyperbolic
  geometry of representations before this batch.
- **Anthology.** It carries ML practice: the learned scale, the squared-
  distance loss for stable gradients and warm-starting SGD from the
  combinatorial embedding. Those belong to the anthology, which does not
  hold it, so the LIT carries `anthology-candidate`.

## Limitations

- **The lower bound is for H² and one family of graphs.** No lower bound is
  proved in H^r for r > 2, so "dimension helps only up to log deg_max" is
  an upper-bound statement plus a footnote.
- **The lower-bound proof uses approximations as equalities**:
  √(2(1 − cos θ)) = θ, and "some algebra shows" steps. The order is
  plausible, but the constants are not established.
- **The precision model is fixed-point coordinates in the Poincaré ball.**
  The covering argument shows any representation of a whole ball needs
  Θ(d) bits. It does not show that encoding a given n-node tree's
  embedding does, and a tree itself takes O(n log n) bits as a list of
  edges. The tradeoff is about coordinates, not about information.
- **The Euclidean impossibility is cited, not proved**, and is attributed
  to Bourgain through Linial et al.
- **Lemma 4.3's statement and proof are stated in different quantities**:
  the statement bounds acosh²(1 + d_E²), while the proof's condition is on
  d_E² itself. The statement appears to be the stronger, so it still
  holds, but the gap is not addressed. The region Ω where the PGA loss is
  convex and contains the optimum is asserted, not constructed.
- **The WordNet comparison is uneven.** It uses Nickel and Kiela's
  published numbers rather than a rerun. The graph is a random BFS tree,
  or a weighted tree for the transitive closure. The experiments are
  stated at ε = 0.1, which for WordNet means 2,877 bits per coordinate,
  while the introduction quotes "almost 500 bits", the ε = 1 figure.
- **Reference errors**: Sarkar [32] and Eppstein and Goodrich [11] carry
  identical venue and page numbers (Graph Drawing 2011, pp. 355–366), so
  one of them is wrong. The proof of Proposition D.2 mixes s and s₁.

## Open questions

- A lower bound in H^r for r > 2 matching Proposition 3.1, or a
  construction beating it.
- Whether the Θ(ℓ) depth cost survives other number systems (storing
  1 − ‖x‖ in floating point, or coordinates relative to the parent), which
  would separate the geometry's cost from the representation's.
- For [QUESTION-025](../questions.d/QUESTION-025.md): whether a co-occurrence model with tree-structured
  attributes yields, under a spectral or PMI embedding, the code-like
  sibling placement of Proposition 3.1, linear directions, both or
  neither.
