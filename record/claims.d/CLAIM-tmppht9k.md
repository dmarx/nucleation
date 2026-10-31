---
status: Active
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
complements:
- CLAIM-414
- CLAIM-079
- CLAIM-481
bears_on:
- QUESTION-125
grounds:
- 'CASE-tmpwxags'
summary: >-
  From A12 §6 of the exchange "Analyze nucleation concepts" (2026-10-31),
  which called it "a surprising result". It is generic for any saddle-node
  whose fold sits away from zero with no feedback from the coupled units to
  the maintaining core, so it is built in rather than surprising. It is
  filed because it is a construction QUESTION-125 asks for: one in which
  the regime changes while the block's gap does not. All numbers were
  recomputed.
---
<!-- inactive-ok-file: QUESTION-125 — Open; the question this construction bears on, cited as open -->

# CLAIM-tmppht9k: An organization's present coupling strength need not reveal the stability of the process maintaining it: in a constructed system whose maintained connector and capacities set a three-unit coupling, the recovery rate of the maintenance goes to zero at its saddle-node while the coupling's spectral gap there stays near 0.989

## The claim

In the seed–capture model of CASE-tmpwxags, with symmetric damage d, the
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
  question. CLAIM-481 separates what coupling does to time scales; this
  claim separates what coupling shows about its own maintenance.
- **That early-warning signals would catch it.** Critical slowing appears in
  the maintenance, not in the coupling. Why such signals are weak evidence
  anyway is THEORY-136's and THEORY-214's point.
