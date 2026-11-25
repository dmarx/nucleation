---
status: Proposed
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  A showing that in the stateful model an institution optimizing over time
  gains nothing from actions whose only effect is to lower its future
  expected losses from exit, challenge, regulation or internal resistance;
  or evidence that, across institutions, such erosion of constraints occurs
  only with a change of leadership or of its members' character, as the
  claim says it need not.
tags:
- society-and-governance
- economics
- operations-research
- ethics
date: '2026-11-24'
line:
- dependence-and-domination
- organizational-normativity
works:
- governance-of-becoming
uses:
- TERM-tmpxr1ox
complements:
- CLAIM-464
- CLAIM-404
- CLAIM-619
- CLAIM-670
- CLAIM-624
grounds:
- THEORY-470
- THEORY-150
title: "Where the losses that discipline an institution's extraction from those who depend on it, their exit, challenge, regulation and internal resistance, depend on a state its own actions change, an institution optimizing a narrow objective over time values weakening those constraints for their own sake, so their erosion can be produced by the optimization itself, with no change in the character of those who run it"
summary: >-
  A46 §10 of the exchange "Memes, Contracts, and Systemic Normativity"
  (ChatGPT, 2026-11-24), restated for shareholder value at A48 §6 ("Regulatory
  arbitrage as second-order optimization"). It reads Doctorow's four
  constraints ([THEORY-470](../theory.d/THEORY-470.md)) as terms of the loss that disciplines extraction
  and makes that loss stateful. [THEORY-470](../theory.d/THEORY-470.md) holds that the constraints
  weakened, not the people; [CLAIM-464](CLAIM-464.md) holds that one intervention can change
  what it would take to correct it. Added: the optimizing policy itself puts a
  value on eroding them. The derivation A46 omits is filled in the note below.
  The wording is A's (ChatGPT, in the exchange "Memes, Contracts, and Systemic
  Normativity"); adopting it is the owner's call.
---

<!-- inactive-ok-file: CLAIM-619 CLAIM-624 THEORY-470 THEORY-150 — Proposed; the held neighbours, Doctorow's accounts and the term -->

# CLAIM-tmpjnly0: Where the losses that discipline an institution's extraction from those who depend on it, their exit, challenge, regulation and internal resistance, depend on a state its own actions change, an institution optimizing a narrow objective over time values weakening those constraints for their own sake, so their erosion can be produced by the optimization itself, with no change in the character of those who run it

## The claim

A46 §10: let e be the intensity of extraction and C_t the relationship's
state; the institution gains G(e) and faces expected losses
L(e, C_t) = L_exit + L_challenge + L_regulation + L_internal resistance, and
"A narrowly optimizing institution might select" e_t* ∈ argmax_e [G(e) −
L(e, C_t)]. Doctorow's constraints become terms of L: competition "Makes
withdrawal a credible source of loss", interoperability "Reduces
participants' switching and substitution costs", regulation "Establishes
externally enforced requirements and consequences", worker power "Enables
internal concerns to acquire effective standing".

"But the relationship is stateful": C_{t+1} = Φ(C_t, e_t, a_t). So "an
organization may allocate resources not only toward improving its current
score but toward transforming the constraints governing its future
optimization. From the perspective of the institution's narrow objective,
weakening effective oversight or alternative provision could itself become
valuable. This is where greedy agency becomes reflexive control." Its
limit: "The model is not a general explanation of corporate behavior, and
legitimate commercial objectives need not generate exploitation."

A48 §6 separates productive improvement, operational efficiency,
extractive improvement, regulatory arbitrage and reflexive capture ("Capacity
of others to establish and enforce requirements"), and guards the claim:
"This does not establish that lobbying, litigation or seeking regulatory
change is intrinsically wrongful. ... The pathological case requires
showing that the organization maintains obstructions to independently
justified constraints."

## What is held and what is added

- [THEORY-470](../theory.d/THEORY-470.md) (Doctorow, Proposed): decay comes from the weakening of the four
  constraints, not from a change in who runs platforms; it names regulation
  "Captured by concentrated industries". [THEORY-150](../theory.d/THEORY-150.md): each stage is made
  possible by the lock-in the one before built.
- [CLAIM-464](CLAIM-464.md): one intervention can alter control, access or enforcement
  before it is reviewed. [CLAIM-619](CLAIM-619.md): answering a challenge by reducing the
  capacity for challenge. [CLAIM-404](CLAIM-404.md): governing an organization through what
  its procedures receive.
- Added: the endogenous form. The optimization assigns the erosion a value
  of its own, so the account needs no change of character, which is how
  A46 §11 reads Doctorow's point that "the relevant constraints can change
  while the preferences of the people running an institution remain
  substantially the same".

## Note of 2026-11-24: the derivation A46 leaves out (the assistant)

A46 asserts that weakening oversight "could itself become valuable" without
showing it. In its own model it follows. Write the institution's value as
V(C) = max over (e, a) of [G(e) − L(e, C) − k(a) + δ V(Φ(C, e, a))], with
k(a) ≥ 0 the cost of an action on the constraints. Suppose (i) L(e, C′) ≤
L(e, C) for every e when C′ is a weaker-constraint state than C, and (ii) Φ
keeps that order (from a weaker state, the same choices lead to a weaker or
equal state). Then V(C′) ≥ V(C) by induction on the horizon, since every
period's payoff is at least as large from C′. An action a that moves the
next state from C to C′ and does nothing else is therefore worth δ[V(C′) −
V(C)] ≥ 0 and is taken whenever that exceeds k(a). Only G, L, Φ and k enter;
nothing about the decision-makers' dispositions does. A two-period check
(python3 -I): with G(e) = e and L(e, C) = C·e², the one-period optimum is
1/(4C), 0.25 at C = 1 and 0.5 at C = 0.5, so an action halving C next period
is taken whenever its cost is below δ·0.25.

Two conditions the model leaves implicit. First, (ii) can fail: eroding a
constraint can itself raise another term of L (visible lobbying invites
regulation or exit), and then the value is net, not guaranteed. Second, the
claim is about the policy, not the motive: the institution need not
represent the constraints as targets, only act on a score that rewards
their weakening. Whether that erosion is wrongful is the separate question
A48 §6 marks, answered only with an independently justified constraint
([CLAIM-624](CLAIM-624.md)). The wording of this note is the assistant's (Claude, in this
session); adopting it is the owner's call.
