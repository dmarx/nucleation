---
number: 807
status: Proposed
formerly:
- CLAIM-tmp9bp04
title: 'A factored feature under weight decay, ŷ = abφ, switches on at a sharp threshold: its strength is q* = (s − λ)₊, the origin loses stability through a pitchfork in the parameters at s = λ, relaxation there is algebraic and the local coefficient of the regularized loss dips from 1 to 3/4, and just above threshold the feature''s variance is of order ε² while its gain in fit is of order ε, so a newly active feature is quiet but consequential'
version: 2
history:
- version: 2
  date: '2026-11-22'
  note: >-
    After the reading of Yang (LIT-2961, NOTE-tmpg5q4t): the sentence
    calling the work unread updated, LIT-2961 removed from the grounds
    (ARG-tmp31laj, Rejected: a parallel, not evidence), and a dated note
    added. Title and thesis unchanged.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation for L(a, b) = ½(ab − s)² + (λ/2)(a² + b²): a
  minimizer with ab ≠ (s − λ)₊, Hessian eigenvalues at the origin other
  than λ ± s, a local loss at s = λ other than λv² + (u² − v²)²/8 in the
  normalized coordinates, or a gain in fit just above threshold not of
  order ε while the variance is of order ε². That the pitchfork is a
  symmetry of the parameters and not of the predictor does not defeat it;
  the claim says so.
tags:
- learning-theory
- loss-landscapes
- representation-learning
date: '2026-11-21'
line:
- learned-structure
rests_on:
- CLAIM-148
- CLAIM-811
grounds:
- THEORY-180
- THEORY-740
- THEORY-087
bears_on:
- QUESTION-511
- QUESTION-217
summary: >-
  A42 §§1–5 and its closing section of the exchange "Rich Get Richer Power
  Laws" (2026-11-21), continuing U25's line on small-eigenvalue subspaces:
  a minimal model of a feature's birth in which threshold, pitchfork,
  algebraic relaxation, a dip in the local coefficient and quiet-but-
  consequential growth all appear at s = λ. Every step checked by the
  assistant, who adds the caveat A's reasoning stated and the visible turn
  did not: the pitchfork is in the parameters, and the predictor only
  kinks. The wording is A's (the other assistant in the exchange "Rich
  Get Richer Power Laws", A42); adopting it is the owner's call.
---

<!-- inactive-ok-file: THEORY-180 CLAIM-828 — Proposed or new -->
<!-- inactive-ok-file: THEORY-tmpu0f9k ARG-tmp31laj THEORY-1429 — Proposed or Rejected; the reading of Yang filed 2026-11-22, the argument that takes it out of the grounds, and Kuehn's classification cited in the note -->
<!-- inactive-ok-file: THEORY-tmpg4aat — Proposed or Rejected; filed 2026-11-21 from the readings of Gutenkunst et al., Transtrum & Qiu, Amari, Park & Ozeki and Wei et al. -->

# CLAIM-807: A factored feature under weight decay, ŷ = abφ, switches on at a sharp threshold: its strength is q* = (s − λ)₊, the origin loses stability through a pitchfork in the parameters at s = λ, relaxation there is algebraic and the local coefficient of the regularized loss dips from 1 to 3/4, and just above threshold the feature's variance is of order ε² while its gain in fit is of order ε, so a newly active feature is quiet but consequential

## The claim

A42 §1: a fine feature φ with E[φ²] = 1, a target sφ, and a learned
contribution abφ under weight decay:

  L(a, b) = ½(ab − s)² + (λ/2)(a² + b²).

Each step below was checked by the assistant with `python3 -I`
(`t5/check2.py`).

- **Threshold.** For fixed q = ab ≥ 0, a² + b² ≥ 2q, so
  L_min(q) = ½(q − s)² + λq and q* = (s − λ)₊. Direct minimization gives
  q* = 0.0000, 0.5000, 1.0000 at s = 0.5, 1.5, 2.0 (λ = 1). This is the
  scalar case of what the record holds for factorizations: weight decay
  narrows a factorization's gauge ([CLAIM-148](CLAIM-148.md)), and acts as a nuclear-norm
  penalty that soft-thresholds a learned map ([THEORY-180](../theory.d/THEORY-180.md)).
- **Pitchfork.** At a = b = 0 the Hessian is [[λ, −s], [−s, λ]], with
  eigenvalues λ ± s. One goes soft at s = λ, and for s > λ minima appear
  at a = b = ±√(s − λ). Per coordinate on a = b = x, gradient flow is
  ẋ = (s − λ)x − x³, the pitchfork normal form (−∂L/∂a = 0.063 against
  0.063 at x = 0.3, s = 1.3).
- **Algebraic relaxation at threshold.** At μ = s − λ = 0, ẋ = −x³ gives
  x₀/√(1 + 2x₀²t) ∝ t^(−1/2) (0.07053 against 0.07053 at t = 100). For small
  μ > 0, growth from x₀ takes about (1/μ) ln(1/x₀): a plateau. A's two
  caveats stand. A start at exactly 0 never leaves. And with s and λ
  fixed, training does not cross the threshold unless something drifts
  ([CLAIM-828](CLAIM-828.md) supplies the drift).
