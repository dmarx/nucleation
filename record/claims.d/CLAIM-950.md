---
number: 950
status: Proposed
formerly:
- CLAIM-tmpn5wpc
title: 'The competence-restriction loop is demonstrable'
statement: >-
  The competence-restriction loop is demonstrable: in capacity dynamics
  where competence is learned by doing and decays with disuse, making
  reinstatement a threshold on capacity turns a restriction justified by a
  lack of competence into a self-perpetuating trap, because the restriction
  causes the decay that holds capacity below the reinstatement threshold;
  the trap has a recoverability deadline, and it is escaped only by a route
  strong enough to restore practice or by training that adds capacity
  directly
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the model of CASE-364, which is CLAIM-605's dynamics
  dC/dt = λPC(1 − C) − μC + g with a restriction giving P = ρ·min(τC, 1)
  while restricted and reinstatement at C ≥ C_r: a showing that under no
  route (ρ = 0, g = 0) a party restricted below C_r can reach C_r; that
  there is no duration of restriction after which release no longer
  restores capacity; that a practice route below ρ_crit = 4μ/(λτ) or a
  party below the shifted threshold is reinstated; or that a training route
  g ≥ μ·C_r fails to reinstate from C = 0. Not defeated by the parameters
  being invented, which the claim grants, nor by restrictions that are not
  of the kind CLAIM-721 names (competence that decays with disuse, lifting
  gated on competence, no route supplied), whose applicability is
  CLAIM-721's question and not this model's.
