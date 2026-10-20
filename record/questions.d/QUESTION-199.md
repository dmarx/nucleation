---
number: 199
status: Open
formerly:
- QUESTION-tmp322q5
title: "Does the training fraction at which networks summing two learned embeddings generalise follow the fraction at which the training set's same-answer equations leave only translation and scale free, across group sizes?"
version: 1
tags:
- representation-learning
- learning-theory
date: '2026-10-19'
line: 'learned-structure'
refines:
- QUESTION-058
summary: >-
  Filed when the promotion audit (batch 043, [ADR-047](../decisions.d/ADR-047.md) v2 and v3) narrowed
  and promoted [THEORY-181](../theory.d/THEORY-181.md) to the zero-loss injective model and to the one
  size Liu et al. measured. The former promote_when asked for the
  multi-size test; this question holds it.
---

# QUESTION-199: Does the training fraction at which networks summing two learned embeddings generalise follow the fraction at which the training set's same-answer equations leave only translation and scale free, across group sizes?

## Why it is a question

[THEORY-181](../theory.d/THEORY-181.md) now states two things. The first is a theorem: in a model that
decodes the sum of two learned embeddings, at zero training loss with an
injective decoder, a training set whose same-answer equations have nullity
2 fixes the embeddings to E_k = a + kb. The second is one measurement:
for non-modular addition with p = 10 and one-dimensional embeddings,
Liu et al. ([LIT-858](../literature.d/LIT-858.md), [NOTE-662](../notes.d/NOTE-662.md)) find that the probability of nullity 2
jumps near a training fraction of 0.4, and that trained networks take
diverging time to form the structure at the same fraction. That is one
size and one embedding dimension. Whether the thresholds stay together as
p grows is what would make the counting argument an account of the
critical training fraction, and not a coincidence at one size.

## What would answer it

Run the same toy, two learned embeddings summed and decoded with addition
hard-coded, at several group sizes p. For each training set, report the
nullity of the linear system its same-answer pairs impose, and whether the
trained network generalises. It is answered yes if, at every p, full
generalisation occurs with high probability exactly on training sets of
nullity 2, and the empirical critical fraction follows the fraction at
which nullity 2 becomes likely. It is answered no by networks in that
setting that generalise fully on training sets of nullity above 2, or by a
critical fraction that departs from the nullity threshold as p grows. More
single-size runs, or pictures of structured embeddings in larger models,
are the wrong kind of evidence: they show structure, not that the training
set's equations are what fix it.
