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

## Note of 2026-11-19: the scheduling follow-up readings, read
<!-- inactive-ok-file: ARG-tmp30ltz THEORY-tmpf6s7m THEORY-tmpmy98s THEORY-tmpq9sev — Proposed or newly filed; cited from the readings of 2026-11-19 -->

Three readings bear on this account. Stern and colleagues
([THEORY-tmpsewbi](THEORY-tmpsewbi.md); [NOTE-tmph6c5h](../notes.d/NOTE-tmph6c5h.md)) qualify its generality: with a tuned
initialization and matched compute, k-Dyck never beats natural-language-
only training in any of three regimes, and an earlier reported gain shrank
when the baseline's embedding scale was fixed; under this account's own
initialization family the additive gain persists at 1B tokens. They do not
reproduce this setup, so the promote_when is neither met nor defeated;
their point that resetting the optimizer hurts a natural-language control
bears on the matched natural-language first phase here. The procedural-
pretraining paper ([THEORY-tmpmy98s](THEORY-tmpmy98s.md)) is a second, independent instance of a
tiny first phase saving later tokens, without a natural-language first-
phase control, so it does not meet the promote_when either. Papadimitriou
and Jurafsky ([THEORY-tmpf6s7m](THEORY-tmpf6s7m.md)), the predecessor, are in partial tension:
in frozen LSTMs flat crossing pairs transfer as well as nesting, where
this account finds hierarchy crucial; architecture, protocol and measure
all differ. Petty and colleagues ([THEORY-tmpq9sev](THEORY-tmpq9sev.md), shared author) find
large code shares hurt natural-language tasks; with this account's finding
that a first phase can run too long, the pair suggests a short, bounded
dose (the filer's inference). Argued in [ARG-tmp30ltz](../arguments.d/ARG-tmp30ltz.md).

## Note of 2026-11-19: the task-composition readings, read
<!-- inactive-ok-file: THEORY-tmp442o6 THEORY-tmp51mqd — Proposed or newly filed; cited from the readings of 2026-11-19 -->

Zhang, Lepori and Pavlick (THEORY-tmp51mqd) go further on mechanism than
this account's post hoc pruning: the located component alone, transplanted
with size-matched random controls, carries the saving, at toy scale and
without counting the first stage. Furuta and colleagues (THEORY-tmp442o6)
find transplanted grokked modules often raise later cost, a parallel to
this account's harmful first phases.
