---
number: 2050
status: Proposed
formerly:
- THEORY-tmpvf16r
title: 'Akyürek and colleagues show that transformers trained from scratch to do linear regression in context behave like standard estimators chosen by their capacity and the data: deep, wide ones match least squares on noiseless data and the Bayes-optimal ridge predictor under label noise, while one-layer models are closest to a single gradient step and two- to four-layer ones to ridge regression; the least-squares weights and moment vector can be decoded, nonlinearly, from their hidden states'
version: 1
source:
- LIT-2811
tags:
- representation-learning
- learning-theory
date: '2026-11-19'
bears_on:
- QUESTION-159
corroborates:
- CLAIM-118
promote_when: >-
  An independent replication of trained in-context linear regressors finds
  the best-fitting ridge parameter tracking σ²/τ² at high capacity, and
  the best-fitting estimator moving from gradient-descent-like to ridge to
  least squares as depth grows.
summary: >-
  From the reading of [LIT-2811](../literature.d/LIT-2811.md) in [NOTE-2121](../notes.d/NOTE-2121.md). Akyürek, Schuurmans,
  Andreas, Ma and Zhou (ICLR 2023; arXiv 2211.15661) prove that a
  transformer can implement one gradient-descent step or one ridge-
  regression update on in-context examples. They then show that
  transformers trained on in-context linear regression behave like
  standard estimators chosen by capacity: one gradient step at one layer
  (poorly), ridge at two to four layers, least squares at eight or more.
  With label noise the high-capacity learners match the Bayes-optimal
  ridge predictor. Probes recover the moment vector and least-squares
  weights from hidden states, but nonlinearly, unlike the constructions.
  Here because A56 cited it beside Garg et al. for in-context learning as
  a learned learner. It measures [THEORY-169](THEORY-169.md)'s caution that trained
  transformers are not shown to do gradient descent, and it is a case of
  [CLAIM-118](../claims.d/CLAIM-118.md)'s split. Read in its NOTE.
---

# THEORY-2050: Akyürek and colleagues show that transformers trained from scratch to do linear regression in context behave like standard estimators chosen by their capacity and the data: deep, wide ones match least squares on noiseless data and the Bayes-optimal ridge predictor under label noise, while one-layer models are closest to a single gradient step and two- to four-layer ones to ridge regression; the least-squares weights and moment vector can be decoded, nonlinearly, from their hidden states

## The account

A transformer with constant depth can implement one gradient-descent step (O(d) width) or one rank-one ridge update (O(d²) width) on in-context examples (Theorems 1–2). Trained ones are matched to such algorithms by their outputs. At 16 layers and width 512 they match OLS on noiseless data and the minimum-Bayes-risk ridge predictor under noise, with the best ridge parameter tracking σ²/τ². At lower capacity the best fit moves from one GD step (1 layer, a poor fit) to ridge (2–4 layers) to OLS (8+). The moment vector XᵀY becomes decodable around layer 7 and the least-squares weights around layer 12, both nonlinearly.

## What it does not show

- That trained transformers run the constructed algorithms: the probes find nonlinear encodings the constructions lack.
- That language models do this; the paper is about linear regression trained from scratch.
- That ICL is always Bayes-optimal: capacity-limited models are not.
- An exact identity of the [QUESTION-159](../questions.d/QUESTION-159.md) kind: the theorems are existence constructions. The question is listed because the reading bears on it, not because it answers it.

## Note of 2026-11-19: Brown and colleagues, read
A parallel (NOTE-tmprmye5): a from-scratch case of the de novo end of Brown and colleagues' spectrum, in-context learning of functions not seen in training.
