---
number: 1336
status: Proposed
formerly:
- THEORY-tmpoy5a7
promote_when: >-
  Reproduction of the cart-pole result from the published model and
  parameters (Table 1, eqs. 4–11), showing both that a controller greedily
  maximizing 10-step empowerment balances the pole and that the states of
  maximum empowerment are not reachable under the agent's own dynamics, and
  a second system, not chosen for having an upright target, in which
  greedily maximized empowerment settles the agent into a regime other than
  the empowerment maxima. A replot of the paper's figures does not settle
  it, and neither does a system where the empowerment maximum is reachable.
title: 'In a cart-pole whose only given utility is 10-step empowerment, a controller that greedily picks the action leading to the more empowered successor balances the pole upright, though the states of highest empowerment lie off-centre and cannot be reached or sustained under the agent''s own dynamics; what the agent can keep is not where empowerment is highest'
version: 1
tags:
- information-theory
- agency
date: '2026-11-03'
source:
- LIT-1951
summary: >-
  Klyubin, Polani and Nehaniv (2008), [LIT-1951](../literature.d/LIT-1951.md), pp. 4–7, read in
  [NOTE-1514](../notes.d/NOTE-1514.md). A single simulation of one model with two actions,
  computed by the authors; the robustness of the off-centre maxima is
  stated, not shown. Proposed for want of a reproduction and a second
  system.
---
<!-- inactive-ok-file: CLAIM-354 — Proposed; the claim the result bears on -->

# THEORY-1336: In a cart-pole whose only given utility is 10-step empowerment, a controller that greedily picks the action leading to the more empowered successor balances the pole upright, though the states of highest empowerment lie off-centre and cannot be reached or sustained under the agent's own dynamics; what the agent can keep is not where empowerment is highest

## Source

Klyubin et al. (2008), [LIT-1951](../literature.d/LIT-1951.md); read in [NOTE-1514](../notes.d/NOTE-1514.md).

## What was actually shown

- Actions ±10 N held for 3 steps of 0.02 s; 10 actions; the angle observed in
  101 bins; perturbed ensembles of 5⁴ starts; capacity by Blahut to 10⁻⁴ bit.
- With other variables zero, empowerment peaks at upright and drops to zero
  past a critical angle (Figure 2).
- Over angle and angular speed, the maximum is off-centre, by 0.07 bit,
  "robust with respect to the variation of parameters", absent without the
  cart (p. 6).
- Those states are unreachable "in a sustained run under its own dynamics",
  like Garden-of-Eden states (p. 6).
- The greedy controller (Figure 4) "performs classic pole-balancing"
  (p. 6), with no plan beyond a 1 + 10 step horizon.

## What this does not say

- That empowerment maximization generally finds the intuitive task.
- That upright is the empowerment optimum: it is near, not at, the maximum.
- Bearing: [CLAIM-354](../claims.d/CLAIM-354.md)'s reachable set, not a state-wise score, is what
  separates what an agent can keep from what is merely best placed.
