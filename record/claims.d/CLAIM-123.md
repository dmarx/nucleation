---
number: 123
status: Proposed
formerly:
- CLAIM-tmpzkhdr
title: 'In conditional generation each condition can be met while their conjunction or relational binding fails, and adding scores composes conditions only under conditional independence at the noisy state'
version: 1
role: thesis
defeated_if: >-
  A text-to-image model whose per-condition satisfaction predicts its
  joint binding accuracy, or a proof that score addition composes
  conditions without the conditional-independence assumption.
tags:
- compositionality
- probabilistic-modeling
date: '2026-10-09'
line: pragmatic-transport
works:
- what-survives-translation
grounds:
- LIT-770
- LIT-776
- LIT-783
- LIT-782
summary: >-
  The manuscript's §7, citing Composable Diffusion, T2I-CompBench and
  Schrödinger bridges. The readings support it, and the manuscript is
  more careful than the paper it cites.
illustrated_by:
- CASE-004
---

# CLAIM-123: In conditional generation each condition can be met while their conjunction or relational binding fails, and adding scores composes conditions only under conditional independence at the noisy state

## The claim

Under a product-of-experts factorization, s₁₂ = s₁ + s₂ − s₀, which is what
Composable Diffusion exploits ([LIT-770](../literature.d/LIT-770.md)). The manuscript adds that this needs
conditional independence at the relevant noisy state and does not guarantee
correct joint bindings. Schrödinger bridges give a path-space view of
conditional transport ([LIT-776](../literature.d/LIT-776.md)).

## What it does not say

It does not say a generative failure is evidence of sheaf contextuality, and
it does not identify denoising time with historical or telephone-game time.
The reading of Composable Diffusion ([NOTE-597](../notes.d/NOTE-597.md)) supports the manuscript's
caution: the paper derives the composition for clean data, applies it at every
noise level without discussion, and loses to an energy-based baseline when
composing relations.

## In C7's appendix

C7 Appendix D, omitted from the extracted manuscript, states the identity's
conditions: "The product-of-experts conditional score identity follows from the
conditional independence of c1 and c2 given x_t and a shared prior p_t(x_t),
subject to positivity and differentiability. It is not a generic identity for
arbitrary prompt embeddings or finite-step diffusion implementations. When scores
are approximate, compositional failures may reflect estimator error, model
misspecification, or sampling limitations." It adds controls: prompts paired by
entities, scene type and length, randomized order and seeds, and evaluation blind
to condition. The open question behind it is [QUESTION-018](../questions.d/QUESTION-018.md).

## A second caveat on adding scores

Ho and Salimans ([LIT-839](../literature.d/LIT-839.md)) show that learned scores are not
conservative, so a guided field is in general the score of no density. That
is a caveat on s₁₂ = s₁ + s₂ − s₀ beyond the conditional independence this
claim states. Attend-and-Excite ([LIT-806](../literature.d/LIT-806.md)) documents conjunctions failing
by omission ("catastrophic neglect"), and in T2I-CompBench++ ([LIT-798](../literature.d/LIT-798.md))
Composable Diffusion is again the weakest method.
