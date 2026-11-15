---
status: Proposed
title: 'Orthogonal task updates can interact: for f_w(x) = (w·x)², the updates (1, 0) and (0, 1) from w = 0 are orthogonal, yet at x = (1, 1) their joint effect exceeds the sum of their separate effects by 2, the mixed second-order term that a model linearized at its base cannot have'
version: 1
standing: stipulated
kind: construction
tags:
- learning-theory
- mathematics
date: '2026-11-15'
line:
- learned-structure
bears_on:
- QUESTION-318
draws_on:
- THEORY-tmpkfmi5
- THEORY-tmpjlixb
summary: >-
  A's construction from A15 of the continuation of the exchange "Explain
  String Theory" (2026-11-15), after the owner's "I suspect there are
  results in the model merging literature that would be relevant here".
  The arithmetic is rechecked (scratch/formal/reconstruction_channel_checks.py).
  No paper read for this filing states it. That the interaction is the
  mixed second derivative integrated over the square, and vanishes
  identically for a model linearized at the base, is the reader's
  derivation; it matches the tangent-space regime of Ortiz-Jimenez et al.
  (THEORY-tmpkfmi5) and the second-order term Zhou et al. bound
  (THEORY-tmpjlixb). Proposed because the
  construction is A's; adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-tmpkfmi5 THEORY-tmpjlixb — Proposed; the readings the construction is set against -->

# CASE-tmp86zrj: Orthogonal task updates can interact

## The construction

The interaction of two updates on an output is

    𝓘(x) = f_{θ0+ΔA+ΔB}(x) − f_{θ0+ΔA}(x) − f_{θ0+ΔB}(x) + f_{θ0}(x)
         = ∫₀¹∫₀¹ D²_θ f_{θ0+sΔA+tΔB}(x)[ΔA, ΔB] ds dt.

For f_w(x) = (w·x)², w0 = 0, ΔA = (1, 0), ΔB = (0, 1) and x = (1, 1), the
four values are 0, 1, 1 and 4, so 𝓘 = 4 − 1 − 1 + 0 = 2, although
ΔA·ΔB = 0.

## What it shows

Orthogonality in parameter space does not make task updates add in
function. Whether they compose depends on curvature along the path that
joins them, and so on the inputs and the downstream computation. That is
why the merging papers read with this filing measure compatibility through
features, singular subspaces or a propagated interference term, not
through parameter angles.

## What it cannot show

That a given merge fails. In models fine-tuned from one start, layerwise
feature linearity often holds approximately (THEORY-tmpjlixb), so the cross
term can be small in practice.
