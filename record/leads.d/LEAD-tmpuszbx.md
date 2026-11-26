---
status: Open
title: 'Formalize the will-organization as the state of the grant scheme'
stage: underway
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
- CLAIM-tmpzzeqo
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
<!-- inactive-ok-file: CLAIM-tmpic0m1 CLAIM-tmphyvh3 CLAIM-tmpzzeqo — new; the claims this lead would ground -->
<!-- inactive-ok-file: CLAIM-918 CLAIM-446 SYNTHESIS-050 SYNTHESIS-087 — Proposed; the formal results it would draw on -->

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

## The mapping (2026-11-26)

The will-organization's state, as the grant scheme can carry it, is

  W_t = (I⁰, b, E, R, τ, γ, α)

| [TERM-023](../terms.d/TERM-023.md) dimension | Quantity | Held by | Status |
|---|---|---|---|
| Precedence ([TERM-017](../terms.d/TERM-017.md): which applicable constraint controls) | influence I_j(r) = I⁰_j(r) + Σ_{i≠j} b_i E_ij(r), against the claim p_j | [CLAIM-282](../claims.d/CLAIM-282.md), [CLAIM-283](../claims.d/CLAIM-283.md) | held, once E is indexed by region |
| Jurisdiction, inner ([TERM-017](../terms.d/TERM-017.md): which constraints apply to a case) | the region r a contest falls in, and the support of I(·, r) | [TERM-103](../terms.d/TERM-103.md)'s C_ij(x, t) is region-indexed; [CLAIM-282](../claims.d/CLAIM-282.md)'s E is not | **gap**: E needs a region index, E_ij(r) |
| Jurisdiction, outer ([TERM-047](../terms.d/TERM-047.md): which regimes W governs) | the regimes whose response kernels move under interventions on W | [TERM-067](../terms.d/TERM-067.md)'s governance-response profile | held, as a test |
| Suspension ([TERM-017](../terms.d/TERM-017.md): when an applicable constraint may be disabled) | a context gate γ_j(c) ∈ [0, 1] on I_j, set by a tolerance Q_{i→j}(y, c) = 1[d_i(y, c) ≤ τ_{i→j}(c)] | [CLAIM-552](../claims.d/CLAIM-552.md) holds the criterion; revocation of R_ij ([TERM-101](../terms.d/TERM-101.md)) is suspension between epochs | **gap**: no in-epoch gate in the scheme |
| Accessibility | an admission variable α_j(r) ∈ [0, 1]: whether j's contribution reaches settlement at all | [CLAIM-349](../claims.d/CLAIM-349.md) (access separate from authority), [CLAIM-448](../claims.d/CLAIM-448.md) (admitted contests) | **gap**: nothing formal |
| Persistence | the decay λ and the epoch length: how long efficacy, once granted, is retained | [CLAIM-443](../claims.d/CLAIM-443.md)'s −λE_ji; [CLAIM-282](../claims.d/CLAIM-282.md)'s epochs | partly held; resumption after interruption is not modelled |
| Transformation | the update map Φ: W_{t+1} = Φ(W_t, settlements_t) | the between-epoch update ([CLAIM-282](../claims.d/CLAIM-282.md)), Hebbian ΔE ([CLAIM-443](../claims.d/CLAIM-443.md)), softmax gradient ([CLAIM-918](../claims.d/CLAIM-918.md)) | held |

**"Organization."** [TERM-074](../terms.d/TERM-074.md)'s sense 1, the relational arrangement, is W_t.
Its sense 2, maintenance, is Φ. Its distinction between an arrangement
maintained by its own activity and one reset from outside ([CLAIM-414](../claims.d/CLAIM-414.md)) is
whether Φ is driven by the organization's own settlements or by an
exogenous reset. The will-organization is then the pair (W_t, Φ),
agent-indexed as [TERM-023](../terms.d/TERM-023.md) requires.

**The would-prevail relation.** Given rankings ≿_k, a pair (s, t) is
*contestable* when the rankings disagree on it. It is settled in its
region r and context c by influence-weighted vote with weights
α_k(r) γ_k(c) I_k(r). The relation of winning moves over all contestable
pairs is [CLAIM-tmphyvh3](../claims.d/CLAIM-tmphyvh3.md)'s disposition. It is computed from W_t and the
rankings alone, and no contest needs to occur. The system has valence
when that relation is acyclic ([CLAIM-434](../claims.d/CLAIM-434.md)), and [TERM-076](../terms.d/TERM-076.md)'s kind clause is a
further check.

## First computation (2026-11-26)

scratch/studies/lead-tmpuszbx/would_prevail.py, run with `python3 -I`, on
three states and two or three perspectives:

1. An arbiter grants all its budget to P1: the potential is P1's ranking.
2. The same rankings, with the arbiter granting to P2: the potential is
   P2's ranking. So a different W with the same rankings gives a different
   valence.
3. W as in 1, with P1's ranking changed: a different potential. So the
   same W with different rankings gives a different valence. Cases 1 to 3
   meet the condition below in both directions, on a toy.
4. Equal influence and Condorcet rankings among three: cyclic, so no
   valence.
5. Rankings that agree on every pair: no contestable pair, so valence is
   absent even dispositionally. This narrows [CLAIM-tmphyvh3](../claims.d/CLAIM-tmphyvh3.md) (version 2).
6. A jurisdiction split over shared states, with every pair contested:
   cyclic. 6a: with one agreed pair, a potential that is nobody's ranking.
   6′: one perspective holding all pairs recovers its ranking. Filed as
   [CLAIM-tmpzzeqo](../claims.d/CLAIM-tmpzzeqo.md).
7. Suspension, where P1 dominates when calm and is gated off under threat:
   the potential switches from P1's ranking to P2's. That is the workbench
   entry's context switching, and [CLAIM-446](../claims.d/CLAIM-446.md)'s threat regime, made formal.

## What remains

- **Close the three gaps.** Index E by region, add the gate γ, and add the
  admission α. Check each against the claims that hold the grant scheme's
  results ([CLAIM-282](../claims.d/CLAIM-282.md), [CLAIM-375](../claims.d/CLAIM-375.md), [CLAIM-918](../claims.d/CLAIM-918.md), [SYNTHESIS-050](../syntheses.d/SYNTHESIS-050.md), [SYNTHESIS-087](../syntheses.d/SYNTHESIS-087.md)),
  so that adding a dimension does not break a result proved without it.
- **Persistence and resumption.** Frijda's resumption after interruption
  needs a state carried across epochs that the decay does not erase.
  [CLAIM-443](../claims.d/CLAIM-443.md)'s prior is the candidate.
- **Settlement rules.** The computation uses influence-weighted vote, with
  no claim term. Add [CLAIM-283](../claims.d/CLAIM-283.md)'s case of a claim outrunning its grant (a
  term in p_k) and see which results survive.
- **Sen is held** (LIT-285, NOTE-255, THEORY-027). It is compared with CLAIM-tmpzzeqo in that claim's note of 2026-11-26.

## What would settle it

A mapping with every dimension placed or shown absent, and one computed
case in which the same scheme state with two different sets of rankings
yields two valences, and two different scheme states with the same
rankings yield two valences. [CLAIM-tmpic0m1](../claims.d/CLAIM-tmpic0m1.md) needs both directions. The
second condition is met on a toy (cases 1 to 3). The first is met except
for the three gaps, and for resumption under persistence.

"Will architecture" is not proposed as a term. It would duplicate
[TERM-074](../terms.d/TERM-074.md)'s sense 1.
