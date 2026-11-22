---
number: 2009
status: Proposed
formerly:
- THEORY-tmp4kekv
title: 'Chen, Kunin, Yamamura and Ganguli show that the symmetry-generated affine sets where a hidden neuron vanishes or two neurons in a layer are identical are invariant under SGD; that for a continuous model of SGD such a set attracts under a sufficient condition weighing the loss''s curvature against gradient noise, which can hold at saddles and maxima; and that VGG-16 and ResNet-18 trained with SGD form clusters of near-identical neurons that grow with the learning rate'
version: 1
source:
- LIT-2793
tags:
- learning-theory
- loss-landscapes
date: '2026-11-19'
promote_when: >-
  The record rederives the invariance of the vanishing-neuron and
  identical-neuron sets and the one-dimensional attractivity condition,
  and an independent replication, or the paper's figures against an
  untrained or matched-tolerance baseline, shows the fraction of
  independent neurons in an SGD-trained deep network falling as the
  learning rate rises.
bears_on:
- QUESTION-206
- QUESTION-080
summary: >-
  From the reading of [LIT-2793](../literature.d/LIT-2793.md) in [NOTE-2127](../notes.d/NOTE-2127.md). The source Velarde
  and colleagues cite for covers attracting SGD; it supports less than
  they cite it for. Proposed until its promote_when is met.
---
<!-- inactive-ok-file: THEORY-2163 THEORY-2164 — Proposed or Rejected; filed 2026-11-21 from the readings of Gutenkunst et al., Transtrum & Qiu, Amari, Park & Ozeki and Wei et al. -->

# THEORY-2009: Chen, Kunin, Yamamura and Ganguli show that the symmetry-generated affine sets where a hidden neuron vanishes or two neurons in a layer are identical are invariant under SGD; that for a continuous model of SGD such a set attracts under a sufficient condition weighing the loss's curvature against gradient noise, which can hold at saddles and maxima; and that VGG-16 and ResNet-18 trained with SGD form clusters of near-identical neurons that grow with the learning rate

## The account

A set that no minibatch update leaves is invariant under SGD. Fixed sets
of reflection symmetries of the parameterization are such sets, and two
occur in every feed-forward network: a hidden neuron with all its
weights zero (when the activation vanishes at zero), and two neurons of
a layer with identical weights. In the stochastic-gradient-flow model,
whether such a set attracts depends on curvature against noise; in one
dimension the sign of α = L″(0) + ½D″(0) decides, and in many dimensions
the authors give only a sufficient condition. Noise can make a saddle or
a maximum attracting. Trained VGG-16 and ResNet-18 networks show large
clusters of near-identical neurons, more with larger learning rates; in
a linear teacher-student model the collapse keeps weak noisy modes from
being learned, continuing after the training loss has plateaued.

## Evidence

Propositions and theorems with proofs for the continuous model; toy
models where thresholds are computed; deep-network experiments at a 10%
tolerance, with GELU, momentum and weight decay fixed. Not shown: a
threshold tested in a deep network, necessity, or the discrete SGD case.

## Note of 2026-11-21: Amari, Park & Ozeki (2006) and Wei et al. (2008), read

A cross-link: the sets this account calls invariant are the older
literature's singular sets. The vanishing-neuron set is Amari, Park and
Ozeki's critical set vᵢwᵢ = 0 and Wei and colleagues' elimination
singularity; the identical-neuron set is the wᵢ = ±wⱼ component and the
overlap singularity ([NOTE-2255](../notes.d/NOTE-2255.md), [NOTE-2254](../notes.d/NOTE-2254.md)). Both earlier works find
these sets attract gradient learning without being stable equilibria, a
"Milnor attractor" ([THEORY-2163](THEORY-2163.md)) or "Milnor-like attractor" whose
basin "has a positive measure" ([THEORY-2164](THEORY-2164.md)), and in Wei and
colleagues noise moves the state along the line until it leaves. This
account adds SGD's own noise as what decides attraction. A parallel, not
an extension: the models and the noise differ, and no relation is
written.