tags:
- society-and-governance
- learning-and-conditioning
- agency
- mathematics
date: '2026-11-22'
line:
- dependence-and-domination
- transient-support
- rightful-power
rests_on:
- CLAIM-605
grounds:
- CASE-364
corroborates:
- CLAIM-721
bears_on:
- QUESTION-478
uses:
- TERM-129
summary: >-
  The assistant's, carrying out [LEAD-104](../leads.d/LEAD-104.md) (2026-11-22). [CLAIM-721](../claims.d/CLAIM-721.md) named
  the model that would make the restriction-induced capability trap
  demonstrable — [CLAIM-605](../claims.d/CLAIM-605.md)'s "with reinstatement made a threshold on
  capacity" — and said no one had written it. [CASE-364](../cases.d/CASE-364.md) writes and
  runs it. The finding: making reinstatement a threshold C_r on capacity
  closes [CLAIM-721](../claims.d/CLAIM-721.md)'s loop in the model. A party restricted below C_r with
  no route to practice or training decays monotonically, never reaches
  C_r, and so is never reinstated — the restriction manufactures the
  evidence that extends it. The trap has a recoverability deadline
  (1.98 time units at [CLAIM-605](../claims.d/CLAIM-605.md)'s parameters) past which even manual
  release fails, the twin of [CLAIM-605](../claims.d/CLAIM-605.md)'s substitution deadline. It is
  escaped only by a practice route that restores exercise above a critical
  fraction (which still cannot ignite a party below threshold) or by a
  training route that adds capacity directly and ignites from zero —
  [CLAIM-605](../claims.d/CLAIM-605.md)'s capacity-first/transfer distinction reached by restriction.
  Each of [CLAIM-721](../claims.d/CLAIM-721.md)'s three conditions is shown necessary. This corroborates
  [CLAIM-721](../claims.d/CLAIM-721.md) with a formal demonstration; whether that moves [CLAIM-721](../claims.d/CLAIM-721.md)'s
  warrant to demonstrated is the owner's call. The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-721 TERM-129 CASE-364 — Proposed or new; the claim this demonstrates, the term it is stated in, and the study that grounds it -->

# CLAIM-950: The competence-restriction loop is demonstrable

## The claim

[CLAIM-721](../claims.d/CLAIM-721.md) holds, interpretively, that where competence is kept by use
and lost with disuse and a restriction lifts when competence is shown, a
restriction justified by a lack of competence lowers the competence it
waits for, so that unless a route to practice or training is supplied the
restriction produces the evidence for its own continuation. It records
that a model of the loop "would be [CLAIM-605](../claims.d/CLAIM-605.md)'s with reinstatement made a
threshold on capacity, which would make the trap demonstrable; no one has
written it." [CASE-364](../cases.d/CASE-364.md) writes and runs it. This claim states what the
model shows.

In [TERM-129](../terms.d/TERM-129.md)'s terms, the model tracks competence as the capacity C; the
restriction acts on exercise (it sets P); and reinstatement is the
authority's decision, here made a function C ≥ C_r of the competence
shown.

1. **The loop closes: the bare restriction is a self-perpetuating trap.**
   With no route (ρ = 0, g = 0), a restricted party's capacity obeys
   dC/dt = −μC and falls monotonically, so a party restricted below C_r
   never reaches it and is never reinstated. The restriction removes the
   exercise by which C would recover, and so causes the very decay the
   reinstatement rule reads as the reason to keep restricting. Periodic
   reviews return an ever-lower competence, each below C_r: the decay is
   the evidence.

2. **A recoverability deadline.** A party restricted above [CLAIM-605](../claims.d/CLAIM-605.md)'s
   unstable threshold C_LOW but below C_r is not reinstated, yet would
   recover if freed — until C decays past C_LOW, after
   t_dead = ln(C₀/C_LOW)/μ. Past the deadline the trap is sprung even
   against a change of heart: releasing the party by hand no longer
   restores capacity. This is [CLAIM-605](../claims.d/CLAIM-605.md)'s full-substitution deadline reached
   by restriction instead of substitution.

3. **The escape turns on the kind of route, as [CLAIM-605](../claims.d/CLAIM-605.md) says of support.**
   A practice route — restoring exercise at a fraction ρ of normal —
   reinstates only if ρ clears a critical fraction (ρ_crit = 4μ/(λτ)) and
   the party is above the restricted threshold; a weak route, or a party
   already low, stays trapped. It "cannot ignite". A training route — one
   that adds capacity directly, independent of exercise — drives C to g/μ
   and reinstates from any start, C₀ = 0 included, once its rate clears
   μ·C_r. This is exactly [CLAIM-605](../claims.d/CLAIM-605.md)'s third result: capacity-first support
   cannot ignite a party below the threshold, a direct capacity transfer
   can. [CLAIM-721](../claims.d/CLAIM-721.md)'s "a route to practice **or training**" is the two apart.

4. **Each of [CLAIM-721](../claims.d/CLAIM-721.md)'s three conditions is necessary.** Remove disuse
   decay and the restriction is a static bar that makes no new evidence;
   remove the competence gate (release on a fixed date) and the party is
   freed regardless, recovering if not yet past the deadline; supply a
   sufficient route and the party is reinstated. Drop any one and the loop
   does not close, as [CLAIM-721](../claims.d/CLAIM-721.md)'s title already states.

## How it sits with the record

- It **corroborates [CLAIM-721](../claims.d/CLAIM-721.md)**: an independent, formal demonstration of the
  loop that claim asserts interpretively. [CLAIM-721](../claims.d/CLAIM-721.md) does not rest on this
  model — it reads real institutions — so this is corroboration, not a
  premise it needs. Whether the demonstration moves [CLAIM-721](../claims.d/CLAIM-721.md)'s warrant from
  interpretive to demonstrated is the owner's call, and is noted on
  [CLAIM-721](../claims.d/CLAIM-721.md).
- It **rests on [CLAIM-605](../claims.d/CLAIM-605.md)**: the model is [CLAIM-605](../claims.d/CLAIM-605.md)'s capacity dynamics,
  modified only in what sets practice and in making exit a threshold on C.
  [CLAIM-721](../claims.d/CLAIM-721.md) had noted that the loop "needs only their premise, decay with
  disuse, and not their supply; the restriction removes the doing
  directly" — which is precisely how the restriction enters the model.
- It **bears on [QUESTION-478](../questions.d/QUESTION-478.md)** (under what conditions a capability should be
  restricted, and who may): the model shows that a restriction gated on
  competence, with no route back, is self-justifying regardless of the
  authority's intent, which bears on when such a restriction is
  defensible.

## What it does not say

- **Not that any real restriction is of this kind.** Whether competence in
  a given case decays with disuse, whether lifting in fact waits on
  competence shown, and whether no route is supplied are [CLAIM-721](../claims.d/CLAIM-721.md)'s
  empirical conditions, not shown here.
- **Not that the numbers carry over.** C_r, the deadline, ρ_crit and g_crit
  all follow from invented parameters. The model shows the structure of the
  loop and the direction of each result, not magnitudes.
- **Not that restriction is wrong, or that the trap is intended.** As
  [CLAIM-721](../claims.d/CLAIM-721.md) says, the loop closes with no one aiming at it, and some
  restrictions rightly stand whatever the actor's competence.
