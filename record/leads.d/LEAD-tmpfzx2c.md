---
status: Open
title: 'Price the provider''s side of the decaying fallback: with the supplier''s cost of supply in the model, find whether it prefers to supply past the party''s capacity deadline, and under which supply rules'
version: 1
stage: idea
method:
- formal
tags:
- game-theory
- society-and-governance
- complex-systems
date: '2026-11-25'
line:
- dependence-and-domination
- transient-support
advances:
- CLAIM-tmp6nzs1
- CLAIM-670
- CLAIM-605
summary: >-
  From the manuscript governance-of-becoming, Article 9 §9.4 (gap G9.2,
  filed under write-manuscript step 6). [CLAIM-tmp6nzs1](../claims.d/CLAIM-tmp6nzs1.md) computes the
  party's terms falling as substitutive supply erodes its fallback, with
  supply exogenous; R's cost of supplying, and so whether R would choose
  to supply past [CLAIM-605](../claims.d/CLAIM-605.md)'s deadline, is not modelled. That is the step
  from produced dependence to a provider that gains by producing it,
  which [CLAIM-670](../claims.d/CLAIM-670.md) states in prose. The wording is the assistant's
  (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmp6nzs1 CLAIM-670 TERM-123 TERM-124 — Proposed or new; the computation this extends, the claim it would model, the bargaining case, and the terms a verdict would need -->

# LEAD-tmpfzx2c: Price the provider's side of the decaying fallback: with the supplier's cost of supply in the model, find whether it prefers to supply past the party's capacity deadline, and under which supply rules

## The gap

[CLAIM-tmp6nzs1](../claims.d/CLAIM-tmp6nzs1.md)'s "What it does not say": "Supply is exogenous. R's cost of
supplying, and so whether R would choose to supply past the deadline, is
not modelled." [CLAIM-670](../claims.d/CLAIM-670.md) holds in prose that an arrangement "can produce
the dependence through which it exploits", and the provider "can use
that reliance to set terms the party could earlier have refused". No
entry has the provider choose.

## What it would take

1. **Give R a cost.** In the script under
   scratch/manuscripts/governance-of-becoming/analysis/, let R pay c per
   unit time of supply, and let supply be R's choice: a duration T, or a
   rule (substitutive or capacity-first, at a level A), fixed before the
   bargain or renegotiated each period.
2. **R's payoff.** R's share of S over the horizon, minus the cost of
   supply, with the Nash split against P's decaying fallback as in
   [CLAIM-tmp6nzs1](../claims.d/CLAIM-tmp6nzs1.md).
3. **The question.** For which c, and which discount rates, R's best T
   lies past [CLAIM-605](../claims.d/CLAIM-605.md)'s deadline (3.098 in its parameters), and whether
   R prefers substitutive to capacity-first supply when both cost the
   same.
4. **A control.** The same with P's fallback held fixed: R should then
   have no reason to prolong supply beyond what it is paid for.

## What would count

R choosing to supply past the deadline where the fixed-fallback control
gives it no such reason shows, in the model, an incentive to produce the
dependence, which is [CLAIM-670](../claims.d/CLAIM-670.md)'s mechanism with a motive. If R never
gains by it at any cost of supply, the produced dependence is a side
effect in this model, not a strategy. Neither is exploitation or
domination without a declared standard ([TERM-123](../terms.d/TERM-123.md), [TERM-124](../terms.d/TERM-124.md)).

## Standing

Open, at stage idea. Checked first: no held lead models the provider's
side; [LEAD-tmpeo8wq](LEAD-tmpeo8wq.md) concerns the party's reach, not the provider's
choice.
