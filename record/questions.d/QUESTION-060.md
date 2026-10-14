---
number: 60
status: Open
formerly:
- QUESTION-tmplynfm
title: 'When a network is trained on data from a structured system, are the variables it comes to represent fixed by its training objective or by what its architecture can represent cheaply, and when do they coincide with the system''s own relevant variables?'
version: 1
tags:
- natural-sciences
- representation-learning
- mathematics
date: '2026-10-12'
line: 'learned-structure'
answered_by:
- THEORY-197
- THEORY-206
summary: >-
  Filed in the fourth synthesis pass to give readings no question asked
  for a place in the argument. It bears on [CLAIM-152](../claims.d/CLAIM-152.md) and [QUESTION-025](QUESTION-025.md).
  [THEORY-197](../theory.d/THEORY-197.md) and [THEORY-206](../theory.d/THEORY-206.md) answer it in part; the body gives each one's
  limit.
---
<!-- inactive-ok-file: THEORY-tmp37j6t THEORY-tmpbx1ck THEORY-tmpn31af — Proposed; partial answers filed today, cited with their limits -->

# QUESTION-060: When a network is trained on data from a structured system, are the variables it comes to represent fixed by its training objective or by what its architecture can represent cheaply, and when do they coincide with the system's own relevant variables?

## The question

A trained network ends up with some internal variables and not others. Two separate things constrain which. One is the objective: what the training rewards keeping. The other is the architecture: which functions it can represent, and at what size. The question is how far each fixes the learned variables. It also asks when the result matches the variables that matter for the system that produced the data, such as the relevant operators of a physical model.

## Why the record needs it

Other lines lean on the answer. [CLAIM-152](../claims.d/CLAIM-152.md) says that what a compression keeps is relative to the target it is sufficient for. A training objective is such a target, so this line inherits that relativity as a claim about networks. [QUESTION-025](QUESTION-025.md) asks whether embeddings carry attribute directions and a concept lattice. Whether those directions appear depends both on the objective and on what the architecture can afford to represent.

## What the record holds

- [THEORY-197](../theory.d/THEORY-197.md): the RBM–renormalization correspondence is "an identity of parametrizations". Away from an exact fit, it "does not make training by distribution fitting a renormalization". In the counterexample, a contrastive-divergence RBM spends its units on noise rather than on the relevant fields. The objective, not the formal match, constrains what is kept. Limit: one counterexample, Boltzmann machines only.
- [THEORY-206](../theory.d/THEORY-206.md): one hidden layer needs "exactly ∏(rᵢ+1) neurons" for a monomial, against O(Σ log rᵢ) for a deep network. So the architecture makes products of many inputs costly, while "bounded-degree polynomials do not" separate depths. Limit: it concerns what networks can represent, not what training finds. It assumes bias-free smooth units, and the uniform lower bound is unproved.
- [THEORY-tmp37j6t](../theory.d/THEORY-tmp37j6t.md): SGD fitting three Picbreeder images in the evolved networks' own architecture does not reproduce their reuse and factoring. With function and architecture both held fixed, the internal variables still differ. Limit: the contrast is between an objective-trained network and one found by target-free search, not between two objectives; qualitative, three images.
- [THEORY-tmpbx1ck](../theory.d/THEORY-tmpbx1ck.md): when a generator's latent dynamics factor, small transformers trained by next-token prediction settle near the factored dimension in approximately orthogonal subspaces, and reach it first even when noise makes it lossy. Limit: the objective is never varied, and architecture is not separated from training.
- [THEORY-tmpn31af](../theory.d/THEORY-tmpn31af.md): models trained on a graph's edge bigrams store it as a global spectral geometry, although a lookup is representable, as cheap and faster to reach. It names training dynamics as a third determinant beside objective and architecture. Limit: empirical; the spectral analysis is informal and for a two-layer model only.

## What would answer it

A family of systems with known relevant variables, trained under objectives and architectures varied separately. With it, a measure of which variables each combination keeps. Or a result that predicts the learned variables from objective and capacity together.
