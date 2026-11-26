---
number: 15
status: Proposed
formerly:
- SYNTHESIS-tmp9cgig
title: 'Anchoring entrenches; filing pays only on reuse'
statement: >-
  Anchoring has costs and a price: an early anchor can entrench its framing,
  and iterative retrieval can turn a framing into a premise, though adaptive
  search is not biased in itself; filing moves work across time and pays
  only when reuse covers it, recurrence weighted by reconstruction cost is a
  worst-case guarantee where reuse cannot be forecast, and recognizing what
  a filed argument answers has a cost that grows with what is stored; the
  price extends from filing to how available a filed entry is kept, but
  only over the set kept in easy reach, and the worst-case bound does not
  extend with it
version: 3
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
- version: 3
  date: '2026-11-26'
  note: >-
    Revised to take the exchange "Alignment consequences brainstorm"
    (ChatGPT, 2026-11-26) into account, under ADR-151, and rewritten from
    an inventory into one argument. Added CLAIM-tmpg2wk1, ARG-tmpedexz,
    CLAIM-tmpdid0k, CLAIM-tmp6toz6 and CLAIM-tmpyk9r5, which carry the
    price of filing over to the price of availability; the design of
    controlled forgetting they belong to is SYNTHESIS-017's. The audit of
    candidate links is dropped from the body; it is in version 2 and the
    curation entry of 2026-11-07. The title is unchanged.
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
- CLAIM-tmpg2wk1
- ARG-tmpedexz
- CLAIM-tmpdid0k
- CLAIM-tmp6toz6
- CLAIM-tmpyk9r5
---
<!-- inactive-ok-file: CLAIM-179 CLAIM-184 CLAIM-301 CLAIM-314 CLAIM-315 — Proposed; components and citations, with their standing -->
<!-- inactive-ok-file: THEORY-1736 — filed from the exchange "luria experiment design", Proposed or Deferred; cited as filed alongside this entry -->
<!-- inactive-ok-file: CLAIM-tmpg2wk1 ARG-tmpedexz CLAIM-tmpdid0k CLAIM-tmp6toz6 CLAIM-tmpyk9r5 CLAIM-tmpu1fef CLAIM-tmp8gkmi SYNTHESIS-016 SYNTHESIS-017 ADR-151 — Proposed or Open; filed from the exchange "Alignment consequences brainstorm" on 2026-11-26, the syntheses it is read beside, and the decision on how a synthesis is written -->

# SYNTHESIS-015: Anchoring entrenches; filing pays only on reuse

*A synthesis of the costs part of the nucleating-argument line ([ADR-083](../decisions.d/ADR-083.md)); the line's synthesis, [SYNTHESIS-016](SYNTHESIS-016.md), is built over it and its two sibling parts. Version 3 takes the exchange "Alignment consequences brainstorm" (ChatGPT, 2026-11-26) into account, under [ADR-151](../decisions.d/ADR-151.md); what the record may forget is [SYNTHESIS-017](SYNTHESIS-017.md)'s. It adds nothing. Its standing is its components'.*

## The question

Anchoring an argument has costs as well as benefits. What do anchors cost
the inquiry built on them, and when is filing something worth what it
costs?

## The argument

**Anchors can entrench, and retrieval gives them a route.** The
assistant's counter is that anchors entrench an early framing
([CLAIM-184](../claims.d/CLAIM-184.md)); its count of 2026-11-06 found that superseded anchors stop
attracting new structure on this record, and its first half, that an
early anchor makes alternatives hard to reach, is unshown. Iterative
retrieval can turn a provisional interpretation into a premise, which
gives entrenchment a route ([CLAIM-301](../claims.d/CLAIM-301.md)), though adaptive search is not
biased in itself ([CLAIM-292](../claims.d/CLAIM-292.md), demonstrated, against [CLAIM-301](../claims.d/CLAIM-301.md)). In
comparative anchoring tasks an anchor shifts a later estimate without
adding evidence about the target, the accessibility step inferred and not
measured ([CLAIM-315](../claims.d/CLAIM-315.md)); [QUESTION-323](../questions.d/QUESTION-323.md) asks for that measurement, and
[QUESTION-109](../questions.d/QUESTION-109.md) and [QUESTION-107](../questions.d/QUESTION-107.md) set the cost of entrenchment against the
benefit of anchoring, for one retrieval and for a sequence. [QUESTION-172](../questions.d/QUESTION-172.md)
is here because [CLAIM-184](../claims.d/CLAIM-184.md) grounds on [THEORY-178](../theory.d/THEORY-178.md). The exchange added the
retrieval-side form of the danger: the record's generated views repeat an
entry across indexes, tag pages, chains and syntheses, a median of 25
generated pages per claim, so a search meets one entry many times and
it gains prominence that is not evidence ([CLAIM-tmp6toz6](../claims.d/CLAIM-tmp6toz6.md)). Whether
retiring an anchor removes its cost is a separate question: [CLAIM-184](../claims.d/CLAIM-184.md) asks
whether a retired anchor stops attracting growth, the owner's point is
that it goes on costing attention even if it does ([CLAIM-184](../claims.d/CLAIM-184.md), note of
2026-11-26, on [CLAIM-tmpu1fef](../claims.d/CLAIM-tmpu1fef.md)).

