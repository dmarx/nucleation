---
number: 87
status: Active
formerly:
- CASE-tmph4ds5
title: 'The discredited instrument and the second population: two pairs of readings
  with the same mean that the mean cannot tell apart once one instrument is discredited
  or a mixture is considered'
version: 1
standing: stipulated
kind: construction
tags:
- mathematical-statistics
- probabilistic-modeling
date: '2026-10-15'
line: formal-apparatus
summary: >-
  A10 §2's paired construction, which A10 recommended filing ("That single paired
  construction makes the dependence of sufficiency on the task and model very easy
  to see"). It grounds the relativity half of [CLAIM-300](../claims.d/CLAIM-300.md).
supports:
- CLAIM-300
---

# CASE-087: The discredited instrument and the second population: two pairs of readings with the same mean that the mean cannot tell apart once one instrument is discredited or a mixture is considered

## The case

X₁, X₂ ~ N(μ, σ²), independent, σ known. History A reads (0, 10), history B
(4, 6). Both means are 5 and both likelihoods for μ are proportional to
exp(−(μ − 5)²/σ²), so the mean is sufficient and the histories are the same
for μ.

- **Source reappraisal.** Instrument 1 is found miscalibrated and X₁
  dropped. History A leaves 10, history B leaves 6. The mean cannot say
  which.
- **Model revision.** Investigators consider (1 − π)N(μ, σ²) +
  πN(μ + δ, σ²). Histories with the same mean and different spread
  carry different evidence for a second component, and the mean has
  discarded it.

## What it can show

That sufficiency holds of a statistic under a model and a decision
family, and lapses when either changes. A10's ladder: a fixed model and
family, where a statistic can suffice; new evidence about old sources;
a new model or question; open-ended inquiry, where "which distinctions
will matter is itself uncertain".

## What it cannot show

That the reasoning behind the estimate is what should have been kept.
A10: "we do not need the researcher's complete historical argument here.
A source-indexed data record would suffice. This is an important
objection to the idea that justificatory history specifically is what
must be preserved."
