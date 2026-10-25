---
number: 954
status: Active
formerly:
- THEORY-tmpg6jfa
title: 'When the information a design yields depends on the unknown parameter, as in nonlinear models or nonlinear functions of linear ones, Bayesian design criteria are normal approximations to expected utility that average a local criterion over the prior, such as the expected log det of the Fisher information, and locally optimal design is the special case of a point-mass prior; a locally optimal design can leave the quantity of interest inestimable, as for the turning point of a quadratic regression on [−1, 1] with best guess ½, where the locally c-optimal design puts half its mass at 0 and half at 1 and identifies only θ₁ + θ₂'
version: 1
history:
- version: 1
  date: '2026-10-25'
  note: >-
    Filed Active from NOTE-1161. The criteria are Chaloner and
    Verdinelli's (15), (18) and (20) and their §4.4 on local optimality.
    The turning-point example is their §7.2. The example's optimality,
    which the review asserts as "straightforward to show", and its
    consequence are re-derived below by Elfving's theorem, which meets
    the condition for Active under ADR-047 v2. The application to
    CASE-159 is the record's.
tags:
- mathematical-statistics
- probabilistic-modeling
date: '2026-10-25'
source:
- LIT-1525
summary: >-
  Chaloner and Verdinelli (1995), [LIT-1525](../literature.d/LIT-1525.md), read in [NOTE-1161](../notes.d/NOTE-1161.md).
  Once the information depends on θ, no design is optimal without saying
  which θ it is optimal for, and the prior is how that is said. The
  approximations' accuracy is "not much known" in general. The claim that
  optimal Bayesian designs gain support points as the prior disperses rests
  on examples, not a theorem, and is not part of this account.
supports:
- CLAIM-452
---
# THEORY-954: When the information a design yields depends on the unknown parameter, as in nonlinear models or nonlinear functions of linear ones, Bayesian design criteria are normal approximations to expected utility that average a local criterion over the prior, such as the expected log det of the Fisher information, and locally optimal design is the special case of a point-mass prior; a locally optimal design can leave the quantity of interest inestimable, as for the turning point of a quadratic regression on [−1, 1] with best guess ½, where the locally c-optimal design puts half its mass at 0 and half at 1 and identifies only θ₁ + θ₂

## Source

Chaloner and Verdinelli (1995), [LIT-1525](../literature.d/LIT-1525.md), §4.2 (approximations),
§4.4 (local optimality), §5.1 (equivalence theorem) and §7.2 (turning
point). Read in [NOTE-1161](../notes.d/NOTE-1161.md). The Elfving argument below is the record's.

## What was actually shown

**The approximation (§4.2).** With the posterior approximated by
N(θ̂, [nI(θ̂, η)]⁻¹), and the predictive distribution of θ̂ by the prior,
expected Shannon information is −(k/2)log(2π) − k/2 + ½∫ log det{nI(θ, η)}
p(θ) dθ. That gives the criterion φ₁(η) = ∫ log det{nI(θ, η)} p(θ) dθ.
Squared-error loss for g(θ), with gradient c(θ), gives
φ₂(η) = −∫ c(θ)ᵀ{nI(θ, η)}⁻¹c(θ) p(θ) dθ. These are averages of local
criteria. With p a point mass at θ₀ they become Chernoff's locally optimal
criteria det I(θ₀, η) and −c(θ₀)ᵀI(θ₀, η)⁻¹c(θ₀) (§4.4). Each is concave
on the space of design measures, so the equivalence theorem certifies a
global optimum by directional derivatives toward one-point designs (§5.1).

**The turning point (§7.2), re-derived.** E[y | x] = θ₀ + θ₁x + θ₂x² on
x ∈ [−1, 1], with f(x) = (1, x, x²). The turning point is
g(θ) = −θ₁/(2θ₂), so ∇g = (0, −1/(2θ₂), θ₁/(2θ₂²)). At a best guess with
g = ½, θ₁ = −θ₂, so ∇g = −(1/(2θ₂))(0, 1, 1). The local criterion is
c-optimality for c = (0, 1, 1).

- *The design.* Put mass ½ at x = 1 and ½ at x = 0. Then
  ½·f(1) − ½·f(0) = (0, ½, ½) = c/2.
- *Its optimality, by Elfving.* A design is c-optimal iff c/ρ is on the
  boundary of the convex hull of {±f(x)} and is reached by its support
  points with signs. Take h = (−1, 0, 2). Then hᵀf(x) = 2x² − 1 ∈ [−1, 1] on
  [−1, 1], so the hyperplane hᵀz = 1 supports the hull. And hᵀ(c/2) = 1,
  with hᵀf(1) = 1 and hᵀ(−f(0)) = 1, so c/2 lies on the face reached by
  +f(1) and −f(0). The design is c-optimal, with ρ = 2 and asymptotic
  variance 4σ²/n for cᵀθ. The only other point where |2x² − 1| = 1 is
  x = −1. Writing c/2 as a combination of +f(1), +f(−1) and −f(0) forces
  the weight on f(−1) to zero, so the optimal design is unique.
- *What it estimates.* M(η) = ½f(0)f(0)ᵀ + ½f(1)f(1)ᵀ has rank 2, with range
  spanned by (1, 0, 0) and (1, 1, 1). Only θ₀ and θ₀ + θ₁ + θ₂ are
  identified, so θ₁ + θ₂ is too. That is enough for the linear function
  cᵀθ but not for the turning point −θ₁/(2θ₂), which needs θ₁ and θ₂
  separately. As the review says, "it is clearly impossible to fit a
  quadratic regression to two data points and estimate the turning point."

What could have failed: the locally optimal design for a nonlinear function
might have been estimable whenever its linearization is, as in linear
c-optimality, where cᵀθ "is always estimable". The example shows that the
linearization at the guess can be estimable while the function is not.

## What this does not say

- **Not that Bayesian designs always avoid the failure.** A prior spread
  over θ moves the c(θ) being averaged and so tends to add support points.
  The review shows this in examples (Chaloner and Larntz) and says "It is
  unclear, however, under what circumstances this is so."
- **Not how good the approximations are.** "Not much is known in general
  about how well these criteria ... perform empirically." Simulations are
  cited for special cases only.
- **Not anything about sequential design** beyond the review's argument
  that nonlinear problems should gain from it (§5.5).

## Connections

- **[CASE-159](../cases.d/CASE-159.md).** The mixture response p_π = Σ πᵢpᵢ is linear in π, but
  its Fisher information is not constant: I_rare(π) = 0.64/(p(1 − p)) with
  p = 0.1 + 0.8π. So designing probes for authority shares is a nonlinear
  design problem in this sense. A design must be judged at a guess of π or
  averaged over a prior on it. In the two-specialist case the choice does
  not depend on π, because the routine context carries zero information at
  every π. With more processes it does, and the equivalence theorem
  certifies the optimum ([NOTE-1161](../notes.d/NOTE-1161.md) computes one).
- **[QUESTION-031](../questions.d/QUESTION-031.md).** A criterion averaged over a prior answers "which
  probes, given what we expect", not "which probes separate". The turning
  point example is a case where the best probes for a linearized question
  fail the real one.
- **[THEORY-956](THEORY-956.md)** is the linear case, where none of this arises.
