---
number: 828
status: Proposed
formerly:
- CLAIM-tmpl9zw4
title: 'When a fine feature''s factored contribution is gated by a parent feature, ŷ = g·abφ, the child switches on only when gs > λ, so acquisition follows a partial order of dependencies rather than a fixed coarse-to-fine chronology; and the time a feature becomes unstable, the time it becomes visible and the time its information was first encoded can all differ'
version: 2
history:
- version: 2
  date: '2026-11-22'
  note: >-
    After the reading of Lee, Smith, Adam and Hoogland (LIT-3001,
    NOTE-tmp1sot8): the sentence calling the work unread updated, the
    influence paragraph revised in place (the equilibrium derivative
    steps, the gradient-flow derivative peaks; the paper's peaks order by
    strength), LIT-3001 removed from the grounds (ARG-tmpe7mqz,
    Rejected), and dated notes added for Lee et al. and for Yang
    (LIT-2961). Title and thesis unchanged.
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

<!-- inactive-ok-file: CLAIM-807 — Proposed, filed with this claim -->
<!-- inactive-ok-file: THEORY-tmpm3ux2 THEORY-tmpu0f9k ARG-tmpe7mqz — Proposed or Rejected; the readings of Lee et al. and of Yang filed 2026-11-22, and the argument that takes Lee et al. out of the grounds -->

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
transitions ([LIT-3001](../literature.d/LIT-3001.md), read on 2026-11-22). The ledger notes that the step from
the derivative to a per-example influence is not made. In this model it
is short. With φ(x) = ±1, the empirical loss depends on the data only
through ŝ = (1/n)Σ y_iφ(x_i). Up-weighting example i by δ moves ŝ by
δ(y_iφ(x_i) − ŝ)/n. Its first-order influence on q* is therefore
(∂q*/∂s)(y_iφ(x_i) − ŝ)/n. That is zero for every example below the
gate's threshold and proportional to its residual above it. The step in
∂q*/∂s is a step in every example's influence, at equilibrium.

*Revised 2026-11-22, after reading Lee et al.:* that step belongs to the
equilibrium derivative. Under gradient flow the derivative peaks
instead. Lee et al.'s own analytic influence (C.6, Eq. 56) runs through
the time-dependent mode strength of [THEORY-740](../theory.d/THEORY-740.md),
g_t(s) = s e^(2st/τ)/(e^(2st/τ) − 1 + s/g₀). Checked with python3 -I at
s = 1, τ = 1, g₀ = 10⁻³: ∂g_t/∂s is 0 at the start, rises to a peak of
2.1345 at t ≈ 3.77, just after the mode reaches half strength
(t ≈ 3.45), and settles to 1. A larger s raises the endpoint and brings
the transition earlier, so the derivative overshoots mid-transition
(peak 1.633 at g₀ = 10⁻², 2.670 at 10⁻⁴). A gated child passing its
threshold under gradient flow would show the same transient on top of
the step. Lee et al.'s peaks order by signal strength: in Saxe's
hierarchy, animal against plant before mammal against bird, the order
[THEORY-740](../theory.d/THEORY-740.md) gives. This claim's ordering by dependency is untested by
their work ([ARG-tmpe7mqz](../arguments.d/ARG-tmpe7mqz.md)). Whether the influence dynamics they report
in transformers have either source is not shown.

## What it does not say

That networks are built from such gates, or that the parent's own
dynamics leave the child's threshold where the exogenous-g model puts it.
The coupled dynamics of g are not given (the ledger's gap at A43; left
open here). The strata-to-semantics correspondence the exchange hopes the
gates realize is [QUESTION-514](../questions.d/QUESTION-514.md).

## Note of 2026-11-22: Lee, Smith, Adam and Hoogland, read

Qualifies the influence step; leaves the thesis untested. Read
([NOTE-tmp1sot8](../notes.d/NOTE-tmp1sot8.md), [THEORY-tmpm3ux2](../theory.d/THEORY-tmpm3ux2.md)), the paper's model is not this one: no
gate and no weight decay, influence taken at a fixed training time
through the mode strength, plus basis-rotation terms with denominators
s_j² − s_i². Its Bayesian account puts a peak in a between-phase term
"maximized when the posterior mass is evenly split" (§2.3), and it names
the link from that account to SGD as its "primary theoretical gap" (§5).
Its influence peaks follow the hierarchy, "the time point of the
branching node matches the peaks in influence" (§3), but in Saxe's
model that order is by strength. The influence paragraph above is
revised accordingly, and [LIT-3001](../literature.d/LIT-3001.md) leaves the grounds ([ARG-tmpe7mqz](../arguments.d/ARG-tmpe7mqz.md),
Rejected). The claim's gating, partial order and three times stand on
its own derivation; the order by dependency awaits [LEAD-207](../leads.d/LEAD-207.md).

## Note of 2026-11-22: Yang, read

A parallel. Yang's probe ([THEORY-tmpu0f9k](../theory.d/THEORY-tmpu0f9k.md), [NOTE-tmpg5q4t](../notes.d/NOTE-tmpg5q4t.md)) has a
secondary threshold βc⁽²⁾ = 1/λmax(Σwithin) inside each supercluster, so
a child split comes only after its parent's: a gating of the same kind,
on a detached probe, ordered by covariance. The paper leaves
"verification at the secondary scale" to future work. No edge.
