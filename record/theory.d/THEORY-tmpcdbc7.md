---
status: Proposed
title: 'Javed and White show that a representation meta-trained by differentiating through online SGD updates on correlated streams (OML), then frozen beneath a small online-learned predictor, lets that predictor learn sequential regression and classification tasks with far less forgetting than pre-trained or sparsity-trained representations, and that such representations come out highly sparse with no dead units.'
version: 1
source:
- LIT-tmppqss3
tags:
- learning-theory
date: '2026-11-19'
bears_on:
- QUESTION-tmpwqepn
promote_when: >-
  An independent replication on Split-Omniglot or Incremental Sine Waves
  finds that online SGD on top of a frozen OML representation keeps
  markedly higher accuracy (or lower error) on earlier classes or
  functions than online SGD on a representation pre-trained on the same
  meta-training data, and that the OML representation has lower instance
  sparsity than the pre-trained one with no dead units.
summary: >-
  From the reading of [LIT-tmppqss3](../literature.d/LIT-tmppqss3.md) in [NOTE-tmpd0h3v](../notes.d/NOTE-tmpd0h3v.md). Javed and White
  (2019), arXiv 1905.12588, NeurIPS 2019. OML meta-trains a representation
  by differentiating through online SGD on correlated streams, then
  freezes it beneath a small predictor that learns online. On Incremental
  Sine Waves and Split-Omniglot this gives far less forgetting than pre-
  trained or sparse representations, and learning faster than approximate
  IID training. The representation turns out highly sparse with no dead
  units. It is here because A54 named it for representations meta-trained
  against forgetting, bearing on overconsolidation ([CLAIM-tmp8ljvp](../claims.d/CLAIM-tmp8ljvp.md)). It
  bears mostly on forgetting: it secures retention and fast acquisition
  together by freezing the representation, and it says nothing on
  plasticity over long training. Read in its NOTE.
---
<!-- inactive-ok-file: CLAIM-tmp8ljvp — Proposed; cited in this filing of 2026-11-19 -->

# THEORY-tmpcdbc7: Javed and White show that a representation meta-trained by differentiating through online SGD updates on correlated streams (OML), then frozen beneath a small online-learned predictor, lets that predictor learn sequential regression and classification tasks with far less forgetting than pre-trained or sparsity-trained representations, and that such representations come out highly sparse with no dead units.

## The account

A network trained end-to-end on a correlated stream overwrites what it learned earlier. OML instead meta-learns a representation by unrolling the online updates a learner will make and scoring the result on everything seen. Interference becomes the training signal, and the representation is shaped so that online updates either generalize or avoid each other. Frozen at test time, it supports learning new functions "with a negligible increase in average MSE" and Omniglot classes "with minimal forgetting". It turns out highly sparse with no dead units, and it improves other continual-learning methods built on it.

## What it does not show

- Not that the representation itself stays plastic. It is frozen at test time.
- Nothing about long training horizons, loss of plasticity, or restoring plasticity.
- Not without a meta-training distribution like the test distribution.
