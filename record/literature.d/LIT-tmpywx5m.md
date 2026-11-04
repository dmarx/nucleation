---
status: Active
status_note: >-
  read 2026-11-04 (NOTE-tmpmn9a9) from arXiv v1; worth reading as a
  factorized rate law for circuit formation in transformer training, with
  emergence, plasticity loss and control read off one equation and an
  explicit ledger of what is proved, conditional and withdrawn. Its
  no-partial-credit fingerprints are a toy grid and an ablation test on
  Pythia; the query–key repair rests on six seeds; mixing is unproved;
  experiments reach 1B parameters, not the 1.4B the abstract names.
title: 'The Kinetics of Training: A Driven-Nucleation Rate Law for Emergence, Plasticity Loss, and Circuit Control in Language Models'
version: 2
history:
- version: 1
  date: '2026-11-04'
  note: >-
    Registered, not read, at the owner's request after the filing of the
    exchange "Organizational Nucleation and SLT", whose A1 cited it under
    a misreading of "nucleation" (QUESTION-275's note of 2026-11-04).
    Checked against the arXiv API on 2026-11-04: Lei Dong, sole author,
    cs.LG, v1 submitted 29 July 2026, which is `published:`; 40 pages, 12
    figures. The summary follows the abstract. Tagged anthology-candidate
    (ADR-005): its subject is training dynamics in language models.
- version: 2
  date: '2026-11-04'
  note: >-
    Read (NOTE-tmpmn9a9), at the owner's request, from the arXiv PDF v1;
    status Deferred → Active. The summary is rewritten from the reading
    and corrected: the experiments name pythia-1b and OLMo-1B as the
    largest models, so "to 1.4B" is the abstract's scope, not a tested
    scale, and the query–key reset was shown on Pythia-70M. The THEORY
    is THEORY-tmpbwwow.
tags:
- learning-theory
- representation-learning
- anthology-candidate
date: '2026-11-04'
published: '2026-07-29'
arxiv: '2607.27281'
first_author: 'Dong'
keywords: []
implementations: []
summary: >-
  Dong (2026) proposes one rate equation for circuit formation in
  transformer training, sites × attempts × drive × e^(−βK) minus
  destruction, with K the jointly necessary attention-head parts still
  missing and no credit for partial alignment. Read forward, a capability
  ignites above a data-concentration floor that is a saddle–node; read
  backward, plasticity loss is depletion of uncommitted heads, invisible in
  the loss and repaired by re-initializing query–key slices (6/6, value
  slices 0/6, on Pythia-70M); and no native SGD knob passes its test for a
  temperature. Pythia and OLMo, to 1B parameters in the experiments
  reported.
---

# LIT-tmpywx5m: The Kinetics of Training: A Driven-Nucleation Rate Law for Emergence, Plasticity Loss, and Circuit Control in Language Models

Dong (2026) — [arXiv:2607.27281](https://arxiv.org/abs/2607.27281)

## Key takeaways

Read (NOTE-tmpmn9a9). Its account is THEORY-tmpbwwow.

- Joint alignment of a circuit's last parts, with no partial credit, is
  "the rate-limiting step of capability formation". The wait counts
  missing parts, not size.
- Ablating one part of a capability's circuit on Pythia leaves a median
  17% of the capability, where partial credit predicts 50–83%.
- Past a critical step a withheld capability "never ignites", while
  validation loss falls smoothly; re-initializing only the query-key
  slices restores learnability.

## Standing in the record

A candidate source for nucleation across a finite barrier, the route
[QUESTION-281](../questions.d/QUESTION-281.md) holds, and for the claim that a joint requirement with no
partial credit has a waiting time set by what is missing. The compatibility
complex of this record's exchange, where a face is all-or-nothing, is the
nearest construct here; whether the two connect is not asked yet.
