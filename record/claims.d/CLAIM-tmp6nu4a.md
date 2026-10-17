---
status: Active
title: 'Measuring every relevant variable is necessary but not sufficient for a Granger-causal analysis to say anything about interventions: the intervention must also be an isolated exogenous change and no influence may act within one sampling step, and then Granger noncausality implies no intervention effect and the effect is identified from the observational predictor, but a Granger-causal relation is still only potentially causal'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  A flaw in the counterexample below: a demonstration that the process in
  it is not Granger-noncausal from a to b relative to {a, b}, or that
  setting a(t) leaves the mean of b(t + 1) unchanged. Or a theorem that
  derives "no intervention effect" from Granger noncausality relative to a
  complete set of variables without any condition excluding influences
  faster than the sampling step. Disagreement about whether Granger
  noncausality ought to be called causal does not bear on it.
tags:
- causality
- mathematical-statistics
date: '2026-10-16'
line:
- formal-apparatus
grounds:
- THEORY-tmp4g68i
uses:
- TERM-tmpq0ms2
summary: >-
  The record's answer to [NOTE-010](../notes.d/NOTE-010.md)'s C5, "if all relevant variables are
  measured, Granger- and Pearl-type analyses coincide", which the ΦID
  review asserts without conditions. Eichler and Didelez ([THEORY-tmp4g68i](../theory.d/THEORY-tmp4g68i.md))
  give sufficient conditions, and complete measurement is one of them. A
  two-variable process with nothing hidden shows it is not enough: a acts
  on b within one step, a is Granger-noncausal for b, and setting a(t)
  changes the mean of b(t + 1) by ργ. Checked by hand and by simulation.
supports:
- CLAIM-tmpa4kr6
---

# CLAIM-tmp6nu4a: Measuring every relevant variable is necessary but not sufficient for a Granger-causal analysis to say anything about interventions: the intervention must also be an isolated exogenous change and no influence may act within one sampling step, and then Granger noncausality implies no intervention effect and the effect is identified from the observational predictor, but a Granger-causal relation is still only potentially causal

## The claim

[NOTE-010](../notes.d/NOTE-010.md) records the ΦID review's C5, §IV A: if all relevant variables
are measured, Granger- and Pearl-type analyses coincide. It has no
citation and no conditions. The record holds instead:

1. **Necessary.** An unobserved relevant process can produce a
   Granger-causal relation. In Eichler and Didelez's Example 4.2 a latent
   Z adds α₁α₂/(1 + α₂²) to X2's one-step coefficient on X1, which the
   reading checked ([NOTE-tmpm48uq](../notes.d/NOTE-tmpm48uq.md)). That is why they need V to include
   every relevant process, observed or not ([THEORY-tmp4g68i](../theory.d/THEORY-tmp4g68i.md)).
2. **Not sufficient.** Their Assumption 2.3(i) also needs the
   intervention independent of the other variables at the same time,
   which excludes influences that act within one sampling step. Without
   it, the inference fails with nothing hidden (below).
3. **What the conditions buy.** A missing edge a → b means no effect on
   b at the next step. Non-ancestry means none at any horizon. The effect
   is identified from the observational predictor, with S = V always
   enough. A present edge is "potentially causal". So the two analyses
   agree on zero effects and share an estimand. They are still not one
   analysis.

## The counterexample

Take two series, nothing hidden: a(t) = ε_a(t) and
b(t) = ρ b(t − 1) + γ a(t) + ε_b(t), with independent white noises, |ρ| < 1
and γ ≠ 0.

- **a is strongly Granger-noncausal for b relative to {a, b}.**
  b(t + 1) = ρ b(t) + γ ε_a(t + 1) + ε_b(t + 1), and ε_a(t + 1) is
  independent of the whole past. So given b's past, a's past adds nothing.
- **Intervening on a(t) changes b(t + 1).** Setting a(t) = x gives
  b(t) = ρ b(t − 1) + γx + ε_b(t), so E b(t + 1) = ργx.
- **What fails.** Assumption 2.3(i): b(t) responds to the intervention on
  a(t). In the mixed graph a and b are joined by a dashed edge, not an
  arrow.

Checked by simulation on 2026-10-16 (ρ = 0.6, γ = 0.8, n = 2·10⁵). OLS of
b(t + 1) on b(t), b(t − 1), a(t), a(t − 1) gives coefficients 0.601,
−0.004, −0.004 and 0.004. The residual correlates 0.62 with a(t + 1),
which is the contemporaneous dependence. The intervention effect is
ργ = 0.48.

The process has zero full-history transfer entropy from a to b and
positive directed information, all of it in the instantaneous term
I(a(t); b(t) | past) ([THEORY-tmppkvwa](../theory.d/THEORY-tmppkvwa.md)). That term is what Granger causality and
transfer entropy leave out.

The example is a sampling problem, not a pathology. Any influence faster
than the sampling interval, or any aggregation over time, puts the
example's structure into the data.

## What it does not say

- That Granger analysis is useless for causal questions. Under the
  conditions it is how the effect is identified.
- That the conditions above are the only sufficient ones. Eichler and
  Didelez give sufficient conditions, and the front-door criterion
  identifies some effects with a confounder unobserved.
- That ΦID's quantities are interventional or not. That is [NOTE-010](../notes.d/NOTE-010.md)'s
  C4 and [THEORY-497](../theory.d/THEORY-497.md)'s footnote-3 condition, which this claim leaves
  standing.
