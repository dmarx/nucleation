---
status: Proposed
promote_when: >-
  Sozou (1998) read in full, confirming that discounting is taken as
  survival with a constant but uncertain hazard, that an exponential prior
  gives 1/(1 + kt), and that other priors give non-hyperbolic discount
  functions.
title: 'Fedus and colleagues restate Sozou''s result that an agent discounting future reward by its probability of surviving to collect it, with a constant but unknown hazard rate, discounts by the Laplace transform of its prior over the hazard, so that an exponential prior gives exactly the hyperbola 1/(1 + kt), a gamma prior 1/(1 + bt)^c and a uniform prior (1 − e^(−kt))/(kt)'
version: 1
tags:
- motivation
- probabilistic-modeling
- anthology-candidate
date: '2026-11-21'
source:
- LIT-tmpa91zo
summary: >-
  Hyperbolic discounting as an average of exponentials over uncertain
  hazard rates, read through Fedus and colleagues because Sozou could not
  be fetched. Proposed until Sozou is read.
---
<!-- inactive-ok-file: NOTE-tmpanyxy NOTE-tmpzdxq3 — Skimmed; cited in the readings of 2026-11-21 -->
<!-- inactive-ok-file: LIT-tmpk0e2v CLAIM-tmpve51e CLAIM-tmp6q7ma THEORY-067 CLAIM-198 — Proposed, Deferred, Unfetched or new; filed in this contribution of 2026-11-21 or the ones it builds on -->

# THEORY-tmp2kqhd: Fedus and colleagues restate Sozou's result that an agent discounting future reward by its probability of surviving to collect it, with a constant but unknown hazard rate, discounts by the Laplace transform of its prior over the hazard, so that an exponential prior gives exactly the hyperbola 1/(1 + kt), a gamma prior 1/(1 + bt)^c and a uniform prior (1 − e^(−kt))/(kt)

## Source

Fedus, Gelada, Bengio, Bellemare and Larochelle, [LIT-tmpa91zo](../literature.d/LIT-tmpa91zo.md), read in [NOTE-tmpanyxy](../notes.d/NOTE-tmpanyxy.md), restating Sozou ([LIT-tmpk0e2v](../literature.d/LIT-tmpk0e2v.md), Unfetched); corroborated by Anchugina, Ryan and Slinko ([NOTE-tmpzdxq3](../notes.d/NOTE-tmpzdxq3.md)).

## What was actually shown

In the restatement: s(t) = ∫p(λ)e^(−λt)dλ; an exponential prior with mean k gives 1/(1 + kt) (§3.2, App. B.2); the uniform, gamma and delta cases (Fig. 2, App. B.3).

## What this does not say

Not Sozou's own treatment of preference reversal or updating; not that every spread of rates gives a hyperbola: only an exponential prior gives 1/(1 + kt) exactly.

## Connections

[THEORY-1117](THEORY-1117.md) and [THEORY-067](THEORY-067.md) (Ainslie); [CLAIM-198](../claims.d/CLAIM-198.md) (preference reversal); [CLAIM-tmpve51e](../claims.d/CLAIM-tmpve51e.md) (the same integral with rate and time swapped); [CLAIM-tmp6q7ma](../claims.d/CLAIM-tmp6q7ma.md).
