---
status: Proposed
promote_when: >-
  A measurement in trained networks that the model's dynamics are the ones
  training follows. Track the singular values ω_j of Σ_W^(−1/2)M̃ through
  the terminal phase of MSE training, without imposed re-whitening, on more
  than one architecture and with several seeds. Check that they grow at a
  common rate, that their ratio tends to 1, and that the limiting direction
  is set by the singular vectors early in training, as Corollary 2 predicts.
  A derivation that drops the continual renormalization, or that allows
  weight decay, would also promote it. It is refuted if, near the central
  path, the ω_j spread apart or stall while L⊥_LS stays negligible. It is
  also refuted if the deviation from the least-squares classifier stops
  being negligible in settings Han, Papyan and Donoho did not test
  (augmentation, many classes, imbalance). Further closed-form results in
  the same renormalized model cannot settle it, nor can NC1–NC4 curves
  alone, which any account of collapse predicts.
title: 'Deep classifiers trained with MSE loss stay near the least-squares classifier for their own features and move along the central path by the dynamics of continually renormalized gradient flow, whose equal-rate growth of the whitened class-separation singular values is how they reach neural collapse, as Han, Papyan and Donoho propose'
version: 1
tags:
- learning-theory
- representation-learning
- loss-landscapes
date: '2026-10-20'
source:
- LIT-974
extends:
- THEORY-278
summary: >-
  Han, Papyan & Donoho (2021; ICLR 2022), [LIT-974](../literature.d/LIT-974.md), read in [NOTE-783](../notes.d/NOTE-783.md). The
  paper's proposed explanation of neural collapse under MSE in real
  networks, filed apart from its measured central-path proximity and its
  derivation in a renormalized model ([THEORY-278](THEORY-278.md)) under [ADR-047](../decisions.d/ADR-047.md) v4.
  Renormalization is imposed, not measured, and every experiment used weight
  decay, which the derivation excludes.
---

# THEORY-tmpdzmf1: Deep classifiers trained with MSE loss stay near the least-squares classifier for their own features and move along the central path by the dynamics of continually renormalized gradient flow, whose equal-rate growth of the whitened class-separation singular values is how they reach neural collapse, as Han, Papyan and Donoho propose

## Source

Han, Papyan & Donoho (2021; ICLR 2022), [LIT-974](../literature.d/LIT-974.md), read in [NOTE-783](../notes.d/NOTE-783.md). The
paper's title and abstract present the central path and the dynamics on it
as an account of how networks trained with MSE reach neural collapse.

## What is asserted

That trained networks, not only the unconstrained-features model, stay
near the least-squares classifier for their own features and follow the
continually renormalized gradient flow along that path, so that the
whitened class-separation singular values grow at a common rate and their
ratio tends to 1. Neural collapse is then the limit of those dynamics.

## What the record holds toward it

[THEORY-278](THEORY-278.md), which is Active, holds the measured half and the derived
half. The measured half is that L⊥_LS is negligible from an early epoch in
VGG, ResNet and DenseNet on five balanced ten-class datasets. The derived
half is that, for unconstrained features renormalized to identity
within-class covariance and with no weight decay, gradient flow gives
ω_j/(4t/N)^(1/4) → 1 and NC1–NC4. The step between them, that networks
train by the renormalized flow, is assumption A3, motivated by batch
normalization and never measured.

## What this does not say

- Anything about cross-entropy, which has no closed-form classifier.
- That collapse is reached in finite training.
- Why collapse stalls at different levels on different datasets.

## What would confirm or reject it

The promote_when, which is the narrowed entry's former condition.
[QUESTION-181](../questions.d/QUESTION-181.md) asks it, and [QUESTION-202](../questions.d/QUESTION-202.md) asks the wider question of where
neural collapse holds at all.
