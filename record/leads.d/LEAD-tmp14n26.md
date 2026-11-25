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

## Note of 2026-11-24: from the revision of the manuscript governance-of-becoming, Part I
<!-- inactive-ok-file: CASE-343 CLAIM-921 — Proposed; cited with their standing -->

The revision of the manuscript's Article 3 (§3.3.4) sorted this lead by
the write-manuscript skill's step 3a ("What the record has already done")
and found it done in part. Held work plays part of its role:

- erosion that depends on how long a supply has done the work, for a
  capacity learned by doing: CLAIM-602 (Active, demonstrated), "what
  decides dependence is the order in which supply and capacity are used,
  not the amount of supply";
- step 1's matched pair, for a capacity rather than a contract: CLAIM-675
  (Active, demonstrated), "Two forms of support that give a party the same
  capabilities now can leave it different capabilities later";
- a state whose funding follows its own use: CASE-343, run, with
  CLAIM-921 deriving the loss;
- CLAIM-921's note of 2026-11-24, which carries that loss to rarely
  invoked guarantees (A32 §9): "The contract might remain formally
  recognized while its guarantee becomes unrealizable."

What no entry does is this lead's own case: a relationship whose
invocations expand its practical jurisdiction and erode the recipient's
alternatives, priced per party over a horizon, including revision and
exit, against one whose invocations leave it unchanged, with the question
whether time-varying ε, σ and R suffice or a term of a new kind is needed.
The extension is that contract case and the per-party ledger; the rest can
cite the entries above. Whether to narrow the lead to it is the owner's
call. No status change. The wording is the assistant's (Claude, in this
session).
