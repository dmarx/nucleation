---
number: 2076
status: Proposed
formerly:
- THEORY-tmpngig0
title: 'Two-phase blends beat random order'
statement: >-
  Feng, Prabhumoye and colleagues find that pretraining an 8B language model
  on a diverse blend followed by a shorter high-quality blend scores higher
  than the same data in random order at the same total tokens, mostly in
  math and code, with the second phase best at about two-fifths of training
version: 1
source:
- LIT-2848
tags:
- learning-theory
- representation-learning
date: '2026-11-19'
promote_when: >-
  An independent study, or a replication with several seeds, finds that at
  fixed total tokens and fixed per-source weights a quality-ordered two-
  phase schedule beats random order of the same blend on downstream
  averages with both arms under the same learning-rate schedule.
summary: >-
  From the reading of [LIT-2848](../literature.d/LIT-2848.md) in [NOTE-2145](../notes.d/NOTE-2145.md). Order at fixed data
  and weights; the gain is small and confounded with an end-of-run anneal.
  Proposed until its promote_when is met.
---

# THEORY-2076: Two-phase blends beat random order

## The account

At 8B and 1T tokens, two-phase ordering averages 52.86 against 51.12 for random order of the same blend and 45.17 for natural weights; the gain is mostly in GSM8K and code. Phase 2 at 40 per cent of training is best; at 50 per cent accuracy degrades.

## Evidence

One run per configuration; the headline chosen from six lengths; phase 2 re-annealed.
