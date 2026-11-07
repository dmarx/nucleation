---
number: 231
status: Proposed
formerly:
- CASE-tmpyzdwh
title: 'Two viable regimes exchanging at rate 1, one of which fails at rate 0.02 into an absorbing state: conditioned on survival the chain settles within a few time units to (0.5025, 0.4975) and stays there, while survival decays as e^(−0.00995t), a mean lifetime of 100.5'
version: 1
standing: stipulated
kind: construction
tags:
- probabilistic-modeling
- complex-systems
date: '2026-11-07'
line:
- distributed-agency
- formal-apparatus
illustrates:
- CLAIM-612
- CLAIM-079
summary: >-
  A22 §5 of the exchange "Individuation, Possibility, and Disposition"
  (2026-11-06 to 07), answering the owner's U10, which read A20's thesis
  through "metastability, ergodicity, stationarity, absorbing states". A
  three-state Markov chain whose two viable regimes mix fast and leak
  slowly into an absorbing failure. The reader reran every number; A's
  survival chart has two last-digit slips. Proposed: the construction is
  exact, but what it is used to show is A's reading. The wording is A's;
  adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-612 — filed from the same exchange, Proposed -->

# CASE-231: Two viable regimes exchanging at rate 1, one of which fails at rate 0.02 into an absorbing state: conditioned on survival the chain settles within a few time units to (0.5025, 0.4975) and stays there, while survival decays as e^(−0.00995t), a mean lifetime of 100.5

## The case

A22 §5 of the exchange "Individuation, Possibility, and Disposition"
(https://chatgpt.com/share/6aee7a9b-f13c-83e9-a865-6a29c2c3ff7e). A
continuous-time Markov chain on {A, B, D}: A and B exchange at rate k, B
fails into D at rate ε, and D has no exit. "D has no outgoing transition
under the model's specified dynamics." A takes k = 1 and ε = 0.02.

The quasi-stationary distribution ν is the normalized left eigenvector of
the generator restricted to {A, B}. Conditioned on survival, the law
started from ν stays ν. Unconditionally, mass leaks into D.

The reader's rerun (numpy):

- The restricted generator's eigenvalues are −0.00995 and −2.01005.
- ν = (0.50250, 0.49750). Mean survival from ν is 100.502.
- The gap is 2.0001, so the conditional relaxation time is about 0.49998.
- Survival from ν is e^(−0.00995t) exactly. A's chart gives 0.3698 at
  t = 100 and 0.2247 at t = 150; the values are 0.3697 and 0.2248.
- Started in A, the law conditioned on survival is (0.5695, 0.4305) at
  t = 1, (0.5116, 0.4884) at t = 2, and ν to four places at t = 5.
- The hazard is εν_B, about ε/2. The ratio of extinction time to mixing
  time is about 4k/ε: 21, 201 and 2001 for ε = 0.2, 0.02 and 0.002.

A: "Yet every surviving trajectory still faces a continuing risk of
irreversible collapse, and absorption eventually occurs with probability
one."

## What it can show

That stationary statistics among survivors, reached on the mixing time,
coexist with certain extinction on a time longer by the ratio of the gap
to the hazard ([CLAIM-612](../claims.d/CLAIM-612.md)). It extends [CLAIM-079](../claims.d/CLAIM-079.md) from stability to
statistics conditioned on survival.

It cannot show anything about repair or regeneration, since nothing
leaves D. A's third sense of persistence, "Regenerative persistence", needs
a chain in which some failures are recoverable ([CLAIM-456](../claims.d/CLAIM-456.md)).
