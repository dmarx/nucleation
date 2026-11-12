---
status: Active
title: 'FairCert: Certifiable Error Rate Fairness for ML and LLM Decision Systems'
version: 2
history:
- version: 2
  date: '2026-11-12'
  note: >-
    Read on 2026-11-12, in NOTE-tmppe0ip; account THEORY-tmp76i78. Status
    Active. Single author, Md Fahim Sikder (Linköping University); "and et
    al." was wrong. The venue is the European Conference on Algorithmic
    Fairness (the workshop formerly EWAF), PMLR 350: 8-23.
- version: 1
  date: '2026-11-12'
  note: >-
    Filed, not read, from the exchange "Medical Ethics and Media Enshitification" (2026-11-11). Checked on 2026-11-12 by fetching the page, which gave the title and date. The record held no LIT with this identifier, title or first author. The PMLR page gives citation_publication_date 2026/09/30 and first author Md Fahim Sikder; the full author list was not recorded. The summary is how A describes the work; a reading should check it first.
tags:
- mathematical-statistics
- society-and-governance
date: '2026-11-12'
published: '2026-09-30'
url: 'https://proceedings.mlr.press/v350/sikder26a.html'
first_author: 'Sikder'
keywords: []
implementations: []
summary: >-
  Sikder (2026), Proceedings of Machine Learning Research 350. Read on
  2026-11-12 in [NOTE-tmppe0ip](../notes.d/NOTE-tmppe0ip.md): FairCert is a black-box audit pipeline that
  turns per-group false-positive-rate (FPR) and true-positive-rate (TPR)
  gaps into finite-sample certificates. Five stages: a stratified split with
  a walled-off 15% audit set; LLM-guided discovery of candidate
  intersectional subgroups from aggregate training statistics (hypotheses),
  confirmed on the disjoint audit set; per-group error rates of the
  classifier's predictions; a certificate built from Clopper-Pearson exact
  intervals per group with a Bonferroni correction over K groups, which
  bounds the worst pairwise gap with probability at least 1−δ and passes if
  the bound is within tolerance ε; and, for failures, per-group threshold
  calibration with the TPR cost reported, plus a structured EU AI
  Act-oriented report. Its account is [THEORY-tmp76i78](../theory.d/THEORY-tmp76i78.md). Registered from the
  exchange "Medical Ethics and Media Enshitification" (2026-11-11), where A
  cited it at A42 §6.
---
<!-- inactive-ok-file: THEORY-tmp76i78 — Proposed; filed from the same exchange -->

# LIT-tmppyl6o: FairCert: Certifiable Error Rate Fairness for ML and LLM Decision Systems

Md Fahim Sikder (2026). "FairCert: Certifiable Error Rate Fairness for ML and LLM Decision Systems." *European Conference on Algorithmic Fairness, Proceedings of Machine Learning Research 350: 8-23*.

## Key takeaways

Read on 2026-11-12 ([NOTE-tmppe0ip](../notes.d/NOTE-tmppe0ip.md)). An assembly, explicitly not new
statistics ("FairCert does not introduce new statistical tools"), of exact
binomial intervals, family-wise correction and permutation inference into an
audit that yields a pass/fail certificate at stated tolerance and
confidence, applied to LLM classifiers and intersectional groups, with an
LLM used only to propose subgroups.

## Standing in the record

Registered on 2026-11-12 from the exchange "Medical Ethics and Media Enshitification" (2026-11-11), where A cited it at A42 §6. It bears on [CLAIM-537](../claims.d/CLAIM-537.md), [QUESTION-tmpuftum](../questions.d/QUESTION-tmpuftum.md).

Read on 2026-11-12; the reading is [NOTE-tmppe0ip](../notes.d/NOTE-tmppe0ip.md) and its account
[THEORY-tmp76i78](../theory.d/THEORY-tmp76i78.md).
