---
status: Proposed
title: 'Two organizations equally impaired during an emotional episode, one dysregulated in DBT''s sense, its threat perspective''s baseline raised by the episode and decaying slowly, the other in the attentional sense, its task sharing a fixed budget with a competing demand: only the first stays impaired after the episode ends, and lowering activation repairs only the first while removing the competing demand repairs only the second'
version: 1
standing: fictional
kind: construction
tags:
- psychopathology-and-treatment
- emotion-and-affect
- self-governance
date: '2026-11-04'
line:
- will-organization
illustrates:
- CLAIM-tmp99a8m
summary: >-
  A construction for the two readings of "cognitive dysregulation" in the
  owner's U29 of the exchange "Organizational Nucleation and SLT"
  (2026-11-04), made at the owner's review: the DBT reading of
  [CLAIM-tmp99a8m](../claims.d/CLAIM-tmp99a8m.md) and A29's attentional reading. Both organizations score
  0.400 during the episode. Afterwards the DBT arm scores 0.655 over the
  next ten time units and stays below 0.95 for 11.0, and its tolerance is
  negative for 12.5, while the attentional arm recovers at once. The
  script is scratch/formal/r3_dysregulation_arms.py. The construction is
  the filer's.
---
<!-- inactive-ok-file: CLAIM-tmp99a8m CLAIM-tmp8e3ye CLAIM-286 — Proposed or new; cited from the exchange "Organizational Nucleation and SLT" of 2026-11-04 as open -->

# CASE-tmp5hhsy: Two organizations equally impaired during an emotional episode, one dysregulated in DBT's sense, its threat perspective's baseline raised by the episode and decaying slowly, the other in the attentional sense, its task sharing a fixed budget with a competing demand: only the first stays impaired after the episode ends, and lowering activation repairs only the first while removing the competing demand repairs only the second

## The case

Each organization does a task whose performance runs from 0 to 1. An
episode lasts from t = 10 to t = 20.

- **The DBT arm.** A threat perspective has activation
  z = b(t) + α d(t), with discrepancy d = 1 during the episode, and is
  active with probability q = σ(κ(z − θ)), as in [CLAIM-tmp8e3ye](../claims.d/CLAIM-tmp8e3ye.md). Its
  baseline is raised by the episode and decays slowly:
  db/dt = −(b − b₀)/τ_b + γ d, with α = 2, b₀ = 0, θ = 1, κ = 8,
  τ_b = 15 and γ = 0.2. While it is active its interpretation is the one
  governance acts on, and the task scores 1 − 0.6 q. These are
  [CLAIM-tmp99a8m](../claims.d/CLAIM-tmp99a8m.md)'s three parameters for Linehan's sensitivity, intensity
  and slow return to baseline.
- **The attentional arm.** The task needs r = 1 of a budget B = 1, and a
  competing demand takes D = 0.6 of it during the episode, so the task
  scores min(1, (B − D)/r). This is A29 §7's Σᵢ rᵢ ≤ Bₜ.

The numbers, from scratch/formal/r3_dysregulation_arms.py:

| arm | during (t 12–20) | t 20–30 | t 30–50 | below 0.95 after the episode |
|---|---|---|---|---|
| DBT | 0.400 | 0.655 | 0.988 | 11.0 |
| attentional | 0.400 | 1.000 | 1.000 | 0 |
| DBT, activation lowered at t = 15 | 0.775 | 1.000 | 1.000 | 0 |
| DBT, competing demand removed | 0.400 | 0.655 | 0.988 | 11.0 |
| attentional, demand removed at t = 15 | 0.775 | 1.000 | 1.000 | 0 |
| attentional, activation lowered | 0.400 | 1.000 | 1.000 | 0 |

In the DBT arm the baseline peaks at b = 1.460, above θ, so after the
episode the perspective is active with no discrepancy at all. Its
tolerance at ε = 0.05, (θ + κ⁻¹ logit ε − b)/α, is negative for 12.5 time
units after the episode ends: [CLAIM-tmp8e3ye](../claims.d/CLAIM-tmp8e3ye.md)'s mark of activation driven
by something other than the discrepancy.

## What it can show

- **Equal impairment does not tell the readings apart.** Both arms score
  0.400 during the episode, by construction.
- **The time course does.** Only the DBT arm outlasts the episode, for as
  long as its baseline takes to return.
- **So does intervention.** Lowering activation, standing in for DBT's
  emotion-regulation and distress-tolerance skills, repairs only the DBT
  arm. Removing the competing demand, reprioritizing, repairs only the
  attentional arm. Each intervention does nothing to the other arm,
  because the other arm has no term for it to act on.

## What it cannot show

- That either mechanism is how cognitive dysregulation works in anyone.
  The parameters are chosen to make the arms equal during the episode.
- That the two are exclusive. A person can have both; the construction
  keeps them apart only to show what separates them.
- That lowering activation is what DBT's skills do. That is
  [CLAIM-tmp99a8m](../claims.d/CLAIM-tmp99a8m.md)'s reading, not a finding ([THEORY-922](../theory.d/THEORY-922.md) concerns urges, not
  cognition).
