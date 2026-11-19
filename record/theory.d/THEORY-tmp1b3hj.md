---
status: Proposed
title: 'Wang and colleagues find, with a per-step Shapley value of each training point toward a validation loss summed over a run, that in GPT-2 pretraining on the Pile the value toward a math corpus goes mostly to ArXiv, that general web crawl holds a positive share only in the first few hundred steps, and that the value per point of every domain shrinks as training proceeds'
version: 1
source:
- LIT-tmprdmjg
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
  From the reading of [LIT-tmprdmjg](../literature.d/LIT-tmprdmjg.md) in [NOTE-tmp4t32o](../notes.d/NOTE-tmp4t32o.md). The measure credits
  only immediate alignment, so it cannot see an early step easing later
  ones. Proposed until its promote_when is met.
---

# THEORY-tmp1b3hj: Wang and colleagues find, with a per-step Shapley value of each training point toward a validation loss summed over a run, that in GPT-2 pretraining on the Pile the value toward a math corpus goes mostly to ArXiv, that general web crawl holds a positive share only in the first few hundred steps, and that the value per point of every domain shrinks as training proceeds

## The account

Per-step Shapley values toward a math validation corpus, over the first 10,000 steps of GPT-2 on the Pile: ArXiv dominant, Pile-CC briefly positive then zero or negative, every domain's per-point value decaying.

## Evidence

One run and one target; early training only; SGD formulas on AdamW.
