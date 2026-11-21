---
status: Proposed
promote_when: >-
  A second reading or reproduction confirming that the composition and
  concatenation rules give Proposition 3's mass-fraction bound, that
  normed Adam or SGD transfers learning rates across width and depth on at
  least one reported architecture, and that Proposition 4's
  depth-independent sharpness holds for the 1/L residual construction.
title: 'Large, Liu, Huh, Bahng, Isola and Bernstein define a modular norm on a network''s weights, built recursively from per-module norms, masses and sensitivities, in which each module''s contribution to the linearized change in output is bounded by its share of the total mass, zero mass freezing a module; normalizing updates in it made learning rates transfer across width and depth in their experiments, and a 1/L residual construction has depth-independent sharpness'
version: 1
tags:
- learning-theory
- representation-learning
- anthology-candidate
date: '2026-11-21'
source:
- LIT-tmp4b6aq
summary: >-
  The modular norm read for [CLAIM-tmpqwoxz](../claims.d/CLAIM-tmpqwoxz.md): mass is a hand-set allocation
  of learning among modules, in ratios, with width handled by the atoms'
  norms. Proposed until its promote_when is met.
---
<!-- inactive-ok-file: CLAIM-tmpqwoxz THEORY-tmpgdk30 THEORY-tmpig1z0 — Proposed, Deferred or new; filed in this contribution of 2026-11-21 or the ones it builds on -->

# THEORY-tmphj4hu: Large, Liu, Huh, Bahng, Isola and Bernstein define a modular norm on a network's weights, built recursively from per-module norms, masses and sensitivities, in which each module's contribution to the linearized change in output is bounded by its share of the total mass, zero mass freezing a module; normalizing updates in it made learning rates transfer across width and depth in their experiments, and a 1/L residual construction has depth-independent sharpness

## Source

Large, Liu, Huh, Bahng, Isola and Bernstein, [LIT-tmp4b6aq](../literature.d/LIT-tmp4b6aq.md), read in [NOTE-tmpzip1x](../notes.d/NOTE-tmpzip1x.md) from arXiv 2405.14813v1 (23 May 2024).

## What was actually shown

Definitions 1–4, Propositions 3–5, §2.3, B.1, D.4 and D.6 as quoted in the NOTE.

## What this does not say

Nothing about the lazy regime, levels or time scales; Proposition 3 does not show actual shares equal mass fractions.

## Connections

[THEORY-tmpgdk30](THEORY-tmpgdk30.md) (modular duality, built on this norm); [THEORY-tmpig1z0](THEORY-tmpig1z0.md) (the spectral condition, the atoms' norm for linear layers); [THEORY-082](THEORY-082.md).
