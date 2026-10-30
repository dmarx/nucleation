---
number: 349
status: Open
formerly:
- QUESTION-tmpxiomw
title: 'On tasks other than Jacobs and colleagues'' four-class vowel discrimination, do mixtures of experts trained on the error of a single expert chosen stochastically by the gate, or on the mixture''s negative log-likelihood, leave most experts with near-zero mixing proportions while matching the accuracy of a dense network of equal size?'
version: 1
tags:
- learning-theory
- probabilistic-modeling
date: '2026-10-30'
line: distributed-agency
summary: >-
  The replication [THEORY-937](../theory.d/THEORY-937.md)'s promotion condition asked for, moved here
  when the twenty-third status review promoted that reading of one study
  ([ADR-065](../decisions.d/ADR-065.md) §3: a request to replicate moves to a QUESTION). The vowel
  task needs two or three lines; whether the sparse division appears on
  tasks without so few natural subtasks is open.
---
<!-- inactive-ok-file: QUESTION-132 — Open; the separate question of whether an idle expert recovers, named -->

# QUESTION-349: On tasks other than Jacobs and colleagues' four-class vowel discrimination, do mixtures of experts trained on the error of a single expert chosen stochastically by the gate, or on the mixture's negative log-likelihood, leave most experts with near-zero mixing proportions while matching the accuracy of a dense network of equal size?

## Why it is a question

[THEORY-937](../theory.d/THEORY-937.md) reports one study ([NOTE-1147](../notes.d/NOTE-1147.md)): on a four-class vowel task with
two natural subtasks, mixtures of 4 or 8 linear experts left all but 2 or
3 experts with mixing proportions effectively zero, and matched
backpropagation networks in accuracy. The authors read the idle experts
as economy: "the system tends to use as few experts as it can to solve a
problem" (p. 84). A task that needs two or three lines cannot show
whether that holds where the subtasks are less obvious. In large sparse
mixtures Shazeer et al. ([LIT-1507](../literature.d/LIT-1507.md)) report imbalance among experts as a
failure, so the benign reading of the vowel result may not carry.

## What would answer it

A second study, on another task, in which mixtures trained this way leave
most experts with near-zero mixing proportions while matching a dense
network of equal size. A run in which they do not, under the same
training errors, answers no for that task. Whether an idle expert could
regain responsibility is [QUESTION-132](QUESTION-132.md)'s question, and a result about it
does not answer this one.
