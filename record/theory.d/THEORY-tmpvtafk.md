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
  Iqbal, Keller, Song, Miyato and Welling (LIT-tmpyahtz), read in
  NOTE-tmpsdqio. A mean-field analysis gives the transition and the
  protected Jacobian component; 100-layer equivariant MLPs train across
  the broken phase; generic networks show the same order parameter with
  no performance gain. Defects (U(1) vortices) form in a convolutional RNN
  but their use is not shown. A stand-in for the thesis of LIT-tmp01nqp,
  the owner's U6 example.
---
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

On QUESTION-125: a bifurcation of the layer map that carries a functional
consequence in equivariant networks and none in generic ones. On
QUESTION-392: whether equivariance creates very deep trainability or is
another route to it depends on the declared space of architectures. On
QUESTION-281: a bifurcation route by which a distinction (phase on the
orbit) is retained through depth.
