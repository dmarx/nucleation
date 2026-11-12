---
status: Proposed
title: 'Boult et al. (2019) argue that a classifier that labels the whole input space, including the region far from its training data, has unbounded open space risk'
version: 1
tags:
- learning-theory
- epistemology
date: '2026-11-12'
source:
- LIT-2300
promote_when: >-
  §2–§5 state that thresholded uncertainty, reject options and background
  classes leave infinite open space risk, and that CAP and EVT models bound
  it (citing their earlier proofs).
summary: >-
  The central account of [LIT-2300](../literature.d/LIT-2300.md), read in [NOTE-tmpdbblh](../notes.d/NOTE-tmpdbblh.md). Proposed until its
  promote_when is met.
---

# THEORY-tmpdui86: Boult et al. (2019) argue that a classifier that labels the whole input space, including the region far from its training data, has unbounded open space risk

## The account

Boult et al. (2019) argue that a classifier that labels the whole input space, including the region far from its training data, has unbounded open space risk. Reject options, background classes and uncertainty thresholds leave that region labelled. Such a classifier assigns unknown inputs to known classes, often with high confidence: "uncertain is not unknown". Bounding the risk takes models whose acceptance region shrinks away from the training data, such as CAP and extreme-value models.
