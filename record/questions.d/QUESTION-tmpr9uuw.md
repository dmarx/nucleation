---
status: Open
title: 'Does raising or holding below threshold one relation''s subject–object co-occurrences in pretraining, with the rest of the corpus unchanged, make its LRE causality cross 0.9 or fail to, and is the threshold, with its spread, recovered across more model sizes and families?'
version: 1
tags:
- representation-learning
date: '2026-10-30'
line: learned-structure
summary: >-
  The promotion condition formerly on [THEORY-269](../theory.d/THEORY-269.md), moved here when the
  status review of 2026-10-30 promoted it under [ADR-065](../decisions.d/ADR-065.md). Merullo et al.
  measured a correlation in three models and say they can draw neither
  causal claims nor conclusions about scale from it.
---

# QUESTION-tmpr9uuw: Does raising or holding below threshold one relation's subject–object co-occurrences in pretraining, with the rest of the corpus unchanged, make its LRE causality cross 0.9 or fail to, and is the threshold, with its spread, recovered across more model sizes and families?

## Why it is a question

[THEORY-269](../theory.d/THEORY-269.md) reports Merullo et al. ([LIT-972](../literature.d/LIT-972.md), read in [NOTE-786](../notes.d/NOTE-786.md)): across 24
factual relations in three models, how well an affine map reproduces a
relation tracks how often its subjects and objects co-occur in
pretraining, with a threshold count per model. The authors: "We can not
draw causal claims about how exposure affects individual representations"
(Appendix A), and they "cannot draw conclusions from only three models".
Whether exposure makes the relation linear, or frequent facts are easy for
some other reason, is open.

## What would answer it

An intervention, not a further correlation. Either of two kinds would do.
One is a pretraining run in which one relation's subject–object
co-occurrences are raised above, or held below, the threshold while the
rest of the corpus is unchanged, with that relation's LRE causality
crossing 0.9 or failing to. The other is the threshold recovered, with its
spread, across more model sizes and families. The exposure account fails if
relations held below the threshold become linear as reliably as those
above it, or if co-occurrence stops predicting causality once few-shot
accuracy and subject and object frequency are controlled for. More
correlations on the same relations cannot settle it, since they cannot
separate exposure from whatever makes facts both frequent and easy.
