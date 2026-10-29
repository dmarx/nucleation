---
status: Deferred
title: 'Optimal Transport for structured data with application on graphs'
version: 1
history:
- version: 1
  date: '2026-10-29'
  note: >-
    Filed, not read, from A6 of the exchange "Paper assessment"
    (2026-10-28 to 29). `published:` is arXiv v1 2018-05-23 (ICML 2019,
    PMLR 97; PMLR's metadata scrambles the authors' names) (ADR-002).
tags:
- mathematics
- network-science
date: '2026-10-29'
published: '2018-05-23'
arxiv: '1805.09114'
first_author: 'Vayer'
keywords:
- 'Fused Gromov-Wasserstein'
- 'optimal transport'
- 'structured data'
- 'graph classification'
- 'barycenters'
implementations: []
summary: >-
  Vayer et al. (2018). The fused Gromov–Wasserstein distance, which
  compares structured objects such as graphs on their features and their
  structure jointly, with a weight between the two; it beats graph
  kernels and convolutional networks on graph classification.
---

# LIT-tmpjs7kp: Optimal Transport for structured data with application on graphs

Vayer, T., Chapel, L., Flamary, R., Tavenard, R., & Courty, N. (2019). Optimal transport for structured data with application on graphs. *ICML 2019*, PMLR 97, 6275–6284.

Not read. The summary is drawn from the abstract and from the exchange's
description, which the lookup of 2026-10-29 checked. A reading should check
it first.

## Why this is here

A6 thought it "probably the most practical model for [CASE-055](../cases.d/CASE-055.md)": independently validated anchor matches break the symmetries pure GW cannot, and the weight between structure and anchors is a scientific parameter to vary, not a hyperparameter to tune. An arm of [CASE-tmph0fxi](../cases.d/CASE-tmph0fxi.md).
