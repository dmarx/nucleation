---
number: 2079
status: Proposed
formerly:
- THEORY-tmprqq7k
title: 'Child-directed curriculum order doesn''t help LMs'
statement: >-
  Feng, Goodman and Frank find that small GPT-2 models trained from scratch
  on about 29M words of child-directed conversation reach about the same
  final syntactic and semantic performance whether conversations come in
  children's age order, in reverse or at random, while shuffling utterances
  within conversations lowers performance on CHILDES, and conclude that the
  developmental curriculum of children's input is not a uniquely valuable
  training signal for language models
version: 1
source:
- LIT-2855
tags:
- learning-theory
- representation-learning
date: '2026-11-19'
promote_when: >-
  An independent study pretraining comparable small models on age-ordered
  child-directed data reproduces, with enough seeds to bound the effect,
  no difference in final syntactic and semantic performance between age-
  ordered, reversed and random global order, together with a measurable
  loss from shuffling utterances within conversations.
summary: >-
  From the reading of [LIT-2855](../literature.d/LIT-2855.md) in [NOTE-2161](../notes.d/NOTE-2161.md). A null for
  developmental order within one corpus, weakly powered. Proposed until
  its promote_when is met.
---

# THEORY-2079: Child-directed curriculum order doesn't help LMs

## The account

Train small language models from scratch on child-directed conversation
ordered by the child's age, reversed, or shuffled: final syntax and
semantics barely differ. Breaking the order of utterances inside each
conversation does hurt. The developmental order of children's input is
not, for these models, a special training signal; local coherence is.

## Evidence

GPT-2 at 124M on about 25M training words, three seeds, heavy
repetition; RoBERTa global-order runs failed to converge.

## Note of 2026-11-19: the scheduling follow-up readings, read
<!-- inactive-ok-file: THEORY-2076 THEORY-2082 THEORY-2083 — Proposed or newly filed; cited from the readings of 2026-11-19 -->

Opper and colleagues ([THEORY-2082](THEORY-2082.md)) agree: developmental or complexity
order barely moves final syntactic scores in small models, and coherent
units matter (sequences beat token blocks). Zhang and colleagues
([THEORY-2074](THEORY-2074.md)) agree for strict ordering within a corpus, and add early
acceleration and warm-up gains. Yıldız and colleagues ([THEORY-2083](THEORY-2083.md))
contrast: across many distinct domains, order changes final perplexity and
forgetting. Feng, Prabhumoye and colleagues ([THEORY-2076](THEORY-2076.md)) share this
account's first author's surname and nothing else; cited with a second
author to keep them apart.
