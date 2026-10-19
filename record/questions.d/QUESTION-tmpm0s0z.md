---
status: Open
title: 'In trained models, do the features'' dimensionality-weighted projectors sum to the identity on their span, as they do in the exact polytope and tegum configurations of uniform superposition?'
version: 1
tags:
- representation-learning
- mathematics
date: '2026-10-19'
line: learned-structure
refines:
- QUESTION-058
summary: >-
  The promotion condition formerly on [THEORY-021](../theory.d/THEORY-021.md), moved here unchanged when
  [THEORY-021](../theory.d/THEORY-021.md) was narrowed to the exact configurations and promoted on
  2026-10-19. The algebra is settled for those configurations. Whether
  trained weights reach them is a measurement no one has made.
---

# QUESTION-tmpm0s0z: In trained models, do the features' dimensionality-weighted projectors sum to the identity on their span, as they do in the exact polytope and tegum configurations of uniform superposition?

## Why it is a question

[THEORY-021](../theory.d/THEORY-021.md), narrowed on 2026-10-19, holds that in the exact configurations
the dimensionality-weighted projectors sum to the identity:
Σᵢ Dᵢ ŵᵢŵᵢᵀ = I. The configurations are regular polygons, the tetrahedron,
antipodal pairs, and spanning tegum products of these, with equal norms
within each factor. So the features form a rank-one POVM compressed from the
n-feature basis. Until that date, [THEORY-021](../theory.d/THEORY-021.md)'s promote_when said "The
algebra is settled for the exact configurations. What is open is whether
trained models reach them", and asked for the measurement. At the owner's
direction, from the promotion audit's batch 010 (ADR-047), the THEORY was
narrowed and promoted on the re-derived algebra, and the condition moved
here unchanged.

It is open because the configurations come from the toy model's best-of-many
runs ([LIT-323](../literature.d/LIT-323.md), read in [NOTE-278](../notes.d/NOTE-278.md)), whose authors expect them to generalise
least, and nothing the record holds measures the frame operator on trained
weights. It refines [QUESTION-058](QUESTION-058.md)'s question of what a trained network's
representation carries.

## What would answer it

The condition formerly on [THEORY-021](../theory.d/THEORY-021.md), unchanged: a measurement on trained
weights, either the toy's W or a sparse autoencoder's decoder directions,
that computes Σᵢ Dᵢ ŵᵢŵᵢᵀ over the represented features and finds it close
to the identity on the span. Finding that the Dᵢ sum to m, or that the
configuration looks like a polytope, does not settle it. Leverage scores
always sum to the rank, and a polytope seen by eye is not a measured frame
operator. Trained configurations whose dimensionalities are sticky at the
polytope values while Σᵢ Dᵢ ŵᵢŵᵢᵀ stays far from the identity would refute
the account for trained models.
