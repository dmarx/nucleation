---
status: Active
status_note: >-
  read in full 2026-10-31 ([NOTE-tmph1our](../notes.d/NOTE-tmph1our.md)); every result reappears in the
  2017 JMLR paper ([LIT-tmpwzrx7](LIT-tmpwzrx7.md)), which is the one to cite. Worth keeping
  as the first statement and as the version Hennick and De Baerdemacker
  cite.
title: 'A Variational Analysis of Stochastic Gradient Algorithms'
version: 2
history:
- version: 1
  date: '2026-10-31'
  note: >-
    Filed, not read, from A4 of the exchange "Analyze nucleation
    concepts" (2026-10-30 to 31). Citation checked against arXiv (v1
    2016-02-08; journal_ref ICML 2016, pp. 354–363). The summary
    follows the abstract and the exchange's description; a reading
    should check it first.
- version: 2
  date: '2026-10-31'
  note: >-
    Read in full from the arXiv preprint 1602.02666v1, 11 pp., in
    NOTE-tmph1our, against the 2017 paper; status Deferred → Active. The
    citation stands. The summary is rewritten from the text. No THEORY of
    its own: it is a second source on THEORY-tmp7gcht.
tags:
- learning-theory
- probabilistic-modeling
- anthology-candidate
date: '2026-10-31'
published: '2016-02-08'
arxiv: '1602.02666'
first_author: 'Mandt'
keywords:
- 'stochastic gradient descent'
- 'variational inference'
- 'stationary distribution'
- 'stochastic gradient Fisher scoring'
implementations: []
summary: >-
  Mandt, Hoffman & Blei (2016). The first version of the 2017 JMLR paper.
  Constant-rate SGD near a quadratic optimum is modelled as an
  Ornstein–Uhlenbeck process; its Gaussian stationary law is fitted to the
  Gaussian posterior by minimising KL over the learning rate, batch size
  and preconditioner, giving the optimal rate 2DS/(N tr BBᵀ) and the exact
  preconditioner (2S/εN)(BBᵀ)⁻¹. It shows SGFS's preconditioner is
  KL-optimal, quantifies its diagonal truncation, and uses constant SGD
  for variational EM over hyperparameters. The later paper adds momentum,
  constant-rate SGLD and iterate averaging.
---

# LIT-tmpxo5z5: A Variational Analysis of Stochastic Gradient Algorithms

Mandt, S., Hoffman, M. D., & Blei, D. M. (2016). A variational analysis of stochastic gradient algorithms. *Proceedings of ICML 2016*, 354–363.

Read in full in [NOTE-tmph1our](../notes.d/NOTE-tmph1our.md).

## Why this is here

Named in A4 as the precursor of Mandt, Hoffman and Blei 2017 ([LIT-tmpwzrx7](LIT-tmpwzrx7.md)). Registered so that the two are read together; the later paper is the one to read first. The reading confirms that this one adds nothing the later one lacks, and that its scope is the same: the stationary regime of a regular model near one optimum.
