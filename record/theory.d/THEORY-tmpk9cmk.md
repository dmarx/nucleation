---
status: Proposed
title: 'Hu, Petty, Shi, Merrill and Linzen report that a short first phase of training on a formal language with hierarchical dependencies, before natural-language pretraining, lowers the natural-language tokens a transformer needs to reach a given loss, counting the first phase''s tokens, by a third at 1B parameters against no first phase; that the copy language and random strings raise that cost; and that attention heads found by pruning after the first phase remain more important than random heads after natural-language training'
version: 1
source:
- LIT-tmpzv4og
tags:
- learning-theory
- representation-learning
date: '2026-11-19'
promote_when: >-
  An independent replication at a stated scale finds that a hierarchical
  formal-language first phase reaches a no-first-phase baseline's natural-
  language loss with fewer total tokens including the first phase, that a
  non-hierarchical first phase does not, and that the pruned first-phase
  heads outperform random heads under ablation after natural-language
  training.
corroborates:
- CLAIM-756
bears_on:
- QUESTION-039
summary: >-
  From the reading of [LIT-tmpzv4og](../literature.d/LIT-tmpzv4og.md) in [NOTE-tmpm4pxy](../notes.d/NOTE-tmpm4pxy.md). An earlier
  acquisition lowering a later one's cost, the earlier cost counted.
  Proposed until its promote_when is met.
---

# THEORY-tmpk9cmk: Hu, Petty, Shi, Merrill and Linzen report that a short first phase of training on a formal language with hierarchical dependencies, before natural-language pretraining, lowers the natural-language tokens a transformer needs to reach a given loss, counting the first phase's tokens, by a third at 1B parameters against no first phase; that the copy language and random strings raise that cost; and that attention heads found by pruning after the first phase remain more important than random heads after natural-language training

## The account

Train a transformer briefly on bracket languages (k-Dyck, k-Shuffle Dyck)
before ordinary language-model pretraining, and it reaches a given
natural-language loss with fewer total tokens, first phase included. The
copy language and random strings do the opposite, so structure, not any
first phase, matters, and a first phase can run too long. A matched
natural-language first phase gets much of the same saving. Heads found by
pruning after the first phase remain important at the end.

## Evidence

Pythia-architecture models at 160M and 1B; one 1B run; a restarted
warmup in all two-phase arms; post-hoc ablation for mechanism.
