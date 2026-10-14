---
status: Proposed
promote_when: >-
  A direct test of the readout account: on few-shot runs that fail because
  of the examples drawn or because labels were consistently relabelled, a
  linear readout trained on the model's own last-token states recovers
  most of the accuracy the model's unembedding loses, in more than one
  model and on natural data. It is refuted if such readouts fail as the
  model does, or if separability measured another way (a trained probe
  rather than manifold capacity) falls with accuracy. What cannot settle
  it: further capacity curves of the kind already shown, which are the
  evidence the claim rests on.
title: 'In few-shot classification by a base language model, failures from the choice of examples or from relabelled categories leave the class representations separable and fail at the vocabulary readout'
version: 1
tags:
- representation-learning
date: '2026-10-14'
source:
- LIT-946
summary: >-
  Kirsanov et al. (2025), [LIT-946](../literature.d/LIT-946.md), read in [NOTE-tmpjl88t](../notes.d/NOTE-tmpjl88t.md): at five
  demonstrations, accuracy across draws of examples runs from below 0.1 to
  about 0.6 while final-layer manifold capacity barely moves, and
  consistently swapped labels fail while capacity matches gold labels. The
  readout explanation is inferred from that dissociation, not measured;
  base Llama-3.1-8B and Gemma-2-2B, mostly synthetic data.
---
<!-- inactive-ok-file: CLAIM-029 CLAIM-118 THEORY-tmpgub9t — Proposed; claims and theory this account bears on, open -->

# THEORY-tmp94b56: In few-shot classification by a base language model, failures from the choice of examples or from relabelled categories leave the class representations separable and fail at the vocabulary readout

## Source

Kirsanov, Chou, Cho and Chung (2025), [LIT-946](../literature.d/LIT-946.md), read in full in
[NOTE-tmpjl88t](../notes.d/NOTE-tmpjl88t.md): §4.1 ("Task performance", "Last-token effects",
"Sensitivity to the choice of demonstrations"), Figure 6, and §5.

## What was actually shown

Manifold capacity, P / D* for P classes where D* is the critical
projection dimension for linear separability, measures how separable the
class point clouds are to an ideal linear decoder.

- **Example choice.** With five demonstrations, accuracy over random draws
  of examples runs "from below 0.1 to approximately 0.6". Final-layer
  capacity of the last token changes little, the worst runs still exceed
  the instruction prompt's capacity, and their layer profile is "nearly
  identical" to the best runs (Fig. 6).
- **Relabelled categories.** When labels are consistently swapped ("Joy" →
  "Anger"), accuracy is low on both the new and the original labels, while
  last-token capacity is "similar to the gold label setting".
- **The contrast case.** Letter-code labels lower capacity as well as
  accuracy, so capacity does track some failures.

Each result could have come out the other way: low-accuracy runs could have
had low capacity, as the letter-code case does.

## What this does not say

- **The readout is not measured.** The paper infers misalignment of the
  unembedding from high capacity with low accuracy. It proposes, and does
  not run, the comparison with a trained linear classifier.
- **Not order effects.** Only which examples were drawn was varied, not
  their order, so Lu et al.'s order sensitivity is not explained by this.
- **Not instruction-tuned models.** Base models only.
- **Not open-ended tasks.** Capacity is defined for fixed label sets.
- **Not that the representation is the "real" task state.** High capacity
  means an ideal linear decoder could separate the classes; it does not
  mean the model represents the intended task.

## Connections

No relations are declared.

- **[CLAIM-029](../claims.d/CLAIM-029.md).** Its defeater cites surface-form sensitivity as evidence
  against a stable frame. This account locates one such sensitivity in
  the readout, with the representation the context sets left nearly
  unchanged.
- **[CLAIM-118](../claims.d/CLAIM-118.md).** It adds a third place where interpretation can fail,
  beside context and interpreter: between what is decodable and what the
  model's own decoder reads.
- **[QUESTION-020](../questions.d/QUESTION-020.md).** A receiver whose representation already separates the
  classes and whose readout fails is a case where improving the
  interpreter's readout, not the signal, would recover the loss. The paper
  does not test that.
- **[THEORY-tmpgub9t](THEORY-tmpgub9t.md)**, from the same reading and [LIT-942](../literature.d/LIT-942.md), holds the
  representation-side finding that demonstrations and instructions act
  differently.
