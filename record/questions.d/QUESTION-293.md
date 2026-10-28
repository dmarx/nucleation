---
number: 293
status: Answered
formerly:
- QUESTION-tmpvsepl
title: 'Is the distortion of a composite of approximate transports bounded by the sum of its parts'' distortions, and does that additive bound survive when the distortion lacks a triangle inequality or a later kernel stretches distances?'
version: 1
tags:
- mathematics
- philosophy-of-language
date: '2026-10-27'
line: pragmatic-transport
refines:
- QUESTION-017
summary: >-
  The additive part of [QUESTION-017](QUESTION-017.md), split off by the status review of
  2026-10-27 under [ADR-049](../decisions.d/ADR-049.md), because [CLAIM-260](../claims.d/CLAIM-260.md) (Active) settles it in full.
  The composite of an ε₁-transport and an ε₂-transport is an
  (Lε₁ + ε₂)-transport when the distortion obeys a triangle inequality,
  with L the later kernel's stretch, so additive when that kernel is
  nonexpansive, as every Markov kernel is in total variation. Without a
  triangle inequality, or with an expansive kernel, the additive bound
  fails.
---

# QUESTION-293: Is the distortion of a composite of approximate transports bounded by the sum of its parts' distortions, and does that additive bound survive when the distortion lacks a triangle inequality or a later kernel stretches distances?

## The question

A50 §2 bounded drift by adding the steps' distortions, assuming a metric.
[QUESTION-017](QUESTION-017.md) asks what bound holds when that assumption is dropped. This
question asks the first part of that: whether the additive bound itself
holds, and under which of the metric's properties.

## The answer

[CLAIM-260](../claims.d/CLAIM-260.md), Active and demonstrated, settles it:

- **With a triangle inequality** the composite's distortion is at most
  Lε₁ + ε₂, where L is how far the later kernel stretches distances. It
  is additive when L ≤ 1. In total variation both conditions hold, since
  it is a metric and every Markov kernel is nonexpansive in it.
- **Without a triangle inequality** the additive bound can fail. Under the
  squared difference of Bernoulli parameters, or squared Hellinger
  distance, two steps of 1/4, or about 0.29, compose to a distortion of 1.
- **With an expansive kernel** it fails too. In Wasserstein-1 on the line,
  x ↦ 2x makes the composite only a (2ε₁ + ε₂)-transport.

What weaker bound holds where the additive one fails, and what holds for
directed distortion, remain [QUESTION-017](QUESTION-017.md)'s.
