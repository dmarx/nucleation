---
number: 2058
status: Proposed
formerly:
- THEORY-tmp1b3hj
title: 'Training-point value shrinks as pretraining runs'
statement: >-
  Wang and colleagues find, with a per-step Shapley value of each training
  point toward a validation loss summed over a run, that in GPT-2
  pretraining on the Pile the value toward a math corpus goes mostly to
  ArXiv, that general web crawl holds a positive share only in the first few
  hundred steps, and that the value per point of every domain shrinks as
  training proceeds
version: 1
source:
- LIT-2865
tags:
- learning-theory
- representation-learning
date: '2026-11-19'
promote_when: >-
  An independent study, or the authors' code run with several seeds or
  validation sets, reproduces with In-Run Data Shapley or TracIN-Ideal on
  a Pile-trained model a positive share for web crawl toward a math target
  only in the first few hundred steps, a dominant ArXiv share, and
  declining average per-point values for each domain.
summary: >-
  From the reading of [LIT-2865](../literature.d/LIT-2865.md) in [NOTE-2143](../notes.d/NOTE-2143.md). The measure credits
  only immediate alignment, so it cannot see an early step easing later
  ones. Proposed until its promote_when is met.
---

# THEORY-2058: Training-point value shrinks as pretraining runs

## The account

Per-step Shapley values toward a math validation corpus, over the first 10,000 steps of GPT-2 on the Pile: ArXiv dominant, Pile-CC briefly positive then zero or negative, every domain's per-point value decaying.

## Evidence

One run and one target; early training only; SGD formulas on AdamW.
