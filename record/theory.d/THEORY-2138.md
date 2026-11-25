---
number: 2138
status: Proposed
formerly:
- THEORY-tmphj4hu
promote_when: >-
  A second reading or reproduction confirming that the composition and
  concatenation rules give Proposition 3's mass-fraction bound, that
  normed Adam or SGD transfers learning rates across width and depth on at
  least one reported architecture, and that Proposition 4's
  depth-independent sharpness holds for the 1/L residual construction.
title: 'Modular norm lets learning rates transfer'
statement: >-
  Large, Liu, Huh, Bahng, Isola and Bernstein define a modular norm on a
  network's weights, built recursively from per-module norms, masses and
  sensitivities, in which each module's contribution to the linearized
  change in output is bounded by its share of the total mass, zero mass
  freezing a module; normalizing updates in it made learning rates transfer
  across width and depth in their experiments, and a 1/L residual
  construction has depth-independent sharpness
version: 1
tags:
- learning-theory
- representation-learning
- anthology-candidate
date: '2026-11-21'
source:
- LIT-2938
summary: >-
  The modular norm read for [CLAIM-775](../claims.d/CLAIM-775.md): mass is a hand-set allocation
  of learning among modules, in ratios, with width handled by the atoms'
  norms. Proposed until its promote_when is met.
---
<!-- inactive-ok-file: CLAIM-775 THEORY-2136 THEORY-2139 — Proposed, Deferred or new; filed in this contribution of 2026-11-21 or the ones it builds on -->

# THEORY-2138: Modular norm lets learning rates transfer

## Source

Large, Liu, Huh, Bahng, Isola and Bernstein, [LIT-2938](../literature.d/LIT-2938.md), read in [NOTE-2235](../notes.d/NOTE-2235.md) from arXiv 2405.14813v1 (23 May 2024).

## What was actually shown

Definitions 1–4, Propositions 3–5, §2.3, B.1, D.4 and D.6 as quoted in the NOTE.

## What this does not say

Nothing about the lazy regime, levels or time scales; Proposition 3 does not show actual shares equal mass fractions.

## Connections

[THEORY-2136](THEORY-2136.md) (modular duality, built on this norm); [THEORY-2139](THEORY-2139.md) (the spectral condition, the atoms' norm for linear layers); [THEORY-082](THEORY-082.md).
