---
status: Proposed
title: 'Li and Webb report that in small transformers and attention-free MLPs trained from scratch on in-context ABA/ABB completion with arbitrary tokens, a swappable token-invariant rule representation develops according to training-data diversity (vocabulary, rules, examples, role-token bias), not according to the architectural features tested, and that at small vocabularies it arrives well after the task is solved'
version: 1
source:
- LIT-tmpqgxkn
tags:
- representation-learning
- learning-theory
date: '2026-11-19'
bears_on:
- QUESTION-392
- QUESTION-tmpex36a
corroborates:
- CLAIM-567
promote_when: >-
  A replication with a random-initialization or untrained control at
  matched width, and with architecture crossed with diversity at low
  diversity, that finds the flip rate tracks diversity and not
  architecture.
summary: >-
  Li and Webb (LIT-tmpqgxkn), read in NOTE-tmp70cux. The flip rate of a
  mean-difference rule vector is 0% at vocabulary 50, 5% at 100 and close
  to 100% from 500; at vocabulary 100 it goes from 5% with 2 rules to 95%
  with 10, and from 98% to near 0% as role-token bias rises, while every
  model still generalizes in distribution. At vocabularies of 100 or less
  the 12-layer model first solves the task without it and acquires it
  long after convergence. Ablated transformers and a pure MLP reach 90–100%
  at vocabulary 10k. The mechanism in the MLP is unidentified, and there
  is no random-network control.
---

# THEORY-tmpmtmq7: Li and Webb report that in small transformers and attention-free MLPs trained from scratch on in-context ABA/ABB completion with arbitrary tokens, a swappable token-invariant rule representation develops according to training-data diversity (vocabulary, rules, examples, role-token bias), not according to the architectural features tested, and that at small vocabularies it arrives well after the task is solved

## The account

Li and Webb (LIT-tmpqgxkn) measure a symbolic mechanism by intervention.
They take the mean residual activation for each rule at the position
where the rule is decided, add the difference, and count how often the
output becomes the other rule's answer. That flip rate rises with
vocabulary size, the number of rules and the number of examples, and
falls with role-token bias, while models keep solving the task in
distribution. Every architecture tested reaches it at high diversity,
including an MLP without attention. At small vocabularies a first,
non-symbolic but generalizing solution comes before it.

## What it does not show

That architecture is irrelevant: it was varied only at the highest
diversity, and it changes how fast the representation appears. That the
MLP holds a role representation and not a whole-state rule direction: its
intervention acts on the whole flattened state, and the authors leave the
mechanism open. That the late phase is grokking: the first phase
generalizes.

## Bearing

It corroborates CLAIM-567: which of two feasible solutions training
reaches, and when, is set by data and capacity. It bears on QUESTION-392
as a learned case where data makes a representable capability reached.
It bears on QUESTION-tmpex36a, the owner's hunch, by leaving the unit level
open.
