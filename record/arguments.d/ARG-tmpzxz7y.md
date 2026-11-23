---
status: Rejected
title: 'Learned scroll parameters, cached so that later gestures need no fresh inference, show by analogy that a stabilized constraint expands what is realizable within a fixed per-task budget'
version: 1
form: analogy
grounds:
- CASE-tmptzhse
concludes:
- CLAIM-761
tags:
- control-theory
- learning-theory
date: '2026-11-22'
line:
- will-organization
summary: >-
  A8 §4 of the exchange "Explain First Contact RL" (ChatGPT, 2026-11-22)
  cites [CLAIM-761](../claims.d/CLAIM-761.md) for the smart-scroll case: the learned mapping "becomes a
  stable, reusable constraint" and future interactions "become easier
  without fresh inference", "amortized sensorimotor coordination". As
  support for [CLAIM-761](../claims.d/CLAIM-761.md)'s thesis, capability expansion within a fixed
  budget, the analogy fails: scrolling is feasible at every parameter
  value, so the stored mapping lowers the cost of later gestures without
  changing which are realizable. Rejected as support. [CLAIM-761](../claims.d/CLAIM-761.md)'s
  standing lives in [CLAIM-761](../claims.d/CLAIM-761.md) itself, Active, unchanged; the weaker point,
  that cached parameters amortize the cost of learning, is [CLAIM-tmpk8ude](../claims.d/CLAIM-tmpk8ude.md)'s
  (A's) and needs no further entry. The wording is the assistant's
  (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-tmptzhse CLAIM-tmpk8ude CLAIM-711 CLAIM-478 — Proposed; the case and claim filed with this argument on 2026-11-22 -->

# ARG-tmpzxz7y: Learned scroll parameters, cached so that later gestures need no fresh inference, show by analogy that a stabilized constraint expands what is realizable within a fixed per-task budget

## The inference

Premise ([CASE-tmptzhse](../cases.d/CASE-tmptzhse.md), A8 §4): an adaptive scroll interface learns, off
the critical path, a friction setting that it then applies with no
inference; later gestures need fewer corrections. Conclusion ([CLAIM-761](../claims.d/CLAIM-761.md)):
a stabilized constraint can be stored work that, by replacing later work
with cheaper operations, changes which activities are realizable within a
fixed per-task budget.

## Critical questions

1. **Are the two alike in the respect that matters?** [CLAIM-761](../claims.d/CLAIM-761.md)'s step is
   from amortization to capability: a task becomes feasible when its least
   per-task cost, the stored constraint's retrieval included, falls within
   a budget it exceeded before. In the scroll case no budget is named that
   a gesture exceeds without the learned setting; reaching a target is
   possible at any friction, at the price of more corrections. The
   respects match on cost lowered and not on feasibility changed.
2. **Is there a respect in which they differ that defeats the
   conclusion?** Yes, the one above. A case where a learned setting made
   some positioning feasible within a fixed time or effort budget that the
   default physics does not meet would restore the analogy; the case as
   proposed does not state one.
3. **Is the analogy needed?** No: what A8 wants from it, that learning can
   run slowly while its product is applied instantly, is held by
   [CLAIM-tmpk8ude](../claims.d/CLAIM-tmpk8ude.md) on [CLAIM-711](../claims.d/CLAIM-711.md) and [CLAIM-478](../claims.d/CLAIM-478.md).

Verdict: Rejected as support for [CLAIM-761](../claims.d/CLAIM-761.md). The case may still illustrate
amortization of the learning's cost.
