---
number: 181
status: Proposed
formerly:
- THEORY-tmps9ng8
promote_when: >-
  What would settle it is the same toy (two learned embeddings summed and
  decoded, addition hard-coded) run at several group sizes p. For each
  training set, it would have to report the nullity of the linear system
  its same-answer pairs impose and whether the trained network generalises.
  The claim holds if, at every p, full generalisation occurs with high
  probability exactly on training sets of nullity 2, and the empirical
  critical fraction follows the fraction at which nullity 2 becomes
  likely. It is refuted by networks in that setting that generalise fully
  on training sets of nullity above 2, or by a critical fraction that
  departs from the nullity threshold as p grows. More single-size runs, or
  pictures of structured embeddings in larger models, are the wrong kind
  of evidence: they show structure, not that the training set's equations
  are what fix it.
title: 'In a model that decodes the sum of two learned embeddings, a training set fixes the generalising representation of addition when its same-answer pairs leave only translation and scale free, and the critical training fraction is where that becomes likely'
version: 1
tags:
- representation-learning
- learning-theory
- anthology-candidate
date: '2026-10-09'
source:
- LIT-858
- LIT-341
summary: >-
  Liu et al. (2022), [LIT-858](../literature.d/LIT-858.md), in a toy built for it: same-answer
  training pairs force equal embedding sums, equal sums carry answers to
  unseen pairs, and for addition with p = 10 the fraction at which the
  forced equations first pin the embedding to a + kb (about 0.4) matches
  the onset of generalisation and Power et al.'s critical fraction
  ([LIT-341](../literature.d/LIT-341.md)). It is shown for one size, 1D embeddings and an operation built
  into the architecture. It is not shown that larger networks generalise
  by this mechanism, and for S₃ the networks generalise beyond it.
---

<!-- inactive-ok-file: THEORY-022 — Proposed; named as the neighbouring account of the modular-addition circuit -->

# THEORY-181: In a model that decodes the sum of two learned embeddings, a training set fixes the generalising representation of addition when its same-answer pairs leave only translation and scale free, and the critical training fraction is where that becomes likely

## Source

- Liu, Kitouni, Nolte, Michaud, Tegmark and Williams (2022), [LIT-858](../literature.d/LIT-858.md),
  §3 and Appendices C–F and H, as read in [NOTE-662](../notes.d/NOTE-662.md).
- Power et al. (2022), [LIT-341](../literature.d/LIT-341.md), for the critical training fraction in the
  original grokking setting, as read in [NOTE-287](../notes.d/NOTE-287.md).

## What was actually shown

The model is (a, b) ↦ Dec(E_a + E_b) with learned embeddings E_k. Take an
"ideal" model: zero training loss and an injective decoder. Then two
training pairs with i + j = m + n force E_i + E_j = E_m + E_n (Proposition
2). Conversely, any such coincidence must respect the arithmetic
(Proposition 1). An unseen pair (i, j) is answered correctly when
E_i + E_j equals the sum for some trained pair. So the accuracy a
representation allows can be computed from the parallelograms it realises.
For 1D embeddings and addition with p = 10, that predicted accuracy matches
the measured accuracy across training fractions and seeds (Fig. 3).

The equations a training set imposes form a linear system. Its null space
always contains translation and scale. When it contains nothing else, the
only solution is E_k = a + kb, which answers every pair. The probability
that a random training set reaches this point jumps near a training
fraction of 0.4 for p = 10. The number of steps for trained networks to
reach 95% of the possible parallelograms diverges at the same place
(Fig. 4). An effective loss on the normalised embeddings, the mean squared
parallelogram defect over the training set divided by Σ|E_k|², has exactly
those ground states. It conserves Σ E_k and Σ|E_k|² (proved), and its third
Hessian eigenvalue, zero below the threshold and rising above it, tracks
the time to structure qualitatively (Fig. 5). The same counting extends to
S₃ with matrix embeddings, where three parallelograms are needed to deduce
a fourth and the threshold is near 0.5 (App. H).

What could have come out otherwise: the networks could have generalised
below the nullity threshold, or failed above it. In 1D toy addition, they
did neither.

## What this does not say

- **That networks generalise this way in general.** The operation is built
  into the architecture: a sum of embeddings, or a product of 3 × 3
  matrices for S₃. The transformer and MNIST evidence in the same paper is
  PCA pictures and hyperparameter sweeps, with no parallelogram count. For
  S₃ the measured accuracy exceeds the parallelogram prediction (Fig. 18e),
  so even in a toy something else contributes.
- **That the threshold is a phase transition.** It is a jump at one size,
  p = 10. No scaling with p is reported, and the paper's "phases" are
  defined by accuracy thresholds.
- **That the effective loss is the network's loss.** It is posited, and
  derived only for a linear decoder with the decoder frozen (App. L). The
  quantitative gaps are attributed to the decoder without a test.
- **That the injectivity assumption holds where grokking was found.** A
  classifier's decoder is not injective, and the original result is a
  classification task.
- **Anything about which hyperparameters to use.** The paper's phase
  diagrams address that, and it is the anthology's subject, not this
  claim's.

## Connections

[THEORY-022](THEORY-022.md) states what the trained modular-addition transformer computes:
characters of ℤ/p at a few frequencies. This THEORY is about why a
training set suffices to fix a structured embedding at all, in a simpler
model. Both put the group in the task and the architecture, not in
anything the network discovers.