- **The local coefficient dips.** With u = (a + b)/√2, v = (a − b)/√2, at
  s = λ, L − L_min = λv² + (u² − v²)²/8 exactly (agreeing to six digits at
  three random points), ≍ v² + u⁴, so the local Gibbs integral scales as
  n^(−3/4). On either side the minima are isolated and nondegenerate, so
  n^(−1). The coefficient goes 1 → 3/4 → 1 across the threshold.
- **Quiet but consequential.** At s = λ + ε, q* = ε. The feature's output
  variance is ε², while the fit improves by sε − ε²/2 = λε + ε²/2. Gain
  per unit of variance grows as λ/ε (1,000 at ε = 10⁻³, λ = 1). A
  feature just switched on is a small-variance direction that matters.
  "A feature may be small because it is unimportant. Or it may be small
  because its corresponding computational mechanism is only beginning to
  differentiate" (A42, closing), and stability analysis, not the
  covariance spectrum, tells the two apart.

## Caveats the assistant adds

- **The pitchfork is a symmetry of the parameters, not of the predictor.**
  The two branches a = b = ±√(s − λ) give the same product, the same
  predictor. What the predictor does at s = λ is a kink: q* is continuous
  and its derivative jumps from 0 to 1. A's reasoning, not shown on the
  share page, said as much ("the two factorized branches represent the
  same predictor, so the pitchfork partly reflects parameter symmetry.
  The observable feature activation has a threshold-like kink, not
  necessarily a physical phase transition"). The visible turn calls it "a
  genuine change in dynamical stability", which is true of the
  parameters, and a "symmetry-breaking bifurcation", which overstates
  what the predictor does.
- **The dip is not Watanabe's learning coefficient.** It is the scaling of
  a Gibbs integral of a regularized loss, with n multiplying the weight
  decay. A42 says so: "A Bayesian RLCT requires specifying the likelihood,
  prior, and how regularization scales with sample size." With λ fixed
  as n grows, the regularizer is not a prior.
- **A42's text is complete.** The owner's U27 said A42 was "cut off
  midthought". The share's data hold A42 as one message merged from two
  fragments (6,549 and 17,222 characters, together 23,771), written at
  16:44:09 and 16:44:59 UTC with a web search between them. The first
  fragment ends at §2. The merged message
  ends with a normal stop. The owner probably saw only the first
  fragment; nothing of the visible turn was lost. What the reasoning
  planned and neither fragment states is the parameter-symmetry caveat
  above and a list of limitations. A43 continued at §10.

## Related work

A42 cites the "Feature Lottery" preprint ([LIT-2961](../literature.d/LIT-2961.md), read on 2026-11-22; see the note
below) for a
pitchfork account of concept emergence in a Gaussian-mixture probe
framework, and Wang et al.'s refined coefficients ([THEORY-975](../theory.d/THEORY-975.md)). The record
holds the pitchfork normal form in another domain ([CLAIM-408](CLAIM-408.md)) and the
plateau-time law without weight decay ([THEORY-740](../theory.d/THEORY-740.md)).

## Note of 2026-11-21: Wei et al. (2008), read

A contrast. This claim has an algebraic relaxation at a threshold. Wei
and colleagues' plateaus near overlap singularities have none: the paper
derives orbits, not time courses, and its long plateau is a noise-driven
walk along a line of equivalent models ([NOTE-tmpl89m0](../notes.d/NOTE-tmpl89m0.md), [THEORY-tmpg4aat](../theory.d/THEORY-tmpg4aat.md)).
The two mechanisms of slow learning near a singular set are different
and the claim does not depend on theirs.

## Note of 2026-11-22: Yang, read

A parallel, and a second instance of this claim's caveat; nothing on the
local coefficient. Yang's probe (THEORY-tmpu0f9k, NOTE-tmpg5q4t) loses
its collapsed state through a supercritical pitchfork with the same
normal form, ε̇ = (β − βc)ε − αε³, and growth from the noise "on a
characteristic timescale that scales as 1/(β − βc)", which is this
claim's plateau of order (1/μ) ln(1/x₀). The symmetry it breaks is also
one of the parameters: which prototype takes which direction is "any
anti-symmetric w", not fixed by the linear analysis, just as the sign of
a = b is not fixed here. So the caveat that the pitchfork is in the
parameters, not the predictor, holds there too.

It does not ground the claim (ARG-tmp31laj, Rejected; LIT-2961 leaves the
grounds). Its bifurcation parameter is a detached probe's precision, not
a signal against weight decay; the paper says nothing of learning
coefficients, so the dip from 1 to 3/4 has no counterpart there; and its
weight decay plays this claim's "something drifts" role only loosely,
setting the escape time after a crossing that comes at steps 34–60 with
or without it. By Kuehn's classification (THEORY-1429) neither pitchfork
is a critical transition: both are supercritical, with no fast jump.
