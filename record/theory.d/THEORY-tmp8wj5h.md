---
status: Proposed
promote_when: >-
  A derivation, or a controlled measurement across depths, showing that
  deep linear networks started off the decoupled set behave the same way:
  learning time, counted in iterations at the stable step size, bounded in
  depth when the initial end-to-end gain on every mode is of order one,
  and growing as a power of 1/ε when it is ε. That means random orthogonal
  or random small weights, not aligned with the task's singular vectors.
  More runs from decoupled starts cannot settle it, since there the result
  is already exact.
title: 'In a deep linear network trained by gradient descent, depth slows learning through the initial end-to-end strength of each mode: from strength of order one the number of iterations stays bounded as depth grows, once the step size falls with depth as stability requires, while from small strength ε the plateau lengthens from ln(1/ε) with one hidden layer towards 1/ε at great depth'
version: 1
tags:
- learning-theory
date: '2026-10-09'
source:
- LIT-tmppqrls
summary: >-
  Saxe, McClelland and Ganguli (2014), [LIT-tmppqrls](../literature.d/LIT-tmppqrls.md), Eqs. 13–17 and
  Appendix B: exact for decoupled initial weights and whitened inputs, with
  the step size bounded by the Hessian at the optimum, and supported on
  MNIST from decoupled starts up to 100 layers. It does not show that
  random orthogonal initialisation is such a start. The paper's account of
  that, isometry of the product of layers, is argued and simulated, not
  derived. It says nothing about nonlinear networks' learning time, and it
  is not advice on how to initialise.
---
<!-- inactive-ok-file: THEORY-186 THEORY-182 THEORY-039 — Proposed; accounts this one is set beside -->

# THEORY-tmp8wj5h: In a deep linear network trained by gradient descent, depth slows learning through the initial end-to-end strength of each mode: from strength of order one the number of iterations stays bounded as depth grows, once the step size falls with depth as stability requires, while from small strength ε the plateau lengthens from ln(1/ε) with one hidden layer towards 1/ε at great depth

## Source

Saxe, McClelland and Ganguli (2014), [LIT-tmppqrls](../literature.d/LIT-tmppqrls.md), §2, §3 and
Supplementary Appendices B–B.1, as read in [NOTE-tmpb36i6](../notes.d/NOTE-tmpb36i6.md).

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
