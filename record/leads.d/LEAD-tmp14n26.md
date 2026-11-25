---
status: Open
title: 'Extend the stored-work cost model with a store that its own use updates, and test whether contract invocation needs new cost terms or only a richer state'
version: 1
stage: idea
priority: medium
method:
- formal
- conceptual
tags:
- operations-research
- society-and-governance
date: '2026-11-24'
line:
- realizability
- dependence-and-domination
advances:
- CLAIM-tmpsf9hp
- QUESTION-tmpb7fx7
- CLAIM-891
summary: >-
  A30 §15 of the exchange 'Memes, Contracts, and Systemic Normativity'
  (ChatGPT, 2026-11-24): "The critical test is whether these require
  genuinely new cost terms, or merely richer state variables and transition
  mechanisms within the existing model ... the current [CASE-326](../cases.d/CASE-326.md)
  implementation uses fixed erosion ... That would need to be tested. I have
  not modified the repository or run a new experiment." The design is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmp80ny9 CLAIM-tmpsf9hp — Proposed or new; this filing's entries and the held entries it maps to, cited with their standing -->

# LEAD-tmp14n26: Extend the stored-work cost model with a store that its own use updates, and test whether contract invocation needs new cost terms or only a richer state

## What it would do

Take [CASE-326](../cases.d/CASE-326.md)'s model and make the store a state updated by its own use,
C_{t+1} = Φ(C_t, q_t, a_t, f_t) (A30 §7), with erosion ε and staleness σ
functions of the history of invocations rather than fixed parameters.
Then:

1. Build two relationships matched in per-use cost and output under
   [CASE-326](../cases.d/CASE-326.md)'s terms at the start, one whose invocations leave it unchanged
   (an explicit agreement enforced from outside) and one whose invocations
   expand its practical jurisdiction and erode the recipient's
   alternatives (A30 §7's "Repeated accommodation" and "Repeated
   reliance").
2. Price each over a horizon, per party (A30 §11's actor-indexed ledger
   J_i), including revision and exit at the end.
3. Ask whether the difference is captured by [CASE-326](../cases.d/CASE-326.md)'s existing terms with
   a richer state (time-varying ε and σ), or whether a term of a new kind
   is needed (A30's spillover S or a per-party revision cost R_i(C, C′)).

It would also price the cost of resolving which relationship applies, by
[CLAIM-tmp80ny9](../claims.d/CLAIM-tmp80ny9.md)'s three kinds, to see whether the second and third fall
outside retrieval and verification.

## What would settle it

The claim [CLAIM-tmpsf9hp](../claims.d/CLAIM-tmpsf9hp.md) is defeated if the two relationships' later costs
never part, or part only by an amount the fixed-parameter formula with a
re-estimated ε reproduces. The model's "richer state" reading is confirmed
if time-varying ε, σ and R suffice; a new term is needed if a per-party
cost of resolving or contesting the invocation does not reduce to them.

## What it needs

Nothing outside the record; [CASE-326](../cases.d/CASE-326.md)'s illustrative values and [LEAD-108](LEAD-108.md)'s
model are the starting point.
