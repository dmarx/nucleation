---
number: 805
status: Proposed
formerly:
- THEORY-tmp0gm1u
promote_when: 'Two kinds of result, one for each half. For the prior: a derivation of the cluster-size preference for the losses as used (VICReg with its hinge variance term, SimCLR at finite temperature), or a measurement of the cluster-size distribution that trained VICReg and SimCLR models induce on data with known unequal classes. For the effect: the imbalance experiment repeated with batches sampled uniformly from a naturally long-tailed dataset, at one architecture across methods, with seeds. The account is refuted for a method if its learned partitions track unequal class sizes as well as an instance-based method''s do. What cannot settle it: more results with two-class batches, or gains from a prior matched with labels.'
title: Volume-maximizing joint-embedding objectives as a class, VICReg and SimCLR as well as MSN and SwAV, carry a prior toward equal-sized clusters, and that prior costs them semantic transfer when the pretraining data are class-imbalanced, including on naturally long-tailed data
version: 1
tags:
- representation-learning
- probabilistic-modeling
date: '2026-10-20'
source:
- LIT-231
summary: The general reading that [THEORY-306](THEORY-306.md) held before the promotion audit narrowed it to the explicit priors of MSN and SwAV and to one experiment with two to eight classes per batch (batch 033). Assran et al. (2022), [LIT-231](../literature.d/LIT-231.md), read in [NOTE-850](../notes.d/NOTE-850.md), argue the prior for the whole class, VICReg through an informal reduction to K-means and SimCLR through a cited equivalence, and read it as the cause of the degradation reported on real long-tailed data. Filed under [ADR-047](../decisions.d/ADR-047.md) v4 so the wide form stays a thesis evidence can confirm or reject.
extends:
- THEORY-306
answers:
- QUESTION-171
---

# THEORY-805: Volume-maximizing joint-embedding objectives as a class, VICReg and SimCLR as well as MSN and SwAV, carry a prior toward equal-sized clusters, and that prior costs them semantic transfer when the pretraining data are class-imbalanced, including on naturally long-tailed data

## Source

Assran et al. (2022), [LIT-231](../literature.d/LIT-231.md), §§3–5 and Appendix C, read in [NOTE-850](../notes.d/NOTE-850.md). The
class-wide prior and its explanation of the degradation joint-embedding
methods show on long-tailed data are the paper's thesis; [NOTE-850](../notes.d/NOTE-850.md) rates both
halves weak beyond MSN and SwAV and beyond batches of two to eight classes.

## What is asserted, and by whom

The thesis has two halves. The prior: every volume-maximizing
joint-embedding objective, not only those that state it, prefers equal-sized
clusters ([NOTE-850](../notes.d/NOTE-850.md), C3 and C4, both weak: VICReg by Proposition 2 for a
simplified loss with an informal last step, SimCLR by a cited equivalence).
The effect: that prior is why these methods lose semantic transfer on
class-imbalanced data, natural long tails included (C7, weak, inferred from
batches of two to eight classes). Assran et al. assert both.

## What the record holds toward it

- [THEORY-306](THEORY-306.md) (Active): the explicit prior in MSN's loss and SwAV's equipartition, and 11 to 18 points of ImageNet linear accuracy lost by SimCLR, MSN and VICReg with two to eight classes per batch, against under one for MAE and data2vec, one run per cell.
- Matching the prior to the class distribution helps on long-tailed pretraining (C6, moderate), which fits the thesis without testing it, since the gain was obtained with the true or a guessed class prior.

## What would confirm or reject it

A derivation or measurement of the prior for VICReg and SimCLR as trained,
and the imbalance effect on naturally long-tailed data with seeds, confirm
it; learned partitions that track unequal classes as well as an
instance-based method's reject it for that method. [QUESTION-171](../questions.d/QUESTION-171.md) asks the
same thing as a question; this entry is the answer Assran et al. propose.
