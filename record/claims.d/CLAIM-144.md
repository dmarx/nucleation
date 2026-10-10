---
number: 144
status: Active
formerly:
- CLAIM-tmpersh3
title: 'Inertial observers who disagree about temporal order differ in coordinates, not in a failure to glue: only spacelike-separated events change order between frames, and frames are global charts related by a group action'
version: 1
role: granted
tags:
- natural-sciences
- mathematics
date: '2026-10-10'
line: pragmatic-transport
undercuts:
- ARG-010
grounds:
- CASE-039
complements:
- CLAIM-035
uses:
- TERM-004
summary: >-
  A164's correction of the owner's U47, which is standard special
  relativity, with two repairs. A164 left out the reading of the
  owner's scenario whose answer is invariant (two passings of one
  marker). And it described frames as patches glued by a cocycle, which
  they are not: each inertial frame charts all of spacetime, and the
  frames are related by the Poincaré group.
illustrated_by:
- CASE-039
---
<!-- inactive-ok-file: ARG-010 — Rejected; cited as the inference this claim undercuts -->
<!-- inactive-ok-file: CLAIM-143 CLAIM-038 — Proposed; open, and cited as open: the claim is under test, not settled -->

# CLAIM-144: Inertial observers who disagree about temporal order differ in coordinates, not in a failure to glue: only spacelike-separated events change order between frames, and frames are global charts related by a group action

## The claim

A164: for two events, Δt′ = γ(Δt − vΔx/c²), and "This reversal is due
specifically to **relativity of simultaneity**, not merely time dilation."
The reversal needs c²Δt² − Δx² < 0, that is, spacelike separation. "If one
event could causally influence the other, their time order cannot reverse
under a proper, orthochronous Lorentz transformation." All of this is
correct. Its conclusion: "**The relativistic example is therefore not
evidence that global gluing fails.**"

So, for the cases [CASE-039](../cases.d/CASE-039.md) separates:

- coincident events have no order to disagree about;
- events on one worldline, such as two passings of one marker, are
  timelike-separated and have an invariant order;
- only spacelike-separated events change order between frames.

## Two repairs to A164

**The owner's own scenario.** A164 moved to "two different markers" without
saying that the scenario U47 described, read either as one meeting or as
two passings of one marker, has an answer every frame agrees on. Only the
substitute scenario has a frame-dependent order.

**No gluing picture.** A164 set its lesson inside a cover of patches, with a
cocycle g_ik = g_jk ∘ g_ij and equivariance O_j(Ts) = ρ_ij O_i(s). But each
inertial frame coordinatizes all of Minkowski space. The transition maps
form a group action, and the cocycle holds trivially. The structure is
invariance or equivariance ([TERM-004](../terms.d/TERM-004.md)), not a sheaf over a cover. The order
of two spacelike events is not an observable that any frame-independent
description contains, so nothing fails to glue. There is no cover whose
sections could fail to glue.

Granted, because it is textbook physics, and because it is what the
argument needs in order to refuse the owner's inference ([ARG-010](../arguments.d/ARG-010.md)).

## What it does not say

- It does not reject A164's lesson for transport, that a correspondence must
  be fixed before a disagreement is read as incompatibility. That lesson is
  [CLAIM-143](CLAIM-143.md), and this claim is its positive control.
- It does not say physics never has gluing obstructions. Holonomy and
  anomalies are real ones, and none of them arose in the exchange.
- It does not say that translation correspondences behave as Lorentz maps
  do. They are not invertible and form no group ([CLAIM-035](CLAIM-035.md)).
- It says nothing for or against [CLAIM-038](CLAIM-038.md)'s allowance that local
  interpretations may lack a global one. It removes one argument offered for
  it.
