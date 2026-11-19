---
status: Proposed
title: 'Iqbal and colleagues show, at initialisation and large width and in experiments, that a deep network with U(1)- or O(k)-equivariant middle layers has a transition at σ_W = 1 above which a symmetry-broken phase conserves the relative phase of two inputs across layers and keeps one Jacobian component O(1) at any depth, so very deep networks train without normalisation over the whole phase, while the same order parameter in non-equivariant networks brings no gain'
version: 1
source:
- LIT-tmpyahtz
tags:
- representation-learning
- learning-theory
date: '2026-11-19'
bears_on:
- QUESTION-125
- QUESTION-392
- QUESTION-281
promote_when: >-
  An independent reproduction, or a peer-reviewed version, showing the
  training advantage beyond Fashion-MNIST, MNIST and toy sequence tasks.
summary: >-
  Iqbal, Keller, Song, Miyato and Welling ([LIT-tmpyahtz](../literature.d/LIT-tmpyahtz.md)), read in
  [NOTE-tmpsdqio](../notes.d/NOTE-tmpsdqio.md). A mean-field analysis gives the transition and the
  protected Jacobian component; 100-layer equivariant MLPs train across
  the broken phase; generic networks show the same order parameter with
  no performance gain. Defects (U(1) vortices) form in a convolutional RNN
  but their use is not shown. A stand-in for the thesis of [LIT-tmp01nqp](../literature.d/LIT-tmp01nqp.md),
  the owner's U6 example.
---
<!-- inactive-ok-file: THEORY-tmpqtb3q — Proposed; cited in this filing of 2026-11-19 -->
<!-- inactive-ok-file: LIT-tmp01nqp — Unfetched; cited in this filing of 2026-11-19 -->

# THEORY-tmpvtafk: Iqbal and colleagues show, at initialisation and large width and in experiments, that a deep network with U(1)- or O(k)-equivariant middle layers has a transition at σ_W = 1 above which a symmetry-broken phase conserves the relative phase of two inputs across layers and keeps one Jacobian component O(1) at any depth, so very deep networks train without normalisation over the whole phase, while the same order parameter in non-equivariant networks brings no gain

## The account

Equivariance is put in the middle layers of a network whose task has no
symmetry. In the broken phase a symmetry rotation of the input must
propagate to the output, so the relative phase on the symmetry orbit is
conserved across layers and one component of the input–output Jacobian is
pinned to the order parameter. Information therefore propagates through
depth over a whole region of parameters, not at a tuned critical point.

## What it does not show

Anything after initialisation, beyond the experiments; anything about
discrete symmetries or domain walls; that defects carry information.

## Bearing

On [QUESTION-125](../questions.d/QUESTION-125.md): a bifurcation of the layer map that carries a functional
consequence in equivariant networks and none in generic ones. On
[QUESTION-392](../questions.d/QUESTION-392.md): whether equivariance creates very deep trainability or is
another route to it depends on the declared space of architectures. On
[QUESTION-281](../questions.d/QUESTION-281.md): a bifurcation route by which a distinction (phase on the
orbit) is retained through depth.

## Note of 2026-11-19: readings for the exchange "Topological protection explained"

Schoenholz and colleagues ([THEORY-tmpqtb3q](THEORY-tmpqtb3q.md)), read: give the baseline this account improves on. In generic random networks, input correlations survive arbitrary depth only at the critical point χ1 = 1, and trainable depth falls to about 6ξc away from it, so deep trainability is fine-tuned. This entry's claim is that equivariance turns that point into a phase. They also show why a generic network's own order parameter carries trainability only at criticality, which makes this entry's dissociation intelligible without testing it. Equivariant networks are not studied.

No status change.

## Note of 2026-11-19: Poole and colleagues, read
Background, with a qualification (NOTE-tmpa7swy). Poole and colleagues supply the generic baseline this account is set against: the χ1 = 1 boundary, and the bias-free transition at σw = 1. In their account the chaotic phase is where depth buys expressivity, so the generic network's chaotic phase is not only something to avoid, and the paper never speaks of an "edge of chaos". Nothing on equivariance, information retention or trainability.
