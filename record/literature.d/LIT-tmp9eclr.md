---
status: Active
status_note: 'read 2026-10-09 ([NOTE-tmpqlhel](../notes.d/NOTE-tmpqlhel.md)); worth reading as the model that turns the hidden-metric account of complex networks around: a simplicial complex grown by gluing d-simplices to (d − 1)-faces, with no geometry in the rule, comes out small-world, clustered, modular and (for d + s > 1) scale-free, with γ = 2 + 1/(d + s − 1) from a master equation. Its dual is a tree, so with every link given equal length each simplex is drawn as an ideal simplex of the Poincaré ball and each new node at the normalised sum of its parent face''s positions. That embedding, not a proof, is the paper''s case that the geometry is hyperbolic, and the authors concede it rests on the equal-length assumption (unequal lengths fit a sphere) and that the ideal-simplex distances are infinite. A fitness on faces gives a numerically observed transition in which the complex grows in one direction.'
title: 'Emergent Hyperbolic Network Geometry'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Filed and read on 2026-10-09 (NOTE-tmpqlhel) from the arXiv PDF of v2
    (29 December 2016, 19 pp.), text extracted with pdftotext: abstract,
    Introduction, Results, Discussion, Methods and the reference list,
    every derivation followed; Figures 1–4 read from captions and text, the
    plotted values not checked. The owner gave only the link; identified
    from the arXiv abstract page and API (arXiv:1607.05710, physics.soc-ph
    with cond-mat.dis-nn and cond-mat.stat-mech; v1 submitted 19 July 2016,
    v2 29 December 2016; journal reference Scientific Reports 7, 41974
    (2017)) and Crossref (DOI 10.1038/srep41974: Scientific Reports 7,
    article 41974, published online and issued 7 February 2017; authors
    Ginestra Bianconi and Christoph Rahmede; same title). `published:` is
    the arXiv v1 date, 19 July 2016, the earliest any source gives
    (ADR-002). v1 was not read. Not held in nucleation before this filing:
    a grep of record/ for the identifiers, the title and Bianconi found
    only passing mentions in NOTE-057 (the Battiston et al. review, LIT-091,
    on the "Bianconi school's" network geometry with flavor) and NOTE-075.
    Not held in the Anthology of the SOTA: a grep of its record/ (clone at
    commit d8b5ba5 of 9 October 2026, which may be stale) for the authors,
    both identifiers and the title found nothing.
tags:
- network-science
- complex-systems
- mathematics
date: '2026-10-09'
published: '2016-07-19'
arxiv: '1607.05710'
doi: '10.1038/srep41974'
first_author: 'Bianconi'
keywords:
- 'simplicial complexes'
- 'network geometry'
- 'hyperbolic geometry'
- 'growing networks'
- 'emergent geometry'
- 'scale-free networks'
- 'quantum gravity'
implementations: []
summary: >-
  Bianconi and Rahmede (2017), Scientific Reports 7, 41974. Growing
  simplicial complexes, made by gluing d-simplices to (d − 1)-faces with
  probability ∝ 1 + s n_α (flavor s = −1, 0, 1), have a tree as their dual
  and, drawn with equal links as ideal simplices in the Poincaré ball,
  fill hyperbolic d-space: the hyperbolic geometry is an outcome of a
  purely combinatorial rule rather than its cause. Degrees are exponential
  for d + s = 1 and power-law with γ = 2 + 1/(d + s − 1) ≤ 3 for
  d + s > 1; clustering and modularity are high for d ≥ 2. Hyperbolicity is
  shown by construction, conditional on equal link lengths, not proved.
---
<!-- inactive-ok-file: THEORY-tmpp6w9v THEORY-tmp1y92d THEORY-tmpzw8vz QUESTION-025 THEORY-185 LIT-102 — Proposed, Open or Rejected; cited as the accounts this reading bears on -->

# LIT-tmp9eclr: Emergent Hyperbolic Network Geometry

