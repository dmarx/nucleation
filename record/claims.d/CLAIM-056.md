---
number: 56
status: Active
formerly:
- CLAIM-tmpghha4
title: 'Local transport errors in a reconstruction chain are bounded by the per-step discrepancies weighted by the sensitivity of the later reconstructions, so the same local error can be damped, accumulated or amplified, and local similarity can coexist with large global drift; the bound measures departure from a reference transport, not whether the act survives'
version: 4
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
- version: 3
  date: '2026-10-29'
  note: >-
    Narrowed and promoted by the tenth status review (ADR-057). CLAIM-031
    and CLAIM-208 are written in (ADR-059): the recursion is a bound, not
    a prediction, and it measures departure from a reference transport,
    not whether the act survives. The defeat condition now names the
    design CLAIM-208 asks for, as CLAIM-059's already does. Version 2's
    title read 'Local transport errors propagate through later
    reconstructions according to the dynamics of those reconstructions,
    so the same local error can be damped, accumulated or amplified, and
    local similarity can coexist with large global drift'; its condition
    read 'In serial reconstruction chains, end-to-end drift is not
    predicted by per-step discrepancies combined with the measured
    sensitivity of later steps.' Premises CLAIM-106 and CLAIM-267 are
    Active, and nothing in the record meets the condition. Proposed to
    Active.
- version: 4
  date: '2026-10-29'
  note: >-
    Its supports entry for CLAIM-068 is removed: the fourteenth status
    review, at the status review's ruling (the owner delegated these
    rulings; ADR-057), dropped this claim from CLAIM-068's rests_on,
    whose body never uses it. The claim is unchanged.
role: thesis
warrant: interpretive
defeated_if: >-
  A serial reconstruction chain whose per-step kernels are estimated from
  several independent retellers on held-out and perturbed inputs, in a
  metric fixed before the data, and whose end-to-end departure from the
  reference transport, on chains not used in the estimation, exceeds the
  bound computed from those estimates by more than their estimation
  error. Such a chain would show that its steps are not a composition of
  per-step transports, as when a reteller sees earlier generations. A
  chain that stays below the bound, however far, does not defeat it.
tags:
- mathematics
- probabilistic-modeling
date: '2026-10-08'
line: pragmatic-transport
works:
- WORK-002
rests_on:
- CLAIM-106
- CLAIM-267
summary: >-
  A50 §2–3, kept nearly verbatim in outline v4 and the manuscript §8.
  The manuscript later restricts the expansive regime: for stochastic
  kernels in total variation, contraction coefficients do not exceed
  one.
supports:
- CLAIM-081
- CLAIM-114
- CLAIM-059
objected_by:
- CLAIM-031
- CLAIM-208
---
<!-- inactive-ok-file: CLAIM-068 — Proposed; open, and cited as open: the claim, argument or reading is under test, not settled -->

# CLAIM-056: Local transport errors in a reconstruction chain are bounded by the per-step discrepancies weighted by the sensitivity of the later reconstructions, so the same local error can be damped, accumulated or amplified, and local similarity can coexist with large global drift; the bound measures departure from a reference transport, not whether the act survives

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

- That a small error means the act survived, or a large one that it did
  not. A chain reorganizes constraints, and one changed constraint can
  change the act while the scalar error stays small ([CLAIM-031](CLAIM-031.md)).
- That the bound predicts drift. It is an upper bound. Its constants
  belong to the retellers' kernels, which a chain with one retelling per
  node cannot estimate ([CLAIM-208](CLAIM-208.md)).

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

## Note of 2026-10-29: the concessions written in

The note of 2026-10-19 left [CLAIM-031](CLAIM-031.md) and [CLAIM-208](CLAIM-208.md) unanswered. Both are
conceded here, by the title and the defeat condition, not answered. What
the claim adds to [CLAIM-267](CLAIM-267.md) is that a serial reconstruction chain is a
composition of transports measured against a reference transport
([CLAIM-106](CLAIM-106.md)). The new condition tests exactly that. Promoted by the tenth
status review on the owner's ruling.
