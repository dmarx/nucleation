---
number: 39
status: Proposed
formerly:
- THEORY-tmpo40cr
promote_when: >-
  What would settle it is one training setting instrumented, in the same
  runs, with every quantity these works use: a mechanistic progress measure,
  the eNTK distance, per-layer gradient SNR, the weight norm and spectrum,
  and I(X;T) under a noise model that belongs to the network rather than to
  the analyst. It would have to report where each transition falls and what
  each later phase does. A new paper with one more phase sequence, measured
  in one more quantity, cannot settle it, since that is the kind of evidence
  that produced the disagreement. The claim is refuted if such a study
  finds the later phases to be one process seen through different
  instruments. One example would be Nanda's cleanup and Prakash & Martin's
  collapse both following the weight norm across a single optimum. It is
  also refuted by a later phase in which I(X;T), under network-intrinsic
  noise, falls and tracks generalisation across nonlinearities and
  optimisers.
title: 'The later phases reported in neural-network training differ in kind: after the transition a network may simplify its weights, acquire item-specific information, lose generalisation, confine its tangent kernel or saturate its units, and none of these is a measured compression of I(X;T)'
version: 1
tags:
- learning-theory
- representation-learning
- information-theory
date: '2026-09-30'
source:
- LIT-345
- LIT-371
- LIT-372
- LIT-369
- LIT-370
summary: >-
  Nanda et al. (2023), [LIT-345](../literature.d/LIT-345.md), Zucchet et al. (2025), [LIT-371](../literature.d/LIT-371.md), Saxe
  et al. (2018), [LIT-372](../literature.d/LIT-372.md), Prakash & Martin (2025), [LIT-369](../literature.d/LIT-369.md), and
  Zhou et al. (2025), [LIT-370](../literature.d/LIT-370.md), each report training as a sequence of
  phases. Their phases are defined by different quantities and fall at
  time scales from 10² to 10⁷ steps. What follows the transition differs in
  kind from work to work. Two of them, the two with a mechanistic
  intervention, show a circuit forming while the loss is flat. Only one
  measures I(X;T), and there the later fall belongs to the estimator. This
  is the record's synthesis across the five, not a claim any of them makes.
---

# THEORY-039: The later phases reported in neural-network training differ in kind: after the transition a network may simplify its weights, acquire item-specific information, lose generalisation, confine its tangent kernel or saturate its units, and none of these is a measured compression of I(X;T)

## Source

- Nanda et al. (2023), [LIT-345](../literature.d/LIT-345.md), §5.2, App. C.2, D.1, as read in [NOTE-283](../notes.d/NOTE-283.md).
- Zucchet et al. (2025), [LIT-371](../literature.d/LIT-371.md), §§2.1–2.2, App. D, as read in [NOTE-319](../notes.d/NOTE-319.md).
- Saxe et al. (2018), [LIT-372](../literature.d/LIT-372.md), §§2, 4, App. C, E, I, as read in [NOTE-320](../notes.d/NOTE-320.md).
- Prakash & Martin (2025), [LIT-369](../literature.d/LIT-369.md), Figs. 1, 4–6, Tables 1–2, as read in [NOTE-317](../notes.d/NOTE-317.md).
- Zhou et al. (2025), [LIT-370](../literature.d/LIT-370.md), Figs. 3–6, as read in [NOTE-318](../notes.d/NOTE-318.md).

## What was actually shown

Each work divides training into phases. None of them compares its phases with the others'.

| Work | Phases, and the quantity that defines them | What the later phase does |
|---|---|---|
| [LIT-345](../literature.d/LIT-345.md) | Memorisation → circuit formation → cleanup; restricted and excluded loss on a known Fourier algorithm, 10³–10⁴ epochs | Simplifies the weights. The weight norm falls and Fourier sparsity rises, and test loss drops |
| [LIT-371](../literature.d/LIT-371.md) | Marginals → plateau → knowledge; attribute loss against an exact entropy baseline | Acquires information. The model comes to tell individuals apart and stores their attributes |
| [LIT-369](../literature.d/LIT-369.md) | Pre-grokking → grokking → anti-grokking; train and test accuracy, 10⁵–10⁷ steps | Loses generalisation. Test accuracy halves, and the weight spectrum concentrates (α < 2, outlier eigenvalues) |
| [LIT-370](../literature.d/LIT-370.md) | Chaos → cone; basin sensitivity and eNTK cosine distance, 10²–10³ iterations | Confines the dynamics. The basin is fixed, and the kernel moves only within a narrow angle |
| [LIT-372](../literature.d/LIT-372.md) | Drift → diffusion in gradient SNR; rise then fall of binned I(X;T), tanh only | Saturates tanh units, which binning reads as lower entropy. The SNR drop is generic near any minimum |

