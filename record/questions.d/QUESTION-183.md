---
number: 183
status: Open
formerly:
- QUESTION-tmpvw33h
title: 'Does the spectral contrastive guarantee hold off a finite augmentation space, and is it non-vacuous on a real augmentation graph?'
version: 1
tags:
- representation-learning
- learning-theory
date: '2026-10-19'
line: 'pragmatic-transport'
refines:
- QUESTION-052
summary: >-
  Filed when the promotion audit (batch 037, [ADR-047](../decisions.d/ADR-047.md) v2) narrowed and
  promoted [THEORY-228](../theory.d/THEORY-228.md) to HaoChen et al.'s guarantee on a finite
  augmentation space, re-derived step by step. Its former promote_when
  asked for two further results, and this question holds both: a proof
  off a finite space, and a measurement showing the bound is non-vacuous.
---

# QUESTION-183: Does the spectral contrastive guarantee hold off a finite augmentation space, and is it non-vacuous on a real augmentation graph?

## Why it is a question

[THEORY-228](../theory.d/THEORY-228.md) now states HaoChen, Wei, Gaidon and Ma's Theorem 3.8 on a
finite augmentation space. At the population optimum of the spectral
contrastive loss, linear-probe error is bounded, up to constant and
logarithmic factors, by the label-recovery error α over the squared
sparsest-partition conductance. Two things the former promote_when asked
for remain undone.

First, the paper's App. F proves only that an eigenbasis exists off a
finite space, under a uniform bound on the density ratio, and asserts the
extension of Theorems 3.8, 4.2 and 4.3 with the proof omitted. Second, α,
the conductance ρ and the eigengap are measured on no real dataset, so
nothing shows the bound is below 1 anywhere.

## What would answer it

A written-out proof of the guarantee on a general augmentation space,
under a stated integrability condition, would answer the first half yes.
A measurement of α and ρ on a real augmentation graph, or on a faithful
proxy, giving a bound below trivial would answer the second half yes. A
finite augmentation graph that meets Assumptions 3.6 and 3.7 but whose
population spectral minimiser has probe error above the bound would refute
the theorem itself. What cannot settle it: linear-probe accuracies of
trained networks, since the theorem is about the population minimiser.
