---
number: 443
status: Active
formerly:
- CLAIM-tmp0qupq
title: 'A learned prior over which processes govern, P(g | z, H) ∝ exp(βQ(g, z) + b_H(g, z)), its bias b_H trained by reward-modulated Hebbian updates to the relations by which one process recruits or endorses another, is a candidate mechanism for durable authority and for amortized governance; but persistence is not amortization, which is shown only when earlier work replaces later computation, communication or recruitment, and a prior over authority differs from a prior over actions only when what is appropriate changes'
version: 3
history:
- version: 2
  date: '2026-10-29'
  note: >-
    Relations corrected by the tenth status review (ADR-057, ADR-058).
    THEORY-913, THEORY-904, THEORY-918, THEORY-908, THEORY-922,
    THEORY-923 and THEORY-909 move from grounds to corroborated_by: all
    seven were filed on 2026-10-24, after the claim, and enter only in
    "What the readings of 2026-10-24 add", as evidence or as narrowings;
    the claim's argument does not stand on any of them. The claim is
    unchanged.
- version: 3
  date: '2026-10-29'
  note: >-
    Relations corrected and promoted by the fourteenth status review
    (ADR-057, ADR-058), at the status review's ruling (the owner
    delegated these rulings). CLAIM-358 moves from rests_on to
    complements: the claim takes from it only the reuse inequality,
    which is cost accounting that holds whatever the costs (checked at
    this review), and the learned prior it describes is what CLAIM-358's
    note of 2026-10-23 calls a learned endorsement, which saves
    negotiation over authority, not the local accommodation, which saves
    escalation, that CLAIM-358 claims. LIT-1492 leaves grounds: it is
    Unavailable and the record holds no reading of it. LIT-1476,
    LIT-1488, LIT-1494 and LIT-1497 leave grounds for version 2's
    reason: filed after the claim, they enter only in "What the readings
    of 2026-10-24 add", and the readings filed from them already
    corroborate it. Its premise CLAIM-277 is Active, no objection is
    filed, and nothing meets its defeated_if. Version 2's sentence read:
    "CLAIM-358's cost argument says when it pays." The inequality now
    says its maintenance and error terms are totals over the N
    encounters. The claim is unchanged.
role: thesis
warrant: interpretive
defeated_if: >-
  A matched comparison in which a fixed switching cost or a cached action
  policy reproduces every response to intervention that the learned
  authority prior predicts, including the response when the appropriate
  action changes and a recruited process could choose another; or
  regulation that becomes cheaper with practice where intervening on the
  learned recruitment relations, with the action policy held fixed, changes
  nothing.
tags:
- self-governance
- learning-and-conditioning
- motivation
date: '2026-10-23'
line:
- will-organization
- distributed-agency
rests_on:
- CLAIM-277
complements:
- CLAIM-349
- CLAIM-344
- CLAIM-364
- CLAIM-444
- CLAIM-358
corroborated_by:
- THEORY-913
- THEORY-904
- THEORY-918
- THEORY-908
- THEORY-922
- THEORY-923
- THEORY-909
summary: >-
  The owner's, 2026-10-23, on whether practice could reconstruct relations
  of practical authority: "what if we just treat this as a kind of momentum
  term? or like a hebbian prior?" Worked through the same day (workbench
  entry of 2026-10-24, U9–U12). Momentum is read as switching cost, the
  Hebbian prior as a learned bias over allocations of authority, and two
  limits are kept: persistence is not amortization, and a prior over
  authority must be told from a prior over actions.
illustrated_by:
- CASE-153
- CASE-155
supports:
- CLAIM-446
---

# CLAIM-443: A learned prior over which processes govern, P(g | z, H) ∝ exp(βQ(g, z) + b_H(g, z)), its bias b_H trained by reward-modulated Hebbian updates to the relations by which one process recruits or endorses another, is a candidate mechanism for durable authority and for amortized governance; but persistence is not amortization, which is shown only when earlier work replaces later computation, communication or recruitment, and a prior over authority differs from a prior over actions only when what is appropriate changes

## The claim

The owner, 2026-10-23: "what if we just treat this as a kind of momentum
term? or like a hebbian prior?"

The two suggestions are different mechanisms on different timescales.

**Momentum, read as switching cost.** g_t = argmax_g [Q(g, z_t) −
κ·1(g ≠ g_{t−1})]. A governing allocation resists small transient changes
of salience. This is inertia or hysteresis rather than momentum in the
optimization sense.

**A Hebbian prior.** Let g be an allocation of authority among the
processes and z the context. Governance is selected as

    P(g | z, H) ∝ exp(β Q(g, z) + b_H(g, z)),

with Q the current evaluation of the allocation and b_H a learned,
history-dependent bias toward allocations used before. The bias is
trained on the relations by which a process j recruits or endorses a
process i:

    ΔE_ji = η x_j y_i (R_t − R̂_t) − λ E_ji,

co-activation gated by an outcome signal, with forgetting. This is a
schematic three-factor rule, not a claim about any neural implementation.
In a familiar context the prior already puts a process in a position to
govern, so the case for it need not be rebuilt. [CLAIM-277](CLAIM-277.md)'s durable
authority from repeated endorsement becomes this prior; [CLAIM-358](CLAIM-358.md)'s note
of 2026-10-23 gives the accounting for when it pays.

