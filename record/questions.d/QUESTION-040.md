---
number: 40
status: Open
formerly:
- QUESTION-tmp0gx60
title: 'When the reification rule prices a candidate found in the same data, among many directions the data only partly determine, what must its Occam term count, and how far does the search inflate the candidate''s d''?'
version: 1
tags:
- model-comparison
- information-geometry
- learning-theory
date: '2026-10-12'
line: 'distributed-agency'
refines:
- QUESTION-035
answered_by:
- THEORY-080
- THEORY-028
summary: >-
  Filed in the fourth synthesis pass to give readings no question asked
  for a place in the argument. It bears on [CLAIM-154](../claims.d/CLAIM-154.md), [CLAIM-188](../claims.d/CLAIM-188.md),
  [CLAIM-152](../claims.d/CLAIM-152.md) and [CLAIM-164](../claims.d/CLAIM-164.md). [THEORY-080](../theory.d/THEORY-080.md) and [THEORY-028](../theory.d/THEORY-028.md) answer it in part;
  the body gives each one's limit.
---

# QUESTION-040: When the reification rule prices a candidate found in the same data, among many directions the data only partly determine, what must its Occam term count, and how far does the search inflate the candidate's d'?

## The question

[CLAIM-154](../claims.d/CLAIM-154.md) prices one candidate direction at a time, and its Gaussian prior and posterior are fixed in advance. Real candidates are blocks or couplings inside a model with many directions. Most of those directions are weakly determined, and the candidate was found by searching the data it is then tested on. The question has two parts. First, what is the right Occam count for a candidate in that setting? Second, by how much does selecting the candidate bias the d'² that the rule compares against that count?

## Why the record needs it

[CLAIM-154](../claims.d/CLAIM-154.md) itself says the rule "prices a candidate; it does not find one". [CLAIM-188](../claims.d/CLAIM-188.md) shows that the Gaussian term misprices candidates whose removal makes the model singular. That leaves the regular but many-directional case open, and it also leaves the effect of search open. [CLAIM-152](../claims.d/CLAIM-152.md) makes the target an input. If the candidate partition was picked to fit that target, the verdict inherits a selection bias. An answer would turn [QUESTION-035](QUESTION-035.md)'s "with what margin" into a corrected threshold.

## What the record holds

- [THEORY-080](../theory.d/THEORY-080.md): in a linearised Gaussian model "the Occam factor is a sum over the NTK's eigenvalues". Each direction pays ½ log(1 + βλ/α), and directions the data do not determine cost nothing. So the count is the number of well-determined directions, not the number of parameters. Limit: the model is linearised. The THEORY says this "removes that question", meaning singularity, "rather than answering it".
- [THEORY-028](../theory.d/THEORY-028.md): the bias of "any data-dependent choice" is at most √(2σ²·I), where I is the information the choice carries about the data. A stable search, one that strong signal settles, biases little. Limit: the bound holds in expectation, for subgaussian statistics.

## What would answer it

A rule that combines the spectral Occam count with a selection correction, checked against exact Bayes factors on a coupled-block model whose candidate is found by search.
