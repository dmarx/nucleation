---
status: Proposed
title: 'Linear mode connectivity emerges during training, not at initialization: copies trained from a shared state become stable to SGD noise after 1.5–20% of training, and independently trained networks become linearly connected after alignment only gradually'
version: 1
tags:
- loss-landscapes
- anthology-candidate
date: '2026-10-30'
source:
- LIT-654
- LIT-661
- LIT-680
extends:
- THEORY-114
promote_when: >-
  The onset measured outside image classification, and the aligned half
  measured on more than MLPs. Frankle et al.'s onset covers six vision
  networks, and Git Re-Basin's aligned onset covers MLPs on MNIST and
  CIFAR-10 only. What would promote: in a language model or a transformer,
  the barrier tracked against training time, with seeds, both between copies
  spawned from a shared state and between independently initialized runs
  aligned under the architecture's symmetry group, with each high at step 0
  and falling to near zero later. Or the aligned onset reproduced for
  standard-width convnets or ResNets. What would refute it: independently
  initialized networks of practical width that are linearly connected after
  alignment at step 0, under an alignment computed from the initial weights
  alone. Or copies spawned at initialization of a standard deep network that
  end up linearly connected. More vision networks with the same onset curve
  cannot settle it.
bears_on:
- QUESTION-312
summary: >-
  The wide form [THEORY-114](THEORY-114.md) held before the tenth status review narrowed it,
  kept as a Proposed reading by the [ADR-047](../decisions.d/ADR-047.md) kind-1 sweep of 2026-10-30: the
  source asserts it, and [THEORY-114](THEORY-114.md), Active, is its evidence.
---
<!-- inactive-ok-file: ADR-047 — Superseded by ADR-057, which keeps its evidence rulings; cited for the kind-1 rule this entry is filed under -->

# THEORY-tmp1h9ud: Linear mode connectivity emerges during training, not at initialization: copies trained from a shared state become stable to SGD noise after 1.5–20% of training, and independently trained networks become linearly connected after alignment only gradually

## Source

Frankle, Dziugaite, Roy & Carbin (2020), [LIT-654](../literature.d/LIT-654.md), read in [NOTE-514](../notes.d/NOTE-514.md); and
Ainsworth, Hayase & Srinivasa (2023), Git Re-Basin, [LIT-661](../literature.d/LIT-661.md), read in
[NOTE-532](../notes.d/NOTE-532.md). Ferbach et al. (2024), [LIT-680](../literature.d/LIT-680.md), read in [NOTE-543](../notes.d/NOTE-543.md), reconciles the
aligned half with connectivity at initialization in principle. What the
networks measured showed is [THEORY-114](THEORY-114.md), which this entry extends.

## The claim

Both papers state the result as a general property of training, not of the
networks they ran. Frankle et al. conclude that standard networks become
stable to SGD noise early in training, after which copies end in one
linearly connected minimum, and that, except in small settings, networks
are unstable at initialization ([NOTE-514](../notes.d/NOTE-514.md), C1–C2). LeNet on MNIST is their
small setting: it is stable from the start. Git Re-Basin concludes that
linear mode connectivity modulo permutation "is an emergent property of
training, and we were unable to uncover it early in training" (§5.2;
[NOTE-532](../notes.d/NOTE-532.md), C3). Ferbach et al.'s width bound explains why the two agree with
Entezari et al.'s theorem of connectivity at initialization: that needs
widths far past any trained in practice.

The evidence is six vision networks for the shared-state half and MLPs on
MNIST and CIFAR-10 for the aligned half. The claim is that training, not
initialization, makes the straight-line connection in general, in other
architectures and tasks as well.

## What would settle it

The promote_when, which is [QUESTION-312](../questions.d/QUESTION-312.md): the onset tracked against training
time, with seeds, in a language model or transformer, for both halves, or
the aligned onset reproduced for standard-width convnets or ResNets.
Connectivity at step 0 under an alignment computed from the initial weights
alone, at practical width, would refute it. More vision networks with the
same onset curve cannot settle it.
