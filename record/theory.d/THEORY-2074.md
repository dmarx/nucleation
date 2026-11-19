---
number: 2074
status: Proposed
formerly:
- THEORY-tmply4g3
title: 'Zhang and colleagues find that ordering pretraining documents from easy to hard by a cheap difficulty measure lets small decoder language models reach a randomly ordered baseline''s best accuracy in substantially fewer steps at the same total tokens, that the gap mostly closes by the end under strict ordering, and that a curriculum phase followed by the baseline''s own shuffled data ends above the baseline'
version: 1
source:
- LIT-2845
tags:
- learning-theory
- representation-learning
date: '2026-11-19'
promote_when: >-
  An independent replication with several seeds, at a stated scale and
  learning-rate schedule, shows that a difficulty-ordered phase reaches a
  shuffled baseline's best accuracy in fewer steps at matched total
  tokens, with the gap narrowing by the end under strict ordering, and
  that a curriculum warm-up followed by the baseline's shuffled
  continuation stays above the token-matched baseline at the end.
bears_on:
- QUESTION-039
summary: >-
  From the reading of [LIT-2845](../literature.d/LIT-2845.md) in [NOTE-2144](../notes.d/NOTE-2144.md). Order within one
  distribution; the warm-up result is the nearest on record to a lasting
  change in later learning rate. Proposed until its promote_when is met.
---

# THEORY-2074: Zhang and colleagues find that ordering pretraining documents from easy to hard by a cheap difficulty measure lets small decoder language models reach a randomly ordered baseline's best accuracy in substantially fewer steps at the same total tokens, that the gap mostly closes by the end under strict ordering, and that a curriculum phase followed by the baseline's own shuffled data ends above the baseline

## The account

At 0.5B on 10B tokens, curricula by compression ratio, MTLD, fertility or document length reach the baseline's best in 18 to 45 per cent fewer steps; strict orderings converge with the baseline by the end. After 10B tokens of curriculum, the same 10B shuffled tokens as the baseline leave the curriculum model 2.6 to 3.5 per cent higher, and about 3.1 per cent at 100B.

## Evidence

Mostly single runs; constant learning rate; zero-shot accuracy of small models.
