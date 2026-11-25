---
number: 2163
status: Proposed
formerly:
- THEORY-tmpbobud
title: 'Fisher singularities cause learning plateaus'
statement: >-
  Amari, Park and Ozeki show that in a multilayer perceptron or gaussian
  mixture the Fisher information degenerates on a continuum of finite
  parameter values, where a unit vanishes or two units coincide, which the
  map to distributions collapses to a cone-type singular point; and that
  near it ordinary gradient learning has fast and slow manifolds, so the
  state is drawn quickly towards the singular set and then moves slowly
  along it, the plateau, even when the truth is regular, while natural
  gradient is repelled from it
promote_when: >-
  The record rederives the Fisher rank loss on vw = 0 for one hidden unit
  and the cone model's split (ξ̇ of order 1 and θ̇ of order ξ under
  gradient, θ̇ of order 1/ξ under natural gradient, from G = diag(1 + c²,
  c²ξ²)), and a simulation of the cone model or the one-unit perceptron
  from a regular truth reproduces a plateau in the gradient loss curve and
  none in the natural-gradient one.
version: 1
tags:
- learning-theory
- loss-landscapes
- information-geometry
date: '2026-11-21'
source:
- LIT-2960
corroborates:
- CLAIM-811
summary: >-
  Amari, Park and Ozeki (2006), [LIT-2960](../literature.d/LIT-2960.md), read in [NOTE-2255](../notes.d/NOTE-2255.md). Where
  network singularities are and what they do to learning: critical sets at
  finite parameters, cone apices in the space of distributions, a Milnor
  attractor for gradient flow, a slow manifold that makes the plateau, and
  repulsion under natural gradient. With the truth at the singularity, the
  gradient along the degenerate direction is cubic (Eq. 5.13), so the
  approach is algebraic, u ∝ t^(−1/2) (the reader's derivation; the paper
  states no rate).
---
<!-- inactive-ok-file: LIT-3017 — Deferred, registered 2026-11-21 from this reading, unread -->

# THEORY-2163: Fisher singularities cause learning plateaus

## Source

Amari, Park and Ozeki, "Singularities Affect Dynamics of Learning in
Neuromanifolds", Neural Computation 18, 1007–1065 (2006), [LIT-2960](../literature.d/LIT-2960.md), read
from the published version in [NOTE-2255](../notes.d/NOTE-2255.md).

## What was actually shown

- **Where.** The Fisher matrix degenerates on C : vw = 0 for one hidden
  unit, and on vᵢwᵢ = 0 or wᵢ = ±wⱼ for k units (Eqs. 2.8–2.9, 2.25);
  "The Cramér-Rao theorem is no longer valid at the critical set C."
  These sets are "not isolated but form a continuum" (p. 1009). In the
  space of distributions the critical set becomes a single point joining
  two components, or the apex of a cone (pp. 1012, 1020, 1022); the image
  of the model near the truth is its "tangent cone" (p. 1025).
- **Plateaus from a regular truth.** C "works as a pseudo-attractor (the
  Milnor attractor) even when the true distribution is at a regular point
  far from it" (p. 1018); "a slow manifold emerges around the critical
  set to which the state is quickly attracted by fast dynamics, and then
  the state escapes toward the optimal point slowly in the slow manifold"
  (p. 1035), derived for the cone model and the mixture, reported from
  Fukumizu and Amari ([LIT-3017](../literature.d/LIT-3017.md)) for perceptrons.
- **Approach to a singular truth.** In the mixture with the truth on the
  singularity, u̇ = −ηc₂(v)²u³ and v̇ is of order u⁴ (Eq. 5.13), so "u
  converges to 0 without significantly changing v". The paper gives no
  rate; u̇ = −au³ integrates to u ∝ t^(−1/2) for large t.
- **Natural gradient.** Near C "the infinitely strong repulsive force
  works in the direction of escape from C" (p. 1034); no slow manifold in
  the cone model.
- **Priors.** A smooth prior favours singular points "with an infinitely
  large factor" (p. 1029).

## What this does not say

- **That singularities are boundaries.** The paper's singular sets lie
  inside parameter space at finite values, and in the space of
  distributions at a cone apex or pinch point; it never uses the word
  "boundary".
- **Plateau lengths or escape rates.** Plateaus are shown in figures; no
  time course of escape is derived.
- **Power-law relaxation or a broad distribution of timescales.** Its
  plateaus are transients that end in escape.
- **Anything about learning coefficients or resolution of
  singularities**, which it names as another framework and does not use.
- **Large networks.** Every derivation is in a model with two effective
  parameters near C.
