---
number: 521
status: Active
formerly:
- CLAIM-tmppht9k
title: 'An organization''s present coupling strength need not reveal the stability of the process maintaining it: in a constructed system whose maintained connector and capacities set a three-unit coupling, the recovery rate of the maintenance goes to zero at its saddle-node while the coupling''s spectral gap there stays near 0.989'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the computed equilibrium curve, fold or spectral gap of
  CASE construction cited, or a showing that the dissociation depends on a
  feature the construction lacks. A general argument about other systems
  cannot defeat what is an existence claim.
tags:
- complex-systems
- individuation
date: '2026-10-31'
line:
- distributed-agency
- formal-apparatus
works:
- WORK-010
complements:
- CLAIM-414
- CLAIM-079
- CLAIM-481
bears_on:
- QUESTION-125
grounds:
- 'CASE-189'
summary: >-
  From A12 §6 of the exchange "Analyze nucleation concepts" (2026-10-31),
  which called it "a surprising result". It is generic for any saddle-node
  whose fold sits away from zero with no feedback from the coupled units to
  the maintaining core, so it is built in rather than surprising. It is
  filed because it is a construction [QUESTION-125](../questions.d/QUESTION-125.md) asks for: one in which
  the regime changes while the block's gap does not. All numbers were
  recomputed.
---
<!-- inactive-ok-file: QUESTION-125 — Open; the question this construction bears on, cited as open -->

# CLAIM-521: An organization's present coupling strength need not reveal the stability of the process maintaining it: in a constructed system whose maintained connector and capacities set a three-unit coupling, the recovery rate of the maintenance goes to zero at its saddle-node while the coupling's spectral gap there stays near 0.989

## The claim

In the seed–capture model of [CASE-189](../cases.d/CASE-189.md), with symmetric damage d, the
positive equilibria satisfy q = 11/12 − 1/(12c²) and
d(c) = (11c² − 1)/(3c(1 + c²)) − 1. The curve has its maximum at
c*² = (7 + 2√15)/11, so c* ≈ 1.1578, q* ≈ 0.8545 and d* ≈ 0.6908: a
saddle-node, beyond which the maintained regime does not exist. Approaching
it, the slowest eigenvalue of the maintenance dynamics goes to zero (A12's
table: −0.8102, −0.5448, −0.3834, −0.2041, −0.0571 as d nears d*).

The three-unit coupling is L = q Bᵀ diag(c₁, c₂) B. At the fold its
spectrum is {0, w, 3w} with w = q*c*, so its gap is λ₂ ≈ 0.9894. The coupled
units are as tightly integrated at the edge of collapse as well inside the
regime.

A12: "An organization's current causal effectiveness need not reveal the
stability of the processes that sustain that effectiveness", and
"maintenance-based individuation identifies a different organizational
property from coupling-based individuation".

## What it does not say

- **That this is surprising.** With no feedback from the coupled units to
  the core, the gap depends on the equilibrium's value and not on its
  stability, so any such fold at nonzero value gives it.
- **That coupling-based identification is wrong.** It answers a different
  question. [CLAIM-481](CLAIM-481.md) separates what coupling does to time scales; this
  claim separates what coupling shows about its own maintenance.
- **That early-warning signals would catch it.** Critical slowing appears in
  the maintenance, not in the coupling. Why such signals are weak evidence
  anyway is [THEORY-136](../theory.d/THEORY-136.md)'s and [THEORY-214](../theory.d/THEORY-214.md)'s point.
- **That the coupling lasts to the fold in a finite system.** The fold is a
  deterministic, infinite-size statement. In a finite system the
  maintained regime is metastable, and the coupling is lost when the
  regime is, at the escape time. The barrier closes as the distance to the
  fold to the power 3/2 ([THEORY-1273](../theory.d/THEORY-1273.md)), so the hazard of escape rises as
  the fold nears. Whether the loss is observed before the fold depends on
  size, noise, the observation horizon and how fast the parameter moves.
  The dissociation holds for as long as the regime does.

## Note of 2026-11-01: where coupling carries maintenance, the dissociation fails

Bechtel and Abrahamsen ([LIT-1936](../literature.d/LIT-1936.md), p. 327) report To et al.'s (2007)
model of the SCN. About 40% of cells can sustain oscillation alone, and
without the coupling peptide VIP about 60% become arrhythmic. For those
cells the coupling is what maintains the oscillation. That is the
feedback from coupled units to the maintaining process that this claim's
construction excludes. In such an architecture, losing the coupling and
losing maintenance go together, so the coupling would not stay strong up
to a fold of maintenance. This is a contrast, not a counterexample. It
supports the claim's own statement that the dissociation belongs to
architectures without that feedback.

No status, title or warrant changes.
