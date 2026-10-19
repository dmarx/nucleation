---
number: 193
status: Active
formerly:
- THEORY-tmpp6w9v
title: 'A simplicial complex grown by gluing each new d-simplex to one (d − 1)-face, by a rule that uses no geometry, has a 1-skeleton whose geodesic triangles are 2-thin at every size, so hyperbolic network geometry in Gromov''s sense is an outcome of the combinatorial growth; the equal-link drawing as ideal simplices is a convention, a tiling of the hyperbolic plane for d = 2 in the manifold flavor but not a tiling of hyperbolic d-space for d ≥ 3'
version: 2
history:
- version: 2
  date: '2026-10-19'
  note: >-
    Corrected and promoted at the owner's direction, carrying out the
    promotion audit's decision
    (record/promotion-audit/decisions/THEORY-193.yaml, batch 011, ADR-047).
    The promote_when asked for a proof that the 1-skeleton's graph metric
    is Gromov δ-hyperbolic with δ bounded independently of N. The record
    supplies it: δ ≤ 2 for every N, d and flavor, from a tree
    decomposition whose bags are the simplices. Under ADR-047 v2 (the
    owner's rule of 2026-10-19), that re-derivation meets the condition.
    The review also found three errors, now corrected. "A tiling of
    hyperbolic d-space" fails for d ≥ 3, because a tree of simplices has
    no cycles around codimension-2 faces, and for s = 0, 1, where siblings
    coincide. "Its dual is a tree" holds for the face-adjacency graph only
    when s = −1. And the old last clause, that the curvature comes from
    the equal-length convention and not from the growth, is true of the
    drawing's constant curvature but not of the graph's coarse
    hyperbolicity, which comes from the growth. The title is rewritten to
    say so.
tags:
- network-science
- complex-systems
- mathematics
date: '2026-10-09'
source:
- LIT-867
summary: >-
  Bianconi and Rahmede (2017), [LIT-867](../literature.d/LIT-867.md), read in [NOTE-678](../notes.d/NOTE-678.md), for the model,
  the degree law and the ideal-simplex drawing. The coarse hyperbolicity
  of the graph is the record's: the source asserts the hyperbolic geometry
  through its drawing and measures nothing on the graph. Every such
  complex has a 1-skeleton with 2-thin geodesic triangles, whatever the
  flavor, so its hyperbolicity is a property of the network. The
  constant-curvature picture, ideal simplices in the Poincaré ball, is a
  choice of drawing. It tiles H² for d = 2 in the manifold flavor, and for
  d ≥ 3 it is not a tiling. This says nothing about whether real networks
  grow this way.
---
<!-- inactive-ok-file: THEORY-188 THEORY-196 QUESTION-025 — Proposed or Open; cited as the accounts this one sits beside -->

# THEORY-193: A simplicial complex grown by gluing each new d-simplex to one (d − 1)-face, by a rule that uses no geometry, has a 1-skeleton whose geodesic triangles are 2-thin at every size, so hyperbolic network geometry in Gromov's sense is an outcome of the combinatorial growth; the equal-link drawing as ideal simplices is a convention, a tiling of the hyperbolic plane for d = 2 in the manifold flavor but not a tiling of hyperbolic d-space for d ≥ 3

## Source

Bianconi and Rahmede (2017), [LIT-867](../literature.d/LIT-867.md), read in [NOTE-678](../notes.d/NOTE-678.md). The thin-triangle
bound below is the record's own. It is written out in
record/promotion-audit/decisions/THEORY-193.yaml.

## What was actually shown

The model: start from one d-simplex. At each step a (d − 1)-face α is
chosen with probability ∝ 1 + s n_α, where the flavor s is −1, 0 or 1 and
n_α is the number of simplices on α minus one. A new d-simplex is glued to
α through one new node.

- **The gluing is a tree.** Each new simplex meets the old complex in one
  face, and has as parent the earliest simplex holding that face. With
  s = −1 a face holds at most two simplices, so the face-adjacency graph
  (the source's dual) is itself a tree. With s = 0 or 1 several simplices
  can be glued on one face, which makes them a clique in that graph. The
  parent structure is a tree for every flavor.
- **The 1-skeleton is Gromov hyperbolic, with δ ≤ 2 at every size** (the
  record's derivation). The simplices, with parent links, give a tree
  decomposition of the 1-skeleton G whose bags are cliques: each vertex's
  simplices form a subtree, because a simplex holding an old vertex holds
  it in the face it was glued to. If a bag lies on the tree path between
  bags of u and v, every u–v path in G meets it. Now take a geodesic
  triangle x, y, z and a point p on [x, y]. Let q be the node of the tripod
  spanned by bags of x, y and z that is nearest a bag of p. Then q's bag
  meets [x, p] and [p, y] on either side of p, so p is within 1 of it. It
  also meets a second side of the triangle. Since a bag is a clique, p is
  within 2 of that side. The bound does not depend on N, d or s. In
  graph-theoretic terms, G is chordal with tree-length 1.
- **The drawing.** With every link of equal length, the source draws each
  simplex as an ideal simplex of the Poincaré ball. The initial nodes sum
  to zero, and each new node sits at the normalised sum of its parent
  face's positions. For d = 2 and s = −1, each new node lands on the open
  arc cut off by its parent edge. The drawn triangles then have disjoint
  interiors and fill the disc as every free edge is glued: a tiling of H²
  by ideal triangles. For s = 0 or 1, siblings coincide ([NOTE-678](../notes.d/NOTE-678.md)). For
  d ≥ 3, a (d − 2)-face of an ideal simplex has at least two ideal vertices,
  so it passes through H^d. In a face-to-face tiling, the tiles around such
  a face form a finite cycle of face-adjacent simplices, whose dihedral
  angles sum to 2π. The grown complex has no such cycle. So for d ≥ 3 the
  drawing is not a tiling: around each such face the simplices form a
  path, and they overlap once their angles pass 2π or never close up. The
  source asserts the tiling and its uniqueness without proof, and [NOTE-678](../notes.d/NOTE-678.md)
  grades that part weak.
- **The statistics, derived.** Degrees follow from a master equation:
  geometric for d + s = 1, and a power law with
  γ = 2 + 1/(d + s − 1) ≤ 3 for d + s > 1, matched by simulation.
  Simulation also gives high clustering and modularity for d ≥ 2. None of
  this depends on the drawing, and it could have failed.

What could have come out otherwise is the degree law, the clustering, and
the thin-triangle bound, whose proof needs the gluing to be a tree and
would not carry over to a rule that closes cycles of simplices. The
drawing's constant curvature could not: the equal-length convention
defines it.

## What this does not say

- **Not that the drawing's curvature comes from the growth.** The source
  says the constant-curvature geometry follows from a "proto-geometry" of
  equal links. With links of different lengths, the same complex can be
  embedded in a d-sphere. What the growth fixes is the coarse geometry of
  the graph metric, which is hyperbolic whatever drawing is chosen.
- **Not that real networks grow this way,** or that their hyperbolicity
  ([THEORY-188](THEORY-188.md)) has this origin. No real network is fitted.
- **Not much beyond what trees already give.** A tree embeds in hyperbolic
  space with low distortion (Sarkar–Sala, [THEORY-196](THEORY-196.md)), and a tree is
  0-hyperbolic. This account extends the point to complexes whose gluing
  is a tree, with δ ≤ 2, and adds the growth statistics. It says nothing
  about complexes with cycles of simplices, and it gives no
  low-distortion embedding in H^d with finite link lengths.
- **Not a statement about learned embeddings.** The source's placement of
  a node at the normalised sum of its ancestors is a rule it chooses. It
  does not bear on whether a co-occurrence embedding carries a hierarchy
  that way, which [QUESTION-025](../questions.d/QUESTION-025.md) asks.
