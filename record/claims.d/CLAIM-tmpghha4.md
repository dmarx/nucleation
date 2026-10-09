---
status: Proposed
title: 'Local transport errors propagate through later reconstructions according to the dynamics of those reconstructions, so the same local error can be damped, accumulated or amplified, and local similarity can coexist with large global drift'
version: 1
role: thesis
defeated_if: >-
  In serial reconstruction chains, end-to-end drift is not predicted by
  per-step discrepancies combined with the measured sensitivity of later
  steps.
tags:
- mathematics
- probabilistic-modeling
date: '2026-10-08'
line: pragmatic-transport
works:
- what-survives-translation
rests_on:
- CLAIM-tmpumy4f
summary: >-
  A50 §2–3, kept nearly verbatim in outline v4 and the manuscript §8.
  The manuscript later restricts the expansive regime: for stochastic
  kernels in total variation, contraction coefficients do not exceed
  one.
supports:
- CLAIM-tmpj8d91
---
<!-- inactive-ok-file: CLAIM-tmpj8d91 CLAIM-tmpumy4f — Proposed; open, and cited as open: the claim, argument or reading is under test, not settled -->

# CLAIM-tmpghha4: Local transport errors propagate through later reconstructions according to the dynamics of those reconstructions, so the same local error can be damped, accumulated or amplified, and local similarity can coexist with large global drift

## The claim

A50: "similarity is not transitive", and "assuming a metric", per-step closeness
ε gives only d(u_0, u_n) ≤ nε. With local discrepancy ε_i and Lipschitz
constant L_i for the later dynamics, e_(i+1) ≤ L_i e_i + ε_i, so
e_n ≤ (∏ L_j) e_0 + Σ ε_i ∏_(j>i) L_j. "This tells us that the impact of local
translation errors depends on the dynamics of subsequent interpretation." Three
regimes: contractive (L < 1, distortions dampen), neutral (L = 1, errors
accumulate), expansive (L > 1, errors amplify).

Manuscript §8 has the same recursion with κ_i, and adds: "For stochastic kernels
in total variation, contraction coefficients do not exceed one; amplification
may arise under other metrics or nonlinear, adaptive representations.
Crucially, the bound quantifies departure relative to a reference transport,
not loss of every communicative virtue." That last sentence descends from A52
§5.2: "Interpret the bound as a statement about error propagation, not a claim
that all communicative changes are errors."

## What it does not say

That drift is random: A50 went on to attraction ([CLAIM-tmpj8d91](CLAIM-tmpj8d91.md)). Nor that it holds
for directed, non-metric distortion ([QUESTION-tmpklhva](../questions.d/QUESTION-tmpklhva.md)).
