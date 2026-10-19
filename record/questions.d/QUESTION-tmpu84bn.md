---
status: Open
title: 'Do trained networks follow the continually renormalized gradient flow toward neural collapse under MSE loss, and does the classifier stay near the least-squares classifier of its features outside Han, Papyan and Donoho''s settings?'
version: 1
tags:
- learning-theory
- representation-learning
date: '2026-10-19'
line: 'learned-structure'
refines:
- QUESTION-051
summary: >-
  Filed when the promotion audit (batch 038, [ADR-047](../decisions.d/ADR-047.md) v2 and v3) narrowed
  and promoted [THEORY-278](../theory.d/THEORY-278.md) to [LIT-974](../literature.d/LIT-974.md)'s measured cells and its renormalized
  model. The former promote_when asked whether ordinary training follows
  that model's dynamics, and whether the central path holds in settings
  the paper did not test. This question holds both.
---

# QUESTION-tmpu84bn: Do trained networks follow the continually renormalized gradient flow toward neural collapse under MSE loss, and does the classifier stay near the least-squares classifier of its features outside Han, Papyan and Donoho's settings?

## Why it is a question

[THEORY-278](../theory.d/THEORY-278.md) now states two things. First, in [LIT-974](../literature.d/LIT-974.md)'s fifteen
dataset–network cells, the MSE-trained classifier stays near the
least-squares classifier of its own features from an early epoch. Second,
in an unconstrained-features model whose features are re-whitened after
every step, gradient flow on that central path drives the class-separation
singular values ω_j of Σ_W^(−1/2)M̃ to infinity at the common rate
(4t/N)^(1/4), with their ratios tending to 1. That limit is neural
collapse. The continual renormalization is imposed, not measured, the
theory sets weight decay to zero while every run used it, and the
measured cells are balanced, ten-class and unaugmented.

## What would answer it

Track the singular values ω_j of Σ_W^(−1/2)M̃ through the terminal phase of
MSE training, without imposed re-whitening, on more than one architecture
and with several seeds. Check that they grow at a common rate, that their
ratio tends to 1, and that the limiting direction is set by the singular
vectors early in training. A derivation that drops the continual
renormalization or allows weight decay would answer the first part in
theory. The answer is no if, near the central path, the ω_j spread apart
or stall while L⊥_LS stays negligible. It is also no if the deviation from
the least-squares classifier stops being negligible with augmentation,
many classes or imbalance. Further closed-form results in the same
renormalized model cannot settle it, nor can NC1–NC4 curves alone, which
any account of collapse predicts.
