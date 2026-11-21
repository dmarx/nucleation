---
number: 828
status: Proposed
formerly:
- CLAIM-tmpl9zw4
title: 'When a fine feature''s factored contribution is gated by a parent feature, ŷ = g·abφ, the child switches on only when gs > λ, so acquisition follows a partial order of dependencies rather than a fixed coarse-to-fine chronology; and the time a feature becomes unstable, the time it becomes visible and the time its information was first encoded can all differ'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the gated model's derivation: a child's equilibrium output
  other than (s − λ/g)₊, an activation condition other than gs > λ, or a
  delay after the stability crossing that does not grow with the
  log-ratio of detection to starting amplitude. For the reading as a
  partial order, a construction in which the gates are given and the
  activation order nonetheless violates the dependencies, a child
  switching on while its gate is below λ/s. Findings that real networks
  learn fine distinctions before coarse ones do not defeat it; the claim
  allows that order when a fine signal is strong.
tags:
- learning-theory
- representation-learning
date: '2026-11-21'
line:
- learned-structure
rests_on:
- CLAIM-807
grounds:
- THEORY-283
- THEORY-740
- LIT-3001
bears_on:
- QUESTION-217
- QUESTION-363
- QUESTION-514
- QUESTION-511
summary: >-
  A43 §§10–13 and 15 of the exchange "Rich Get Richer Power Laws"
  (2026-11-21), the continuation the owner asked for at U27: a parent gate
  that makes a child feature's threshold depend on what has been learned,
  a delayed bifurcation, and the split of a feature's onset into
  "t_encoded", "t_stable" and "t_behavioral". Checked by the assistant, who
  corrects the delay formula, which leaves out the decay before the
  crossing, and makes the step from the optimum's derivative to an
  influence function that A left implicit. The wording is A's (the other
  assistant in the exchange "Rich Get Richer Power Laws", A43); adopting
  it is the owner's call.
---

<!-- inactive-ok-file: CLAIM-807 LIT-3001 — Proposed, filed with this claim, or a Deferred work registered from the exchange and not yet read -->

# CLAIM-828: When a fine feature's factored contribution is gated by a parent feature, ŷ = g·abφ, the child switches on only when gs > λ, so acquisition follows a partial order of dependencies rather than a fixed coarse-to-fine chronology; and the time a feature becomes unstable, the time it becomes visible and the time its information was first encoded can all differ

## The claim

**The gated child (A43 §10).** L(a, b; g) = ½(gab − s)² + (λ/2)(a² + b²),
with g ≥ 0 the strength of a parent feature, treated as slowly varying.
At the origin the Hessian has eigenvalues λ ± gs. Per coordinate on
a = b = x, ẋ = (gs − λ)x − g²x³. The child is active when g > λ/s, with
output gab = s − λ/g. Checked: at g = 1.5, s = λ = 1, direct minimization
gives gab = 0.3333 = s − λ/g. "The fine distinction's statistical signal
can be present throughout training, yet the computational structure
needed to exploit it may not become stable until a more general feature
reaches sufficient strength." It extends [CLAIM-807](CLAIM-807.md) by making the
threshold depend on what has been learned, which supplies the drift that
claim lacked.

**A partial order, not a chronology (A43 §11).** With
t_c* = inf{t : g_c(t)s_c > λ_c}, the order of activation follows the gates'
dependencies, but "a strong fine-grained signal may cross its threshold
unusually early", so "the structural prediction is more accurately a
partial order of dependencies than a universal coarse-to-fine chronology".
The record's [THEORY-283](../theory.d/THEORY-283.md) has features recovered at sample counts set by
their weights, and [THEORY-740](../theory.d/THEORY-740.md) has modes learned at times set by their
strengths. Both are orders by signal strength. This adds an order by
dependency.

**Three times (A43 §§12–13).** "t_encoded" (the information is available
in the representation), "t_stable" (a mechanism to use it becomes
dynamically stable) and "t_behavioral" (the capability is measurably
expressed). The gated model separates the last two by delayed growth.
The small-eigenvalue findings suggest the first can precede both. A
calls this the difference between "information acquisition" and
"information activation".

## Corrections and additions by the assistant

**The delay formula leaves out the memory of the stable phase.** A43 §12
takes μ(t) ≈ α(t − t*) and gives t_det − t* ≈ √((2/α) ln(x_det/x₀)), using x₀
as the amplitude at t*. A feature present from t₀ < t* first decays while
μ < 0, by exp[−α(t* − t₀)²/2], and must regrow that much. The exact
linear-regime delay is

  t_det − t* = √((2/α) ln(x_det/x₀) + (t* − t₀)²).

With α = 1, x₀ = 10⁻³ and x_det = 0.1, it is 3.04 when t₀ = t* (A's case),
3.64 when t₀ = t* − 2 and 5.85 when t₀ = t* − 5 (`t5/check2.py`). This is
the standard delay of a slow passage through a bifurcation. Noise
bounds it in practice by resetting the amplitude to the noise floor. So
A's formula understates the gap between t_stable and t_behavioral for a
feature that sat below threshold for a while, which is the case the
claim is about.

**From the optimum's derivative to influence.** A43 §15 notes that
∂q*/∂s jumps from 0 to 1 at activation, and links it to Lee et al.'s
finding that training-data influence changes sign and peaks at stage
transitions ([LIT-3001](../literature.d/LIT-3001.md), unread). The ledger notes that the step from
the derivative to a per-example influence is not made. In this model it
is short. With φ(x) = ±1, the empirical loss depends on the data only
through ŝ = (1/n)Σ y_iφ(x_i). Up-weighting example i by δ moves ŝ by
δ(y_iφ(x_i) − ŝ)/n. Its first-order influence on q* is therefore
(∂q*/∂s)(y_iφ(x_i) − ŝ)/n. That is zero for every example below the
gate's threshold and proportional to its residual above it. The step in
∂q*/∂s is a step in every example's influence. Whether the influence
dynamics Lee et al. report in transformers have this source is not
shown.

## What it does not say

That networks are built from such gates, or that the parent's own
dynamics leave the child's threshold where the exogenous-g model puts it.
The coupled dynamics of g are not given (the ledger's gap at A43; left
open here). The strata-to-semantics correspondence the exchange hopes the
gates realize is [QUESTION-514](../questions.d/QUESTION-514.md).
