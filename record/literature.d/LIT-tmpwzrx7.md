---
status: Active
status_note: >-
  read in full 2026-10-31 (NOTE-tmpiaa2o); the paper the owner recalled at
  U4, and the right one, but what it shows is narrower than "the same
  process": near one non-degenerate minimum, the optimiser's noise scale
  ε/S plays the part of 1/N, and training time enters only as the wait
  for stationarity (THEORY-tmp7gcht, THEORY-tmp8ggnh).
title: 'Stochastic Gradient Descent as Approximate Bayesian Inference'
version: 2
history:
- version: 1
  date: '2026-10-31'
  note: >-
    Filed, not read, from A4 of the exchange "Analyze nucleation
    concepts" (2026-10-30 to 31). Citation checked against arXiv (v1
    2017-04-13), whose journal_ref gives JMLR 18 (2017) 1–35. The
    summary follows the abstract and the exchange's description; a
    reading should check it first.
- version: 2
  date: '2026-10-31'
  note: >-
    Read in full from the arXiv preprint 1704.04289v2 (19 January 2018),
    the JMLR typeset version, 35 pp., in NOTE-tmpiaa2o; status Deferred →
    Active. The citation stands; the JMLR article number 134 was not
    checked against the PDF, which gives only "18 (2017) 1-35". The
    summary is rewritten from the text. It keeps "not the initial search
    phase", which the paper says itself (p. 8), and adds that the result
    requires a positive-definite Hessian. Two THEORYs filed.
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
- 'iterate averaging'
implementations: []
summary: >-
  Mandt, Hoffman & Blei (2017). Constant-rate SGD near a minimum with
  positive-definite Hessian A and constant gradient-noise covariance BBᵀ is
  modelled as an Ornstein–Uhlenbeck process whose Gaussian stationary
  covariance solves AΣ + ΣA = (ε/S)BBᵀ. Minimising KL to the Gaussian
  posterior gives the optimal constant rate 2SD/(N tr BBᵀ) and the
  preconditioner (2S/εN)(BBᵀ)⁻¹, which matches the posterior exactly;
  momentum only rescales the covariance; constant-rate SGLD overestimates
  the posterior covariance; and averaging T iterates gives covariance
  A⁻¹BBᵀA⁻¹/(TS), the posterior's for TS observations in a well-specified
  model. Tested on linear, logistic and softmax regression. The search
  phase, singular minima and multiple basins are outside the analysis.
---
<!-- inactive-ok-file: QUESTION-tmpiir0l THEORY-209 — Open or Proposed; the question this grounds, and Kunin's deep-network reading -->

# LIT-tmpwzrx7: Stochastic Gradient Descent as Approximate Bayesian Inference

Mandt, S., Hoffman, M. D., & Blei, D. M. (2017). Stochastic gradient descent as approximate Bayesian inference. *Journal of Machine Learning Research*, 18(134), 1–35.

Read in full in NOTE-tmpiaa2o.

## Why this is here

The paper the owner recalled at U4 ("I think there's a David M Blei paper that discusses this") against A3's claim that Bayesian posterior dominance as n grows "is not the same process" as gradient-based optimization over training time. A4 conceded the separation was "too strong", with a limit kept here: the result relates SGD's long-run distribution to a posterior for a fixed dataset, not training time t to sample size n. The reading bears A4's limit out and sharpens it. The result assumes a positive-definite Hessian, so it concerns a regular model in one basin, where the posterior has no phases to order. What it maps to sample size is the optimiser's noise scale, ε/S against 1/N (THEORY-tmp7gcht). The one place examples processed map to a sample size is iterate averaging after equilibration (THEORY-tmp8ggnh). The record already reads this line of work through Kunin et al. (THEORY-209) and the underdamped stationary Gaussian (THEORY-779), which is this paper's well-specified case with momentum; NOTE-293 cites this paper for McCandlish's temperature. It grounds QUESTION-tmpiir0l. Its precursor is LIT-tmpxo5z5.
