---
status: Open
title: 'Formalize the will-organization as the state of the grant scheme'
stage: idea
priority: medium
method:
- formal
- conceptual
tags:
- self-governance
- agency
- mathematics
date: '2026-11-26'
line:
- will-organization
- formal-apparatus
advances:
- TERM-023
- CLAIM-tmpic0m1
- CLAIM-tmphyvh3
summary: >-
  The owner, 2026-11-26: "I thought we had a fairly rigorous formalization
  that satisfied this kind of "authority structure" already ... we probably
  still need to formalize what we mean by "organization" or "architecture"
  as well". The record has both halves and no bridge between them:
  [TERM-023](../terms.d/TERM-023.md) defines the will-organization in words, and the
  distributed-agency line's grant scheme is a formal model of influence
  allocation, but no entry says the one realizes the other. The wording is
  the assistant's (Claude, in this session); adopting it is the owner's
  call.
---
<!-- inactive-ok-file: CLAIM-tmpic0m1 CLAIM-tmphyvh3 — new; the claims this lead would ground -->
<!-- inactive-ok-file: CLAIM-918 SYNTHESIS-050 SYNTHESIS-087 — Proposed; the formal results it would draw on -->

# LEAD-tmpuszbx: Formalize the will-organization as the state of the grant scheme

## What the record holds

- **The concept.** [TERM-023](../terms.d/TERM-023.md) (Active): "the maintained organization of
  relations governing the conditions under which an agent's available
  action-generating regimes acquire, retain, lose, or alter practical
  efficacy", with accessibility, precedence and persistence, and
  [TERM-017](../terms.d/TERM-017.md)'s precedence, jurisdiction and suspension, plus transformation.
- **"Organization."** [TERM-074](../terms.d/TERM-074.md) (Active) separates four senses: relational
  arrangement, organizational maintenance, collective institution and
  organizational closure. It disambiguates the word without formalizing
  it.
- **The formal model.** The distributed-agency line's grant scheme gives
  operators claimed priority p_i and granted influence I_i ([CLAIM-283](../claims.d/CLAIM-283.md)),
  grants through maintained relations ([TERM-101](../terms.d/TERM-101.md)) and conferral in general
  ([TERM-103](../terms.d/TERM-103.md)), accounting rules for authority (one-hop allocation within
  an epoch, damped recursive delegation; [CLAIM-282](../claims.d/CLAIM-282.md), [CLAIM-375](../claims.d/CLAIM-375.md),
  [SYNTHESIS-087](../syntheses.d/SYNTHESIS-087.md)), its scoring ([SYNTHESIS-050](../syntheses.d/SYNTHESIS-050.md)), softmax shares learned by
  gradient ([CLAIM-918](../claims.d/CLAIM-918.md)), and a learned prior over which processes govern
  ([CLAIM-443](../claims.d/CLAIM-443.md)).

No entry states that the grant scheme's state is a will-organization, or
which of [TERM-023](../terms.d/TERM-023.md)'s dimensions it represents.

## What it would do

1. **Map the dimensions.** For each of [TERM-023](../terms.d/TERM-023.md)'s dimensions, say which
   quantity of the grant scheme represents it, or that none does. A first
   guess, to be checked against the claims:
   - Precedence is I_i, with p_i as the claim.
   - Jurisdiction is influence indexed by contest domain, if the scheme
     has it.
   - Suspension is a grant withheld or revoked.
   - Transformation is the learning rule ([CLAIM-918](../claims.d/CLAIM-918.md), [CLAIM-443](../claims.d/CLAIM-443.md)).
   - Accessibility and persistence have no obvious counterpart.
2. **State "organization" formally** in [TERM-074](../terms.d/TERM-074.md)'s first two senses: the
   arrangement as the scheme's state (the grant relations and the
   accounting rule), and maintenance as its update rule.
3. **Compute valence from it.** With rankings added, derive the ordering
   contests would be settled along ([CLAIM-tmphyvh3](../claims.d/CLAIM-tmphyvh3.md)'s disposition) from the
   scheme's state alone. Check it against [TERM-076](../terms.d/TERM-076.md) on simulated
   negotiations of two or three perspectives: the scenarios of the
   workbench entry of 2026-11-26 (170642).

## What would settle it

A mapping with every dimension placed or shown absent, and one computed
case in which the same scheme state with two different sets of rankings
yields two valences, and two different scheme states with the same
rankings yield two valences. [CLAIM-tmpic0m1](../claims.d/CLAIM-tmpic0m1.md) needs both directions.

"Will architecture" is not proposed as a term. It would duplicate
[TERM-074](../terms.d/TERM-074.md)'s sense 1.
