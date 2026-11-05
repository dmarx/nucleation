---
number: 1405
status: Proposed
formerly:
- THEORY-tmpl2ztw
promote_when: >-
  A reading confirms, from the paper's numerical example or from another
  conversion made by the same method, that the optimized frame keeps a
  second self-equilibrium state with the specified output displacement,
  with the obstacle in place, and that every thin-element strain stays at
  or below the cap, so that no point hinge forms.
title: 'Kinoshita and Ohsaki show that a bistable compliant truss mechanism, whose second stable state comes from snap-through stopped by contact with an obstacle, can be converted into a single-piece frame mechanism with the same function by optimizing thin pseudo-joints at its former pin joints under a strain cap, without lumping deformation into a point hinge'
version: 1
tags:
- natural-sciences
- operations-research
date: '2026-11-05'
source:
- LIT-2029
summary: >-
  Kinoshita and Ohsaki (2009), [LIT-2029](../literature.d/LIT-2029.md), read in full in [NOTE-1597](../notes.d/NOTE-1597.md).
  Proposed: the conversion is shown on one seven-node example, in
  simulation, with equivalence judged by overlaid force–displacement
  curves. It does not say that the frame is bistable without the obstacle,
  that the method finds frames without a truss to start from, or that a
  fabricated frame behaves as computed.
---

# THEORY-1405: Kinoshita and Ohsaki show that a bistable compliant truss mechanism, whose second stable state comes from snap-through stopped by contact with an obstacle, can be converted into a single-piece frame mechanism with the same function by optimizing thin pseudo-joints at its former pin joints under a strain cap, without lumping deformation into a point hinge

## Source

Kinoshita and Ohsaki (2009), [LIT-2029](../literature.d/LIT-2029.md); read in [NOTE-1597](../notes.d/NOTE-1597.md).

## What was actually shown

- **The two-bar study** (Sec. 3): with thin elements of area A/50 at the
  top node, the frame's force–displacement and spring-force curves nearly
  match the two-bar truss's; stiffer joints lose the snap-through.
- **The conversion problem** (Sec. 4.2): minimize the reaction P∗ at the
  second limit point over the end-region ratios α and β, keeping the output
  displacement and bounding thin-element strain by ε̄. A negative P∗ is
  what lets a second self-equilibrium state exist with the obstacle.
- **The example** (Sec. 5, Table 1): the converted frame "also has the
  second self-equilibrium state", and the four thin-end strain ratios are
  0.06 to 0.99 of ε̄ = 0.05. This could have come out otherwise: P∗ might
  not have gone negative under the strain cap, or the cap might have
  forced a frame without the output displacement.

## What this does not say

- That the second stable state is elastic: it rests on contact with a
  placed obstacle after snap-through, not on a double-well energy.
- That the frame is "equivalent" in any measured sense beyond the overlaid
  curves of one case.
- That the method works without a bistable truss from OPT1, which the
  paper takes as given.
- That a fabricated part behaves as computed; nothing was built.
