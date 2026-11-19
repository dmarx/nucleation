---
number: 2027
status: Proposed
formerly:
- THEORY-tmpgjb4y
title: 'Dohare and colleagues show that networks trained by standard backpropagation on long sequences of new supervised tasks (Continual ImageNet, Permuted MNIST, class-incremental CIFAR-100) gradually lose the ability to learn each new task, down to about the level of a linear network, which is distinct from forgetting old tasks, and that methods which keep weights small while continually injecting fresh random units from the start of training, best of all their continual backpropagation, maintain that ability.'
version: 1
source:
- LIT-2810
tags:
- learning-theory
- representation-learning
date: '2026-11-19'
bears_on:
- QUESTION-495
corroborates:
- CLAIM-757
promote_when: >-
  An independent group, with code not the authors', reproduces on
  Continual ImageNet or class-incremental CIFAR-100 that backpropagation's
  accuracy on later tasks of fixed difficulty falls to near a linear
  baseline (or below retraining from scratch, with old classes still
  trained), and that continual backpropagation keeps later-task accuracy
  at or above early-task accuracy.
summary: >-
  From the reading of [LIT-2810](../literature.d/LIT-2810.md) in [NOTE-2137](../notes.d/NOTE-2137.md). Dohare, Hernandez-
  Garcia, Rahman, Mahmood and Sutton (2023), arXiv 2306.13812 (v3,
  "Maintaining Plasticity in Deep Continual Learning"), published with Lan
  as "Loss of plasticity in deep continual learning", Nature 632, 768-774
  (2024), open access. On long sequences of new tasks (Continual ImageNet,
  Permuted MNIST, class-incremental CIFAR-100, ant locomotion with PPO),
  standard deep learning gradually loses the ability to learn new tasks,
  which the authors keep distinct from forgetting. On ImageNet it falls to
  about a linear network, and on CIFAR-100 below retraining from scratch
  with old classes still trained. Small weights with continual injection
  of randomness (Shrink and Perturb, and their continual backpropagation)
  maintain plasticity, but all are applied from the start, and none is
  tested as a late rescue. It is here for overconsolidation (CLAIM-
  tmp8ljvp) beside [THEORY-1353](THEORY-1353.md), whose depletion reading it fits:
  plasticity is lost while the network keeps practising on varied tasks.
  Read in its NOTE.
---
<!-- inactive-ok-file: THEORY-1353 — Proposed; cited in this filing of 2026-11-19 -->

# THEORY-2027: Dohare and colleagues show that networks trained by standard backpropagation on long sequences of new supervised tasks (Continual ImageNet, Permuted MNIST, class-incremental CIFAR-100) gradually lose the ability to learn each new task, down to about the level of a linear network, which is distinct from forgetting old tasks, and that methods which keep weights small while continually injecting fresh random units from the start of training, best of all their continual backpropagation, maintain that ability.

## The account

Long continual training erodes what random initialization gave the network: small weights, live units, diverse features. With those gone, gradient descent learns each new task less well. Accuracy on Continual ImageNet falls from 89% on early tasks to 77% by the 2000th, and on class-incremental CIFAR-100 incremental training falls below retraining from scratch even though old classes are still trained. "Plasticity is maintained indefinitely only by algorithms that continually inject diversity into the network". Continual backpropagation does this by reinitializing a few low-utility units at every step.

## What it does not show

- Not that a remedy applied after plasticity is lost restores it. Every method runs from the start.
- Not a threshold. The decline reported is gradual.
- Not for large language models or pre-training on one stationary corpus. The tasks change continually.
- Not that continual backpropagation preserves old knowledge. The authors say it does not tackle forgetting.

## Note of 2026-11-19: Chen, Kunin, Yamamura and Ganguli, read
An analogy from Chen and colleagues ([NOTE-2127](../notes.d/NOTE-2127.md)), who do not discuss plasticity. Their collapse lowers the number of independent neurons and the effective rank and produces vanishing neurons, which parallel two of this account's correlates. Exactly coincident or zeroed units can never be separated by gradients, and near-collapsed ones escape slowly ("the repulsive escape will take longer the closer it starts from the invariant set", p. 10). On that reading, reinitializing units breaks a symmetry SGD cannot break. Their vanishing neurons are zero-weight GELU units, not dead ReLU units.
