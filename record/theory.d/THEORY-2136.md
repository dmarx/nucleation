---
number: 2136
status: Proposed
formerly:
- THEORY-tmpgdk30
promote_when: >-
  A re-derivation, from the definitions in §§3.3–4.3, that the RMS→RMS
  duality map of a d_out×d_in matrix is √(d_out/d_in)·UVᵀ and that eqs.
  (11)–(12) are the duality maps of the composite and tuple norms, and a
  check that iteration (15) maps every singular value in (0, √3) to 1 in
  the limit.
title: 'Duality map orthogonalizes linear-layer gradients'
statement: >-
  Bernstein and Newhouse construct a duality map for general networks by
  assigning each layer an operator norm and inducing a map recursively
  through the modular norm; for a linear layer under the RMS→RMS norm it
  sends a gradient UΣVᵀ to √(d_out/d_in)·UVᵀ, an update whose singular
  values all have the same magnitude, approximated by a Newton–Schulz
  iteration that converges to UVᵀ
version: 1
tags:
- learning-theory
- representation-learning
- anthology-candidate
date: '2026-11-21'
source:
- LIT-2952
summary: >-
  The reading behind [CLAIM-774](../claims.d/CLAIM-774.md)'s update rule: modular dualization of
  a linear layer is the scaled polar factor, every singular direction
  moved by the same amount. Proposed until its promote_when is met.
---
<!-- inactive-ok-file: THEORY-186 — Proposed; cited in the readings of 2026-11-21 -->
<!-- inactive-ok-file: CLAIM-774 THEORY-2138 THEORY-2139 — Proposed, Deferred or new; filed in this contribution of 2026-11-21 or the ones it builds on -->

# THEORY-2136: Duality map orthogonalizes linear-layer gradients

## Source

Bernstein and Newhouse, [LIT-2952](../literature.d/LIT-2952.md), read in [NOTE-2232](../notes.d/NOTE-2232.md) from arXiv 2410.21265v2 (6 Dec 2024).

## What was actually shown

Table 1, Proposition 1, §§4.1, 5.3, 6.4 and 6.5 as quoted in the NOTE.

## What this does not say

Nothing about the order or speed with which directions are learned, about finite-step Newton–Schulz accuracy, or about experiments of its own.

## Connections

[THEORY-2138](THEORY-2138.md) (the modular norm); [THEORY-2139](THEORY-2139.md) (the spectral condition); [THEORY-427](THEORY-427.md) (Shampoo); [THEORY-186](THEORY-186.md) and [THEORY-740](THEORY-740.md) (Saxe's dynamics, which [CLAIM-774](../claims.d/CLAIM-774.md) contrasts).
