---
number: 2034
status: Proposed
formerly:
- THEORY-tmpm09s4
title: 'Meta-learning is optimizing a meta-objective'
statement: >-
  Hospedales, Antoniou, Micaelli and Storkey characterize neural-network
  meta-learning as end-to-end optimization of an explicitly defined
  meta-objective over many learning episodes, so as to improve future
  learning, and order the field on three axes, what is meta-learned, how it
  is optimized and what objective it serves; they name meta-overfitting and
  generalization to task distributions other than the training one as open
  problems
version: 1
source:
- LIT-2796
tags:
- learning-theory
date: '2026-11-19'
bears_on:
- QUESTION-495
promote_when: >-
  The record accepts the survey's characterization and taxonomy as a fair
  map of the field as of 2020: a reading of a second survey or of the
  primary works it cites (MAML, LIT-2816, among them) agrees with its
  definition and with its three axes.
summary: >-
  From the reading of [LIT-2796](../literature.d/LIT-2796.md) in [NOTE-2108](../notes.d/NOTE-2108.md). Hospedales, Antoniou,
  Micaelli and Storkey (2020), arXiv 2004.05439, a survey of meta-learning
  in neural networks. It defines meta-learning as end-to-end optimization
  of an explicit meta-objective over many learning episodes "to improve
  its future learning performance", orders methods by what is meta-
  learned, how and for what objective, and lists meta-overfitting,
  generalization to task distributions other than the training one, and
  the lack of task families as open problems. Here because the owner asked
  at U24 for prior meta-learning literature and A54 named this survey: it
  confirms that meta-learning's objective targets future learning, as
  [QUESTION-495](../questions.d/QUESTION-495.md) and [CLAIM-758](../claims.d/CLAIM-758.md) say, and that every such objective
  presupposes a declared task family. Skimmed (taxonomy, formalization,
  meta-objectives, continual learning, challenges); read in its NOTE.
---
<!-- inactive-ok-file: CLAIM-758 — Proposed; cited in this filing of 2026-11-19 -->
<!-- inactive-ok-file: NOTE-2108 — Skimmed; cited in this filing of 2026-11-19 -->

# THEORY-2034: Meta-learning is optimizing a meta-objective

## The account

The survey separates meta-learning from transfer, multi-task and most
continual learning by the presence of an explicit outer objective that
evaluates learning on held-out data, and formalizes it as bilevel
optimization over a task distribution. Its taxonomy has three axes:
meta-representation (initializations, optimizers, feed-forward models,
losses, architectures and more), meta-optimizer (gradient, RL, evolution)
and meta-objective (sample efficiency, learning speed, asymptotic
performance, robustness, continual retention), and it adds a degree of
amortization between learning paid for in meta-training and learning
done at meta-test. Meta-overfitting is metaknowledge that does not
generalize from source to target tasks; generalization to a different task
distribution and the lack of task families are listed as open.

## What it does not show

Any result of its own; that its taxonomy is the right one. Skimmed:
the application sections were not read, so nothing here rests on them.
