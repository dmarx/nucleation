---
status: Proposed
title: 'Coupled competence and valuation model of interest'
statement: >-
  Two variables on [0, 1], competence c in an activity and the activity's
  motivational significance v, with ċ = αv(1 − c) − μc and v̇ = βc(1 − v)
  − νv + s(t), where engagement driven by v builds competence, competence
  makes rewarding experience accessible and so builds v, both decay, and
  s(t) is temporary external support such as mentorship
version: 1
standing: stipulated
kind: construction
tags:
- motivation
- learning-and-conditioning
- complex-systems
date: '2026-11-26'
line:
- transient-support
- will-organization
- flourishing-and-meaning
summary: >-
  A21 §5 of the exchange "Alignment consequences brainstorm" (ChatGPT,
  2026-11-26), "A minimal dynamical model of axiological nucleation",
  offered as "Illustrative dynamics, not fitted psychological data", with
  an interactive figure whose sliders set "Temporary external support" and
  "Competence–valuation coupling". A21 linearizes at zero and finds it
  unstable when αβ > μν, which is right, and itself notes "the model above
  has a coupling threshold, not a finite-amplitude nucleation threshold".
  [CLAIM-tmpyk6bi](../claims.d/CLAIM-tmpyk6bi.md) works out what that leaves for the support term. The
  wording is A's; adopting it is the owner's call.
---
<!-- inactive-ok-file: ARG-tmpahwlh CLAIM-tmp1njmb CLAIM-tmpyk6bi — Proposed, Rejected; filed, registered or cited in the filing of 2026-11-26 from the exchange "Alignment consequences brainstorm" -->

# CASE-tmpaqihm: Coupled competence and valuation model of interest

## The model

A21 §5 asks "Could an interest exhibit something analogous to a
nucleation threshold?" and writes

  ċ = αv(1 − c) − μc,
  v̇ = βc(1 − v) − νv + s(t),

"Here s(t) represents temporary external support, such as mentorship or
encouragement. The important feature is the reciprocal coupling.
Competence helps make rewarding experiences accessible, while those
experiences motivate the exercise through which competence develops."

Without support the Jacobian at the origin is [[−μ, α], [β, −ν]], and
"The zero state becomes unstable when" αβ > μν, which A21 reads as
"reciprocal production exceeds the combined decay of its constituent
capacities", and as "a simple mechanism through which an initially
instrumental activity becomes motivationally self-maintaining".

The figure's two captions are "With these parameters, reciprocal
reinforcement supports a nonzero equilibrium even after the external
support is withdrawn" and "With these parameters, reciprocal
reinforcement is insufficient to sustain a positive equilibrium after
support is withdrawn."

## What A21 itself limits

- "A genuine nucleation model with coexisting stable low- and
  high-interest states would require additional nonlinearities."
- "even that richer model would only explain the stabilization of
  motivational significance. It would not yet establish that the interest
  is authentic, worthwhile, or a legitimate purpose."

## What it is used for

It is the model A21 offers for its mechanism, [CLAIM-tmp1njmb](../claims.d/CLAIM-tmp1njmb.md). [CLAIM-tmpyk6bi](../claims.d/CLAIM-tmpyk6bi.md)
derives its equilibria and shows that the support term cannot decide
whether an interest outlasts the support; [ARG-tmpahwlh](../arguments.d/ARG-tmpahwlh.md) is the inference from the
model to the claim. The record's model with a seed threshold is
[CLAIM-1310](../claims.d/CLAIM-1310.md)'s fold.
