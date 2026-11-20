---
status: Answered
title: 'On the orbits of a function-preserving symmetry that acts on the parameters as a diffeomorphism, such as permuting hidden units, rescaling across a ReLU or an orthogonal map of a residual stream, is the common-descent verdict constant, and is a frustration residual budgeted in a fixed Euclidean norm?'
version: 1
tags:
- information-geometry
- loss-landscapes
date: '2026-11-20'
line:
- learned-structure
refines:
- QUESTION-127
summary: >-
  The part of QUESTION-127 the record has answered, split off under ADR-049
  at the status review of 2026-11-20. CLAIM-629 (Active, demonstrated): the
  common-descent verdict is constant on every such orbit; the Euclidean
  residual is constant where the symmetry's derivative is orthogonal, so
  across permutations and orthogonal maps, and can change along rescalings.
  Symmetries that are not diffeomorphisms, the other diagnoses and
  trajectories stay with QUESTION-127.
---

# QUESTION-tmpr6jhg: On the orbits of a function-preserving symmetry that acts on the parameters as a diffeomorphism, such as permuting hidden units, rescaling across a ReLU or an orthogonal map of a residual stream, is the common-descent verdict constant, and is a frustration residual budgeted in a fixed Euclidean norm?

## Why it was a question

QUESTION-127 left open "Whether a frustration verdict is constant on
symmetry orbits", because function-preserving symmetries "relate distinct
points that compute the same function" and are not charts of one space, so
CLAIM-366's chart invariance does not settle them.

## Answer

CLAIM-629 (Active, demonstrated). The three symmetries QUESTION-127 names
are linear isomorphisms of the parameters, so each is a diffeomorphism.
Differentiating L_i∘σ = L_i gives g_i(θ) = Dσ(θ)ᵀ g_i(σθ), and an invertible
linear map keeps 0 in or out of the convex hull of the gradients:

- **Common descent** is constant on every such orbit.
- **The residual Φ_r of CLAIM-365, in the Euclidean norm,** is constant
  where Dσ is orthogonal, so along permutations and orthogonal maps. Along
  rescalings it can change: one demand on f = v·relu(ux) has squared
  gradient norm 612 at (4, 1) and 288 at its image (2, 2).

## What it leaves to QUESTION-127

Symmetries that are not diffeomorphisms, such as the blow-ups of CLAIM-305;
the other diagnoses QUESTION-127 lists, governance regret and modular
localization (the compatibility complex is CLAIM-555's, Proposed); and
trajectories, which carry the optimizer.
