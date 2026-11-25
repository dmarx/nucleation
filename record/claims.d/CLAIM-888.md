---
number: 888
status: Proposed
formerly:
- CLAIM-tmpc4gyx
title: 'In the coupled meaning–influence model, where each operator''s authority is scored against the interpretation it helped make dominant, a governance intervention''s later effect on a response under a new frame takes the sign of the treated operator''s reading there and survives in proportion to the operators'' dissent under the frames passed through, growing where η·Δa²/2 > κ; so separate interpretation and governance models of matched complexity and training data mispredict held-out compositions of interventions and frame changes when that loop is present, and gain nothing on the joint model when it is absent'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-029, from the
    study of CASE-324.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation: for two operators under one context,
  linearized at the symmetric allocation, det(I − J) other than
  ρ(κ − η·Δa²/2), or growth of a small perturbation of authority on the
  wrong side of η·Δa²/2 = κ. Or, in CASE-324's construction, a model
  with no loop from interpretation to authority, of no more parameters than
  the joint model and fitted to the same training data, that predicts the
  effects of the held-out compositions as well as the joint model where
  η > 0, or a joint model that beats the cut model where η = 0 beyond
  what its extra parameter buys. Not defeated by a real system without
  the loop, which the claim does not say any system has, nor by
  constructions outside the model.
tags:
- complex-systems
- self-governance
- pragmatics
date: '2026-11-22'
line:
- distributed-agency
- will-organization
- pragmatic-transport
rests_on:
- CLAIM-297
grounds:
- CASE-324
complements:
- CLAIM-330
- CLAIM-336
bears_on:
- QUESTION-088
summary: >-
  The joint prediction [LEAD-029](../leads.d/LEAD-029.md) asked for, derived in [CLAIM-297](CLAIM-297.md)'s operator
  model and shown in [CASE-324](../cases.d/CASE-324.md). A governance intervention changes
  authority; through [CLAIM-336](CLAIM-336.md)'s mapping, the frame is the context under
  which operators act and the judgement is the read-out of the shared
  state. Then (1) the intervention's effect under a later frame is set by
  the treated operator's reading in that frame, which a governance effect
  added to an interpretation model cannot express, and (2) how much of it
  survives depends on how much the operators disagree under the frames in
  between, with [CLAIM-330](CLAIM-330.md)'s threshold in the form η·Δa²/2 > κ, which a
  model whose authority ignores interpretation cannot express. In the
  simulation the joint model predicted held-out compositions two to thirty
  times better than such models when the loop was present, and tied the
  cut model, with a worse BIC, when it was absent. It is a result about
  the model, not about any system. The wording is the assistant's
  (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-336 CLAIM-286 ARG-065 CASE-324 — Proposed or new; the owner's unification and its premise and argument, cited as open, and the study filed with this claim -->

# CLAIM-888: In the coupled meaning–influence model, where each operator's authority is scored against the interpretation it helped make dominant, a governance intervention's later effect on a response under a new frame takes the sign of the treated operator's reading there and survives in proportion to the operators' dissent under the frames passed through, growing where η·Δa²/2 > κ; so separate interpretation and governance models of matched complexity and training data mispredict held-out compositions of interventions and frame changes when that loop is present, and gain nothing on the joint model when it is absent

## The claim

[CLAIM-336](CLAIM-336.md) is the owner's thesis that the pragmatic-transport and
will-organization lines describe one model. Its blocker, in its note of
2026-10-29, is that "no joint prediction of the pragmatic-transport and
will-organization lines has been derived through the mapping". This claim
states one, derived in [CLAIM-297](CLAIM-297.md)'s model and checked by simulation in
[CASE-324](../cases.d/CASE-324.md).

Take operators i that, under a frame q, pull a shared interpretive state x
toward readings aᵢ(q), with authority w = softmax(u), and let each
operator's u be updated by how well its reading agrees with the
interpretation that results ([CLAIM-297](CLAIM-297.md)'s circuit). A governance
intervention adds to one operator's u. Then:

1. **Sign.** The intervention's effect on a judgement under a later frame
   q′ is carried by the authority it moved, so it has the sign and size of
   the treated operator's reading under q′ relative to the others, whatever
   its effect was when it was applied.
2. **Persistence.** For two operators under one frame with dissent
   Δa = a₁ − a₂, linearized at the symmetric allocation,
   det(I − J) = ρ(κ − η·Δa²/2). A shift of authority decays at the
   governance rate where the operators agree, and grows exactly where
   η·Δa²/2 > κ. So how much of an intervention survives depends on the
   frames the system passes through after it. This is [CLAIM-330](CLAIM-330.md)'s
   condition βγ > (1 − α)(1 − δ) with the entries this model gives.

A model that adds a governance effect to an interpretation model misses
(1). A model in which governance moves authority but interpretation never
does, of the same or greater flexibility, misses (2). In the simulation,
with the loop present, both kinds mispredicted held-out compositions of an
intervention and a later frame change by two to thirty times the joint
model's error, on the same training data and with no more parameters.
With no loop, the joint model gained nothing and its BIC was the worse.

## What it does not say

- That any person, interpreter or system has the loop. The simulated
  world is built to have it or not; the result is that the comparison can
  tell, and what the prediction is.
- That [CLAIM-336](CLAIM-336.md) holds. It answers the blocker's "no joint prediction has
  been derived" within the model. The second clause of [CLAIM-336](CLAIM-336.md)'s
  defeater asks the comparison of real or independently generated
  observations; [ARG-065](../arguments.d/ARG-065.md)'s critical question "does a rival explain as
  well?" is answered no only for data with the loop.
- That the joint model wins when misspecified by as much. With the score
  −|aᵢ − x| in the generator its error was about half the best separate
  model's; with the score it assumes, between about a half (damped, D1)
  and a thirtieth (amplifying, D2).
- Anything about [CLAIM-286](CLAIM-286.md)'s phenomena (habit, rumination, rigidity,
  akrasia, insight) or models built for them; the construction has none.
