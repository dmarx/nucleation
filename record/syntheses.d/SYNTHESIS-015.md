---
number: 15
status: Proposed
formerly:
- SYNTHESIS-tmp9cgig
title: 'Anchoring has costs and a price: an early anchor can entrench its framing, and iterative retrieval can turn a framing into a premise, though adaptive search is not biased in itself; filing moves work across time and pays only when reuse covers it, recurrence weighted by reconstruction cost is a worst-case guarantee where reuse cannot be forecast, and recognizing what a filed argument answers has a cost that grows with what is stored'
version: 2
history:
- version: 2
  date: '2026-11-10'
  note: >-
    Three components added after ADR-085's sweep gave them this line:
    CLAIM-315 and QUESTION-323, which bear on and refine QUESTION-109,
    and QUESTION-095, which refines QUESTION-098. No component already
    here mentions any of them, so each is set out through its own
    relation, and the link that would join CLAIM-315 to CLAIM-184 and
    CLAIM-301 goes under what is not stated. Nothing else changes.
defeated_if: >-
  A component misstated or misattributed
  here; an in-force component of the costs part of nucleating-argument
  left out; or a link this account states that no component states. Its
  standing is its components'.
tags:
- design-rationale
- epistemology
- information-retrieval
date: '2026-11-07'
line:
- nucleating-argument
integrates:
- CLAIM-184
- CLAIM-301
- CLAIM-292
- QUESTION-109
- QUESTION-107
- QUESTION-172
- CLAIM-179
- CLAIM-303
- CLAIM-308
- CLAIM-314
- CASE-088
- QUESTION-098
- QUESTION-237
- CLAIM-315
- QUESTION-323
- QUESTION-095
---
<!-- inactive-ok-file: ADR-083 CLAIM-179 CLAIM-182 CLAIM-184 CLAIM-301 CLAIM-298 CLAIM-303 CLAIM-308 CLAIM-314 CLAIM-315 — Proposed; components and citations, with their standing -->

# SYNTHESIS-015: Anchoring has costs and a price: an early anchor can entrench its framing, and iterative retrieval can turn a framing into a premise, though adaptive search is not biased in itself; filing moves work across time and pays only when reuse covers it, recurrence weighted by reconstruction cost is a worst-case guarantee where reuse cannot be forecast, and recognizing what a filed argument answers has a cost that grows with what is stored

*A part account of the nucleating-argument line ([ADR-083](../decisions.d/ADR-083.md), version 2); the line's account is built over it and its two sibling parts.*

## The account

**Costs.**

