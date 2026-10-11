---
status: Active
title: 'Failure of a self to hold together across contexts is a monodromy around a cycle of contexts: any two locally consistent contexts glue, and the minimal model of the obstruction needs three'
version: 1
history:
- version: 1
  date: '2026-10-11'
  note: >-
    Dual-filed from MOM-CLM-165 under ADR-037. Active here, in the
    abelian (circle-valued) case only, because the check was re-run
    independently on 2026-10-11. Gradient descent on the frustrated XY
    energy, from 60 random starts, matched the closed form
    min_k 3(1 − cos((2πk − Φ)/3)) to six decimals in all eight of MOM's
    settings, including the case 2π/3 that a careless branch choice
    gets wrong. On two contexts (one edge) the minimum was 0 for every
    random offset tried.
role: thesis
defeated_if: >-
  Two locally consistent contexts that agree on their overlap and still
  fail to glue (in the abelian setting), or a three-context cycle with
  zero monodromy whose frustrated energy has a positive minimum.
  Cover-dependence and nonabelian targets are named limits, not defeaters.
tags:
- mathematics
- self
- phenomenal-unity
date: '2026-10-11'
line: distributed-agency
summary: >-
  Dual-filed from [MOM-CLM-165](https://github.com/dmarx/mathematics-of-meaning/blob/main/record/claims.d/CLM-165.md) ([ADR-037](../decisions.d/ADR-037.md)). Model contexts (roles, personas,
  sub-agents) as a cover, and the offsets that reconcile neighbours as a
  cochain. A global section, one coherent self, exists exactly when the
  monodromy Φ around a cycle vanishes. Two contexts always glue, so
  compartmentalization needs a loop. The frustrated XY or Kuramoto energy
  finds the obstruction: its minimum is 0 exactly when Φ ≡ 0. Abelian
  case only; re-checked here.
---
<!-- inactive-ok-file: ADR-037 — Proposed; the decision this entry is filed under -->
<!-- inactive-ok-file: CLAIM-tmpigdl0 — Proposed; the open objection this result partly answers -->

# CLAIM-tmp3u2m7: Failure of a self to hold together across contexts is a monodromy around a cycle of contexts: any two locally consistent contexts glue, and the minimal model of the obstruction needs three

## The claim

From [MOM-CLM-165](https://github.com/dmarx/mathematics-of-meaning/blob/main/record/claims.d/CLM-165.md). Take the ways of being as a torsor under a group G, with
α_ij ∈ G the offset that reconciles context i with context j. On a
three-context cycle whose triple overlap is empty, the monodromy
Φ = α₁₂ + α₂₃ + α₃₁ is the Čech H¹ class. A global section, one coherent
self, exists if and only if Φ = 0. With a two-set cover the nerve is an
edge, so H¹ vanishes, and two locally consistent personas that agree on
their overlap always glue. Compartmentalization, where every pair is fine
and no whole is consistent, is a loop phenomenon.

The frustrated XY energy D(θ) = Σ[1 − cos(θ_j − θ_i − α_ij)] has a minimum
in closed form, min_k 3(1 − cos((2πk − Φ)/3)), which is 0 exactly when
Φ ≡ 0 mod 2π.

## Why this record holds it

It is re-checked (history note). It also answers, in part, an objection this
record left open. [CLAIM-tmpigdl0](CLAIM-tmpigdl0.md) says "synchronization" of a self's parts
lacks a coupling, an order parameter and transitions. Here a self's unity is
literally a phase-synchronization problem: phases θ_i, couplings with
offsets α_ij, and a global minimum that is zero or not. That holds within a
model of contexts, not of interests over time. That bearing is this record's.

## What it does not say

- **That the energy measures how dissociated someone is.** D_min depends on Φ
  only up to a half-turn and is capped at 1.5. The obstruction class is the
  invariant. The energy is a bounded readout of it. [MOM-CLM-165](https://github.com/dmarx/mathematics-of-meaning/blob/main/record/claims.d/CLM-165.md) says so.
- **Anything about nonabelian targets**, where the monodromy is
  order-dependent and there is no closed form.
- **That the result is cover-independent.** Only the cover-dependent readout
  has been computed, and refining three contexts into six can redistribute
  the frustration. MOM leaves this open, and so does this record.
