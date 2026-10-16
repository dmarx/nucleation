---
status: Active
title: "Under genericity conditions, two dense or top-k (k ≥ 2) mixture-of-experts layers compute the same function only if they differ by a permutation of the experts with their gates and a common translation of the gate weights, and the translation leaves every interpolation barrier unchanged, so expert order is the only gate symmetry alignment must undo"
version: 1
tags:
- loss-landscapes
- mathematics
- anthology-candidate
date: '2026-10-16'
source:
- LIT-670
answers:
- QUESTION-069
summary: >-
  Tran, Trinh, Bui & Nguyen (2025), [LIT-670](../literature.d/LIT-670.md), read in [NOTE-513](../notes.d/NOTE-513.md). Softmax is
  invariant to a common shift of scores and the sum to the order of terms,
  so G(n) = ℝ^d × ℝ × S_n preserves the layer; Theorems 4.1–4.2 show that
  generically it is all of the gate's symmetry, for dense gating and for
  top-k with k ≥ 2 (top-1 has an extra scaling). Aligning expert order and
  then each expert's hidden units gives barriers of 0.0044–0.0066 between
  GPT-2 MoE layers fine-tuned from different seeds, against 0.14–0.86
  without the order step. Every experiment shares and freezes the backbone
  around the inserted layer, so it is not evidence about independently
  trained MoE models.
---
<!-- inactive-ok-file: THEORY-112 THEORY-114 — Proposed; the alignment and shared-history accounts this result is set beside, not leaned on -->

# THEORY-tmpe5k4b: Under genericity conditions, two dense or top-k (k ≥ 2) mixture-of-experts layers compute the same function only if they differ by a permutation of the experts with their gates and a common translation of the gate weights, and the translation leaves every interpolation barrier unchanged, so expert order is the only gate symmetry alignment must undo

## Source

Tran, Trinh, Bui & Nguyen (2025), [LIT-670](../literature.d/LIT-670.md) (NeurIPS 2025), read in [NOTE-513](../notes.d/NOTE-513.md).
[NOTE-513](../notes.d/NOTE-513.md) judged it not a THEORY source on its own, because its theorems
concern function equivalence and its experiments do not test whether
independently trained MoE models share a basin. This account states the
theorems as what they are, a characterisation of the gate's symmetry, and
keeps the experiments in their scope.

## What was actually shown

**The group.** G(n) = ℝ^d × ℝ × S_n acts by permuting experts with their
gating rows and adding a common (c_W, c_b) to every gating row. Softmax is
translation-invariant and the sum permutation-invariant, so dense and
top-k MoEs are invariant, on the open dense set where gate scores are
distinct (Propositions 3.1–3.2).

**It is all of the gate's symmetry, generically.** For dense gating, if the
experts are pairwise distinct functions and the gate differences W_i − W_j
are pairwise distinct, two MoEs computing the same function have the same
number of experts and parameters related by G(n) (Theorem 4.1). For top-k
with k ≥ 2 the same holds if the experts are strongly distinct (differ on
a dense set) and consecutive gate differences are linearly independent,
which needs n − 1 ≤ d (Theorem 4.2). Top-1 gating has an extra
positive-scaling symmetry and is set aside.

**Translation does not move barriers.** B(φ_A, φ_B) = B(φ_A, hφ_B) for any
pure translation h (Proposition D.1).

**The experiments.** Expert order is matched by a linear assignment on
centred gate weights or on Gram matrices of each expert's weights, then
hidden units are weight-matched within each matched pair. On One Billion
Word with a 12-layer GPT-2 and 4 or 8 experts, the barrier after full
matching is 0.0044–0.0066, and without the expert-order step 0.14–0.86
(Table 10). On CIFAR-10 ViTs matching leaves barriers at 4.16–10.83% of
naive interpolation's (Tables 3, 11).

**What could have come out otherwise.** The gate could have had further
symmetries, and skipping expert order could have cost little. Neither.

## What this does not say

- **That independently trained MoE models are linearly connected.** In
  every experiment a pretrained ViT or GPT-2 is frozen, one feed-forward
  layer is replaced by a randomly initialised MoE, and only that layer is
  fine-tuned from different seeds. The models compared share every weight
  outside the MoE.
- **That permutations suffice for linear connectivity.** For the gate,
  translation is irrelevant to barriers; that permutations then suffice
  rests on prior work (§5.1), not on this paper.
- **Anything inside the experts.** Experts are black boxes in the
  theorems; their internal symmetries are handled by weight matching.
- **That trained MoEs are generic.** Shared or collapsed experts would
  break the conditions, and whether trained models meet them is not
  checked.
- **A bound on the barrier.** The authors say the method gives none.

## Connections

- **[THEORY-112](THEORY-112.md)** holds that once an architecture's symmetries are factored
  out most of the linear barrier disappears, and that the group that
  matters is the full one: permutations for MLPs and CNNs, an orthogonal
  map on the residual stream for transformers. This account supplies the
  gate's part of the group for MoE layers.
- **[THEORY-114](THEORY-114.md)** holds that copies trained from a shared state become
  linearly connected only after early training. These experiments share a
  whole pretrained backbone, a far larger shared history than that.
- **[QUESTION-069](../questions.d/QUESTION-069.md)** asks how much connectedness depends on the shared
  history that produced the solutions. Here the shared history is almost
  everything but one layer.
- **The anthology's** [ANTH-SOTA-217](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/practices.d/SOTA-217.md) (align hidden-unit permutations before
  averaging) would need expert order aligned first for MoE layers.
