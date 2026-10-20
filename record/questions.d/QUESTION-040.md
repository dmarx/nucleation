---
number: 40
status: Open
formerly:
- QUESTION-tmp0gx60
title: 'When the reification rule prices a candidate found in the same data, among many directions the data only partly determine, what must its Occam term count, and how far does the search inflate the candidate''s d''?'
version: 3
history:
- version: 2
  date: '2026-10-14'
  note: >-
    After the reading of LIT-964's Supplementary Material (NOTE-848).
    "What the record holds" adds THEORY-318 for the selection-bias
    half, with its limit. The question stays open.
- version: 3
  date: '2026-10-19'
  note: >-
    THEORY-318 narrowed and promoted (promotion audit, batch 044): its
    bullet in "What the record holds" now gives the narrowed claim, and
    the holdout clause is QUESTION-196. The question stays open.
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
- THEORY-318
summary: >-
  Filed in the fourth synthesis pass to give readings no question asked
  for a place in the argument. It bears on [CLAIM-154](../claims.d/CLAIM-154.md), [CLAIM-188](../claims.d/CLAIM-188.md),
  [CLAIM-152](../claims.d/CLAIM-152.md) and [CLAIM-164](../claims.d/CLAIM-164.md). [THEORY-080](../theory.d/THEORY-080.md) and [THEORY-028](../theory.d/THEORY-028.md) answer it in part;
  the body gives each one's limit.
refined_by:
- QUESTION-196
---

# QUESTION-040: When the reification rule prices a candidate found in the same data, among many directions the data only partly determine, what must its Occam term count, and how far does the search inflate the candidate's d'?

## The question

[CLAIM-154](../claims.d/CLAIM-154.md) prices one candidate direction at a time, and its Gaussian prior and posterior are fixed in advance. Real candidates are blocks or couplings inside a model with many directions. Most of those directions are weakly determined, and the candidate was found by searching the data it is then tested on. The question has two parts. First, what is the right Occam count for a candidate in that setting? Second, by how much does selecting the candidate bias the d'² that the rule compares against that count?

## Why the record needs it

[CLAIM-154](../claims.d/CLAIM-154.md) itself says the rule "prices a candidate; it does not find one". [CLAIM-188](../claims.d/CLAIM-188.md) shows that the Gaussian term misprices candidates whose removal makes the model singular. That leaves the regular but many-directional case open, and it also leaves the effect of search open. [CLAIM-152](../claims.d/CLAIM-152.md) makes the target an input. If the candidate partition was picked to fit that target, the verdict inherits a selection bias. An answer would turn [QUESTION-035](QUESTION-035.md)'s "with what margin" into a corrected threshold.

## What the record holds

- [THEORY-080](../theory.d/THEORY-080.md): in a linearised Gaussian model "the Occam factor is a sum over the NTK's eigenvalues". Each direction pays ½ log(1 + βλ/α), and directions the data do not determine cost nothing. So the count is the number of well-determined directions, not the number of parameters. Limit: the model is linearised. The THEORY says this "removes that question", meaning singularity, "rather than answering it".
- [THEORY-028](../theory.d/THEORY-028.md): the bias of "any data-dependent choice" is at most √(2σ²·I), where I is the information the choice carries about the data. A stable search, one that strong signal settles, biases little. Limit: the bound holds in expectation, for subgaussian statistics.
- NML's parametric complexity comp(M; v) ([LIT-238](../literature.d/LIT-238.md), read in [NOTE-760](../notes.d/NOTE-760.md)): the log of the number of distinguishable distributions, (k/2) log(n/2π) + log ∫ √|I|. It is a candidate Occam count. Like [THEORY-080](../theory.d/THEORY-080.md)'s spectral count, it weights directions by Fisher information rather than counting parameters, and models with equal parameter counts differ in it. Limit: it does not address the selection-bias half of the question.
- [THEORY-318](../theory.d/THEORY-318.md) ([LIT-964](../literature.d/LIT-964.md), Supplementary Material only): a bound k on the max-information between a dataset and an analyst's chosen statistic multiplies by at most 2^k the probability that the statistic overfits, and ε-differential privacy keeps k at most log₂e·εn. Whether a holdout can then validate many adaptively chosen statistics, through Thresholdout, is [QUESTION-196](QUESTION-196.md). Limit: statistical queries on a discrete universe, and a procedure that prevents inflation, not a correction that says how far a search already run inflated its result.

## What would answer it

A rule that combines the spectral Occam count with a selection correction, checked against exact Bayes factors on a coupled-block model whose candidate is found by search.
