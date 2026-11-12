---
status: Proposed
title: 'The chain and the complete graph on the same configurations show that peak-capacity thresholds do not fix cumulative transition costs'
version: 1
form: existence
grounds:
- CASE-tmpbbfq8
concludes:
- CLAIM-tmp2u6bs
tags:
- mathematics
- operations-research
date: '2026-11-12'
line:
- realizability
- formal-apparatus
summary: >-
  The construction case grounding A's claim, as A argued it in the exchange
  "Identify Synthesis Opportunities" (2026-11-08, A12 and A14). Filed
  because the case is the claim's only ground, so the claim's standing
  depends on this inference (load-bearing). A chose `grounds` over
  `illustrates` at A14 because the constructions "establish the claims'
  mathematical results". The wording of the inference is A's; adopting it
  is the owner's call.
---
<!-- inactive-ok-file: CASE-tmpbbfq8 CLAIM-tmp2u6bs — Proposed; the case and the claim this inference joins, filed with it -->

# ARG-tmp0kv5r: The chain and the complete graph on the same configurations show that peak-capacity thresholds do not fix cumulative transition costs

## The inference

[CASE-tmpbbfq8](../cases.d/CASE-tmpbbfq8.md) gives, for every n, two systems with the same peak
threshold between every pair of configurations and least cumulative
costs of n and 1 from one end to the other. One such pair for each n
shows that the thresholds leave the cumulative cost free up to any
factor, which is [CLAIM-tmp2u6bs](../claims.d/CLAIM-tmp2u6bs.md).

## Critical questions

- **Is the case coherent?** Yes. Both systems are finite graphs with
  stated costs on configurations and moves. The thresholds and the least
  costs follow from the definitions; the filer rechecked them by
  Dijkstra for n = 2, 3, 10, 40 and 100 on 2026-11-12, and A reported its
  own check for n = 2 to 40.
- **Does it separate the very things the conclusion says come apart?**
  Yes, for thresholds against least spend. It holds the threshold of
  every pair fixed, which is everything [CLAIM-581](../claims.d/CLAIM-581.md)'s hierarchy is made
  from, and varies only the least spend. It does not hold the move sets
  fixed. The claim does not need that: it is about what the thresholds
  determine, not about what a fixed architecture does under two
  semantics.
