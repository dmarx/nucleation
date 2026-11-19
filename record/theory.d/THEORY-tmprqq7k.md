---
status: Proposed
title: 'Feng, Goodman and Frank find that small GPT-2 models trained from scratch on about 29M words of child-directed conversation reach about the same final syntactic and semantic performance whether conversations come in children''s age order, in reverse or at random, while shuffling utterances within conversations lowers performance on CHILDES, and conclude that the developmental curriculum of children''s input is not a uniquely valuable training signal for language models'
version: 1
source:
- LIT-tmpdvkoo
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
  From the reading of [LIT-tmpdvkoo](../literature.d/LIT-tmpdvkoo.md) in [NOTE-tmpu1se9](../notes.d/NOTE-tmpu1se9.md). A null for
  developmental order within one corpus, weakly powered. Proposed until
  its promote_when is met.
---

# THEORY-tmprqq7k: Feng, Goodman and Frank find that small GPT-2 models trained from scratch on about 29M words of child-directed conversation reach about the same final syntactic and semantic performance whether conversations come in children's age order, in reverse or at random, while shuffling utterances within conversations lowers performance on CHILDES, and conclude that the developmental curriculum of children's input is not a uniquely valuable training signal for language models

## The account

Train small language models from scratch on child-directed conversation
ordered by the child's age, reversed, or shuffled: final syntax and
semantics barely differ. Breaking the order of utterances inside each
conversation does hurt. The developmental order of children's input is
not, for these models, a special training signal; local coherence is.

## Evidence

GPT-2 at 124M on about 25M training words, three seeds, heavy
repetition; RoBERTa global-order runs failed to converge.
