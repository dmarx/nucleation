---
status: Proposed
promote_when: >-
  A reading or replication confirms that the data-free network's energy
  curves match an independent mechanical model, not only the truss model
  it was trained on, for several conical Kresling geometries; that
  inverse-designed geometries reach the specified stable heights and
  barrier within stated error; and that a stack designed with ascending
  barriers folds in that order in a physical prototype.
title: 'A neural network trained only on the equilibrium and energy conditions of a truss model of conical Kresling origami recovers its energy curve and inverts it to geometries with prescribed stable heights and barrier, and stacks of such cells with ascending barriers fold in the designed order under compression'
version: 1
tags:
- natural-sciences
- anthology-candidate
date: '2026-11-05'
source:
- LIT-tmpovo05
summary: >-
  Kang, Kim, Yang and Ryu (2025), LIT-tmpovo05, read in NOTE-tmpxbvec.
  Forward and inverse results are checked against a beam-truss FEA that
  shares the network's truss abstraction; the folding order is checked also
  in one scaled PET prototype, where barriers differ from prediction and
  are compared after normalizing to the bottom layer. It does not say the
  truss model captures the mechanics of real cells.
---

# THEORY-tmpb6xqr: A neural network trained only on the equilibrium and energy conditions of a truss model of conical Kresling origami recovers its energy curve and inverts it to geometries with prescribed stable heights and barrier, and stacks of such cells with ascending barriers fold in the designed order under compression

## Source

Kang, Kim, Yang and Ryu (2025), LIT-tmpovo05; read in NOTE-tmpxbvec.

## What was actually shown

- **Forward**: energy curves matching a beam-truss FEA with R² > 0.93.
- **Inverse**: geometries matching target heights and barriers with
  R² > 0.99, one of many that fit; some barrier targets infeasible.
- **Deployment**: three-layer stacks with barriers 0.05, 0.08 and 0.11
  fold bottom to top in FEA and in a 16× scaled PET prototype; normalized
  barrier errors −7.93% (middle) and −16.16% (top), with residual energy
  after each fold.

## What this does not say

- That the mechanics are validated independently: the FEA uses the same
  truss abstraction.
- That absolute barriers are predicted: the prototype is compared after
  normalization.
- Anything about dynamics or rate effects, or about reachability under a
  limited load.
