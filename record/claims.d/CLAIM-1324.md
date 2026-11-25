---
number: 1324
status: Active
formerly:
- CLAIM-tmpu5cap
title: 'In A11''s model of confirmation feedback, where an agent adds each observation''s log-likelihood ratio a·y to its log odds ℓ while ℓ tilts which observations it samples, q(y | ℓ) ∝ p(y)exp(κℓy), and never corrects for the tilt, the unbiased state is unstable for every κ > 0; the threshold κ > 2/3 shown with it comes from the illustration''s decay factor 0.92, and a decay λ puts the threshold at κ = λ/a'
version: 2
history:
- version: 2
  date: '2026-11-24'
  note: >-
    Active: an independent checker, who did not write it, reproduced every
    computation in it with its own code (2026-11-24). The owner left the
    promotion of verified entries to the assistant's discretion.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation: under the stated model with balanced evidence
  the expected increment of ℓ is not a·tanh(κℓ), or the slope of the
  expected map at ℓ = 0 is not 1 + aκ without decay and 1 − λ + aκ with it.
tags:
- probabilistic-modeling
- cognition
date: '2026-11-24'
line:
- formal-apparatus
- distributed-agency
complements:
- CLAIM-330
summary: >-
  The assistant's gap fill ([ADR-137](../decisions.d/ADR-137.md)) for A11 §6 of the exchange "Memes,
  Contracts, and Systemic Normativity" (2026-11-24). A11 states a sampling
  model of confirmation bias and illustrates it with a different update,
  x_{t+1} = 0.92x_t + 0.12 tanh(κx_t), whose symmetry "becomes unstable
  when κ exceeds 2/3". The derivation shows the threshold belongs to the
  illustration's decay, not to the model: an accumulator that does not
  correct for its own selection has no threshold, so a small lean is
  amplified at any coupling. That is [CLAIM-330](CLAIM-330.md)'s condition that each field
  be stable alone. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---

# CLAIM-1324: In A11's model of confirmation feedback, where an agent adds each observation's log-likelihood ratio a·y to its log odds ℓ while ℓ tilts which observations it samples, q(y | ℓ) ∝ p(y)exp(κℓy), and never corrects for the tilt, the unbiased state is unstable for every κ > 0; the threshold κ > 2/3 shown with it comes from the illustration's decay factor 0.92, and a decay λ puts the threshold at κ = λ/a

## What A11 says

A11 §6 takes binary observations y ∈ {−1, +1}, the Bayesian log-odds update
ℓ_{t+1} = ℓ_t + log p(y_t | H₁)/p(y_t | H₀), and supposes "the agent's existing
interpretation influences the probability that an observation enters its
available evidence", q(y | ℓ) ∝ p(y)exp(κℓy). "Even if subsequent inference
is internally consistent, failing to account for this selection can
generate a self-reinforcing bias." Its interactive figure, "with balanced
underlying evidence", runs instead x_{t+1} = 0.92x_t + 0.12 tanh(κx_t) and
says: "Symmetry becomes unstable when κ exceeds 2/3. This is a toy
construction, not a fitted psychological model."

## The derivation

Take balanced evidence, p(+1) = p(−1) = 1/2, and symmetric hypotheses, so
the log-likelihood ratio of y is a·y with a > 0. Under q,

q(+1 | ℓ) = e^{κℓ}/(e^{κℓ} + e^{−κℓ}), so E_q[y | ℓ] = tanh(κℓ),

and the expected update of an agent that does not correct for the tilt is
E[ℓ_{t+1} | ℓ_t] = ℓ_t + a·tanh(κℓ_t). Its slope at ℓ = 0 is 1 + aκ, above 1
for every κ > 0: the unbiased state is unstable at any coupling. Mixing in a
share f of untilted observations gives slope 1 + (1 − f)aκ, still above 1
for f < 1, since balanced untilted evidence has no expected drift.

What stabilizes the unbiased state is a pull back toward it: a decay of the
log odds, (1 − λ)ℓ_t + a·tanh(κℓ_t), with slope 1 − λ + aκ, unstable exactly
when κ > λ/a. A11's figure is this map with λ = 0.08 and a = 0.12, so its
threshold is 0.08/0.12 = 2/3. The dashed "independent evidence" curve in the
same figure, initial·0.92^t, decays for the same reason; an undecayed
accumulator on balanced evidence would not drift back.

An agent that does correct for the tilt adds the log of the ratio of the
two hypotheses' normalizers of q, a term that does not depend on y, and
removes the drift. That is A11's "failing to account for this selection".

## The check

`python3 -I`, 2026-11-24. The figure's map converges to 0 at κ = 0.60 and to
0.556 at κ = 0.70 from a start of 0.15, as the threshold 2/3 requires. With
no decay the expected map leaves 0 at κ = 0.05 and at κ = 0.20 (slopes 1.006
and 1.024). Simulated with noise, 2,000 runs of 400 steps from ℓ = 0.15
with a = 0.12: at κ = 0.2 the mean |ℓ| is 37.5, against 1.87 at κ = 0 (a
random walk, whose expected value is 1.91), and 62.5% of runs end on the
side of the initial lean.

## Bearing

[CLAIM-330](CLAIM-330.md) makes the coupling destabilize symmetry in its linearized model
"with each field stable alone", above a threshold. A11 calls its model "a
natural extension of [CLAIM-330](CLAIM-330.md), [CLAIM-340](CLAIM-340.md) and [CASE-123](../cases.d/CASE-123.md)". It is one only once
belief has its own restoring term, the decay; without it there is no
threshold, and the amplification of a small lean that A11 attributes to
nucleation happens at any coupling, with the side chosen partly by noise.

## What it does not say

Anything about people. Like A11's figure, it is a toy; it locates where the
threshold in the toy comes from.
