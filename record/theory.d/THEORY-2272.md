---
number: 2272
status: Proposed
formerly:
- THEORY-tmpnit00
promote_when: >-
  Both halves of the title are confirmed independently of this paper: an
  evaluation of real models on more than one intersectional dataset (not
  only uniform random distributions and UCI Adult) finds that rankings
  under different meta-metrics disagree, with the disagreement growing
  with the number of subgroups; and the taxonomy is checked to cover the
  meta-metrics in use, so that the reversals are not artefacts of an
  unusual choice of comparison, aggregation or weighting.
title: 'Fairness meta-metrics can reverse rankings'
statement: >-
  Monnier, George, Guyard, Tarnec and Kountouris (2026) show that turning
  intersectional subgroup fairness measurements into one score requires a
  meta-metric, a choice of comparison, aggregation and weighting, and that
  different meta-metrics, which agree only when there is no disparity, can
  reverse the fairness ranking of the same distributions and models,
  increasingly so as subgroups multiply, so that the choice encodes which
  pattern of disadvantage counts as worse and needs its own justification
version: 1
tags:
- society-and-governance
- mathematical-statistics
date: '2026-11-22'
source:
- LIT-2451
bears_on:
- QUESTION-456
- QUESTION-129
corroborates:
- CLAIM-348
summary: >-
  Monnier et al., read in [NOTE-2364](../notes.d/NOTE-2364.md) (Read). A taxonomy of
  meta-metrics, m = f_a ∘ f_w ∘ f_c (comparison, weighting, aggregation),
  with synthetic and UCI Adult evidence that they reverse fairness
  rankings, and guidelines that match meta-metrics to the disparity
  pattern a context most needs to avoid. It takes the subgroups as fixed
  by prior deliberation, so it bears on how identified demands are
  weighed, not on who counts.
---

# THEORY-2272: Fairness meta-metrics can reverse rankings

## Source

Monnier et al. (2026), [LIT-2451](../literature.d/LIT-2451.md), read in [NOTE-2364](../notes.d/NOTE-2364.md).

## The account

A base metric (true positive rate, say) gives each intersectional
subgroup a benefit. A single score then needs a meta-metric: compare
subgroups (one-vs-all or one-vs-mean, by difference or ratio), optionally
weight the comparisons (by sample size, inversely to it, by distance in
attribute space), and aggregate (L_q norm, ordered weighted average,
share of gaps above ε, or mutual information directly). The literature
mostly uses the worst gap by default.

All meta-metrics agree when every subgroup gets the same benefit, and
diverge otherwise. Different ones penalize different patterns: one
subgroup isolated far from the rest, blocks of subgroups, a continuous
spread of small gaps. The worst-gap rule scores four quite different
unequal profiles the same. Since "none of the identified profiles is
inherently more problematic than another", the choice of meta-metric is a
normative choice that the measurements do not make.

## What was actually shown

An existence proof on five hand-chosen profiles, every pair of which is
ranked both ways by some pair of meta-metrics; an application to seven
default models on UCI Adult with ten Sex × Race subgroups, in which each
model is fairest under some meta-metric; and rank correlations over 1000
random distributions, τ 0.73–0.87 at four subgroups and 0.49–0.79 at
eight, falling as subgroups grow. Each could have shown agreement.

## What this does not say

- It does not say which meta-metric is right anywhere; it says the
  choice must be justified by the conception of fairness in play, and
  leaves that to domain and social-science expertise.
- It does not address who the subgroups are: "The designation of an
  attribute as sensitive is assumed to result from prior normative and
  societal deliberation."
- It does not say small groups vanish in aggregates; that depends on a
  weighting the paper treats as one more choice.
- It does not combine the choice with the statistical uncertainty of
  small subgroups.
