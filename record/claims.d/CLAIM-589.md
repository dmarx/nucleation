---
number: 589
status: Proposed
formerly:
- CLAIM-tmpx3v84
title: 'A motion the constraints permit need not be one the available inputs can drive, and a motion the inputs can drive need not be cheap, reliable or sustainable: permitted directions, actuated directions and transitions achievable at acceptable cost are three objects, the second contained in the first at each instant, while over a horizon what is reachable can exceed what either spans at an instant'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the witnesses or the containment: an input that moves a
  mechanism in a direction its constraints forbid at that instant; a
  point in the plane driven only along x that reaches a state off the
  line; a target of ẋ = x + u with |u| ≤ 1 that is reached and cannot be
  held under the stated bound but can in fact be held; or an error in
  CLAIM-345 or CLAIM-542, on which the cost and reliability separations
  rest. Not defeated by systems in which the three coincide, nor by
  mechanisms in which passive freedoms do useful work without being
  driven; the claim is that the three can come apart.
tags:
- control-theory
- mathematics
- agency
date: '2026-11-05'
line:
- realizability
- formal-apparatus
rests_on:
- CLAIM-345
- CLAIM-542
grounds:
- THEORY-1432
- THEORY-1390
complements:
- CLAIM-354
- CLAIM-567
- CLAIM-582
summary: >-
  A's proposal, from the pasted synthesis on constraint architectures
  (pasted by the owner on 2026-11-04, continuing the exchange on emergency
  readiness whose share link could not be fetched), Parts 1 and 2: "A
  permitted motion is not necessarily a controllable motion, and a
  controllable motion is not necessarily inexpensive, reliable, or
  sustainable." The record held the later links (cost in [CLAIM-345](CLAIM-345.md),
  reliability in [CLAIM-542](CLAIM-542.md) and [CLAIM-567](CLAIM-567.md)) and the first only as
  [CASE-194](../cases.d/CASE-194.md)'s shared actuator. A point driven along one axis gives the
  first separation; an unstable scalar with bounded input gives
  reachable-but-not-holdable. Murray and Sastry's car shows that over a
  horizon reach can exceed what is permitted at an instant, and Hopkins's
  actuation spaces that whether a freedom can be driven by linear
  actuators depends on stiffness. The wording is A's; adopting it is the
  owner's call.
---
<!-- inactive-ok-file: CASE-194 THEORY-1432 THEORY-1390 NOTE-1596 — Proposed or Skimmed; an entry of 2026-11-05 from the same paste, the shared-actuator case and the readings' accounts, cited as filed, nothing here rests on their being settled -->

# CLAIM-589: A motion the constraints permit need not be one the available inputs can drive, and a motion the inputs can drive need not be cheap, reliable or sustainable: permitted directions, actuated directions and transitions achievable at acceptable cost are three objects, the second contained in the first at each instant, while over a horizon what is reachable can exceed what either spans at an instant

## The claim

A: "A mechanism may be free to move in a direction without possessing the
means to drive itself in that direction." And: "A permitted motion is not
necessarily a controllable motion, and a controllable motion is not
necessarily inexpensive, reliable, or sustainable."

Write F(q) for the directions the constraints permit at q, and G(q) for the
span of the directions the inputs drive. An input pushing against a
constraint moves nothing along it, so every driven velocity is permitted:
G(q) ⊆ F(q) at each instant.

**Permitted, not driven.** A point in the plane with no constraints, so
F = ℝ², and one input along x: ẋ = u, ẏ = 0. The y direction is permitted
at every instant and driven at none, and nothing reaches off the line
y = y₀. Hopkins's thesis gives the mechanical form ([NOTE-1596](../notes.d/NOTE-1596.md), skimmed;
[THEORY-1390](../theory.d/THEORY-1390.md)). Where actuators must act to drive a flexure's freedoms
without parasitic error is set by the flexures' stiffness, and if the
system's actuation space is not among the twenty-six, "the designer knows
that this system cannot be actuated with linear actuators alone". The
freedom space alone does not settle that. [CASE-194](../cases.d/CASE-194.md)'s structural
organization, with one shared actuator setting, is the organizational
construction.

**Driven, not cheap.** Equal controllability rank leaves the least effort
free: Δ²/b² for x_{t+1} = x_t + b·u, unbounded as b → 0 ([CLAIM-345](CLAIM-345.md)).

**Cheap, not reliable.** Along an unstable direction a larger exponent
lowers the least effort, while an open-loop input against noise in the
same direction loses signal-to-noise ratio ([CLAIM-542](CLAIM-542.md)). A reachable
target can also be reached with probability 1/2 when the process meets an
unbiased fork ([CLAIM-567](CLAIM-567.md)).

**Reached, not sustainable.** Take ẋ = x + u with |u| ≤ 1, from x = 0.
Setting u = 1 gives ẋ = x + 1 > 0, so x = 2 is reached. Holding it needs
ẋ = 0, that is u = −2, which the bound forbids. The state is reachable and
cannot be held. This is the shape of [CLAIM-079](CLAIM-079.md)'s split between stability
and viability, with the input bound as the constraint.

**Over a horizon, reach exceeds the instant.** The containment G ⊆ F holds
at each instant. Reach over a horizon is bounded by neither. Murray and
Sastry ([NOTE-1622](../notes.d/NOTE-1622.md); [THEORY-1432](../theory.d/THEORY-1432.md)): "the Lie bracket is the infinitesimal
motion that results from flowing around a square defined by two tangent
vectors", and by Chow's theorem a driftless system whose input fields and
their brackets span every direction is controllable. The kinematic car's
rolling constraint forbids sideways motion at each instant, and loops of
input reach sideways displacements. A: "a purely instantaneous account of
freedom may radically underestimate long-horizon capability". So the
first object, read at an instant, is not an upper bound on capability.

## What it does not say

- **That the three are ordered as capabilities.** Only the containment of
  driven directions in permitted ones, at an instant, is an order. Over a
  horizon, reach can exceed both.
- **That an undriven freedom is useless.** In Dollar and Howe's hand
  ([NOTE-1575](../notes.d/NOTE-1575.md)), "An adaptive, underactuated hand has fewer actuators than
  degrees of freedom", and the freedoms left passive do the work of fitting
  the grasp. A freedom need not be driven to be used.
- **Anything about organizations.** A's reading, that an organization can
  be permitted a change it has no means to make, is an analogy. The
  witnesses are a construction, a scalar system and mechanisms.
