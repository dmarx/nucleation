---
number: 1528
status: Proposed
formerly:
- THEORY-tmpwbm0d
promote_when: >-
  An independent simulation or experiment on loopy 4-vertex crease
  patterns designed with one folding motion reproduces exponential growth
  of distractor branches with pattern size, and shows that whether the
  actuated creases' folding islands cover the sheet predicts folding
  success better than the number of actuators.
title: 'Crease patterns designed with one folding motion inevitably have exponentially many distractor branches meeting at the flat state, created by frustrated loops of two-branch vertices, and the spatial placement of actuators, read through the cover of their folding islands, predicts folding success better than their number'
version: 1
tags:
- natural-sciences
- complex-systems
- mathematics
date: '2026-11-06'
source:
- LIT-2074
extends:
- THEORY-1418
summary: >-
  The generalization Stern, Pinson & Murugan (2017), [LIT-2074](../literature.d/LIT-2074.md), read in
  [NOTE-1571](../notes.d/NOTE-1571.md), assert: in their abstract, that "even crease patterns with
  only one designed folding motion inevitably contain an exponential
  number of ‘distractor’ folding branches", and in their results, that the
  union of folding islands is "a much better predictor of folding success
  than just the number of actuators". Split from [THEORY-1418](THEORY-1418.md) at its
  narrowing by the status review of 2026-11-06 ([ADR-047](../decisions.d/ADR-047.md) kind 1), keeping
  its old promote_when. One study: idealized rigid panels, zero-temperature
  descent, meshes up to 6 × 6, actuation on one 4 × 4 pattern.
---

# THEORY-1528: Crease patterns designed with one folding motion inevitably have exponentially many distractor branches meeting at the flat state, created by frustrated loops of two-branch vertices, and the spatial placement of actuators, read through the cover of their folding islands, predicts folding success better than their number

## Source

Stern, Pinson & Murugan (2017), [LIT-2074](../literature.d/LIT-2074.md); read from the arXiv v1 preprint in
[NOTE-1571](../notes.d/NOTE-1571.md). What the one study measured is [THEORY-1418](THEORY-1418.md)'s.

## What was actually shown

Only what [THEORY-1418](THEORY-1418.md) reports: N_branches ∼ 2^(α√A), α ≈ 2.25, on random quad
meshes up to 6 × 6; the over-determined fourth vertex of a loop as the
source of the glassy landscape; and, on one 4 × 4 pattern, five actuators
"60× more likely to fold the pattern if it has U F I = 1 rather than U F I <
1". The general form stated here is the authors' extrapolation from those.

## What this does not say

- That covering folding islands is necessary or sufficient for folding: the
  authors "are unable to formulate a strict necessary and sufficient
  condition".
- That the difficulty persists beyond the flat state.
- That folding self-folding origami is NP-hard; the comparison with SAT is
  an analogy.
