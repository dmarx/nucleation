---
number: 113
status: Active
formerly:
- THEORY-tmpm7dzo
title: 'Merging ResNets trained from different initialisations on disjoint halves of a label set by permuting one onto the other and averaging fell far short of the ensemble; their cross-model feature correlation fell with depth, merging only the early layers recovered most of the ensemble''s accuracy, and merging features within each model as well as across both helped at 4× width and above; Stoica et al. attribute the failure to features with no counterpart in the other model'
version: 2
history:
- version: 2
  date: '2026-10-29'
  note: >-
    Narrowed and promoted by the eleventh status review (ADR-057;
    ADR-047's evidence ruling). Stoica et al. was read in full (NOTE-523).
    The title now reports what was measured and gives the no-counterpart
    explanation as the authors', since no same-task control separates
    task difference from depth. The old title: Merging models trained on
    different tasks from different initialisations fails where their
    features have no counterpart in the other model, and such features
    grow more common with depth. The promote_when moves unchanged to
    QUESTION-tmp32xm6, as THEORY-114's did to QUESTION-312.
tags:
- loss-landscapes
- representation-learning
- anthology-candidate
date: '2026-10-03'
source:
- LIT-665
summary: >-
  Stoica et al. (2023), [LIT-665](../literature.d/LIT-665.md), merge ResNets trained from different
  initialisations on disjoint label sets. Permute-then-average fails, which
  they explain by the permuted model lying in a basin for its own task
  only. Mean cross-model feature correlation falls with depth (0.50, 0.37,
  0.27 at three depths). Merging only the early layers and keeping later
  layers as task heads recovers most of the ensemble's accuracy. Merging
  features within one model as well as across both helps once the models
  are wide enough to hold redundant features. With full merging on
  ImageNet-1k, ZipIt! is no better than permutation (8.6%). No same-task
  control separates the effect of task difference from that of depth;
  that is QUESTION-tmp32xm6.
supports:
- CLAIM-187
- CLAIM-263
bears_on:
- QUESTION-tmp32xm6
---
<!-- inactive-ok-file: THEORY-116 THEORY-107 — Proposed; accounts named in Connections, nothing here rests on them -->

# THEORY-113: Merging ResNets trained from different initialisations on disjoint halves of a label set by permuting one onto the other and averaging fell far short of the ensemble; their cross-model feature correlation fell with depth, merging only the early layers recovered most of the ensemble's accuracy, and merging features within each model as well as across both helped at 4× width and above; Stoica et al. attribute the failure to features with no counterpart in the other model

## Source

- Stoica, Bolya, Bjorner, Ramesh, Hearn & Hoffman (2023), [LIT-665](../literature.d/LIT-665.md),
  read in [NOTE-523](../notes.d/NOTE-523.md): §§3–5, Tables 1–5, Fig. 7, Appendices A, C, D
  and G.

## What was actually shown

**Permutation assumes a counterpart for every feature.** Stoica et al.
merged two models with the same architecture, trained from different
initialisations on disjoint halves of a label set. Merging by permutation
maps each feature of one model to exactly one feature of the other. Their
argument is that models trained on different tasks need not have learned
the same features, so the permuted model lies in a low-loss basin for its
own task but not for the other ([LIT-665](../literature.d/LIT-665.md), §3, Fig. 2). On CIFAR-10
split 5+5, with ResNet-20 at 4× width and joint 10-way accuracy, Git
Re-Basin's merge reaches 46.2. The paper's permutation baseline reaches
58.4, and the ensemble 87.4 (Table 1a).

**Correspondence falls with depth.** For ResNet-20 at 8× width on CIFAR-100
split 50+50, the mean correlation between the two models' features at
layers 7, 13 and 19 of 20 is 0.50, 0.37 and 0.27 (App. A, Table 5). The
authors tie this to Kornblith et al.'s finding that layers grow more
dissimilar with depth. Merging only the early layers, and passing the
merged features to each model's own remaining layers as task heads,
recovers most of the ensemble. On CIFAR-10 that is 83.8 joint at 13 of 20
layers. On ImageNet-1k split 200+200 with ResNet-50, it is 60.9 at 10 of
50 layers against 63.3 for the ensemble (Table 2).

**Unmatched features can be merged with their own duplicates.** ZipIt!
pairs the most correlated features anywhere in the two models' combined
features, within one model as well as across both. Restricted to
cross-model pairs it reduces to permute-then-average. Fully merged on
CIFAR-10 it reaches 79.1, against 58.4 for permutation (Table 1a). The
gain needs width. On CIFAR-100, below 4× width ZipIt! equals permutation;
above it, ZipIt! rises towards the ensemble while permutation plateaus
near 45% (Fig. 7b). On ImageNet-1k at 1× width, full merging gives 8.6
for both (Table 2). Their Theorem 1 states the same in a random two-layer
setting. With a fraction Γ of redundant units, the barrier bound of
Entezari et al. shrinks by (1 − 2Γ)^(1/(2d+4)) and is zero for Γ ≥ 0.5
(App. G).

## What this does not say

- **It does not separate task from depth.** There is no same-task control
  for Table 5. Kornblith et al.'s depth effect is a same-task finding, so
  correspondence may fall with depth whether or not the tasks differ. The
  title reports the fall and the authors' attribution, not that the task
  difference adds to it; whether it does is [QUESTION-tmp32xm6](../questions.d/QUESTION-tmp32xm6.md).
- **The full-merge numbers depend on a shared output space.** The CIFAR
  models are trained with a CLIP-style loss onto text embeddings of class
  names, so their outputs live in one space. With cross-entropy heads,
  full merging falls below each original model for every method (App. D).
- **The merge through ReLU is linear.** Merging and unmerging pass through
  nonlinearities as if they were linear, which App. C admits is an
  approximation. Some of the loss attributed to missing counterparts may
  be this approximation.
- **The theorem is for random two-layer networks.** Its transfer to
  trained deep networks rests on Fig. 7b's width trend.
- **It says nothing about models from one pretrained start**, which the
  paper explicitly leaves.

## Connections

- **[THEORY-107](THEORY-107.md)** is the other half of the question "why does
  merging lose accuracy?". For models fine-tuned from one pretrained start
  it locates the loss in parameter coordinates, redundant updates and sign
  conflicts, with no alignment step at all. This account locates it in
  features, for models with no shared start. They are filed apart because
  their settings, evidence and refuting results differ. Neither tests the
  other's regime, so they are not rivals. ZipIt!'s open question, whether
  within-model merging helps from a shared start, is where they would
  meet.
- **[THEORY-116](THEORY-116.md)** says a barrier left after alignment marks a
  difference in the attributes the models rely on. Disjoint-task models
  are such a case by construction. Their surviving barrier, and the
  failure of a one-to-one matching to remove it, are what that account
  predicts. This account adds where in depth the difference sits.
- **[THEORY-112](THEORY-112.md)**, filed alongside this one, found the barrier left
  after weight matching falling with width. Here
  width helps a different way: by giving each model redundant features to
  merge with themselves, not by making a one-to-one matching exist.
- **Practice across the boundary.** The anthology's [ANTH-SOTA-217](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/practices.d/SOTA-217.md) (align
  permutations before averaging) is narrowed by this result to models
  that learned the same features. For models trained on disjoint tasks,
  alignment by permutation is the wrong transformation.