- [CLAIM-184](../claims.d/CLAIM-184.md) (the assistant's; counter, interpretive, Proposed): anchors
  entrench. Its note of 2026-11-06 reports the count: superseded anchors stop
  attracting new structure on this record. Its first half is unshown.
- [CLAIM-301](../claims.d/CLAIM-301.md) (A's; thesis, interpretive, Proposed): iterative retrieval can
  turn a provisional interpretation into a premise, giving [CLAIM-184](../claims.d/CLAIM-184.md) a route.
- [CLAIM-292](../claims.d/CLAIM-292.md) (A's; granted, demonstrated, Active): adaptive search is not
  biased in itself, filed against [CLAIM-301](../claims.d/CLAIM-301.md).
- [QUESTION-109](../questions.d/QUESTION-109.md) (A's, Open) sets [CLAIM-184](../claims.d/CLAIM-184.md)'s cost against [CLAIM-182](../claims.d/CLAIM-182.md)'s
  benefit, and [QUESTION-107](../questions.d/QUESTION-107.md) (A's, Open) refines it from one retrieval to a
  sequence. [QUESTION-172](../questions.d/QUESTION-172.md) (Open) is here because [CLAIM-184](../claims.d/CLAIM-184.md) grounds on
  [THEORY-178](../theory.d/THEORY-178.md).
- CLAIM-315 (the record's split of CLAIM-298 under ADR-043; thesis,
  empirical, Proposed; first line pragmatic-transport) bears on
  QUESTION-109. In comparative anchoring tasks an anchor shifts a later
  estimate without adding evidence about the target, and the shift is
  "carried by anchor-consistent knowledge made more accessible"; "the
  shift is established, the accessibility step is inferred and has not
  been measured". QUESTION-323 (Open; first line pragmatic-transport), a
  promotion condition moved from THEORY-335, refines QUESTION-109 and asks
  for that measurement: whether anchor-consistent knowledge is more
  accessible "on a measure first shown sensitive to direct priming", and
  whether the difference goes with the size of the shift.

**Price.**

- [CLAIM-179](../claims.d/CLAIM-179.md) (the assistant's; thesis, interpretive, Proposed): agent filing
  moves the cost of capture to the party that would re-derive; "The
  disparity does not disappear. It moves."
- [CLAIM-303](../claims.d/CLAIM-303.md) (A's; thesis, interpretive, Proposed): filing moves work across
  time, and recurrence "is evidence of reuse, not the criterion". [CASE-088](../cases.d/CASE-088.md)
  (A's, Active) works its arithmetic.
- [CLAIM-308](../claims.d/CLAIM-308.md) (counter, demonstrated, Proposed), against [CLAIM-303](../claims.d/CLAIM-303.md): where reuse
  cannot be forecast, the break-even rule is within 2 − (c_a + u)/c_r of
  hindsight. It concedes [CLAIM-314](../claims.d/CLAIM-314.md).
- [CLAIM-314](../claims.d/CLAIM-314.md) (counter, interpretive, Proposed), against [CLAIM-308](../claims.d/CLAIM-308.md):
  recognizing what a filed argument answers has a cost that grows with what
  is stored, so per-item decisions are not independent.
- [QUESTION-098](../questions.d/QUESTION-098.md) (the owner's U11 and A11, Open) asks when filing is worth
  it. [QUESTION-237](../questions.d/QUESTION-237.md) (Open) is a promotion condition moved from [THEORY-376](../theory.d/THEORY-376.md).
- QUESTION-095 (the owner's, 2026-10-15, Open; first line
  distributed-agency) refines QUESTION-098. It asks whether leaving a
  result where it can be cheaply retrieved is "the same trade as
  amortizing the computation", with CLAIM-303's filing as one of three
  instances, beside a crew's speed bugs and availability computed before
  a request. Its notes register literatures that price parts of the
  trade, among them an erosion of the internal route under offloading, "a
  cost CLAIM-303's fixed reconstruction cost leaves out".

## Links tested as claims

None is filed as a claim: the links are held as `complements`, `objects_to`, `refines`
and `illustrates` relations and in the bodies cited. Two candidates were
tested.

- **[CLAIM-184](../claims.d/CLAIM-184.md)'s count against [CLAIM-303](../claims.d/CLAIM-303.md)'s second defeater** ("upkeep and
  stale reuse are negligible"): one step from the count, reaching neither
  upkeep nor stale entries never retired. A note on [CLAIM-303](../claims.d/CLAIM-303.md), not a
  synthesis.
- **[CLAIM-314](../claims.d/CLAIM-314.md)'s store-level cost as the basis of the second-occurrence
  throttle:** the throttle is itself an item-by-item rule, and nothing shows
  it bounds the cost [CLAIM-314](../claims.d/CLAIM-314.md) says such rules cannot see.

## Not stated on the record

- What [CLAIM-184](../claims.d/CLAIM-184.md)'s count does to [CLAIM-303](../claims.d/CLAIM-303.md)'s staleness term.
- Whether the second-occurrence throttle bounds [CLAIM-314](../claims.d/CLAIM-314.md)'s store-level
  cost.
- Which claim [QUESTION-237](../questions.d/QUESTION-237.md) bears on.
- Whether CLAIM-315's accessibility step, if QUESTION-323 finds it, is the
  route by which an early anchor entrenches (CLAIM-184) or by which
  retrieval turns a framing into a premise (CLAIM-301). No component
  names the other.
- Whether the erosion QUESTION-095's notes record belongs in CLAIM-303's
  break-even or CLAIM-308's bound.

## What it does not say

- That the record's filing pays: nothing measures reuse or recognition cost
  on the record.
- That an early anchor has locked in a framing here.
- Anything with standing of its own.
