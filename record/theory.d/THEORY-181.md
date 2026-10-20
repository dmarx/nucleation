---
number: 181
status: Active
formerly:
- THEORY-tmps9ng8
title: "In a model that decodes the sum of two learned embeddings, at zero training loss with an injective decoder, a training set fixes the generalising representation of addition when its same-answer pairs leave only translation and scale free; for non-modular addition with p = 10 and one-dimensional embeddings, generalisation sets in near the training fraction, about 0.4, at which that becomes likely"
version: 2
history:
- version: 2
  date: '2026-10-19'
  note: >-
    Narrowed and promoted, carrying out the promotion audit's decision for
    THEORY-181 (batch 043, ADR-047 v2 and v3). The theorem is re-derived
    in the dated note below and the title names its model: zero training
    loss and an injective decoder. The critical-fraction clause is held to
    the one size Liu et al. measured, non-modular addition with p = 10 and
    1D embeddings. The former promote_when, a test across sizes, moves to
    QUESTION-199.
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
answers:
- QUESTION-058
---

<!-- inactive-ok-file: THEORY-022 — Proposed; named as the neighbouring account of the modular-addition circuit -->

# THEORY-181: In a model that decodes the sum of two learned embeddings, at zero training loss with an injective decoder, a training set fixes the generalising representation of addition when its same-answer pairs leave only translation and scale free; for non-modular addition with p = 10 and one-dimensional embeddings, generalisation sets in near the training fraction, about 0.4, at which that becomes likely

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

## Note of 2026-10-19: the theorem re-derived, and the measurement held to one size

The promotion audit (batch 043, [ADR-047](../decisions.d/ADR-047.md) v2 and v3) re-derived the theorem
and held the measurement to what was measured.

**The theorem.** The model is (a, b) ↦ Dec(E_a + E_b), with embeddings
E_k ∈ R^m. At zero training loss with an injective decoder, two training
pairs with the same answer, i + j = u + v, force E_i + E_j = E_u + E_v
(Proposition 2: equal outputs, and Dec is injective). Each such equation
is linear in (E_0, …, E_(p−1)) and acts on each of the m coordinates
separately. Every solution space contains the constants (E_k = a) and the
scalings (E_k = kb), since both make the sum depend on i + j alone. If the
nullity is 2, the solutions are exactly E_k = a + kb with a, b ∈ R^m.
Then E_i + E_j = 2a + (i + j)b depends on the answer alone, so every
unseen pair whose answer occurs in training gets that answer's sum, which
the decoder maps to the answer. That is the sense of "fixes the
generalising representation": unique up to translation and scale. A pair
whose answer no training pair has is not answered by the representation
alone; the extreme sums 0 and 2p − 2 each come from one pair.

**The measurement.** [NOTE-662](../notes.d/NOTE-662.md) read Liu et al. in full. For non-modular
addition with p = 10 and one-dimensional embeddings, the probability that
a random training set has nullity 2 jumps near a fraction of 0.4, a value
the text states. The steps trained networks need to realise 95% of the
parallelograms diverge at the same fraction (Fig. 4a–b). That is one study
at one size, so the title is held to it ([ADR-047](../decisions.d/ADR-047.md) v3). That the critical
fraction tracks the nullity threshold at other sizes, which the former
promote_when asked, is [QUESTION-199](../questions.d/QUESTION-199.md). Power et al.'s critical fraction
comes from a different task, modular arithmetic with a transformer, and
the title no longer names it.
