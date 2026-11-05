---
number: 1427
status: Proposed
formerly:
- THEORY-tmpucnpz
promote_when: >-
  A proof, or an independent computation on generic triangulations that are
  not H1, that the number of real branches of nearly-flat configurations
  meeting at the flat state of a four-boundary-vertex triangulated rigid
  origami is 2^Vi, and that the branches pair with the patterns of vertex
  popping states up to global sign.
title: 'Chen and Santangelo show that a flat triangulated rigid origami sits at a singular point of its configuration space where generically 2^Vi folding branches meet, one pair for each pattern of vertex popping states, so folding from flat is exponentially ambiguous'
version: 1
tags:
- mathematics
- natural-sciences
date: '2026-11-05'
source:
- LIT-2021
summary: >-
  Chen and Santangelo (2018), [LIT-2021](../literature.d/LIT-2021.md), read in [NOTE-1614](../notes.d/NOTE-1614.md) (main
  text in full, appendices skimmed). Proposed: the count of 2^Vi branches
  is numerical for Vi from 2 to 8 and proven only for H1 triangulations,
  which are rare; second-order solutions are treated as configurations
  without a general guarantee; and only patterns with four boundary
  vertices are treated. It does not say how the branches join away from
  the flat state, or that a real sheet misfolds at any measured rate.
---

# THEORY-1427: Chen and Santangelo show that a flat triangulated rigid origami sits at a singular point of its configuration space where generically 2^Vi folding branches meet, one pair for each pattern of vertex popping states, so folding from flat is exponentially ambiguous

## Source

Chen and Santangelo (2018), [LIT-2021](../literature.d/LIT-2021.md); read in [NOTE-1614](../notes.d/NOTE-1614.md).

## What was actually shown

- **Singularity** (abstract, §II C): the generic configuration space has
  dimension D = Ve − 3, but the flat state admits D + Vi first-order
  motions, so "the degeneracy of the unfolded state makes a linear
  approach impossible there".
- **The constraints** (§II A–B): one quadratic constraint per self stress;
  the wheel stress constraint "is precisely Gaussian curvature
  preservation", a quadratic form with one negative eigenvalue at each
  internal vertex, whose null cone has two nappes (popped up, popped down).
- **The count** (§III A–B): in numerical root-finding on random Delaunay
  triangulations with four boundary vertices, Vi from 2 to 8, the
  second-order system's roots were, with a few exceptions, distinct and
  real, giving 2^Vi branches, "exactly two branches with each such pair of
  sign patterns". The exceptions contain triangulated triangles.
- **Proof for H1** (§IV): for triangulations built by Henneberg-1 moves the
  configuration space consists of 2^Vi intersecting one-dimensional
  branches, to all orders.
- **Self-folding** (§V): no driving force can be perpendicular to every
  wrong branch for even modest Vi.

## What this does not say

- That the count is proven for generic triangulations; it is a numerical
  finding there.
- That second-order solutions are always configurations.
- Anything about D > 1, or about how branches connect away from the flat
  state.
- That branches are told apart by mountain–valley assignment; they are
  not necessarily.
- How often a real sheet misfolds; that is inferred, not measured.
