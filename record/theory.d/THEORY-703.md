---
number: 703
status: Proposed
formerly:
- THEORY-tmp427vb
promote_when: >-
  A system whose degree of weak emergence is fixed by a criterion that does
  not use G-emergence or its regressions, such as Bedau's incompressibility
  shown analytically or a ΦID or dynamical-independence computation on the
  same data, in which G-emergence orders the cases as that criterion does,
  and keeps the order when the regression class is enlarged until the
  micro-to-macro prediction is no longer misspecified. Another hand-built
  model whose conditions are chosen to look emergent does not settle it.
title: "Weak emergence of a macro variable from micro variables can be measured as its Granger autonomy from them times their mean Granger causation of it, which is zero if it is independent of them or fully predicted by them; in a boids model this measure, and Granger causation from the flock's centre of mass to each boid, are higher for flocking than for random or rigid motion; the measure is relative to the regression model and the variables included"
version: 1
tags:
- complex-systems
- causality
date: '2026-10-16'
source:
- LIT-1170
summary: >-
  Seth (2010), [LIT-1170](../literature.d/LIT-1170.md), read in full in [NOTE-935](../notes.d/NOTE-935.md). The definitions
  are exact; the evidence is two hand-built agent-based models. Seth
  concedes that the measure is epistemic: positive with missing micro
  factors or a limited predictor, zero with the system as predictor.
  Proposed until it is tested against an independent criterion.
supports:
- CLAIM-334
---

# THEORY-703: Weak emergence of a macro variable from micro variables can be measured as its Granger autonomy from them times their mean Granger causation of it, which is zero if it is independent of them or fully predicted by them; in a boids model this measure, and Granger causation from the flock's centre of mass to each boid, are higher for flocking than for random or rigid motion; the measure is relative to the regression model and the variables included

## Source

Seth (2010), "Measuring Autonomy and Emergence via Granger Causality",
*Artificial Life* 16(2): 179–196, [LIT-1170](../literature.d/LIT-1170.md), read in full in
[NOTE-935](../notes.d/NOTE-935.md) from the deposited published version.

## What was actually shown

**Definitions.** G-autonomy ga_{X|E} = log(var(ε without X's own
lags)/var(ε full)) (Eq. 3). G-emergence ge_{M|m} = ga_{M|m}·(1/N)Σ
gc_{mᵢ→M} (Eq. 4), with Taylor-expanded regressors for the nonlinear
version (Eqs. 5–6).

**A constructed system (Eq. 7, Table 1).** G-autonomy is zero for white
noise and for a variable driven only by white noise, and high for
variables with their own autoregressive terms. The set of G-causalities
does not fix the G-autonomies.

**Predator–prey (§3).** Predator G-autonomy orders the four conditions
as built, and the evolved controller beats the rule that uses internal
state.

**Boids (§4).** G-emergence of the centre of mass and Granger causation
from it to the boids are higher in the hand-chosen flocking condition
than in rigid or random motion, linear and nonlinear alike.

What could have come out otherwise: G-emergence could have failed to
separate the three boids conditions, or been highest for the rigid
formations.

## What this does not say

- **That G-emergence measures emergence independently of the analyst.** It
  is positive when micro factors are missing or the predictor is limited,
  and would be zero with the system itself as predictor (§5.2).
- **That downward Granger causation is downward causation.** It is Granger
  causation from macro to micro, which Seth calls "ontologically
  innocent". An intervention on the centre of mass that leaves the boids
  at that time unchanged does not exist, so it is not an interventional
  effect in [THEORY-704](THEORY-704.md)'s sense ([CLAIM-334](../claims.d/CLAIM-334.md)).
- **That evolution promotes autonomy in general.** One model, one evolved
  controller, conditions ordered by construction.
- **Anything about consciousness.** §5.3's link to volition is a
  hypothesis, untested.
- **That the measure is robust.** Fig. 6's smoothness is by inspection.

## Connections

- [THEORY-497](THEORY-497.md) (ΦID) and [THEORY-257](THEORY-257.md) (dynamical independence) are later
  accounts of the same phenomenon. Dynamical independence asks only that
  the micro history add nothing to the macro variable's self-prediction.
  G-emergence asks for dependence and autonomy at once.
- Hoel et al.'s complaint that Granger emergence is not causal
  ([NOTE-726](../notes.d/NOTE-726.md)) is one Seth accepts.
- [TERM-058](../terms.d/TERM-058.md) defines Granger causality in the record's own words.
