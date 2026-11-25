---
number: 2078
status: Proposed
formerly:
- THEORY-tmpq9sev
title: 'More code aids compositional, hurts language'
statement: >-
  Petty, van Steenkiste and Linzen find that in 374M-parameter language
  models pretrained on natural language and code shuffled together, a larger
  code share improves fine-tuned compositional generalization to
  formal-output semantic parsing beyond what the same extra language data
  gives, and improves multi-digit arithmetic, while it lowers
  natural-language-output generalization and morphology, reasoning and
  world-knowledge tasks
version: 1
source:
- LIT-2846
tags:
- learning-theory
- representation-learning
- compositionality
date: '2026-11-19'
promote_when: >-
  An independent replication with several seeds at a stated scale finds
  that a higher code share in shuffled pretraining raises generalization
  accuracy on a formal-output semantic-parsing benchmark more than
  language-only data of the same size, and lowers accuracy on a natural-
  language-output transformation benchmark, under both fixed-total-data
  and fixed-language-data budgets.
summary: >-
  From the reading of [LIT-2846](../literature.d/LIT-2846.md) in [NOTE-2139](../notes.d/NOTE-2139.md). Code's effect as a
  share, not an order; it bears on the owner's code-first lead only by
  contrast. Proposed until its promote_when is met.
---

# THEORY-2078: More code aids compositional, hurts language

## The account

Varying code share from 0 to 90 per cent at fixed total data, and from 0 to
50 per cent at fixed language data with size-matched language-only
baselines, code helps where the output is formal and hurts where it is
natural language or draws on world knowledge. Across BigBench, code widens
the spread of task effects without moving their mean significantly.

## Evidence

Five seeds per mixture; linear fits; one scale; code interleaved
throughout, so nothing on order.
