---
status: Active
status_note: >-
  Read on 2026-11-23 ([NOTE-tmpw2i45](../notes.d/NOTE-tmpw2i45.md)). Worth reading for the shallow-network
  theory that the work of Anguita and colleagues extends, and for a
  function-preserving rescaling after pretraining that changes what
  fine-tuning learns.
title: 'Inductive biases of multi-task learning and finetuning: multiple regimes of feature reuse'
version: 2
history:
- version: 1
  date: '2026-11-23'
  note: >-
    Filed, not read, by the lead run of 2026-11-23, from the reading of
    Anguita and colleagues (NOTE-2159), which names it as the work its
    theory extends. Not held: no hit for the arXiv id 2310.02396, the
    title or Lippl in record/literature.d. The arXiv API answered "Rate
    exceeded" on 2026-11-23 and was not retried; the identifier, authors,
    dates and venue were checked on the arXiv abstract page instead, no
    email address sent: v1 2023-10-03, v4 2024-10-31, comment "Accepted to
    NeurIPS 2024".
- version: 2
  date: '2026-11-23'
  note: >-
    Read on 2026-11-23 by the lead run from the arXiv HTML of v4. Account
    THEORY-tmpw69kb, with THEORY-tmpfysqg for the deep-network results.
    Summary rewritten.
tags:
- learning-theory
- representation-learning
- anthology-candidate
date: '2026-11-23'
published: '2023-10-03'
arxiv: '2310.02396'
first_author: 'Lippl'
keywords:
- multi-task learning
- finetuning
- implicit regularization
- diagonal linear networks
- nested feature selection
implementations: []
summary: >-
  Lippl and Lindsey (NeurIPS 2024), arXiv 2310.02396. Derives the
  regularization penalties of multi-task learning and of pretraining then
  fine-tuning in diagonal linear and one-hidden-layer ReLU networks: both
  favour reusing pretrained features and learning a sparse set of new
  ones, the two biases trade off exactly ("ℓ-order + FD = 1"), and
  fine-tuning has a "nested feature selection" regime that picks a sparse
  subset of the pretrained features. Rescaling the weights after
  pretraining moves a network between regimes and, in ResNets, improves
  fine-tuning. Registered by the lead run of 2026-11-23 as the precursor
  of Anguita and colleagues ([LIT-2861](LIT-2861.md)). Read in [NOTE-tmpw2i45](../notes.d/NOTE-tmpw2i45.md).
---
<!-- inactive-ok-file: THEORY-tmpw69kb THEORY-tmpfysqg — Proposed; filed by the lead run of 2026-11-23 -->

# LIT-tmpkuq67: Inductive biases of multi-task learning and finetuning: multiple regimes of feature reuse

Lippl and Lindsey (2023; NeurIPS 2024). arXiv 2310.02396.

## Key takeaways

- Pretraining then fine-tuning a two-layer diagonal linear network from
  infinitesimal initialization minimizes a penalty set per dimension by
  the pretrained coefficient and the readout's re-initialization scale:
  ℓ1-like for features pretraining did not use, weighted-ℓ2 for large
  pretrained ones.
- Sparsity and dependence on pretrained features trade off exactly, and
  between the two limits lies a nested feature selection regime, reached by
  rescaling the weights after pretraining.
- In deep networks rescaling by less than 1 improves ResNet fine-tuning on
  CIFAR-100 and ImageNet transfer; Vision Transformers do not benefit.

## Standing in the record

Registered and read on 2026-11-23 ([NOTE-tmpw2i45](../notes.d/NOTE-tmpw2i45.md), [THEORY-tmpw69kb](../theory.d/THEORY-tmpw69kb.md),
[THEORY-tmpfysqg](../theory.d/THEORY-tmpfysqg.md)). Anguita and colleagues ([LIT-2861](LIT-2861.md)) extend its
diagonal-network theory from infinitesimal initialization to arbitrary
absolute and relative scales.
