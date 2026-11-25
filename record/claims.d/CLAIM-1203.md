---
number: 1203
status: Active
formerly:
- CLAIM-tmpzbytm
title: "In the sequential model of inquiry depth the best depth never falls as the deadline lengthens when execution readiness is log-concave in the time left, but when execution takes either a fast or a slow route a longer deadline can make a much shallower inquiry best, because the time it saves buys the slow route"
version: 2
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the cross-partial or in the appeal to monotone comparative
  statics; or a recomputation of the bimodal example in which the best
  depth does not fall as H passes about 7.04.
tags:
- operations-research
- probabilistic-modeling
- epistemology
date: '2026-11-23'
line:
- readiness
- learning-and-inquiry
- formal-apparatus
bears_on:
- QUESTION-520
rests_on:
- CLAIM-1008
summary: >-
  A gap in A52 §3 of the exchange "Explain First Contact RL" (ChatGPT,
  2026-11-23), filled. A52 derives the first-order condition for the best
  depth of inquiry before execution ([CLAIM-1008](CLAIM-1008.md)) and concludes that
  "The appropriate depth of questioning depends on the deadline", without
  saying how. The condition is necessary only. Here: a sufficient
  condition under which the best depth rises with the deadline, and a
  checked example in which it falls sharply instead. The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
history:
- version: 2
  date: '2026-11-25'
  note: >-
    Promoted to Active under the owner's delegation of 2026-11-24
    ("handle the fixes for the twelve ... use your best judgement"),
    as the status pass of 2026-11-24 and the reruns of 2026-11-25
    applied it to independently recomputed demonstrated claims. It was
    rerun by a session other than the filer's on 2026-11-25 (scratch/formal/maintained_nuclei_check.py;
    the curation entry of 2026-11-25 02:20) and reproduced; it was then
    held back only by CLAIM-1114, which the recomputation pass of
    2026-11-25 promoted. ADR-057: it rests on CLAIM-1008, Active (promoted just before it); no objection targets it; and
    nothing meets its defeated_if.
---

# CLAIM-1203: In the sequential model of inquiry depth the best depth never falls as the deadline lengthens when execution readiness is log-concave in the time left, but when execution takes either a fast or a slow route a longer deadline can make a much shallower inquiry best, because the time it saves buys the slow route

## The gap

[CLAIM-1008](CLAIM-1008.md) (A52 §3): P(k) = p(k) F(H − t(k)), with the first-order
condition p′/p = t′ F′/F. A52 reads it as "The appropriate depth of
questioning depends on the deadline and on the target's response
dynamics." The condition is necessary for an interior maximum and can have
several solutions, so it says neither where the best depth lies nor which
way it moves with H.

## The derivation

Take logarithms: L(k, H) = log p(k) + log F(H − t(k)). Then

∂²L/∂k∂H = −t′(k) · (log F)″(H − t(k)).

- **Monotone case.** If t is nondecreasing and F is log-concave (as normal,
  exponential and gamma distribution functions of execution time with shape
  at least 1 are), the cross-partial is at least 0. L is supermodular in
  (k, H), and by Topkis's theorem the smallest and largest maximizers are
  nondecreasing in H. A longer deadline never makes a shallower inquiry
  best.
- **Unique optimum.** If in addition log p is concave and t is convex, then
  H − t(k) is concave, log F is concave and nondecreasing, and so L is
  concave in k. The maximizer is an interval, a point when either
  concavity is strict, and the first-order condition finds it.
- **Without log-concavity.** When execution takes a fast route or a slow
  one, F is a mixture with a plateau between them, log F is convex where F
  rises again after the plateau, and the cross-partial changes sign. The
  best depth can then jump down as H grows: once the deadline admits the
  slow route, cutting inquiry short to leave time for it beats inquiring
  deeply and relying on the fast route alone.

## The check

With python3 -I, p(k) = 1 − e^(−k), t(k) = k, and grid search over k.

- F the normal distribution function with mean 3 and s.d. 0.7
  (log-concave): k* = 0.77, 1.27, 1.90, 3.35, 4.93 and 8.25 at H = 4, 5,
  6, 8, 10 and 14, rising throughout.
- F = ½Φ((h − 1)/0.3) + ½Φ((h − 6)/0.3), execution taking about one day or
  about six with equal chance: k* rises to 5.02 at H = 7.0 (P = 0.496),
  then falls to 0.90 at H = 7.05 (P = 0.502), and is 1.20 at H = 7.5 and
  1.58 at H = 8.

## What it does not say

- Not that A52's conclusion is wrong. The best depth does depend on the
  deadline and on F; what this adds is the direction, and that the
  direction can reverse.
- Not that the bimodal case is typical. It shows that the rule that more time
  warrants deeper inquiry needs a condition on the target's response dynamics, which is
  the part of A52's sentence the model had not used.

## Note of 2026-11-25: rerun, and what holds it back

<!-- inactive-ok-block: CLAIM-1157 — Proposed; the premises that hold CLAIM-1008 back -->
Rerun on 2026-11-25 by the assistant, a session other than the filer's, at the owner's word ("go ahead with the reruns"; the owner delegated on 2026-11-24 the promotion of demonstrated claims independently recomputed). The filer's script was not kept, so the check was rebuilt from this entry alone as `scratch/formal/inquiry_depth_check.py`, with a negative control, and run with python3 -I. Every computation reproduces. Under the normal F, k* is 0.77, 1.27, 1.90, 3.35, 4.93 and 8.25 at H = 4, 5, 6, 8, 10 and 14; (log F)″ is negative over h in [0, 14), and k* never falls over H from 2 to 14 in steps of 0.05. Under the mixture, k* is 5.02 at H = 7.0 (P = 0.496), 0.90 at H = 7.05 (P = 0.502), 1.20 at 7.5 and 1.58 at 8; it rises over H from 6 to 7, first drops at H = 7.035 (the entry's "about 7.04"), and (log F)″ is positive on part of (2, 7), where the cross-partial changes sign. The normal F is the control for the mixture: the same search finds no fall. What holds it back: [ADR-057](../decisions.d/ADR-057.md)'s first criterion. Its one premise, [CLAIM-1008](CLAIM-1008.md), is Proposed (rerun today and reproduced, but held by [CLAIM-1157](CLAIM-1157.md) and that by [CLAIM-1114](CLAIM-1114.md)). It goes Active after [CLAIM-1008](CLAIM-1008.md). The note is the assistant's (Claude, in this session). No status change.
