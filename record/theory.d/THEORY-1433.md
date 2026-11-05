---
number: 1433
status: Proposed
formerly:
- THEORY-tmpybouv
promote_when: >-
  A reading, of the journal text or of an independent implementation,
  confirms from worked examples that removing material by the topological
  derivative of the weighted strain-energy ratio yields compliant
  mechanisms without point flexures, and that raising the weighting
  parameter raises geometric advantage while lowering mechanical
  advantage.
title: 'Krishnakumar and Suresh show that compliant mechanisms can be designed by topology optimization without pseudo-densities, by removing material where the topological derivative of a mutual-to-weighted-input-and-output strain-energy objective is lowest, which yields designs without point hinges and lets one parameter trade geometric against mechanical advantage'
version: 1
tags:
- natural-sciences
- operations-research
date: '2026-11-05'
source:
- LIT-2099
summary: >-
  Krishnakumar and Suresh (2015), [LIT-2099](../literature.d/LIT-2099.md), read in full in
  [NOTE-1582](../notes.d/NOTE-1582.md) from a lab-posted manuscript, as a stand-in for Sigmund
  (1997). Proposed: hinge-freedom is shown by pictures of a handful of
  coarse-mesh designs, and the η trade-off on one example. It is the
  authors' account of their own method, not of Sigmund's; it does not say
  that the designs stay hinge-free under stress constraints or large
  deformation, or that they were built.
---
<!-- inactive-ok-file: LIT-2043 — Unavailable and new; the unread original this neighbour stands in for, cited as open -->

# THEORY-1433: Krishnakumar and Suresh show that compliant mechanisms can be designed by topology optimization without pseudo-densities, by removing material where the topological derivative of a mutual-to-weighted-input-and-output strain-energy objective is lowest, which yields designs without point hinges and lets one parameter trade geometric against mechanical advantage

## Source

Krishnakumar and Suresh (2015), [LIT-2099](../literature.d/LIT-2099.md); read in [NOTE-1582](../notes.d/NOTE-1582.md).

## What was actually shown

- **The objective** (Sec. 3.1): φ = S_mut / (2ηS_in + 2(1−η)S_out), under a
  volume limit, a modification of Ansola et al.'s ratio (η = 0.5).
- **The parameterization** (Secs. 3.2–4): the topological derivative of φ,
  thresholded as a level set, removes material step by step; elements are
  in or out, so no pseudo-densities, and the matrices stay
  well-conditioned.
- **The examples** (Sec. 5): 2D inverter with GA 0.8 and MA 0.71; cruncher
  with GA 0.32 and MA 1.59 at η = 0.5 and GA 0.59 and MA 1.1 at η = 0.6,
  designs "devoid of point-flexures"; a grasper and 3D designs. Point
  hinges could have formed; in these designs they did not.

## What this does not say

- Anything about Sigmund's (1997) formulation beyond the one-line account
  of it, [LIT-2043](../literature.d/LIT-2043.md) being unread.
- That the designs are hinge-free in a measured sense: no
  stress-concentration measure is given.
- That the method holds with springs, stress constraints or large
  deformation, which are future work.
- That the η trade-off traces the Pareto front.
