---
number: 2131
status: Proposed
formerly:
- THEORY-tmp2kqhd
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
- LIT-2944
summary: >-
  Hyperbolic discounting as an average of exponentials over uncertain
  hazard rates, read through Fedus and colleagues because Sozou could not
  be fetched. Proposed until Sozou is read.
---
<!-- inactive-ok-file: NOTE-2221 NOTE-2234 — Skimmed; cited in the readings of 2026-11-21 -->
<!-- inactive-ok-file: THEORY-2150 — Proposed; the reading of Mitzenmacher, 2026-11-21 -->
<!-- inactive-ok-file: LIT-2949 CLAIM-777 CLAIM-769 THEORY-067 CLAIM-198 — Proposed, Deferred, Unfetched or new; filed in this contribution of 2026-11-21 or the ones it builds on -->
<!-- inactive-ok-file: THEORY-tmpczldx CLAIM-tmpf9qt9 — Proposed; the reading of Beck and Cohen and the assistant's condition on the spread, 2026-11-22 -->

# THEORY-2131: Fedus and colleagues restate Sozou's result that an agent discounting future reward by its probability of surviving to collect it, with a constant but unknown hazard rate, discounts by the Laplace transform of its prior over the hazard, so that an exponential prior gives exactly the hyperbola 1/(1 + kt), a gamma prior 1/(1 + bt)^c and a uniform prior (1 − e^(−kt))/(kt)

## Source

Fedus, Gelada, Bengio, Bellemare and Larochelle, [LIT-2944](../literature.d/LIT-2944.md), read in [NOTE-2221](../notes.d/NOTE-2221.md), restating Sozou ([LIT-2949](../literature.d/LIT-2949.md), Unfetched); corroborated by Anchugina, Ryan and Slinko ([NOTE-2234](../notes.d/NOTE-2234.md)).

## What was actually shown

In the restatement: s(t) = ∫p(λ)e^(−λt)dλ; an exponential prior with mean k gives 1/(1 + kt) (§3.2, App. B.2); the uniform, gamma and delta cases (Fig. 2, App. B.3).

## What this does not say

Not Sozou's own treatment of preference reversal or updating; not that every spread of rates gives a hyperbola: only an exponential prior gives 1/(1 + kt) exactly.

## Connections

[THEORY-1117](THEORY-1117.md) and [THEORY-067](THEORY-067.md) (Ainslie); [CLAIM-198](../claims.d/CLAIM-198.md) (preference reversal); [CLAIM-777](../claims.d/CLAIM-777.md) (the same integral with rate and time swapped); [CLAIM-769](../claims.d/CLAIM-769.md).

## Note of 2026-11-21: Mitzenmacher, read

A **parallel**, with no edge. Mitzenmacher's §7 ([LIT-3003](../literature.d/LIT-3003.md), read in
[NOTE-2237](../notes.d/NOTE-2237.md); [THEORY-2150](THEORY-2150.md)) has this account's structure with the roles
moved: a family indexed by time, here a lognormal of variance t, averaged
over an exponential distribution of the time, gives a power law,
∫ λe^(−λt)·lognormal_t dt ∝ x^(−1−√(2λ)) for x above 1. Sozou averages
exponentials over an exponential spread of hazards and gets a hyperbola.
Neither work draws the connection. The account is unchanged.

## Note of 2026-11-22: Beck and Cohen, read

Beck and Cohen (LIT-2962, read in NOTE-tmpj8ro5; THEORY-tmpczldx)
**corroborate the mathematics**: the same integral, "the Laplace transform
of the probability density f(β)" (p. 3), with the same gamma and uniform
results, derived independently in physics for a fluctuating inverse
temperature. They say nothing of discounting, so this account's
`promote_when`, which asks for Sozou, is not met. The assistant's
CLAIM-tmpf9qt9 adds the general condition: the asymptotic hyperbola needs
only a positive density at zero hazard. The account is unchanged.
