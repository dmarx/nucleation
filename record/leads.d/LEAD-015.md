---
number: 15
status: Open
formerly:
- LEAD-tmp0ccpq
title: 'Derive the two-institution version of the symmetry-breaking condition, building the coupled meaning-influence model for two regulators'
version: 1
stage: specified
priority: high
method:
- formal
tags:
- complex-systems
- self-governance
- society-and-governance
date: '2026-11-19'
line:
- distributed-agency
advances:
- CLAIM-404
- CLAIM-330
operationalized_in:
- CASE-092
presupposes:
- LEAD-090
summary: >-
  [CLAIM-404](../claims.d/CLAIM-404.md) is a premise of [CLAIM-545](../claims.d/CLAIM-545.md) and rests on a model that has not
  been built. Named in [CLAIM-404](../claims.d/CLAIM-404.md). Filed by the backlog audit of
  2026-11-19.
---
<!-- inactive-ok-file: CASE-tmpd80em CLAIM-tmp0v3wu CLAIM-tmpz8q70 CLAIM-tmp42aba — new; filed 2026-11-22 for LEAD-015 and cited in the note of that date -->
<!-- inactive-ok-file: CASE-363 CLAIM-947 CLAIM-948 — new; filed 2026-11-22 for LEAD-090 and cited in the note of that date -->
<!-- inactive-ok-file: CLAIM-545 — Proposed; cited in the backlog audit of 2026-11-19 -->

# LEAD-015: Derive the two-institution version of the symmetry-breaking condition, building the coupled meaning-influence model for two regulators

## What it would do

Extend the model to two regulating institutions and derive the condition
under which their symmetric state is unstable, as [CLAIM-330](../claims.d/CLAIM-330.md) does for one.

Where the record names it:

- [CLAIM-404](../claims.d/CLAIM-404.md): "it is a local instability condition for [CASE-092](../cases.d/CASE-092.md)'s unbuilt
  model, and the two-institution version has not been derived."

## What would count

A derived condition gives [CLAIM-404](../claims.d/CLAIM-404.md) a worked model and may move its
warrant to demonstrated. A model in which no such instability exists
defeats it.

## Note of 2026-11-22: what [LEAD-090](LEAD-090.md)'s build gives this lead

[LEAD-090](LEAD-090.md), which this lead presupposes, was carried out as [CASE-363](../cases.d/CASE-363.md). The one-institution model is now built (scratch/studies/lead-090/model.py), with its mean-field map, its Jacobian, the closed-form threshold gσ² > 2(1 − φ(1 − ε)) ([CLAIM-947](../claims.d/CLAIM-947.md)), and an exact rewriting as weighted averaging with stubborn sources and agreement-weighted adaptive weights ([CLAIM-948](../claims.d/CLAIM-948.md)). Its fixed points are a Curie–Weiss equation, so a two-institution version would be two such fields coupled, with its symmetric-state condition read from a 4×4 Jacobian of the same kind of entries. What remains is this lead's own step: to say how the regulator's evidence or resources depend on the regulated institution's state ([CLAIM-404](../claims.d/CLAIM-404.md)'s closing of the loop between the two) and derive that condition. No status or stage is changed.

## Note of 2026-11-22: derived, in [CASE-tmpd80em](../cases.d/CASE-tmpd80em.md)

The two-institution model is built and its condition derived, as [CASE-tmpd80em](../cases.d/CASE-tmpd80em.md) (code, tests, derivation and results in scratch/studies/lead-015/). Two of [CASE-363](../cases.d/CASE-363.md)'s reduced institutions, an evaluator and an evaluated party, are coupled through four channels read from [CLAIM-404](../claims.d/CLAIM-404.md): the party's meaning tilts the evaluator's evidence (θ) and its conferral (ω); the evaluator's reading is evidence for the party (χ) and redistributes authority inside it (ψ). This is the step the note above left open: how the regulator's evidence or resources depend on the regulated institution's state.

- **The condition** ([CLAIM-tmp0v3wu](../claims.d/CLAIM-tmp0v3wu.md), demonstrated). With nonnegative channels and each institution stable alone, the symmetric state is unstable exactly when (θ + σ_E ω)(χ + σ_P ψ) > Δ_E Δ_P, Δ_i = (1 − φ′_i) − g_iσ_i²/2; in general, when the round-trip gain ρ(G_P C_PE G_E C_EP) exceeds 1. The rates and memories cancel. 1,802 of 1,802 random parameter sets agreed with the nonlinear map.
- **What it says for [CLAIM-404](../claims.d/CLAIM-404.md)** ([CLAIM-tmpz8q70](../claims.d/CLAIM-tmpz8q70.md), demonstrated). Such an instability exists, so the lead's defeater ("A model in which no such instability exists") is not met by this model. It captures the evaluator's reading with neither institution having a loop inside it, with the evaluator in Regime B (its authority stays balanced, its reading does not), and with its evidence independent while a resource channel runs. Cutting the return channel removes it.
- **An alternative reading of "resources"** ([CLAIM-tmp42aba](../claims.d/CLAIM-tmp42aba.md), demonstrated). As capacity (the party scaling the evaluator's conferral gain) rather than direction, resources drop from the linear condition but capture one side below it from a large push.

Whether [CLAIM-404](../claims.d/CLAIM-404.md)'s warrant should move from interpretive toward demonstrated for its third part, and which reading of resources the record takes, are the owner's. Not done: a condition for the oscillatory instability under corrective channels, and the basins of the below-threshold captures. No status or stage is changed.
