---
number: 342
status: Proposed
formerly:
- CLAIM-tmpt568z
title: 'What keeps a judgement–observation loop from confirming itself is evidence whose arrival or scoring does not pass through the interpretation it tests; action is one source of such evidence, not a necessary one, and a loop that selects its own evidence can lock in with action available'
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  A loop whose evidence is scored independently of the interpretation it
  tests, or whose per-context marginals are fixed from outside, shown to
  lock in all the same. Or a showing that the only evidence an agent can
  receive that does not pass through its own interpretations arrives
  through its own action on the world. A showing that action is a common
  or efficient source of such evidence does not defeat it.
tags:
- cognition
- probabilistic-modeling
- psychopathology-and-treatment
date: '2026-10-16'
line:
- distributed-agency
- pragmatic-transport
rests_on:
- CLAIM-330
- CLAIM-141
grounds:
- THEORY-285
- THEORY-324
- LIT-1181
objects_to:
- CLAIM-339
complements:
- CLAIM-341
- CLAIM-338
summary: >-
  The assistant's synthesis, A3 and A4 of the exchange of 2026-10-16,
  filed at the owner's request at U5. Three results the record already
  holds. [CLAIM-330](CLAIM-330.md): capture in the operator model needs both arrows of
  [CLAIM-297](CLAIM-297.md)'s circuit, and scoring operators independently of the
  dominant interpretation removes it. [CLAIM-141](CLAIM-141.md): a loop always has a
  distributional fixed point, so what binds it is a constraint that
  prescribes marginals. [THEORY-285](../theory.d/THEORY-285.md) ([NOTE-766](../notes.d/NOTE-766.md)): an active-inference agent
  locks in with action available, because its own sampling policy
  withholds the evidence that would correct it. The claim does not say
  action is unimportant, only that it is not what does the anchoring.
---

# CLAIM-342: What keeps a judgement–observation loop from confirming itself is evidence whose arrival or scoring does not pass through the interpretation it tests; action is one source of such evidence, not a necessary one, and a loop that selects its own evidence can lock in with action available

## The claim

[CLAIM-339](CLAIM-339.md) objects to [CLAIM-341](CLAIM-341.md) that a judgement–observation loop
with no action has a self-confirming minimum: judge so that what is
observed confirms what is expected. The record already holds three results
that bear on that minimum.

- **It exists for every loop.** [CLAIM-141](CLAIM-141.md): "Passing from values to
  distributions creates solutions." A loop that feeds its outputs back as
  inputs has a self-consistent distribution whether or not it acts. What
  makes a fixed point wrong is a constraint from outside it that prescribes
  marginals, the kind a contextual empirical model imposes ([TERM-042](../terms.d/TERM-042.md)).
- **Action does not prevent it.** In the active-inference model of
  [THEORY-285](../theory.d/THEORY-285.md), the agent can act, and still "as long as the sensory
  attenuation policy is selected, no amount of observations will render
  prior beliefs obsolete" ([NOTE-766](../notes.d/NOTE-766.md)). The policy "withholds the only
  observations that could lower that precision", and what it attenuates
  is a "sensory or cognitive periphery". Lock-in comes from the loop
  selecting its own evidence, and action is one of the ways it selects.
  Friston et al. say so of action in general: it is "sampling selectively
  what one expects to experience", and the weakness this brings "becomes
  the strength" ([LIT-1181](../literature.d/LIT-1181.md), [NOTE-960](../notes.d/NOTE-960.md)).
- **Independent scoring prevents it.** [CLAIM-330](CLAIM-330.md) (Active, demonstrated): in
  the linearized operator model, capture starting at symmetry needs both
  arrows of [CLAIM-297](CLAIM-297.md)'s circuit, authority shaping interpretation and
  interpretation shaping endorsement. "Scoring operators independently of
  the dominant interpretation (Regime B, γ ≈ 0) removes the
  coupling-driven instability."

So what anchors the loop is evidence whose arrival or scoring does not run
through the interpretation it tests. Action on the world is one source of
such evidence: it brings in what the agent did not ask for. Others are a
source the agent does not select, such as an interlocutor, a scheduled
probe or a body state, and a scoring rule fixed independently of the
current interpretation. Ashby's ultrastability has the same structure: a
second channel, from the essential variables to the parameters of the
first loop, that the first loop's behaviour does not set ([THEORY-324](../theory.d/THEORY-324.md)).

## What it does not say

- It does not say an agent without action has independent evidence. The
  locked-in case asks whether one does ([CASE-107](../cases.d/CASE-107.md)). Damasio's
  re-enacted body states ([THEORY-500](../theory.d/THEORY-500.md)) and the visceromotor regulation
  that survives paralysis ([NOTE-434](../notes.d/NOTE-434.md)) are candidates.
- [CLAIM-330](CLAIM-330.md) is a linearization at symmetry. It shows what independent
  scoring removes near that point, not that it prevents every form of
  lock-in.
- It does not say what in a single mind plays the part of Regime B's
  independent scoring. [QUESTION-121](../questions.d/QUESTION-121.md) asks, with five candidates from
  the record: unselected input, the body, commitment before evidence,
  processing signals and other people. A paralysed person keeps the first,
  the second and the fifth inbound, so losing action need not mean losing
  the anchor.

## Note of 2026-10-18: re-derived as independent audit

The exchange of 2026-10-17 proposed this claim's thesis four times as a
design requirement, without citing it.

- A36 §4, on cryptographic commitments as "**independent endorsement
  audits**": a commitment protocol lets an auditor check that a prediction
  "was not changed retroactively", but "it only solves one problem: **the
  timing and integrity of the prediction**. It does not establish that the
  outcome is interpreted correctly, that the scoring rule is appropriate, or
  that the operator was exposed to representative evidence." That is
  [CLAIM-340](CLAIM-340.md)'s limit: commitment fixes when the prediction is made, not how
  the evidence is read.
- A39's second case study: "endorsement based on independent performance
  evidence versus endorsement scored through the interpretations whose
  authority is being evaluated", which A39 called "the best candidate for
  an early discriminating experiment".
- A40's Study C, key control: "Evaluate the demands using evidence
  independent of the processes whose authority is being assessed."
- A41's security table, whose row for independent audit reads "Prevent the
  actor being evaluated from controlling all the evidence of its
  competence", and its
  variant that would "compromise the processes responsible for evaluating
  other processes' competence. That tests whether the organization has any
  genuinely independent means of checking its own allocation of authority."
  That variant is in [CASE-tmp4nzjz](../cases.d/CASE-tmp4nzjz.md). It puts this claim under attack: the
  evidence that does not pass through the tested interpretation is itself
  scored by a process an insider may hold.
