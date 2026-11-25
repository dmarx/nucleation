---
number: 2060
status: Proposed
formerly:
- THEORY-tmp5jrhv
title: 'Influential data shift from literature to STEM'
statement: >-
  Nishida and colleagues find that if a pretraining example's influence is
  measured as how much its update shortens the parameter distance to the
  run's final weights, then in Pythia runs literature-classified examples
  are relatively prominent among the most influential early and STEM
  examples later, and high-perplexity text is most influential mid-training
version: 1
source:
- LIT-2851
tags:
- learning-theory
- representation-learning
date: '2026-11-19'
promote_when: >-
  An independent study, on a second model family or corpus, reproduces
  with the same endpoint-distance measure or a function-space version of
  it that literature-classified examples are a larger share of the top
  contributors early than late and STEM-classified examples a larger share
  late than early, across at least three seeds with the data order varied.
summary: >-
  From the reading of [LIT-2851](../literature.d/LIT-2851.md) in [NOTE-2149](../notes.d/NOTE-2149.md). Attribution within
  ordinary runs; the authors state it does not show the effect of changing
  order. Proposed until its promote_when is met.
---

# THEORY-2060: Influential data shift from literature to STEM

## The account

Influence as alignment with the endpoint, estimated from checkpoints of six Pythia sizes and PolyPythia seeds: literature-classified data relatively prominent early, STEM later, hard text mid-training, opponents rising late. Patterns vary with size and with the influence measure.

## Evidence

Attribution only, endpoint-dependent, one run per configuration.
