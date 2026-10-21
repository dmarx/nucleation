---
status: Active
status_note: >-
  read 2026-10-21 (NOTE-tmpmuo87) in full, from arXiv:2002.06673v4; worth reading for the split between performative stability (optimal for the distribution one's own deployment induces, the fixed point of retraining) and performative optimality, for the exact conditions under which retraining converges to a unique stable point (smooth, strongly convex loss and ε < γ/β, each shown necessary; THEORY-tmpwl9bj), and for the bound 2L_zε/γ between stable points and optima (THEORY-tmp9lnfi). Read it knowing that its conditions hold in its own simulation only at the smallest ε, that the distribution map depends on the current model alone, and that it says nothing about how to reach the optimum.
title: 'Performative Prediction'
version: 2
history:
- version: 1
  date: '2026-10-21'
  note: >-
    Filed, not read. Citation checked against Crossref, OpenAlex and arXiv on 2026-10-21. `published:` is arXiv v1, 16 February 2020 (ICML 2020), per ADR-002. No DOI. The exchange's citation was right. Flagged `anthology-candidate` as a machine-learning paper the anthology may want; it carries no instruction for ML practice.
- version: 2
  date: '2026-10-21'
  note: >-
    Read in full at the owner's request ("get started reading the proposed works"), NOTE-tmpmuo87, from arXiv v4 (26 February 2021), text extracted with pdftotext; the PMLR text was not compared. Status Deferred → Active. The summary is checked against the reading and sharpened: the convergence conditions are stated, and the two notions are said to be close, not only different.
tags:
- learning-theory
- anthology-candidate
date: '2026-10-21'
published: '2020-02-16'
arxiv: '2002.06673'
url: 'https://proceedings.mlr.press/v119/perdomo20a.html'
first_author: 'Perdomo'
keywords:
- 'performative prediction'
- 'performative stability'
- 'repeated risk minimization'
- 'distribution shift'
- 'strategic classification'
implementations: []
summary: >-
  Perdomo, Zrnic, Mendler-Dünner & Hardt (2020). When a deployed prediction changes the distribution of the outcomes it predicts, define performative stability (a model optimal for the distribution it induces) and performative optimality (least risk on the distribution it induces); show they can differ; prove that with a smooth, strongly convex loss and a distribution map ε-Lipschitz in Wasserstein distance, retraining converges to a unique stable point when ε < γ/β, that each condition is needed, and that stable points lie within 2L_zε/γ of optima.
---
<!-- inactive-ok-file: CLAIM-tmpeftzb — Proposed; filed from the same exchange, named as the entry this work bears on -->
<!-- inactive-ok-file: TERM-tmp5lqn0 — Proposed; filed from the same exchange, named as the entry this work bears on -->
# LIT-tmpwbhro: Performative Prediction

Perdomo, J. C., Zrnic, T., Mendler-Dünner, C. & Hardt, M. (2020). Performative Prediction. *Proceedings of the 37th International Conference on Machine Learning*, PMLR 119: 7599–7609. Preprint: arXiv:2002.06673 (16 February 2020).

Read 2026-10-21 in full, in NOTE-tmpmuo87. The summary was checked against
the reading.

## Why this is here

A25 called it "essential prior art for any claim about representations participating in the reproduction of the social structures they describe", and drew the warning that "a description that is well calibrated against outcomes generated under its own use need not be an adequate description of the system under a different policy or observational regime." A26 §2 built on it. Bears on [CLAIM-tmpeftzb](../claims.d/CLAIM-tmpeftzb.md), [CLAIM-tmppi0xf](../claims.d/CLAIM-tmppi0xf.md) and [TERM-tmp5lqn0](../terms.d/TERM-tmp5lqn0.md), and on [CLAIM-350](../claims.d/CLAIM-350.md).
