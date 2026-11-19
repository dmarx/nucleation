---
status: Proposed
title: 'Lohmiller and Slotine show that if the generalized Jacobian F = (Θ̇ + Θ ∂f/∂x)Θ⁻¹ of a smooth system ẋ = f(x, t) is uniformly negative definite in a region, with M = ΘᵀΘ uniformly positive definite, then any trajectory starting in an M-ball about a given trajectory and contained in that region converges to it exponentially, that conversely every exponentially convergent system is contracting in some metric, and that contraction is preserved under parallel, skew-symmetric feedback and hierarchical combination'
version: 1
source:
- LIT-tmprrdom
tags:
- control-theory
- mathematics
date: '2026-11-19'
promote_when: >-
  Theorem 2 and the hierarchical-combination argument of §3.8.3 are re-
  derived step by step from the virtual dynamics d/dt δz = F δz, and the
  converse construction of §3.5 (eq. 11) is checked, including the
  authors' handling of a metric that grows without bound.
summary: >-
  From the reading of [LIT-tmprrdom](../literature.d/LIT-tmprrdom.md) in [NOTE-tmp2wkbb](../notes.d/NOTE-tmp2wkbb.md). Lohmiller, Slotine
  (1998), Automatica 34(6), DOI 10.1016/S0005-1098(98)00019-3, read from
  the authors' final manuscript (NSL-961001, December 1997) on the MIT
  Nonlinear Systems Laboratory site. It founds contraction analysis. If
  the generalized Jacobian F = (Θ̇ + Θ ∂f/∂x)Θ⁻¹ is uniformly negative
  definite in a metric M = ΘᵀΘ, all trajectories in a ball inside the
  region converge exponentially to one another, so initial conditions are
  forgotten. Conversely, every exponentially convergent system is
  contracting in some metric, and contraction survives parallel, skew-
  symmetric feedback and hierarchical combination, the last offered as a
  common frame for singular perturbations. Here because A29 grounded
  selective contraction in it; it is not the source of partial contraction
  toward invariant manifolds (that is Wang and Slotine 2005, not held),
  only of two remarks on convergence on a subspace. [THEORY-773](THEORY-773.md)'s
  disturbance lemma rests on its eq. (15). Read in its NOTE.
---

# THEORY-tmprpscg: Lohmiller and Slotine show that if the generalized Jacobian F = (Θ̇ + Θ ∂f/∂x)Θ⁻¹ of a smooth system ẋ = f(x, t) is uniformly negative definite in a region, with M = ΘᵀΘ uniformly positive definite, then any trajectory starting in an M-ball about a given trajectory and contained in that region converges to it exponentially, that conversely every exponentially convergent system is contracting in some metric, and that contraction is preserved under parallel, skew-symmetric feedback and hierarchical combination

## The account

Write the virtual dynamics of ẋ = f(x, t) in differential coordinates δz = Θ(x, t)δx as d/dt δz = Fδz with F = (Θ̇ + Θ ∂f/∂x)Θ⁻¹. Then d/dt(δzᵀδz) = 2δzᵀFδz, so F ≤ −βI gives exponential decay of every virtual displacement and, by path integration, of the distance between any two trajectories in a ball contained in the region (Theorem 2). An exponentially convergent system is contracting in the metric solving Ṁ = −βM − M∂f/∂x − (∂f/∂x)ᵀM, M(0) = kI (§3.5). A hierarchical system with contracting diagonal blocks and bounded coupling converges to a single trajectory, a disturbance d keeps trajectories within a ball of radius set by Ṙ + |λmax|R ≤ ‖Θd‖, and the analogous discrete-time condition is FᵢᵀFᵢ − I ≤ −βI.

## What it does not show

The paper proves convergence of all trajectories to one, not to a manifold. Partial contraction, contraction toward an invariant subspace or manifold that keeps distinctions transverse to it, is not developed here: §3.9 states two remarks in that direction without theorems, and the theory was developed later (Wang and Slotine 2005, not held). Nothing is stochastic.
