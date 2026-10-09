---
status: Proposed
promote_when: >-
  A proof, for at least the manifold flavor s = −1, that the graph metric
  of the grown complex's 1-skeleton is Gromov δ-hyperbolic with δ bounded
  independently of N, or that the complex admits an embedding in H^d with
  finite link lengths and distortion bounded independently of N. Either
  would make the hyperbolicity a property of the network rather than of
  the drawing the source chooses. A counterexample would refute it: a δ
  that grows with N, or a proof that bounded-distortion embeddings in H^d
  do not exist. More pictures of the ideal-simplex drawing, or more
  agreement of degree, clustering and modularity with real networks,
  cannot settle it, because the drawing is hyperbolic by construction and
  the statistics do not depend on it.
title: 'A simplicial complex grown by gluing each new d-simplex to one (d − 1)-face, by a rule that uses no geometry, has a tree as its dual and, with every link taken as equal, is a tiling of hyperbolic d-space by ideal simplices; so hyperbolic network geometry can be the outcome of combinatorial growth rather than its cause, though the curvature comes from the equal-length convention and not from the growth'
version: 1
tags:
- network-science
- complex-systems
- mathematics
date: '2026-10-09'
source:
- LIT-tmp9eclr
summary: >-
  Bianconi and Rahmede (2017), [LIT-tmp9eclr](../literature.d/LIT-tmp9eclr.md): the tree dual is immediate
  and the degree law (geometric for d + s = 1, γ = 2 + 1/(d + s − 1) for
  d + s > 1) is derived by a master equation; the hyperbolic geometry is a
  drawing, ideal simplices in the Poincaré ball, with uniqueness asserted.
  The source itself says unequal link lengths would fit the same complex in
  a sphere. It does not measure hyperbolicity on the graph, and it does
  not show real networks grow this way.
---
<!-- inactive-ok-file: THEORY-tmp1y92d THEORY-tmpzw8vz QUESTION-025 — Proposed or Open; cited as the accounts this one sits beside -->

# THEORY-tmpp6w9v: A simplicial complex grown by gluing each new d-simplex to one (d − 1)-face, by a rule that uses no geometry, has a tree as its dual and, with every link taken as equal, is a tiling of hyperbolic d-space by ideal simplices; so hyperbolic network geometry can be the outcome of combinatorial growth rather than its cause, though the curvature comes from the equal-length convention and not from the growth

## Source

Bianconi and Rahmede (2017), [LIT-tmp9eclr](../literature.d/LIT-tmp9eclr.md), read in [NOTE-tmpqlhel](../notes.d/NOTE-tmpqlhel.md).

## What was actually shown

The model: from one d-simplex, at each step a (d − 1)-face α is chosen
with probability ∝ 1 + s n_α (flavor s = −1, 0, 1; n_α the simplices on α
minus one) and a new d-simplex is glued to it through one new node.

- **The dual is a tree.** Each new simplex meets the old complex in one
  face, so simplices joined by shared faces form a tree. This is
  immediate.
- **The drawing.** With every link of equal length, the source draws each
  simplex as an ideal simplex of the Poincaré ball (all vertices on the
  boundary sphere, so all edges equal), the initial nodes summing to zero
  and each new node at the normalised sum of its parent face's positions.
  A tree of ideal simplices tiles H^d, so the drawing fills hyperbolic
  space as t → ∞. The source asserts this is the only embedding that does;
  it gives no proof. It adds the small-world argument (N ≃ e^D cannot be
  fitted in a finite-dimensional Euclidean space with equal links) and
  concedes that small world alone is not sufficient.
- **The statistics, derived.** Degrees by a master equation: geometric
  for d + s = 1, power-law with γ = 2 + 1/(d + s − 1) ≤ 3 for d + s > 1,
  matched by simulation. High clustering and modularity for d ≥ 2 by
  simulation. These do not depend on the drawing, and could have failed.

What could have come out otherwise is the degree law and the clustering.
The hyperbolicity could not, given the equal-length convention: it is how
the drawing is defined.

## What this does not say

- **Not that the network's own metric is hyperbolic.** In the ideal
  drawing every pair of nodes is infinitely far apart, and for s = 0, 1
  sibling nodes coincide. No Gromov δ, discrete curvature or
  finite-distortion embedding is computed. The promote_when asks for one.
- **Not that the curvature comes from the growth.** The source says the
  geometry follows from a "proto-geometry" of equal links, and that with
  links of different lengths the same complex can be embedded in a
  d-sphere. What the growth supplies is the tree-shaped dual; the sign of
  the curvature is a convention placed on it.
- **Not that real networks grow this way,** or that their hyperbolicity
  ([THEORY-tmp1y92d](THEORY-tmp1y92d.md)) has this origin. No real network is fitted.
- **Not more than trees already give.** That a tree embeds in hyperbolic
  space with low distortion is the Sarkar–Sala result ([THEORY-tmpzw8vz](THEORY-tmpzw8vz.md)).
  This account extends the point from trees to complexes whose dual is a
  tree, and adds the growth statistics; it does not show hyperbolicity in
  complexes whose dual has cycles.
- **Not a statement about learned embeddings.** The source's placement of
  a node at the normalised sum of its ancestors is a rule it chooses. It
  does not bear on whether a co-occurrence embedding carries a hierarchy
  that way, which [QUESTION-025](../questions.d/QUESTION-025.md) asks.
