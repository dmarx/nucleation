---
number: 158
status: 'Open'
formerly:
- QUESTION-tmp7nyvd
title: "Does gradient descent on a two-layer network, without a spectral initialization or a data split, recover direction k of a scale-free hierarchical multi-index target at n = Θ(a_k^(−2) d) samples and attain the optimal weighted error, and do the same thresholds hold for an input law that is not isotropic Gaussian?"
version: 1
tags:
- learning-theory
- representation-learning
date: '2026-10-19'
line: 'learned-structure'
refines:
- QUESTION-039
summary: >-
  The condition formerly on [THEORY-283](../theory.d/THEORY-283.md), moved here unchanged when
  [THEORY-283](../theory.d/THEORY-283.md) was narrowed and promoted on 2026-10-19. The thresholds and
  rates are proved for the Bayes-optimal and spectral estimators, and for a
  network whose first layer is the spectral estimator. Whether gradient
  descent reaches them, or whether they survive a second input law, is open.
---

# QUESTION-158: Does gradient descent on a two-layer network, without a spectral initialization or a data split, recover direction k of a scale-free hierarchical multi-index target at n = Θ(a_k^(−2) d) samples and attain the optimal weighted error, and do the same thresholds hold for an input law that is not isotropic Gaussian?

## Why it is a question

[THEORY-283](../theory.d/THEORY-283.md), narrowed on 2026-10-19, holds that for a hierarchical
multi-index target with isotropic Gaussian inputs and even, separable
links, direction k becomes weakly recoverable at n = Θ(a_k^(−2) d), that a
target-agnostic spectral estimator attains the thresholds and the optimal
weighted error, and that a network given that estimator as its first layer
attains them in excess risk ([LIT-940](../literature.d/LIT-940.md)). Until that date its promote_when
asked for more. At the owner's direction, from the promotion audit's batch
024 ([ADR-047](../decisions.d/ADR-047.md)), the THEORY was narrowed and promoted on the proved results,
and the condition moved here unchanged. It refines [QUESTION-039](QUESTION-039.md)'s question
of what sets the order and moment of acquisition.

It is open because the network theorem is for Algorithm 1 (spectral
initialization, a data split, a ridge readout). The link to gradient
descent is [LIT-940](../literature.d/LIT-940.md)'s Remark 3.5, cited from other work, not proved, and
every result is for isotropic Gaussian inputs.

## What would answer it

The condition formerly on [THEORY-283](../theory.d/THEORY-283.md), unchanged. A proof that gradient
descent on a two-layer network, without a spectral initialization or a
data split, recovers direction k at n = Θ(a_k^(−2) d) samples and attains
the optimal weighted error. Or the same thresholds proved for a second
input law that is not isotropic Gaussian. It is refuted inside the regime
by a direction that a Bayes-optimal or spectral estimator recovers well
below a_k^(−2) d, or one that stays unrecoverable well above it.
Simulations of more spikes leaving the bulk cannot settle it.
