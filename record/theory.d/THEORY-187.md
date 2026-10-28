---
number: 187
status: Active
formerly:
- THEORY-tmp8wj5h
title: 'In a deep linear network trained by gradient descent on whitened inputs from decoupled, balanced initial weights, depth slows learning through the initial end-to-end strength of each mode: counting iterations as learning time over the stable step size, from strength of order one the number of iterations stays bounded as depth grows, once the step size falls with depth as stability requires, while from small strength ε the plateau lengthens from ln(1/ε) with one hidden layer towards 1/ε at great depth'
version: 3
history:
- version: 2
  date: '2026-10-19'
  note: >-
    Narrowed and promoted from Proposed to Active at the owner's direction,
    carrying out the promotion audit's decision for THEORY-187 (batch 027,
    ADR-047). The title stated the depth law for any deep linear network; it
    now names the start the exact theory covers, whitened inputs and
    decoupled, balanced initial weights, and how iterations are counted. The
    mode equations, the finite-depth plateau exponent (N_l − 3)/(N_l − 1) that
    NOTE-667 did not check, the stable step size and the iteration count are
    re-derived in the note of 2026-10-19 below (ADR-047 v2). The promote_when
    asked about starts off the decoupled set, which the body disclaims. It
    moves, unchanged, to QUESTION-166.
- version: 3
  date: '2026-10-20'
  note: >-
    The narrowing-loss sweep (batch 066, ADR-047 v4) filed
    THEORY-792 as a Proposed THEORY that extends this one, to carry
    what the narrowing dropped: the depth law from generic starts, such
    as random orthogonal weights, which the paper argues from
    simulation. This entry's status and title are unchanged.
tags:
- learning-theory
date: '2026-10-09'
source:
- LIT-864
summary: >-
  Saxe, McClelland and Ganguli (2014), [LIT-864](../literature.d/LIT-864.md), Eqs. 13–17 and
  Appendix B: exact for decoupled initial weights and whitened inputs, with
  the step size bounded by the Hessian at the optimum, and supported on
  MNIST from decoupled starts up to 100 layers. It does not show that
  random orthogonal initialisation is such a start. The paper's account of
  that, isometry of the product of layers, is argued and simulated, not
  derived. It says nothing about nonlinear networks' learning time, and it
  is not advice on how to initialise.
supports:
- CLAIM-360
extended_by:
- THEORY-792
bears_on:
- QUESTION-039
---
<!-- inactive-ok-file: THEORY-792 — Proposed; the wider claim this account was narrowed from, which extends it and is cited as open -->
<!-- inactive-ok-file: THEORY-186 THEORY-182 THEORY-039 — Proposed; accounts this one is set beside -->

# THEORY-187: In a deep linear network trained by gradient descent on whitened inputs from decoupled, balanced initial weights, depth slows learning through the initial end-to-end strength of each mode: counting iterations as learning time over the stable step size, from strength of order one the number of iterations stays bounded as depth grows, once the step size falls with depth as stability requires, while from small strength ε the plateau lengthens from ln(1/ε) with one hidden layer towards 1/ε at great depth

## Source

Saxe, McClelland and Ganguli (2014), [LIT-864](../literature.d/LIT-864.md), §2, §3 and
Supplementary Appendices B–B.1, as read in [NOTE-667](../notes.d/NOTE-667.md).

## What was actually shown

Take a linear network with N_l layers, whitened inputs and squared error.
Start its weights on the decoupled set, where each layer's singular vectors
chain into the next and the first and last match the SVD of the
input–output correlation. Then each singular mode evolves alone, as N_l − 1
scalars aᵢ descending (1/2τ)(s − Πaᵢ)². The differences aᵢ² − aⱼ² are
conserved, and from equal starts the end-to-end strength u = Πaᵢ obeys
τu̇ = (N_l − 1)u^{2−2/(N_l−1)}(s − u). This is exact.

Two consequences follow.

- **Small start.** With one hidden layer, learning from u = ε takes about
  (τ/s)ln(s/ε). As depth grows the factor u^{2−2/(N_l−1)} starves growth
  near zero. Integrating the equation gives a plateau of order
  ε^{−(N_l−3)/(N_l−1)}, and the paper's infinite-depth solution, Eq. 17,
  has an s/ε term. The exponent at finite depth is my integration; the
  paper states only the end cases.
- **Large start.** Depth also raises the curvature. The top Hessian
  eigenvalue at the optimum is (N_l − 1)s^{(2N_l−4)/(N_l−1)}/τ, so the stable
  step size falls as 1/(N_l s²). Measured at that step size, the iterations
  an infinitely deep network needs exceed a three-layer network's by about
  cs/ε, which is finite (Appendix B.1). When the initial strength is of
  order one, depth costs a bounded number of iterations.

The experiment that could have come out otherwise is Fig. 4. Deep linear
networks on MNIST, 3 to 100 layers with width 1000, start on the decoupled
set at u₀ = 0.001, and each depth gets the best of twenty step sizes. The
iterations to a fixed training error saturate with depth, and the best step
sizes fall as 1/N_l, as predicted.

The paper then argues that the same holds from random starts whose product
of layers is close to an isometry. Gaussian layers scaled to preserve norm
on average have a product whose singular values become heavy-tailed with
depth, as computed numerically. Orthogonal layers have an exactly
orthogonal product. On MNIST, learning time grows with depth from the
first and not from the second, nor from pretraining (Fig. 6A).

