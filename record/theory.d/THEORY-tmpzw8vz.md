---
status: Proposed
promote_when: >-
  A complete proof of the lower bound, without the small-angle substitution
  taken as an equality, extended to the Poincaré ball H^r for r > 2: that
  any embedding of some family of trees with worst-case distortion 1 + ε
  needs Ω((ℓ/(εr)) log deg_max) bits per coordinate for r up to about
  log deg_max, and Ω(ℓ/ε) beyond. Or a construction that beats the upper
  bound in depth, which would refute the linear dependence on ℓ. Further
  experiments in which deep trees need more bits than bushy ones cannot
  settle it, because the upper bound already predicts that.
title: 'A finite tree embeds in the hyperbolic plane with worst-case distortion 1 + ε, but because a hyperbolic distance d takes about d bits to write, its coordinates need Θ((ℓ/ε) log deg_max) bits: logarithmic in the branching, linear in the longest path ℓ, so hyperbolic space is economical for shallow bushy hierarchies and not for deep ones'
version: 1
tags:
- representation-learning
- mathematics
date: '2026-10-09'
source:
- LIT-tmpt10fk
summary: >-
  Sala, De Sa, Gu and Ré (2018), [LIT-tmpt10fk](../literature.d/LIT-tmpt10fk.md). The upper bound is Sarkar's
  construction with the paper's bit count. The lower bound is proved for H²
  and one family of trees, with an approximation, and dimension's help is
  shown only as an upper bound. The cost is a cost of coordinates in a
  fixed-point model, not of the information in the tree, and it says
  nothing about Euclidean or linear-direction representations of the same
  hierarchy.
---
<!-- inactive-ok-file: THEORY-185 QUESTION-025 CLAIM-119 — Proposed or open; cited as the accounts this one sits beside -->

# THEORY-tmpzw8vz: A finite tree embeds in the hyperbolic plane with worst-case distortion 1 + ε, but because a hyperbolic distance d takes about d bits to write, its coordinates need Θ((ℓ/ε) log deg_max) bits: logarithmic in the branching, linear in the longest path ℓ, so hyperbolic space is economical for shallow bushy hierarchies and not for deep ones

## Source

Sala, De Sa, Gu and Ré (2018), [LIT-tmpt10fk](../literature.d/LIT-tmpt10fk.md): §3.2, Lemma D.1, Proposition
3.1 with its proof in Appendix D, and Table 7, as read in [NOTE-tmprdxf9](../notes.d/NOTE-tmprdxf9.md).
The embedding itself is Sarkar's (Graph Drawing 2011), which neither record
holds.

## What was actually shown

**Why trees fit.** In the Poincaré disk, two points at equal radius near
the boundary are almost exactly as far apart as the path between them
through the origin, at any angle. The geometry behaves like a tree, in
which the path between siblings runs through their parent. Sarkar's
construction places each node's children evenly on a hyperbolic circle of
radius τ = ((1 + ε)/ε)·2 log(deg_max/(π/2)) around it. Every tree then
embeds in two dimensions with worst-case distortion at most 1 + ε, and
every neighbourhood is preserved.

**What it costs.** A point at hyperbolic distance d from the origin has
1 − ‖x‖ of order e^(−d), so its coordinates need about d bits. Ball volume
grows exponentially in hyperbolic space, so by covering the cost is Θ(d) in
any model, against log d in Euclidean space. The largest distance in
Sarkar's embedding is ℓτ = O((ℓ/ε) log deg_max), and that is the bit count.
For a root carrying deg_max chains of length m (ℓ = 2m), any H² embedding
with distortion 1 + ε must put a node at depth whose −log(1 − ‖x‖) is
Ω((ℓ/ε) log deg_max), so the bound is tight in the plane. The degree
enters only through the angle siblings need. In H^r, code-selected
placement on a hypercube widens that angle, cutting the upper bound to
O((ℓ/(εr)) log deg_max) up to r ≈ log deg_max. The depth term is
untouched by dimension.

**The number that could have come out otherwise.** On real hierarchies the
bound's shape appears: at ε = 0.1, 102 bits for a 40-node balanced tree,
2,358 for a CS PhD advisor graph (deg_max 46), and 2,877 for WordNet's
hypernym tree (deg_max 404). A 344-node phylogenetic tree with deg_max 16
needed 2,361, about as much as WordNet with 25 times the degree. That fits
a cost that grows with path length, not with branching. The paper reports
no tree depths, so this is a reading of its table, not a test. In floating point, h-MDS reached MAP 0.347
at 128 bits and 1.0 at 512 on a 3-ary tree. A precision cost that did not
grow with the embedded distances would have shown flat numbers here.

## What this does not say

- **Not proved in r > 2 dimensions.** The lower bound is for the plane.
  That dimension stops helping beyond log deg_max is a footnote argument,
  and the H^r rate is an upper bound only.
- **Not with exact constants.** The lower-bound proof replaces
  √(2(1 − cos θ)) by θ as an equality and passes over "some algebra". The
  order is credible, but no constant is established.
- **Not that a tree carries Θ(ℓ) bits of information per node.** The cost
  is that of fixed-point coordinates in the Poincaré ball (bits until
  1 − ‖x‖ does not round to zero). A tree is a list of edges in O(n log n)
  bits. Whether other coordinates escape the depth cost (relative to the
  parent, or in floating point) is open, so the finding is about the
  geometry under that representation.
- **Not that Euclidean space is worse at everything.** The contrast, that
  trees cannot be embedded in Euclidean space with distortion near 1 in
  any dimension, is cited, not proved here. It concerns distances only.
- **Not about linear directions or attributes.** It concerns metric
  embeddings of a known tree. It says nothing about whether an embedding
  learned from co-occurrence carries a hierarchy as linear directions,
  which is [QUESTION-025](../questions.d/QUESTION-025.md)'s question. [THEORY-185](THEORY-185.md)'s independent binary
  attributes give a hypercube, not a tree, and are outside its scope.
- **Not that real hierarchies are trees.** For graphs further from trees
  the construction loses fidelity (MAP 0.70–0.82 on the denser graphs).
  A concept lattice in which categories share attributes, as [CLAIM-119](../claims.d/CLAIM-119.md)
  holds, is not a tree, and this account's advantage does not transfer
  to it unaltered.
- **Not an instruction.** It says what a hyperbolic tree embedding costs,
  not whether to use one.
