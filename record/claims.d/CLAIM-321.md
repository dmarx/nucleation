---
number: 321
status: Proposed
formerly:
- CLAIM-tmpjni98
title: 'In text-to-image diffusion models each condition of a prompt can be met while their conjunction or relational binding fails: benchmarks find single objects rendered almost always and attribute binding and relations failing most, and composing by adding scores does worst on relations'
version: 1
role: thesis
warrant: empirical
defeated_if: >-
  Evaluations that check each condition and the joint binding on the same
  images and find that a model's per-condition satisfaction predicts its
  joint binding accuracy, so that conjunctions and relational bindings
  fail only when some single condition does.
tags:
- compositionality
- probabilistic-modeling
date: '2026-10-15'
line:
- pragmatic-transport
works:
- what-survives-translation
grounds:
- LIT-782
- LIT-783
- LIT-806
- LIT-798
- LIT-770
corroborates:
- CLAIM-123
summary: >-
  Split from [CLAIM-123](CLAIM-123.md) under [ADR-043](../decisions.d/ADR-043.md): the empirical part of that claim,
  that each condition can be met while their conjunction or relational
  binding fails, documented by GenEval, T2I-CompBench and T2I-CompBench++,
  by Attend-and-Excite's "catastrophic neglect", and by Composable
  Diffusion losing to an energy-based baseline on relations. It
  corroborates [CLAIM-123](CLAIM-123.md)'s derivation without carrying it, and does not
  say what causes the failures.
---

# CLAIM-321: In text-to-image diffusion models each condition of a prompt can be met while their conjunction or relational binding fails: benchmarks find single objects rendered almost always and attribute binding and relations failing most, and composing by adding scores does worst on relations

## The claim

This is the observed half of [CLAIM-123](CLAIM-123.md), stated on its own so that its
warrant can be. [CLAIM-123](CLAIM-123.md)'s derivation says that adding scores,
s₁₂ = s₁ + s₂ − s₀, composes conditions only under conditional
independence at the noisy state and "does not guarantee correct joint
bindings". What the readings show is that joint bindings do in fact fail
where single conditions are met.

- GenEval ([LIT-782](../literature.d/LIT-782.md), [NOTE-593](../notes.d/NOTE-593.md)) scores every diffusion model it tests at
  0.97–0.98 on single objects, and the best 2023 open model at most 0.35
  on attribute binding and 0.15 on relative position; failures include
  colours swapped between the two objects. T2I-CompBench ([LIT-783](../literature.d/LIT-783.md)) builds
  its prompts around the same attribute-binding and relation failures.
- Attend-and-Excite ([LIT-806](../literature.d/LIT-806.md)) documents conjunctions failing by omission
  ("catastrophic neglect").
- Composable Diffusion ([LIT-770](../literature.d/LIT-770.md), [NOTE-597](../notes.d/NOTE-597.md)), the method that adds scores,
  "loses to an energy-based baseline when composing relations", and in
  T2I-CompBench++ ([LIT-798](../literature.d/LIT-798.md)) "Composable Diffusion is again the weakest
  method".

## What it does not say

- What causes the failures. C7's appendix, quoted in [CLAIM-123](CLAIM-123.md): "When
  scores are approximate, compositional failures may reflect estimator
  error, model misspecification, or sampling limitations." A failure is
  not evidence that conditional independence at the noisy state fails.
- That a generative failure is evidence of sheaf contextuality, or that
  denoising time is historical or telephone-game time.
- That binding always fails. The benchmarks report rates, for the models
  and prompt templates they test.