## What this does not say

- **Not that random orthogonal weights are a decoupled start.** They are
  not aligned with the task's singular vectors, so the exact theory does
  not reach them. Their depth-independence is one MNIST experiment, and
  the explanation by dynamical isometry is an argument with no derivation
  of learning time from the Jacobian spectrum.
- **Not that the stepwise, strongest-first schedule survives a start of
  order one.** That schedule is the small-start corner ([THEORY-186](THEORY-186.md)). From a
  near-isometric start the modes are already of order one, and the paper
  does not describe the order in which the residual is learned.
- **Not that deep networks learn faster.** Continuous-time learning time
  falls with depth at a fixed rate, which is an artefact. Counted at the
  stable step size, depth adds delay, bounded only when the start is
  strong. The count is in iterations, not computation.
- **Not about nonlinear networks' learning time.** The paper's nonlinear
  results concern signal propagation at initialisation (an order-to-chaos
  transition at gain 1 for orthogonal tanh networks). They do not show
  that learning time follows.
- **Not about correlated inputs** beyond input correlations that share the
  task's singular vectors (Appendix E, stated without being worked out).
- **Not an instruction.** That orthogonal initialisation or pretraining
  should be used is the paper's recommendation for practice. It belongs to
  the anthology, and is not what this account claims.

## Where it sits

[THEORY-186](THEORY-186.md) states the small-start, one-hidden-layer case, mode by mode in
order of strength. This account adds how depth and the initial scale set
the length of the plateaus. [THEORY-039](THEORY-039.md) holds plateaus and transitions as
one kind of training phase; here their length depends on the initial scale
in a way that changes with depth. [THEORY-182](THEORY-182.md)'s sigmoids are the
one-hidden-layer case for a symmetric factorisation.

## Note of 2026-10-13: the balanced-start condition, under gradient flow and SGD

This account is exact for decoupled, balanced initial weights. Two
readings filed on 2026-10-13 bear on that condition.

- **Under gradient flow, balance is kept.** The difference of squared
  norms between adjacent layers is conserved (Neural Mechanics, [LIT-1012](../literature.d/LIT-1012.md),
  Theorem 1). A balanced start stays balanced, which the exact solution
  relies on.
- **Under SGD, balance is approached.** Minibatch noise drives the
  difference toward balance ([THEORY-211](THEORY-211.md)). For a two-layer linear network,
  Ziyin et al. find uᵢ² = wᵢ² at stationarity, with probability 1.

So balance is less special under SGD than under gradient flow. But the
attraction acts over the long run, at stationarity. It does not supply
balance during the stage-like transitions this account describes, which
still need the balanced start, or something close to it.

## Note of 2026-10-19: the depth law re-derived for the decoupled start

Carried out for the promotion audit's batch 027 ([ADR-047](../decisions.d/ADR-047.md) v2). Let
m = N_l − 1 be the number of weight layers.

1. **Mode equations.** On the decoupled set with whitened inputs, a mode of
   strength s has loss (1/2τ)(s − u)², u = a₁⋯a_m. Gradient flow gives
   τȧᵢ = (s − u)∏_{j≠i}aⱼ, so d(aᵢ²)/dt = (2/τ)(s − u)u for every i. The
   differences aᵢ² − aⱼ² are conserved, a balanced start stays balanced,
   and with aᵢ = a, u = aᵐ: τu̇ = m u^{2−2/m}(s − u).
2. **Small start.** The time from u = ε to near s is
   (τ/m)∫ du/(u^{2−2/m}(s − u)). For m = 2 this is (τ/2s)ln(s/ε) + O(1).
   For m > 2 the integral is dominated near ε and is about
   (τ/m)ε^{−(m−2)/m}/((1 − 2/m)s). The exponent (m − 2)/m =
   (N_l − 3)/(N_l − 1) rises to 1, the 1/ε of Eq. 17, as depth grows.
3. **Stable step.** At the optimum the Hessian is (1/τ)∇u∇uᵀ with
   ∂u/∂aᵢ = s^{1−1/m}, so its top eigenvalue is m s^{2−2/m}/τ and the stable
   step is of order τ/(m s^{2−2/m}), about 1/(N_l s²) at depth.
4. **Iterations.** Time over that step is s^{2−2/m} times the integral in
   step 2. From an initial strength of order one the integral converges as
   m grows, so the count is bounded in depth. From ε it is about
   s^{1−2/m}ε^{−(m−2)/m}/(1 − 2/m), growing towards s/ε.

Each step uses the balanced, decoupled start. Off the decoupled set the
modes couple and step 1 fails, which is why the general case is
[QUESTION-166](../questions.d/QUESTION-166.md).

## Note of 2026-10-20: the wider claim filed separately

When this THEORY was narrowed to what its source showed, the wider claim
it had stated was left with nowhere to go but this body and a QUESTION.
Under [ADR-047](../decisions.d/ADR-047.md) v4 it is now its own Proposed THEORY, [THEORY-792](THEORY-792.md), which extends
this one: the depth law from generic starts, such as random orthogonal weights, which the paper argues from simulation. This entry is that THEORY's evidence and is not
changed by it.
