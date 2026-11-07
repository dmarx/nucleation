---
number: 612
status: Proposed
formerly:
- CLAIM-tmp7cpzx
title: "Statistics conditioned on survival can be stationary and quickly reached while absorption is certain: in a finite chain whose viable states all lead to an absorbing failure, the distribution of the survivors settles on the mixing time and the survivors die out on a time longer by the ratio of the spectral gap to the hazard, so a surviving organization's stable statistics are no evidence that it persists"
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the construction: a finite chain in which an absorbing state
  is reachable from every viable state and survival does not go to zero,
  or a quasi-stationary distribution, gap or hazard for CASE-231 other
  than stated. Also defeated if it only restates CLAIM-079's note of
  2026-11-04, that under small noise every stable state is only
  metastable: the claim must add that the survivors' statistics, not only
  a deterministic regime, are stationary and fast while extinction is
  certain. Not defeated by a chain with a transition out of the failure
  state, which is then not absorbing; the claim is about absorbing failure.
tags:
- probabilistic-modeling
- complex-systems
- individuation
date: '2026-11-07'
line:
- distributed-agency
- formal-apparatus
grounds:
- CASE-231
complements:
- CLAIM-079
- CLAIM-566
uses:
- TERM-071
summary: >-
  A22 §5 of the exchange "Individuation, Possibility, and Disposition"
  (2026-11-06 to 07), on quasi-stationary distributions, answering the
  owner's U10. A: "The conditional organization can be extraordinarily
  stable while its unconditional survival is not." The general statement
  over finite chains is the reader's framing of A's worked model,
  [CASE-231](../cases.d/CASE-231.md), whose numbers the reader reran. The wording is A's;
  adopting it is the owner's call.
---
<!-- inactive-ok-file: ARG-056 — filed from the same exchange, Proposed -->
<!-- inactive-ok-file: CASE-231 — filed from the same exchange, Proposed -->

# CLAIM-612: Statistics conditioned on survival can be stationary and quickly reached while absorption is certain: in a finite chain whose viable states all lead to an absorbing failure, the distribution of the survivors settles on the mixing time and the survivors die out on a time longer by the ratio of the spectral gap to the hazard, so a surviving organization's stable statistics are no evidence that it persists

## The claim

A22 §5 of the exchange "Individuation, Possibility, and Disposition"
(https://chatgpt.com/share/6aee7a9b-f13c-83e9-a865-6a29c2c3ff7e): "The
conditional organization can be extraordinarily stable while its
unconditional survival is not." And: "The existence of a compelling,
low-dimensional, statistically stable description tells us little by
itself about the permanence of the process it describes."

In [CASE-231](../cases.d/CASE-231.md) the survivors' law reaches its quasi-stationary value
within about five time units and the mean lifetime is about 100.5. The
ratio of the two times is about 4k/ε, so it grows without bound as the
hazard falls, and the survivors' statistics look the same throughout.

It extends [CLAIM-079](CLAIM-079.md)'s note of 2026-11-04 (under small noise "every stable
state is only metastable") from deterministic stability to statistics
conditioned on survival. It separates what [CLAIM-566](CLAIM-566.md) calls persistence
over a horizon from the stationarity of what the survivors do. It also
names a sense [TERM-071](../terms.d/TERM-071.md) lacks. A22 §5 distinguishes "Conditional
persistence", "Survival persistence" and "Regenerative persistence"; the
first, "what the system looks like while it continues to exist", is new
to the record.

## What it does not say

- That stable statistics are evidence against persistence. They are no
  evidence either way; the hazard has to be estimated separately.
- Anything about regeneration. With a way out of the failure state, the
  failure is not absorbing ([CLAIM-456](CLAIM-456.md) on which losses are repairable).

## How far "no evidence" holds

Argued at the owner's review ([ARG-056](../arguments.d/ARG-056.md)), rerunning [CASE-231](../cases.d/CASE-231.md)'s
script. Stationarity and the speed of settling carry no information about
the hazard. The values of the quasi-stationary distribution carry a
trace of it, of order ε/(8k): from (0.5, 0.5) at ε = 0 to
(0.5249, 0.4751) at ε = 0.2. "No evidence" is exact for the first two and
nearly so for the third.
