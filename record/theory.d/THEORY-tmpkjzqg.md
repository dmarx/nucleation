---
status: Proposed
title: 'McDermott, Yap, Szolovits and Zitnik propose that pre-training helps a later per-sample task to the degree that the relational structure it induces among sample embeddings agrees with that task: a loss term aligning embeddings to a chosen pre-training graph bounds asymptotic nearest-neighbour fine-tuning accuracy by the task''s local consistency over the graph, matched or improved on language-model and supervised pre-training in fifteen real-domain comparisons, and did worse than language-model pre-training alone with a graph misaligned with the task'
version: 1
source:
- LIT-tmp995ll
tags:
- learning-theory
- representation-learning
date: '2026-11-19'
promote_when: >-
  An independent study with pre-training data and compute held fixed,
  fine-tuning the model and not only probing it, shows fine-tuned
  performance after graph-aligned pre-training rising with the task's
  local consistency over the graph and falling below language-model-only
  pre-training where it is low, and, in a real domain, a gain over a
  matched continued-training control with a graph not built from the fine-
  tuning labels.
corroborates:
- CLAIM-350
- CLAIM-152
summary: >-
  From the reading of [LIT-tmp995ll](../literature.d/LIT-tmp995ll.md) in [NOTE-tmp074zx](../notes.d/NOTE-tmp074zx.md). Cited by ChatGPT for
  the owner's point that pretraining shows acquired organization making
  later learning cheaper; it shows final performance, not cost. Proposed
  until its promote_when is met.
---

# THEORY-tmpkjzqg: McDermott, Yap, Szolovits and Zitnik propose that pre-training helps a later per-sample task to the degree that the relational structure it induces among sample embeddings agrees with that task: a loss term aligning embeddings to a chosen pre-training graph bounds asymptotic nearest-neighbour fine-tuning accuracy by the task's local consistency over the graph, matched or improved on language-model and supervised pre-training in fifteen real-domain comparisons, and did worse than language-model pre-training alone with a graph misaligned with the task

## The account

What pre-training contributes to a later task is the relational structure
it imposes among sample embeddings. Add to a language-model objective a
term that makes two samples' embeddings close exactly when they are
linked in a chosen graph; then a nearest-neighbour classifier on the
embeddings reaches, in the limit of data, at least the task's local
consistency over that graph. A graph defined by class labels caps what
later tasks can get. In proteins, abstracts and protein-interaction
networks the method matched or beat its baselines; in semi-synthetic
data a graph misaligned with the task did worse than language-model
pre-training alone.

## Evidence

A theorem for nearest-neighbour probes in the infinite-data limit; one run
per configuration, significance at p < 0.1; small real-domain gains that
an ablation shrinks; small semi-synthetic models.
