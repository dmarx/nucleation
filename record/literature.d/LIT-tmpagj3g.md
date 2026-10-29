---
status: Active
status_note: >-
  read in full 2026-10-29 ([NOTE-tmpuxoku](../notes.d/NOTE-tmpuxoku.md)) from arXiv v5; worth reading as
  an exact, small-scale statement of the difference between compressing
  for prediction and compressing for control: at full control the
  optimum is the partition of X by p(y | do(x)), which the ordinary
  bottleneck misses under confounding. Toy problems only.
title: 'The Causal Information Bottleneck and Optimal Causal Variable Abstractions'
version: 2
history:
- version: 1
  date: '2026-10-29'
  note: >-
    Filed, not read, from A7 of the exchange "Paper assessment"
    (2026-10-28 to 29). `published:` is arXiv v1 2024-10-01 (UAI 2025,
    PMLR 286) (ADR-002). The authors spell the name Simoes, without the
    tilde A7 gave it.
- version: 2
  date: '2026-10-29'
  note: >-
    Read in full from arXiv 2410.00535v5 (11 June 2025, "Accepted at UAI
    2025"), 20 pp. with appendix (NOTE-tmpuxoku); earlier versions and the
    PMLR version were not read. Status Deferred → Active; summary
    rewritten from the text. The citation stands.
tags:
- causality
- information-theory
date: '2026-10-29'
published: '2024-10-01'
arxiv: '2410.00535'
first_author: 'Simoes'
keywords:
- 'causal information bottleneck'
- 'causal abstraction'
- 'information bottleneck'
- 'interventions'
implementations: []
summary: >-
  Simoes, Dastani & van Ommen (2024; UAI 2025). The causal information
  bottleneck learns a stochastic abstraction T of discrete variables X by
  trading the information T keeps about X against Ic(Y | do(T)), the
  entropy reduction in a target Y when T is set by intervention under a
  uniform protocol over X. Intervening on T is defined as a mixture of
  interventions on X through Bayes inversion of the encoder, and is
  identifiable by a backdoor formula. At full weight on control the
  optimum is the partition of X by p(y | do(x)), Chalupka et al.'s causal
  macrovariables, which the ordinary bottleneck misses under
  confounding. Three toy SCMs confirm it.
---

# LIT-tmpagj3g: The Causal Information Bottleneck and Optimal Causal Variable Abstractions

Simoes, F. N. F. Q., Dastani, M., & van Ommen, T. (2025). The causal information bottleneck and optimal causal variable abstractions. *UAI 2025*, PMLR 286, 3878–3897.

## Why this is here

A7 joined three of the record's ideas through it: task-relative fidelity ([CLAIM-259](../claims.d/CLAIM-259.md)), legibility for a bounded receiver ([CLAIM-455](../claims.d/CLAIM-455.md)), and the difference between supporting prediction and supporting control. A rendering may keep what a task's control needs while losing most of the source. [CLAIM-348](../claims.d/CLAIM-348.md)'s caution stands: optimizing for one task does not make it the task that matters.

The reading ([NOTE-tmpuxoku](../notes.d/NOTE-tmpuxoku.md)) bears this out, with one addition: control
here is relative to a chosen intervention protocol as well as to the
target, and the intervention on T is a stipulation, not a mechanism.
