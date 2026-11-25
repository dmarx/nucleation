---
number: 1904
status: Proposed
formerly:
- THEORY-tmpup4vk
promote_when: >-
  The addition and negation results reproduced by a second group on
  pretrained models and tasks the paper did not use, with the coefficient
  tuned as the paper tunes it and the cost of that tuning reported: one
  model built by adding task vectors from one start comes close to the
  specialised models on all its tasks, and subtracting a task's vector
  removes most of that task's accuracy while a control task loses little.
  It is refuted if, so tuned, added task vectors fall well below the
  specialised models on most task pairs, or negation costs the control
  task about as much as the target.
title: 'Task vectors add and negate task skills'
statement: >-
  Ilharco et al.: for CLIP, GPT-2 and T5 models fine-tuned from one
  pretrained start, adding the weight differences that fine-tuning on
  different tasks produced, scaled by a coefficient tuned on validation
  data, gives one model close to the specialised models on all of the tasks,
  and subtracting a task's difference lowers accuracy on that task with
  little loss on a control task
version: 1
tags:
- loss-landscapes
- representation-learning
- anthology-candidate
date: '2026-11-15'
source:
- LIT-2638
bears_on:
- QUESTION-069
summary: >-
  Ilharco et al. (2023), [LIT-2638](../literature.d/LIT-2638.md), read in [NOTE-1970](../notes.d/NOTE-1970.md). Negation of
  a CLIP ViT-L/14 task vector cut target accuracy by 45.8 points with
  little change on ImageNet; adding eight image tasks' vectors reached
  91.2% normalized accuracy; GPT-2 toxicity and T5 GLUE follow. All within
  one pretrained start, with λ tuned per edit on validation data. The
  paper offers no mechanism: that near-orthogonal task vectors enable
  addition is its speculation. The wording is the reader's; adopting it
  is the owner's call.
---
<!-- inactive-ok-file: THEORY-107 THEORY-1892 THEORY-1874 THEORY-1898 THEORY-1872 THEORY-1890 — new tmp codes, or Proposed; this account's source and reading, and accounts that explain or qualify it, named and not leaned on -->

# THEORY-1904: Task vectors add and negate task skills

## Source

Ilharco, Ribeiro, Wortsman, Gururangan, Schmidt, Hajishirzi & Farhadi
(2023), [LIT-2638](../literature.d/LIT-2638.md), read in [NOTE-1970](../notes.d/NOTE-1970.md): §§1–7 and Appendix A.

## The result

A task vector is τ = θ_ft − θ_pre. An edit is θ + λτ, with λ chosen on
held-out validation data.

- **Negation** (§3.1): CLIP ViT-L/14 target accuracy falls from 64.8 to
  19.0 on average over eight tasks, while ImageNet falls only from 75.5 to
  72.9. A random vector of the same per-layer magnitude does little, and
  gradient ascent destroys the control. GPT-2 Large toxic generations fall
  from 4.8% to 0.8% at a perplexity cost of 16.4 → 16.9 (§3.2).
- **Addition** (§4.1): pairs reach 98.9% normalized accuracy on average,
  and all eight image tasks 91.2%.
- **Ensembles** (App. A): the two-model weight average tracks the logit
  ensemble in accuracy, r = 0.99.

Each could have failed. Fine-tuning is nonlinear in the weights, and
nothing guarantees that the sum of two updates does either task.

## What it does not show

- **Why it works.** The paper suggests near-orthogonal task vectors enable
  addition, as speculation. Orthogonal updates can still interact through
  curvature (A's toy, checked in [NOTE-1970](../notes.d/NOTE-1970.md)). Later work offers
  mechanisms that do not rely on orthogonality: disentanglement in
  function space ([THEORY-1892](THEORY-1892.md)), layer-level overlap of singular
  vectors ([THEORY-1874](THEORY-1874.md)), over-counting of shared directions
  ([THEORY-1898](THEORY-1898.md)), low-frequency amplitude mismatch ([THEORY-1872](THEORY-1872.md))
  and, at the level of features, cross-task linearity ([THEORY-1890](THEORY-1890.md)).
  TIES's sign conflicts are [THEORY-107](THEORY-107.md).
- **That it works without tuning.** λ is chosen on validation data for
  each operation, so the headline numbers include a search.
- **Anything across starts.** The authors operate "only on models
  fine-tuned from the same pre-trained initialization".
- **That addition matches the specialised models.** Normalized accuracy
  of 91.2% for eight tasks is a gap, and it widens as tasks are added.
