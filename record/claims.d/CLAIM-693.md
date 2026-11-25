---
number: 693
status: Proposed
formerly:
- CLAIM-tmpicwgd
title: 'Detecting outside maintenance scales with mimicry'
statement: >-
  The interventions needed to find that a structure's maintenance comes from
  outside grow with how much of the internal production law the outside
  maintainer reproduces: a supply that ignores the structure's state is
  exposed by perturbing the state, one that runs the law on a delayed
  reading of the state is exposed only by perturbations faster than its
  delay, and one that runs the exact law on the present state is exposed
  only by intervening on the production mechanism
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An outside maintainer that reproduces more of the production law than
  another yet is exposed by coarser interventions on state, within one
  model; or a reading of CLAIM-522 under which its "Delay, saturation and
  noise may leave signatures" already states this ordering, so that the
  claim restates it.
tags:
- complex-systems
- causality
- individuation
date: '2026-11-15'
line:
- transient-support
- distributed-agency
complements:
- CLAIM-522
grounds:
- CASE-268
- CASE-265
summary: >-
  The assistant's, offered at the end of the filing of 2026-11-15 and
  filed at the owner's request. [CLAIM-522](CLAIM-522.md) proves the ideal end: a
  controller that supplies the internal law as state feedback mimics
  internal maintenance under every intervention on state. [CASE-265](../cases.d/CASE-265.md)
  showed the other end: a constant controller is exposed by perturbing the
  state. This claim fills the rungs between with one family, demonstrated
  for delayed copies of the law in [CASE-268](../cases.d/CASE-268.md). That the ordering holds
  beyond that family is the claim's general reading and stays open. The
  wording is the assistant's (Claude, in this session); adopting it is the
  owner's call.
---
<!-- inactive-ok-file: CASE-268 CASE-265 — Proposed or new; the constructions the claim rests on -->

# CLAIM-693: Detecting outside maintenance scales with mimicry

## The demonstration

In the mutual-maintenance model ([CASE-265](../cases.d/CASE-265.md), [CASE-268](../cases.d/CASE-268.md)):
- A constant supply of the capacity differs from internal production
  after a brief knock to the structure, by 0.146.
- A supply running the law on a reading of the structure τ old differs by
  0.146, 0.083, 0.033 and 0.010 for τ = 1, 0.3, 0.1 and 0.03.
- A supply running the law on the present state differs by nothing under
  any knock or start tried. Cutting the internal pathway separates it
  at once.

## What it changes

[CLAIM-522](CLAIM-522.md) says only interventions on the mechanism separate internal
production from an ideal outside controller. It allows that imperfect
controllers "may leave signatures". This claim says the signatures have an
order. An auditor asking whether an organization maintains itself or is
kept from outside should choose interventions finer than the suspected
maintainer's fidelity. A coarse audit that finds nothing is evidence only
against coarse maintainers.

## What it does not say

That fidelity is one-dimensional. A maintainer can be exact in one
respect and crude in another, and then each respect has its own rung.

## Note of 2026-11-25: rerun, and what holds it back

Rerun on 2026-11-25 by the assistant, a session other than the filer's, in the recomputation pass of [LEAD-252](../leads.d/LEAD-252.md), at the owner's go-ahead of 2026-11-25 ("go ahead with the reruns"). Both constructions it rests on reproduce (their notes of this date): `scratch/formal/maintainer_ladder_check.py` gives the gaps 0.146, 0.083, 0.033 and 0.010 for τ = 1, 0.3, 0.1 and 0.03, 0.146 for the constant supply and zero for the exact controller, and an independent RK4 integration agrees to four decimals; `scratch/formal/soliton_testbed_checks.py` passes. What holds it back: [ADR-057](../decisions.d/ADR-057.md)'s first criterion. Its grounds [CASE-268](../cases.d/CASE-268.md) and [CASE-265](../cases.d/CASE-265.md) are Proposed constructions, whose adoption is the owner's and is not a matter of recomputation. It goes Active when they do. The note is the assistant's (Claude, in this session). No status change.
