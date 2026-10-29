---
number: 305
status: Open
formerly:
- QUESTION-tmpuk5nc
title: 'From small random weights not aligned with the data''s eigenbasis, does a linear-attention layer trained on in-context regression come into alignment with that basis before or while its modes are learned, so that its learning is staged by the input spectrum without the alignment being assumed?'
version: 1
tags:
- learning-theory
- representation-learning
date: '2026-10-29'
line: learned-structure
refines:
- QUESTION-039
summary: >-
  The promotion condition formerly on [THEORY-481](../theory.d/THEORY-481.md), moved here when the
  ninth status review narrowed it to the aligned case it derives and
  promoted it, as [THEORY-285](../theory.d/THEORY-285.md)'s moved to [QUESTION-303](QUESTION-303.md). [THEORY-186](../theory.d/THEORY-186.md)
  holds the same open claim for two-layer linear networks.
---

# QUESTION-305: From small random weights not aligned with the data's eigenbasis, does a linear-attention layer trained on in-context regression come into alignment with that basis before or while its modes are learned, so that its learning is staged by the input spectrum without the alignment being assumed?

## Why it is a question

[THEORY-481](../theory.d/THEORY-481.md)'s derivation assumes the weights are aligned with the input
covariance's eigenbasis at initialisation and throughout ([NOTE-658](../notes.d/NOTE-658.md), the
paper's A.11.2), and its simulations start aligned. Whether training from a
random start reaches that alignment, and so whether the staged learning
holds in general, is not shown.

## What would answer it

An analysis or simulation showing that from small random initial weights
not aligned with the data's eigenbasis, a linear-attention layer trained on
in-context regression aligns with that basis before or while its modes are
learned, so that the per-mode logistic curves and their ordering by input
variance hold without the alignment being assumed; or the same staged
learning measured in a trained layer whose tasks do not share the input
covariance's eigenbasis. Timing coincidences of spectral measures in
non-linear transformers cannot settle it, and neither can more simulations
from aligned starts.
