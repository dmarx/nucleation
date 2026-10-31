---
status: Deferred
status_note: >-
  filed 2026-10-31 from A4 of the exchange "Analyze nucleation concepts" (2026-10-30 to 31); not read.
title: 'Stochastic Gradient Descent as Approximate Bayesian Inference'
version: 1
history:
- version: 1
  date: '2026-10-31'
  note: >-
    Filed, not read, from A4 of the exchange "Analyze nucleation
    concepts" (2026-10-30 to 31). Citation checked against arXiv (v1
    2017-04-13), whose journal_ref gives JMLR 18 (2017) 1–35. The
    summary follows the abstract and the exchange's description; a
    reading should check it first.
tags:
- learning-theory
- probabilistic-modeling
- anthology-candidate
date: '2026-10-31'
published: '2017-04-13'
arxiv: '1704.04289'
first_author: 'Mandt'
keywords:
- 'stochastic gradient descent'
- 'approximate Bayesian inference'
- 'stationary distribution'
- 'Ornstein-Uhlenbeck process'
- 'learning rate'
implementations: []
summary: >-
  Mandt, Hoffman & Blei (2017). Constant-step SGD, modelled near a local
  optimum as a multivariate Ornstein–Uhlenbeck process under a locally
  quadratic loss and constant gradient-noise covariance, has a
  stationary distribution that can be tuned by learning rate, batch size
  and preconditioning to approximate a Bayesian posterior, so SGD can be
  used as an approximate sampler. The result concerns the stationary
  regime, not the initial search phase.
---

# LIT-tmpwzrx7: Stochastic Gradient Descent as Approximate Bayesian Inference

Mandt, S., Hoffman, M. D., & Blei, D. M. (2017). Stochastic gradient descent as approximate Bayesian inference. *Journal of Machine Learning Research*, 18(134), 1–35.

Filed, not read.

## Why this is here

The paper the owner recalled at U4 ("I think there's a David M Blei paper that discusses this") against A3's claim that Bayesian posterior dominance as n grows "is not the same process" as gradient-based optimization over training time. A4 conceded the separation was "too strong", with a limit kept here: the result relates SGD's long-run distribution to a posterior for a fixed dataset, not training time t to sample size n. The record already reads this line of work through Kunin et al. (THEORY-209) and the underdamped stationary Gaussian (THEORY-779), and NOTE-293 cites this paper without a LIT. It grounds QUESTION-tmpiir0l.
