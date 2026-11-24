---
status: Proposed
title: "The stored-work cost model of the three priced cases, applied to a contract as a store by formal application, prices its formation, upkeep, recognition, checking and revision but not an invocation that changes the store, so the model needs invocation to return the contract's next state"
version: 1
form: formal-application
rests_on:
- CLAIM-761
- CLAIM-569
grounds:
- CASE-326
concludes:
- CLAIM-tmpsf9hp
tags:
- operations-research
- society-and-governance
date: '2026-11-24'
line:
- realizability
summary: >-
  A30 §§2 and 15 of the exchange 'Memes, Contracts, and Systemic
  Normativity' (ChatGPT, 2026-11-24) maps [CASE-326](../cases.d/CASE-326.md)'s terms onto a contract's
  lifecycle and finds them sufficient for formation, upkeep, recognition,
  verification and revision, but says "the current [CASE-326](../cases.d/CASE-326.md) implementation
  uses fixed erosion and does not establish the full endogenous contractual
  dynamics described here." This ARG holds that support judgement: the
  mapping holds, and one assumption fails in the new domain. The
  conclusion's standing is [CLAIM-tmpsf9hp](../claims.d/CLAIM-tmpsf9hp.md)'s. The inference is A's; the
  answers to the critical questions are the assistant's (Claude, in this
  session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-326 CLAIM-tmp80ny9 CLAIM-tmpsf9hp — Proposed or new; this filing's entries and the held entries it maps to, cited with their standing -->

# ARG-tmpa5ped: The stored-work cost model of the three priced cases, applied to a contract as a store by formal application, prices its formation, upkeep, recognition, checking and revision but not an invocation that changes the store, so the model needs invocation to return the contract's next state

## The inference

[CASE-326](../cases.d/CASE-326.md) prices a served demand on the store route as

    ρ + v + σ[δ(c(1+ε) + R + σ_A L_A) + (1 − δ)L],

with construction F and upkeep U beside it. A30 §2 quotes the formula
exactly (checked against [CASE-326](../cases.d/CASE-326.md) on 2026-11-24) and reads each term
contractually: F as formation, U as maintenance of expectations, π as the
chance an existing contract serves the demand, ρ as identifying and
invoking it, v and δ as checking applicability and compliance, σ as the
chance inherited arrangements are inadequate, R as renegotiation, ε as the
loss of independent capability through reliance. "Read contractually,
this describes the cost of reusing an established arrangement rather than
resolving the relationship anew." So the lifecycle is priced. A30 §6
applies [CLAIM-303](../claims.d/CLAIM-303.md)'s break-even, F + n(ρ + v + u) < nc, so n > F/(c − ρ − v
− u) when the denominator is positive (checked: at A30's slider values F
= 24, c = 8, ρ + v = 2, u = 1, n > 4.8).

The invocation is not priced: the model's store is the same before and
after a use, and σ and ε enter as fixed parameters. A contract's
invocation can change it ([CLAIM-tmpsf9hp](../claims.d/CLAIM-tmpsf9hp.md)). So the model applies to
contracts once invocation returns the next contractual state.

## Critical questions

- **Does the mapping premise hold?** For the lifecycle, yes: a contract is
  a stabilized constraint ([CLAIM-761](../claims.d/CLAIM-761.md)), and [CLAIM-569](../claims.d/CLAIM-569.md)'s three requirements
  are its formation, persistence and exit. One part of the mapping is
  loose: A30 maps ρ to "identifying and invoking the contract", but the
  cost of resolving which relationship applies ([CLAIM-tmp80ny9](../claims.d/CLAIM-tmp80ny9.md)) can
  include negotiation or forming a new arrangement, which is not
  retrieval. Only the first of [CLAIM-tmp80ny9](../claims.d/CLAIM-tmp80ny9.md)'s three kinds is a
  retrieval or verification cost.
- **Are the model's assumptions met in the new domain?** Not all.
  [CASE-326](../cases.d/CASE-326.md) states that "ε is a fixed fraction, not a function of how" the
  store is used, and treats staleness as a probability per use. For a
  contract, erosion of the parties' alternatives and the inadequacy of the
  arrangement are produced by its invocations (A30 §7's table; the
  dependency dynamics introduced earlier in the exchange). Where they are,
  the per-demand cost is path-dependent and the fixed-parameter formula
  misprices it. Where invocations do not change the arrangement (an
  explicit, externally enforced agreement), the assumption holds and the
  model applies as it stands.
- **Does a richer state suffice?** Open, and the conclusion does not
  decide it: A30 suspects richer state variables "will cover most of the
  cases". [LEAD-tmp14n26](../leads.d/LEAD-tmp14n26.md) tests it.
