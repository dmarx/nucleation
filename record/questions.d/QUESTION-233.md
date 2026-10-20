---
number: 233
status: Open
formerly:
- QUESTION-tmpcvdv0
title: 'Do language models show the data-limited exponent γ/(2β) because data limits the usable horizon: does the exponent track γ/(2β) when one corpus statistic is moved and the other held, and does the match survive at horizons of thousands of tokens with γ estimated outside the model class?'
version: 1
tags:
- learning-theory
- linguistics
- information-theory
date: '2026-10-20'
line: learned-structure
summary: >-
  Filed when the promotion audit (batch 062, [ADR-047](../decisions.d/ADR-047.md) v2 and v3) narrowed
  and promoted [THEORY-204](../theory.d/THEORY-204.md). That the fitted data-limited exponent matches
  γ/(2β) on TinyStories and WikiText-103, and that assumed per-lag
  scaling forms give min(δ, γ/(2β)), is settled. Whether real learners
  show the exponent for the horizon reason was the old promote_when, and
  it moves here.
answered_by:
- THEORY-tmpz9axt
---

# QUESTION-233: Do language models show the data-limited exponent γ/(2β) because data limits the usable horizon: does the exponent track γ/(2β) when one corpus statistic is moved and the other held, and does the match survive at horizons of thousands of tokens with γ estimated outside the model class?

## Why it is a question

[THEORY-204](../theory.d/THEORY-204.md) now states two things. Under assumed scaling forms for each
lag's learning curve, a horizon n*(P) ~ P^(1/(2β)) gives a data-limited
loss exponent of min(δ, γ/(2β)). And on two corpora, at up to about 10^8
tokens and horizons of tens of tokens, the exponent fitted to transformer
learning curves overlaps γ/(2β). Cagnetta et al. ([LIT-888](../literature.d/LIT-888.md)) offer the
horizon as the reason. The match does not show that it is the reason:
another route could give the same number at that scale.

An answer is one of the following:

- **An intervention.** Text whose correlations beyond some lag are
  weakened while its short-range statistics are kept, or a synthetic
  language with tunable β and γ, with the measured exponent tracking
  γ/(2β) as one is moved and the other held. The exponent should depart
  from γ/(2β) when the within-horizon excess loss is made to decay slowly.
- **Scale.** The same match where the usable horizon reaches thousands of
  tokens, with γ estimated without a neural model of the same class.

More collapses at the scale already reported, with γ read off the trained
models' own n-gram losses, cannot settle it.
