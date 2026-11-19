---
number: 2036
status: Proposed
formerly:
- THEORY-tmpn978s
title: 'Miyato and colleagues build network layers from unit vectors on a sphere updated by a generalised Kuramoto rule with a data-dependent symmetry-breaking bias, and report that the bias and norm-based readouts are needed for stable training'
version: 1
source:
- LIT-2814
tags:
- representation-learning
- complex-systems
date: '2026-11-19'
promote_when: >-
  The experimental sections are read and confirm that removing the bias
  or the norm readout destabilizes training.
summary: >-
  Miyato, Löwe, Geiger and Welling ([LIT-2814](../literature.d/LIT-2814.md)), read in part in
  [NOTE-2107](../notes.d/NOTE-2107.md). Oscillatory units on a sphere, coupled by a generalised
  Kuramoto update, with the conditioning input acting as a symmetry-breaking
  field. Here as context for the architecture of [LIT-2787](../literature.d/LIT-2787.md).
---
<!-- inactive-ok-file: NOTE-2107 — Skimmed; cited in this filing of 2026-11-19 -->
<!-- inactive-ok-file: LIT-2787 — Unfetched; cited in this filing of 2026-11-19 -->

# THEORY-2036: Miyato and colleagues build network layers from unit vectors on a sphere updated by a generalised Kuramoto rule with a data-dependent symmetry-breaking bias, and report that the bias and norm-based readouts are needed for stable training

## The account

Each unit is a unit vector; its update rotates it by its own frequency
and pulls it toward the bias and its neighbours' states, projected onto
the sphere. The bias breaks the global rotational symmetry, and
norm-based readouts discard the remaining global phase.

## What it does not show

Anything about domain walls, Z2 symmetry or topological defects.
