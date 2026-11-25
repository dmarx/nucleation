---
number: 2082
status: Proposed
formerly:
- THEORY-tmpshgvo
title: 'Complexity curricula don''t help BabyLM grammar'
statement: >-
  Opper, Morrison and Siddharth find that a small masked language model
  trained for a fixed step budget on the BabyLM strict-small corpora
  acquires grammar, as BLiMP measures it, no better under
  sequence-complexity curricula than under random sampling, better on
  transcribed speech alone than on text alone, and only marginally better
  under a simple-to-complex corpus order than under random sampling
version: 1
source:
- LIT-2857
tags:
- learning-theory
- representation-learning
- linguistics
date: '2026-11-19'
promote_when: >-
  An independent study at comparable scale, with enough seeds to bound the
  effects, reproduces at a fixed step budget that speech-only training
  beats text-only on BLiMP, that complexity-ordered curricula give no
  significant gain over random sampling on the BabyLM corpora, and that a
  simple-to-complex corpus order gains at most marginally over random
  sampling.
summary: >-
  From the reading of [LIT-2857](../literature.d/LIT-2857.md) in [NOTE-2146](../notes.d/NOTE-2146.md). A weak, mostly
  negative check on curricula in small language models, beside
  THEORY-2079. Proposed until its promote_when is met.
---

# THEORY-2082: Complexity curricula don't help BabyLM grammar

## The account

At 120k steps, curricula ordered by entropy, unigram probability or block
size do not beat random sampling. Speech alone beats text alone. Ordering
corpora from child-directed speech to Wikipedia beats the reverse by about
two points and random sampling by under one; on a text-heavy control it
gains slightly. The authors credit random sampling's strength to the share
of steps short speech lines take.

## Evidence

Three seeds, no tests; one model size; steps fixed, tokens not.
