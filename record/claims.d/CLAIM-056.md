---
number: 56
status: Proposed
formerly:
- CLAIM-tmpghha4
title: 'Local transport errors propagate through later reconstructions according to the dynamics of those reconstructions, so the same local error can be damped, accumulated or amplified, and local similarity can coexist with large global drift'
version: 2
history:
- version: 2
  date: '2026-10-19'
  note: >-
    Warrant corrected from demonstrated to interpretive at the owner's
    direction, carrying out the promotion audit's decision
    (record/promotion-audit/decisions/CLAIM-056.yaml, batch 004, ADR-047).
    The recursion, its three regimes and the total-variation restriction
    have been CLAIM-267's since the ADR-040 split of 2026-10-13. What this
    claim adds is that transport errors in serial reconstruction chains
    behave so, and its defeat condition is empirical with no observation
    under it, which ADR-043 counts as interpretive. The status stays
    Proposed.
role: thesis
warrant: interpretive
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
- CLAIM-106
- CLAIM-267
summary: >-
  A50 §2–3, kept nearly verbatim in outline v4 and the manuscript §8.
  The manuscript later restricts the expansive regime: for stochastic
  kernels in total variation, contraction coefficients do not exceed
  one.
supports:
- CLAIM-068
- CLAIM-081
- CLAIM-114
- CLAIM-059
objected_by:
- CLAIM-031
- CLAIM-208
---
<!-- inactive-ok-file: CLAIM-068 — Proposed; open, and cited as open: the claim, argument or reading is under test, not settled -->

# CLAIM-056: Local transport errors propagate through later reconstructions according to the dynamics of those reconstructions, so the same local error can be damped, accumulated or amplified, and local similarity can coexist with large global drift

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

That drift is random: A50 went on to attraction ([CLAIM-068](CLAIM-068.md)). Nor that it holds
for directed, non-metric distortion ([QUESTION-017](../questions.d/QUESTION-017.md)).

## Note of 2026-10-13: the general content is filed separately

Under [ADR-040](../decisions.d/ADR-040.md), the error recursion and its three regimes is filed on its own as [CLAIM-267](CLAIM-267.md), in the
formal-apparatus line, resting on no claim. This claim now rests on it for
the general content, and keeps [CLAIM-106](CLAIM-106.md)'s graded fidelity, which makes the discrepancy a transport error. Claims in other lines that need
only the general content cite [CLAIM-267](CLAIM-267.md), so setting pragmatic-transport aside
does not take it from them.

## Note of 2026-10-19: the warrant

The derivation is [CLAIM-267](CLAIM-267.md)'s. This claim applies it to serial reconstruction
chains, reading the per-step discrepancy as a transport error against a
reference transport, which rests on [CLAIM-106](CLAIM-106.md)'s graded fidelity. Whether
end-to-end drift in real chains follows the per-step discrepancies and the
later steps' sensitivity is what the defeat condition tests, and no such
measurement is held. So the warrant is interpretive. [CLAIM-031](CLAIM-031.md) and [CLAIM-208](CLAIM-208.md)
object to it and are unanswered.
