---
status: Proposed
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
- CASE-tmp4sjw7
---

# CLAIM-tmpzkhdr: In conditional generation each condition can be met while their conjunction or relational binding fails, and adding scores composes conditions only under conditional independence at the noisy state

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
