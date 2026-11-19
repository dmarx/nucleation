---
number: 2081
status: Proposed
formerly:
- THEORY-tmpsewbi
title: 'Stern and colleagues find that in transformers below one billion parameters, spending a share of a fixed compute budget on a first phase of formal-language, cellular-automaton, synthetic or code data never lowers natural-language validation loss below spending it all on natural language, that earlier reported gains shrink when the baseline is better initialized, and that what the first phase taught is overwritten at the switch unless the data are interleaved'
version: 1
source:
- LIT-2864
tags:
- learning-theory
- representation-learning
- anthology-candidate
date: '2026-11-19'
promote_when: >-
  An independent study at a stated scale finds that a compute-matched
  synthetic or code first phase does not lower natural-language validation
  loss below natural-language-only training with a tuned initialization,
  in at least one data-constrained and one data-unconstrained regime, and
  that loss on the first-phase distribution rises after the switch but not
  under interleaving of the same data.
summary: >-
  From the reading of [LIT-2864](../literature.d/LIT-2864.md) in [NOTE-2152](../notes.d/NOTE-2152.md). It qualifies the
  generality of [THEORY-2071](THEORY-2071.md) and answers the owner's code-first idea
  negatively at these scales. Proposed until its promote_when is met.
---

# THEORY-2081: Stern and colleagues find that in transformers below one billion parameters, spending a share of a fixed compute budget on a first phase of formal-language, cellular-automaton, synthetic or code data never lowers natural-language validation loss below spending it all on natural language, that earlier reported gains shrink when the baseline is better initialized, and that what the first phase taught is overwritten at the switch unless the data are interleaved

## The account

At matched FLOPs, with spectral initialization, a first phase of k-Dyck, NCA, declarative-reference data or code never beats natural-language-only training on validation loss, in data-constrained, data-unconstrained and over-Chinchilla regimes, and no first phase has a better scaling fit. Added on top of a fixed natural-language budget, a first phase helps at 50M–100M tokens and not at 1B. Loss on the first-phase distribution rises after the switch; interleaving prevents it.

## Evidence

Three seeds for most metrics; up to 881M parameters; Hu and colleagues' exact setup not reproduced.