**Worked example (DBT).** An avoidance process A, a relationship process
B and a pause-and-assess procedure R. At first B has influence only if R is
recruited deliberately and at cost. After practice, A's own activation
recruits R. Neither A nor B changes what it values. What changes is the
conditional probability that one process's activation recruits another
with a regulatory role ([CLAIM-349](CLAIM-349.md)'s note of 2026-10-23).

## Two limits

**Persistence is not amortization.** A strong prior can change which
allocation wins while every process still does all the same costly
evaluation and negotiation. Amortization is shown only when earlier work
replaces later computation, communication or supervisory recruitment. In
[CLAIM-358](CLAIM-358.md)'s terms, reuse pays under a declared cost measure and comparable
outcomes when N(c_d − c_π) > F + C_maintenance + C_error, with
C_maintenance and C_error totalled over the N encounters, and the
inequality has to be measured, not inferred from stable behaviour.

**A prior over authority is not a prior over actions.** "When distressed,
pause" is an action policy. "When distressed, make this other process's
evaluation available before acting" is a relation of influence. They look
the same in familiar situations and come apart when the appropriate action
changes: a recruited process with the information and capacity can choose
a different response, and a cached action cannot.

**Naive Hebbian learning entrenches.** Whatever is recruited often gets
more chances to succeed and is reinforced whether or not it deserved
authority, and a routine that controls which alternatives are considered
reinforces its own use. The prior encodes a history of reinforcement under
a sampling regime, not competence. This is [CLAIM-277](CLAIM-277.md)'s warning and
[CLAIM-364](CLAIM-364.md)'s, and it is where the same exchange found a candidate account of
anxiety ([CLAIM-446](CLAIM-446.md)).

## The test

Train two systems to the same action. In one, reinforce the cue-to-action
mapping; in the other, reinforce recruitment of a process that chooses
among actions. Then change which action is appropriate. Separately,
compare recurrent cost before and after training: responses that become
more persistent with no computation or supervision saved are not evidence
for amortization. Learned local accommodation and a compiled supervisor
should also fail differently when lower-level interactions and
higher-level deliberation are disrupted selectively.


**What the readings of 2026-10-24 add.** Friston et al. ([NOTE-1138](../notes.d/NOTE-1138.md), [THEORY-923](../theory.d/THEORY-923.md)) is a published analogue of the selection rule, π = σ(Ê − F − γG), but over action policies, not over who governs. Its learned prior grows by counting the policies pursued, with no reward gate. That is closer to the entrenchment warned of below than to the rule above. Its devaluation simulation runs this claim's test on the cached arm: once formed, the habit persists. Every policy is still scored on every trial, so the paper shows persistence, not amortization. Gerstner et al. ([NOTE-1130](../notes.d/NOTE-1130.md), [THEORY-909](../theory.d/THEORY-909.md)) narrow "three-factor rule". Only the hour-scale tag of synaptic consolidation is well established. Eligibility traces on the scale of seconds have recent support, mostly from brain slices, and the rule above lacks the decaying trace that learning from delayed outcomes needs. With reward minus expected reward as the third factor, frequency alone is not reinforced, which answers part of the entrenchment point below; what is never recruited is still never credited. Implementation intentions ([NOTE-1124](../notes.d/NOTE-1124.md), [NOTE-1131](../notes.d/NOTE-1131.md); [THEORY-913](../theory.d/THEORY-913.md), [THEORY-904](../theory.d/THEORY-904.md), [THEORY-918](../theory.d/THEORY-918.md), [THEORY-908](../theory.d/THEORY-908.md)) are the nearest studied case. An if–then plan "delegat[es] the control of goal-directed behavior to specified situational cues", which is a prior over actions, not over who governs. It works only while the goal is active, a third arrangement this claim had not named. The effect is reliable but small: d = .65 in the 2006 meta-analysis, uncorrected for publication bias, and about .15 after the 2024 review's robust Bayesian correction. The 2006 tests of efficiency and conserved capability measure later effort saved, not only persistence, though for a cached action. What happens when the planned response proves wrong is the authors' open question ("We do not know yet what happens"), and it is this claim's test. Edwards et al. ([NOTE-1121](../notes.d/NOTE-1121.md), [THEORY-922](../theory.d/THEORY-922.md)) associate DBT homework with falling urges, not with less frequent behaviour, and phone coaching did not significantly predict outcome. They measure neither skill use nor its cost. Linehan's manual and Amestoy et al.'s mediation study were sought and are Unavailable.

## What it does not say

- That this is how DBT works. The DBT example is a functional
  interpretation, and the record holds no reading of Linehan.
- Which learning law is right: Hebbian updates, Bayesian policy priors and
  learned arbitration can produce the same behaviour from different
  dynamics.
- That a learned governance arrangement that is cheap and stable is
  appropriate ([QUESTION-087](../questions.d/QUESTION-087.md)).

## Note of 2026-10-29: promoted

The fourteenth status review promoted the claim, at the status review's
ruling (the owner delegated these rulings), after moving [CLAIM-358](CLAIM-358.md) to
complements and the LITs out of grounds. Its test, a change of the
appropriate action after training a cached and a recruited arm, is still
unrun; Friston et al.'s devaluation run is the cached arm alone.