Ginestra Bianconi and Christoph Rahmede (2017), *Scientific Reports* 7,
41974 — [ARXIV-1607.05710](https://arxiv.org/abs/1607.05710), DOI-10.1038/srep41974

## Key takeaways

- **The model.** Start from one d-simplex. At each step pick a
  (d − 1)-face α with probability ∝ 1 + s n_α, where n_α is the number of
  d-simplices on it minus one, and glue a new d-simplex to it through one
  new node. Flavor s = −1 allows only faces with n_α = 0, so the complex is
  a discrete manifold; s = 0 is uniform; s = 1 is preferential attachment
  on faces. The rule refers to no coordinate or distance.
- **Degrees, derived.** A master equation gives the degree distribution in
  closed form: geometric, P(k) = (d/(d+1))^{k−d}/(d+1), when d + s = 1, and
  a ratio of Gamma functions with a power-law tail k^{−γ},
  γ = 2 + 1/(d + s − 1) ≤ 3, when d + s > 1 (d = 1, s = 1 is the
  Barabási–Albert γ = 3). Simulations match (Fig. 2). This is the part of
  the paper that is derived and could have failed.
- **Geometry, by construction.** Each new d-simplex is glued to one face,
  so the dual (simplices as nodes, shared faces as links) is a tree. With
  every link taken to have the same length, the paper draws each simplex
  as an ideal simplex of the Poincaré ball, with the first d + 1 nodes on
  the sphere summing to zero and each new node at the normalised sum of
  its parent face's node positions. This is offered as the unique
  embedding that fills the space as t → ∞, which is asserted, not proved.
  The case is also argued from the small-world property (N ≃ e^D cannot
  fit a finite-dimensional Euclidean space with equal links), which the
  paper itself says is not sufficient.
- **What the hyperbolicity rests on.** The authors say it is a
  consequence of the equal-length "proto-geometry": with unequal lengths
  the same complex embeds in a sphere. In the ideal embedding all node
  distances are infinite, and for s = 0, 1 sibling nodes from one face
  coincide, so the embedding is clean only for the manifold flavor s = −1.
  For s = −1, d = 3 the complexes are stacked polytopes tied to Apollonian
  packings, whose symmetry group is a discrete subgroup of SO(3,1); for
  d = 2 the paper links them to Farey sequences without a derivation.
- **Network signatures together.** For d ≥ 2, modularity 0.80–0.97 and
  average clustering 0.65–0.84 (N = 10⁴, 20 realisations, Table I), with
  the small-world property for all flavors except the chain (d = 1,
  s = −1).
- **A transition in the geometry, numerically.** Giving faces a fitness
  e^{−βε_α} from random node energies and attaching ∝ η_α(1 + s n_α), at
  large β the centroid of node positions R approaches 1 and their spread
  σ vanishes with size: the complex grows in one direction of the ball.
  Shown by simulation (Fig. 4, N up to 10⁴, d = 2, 3, s = −1), with the
  maximum degree peaking at the transition for d = 3 only.

## Standing in the record

Filed on 2026-10-09 at the owner's request, in the second part of the
batch on hierarchy and hyperbolic geometry asked for after the record opened
[QUESTION-025](../questions.d/QUESTION-025.md). The owner gave only the link.

Read the same day ([NOTE-tmpqlhel](../notes.d/NOTE-tmpqlhel.md)). It is the companion to Krioukov et
al. ([LIT-tmp0u9c9](LIT-tmp0u9c9.md), [THEORY-tmp1y92d](../theory.d/THEORY-tmp1y92d.md)), whose model it cites as its foil:
there nodes are sprinkled in a hyperbolic space and the network follows
from distance; here the network grows by a combinatorial rule and the
hyperbolic picture follows from its tree-shaped dual. The reading is the
source of [THEORY-tmpp6w9v](../theory.d/THEORY-tmpp6w9v.md). It is also a worked instance of the
higher-order network geometry the Battiston et al. review ([LIT-091](LIT-091.md))
maps only in passing, and of the "emergent space" theme that [LIT-102](LIT-102.md)
gestures at without a construction. It does not answer [QUESTION-025](../questions.d/QUESTION-025.md); the
NOTE says what it offers it.