**A shared feature, in two works only.** Both works with a mechanistic intervention find a circuit forming while the loss is flat. In [LIT-345](../literature.d/LIT-345.md) it forms while train and test loss stay flat. Ablating its frequencies, or keeping only them, confirms the circuit. In [LIT-371](../literature.d/LIT-371.md) it forms during the plateau, and patching in post-plateau attention patterns removes the plateau. In [LIT-345](../literature.d/LIT-345.md) the circuit forms after memorisation and generalisation follows the cleanup. In [LIT-371](../literature.d/LIT-371.md) the circuit forms before the item-specific learning it enables ([NOTE-319](../notes.d/NOTE-319.md)). [LIT-370](../literature.d/LIT-370.md)'s early settling of the kernel is of the same shape, but it is measured in a different quantity with no intervention on structure. [LIT-369](../literature.d/LIT-369.md) and [LIT-372](../literature.d/LIT-372.md) measure no circuit.

**No later phase is IB compression.** Of the five, only [LIT-372](../literature.d/LIT-372.md) measures I(X;T). There its fall occurs only for double-saturating units under an imposed binning, and full-batch GD shows it as SGD does ([THEORY-035](THEORY-035.md)). The other four measure no information quantity. In [LIT-371](../literature.d/LIT-371.md) the later phase must *raise* the information the recall position carries about the named individual. That is the reader's inference in [NOTE-319](../notes.d/NOTE-319.md), not a measurement. The later phases of [LIT-345](../literature.d/LIT-345.md) and [LIT-369](../literature.d/LIT-369.md) are "simplifications" of the weights, and they point in opposite directions. One comes with generalisation, the other with its loss, under WD = 0 ([NOTE-317](../notes.d/NOTE-317.md)).

## What this does not say

- **That training has no general phase structure.** The five works use different tasks, architectures, optimisers, regularisers and time scales. The differences here may belong to those settings rather than to training. The claim is that the record's evidence shows no shared later phase, not that none exists.
- **That the five transitions are the same event.** They range from 10² iterations ([LIT-370](../literature.d/LIT-370.md)) to 10⁶ steps ([LIT-369](../literature.d/LIT-369.md)). No work measures another's quantity, so whether any two coincide is open.
- **That the circuit-under-a-flat-loss pattern is general.** It rests on one synthetic algorithmic task and one synthetic factual-recall task. Both are small transformers, and the phase boundaries in [LIT-345](../literature.d/LIT-345.md) are drawn by eye.
- **That [LIT-369](../literature.d/LIT-369.md)'s diagnostics hold.** Its own weight-decay control shows α < 2 with traps and no collapse. It is cited here only for the accuracy phases and the direction of the spectral change.
- **That no network discards input information.** [LIT-372](../literature.d/LIT-372.md) §5 finds task-irrelevant information discarded *during* fitting, not in a later phase.

## Connections

- [THEORY-035](THEORY-035.md) rejects the IB account of a later compression phase. This document generalises its negative finding across the record's other phase sequences, without depending on it. Neither relation is declared, because this claim is about the phase literature, not about the mechanism that document rejects.
- [LIT-324](../literature.d/LIT-324.md) ([NOTE-298](../notes.d/NOTE-298.md)) is the origin of the drift → diffusion and fitting → compression picture. [LIT-341](../literature.d/LIT-341.md) ([NOTE-287](../notes.d/NOTE-287.md)) is the grokking phenomenon behind [LIT-345](../literature.d/LIT-345.md) and [LIT-369](../literature.d/LIT-369.md). [LIT-348](../literature.d/LIT-348.md) names the noise scale that the gradient-SNR transition precedes.
