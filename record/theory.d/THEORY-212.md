---
number: 212
status: Proposed
formerly:
- THEORY-tmphyt3v
promote_when: >-
  The regime dependence found outside the solvable model. What would
  promote: in deep or nonlinear networks trained by gradient descent from
  starts that differ only in the relative scale of layers, with the
  absolute scale fixed, learning curves going from stage-like to
  exponential, and the NTK from moving to static, as the relative scale
  moves from balanced to unbalanced. Kunin et al. (2024), which the paper
  cites for nonlinear and practical settings, is the first source to read.
  What would refute it: networks where the relative scale, with absolute
  scale fixed, makes no difference to the regime. The checks on the
  solvable model itself, such as simulations matching the formulas, cannot
  settle it.
title: 'In a two-layer linear network trained by gradient flow, the relative scale of the two layers, which gradient flow conserves, sets the learning regime: balanced layers learn in sigmoidal stages and both build task-specific representations, while strongly unbalanced layers learn exponentially with a static kernel and leave the larger layer task-agnostic'
version: 1
tags:
- learning-theory
- representation-learning
- anthology-candidate
date: '2026-10-13'
source:
- LIT-943
summary: >-
  Dominé et al. (2025), [LIT-943](../literature.d/LIT-943.md), read in [NOTE-715](../notes.d/NOTE-715.md). With whitened
  inputs and a λ-balanced start, W₂ᵀW₂ − W₁W₁ᵀ = λI, the full gradient flow
  is solved exactly. λ is conserved and sets the regime. As λ → 0,
  singular values are learned in sigmoidal stages, as in Saxe et al., and
  both layers become task-specific. As |λ| → ∞, learning is exponential,
  the NTK is static, and the larger layer stays near the identity while
  the smaller carries the task at scale ∝ 1/|λ|. The paper analyses
  gradient flow only. Under SGD the conserved quantity drifts
  ([THEORY-211](THEORY-211.md)), which [QUESTION-081](../questions.d/QUESTION-081.md) takes up.
bears_on:
- QUESTION-039
---
<!-- inactive-ok-file: THEORY-186 QUESTION-081 — Proposed or Open; the readings this account generalizes or is set beside, and the question it raises, open -->

# THEORY-212: In a two-layer linear network trained by gradient flow, the relative scale of the two layers, which gradient flow conserves, sets the learning regime: balanced layers learn in sigmoidal stages and both build task-specific representations, while strongly unbalanced layers learn exponentially with a static kernel and leave the larger layer task-agnostic

## Source

Dominé, Anguita, Proca, Braun, Kunin, Mediano & Saxe (2025), [LIT-943](../literature.d/LIT-943.md), read
in [NOTE-715](../notes.d/NOTE-715.md): §§1–7, with the proofs unchecked.

## The claim

Hold the absolute scale of the initialization fixed and vary how it is
split between the two layers, measured by λ in W₂ᵀW₂ − W₁W₁ᵀ = λI. Under
gradient flow λ never changes, so the split at initialization governs
the whole trajectory:

- **Balanced (λ → 0): rich.** Each singular value of the input–output map
  is learned in a sigmoidal transition, in order of strength. The NTK
  changes, and both layers end with task-specific representations,
  whatever the absolute scale. This is the stage-like learning of
  [THEORY-186](THEORY-186.md).
- **Unbalanced (|λ| → ∞): lazy.** Transitions are exponential,
  1 − e^{−|λ|t/τ}, and all modes are learned together, as in a shallow
  network. The NTK is static. The larger layer stays near an identity
  projection. The smaller layer carries the task structure, but at a
  scale ∝ 1/|λ| that leaves it out of the kernel.
- **Architecture and sign.** In funnel and inverted-funnel networks, one
  sign of λ gives lazy learning and the other gives a lazy phase followed
  by a delayed rich phase.

## What it bears on

- **[QUESTION-039](../questions.d/QUESTION-039.md)** asks what sets the order and moment at which structure
  is acquired. Here a single conserved quantity of the initialization
  decides whether acquisition comes in ordered stages or all at once.
- **[THEORY-186](THEORY-186.md) and [THEORY-187](THEORY-187.md)** are the balanced, aligned special case.
  Their condition of a balanced start is here a parameter, not a
  restriction.
- **[THEORY-211](THEORY-211.md).** Under SGD λ is not conserved: minibatch noise drives
  it toward the point where the layers' gradient noise balances. This
  account's control parameter is therefore fixed only under gradient flow.
  [QUESTION-081](../questions.d/QUESTION-081.md) asks what that does to the regimes.

## What this does not say

- It does not cover deep or nonlinear networks. The paper defers those to
  Kunin et al. (2024), not held, and expects the nonlinear case to differ.
- It does not cover SGD. The paper never models minibatch noise.
- It does not say which regime generalizes better in general. The
  transfer and fine-tuning results are on small constructed tasks.
- It does not instruct. Initialization schemes for practice belong to the
  anthology.
