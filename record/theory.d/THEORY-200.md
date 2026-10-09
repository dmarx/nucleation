---
number: 200
status: Proposed
formerly:
- THEORY-tmpvxccc
promote_when: >-
  A result in which the two invariances could have come apart and did not,
  or a test outside the synthetic model. For instance: a sparse
  hierarchical model whose displacement probabilities are non-uniform, or
  whose displaced and synonymous variants carry different label statistics,
  with the training-set sizes at which synonym invariance, displacement
  invariance and low test error arrive tracked separately and found to
  follow the detection threshold of each; or a measurement on natural
  images in which sensitivity to swapping low-level parts (for instance
  parts resampled by a diffusion model) and sensitivity to small
  deformations both fall at the training-set size at which test error
  does. Further collapses of SRHM learning curves at other s, L or s0
  cannot settle it, because in that model displaced and synonymous
  variants share their parent's statistics by construction.
title: 'On sparse hierarchical data, deep networks become insensitive to swapping synonymous parts and to small displacements of informative features at the training-set size at which they learn the task'
version: 1
tags:
- learning-theory
- compositionality
- representation-learning
date: '2026-10-09'
source:
- LIT-880
summary: >-
  Tomasini and Wyart (2024), [LIT-880](../literature.d/LIT-880.md): measured for locally connected,
  convolutional and fully connected networks on the Sparse Random
  Hierarchy Model with s ≤ 3 and L ≤ 3, with thresholds for the two
  sensitivities tuned per setting; the sample size is about
  (s0 + 1)^L n_c m^L times s^(L/2) without weight sharing, with a one-step
  argument for the (s0 + 1)^L, and about (s0 + 1)^2 n_c m^L with it,
  unexplained. Both invariances keep the parent's label statistics by
  construction, so the model shows that trained networks do the grouping,
  not that the invariances could not separate, and the extension to
  images is an analogy.
---
<!-- inactive-ok-file: THEORY-195 THEORY-186 QUESTION-025 — Proposed or open; cited as the account this one extends and those it is set beside -->

# THEORY-200: On sparse hierarchical data, deep networks become insensitive to swapping synonymous parts and to small displacements of informative features at the training-set size at which they learn the task

## Source

Tomasini and Wyart (2024; ICML 2024, PMLR 235), [LIT-880](../literature.d/LIT-880.md), Eqs. 3–8
and 12, Figs. 1, 4–17, Appendices A–G, as read in [NOTE-684](../notes.d/NOTE-684.md).

## What was actually shown

**The data.** The Random Hierarchy Model of [LIT-877](../literature.d/LIT-877.md) with an uninformative
symbol: each of the s informative children of a symbol sits in its own
sub-patch of s0 + 1 positions, at a position drawn independently, with
empties elsewhere, and empties rewrite to empties. Inputs have
d = (s(s0 + 1))^L positions of which s^L carry a one-hot feature. The label
is unchanged when a feature moves within its sub-patch (a discretised
deformation) and when a tuple is swapped for a synonym.

**The measurements.** Networks with L hidden layers whose filters match the
tree, trained by SGD, reach 10% test error at P* ≈ s^(L/2)(s0 + 1)^L n_c m^L
without weight sharing and P* ≈ C(s0 + 1)^2 n_c m^L with it, at maximal m
(Figs. 4, 10, 13); a second placement rule gives the same (Figs. 7, 8). The
training-set sizes at which the second layer's sensitivity to synonym
swaps, and to displacements, fall below a threshold match P* across L, v, s
and s0, for locally connected, convolutional and fully connected networks
(Figs. 6, 11, 14, 16), with invariance to level-l changes appearing from
layer l + 1 at all levels together (Figs. 12, 15). Across seven
architectures on one instance, test error rises with both sensitivities
(Figs. 1C–F, 17). Each of these could have come out otherwise: sparsity
could have cost an exponential number of examples in d, or one invariance
could have arrived well before the other or before the task was learned.

**The argument.** Displaced and synonymous variants of a part share their
parent and so their class statistics; grouping lower-level patterns by
those statistics removes both kinds of variation at once. In a locally
connected network each first-layer weight sees one position, informative
in a fraction (s0 + 1)^(−L) of the data, so the first gradient step is the
non-sparse one with that fraction of the data (Appendix C, Eq. 12, exact
for an infinitely wide network with a fixed Gaussian readout and uniform
initial weights); the
correlation threshold n_c m^L of [THEORY-195](THEORY-195.md) then scales by (s0 + 1)^L.

## What this does not say

- **Not that the two invariances are bound together in general.** In the
  model they share the parent's statistics by construction, so one grouping
  removes both. What was tested is that trained networks perform that
  grouping, and at the size at which they learn.
- **Not a precise coincidence.** The thresholds for the two sensitivities
  were chosen per setting from the curves' shapes, and agreement is read on
  log–log scatter plots over about two decades.
- **Not an account of weight sharing's cost.** The (s0 + 1)^2 for CNNs is
  measured, not derived, and the one-step argument does not give it.
- **Not a result about images.** The CIFAR-10 correlation between
  deformation stability and error is reproduced in shape on the synthetic
  task; synonym sensitivity was not measured on images, and the discrete
  displacement of one-hot features among empties is not a smooth
  deformation of a dense signal.
- **Not about hierarchies of attributes**, and so not about [QUESTION-025](../questions.d/QUESTION-025.md):
  the hierarchy is part–whole, and there is no co-occurrence embedding,
  attribute or linear direction.
- **Not an instruction.** It says when invariance is acquired, not how to
  train or which architecture to choose.

## Connections

It extends [THEORY-195](THEORY-195.md) from dense to sparse data: the same correlation
threshold, diluted by the informative fraction for locally connected
networks, with a second invariance arriving alongside the first. It is the
learned counterpart of the deformation-stability prior that the
geometric-deep-learning blueprint ([LIT-319](../literature.d/LIT-319.md)) builds into architectures. Like
[THEORY-195](THEORY-195.md), it is about training-set size, not the training-time stages of
[THEORY-186](THEORY-186.md).