**Filing moves work across time, and pays only on reuse.** Agent filing
moves the cost of capture to the party that would otherwise re-derive
([CLAIM-179](../claims.d/CLAIM-179.md)). Filing moves work across time, and recurrence is evidence of
reuse, not the criterion ([CLAIM-303](../claims.d/CLAIM-303.md), its arithmetic worked in [CASE-088](../cases.d/CASE-088.md)).
Where reuse cannot be forecast, filing once repeated reconstruction would
exceed its cost is within a constant factor of hindsight ([CLAIM-308](../claims.d/CLAIM-308.md),
demonstrated, against [CLAIM-303](../claims.d/CLAIM-303.md)). But recognizing what a filed argument
answers costs more as more is stored, so the decision for one item is not
independent of the rest ([CLAIM-314](../claims.d/CLAIM-314.md), against [CLAIM-308](../claims.d/CLAIM-308.md), which concedes
it). When filing is worth it is the owner's question ([QUESTION-098](../questions.d/QUESTION-098.md)), and
whether leaving a result where it can be cheaply retrieved is the same
trade as amortizing a computation is its refinement ([QUESTION-095](../questions.d/QUESTION-095.md));
[QUESTION-237](../questions.d/QUESTION-237.md) is a promotion condition moved from [THEORY-376](../theory.d/THEORY-376.md).

**The price carries over from filing to availability, but not entry by
entry.** [CLAIM-303](../claims.d/CLAIM-303.md) prices filing, and an entry once filed is never priced
again; the owner's point about the record's size is the case it does not
cover ([CLAIM-303](../claims.d/CLAIM-303.md), note of 2026-11-26). A extends it into a cost for each
tier of availability: maintenance, retrieval noise, expected
reactivation, expected loss while unavailable, and transition
([CLAIM-tmpg2wk1](../claims.d/CLAIM-tmpg2wk1.md)). Because [CLAIM-314](../claims.d/CLAIM-314.md) makes the attention an entry costs a
property of the whole corpus, the extension holds only with the noise
term taken over the set kept in easy reach ([ARG-tmpedexz](../arguments.d/ARG-tmpedexz.md)). [CLAIM-308](../claims.d/CLAIM-308.md)'s
reconstruction-weighted rule transfers as a family of retention policies,
and its bound does not: the bound is for a one-way decision under fixed
costs, and a tier can be changed back ([CLAIM-308](../claims.d/CLAIM-308.md), note of 2026-11-26). A
states the net effect [CLAIM-314](../claims.d/CLAIM-314.md) gives a mechanism for: past some point,
growth of the accessible corpus raises the cost of realizing what the
corpus already supports by more than holding it saved ([CLAIM-tmpdid0k](../claims.d/CLAIM-tmpdid0k.md)),
the limit [QUESTION-095](../questions.d/QUESTION-095.md) asks about. Condensing may also earn more than it
saves: condensation that preserves capability may widen the inquiry
frontier, [CLAIM-761](../claims.d/CLAIM-761.md)'s stored work applied to forgetting ([CLAIM-tmpyk9r5](../claims.d/CLAIM-tmpyk9r5.md),
with [CLAIM-tmp8gkmi](../claims.d/CLAIM-tmp8gkmi.md) in [SYNTHESIS-017](SYNTHESIS-017.md)).

## Where it stands

The price of filing is the firm part: [CLAIM-303](../claims.d/CLAIM-303.md) and its arithmetic case
([CASE-088](../cases.d/CASE-088.md)), [CLAIM-308](../claims.d/CLAIM-308.md)'s demonstrated bound and [CLAIM-292](../claims.d/CLAIM-292.md) are in force.
[CLAIM-314](../claims.d/CLAIM-314.md)'s objection and everything on entrenchment are Proposed. Nothing
measures reuse or recognition cost on the record. The exchange's
extensions are A's hypotheses, narrowed by the assistant, and unmeasured;
a trial of one line's working view against the full retrieval surface at
a fixed budget would give [CLAIM-314](../claims.d/CLAIM-314.md) its measure ([LEAD-tmpolbqp](../leads.d/LEAD-tmpolbqp.md); [CLAIM-314](../claims.d/CLAIM-314.md),
note of 2026-11-26).

## Not stated on the record

- What [CLAIM-184](../claims.d/CLAIM-184.md)'s count does to [CLAIM-303](../claims.d/CLAIM-303.md)'s staleness term.
- Whether the second-occurrence throttle bounds [CLAIM-314](../claims.d/CLAIM-314.md)'s store-level
  cost.
- Which claim [QUESTION-237](../questions.d/QUESTION-237.md) bears on.
- Whether [CLAIM-315](../claims.d/CLAIM-315.md)'s accessibility step, if [QUESTION-323](../questions.d/QUESTION-323.md) finds it, is the
  route by which an early anchor entrenches ([CLAIM-184](../claims.d/CLAIM-184.md)) or by which
  retrieval turns a framing into a premise ([CLAIM-301](../claims.d/CLAIM-301.md)).
- Whether the erosion [QUESTION-095](../questions.d/QUESTION-095.md)'s notes record belongs in [CLAIM-303](../claims.d/CLAIM-303.md)'s
  break-even or [CLAIM-308](../claims.d/CLAIM-308.md)'s bound.
- **A competitive bound for tiers.** [CLAIM-308](../claims.d/CLAIM-308.md)'s note says its bound does
  not carry over; no entry states the bound that would hold for a tier
  that can be changed back.
- **Projection prominence as entrenchment.** [CLAIM-tmp6toz6](../claims.d/CLAIM-tmp6toz6.md)'s repeated
  meeting of one entry resembles the route [CLAIM-301](../claims.d/CLAIM-301.md) gives [CLAIM-184](../claims.d/CLAIM-184.md); no
  entry says that generated views entrench.

## What it does not say

That the record's filing pays, that an early anchor has locked in a
framing here, or that keeping fewer entries in reach would help. Park et
al. ([THEORY-1736](../theory.d/THEORY-1736.md)) is a converse failure, agents with no anchoring at all,
and evidence for neither side.
