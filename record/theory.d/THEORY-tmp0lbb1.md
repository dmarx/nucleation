---
status: Proposed
title: 'Bengio, Louradour, Collobert and Weston report that training first on easier examples and then on the target distribution lowers final test error against target-only training in shape recognition, better than unordered training on both sets, and in a neural language model with a growing vocabulary, and propose that a curriculum acts as a continuation method and, on the surface, as a regularizer'
version: 1
source:
- LIT-tmpuo84j
tags:
- learning-theory
date: '2026-11-19'
promote_when: >-
  An independent replication, with hyperparameters tuned for both
  conditions, finds easy-to-hard ordering giving significantly lower final
  test error than both target-only and unordered union training at matched
  budgets on these or comparable tasks.
corroborates:
- CLAIM-756
summary: >-
  From the reading of [LIT-tmpuo84j](../literature.d/LIT-tmpuo84j.md) in [NOTE-tmpk9vq9](../notes.d/NOTE-tmpk9vq9.md). A final-performance
  result in which an earlier step weak on its own belongs to the best
  policy. Proposed until its promote_when is met.
---

# THEORY-tmp0lbb1: Bengio, Louradour, Collobert and Weston report that training first on easier examples and then on the target distribution lowers final test error against target-only training in shape recognition, better than unordered training on both sets, and in a neural language model with a growing vocabulary, and propose that a curriculum acts as a continuation method and, on the surface, as a regularizer

## The account

A curriculum is a sequence of training distributions that reweights the
examples, from easier to the target. Spending part of a fixed budget on
easier shapes first, then on the target, ends with lower error than
spending all of it on the target or on both sets unordered; a language
model whose vocabulary grows ends better though it trails for its first
billion updates. The authors read this as a continuation method, which
optimizes a smoothed objective first, reaching better minima.

## Evidence

Small experiments with seeds averaged; final error only; baseline-tuned
hyperparameters.

## Note of 2026-11-19: the scheduling follow-up readings, read
<!-- inactive-ok-file: THEORY-tmp5jrhv THEORY-tmpshgvo — Proposed or newly filed; cited from the readings of 2026-11-19 -->

Three parallel tests of easy-first ordering. Zhang and colleagues (THEORY-
tmply4g3) find it reaches a random baseline's best in 18 to 45 per cent
fewer steps in language-model pretraining, with the gap mostly closing by
the end under strict ordering and a lasting gain when the curriculum is a
warm-up; constant learning rate, mostly single runs. Opper and colleagues
([THEORY-tmpshgvo](THEORY-tmpshgvo.md)) find sequence-complexity curricula no better than random
at BabyLM scale, and a corpus order only marginally better. Nishida and
colleagues ([THEORY-tmp5jrhv](THEORY-tmp5jrhv.md)) find hard text most aligned mid-training, an
attribution pattern, not a curriculum test. Qualifies: easy first helps
speed more than endpoint.
