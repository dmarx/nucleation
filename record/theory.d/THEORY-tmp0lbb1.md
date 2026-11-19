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
  From the reading of LIT-tmpuo84j in NOTE-tmpk9vq9. A final-performance
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
