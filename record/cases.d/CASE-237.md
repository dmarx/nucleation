---
number: 237
status: Proposed
formerly:
- CASE-tmpmjn9t
title: 'Two complementary capacities whose success probabilities each rise from 0.8 to 0.85 while the probability that both hold falls from 0.8 to 0.7, because they went from failing together to failing apart'
version: 1
standing: fictional
kind: construction
tags:
- probabilistic-modeling
- operations-research
date: '2026-11-12'
line:
- readiness
- formal-apparatus
illustrates:
- CLAIM-632
- CLAIM-587
bears_on:
- QUESTION-395
summary: >-
  A's construction, from the exchange "Identify Synthesis Opportunities"
  (2026-11-08, A8 and A14), filed as a case at the owner's instruction
  (U5) that claims resting on explicit constructions be connected to cases
  describing them. A offered it as the proof of a new claim, that
  improving every required capacity can lower readiness when the
  capacities' dependence changes. The record already holds that result in
  substance: [CLAIM-632](../claims.d/CLAIM-632.md)'s records identify readiness only when the
  dependence is known, and certify a floor only from the lower Fréchet
  bound. So the case illustrates [CLAIM-632](../claims.d/CLAIM-632.md) and [CLAIM-587](../claims.d/CLAIM-587.md), and A's claim is
  not filed. The wording is A's; adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-632 — Proposed; the claim the construction illustrates -->

# CASE-237: Two complementary capacities whose success probabilities each rise from 0.8 to 0.85 while the probability that both hold falls from 0.8 to 0.7, because they went from failing together to failing apart

## The case

A response needs two complementary capacities, A and B, and succeeds only
when both hold ([CLAIM-587](../claims.d/CLAIM-587.md)'s conjunction). Readiness is R = Pr(A and B)
([TERM-115](../terms.d/TERM-115.md)). A's table, from A8:

| measure | before | after |
|---|---:|---:|
| capacity A succeeds | 0.80 | 0.85 |
| capacity B succeeds | 0.80 | 0.85 |
| both succeed | 0.80 | 0.70 |

A: "Before, the two capacities fail together. Afterwards, their failures
occur separately. Each capacity becomes individually more reliable, but
the probability that both are ready decreases."

The joint laws exist. Before: both hold with 0.80, neither with 0.20, and
exactly one with 0. After: both hold with 0.70, exactly one with 0.15
each, and neither with 0. Each is a probability distribution with the
stated marginals, checked by the filer on 2026-11-12. Before, R sits at
its Fréchet upper bound, min Pᵢ = 0.8; after, at its lower bound,
P_A + P_B − 1 = 0.7.

## What it shows

- **A record of rising marginals does not show rising readiness.** This
  is [CLAIM-632](../claims.d/CLAIM-632.md)'s point, that per-capacity records "identify it only when
  the capacities' dependence is known", applied to two records in time.
  Applying [CLAIM-632](../claims.d/CLAIM-632.md)'s certification rule with the old upper bound as the
  floor gives the comparative form: per-capacity records certify that
  readiness rose only when the new lower bound, ΣP′ᵢ − (n − 1), exceeds
  the old upper bound, min Pᵢ. Here 0.7 does not exceed 0.8, so the
  records leave open a fall, and the construction realizes one.
- **Why the value of one capacity depends on the others** ([CLAIM-587](../claims.d/CLAIM-587.md)): a
  change that decouples the capacities' failures can cost more joint
  readiness than it buys in each.

## What it cannot show

- That improvements in practice tend to decouple failures. The
  construction is fictional and shows only that it can happen.
- Anything when capacities substitute for one another, which [CLAIM-587](../claims.d/CLAIM-587.md)
  and [CLAIM-632](../claims.d/CLAIM-632.md) exclude.

## Provenance

A drafted it as the evidence for a claim it numbered 633, in a
patch bundle that was never committed (A7: "Nothing will be written to
the repository"). That number now names a different claim on the record.
A first linked claim and case by `grounds`; since the claim is held by
[CLAIM-632](../claims.d/CLAIM-632.md), the case only illustrates it here.
