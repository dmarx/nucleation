---
number: 704
status: Active
formerly:
- THEORY-tmp4g68i
title: "In a stationary multivariate time series whose components include every relevant process, with interventions that are isolated exogenous changes and no instantaneous causation, a missing Granger-causal edge from a to b means intervening on a has no effect on b at the next step, non-ancestry means no effect at any horizon, and a set whose observed past blocks every back-door path into b's ancestors identifies the effect from observational data, as a multi-step linear-predictor coefficient in the Gaussian case"
version: 1
tags:
- causality
- mathematical-statistics
date: '2026-10-16'
source:
- LIT-1164
summary: >-
  Eichler & Didelez (2007), [LIT-1164](../literature.d/LIT-1164.md), read in full in [NOTE-941](../notes.d/NOTE-941.md). The
  back-door results are proved; the edge-to-effect statements in the
  conclusion are said to follow by the same reasoning; the front-door
  proof is deferred. All conditions are sufficient, and Assumption 2.3 is
  untestable from observational data. Two worked effects were checked.
supports:
- CLAIM-333
- CLAIM-334
---

# THEORY-704: In a stationary multivariate time series whose components include every relevant process, with interventions that are isolated exogenous changes and no instantaneous causation, a missing Granger-causal edge from a to b means intervening on a has no effect on b at the next step, non-ancestry means no effect at any horizon, and a set whose observed past blocks every back-door path into b's ancestors identifies the effect from observational data, as a multi-step linear-predictor coefficient in the Gaussian case

## Source

Eichler & Didelez (2007), "Causal Reasoning in Graphical Time Series
Models", UAI 2007: 109–116, arXiv 1206.5246, [LIT-1164](../literature.d/LIT-1164.md), read in full
in [NOTE-941](../notes.d/NOTE-941.md).

## What was actually shown

**Causation by intervention.** The effect of Xa(t) on Xb(t + h), h > 0,
is E_{σa(t)=s} Xb(t + h) for an atomic, conditional or random
intervention s (Defs. 2.1, 2.5).

**Assumption 2.3.** (i) The intervention is independent of the system's
past and of the other components at t, which excludes instantaneous
causality. (ii) The future depends on the intervention only through the
present and past. This is believable only if the system V includes every
relevant process, observed or not.

**Identification (Theorem 3.1).** If the observed past of S makes
Xb(t + h) independent of σa(t), the effect is an observational quantity.
Under Assumption 2.3, S = V always qualifies.

**Graphs (Lemma 4.10, Theorems 4.8, 4.11, 4.13).** If X satisfies the
global Granger-causal Markov property for a mixed graph, m-blocking of
every an(b)-pointing back-door path given S suffices. A front-door
criterion handles a latent confounder of the cause.

**Granger to intervention (Conclusion).** No directed edge a → b means no
effect of Xa(t) on Xb(t + 1); a ∉ an(b) means no effect at any horizon.
A present edge is "potentially causal".

**Gaussian case (Example 3.2).** The effect of setting Xa(t) = x* is
Φ_ba^{(h)}(1)x*. Examples 4.2 (back-door, latent Z) and 4.14 (front-door)
both give β₁₂β₂₃x₃*, which the reading checked against the defining
equations.

What could have come out otherwise: in Example 4.2 the latent Z biases
the one-step regression coefficients, and the effect is still recovered,
because the bias cancels in the two-step predictor.

## What this does not say

- **That measuring every relevant process is enough.** Assumption 2.3(i)
  is a separate condition. A process with every variable measured but a
  causal influence faster than the sampling step violates it, and Granger
  noncausality can then coexist with an intervention effect
  ([CLAIM-333](../claims.d/CLAIM-333.md)).
- **That a Granger-causal edge is a causal effect.** Only the absence of an
  edge is given an interventional meaning. A present edge is potential.
- **When an effect is not identifiable.** All criteria are sufficient.
- **That Assumption 2.3 can be checked from data.** It rests on background
  knowledge.
- **Anything about contemporaneous effects**, which the definitions
  exclude (h > 0).

## Connections

- It states the conditions that [NOTE-010](../notes.d/NOTE-010.md)'s C5 omits. The record's
  statement is [CLAIM-333](../claims.d/CLAIM-333.md).
- Its Assumption 2.3 is the time-series form of [THEORY-497](THEORY-497.md)'s condition
  that p(X_t′ | X_t) be a do()-distribution. Its back-door theorem needs
  no faithfulness.
- Supervenience rules out the intervention 2.3(i) requires for a macro
  variable, so macro-to-micro Granger causation is not an effect in this
  sense ([CLAIM-334](../claims.d/CLAIM-334.md)).
- Ay and Polani's information flow ([THEORY-710](THEORY-710.md)) is the
  information-theoretic measure of the same interventional notion. It
  assumes the mechanisms are known; this paper supplies conditions for
  identifying effects from observational data.
