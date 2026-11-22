---
status: Proposed
promote_when: >-
  An independent reproduction, on the released code or on fresh runs, of
  three things the title asserts: the probe's Hessian threshold at
  β = 1/λmax(Cov z) on real encoder features; in modular-addition
  grokking, a crossing near the start of training with generalisation
  thousands of steps later, sooner with more weight decay and absent
  within the paper's horizon without it; and a positive early-to-late
  per-atom part-of-speech purity correlation in a sparse autoencoder.
  Not met by a restatement that cites this paper. Not defeated by a
  showing that the probe's crossing does not cause the network's
  plateau, which the title does not assert.
title: "Yang finds that a detached Gaussian-mixture probe fitted to an encoder's output loses its collapsed state through a supercritical pitchfork at a precision equal to the reciprocal of the largest eigenvalue of the features' covariance, that the visible split can lag that crossing by orders of magnitude, so that in modular-addition grokking the crossing comes near step 40 and generalisation thousands of steps later, sooner with more weight decay, and that in sparse autoencoders an atom's part-of-speech purity early in training predicts its purity at convergence"
version: 1
tags:
- learning-theory
- representation-learning
date: '2026-11-22'
source:
- LIT-2961
bears_on:
- QUESTION-217
summary: >-
  Yang (2026), [LIT-2961](../literature.d/LIT-2961.md), read in [NOTE-tmpg5q4t](../notes.d/NOTE-tmpg5q4t.md). Rose, Gurewitz and Fox's
  annealing threshold made dynamic, with the crossing separated from the
  visible split. The sharp edges: the pitchfork is the probe's, and the
  probe is detached ("the encoder's gradients never see the probe"); the
  bridge from the probe's split to the network's grokking plateau is a
  tilt the paper adds by hand and calls empirical; the per-atom choice is
  made by noise and cubic terms on a shared unstable subspace, not by
  small initial advantages compounding. Proposed until reproduced.
---
<!-- inactive-ok-file: THEORY-1429 — Proposed; the reading that qualifies the paper's language -->

# THEORY-tmpu0f9k: Yang finds that a detached Gaussian-mixture probe fitted to an encoder's output loses its collapsed state through a supercritical pitchfork at a precision equal to the reciprocal of the largest eigenvalue of the features' covariance, that the visible split can lag that crossing by orders of magnitude, so that in modular-addition grokking the crossing comes near step 40 and generalisation thousands of steps later, sooner with more weight decay, and that in sparse autoencoders an atom's part-of-speech purity early in training predicts its purity at convergence

## Source

Yang (2026), "Feature Lottery? A Bifurcation Theory of Concept
Emergence", arXiv 2605.24057, [LIT-2961](../literature.d/LIT-2961.md), read in [NOTE-tmpg5q4t](../notes.d/NOTE-tmpg5q4t.md).

## What was actually shown

- **Proved:** the Hessian of the probe's negative log-likelihood at the
  collapsed state has anti-symmetric eigenvalues (β/K)(1 − βσᵢ²), the
  lowest crossing zero at βc = 1/λmax(Σ) (Theorem 1), Rose's critical
  temperature in another convention. Checked numerically by the reader.
- **Proved, from its hypotheses:** if β rises and βc falls, they cross
  (Prop. 1, an intermediate-value step).
- **Observed:** crossing at steps 34–60 in all 15 grokking runs; escape
  times from 8,900 to 147,167 steps as weight decay falls from 1.0 to 0.1;
  no escape in 50,000 steps without weight decay (three seeds).
- **Observed:** Spearman +0.41 between per-atom POS purity at 5% of
  training and at convergence in SAEs on Pythia-160M, across dictionary
  sizes, rising to +0.88 at half of training.

## What this does not say

- That the network's weights pass through a bifurcation. The probe is
  detached, and the crossing time depends in part on the probe's own
  learning rate for β and its starting value, which are not swept.
- That the probe's crossing causes the grokking plateau or its end. The
  link is the tilt γU(ε) of App. C, added by hand.
- Anything about local learning coefficients or singular learning theory.
- That a "sharp dynamical phase transition" in Kuehn's sense occurs
  ([THEORY-1429](THEORY-1429.md)): a supercritical pitchfork has no fast jump.
- That early advantages compound. The direction each atom takes is chosen
  by "initialization noise and the cubic terms" and persists for a finite
  window (Prop. 2).
