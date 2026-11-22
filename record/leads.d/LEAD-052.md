---
number: 52
status: Open
formerly:
- LEAD-tmp8w5n1
title: 'Train on synthetic data with a known tree and spectral strength per level varied independently of the tree, and map when acquisition is coarse-first, fine-first, simultaneous or mixed'
version: 1
stage: idea
priority: medium
method:
- empirical
- formal
tags:
- learning-theory
- representation-learning
date: '2026-11-19'
line:
- learned-structure
advances:
- QUESTION-217
- QUESTION-039
operationalized_in:
- CASE-tmp7n58t
summary: >-
  Named in [QUESTION-217](../questions.d/QUESTION-217.md). Filed by the backlog audit of 2026-11-19.
---

# LEAD-052: Train on synthetic data with a known tree and spectral strength per level varied independently of the tree, and map when acquisition is coarse-first, fine-first, simultaneous or mixed

## What it would do

Train deep linear, kernel-regime and small nonlinear networks and report a
phase diagram of acquisition order; state sufficient conditions as a
theorem where possible.

Where the record names it:

- [QUESTION-217](../questions.d/QUESTION-217.md): "synthetic data with a known tree, with the spectral
  strength assigned to each level varied independently of the tree"

## What would count

Order set by spectral strength rather than depth answers [QUESTION-217](../questions.d/QUESTION-217.md) for
these classes and bears on [QUESTION-039](../questions.d/QUESTION-039.md).


## Note of 2026-11-22: carried out

<!-- inactive-ok-file: CASE-tmp7n58t CLAIM-tmpzujm1 CLAIM-tmp0h57p — new; the study and claims of this lead, filed 2026-11-22 -->

Done on 2026-11-22 (scratch/studies/lead-052/, with eleven tests): exact
kernel flow, NTK-parametrized ReLU networks of width 64 to 4096, deep
linear networks of two and three layers, and two-layer ReLU networks from
small and order-one scale, on a depth-3 tree over a grid of target
strengths and a grid of input against target strengths
(CASE-tmp7n58t). The theorem the lead hoped for holds for two classes on
tree-symmetric data (CLAIM-tmpzujm1): kernels order the levels by input
strength alone, decoupled deep linear networks by input times target
strength. The small ReLU network keeps the linear direction with a
compressed spread (CLAIM-tmp0h57p). What remains: data off the tree
symmetry, sampled or noisy items, hidden-layer probes as decoders, larger
trees and networks, and explanations for the ReLU network's compression
and the three-layer linear network's heavier weighting of target strength.
