---
number: 2300
status: Proposed
formerly:
- THEORY-tmpq02z9
promote_when: >-
  An independent simulation of identical phase oscillators with slowly
  adapting product-form coupling confirms what the title says: that a
  split into synchronized and desynchronized groups arises from unstructured
  initial conditions, that the desynchronized group's dynamics changes from
  stationary to breathing to chaotic while the membership stays fixed, and
  that branches end in jumps that enlarge the synchronized cluster, with
  the sequence depending on history.
title: 'Augustsson and colleagues report that identical phase oscillators coupled through slowly adapting product-form weights split by themselves into a synchronized cluster and a desynchronized group; while the cluster fraction stays fixed, the desynchronized group passes from stationary through breathing to chaotic dynamics without any change of membership, each such branch ends in a crisis-like jump that enlarges the cluster, and which sequence of cluster sizes occurs depends on initial conditions and on the direction of a parameter sweep'
version: 1
tags:
- complex-systems
- network-science
date: '2026-11-22'
source:
- LIT-2244
bears_on:
- QUESTION-281
summary: >-
  Augustsson, Cestnik, Wolfrum, Bick, Yanchuk and Martens (2026),
  [LIT-2244](../literature.d/LIT-2244.md), read in [NOTE-2374](../notes.d/NOTE-2374.md) (supplement unread). Numerical, with
  exact reductions on invariant cluster subspaces. It bears on
  [QUESTION-281](../questions.d/QUESTION-281.md) as a case of a distinction made at an instability, kept
  through changes of dynamics, and remade by crises. Proposed until
  reproduced independently.
---

# THEORY-2300: Augustsson and colleagues report that identical phase oscillators coupled through slowly adapting product-form weights split by themselves into a synchronized cluster and a desynchronized group; while the cluster fraction stays fixed, the desynchronized group passes from stationary through breathing to chaotic dynamics without any change of membership, each such branch ends in a crisis-like jump that enlarges the cluster, and which sequence of cluster sizes occurs depends on initial conditions and on the direction of a parameter sweep

## Source

Augustsson, Cestnik, Wolfrum, Bick, Yanchuk and Martens (2026),
"Self-organizing Chimera States in Adaptive Networks", arXiv 2608.20517,
[LIT-2244](../literature.d/LIT-2244.md), read in [NOTE-2374](../notes.d/NOTE-2374.md).

## The account

Phases follow a Kuramoto–Sakaguchi law with weights wₖₗ = ηₖζₗ, the
receiver's sensitivity times the sender's efficacy, which relax slowly
(ε = 0.01) toward targets set by each unit's phase relative to the global
order parameter. Full synchrony loses transverse stability at a closed-form
cluster-branching point. Beyond it, from random starts, the population
splits into a synchronized cluster of fraction ρ and a desynchronized
group with a common mean frequency. Sweeping one parameter, the
desynchronized group's dynamics passes from stationary to breathing to
chaotic by a quasiperiodic route while ρ and the membership stay fixed;
then some desynchronized units join the cluster and a new branch begins.
The landscape is highly multistable and path-dependent.

## Bearing

[QUESTION-281](../questions.d/QUESTION-281.md): the distinction between the groups comes into being at an
instability of synchrony, is kept through bifurcations of one group's
dynamics, and passes away in jumps. Keeping and making come apart here:
the membership persists while the dynamics changes, and changes only at
crises.
