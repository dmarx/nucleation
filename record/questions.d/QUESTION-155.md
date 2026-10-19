---
number: 155
status: Open
formerly:
- QUESTION-tmpgpocu
title: 'Does a lossy-compression bound on generalisation error give a non-trivial value for an algorithm whose output carries infinite information about its sample, such as deterministic training of a network with continuous weights?'
version: 1
tags:
- learning-theory
- information-theory
date: '2026-10-19'
line: 'learned-structure'
summary: >-
  The promotion condition formerly on [THEORY-248](../theory.d/THEORY-248.md), moved here unchanged when
  [THEORY-248](../theory.d/THEORY-248.md) was narrowed and promoted on 2026-10-19. The bound is proved
  and finite wherever the output law's rate-distortion function is. No one
  has evaluated it for a learned model whose I(S;W) is infinite.
---

# QUESTION-155: Does a lossy-compression bound on generalisation error give a non-trivial value for an algorithm whose output carries infinite information about its sample, such as deterministic training of a network with continuous weights?

## Why it is a question

[THEORY-248](../theory.d/THEORY-248.md), narrowed on 2026-10-19, holds that the expected generalisation
error is at most √(2σ²R_E(ε)/n) + ε, with R_E(ε) the least information about
the sample carried by any surrogate output within ε in expected
generalisation error. For an L-Lipschitz loss, R_E(ε) is at most the
rate-distortion function of the output's law at distortion ε/(2L), which
can be finite where I(S;W) is infinite. Until that date, [THEORY-248](../theory.d/THEORY-248.md)'s
promote_when asked for the bound to be evaluated for such an algorithm and
found non-trivial. At the owner's direction, from the promotion audit's
batch 019 ([ADR-047](../decisions.d/ADR-047.md)), the THEORY was narrowed and promoted on the proved
bound, and the condition moved here unchanged.

It is open because the bound depends on the unknown data distribution,
through P_W, and [LIT-236](../literature.d/LIT-236.md) evaluates it only for a Gaussian mean, with a units
error ([NOTE-780](../notes.d/NOTE-780.md)). Finite is not the same as non-vacuous.

## What would answer it

The condition formerly on [THEORY-248](../theory.d/THEORY-248.md), unchanged. A bound of this form,
R_E(ε) or the rate-distortion function of the output's law, is evaluated
for an algorithm whose I(S;W) is infinite, such as deterministic training
of a network with continuous weights, and gives a non-trivial value. The
distortion must be measured in the units the Lipschitz condition uses.
Correlations between estimated compressibility and test error across
training settings cannot settle it, since they do not show that the bound
holds or is tight.
