---
number: 240
status: Answered
formerly:
- QUESTION-tmpc4mhm
title: 'Does a transport whose local kernels commute with restriction preserve overlap consistency, and does a transport induced by one global stochastic kernel preserve global extendability?'
version: 1
tags:
- contextuality
- mathematics
date: '2026-10-21'
line: pragmatic-transport
refines:
- QUESTION-022
summary: >-
  The part of [QUESTION-022](QUESTION-022.md) the manuscript's Propositions 1 and 2 settle,
  split off under [ADR-049](../decisions.d/ADR-049.md). Yes to both, for finite scenarios: [CLAIM-121](../claims.d/CLAIM-121.md)
  for overlap consistency and [CLAIM-070](../claims.d/CLAIM-070.md) for global extendability. Both
  are sufficient conditions. Whether they are necessary, and what
  transports that change the cover do, stays with [QUESTION-022](QUESTION-022.md).
answered_by:
- CLAIM-070
- CLAIM-121
---

# QUESTION-240: Does a transport whose local kernels commute with restriction preserve overlap consistency, and does a transport induced by one global stochastic kernel preserve global extendability?

## Answer

Yes to both, for finite scenarios. This is the part of [QUESTION-022](QUESTION-022.md) that
A110 §IX called "a starting result", split off on 2026-10-21 ([ADR-049](../decisions.d/ADR-049.md)).

- **Overlap consistency.** [CLAIM-121](../claims.d/CLAIM-121.md), the manuscript's Proposition 1. If
  the local kernels commute with restriction, an overlap-consistent source
  model is carried to an overlap-consistent target model. The proof
  exchanges pushforward and restriction, then uses the source's overlap
  consistency.
- **Global extendability.** [CLAIM-070](../claims.d/CLAIM-070.md), the manuscript's Proposition 2. If
  each local kernel is the restriction of one global kernel K_X, the
  pushforward of a global extension p of the source is a global extension
  of the target, (K_X)#p.

Both CLAIMs are Active with a demonstrated warrant. Each answers the
question as posed here, which asks whether these two classes preserve,
not which classes do.

## What it leaves to [QUESTION-022](QUESTION-022.md)

Both results are sufficient conditions. Neither says that a transport
outside these classes fails to preserve, and neither covers transports
that change the measurement cover. [CLAIM-121](../claims.d/CLAIM-121.md) also concerns marginal
consistency only, "not global noncontextuality".
