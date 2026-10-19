---
status: Open
title: "Does Thresholdout keep every one of m adaptively chosen statistical queries within τ of its true mean, with probability 1 − β, on a holdout whose size grows only logarithmically in m, as Dwork and co-authors' Theorem 11 states?"
version: 1
tags:
- mathematical-statistics
- learning-theory
date: '2026-10-19'
line: 'distributed-agency'
refines:
- QUESTION-040
summary: >-
  Filed when the promotion audit (batch 044, [ADR-047](../decisions.d/ADR-047.md) v2) narrowed and
  promoted THEORY-318 to the two results the record has re-derived:
  max-information bounds the chance of overfitting, and ε-differential
  privacy bounds max-information. The holdout clause, and the former
  promote_when's request for the deferred proofs, are held here.
---

# QUESTION-tmpemkme: Does Thresholdout keep every one of m adaptively chosen statistical queries within τ of its true mean, with probability 1 − β, on a holdout whose size grows only logarithmically in m, as Dwork and co-authors' Theorem 11 states?

## Why it is a question

[THEORY-318](../theory.d/THEORY-318.md) now states what the Supplementary Material of [LIT-964](../literature.d/LIT-964.md) proves
and the record has re-derived: a bound k on the max-information between a
dataset and an analyst's chosen statistic multiplies the chance that the
statistic overfits by at most 2^k, and ε-differential privacy keeps k at
most log₂e·εn. That bound alone needs ε of order τ² over the whole
interaction, too strict to reuse a holdout at useful sizes. Reuse rests on
the sharper transfer theorems (Theorems 6 and 8), on Thresholdout's
privacy (Lemma 10), and on its accuracy guarantee (Theorem 11), whose
proofs are in the companion papers (arXiv:1411.2664, arXiv:1506.02629).
[NOTE-848](../notes.d/NOTE-848.md) read their statements, not their proofs, and the Science main
text was not reached.

## What would answer it

A reading of the proofs of Theorems 6, 8 and 11 and Lemma 10 in the
companion papers, confirming the bounds as stated, would answer it yes.
An ε-differentially private mechanism and an adaptive analyst for which
the chosen statistic's empirical mean exceeds its true mean by τ with
probability above the stated bound would answer it no. Simulations in
which a reused holdout does or does not overfit cannot settle it: the
claim is a worst case over all analysts, and the simulated implementation
is not the analysed algorithm.
