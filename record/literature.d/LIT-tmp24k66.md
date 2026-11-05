---
status: Active
status_note: >-
  read in full 2026-11-05 (NOTE-tmpt066u) from the arXiv v1 preprint; worth
  reading as the extension of second-order origami rigidity to vertices
  carrying Gaussian curvature, and for the finding that the sign of the
  curvature changes the topology of the near-flat configuration space: a
  non-intersecting vertex with positive curvature has its popped-up and
  popped-down nappes split into disconnected components, one with negative
  curvature keeps them joined by a neck, and a degree-4 vertex is split for
  either sign. Its main limits: local to the flat state and small
  curvature; the disconnection depends on forbidding self-intersection; the
  multi-vertex statement rests on an assumption and leaves open which
  combinations of nappes exist; the published PRE text was not compared.
title: 'Topological transitions in the configuration space of non-Euclidean origami'
version: 1
history:
- version: 1
  date: '2026-11-05'
  note: >-
    Registered and read on 2026-11-05 from the owner's pasted synthesis on
    FACT, rigidity, compliant mechanisms and origami, written by another
    assistant (A) and pasted by the owner on 2026-11-04, which lists it as
    O12 for the disconnection of positively curved vertices' configuration
    spaces. Citation checked against Crossref by the reader: M. Berry, M.
    E. Lee-Trimble and C. D. Santangelo (Crossref gives initials only),
    Physical Review E 101(4), 043003, online 2020-04-23, under the APS
    default licence; arXiv 1910.01008, v1 only, 2019-10-02, which is
    `published:`, with the journal reference added. A's citation is
    correct; the sentence A puts in quotation marks is not in the paper
    (see the NOTE). Not held before (no hit for the DOI, the arXiv id,
    the title or Santangelo). Copy: the arXiv v1 PDF,
    https://arxiv.org/pdf/1910.01008v1, which predates acceptance,
    extracted with pdftotext.
tags:
- mathematics
- natural-sciences
date: '2026-11-05'
published: '2019-10-02'
arxiv: '1910.01008'
doi: '10.1103/PhysRevE.101.043003'
first_author: 'Berry'
keywords:
- 'non-Euclidean origami'
- 'Gaussian curvature'
- 'configuration space'
- 'rigid origami'
- 'nappe'
- 'self-folding'
implementations: []
summary: >-
  Berry, Lee-Trimble & Santangelo (2020). In origami with flat faces and
  curvature K = 2π − Σα at the vertices, the second-order isometry
  condition at a vertex becomes hᵀQh = K, with Q having one negative
  eigenvalue. Near the flat state, for small K and fold angles kept in
  (−π, π), a vertex with K > 0 has a two-sheeted solution set whose
  popped-up and popped-down nappes are disconnected, and one with K < 0 a
  one-sheeted set joining them by a neck; numerical tracing of a 5-fold
  vertex agrees, and degree-4 vertices are disconnected for both signs.
  Under an assumption, multi-vertex branches distinguished by a K > 0
  vertex's nappe are disconnected too. The authors propose curvature as a
  handle against misfolding.
---
<!-- inactive-ok-file: THEORY-tmps6lqg — Proposed or new; cited from the reading of Berry, Lee-Trimble and Santangelo (2020) as open -->

# LIT-tmp24k66: Topological transitions in the configuration space of non-Euclidean origami

Berry, M., Lee-Trimble, M. E. & Santangelo, C. D. (2020). Topological transitions in the configuration space of non-Euclidean origami. *Physical Review E* 101(4): 043003. doi:10.1103/PhysRevE.101.043003. arXiv:1910.01008.

## Key takeaways

*From the reading, NOTE-tmpt066u. Sections are the arXiv version's.*

- **The result** (abstract): "The configuration space of non-intersecting,
  oriented vertices with positive Gaussian curvature decomposes into
  disconnected subspaces; there is no pathway between them without tearing
  the origami." And "In contrast, the configuration space of negative
  Gaussian curvature vertices remain connected."
- **Local.** It holds near the flat state, for small curvature.
- **Self-intersection matters** (§II): where faces may pass through each
  other, "isometric trajectories can pass from one nappe to the other for
  any K", anecdotally.
- **Degree 4** (§II): "the two nappes become disconnected for both positive
  and negative Gaussian curvature."
- **Multi-vertex, conditional** (§III): it rests on "We further assume that
  this equation has two distinct real solutions for hn", and "it is
  difficult to determine whether or not every combination of nappes can be
  realized when K > 0."

## Standing in the record

The pasted synthesis on constraint architectures cites it for the
disconnection of positively curved vertices, and is right in substance,
but the sentence A puts in quotation marks is A's paraphrase, and A drops
the conditions: near-flat states, small curvature, no self-intersection.
It is a clean instance of A's "Feasible target ⇏ reachable target":
every state on each nappe is a valid configuration, and under the declared
motions, rigid, non-intersecting and without tearing, one nappe cannot be
reached from the other. Relax non-intersection and, by the authors'
anecdote, the separation goes, which fits A's point that impossibility is
relative to the declared admissible transformations. Filed from it:
THEORY-tmps6lqg. No instruction for machine-learning practice.
