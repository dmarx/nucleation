---
number: 1454
status: Proposed
formerly:
- CLAIM-tmpyk6bi
title: 'Linear coupling leaves support no role in interest'
statement: >-
  In the coupled competence–valuation model ċ = αv(1 − c) − μc, v̇ =
  βc(1 − v) − νv + s(t), whether an interest outlasts temporary support
  does not depend on the support: when αβ > μν every trajectory with any
  positive competence or valuation goes to the one positive equilibrium
  c* = (αβ − μν)/(β(α + μ)), v* = (αβ − μν)/(α(β + ν)), however small the
  seed, and when αβ ≤ μν every trajectory returns to zero, however large
  or long the support; support changes only timing; a coupling that is
  weak at low competence, βc²(1 − v)/(K² + c²) for instance, gives zero
  and a positive state both stable, with a threshold support must carry
  the state past, which is CLAIM-1310's seed threshold in two variables
version: 1
role: counter
warrant: demonstrated
defeated_if: >-
  An error in the derivation or the runs: parameters with αβ > μν and an
  initial state in the closed unit square other than the origin from which
  the unsupported model does not reach (c*, v*); parameters with αβ ≤ μν
  from which some finite support leaves a positive state after it ends;
  or, for the sigmoidal variant at the stated parameters, a run in which
  the outcome does not depend on whether the support exceeds the
  threshold.
tags:
- motivation
- complex-systems
- learning-and-conditioning
date: '2026-11-26'
line:
- transient-support
- will-organization
rests_on:
- CLAIM-1310
grounds:
- CASE-430
objects_to:
- CLAIM-1352
summary: >-
  A gap fill ([ADR-137](../decisions.d/ADR-137.md)) for A21 §5 of the exchange "Alignment consequences
  brainstorm" (ChatGPT, 2026-11-26), a model's reading checked (step 9a):
  the numbers are right, the instability condition αβ > μν and A21's own
  remark that it is "a coupling threshold, not a finite-amplitude
  nucleation threshold", but the parameter s(t), read as "temporary
  external support, such as mentorship or encouragement", cannot do what
  the figure's slider and A21's "even after the external support is
  withdrawn" suggest: it never decides the outcome. So the model does not
  show "a simple mechanism through which an initially instrumental
  activity becomes motivationally self-maintaining" with support's help.
  A one-line change to the coupling gives a model in which it does.
  Checked with python3 -I. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-430 CLAIM-1352 — Proposed; filed, registered or cited in the filing of 2026-11-26 from the exchange "Alignment consequences brainstorm" -->

# CLAIM-1454: Linear coupling leaves support no role in interest

## The gap

A21 §5 ([CASE-430](../cases.d/CASE-430.md)) introduces s(t) as support and draws its figure with
a slider for "Temporary external support" beside one for
"Competence–valuation coupling", captioned "With these parameters,
reciprocal reinforcement supports a nonzero equilibrium even after the
external support is withdrawn". It then reads the linear stability
condition as "a simple mechanism through which an initially instrumental
activity becomes motivationally self-maintaining", and says "the
relationship to Nucleation's transient-support models is promising". The
transient-support line asks whether support can be withdrawn and leave a
self-maintaining process ([CLAIM-600](CLAIM-600.md)). The question for the model is
whether s does anything to that outcome.

## The derivation

On the unit square, with s = 0:

1. **Equilibria.** ċ = 0 gives c = αv/(αv + μ), v̇ = 0 gives v = βc/(βc + ν).
   Substituting, a nonzero solution satisfies αβc + μβc + μν = αβ, so
   c* = (αβ − μν)/(β(α + μ)) and v* = (αβ − μν)/(α(β + ν)), positive
   exactly when αβ > μν. There is at most one positive equilibrium.
2. **No coexistence.** The system is cooperative (∂ċ/∂v = α(1 − c) ≥ 0,
   ∂v̇/∂c = β(1 − v) ≥ 0) and its vector field is strictly sublinear
   (f(λx) ≥ λf(x) for 0 < λ < 1, since (1 − λc) ≥ (1 − c)). For such systems
   the origin and a unique positive equilibrium cannot both be
   attracting: when αβ > μν the origin is a saddle (its determinant μν − αβ is negative) and every
   nonzero trajectory goes to (c*, v*); when αβ ≤ μν the origin attracts
   the whole square. (This is the standard dichotomy for cooperative
   systems with concave nonlinearities.)
3. **So support decides nothing.** Support adds to v̇ while it lasts and
   leaves the state somewhere in the square when it ends. From there, by
   2, the outcome is fixed by αβ against μν alone: above, any seed, even
   one with no support at all, reaches the interest; below, no support
   leaves one. The slider for support changes how fast the curves rise,
   not whether they stay up. In [CLAIM-1310](CLAIM-1310.md)'s terms the first regime is
   "past a spinodal", where "no seed is needed".
4. **A coupling that gives support a role.** Let valuation grow only once
   competence is appreciable: v̇ = βc²(1 − v)/(K² + c²) − νv + s(t). Now the
   linearization at zero has no coupling term, the origin is stable for
   all parameters, and for a range of them a stable positive state
   coexists with it, separated by an unstable one. Support must carry the
   state past the unstable one; a brief strong pulse needs less total
   support than a long weak one, as in [CLAIM-1310](CLAIM-1310.md)'s fold.

**Check (python3 -I).** Euler steps of 0.01 to t = 400. 300 random
parameter sets on [0.05, 2], each under three support schedules
(amplitude 0.02 for time 1, 0.5 for 5, 1.0 for 20), from the origin:
with |αβ − μν| > 0.05 every run ended within 10⁻³ of the predicted state,
(c*, v*) or zero, whatever the schedule (largest error 1.1 × 10⁻⁵). At α =
β = 1, μ = ν = 0.5 both a support of 0.001 for time 1 and of 1 for time 30
end at (0.5, 0.5), the formula's value; at α = β = 0.4 both supports end
at zero. In the sigmoidal variant with α = 1, β = 2, μ = ν = 0.5, K = 0.5,
the positive equilibria are at c = 0.033 (unstable) and c = 0.582
(stable); the critical support amplitude is 0.0377 for duration 1 (total
0.0377), 0.0083 for duration 5 (total 0.0417) and 0.0032 for duration 20
(total 0.0645); 0.9 times the critical amplitude for duration 20 ends at
zero and 1.1 times ends at (0.582, 0.697).

## What follows

- A21's own correction, that the model has "a coupling threshold, not a
  finite-amplitude nucleation threshold", is right, and it has a
  consequence A21 does not draw: the parameter introduced as support has
  no part in the conclusion the model is offered for. The outcome is a
  property of the person and the activity (α, β, μ, ν), not of the help.
- So the model gives no counterpart to "Maintained situational interest |
  Externally supported organization" in A21's mapping ([CLAIM-1352](CLAIM-1352.md)), or
  to an interest that would not have formed without a mentor.
- The record's account of when support can be withdrawn needs the
  threshold of step 4: [CLAIM-600](CLAIM-600.md)'s "large enough to carry the supported
  party past any threshold that process has" is empty in the linear
  model, which has none.

## What it does not say

That the sigmoidal coupling is right for interests. It is one coupling
that gives the property the transient-support reading needs; which
holds is empirical, the dependence of valuation growth on competence at
low competence ([LEAD-285](../leads.d/LEAD-285.md)'s interest-development case).
