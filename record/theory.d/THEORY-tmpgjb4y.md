---
status: Proposed
title: 'Dohare and colleagues show that networks trained by standard backpropagation on long sequences of new supervised tasks (Continual ImageNet, Permuted MNIST, class-incremental CIFAR-100) gradually lose the ability to learn each new task, down to about the level of a linear network, which is distinct from forgetting old tasks, and that methods which keep weights small while continually injecting fresh random units from the start of training, best of all their continual backpropagation, maintain that ability.'
version: 1
source:
- LIT-tmpco2kf
tags:
- learning-theory
- representation-learning
date: '2026-11-19'
bears_on:
- QUESTION-tmpwqepn
promote_when: >-
  An independent group, with code not the authors', reproduces on
  Continual ImageNet or class-incremental CIFAR-100 that backpropagation's
  accuracy on later tasks of fixed difficulty falls to near a linear
  baseline (or below retraining from scratch, with old classes still
  trained), and that continual backpropagation keeps later-task accuracy
  at or above early-task accuracy.
summary: >-
  From the reading of [LIT-tmpco2kf](../literature.d/LIT-tmpco2kf.md) in [NOTE-tmpzn6c6](../notes.d/NOTE-tmpzn6c6.md). Dohare, Hernandez-
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

# THEORY-tmpgjb4y: Dohare and colleagues show that networks trained by standard backpropagation on long sequences of new supervised tasks (Continual ImageNet, Permuted MNIST, class-incremental CIFAR-100) gradually lose the ability to learn each new task, down to about the level of a linear network, which is distinct from forgetting old tasks, and that methods which keep weights small while continually injecting fresh random units from the start of training, best of all their continual backpropagation, maintain that ability.

## The account

Long continual training erodes what random initialization gave the network: small weights, live units, diverse features. With those gone, gradient descent learns each new task less well. Accuracy on Continual ImageNet falls from 89% on early tasks to 77% by the 2000th, and on class-incremental CIFAR-100 incremental training falls below retraining from scratch even though old classes are still trained. "Plasticity is maintained indefinitely only by algorithms that continually inject diversity into the network". Continual backpropagation does this by reinitializing a few low-utility units at every step.

## What it does not show

- Not that a remedy applied after plasticity is lost restores it. Every method runs from the start.
- Not a threshold. The decline reported is gradual.
- Not for large language models or pre-training on one stationary corpus. The tasks change continually.
- Not that continual backpropagation preserves old knowledge. The authors say it does not tackle forgetting.
