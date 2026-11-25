---
number: 155
status: Proposed
formerly:
- TERM-tmpqfgw9
complements:
- TERM-042
title: 'determinacy cover'
statement: >-
  determinacy cover, of a receiver population at a threshold: the questions
  it answers determinately, as a thresholded functional of the empirical
  model
version: 1
tags:
- contextuality
- mathematics
date: '2026-11-22'
line:
- pragmatic-transport
draws_on:
- THEORY-012
---
<!-- inactive-ok-file: CLAIM-201 CLAIM-251 — Proposed; the entries that use "cover" in this operational sense, and the counter that asked for a separate name -->

# TERM-155: determinacy cover

## Definition

Fix a measurement scenario (X, M, O) and an empirical model e on it (the
communicative object of [TERM-042](TERM-042.md): a distribution e_C over ℰ(C) per
context C ∈ M). Fix a threshold θ. The **determinacy cover** of a receiver
population whose responses are e is

  D_θ(e) = { x ∈ X : max_o m_x(o) ≥ θ },

the measurements whose response marginal m_x is concentrated above θ — the
questions the population answers determinately, in [CLAIM-201](../claims.d/CLAIM-201.md)'s sense
("agreement among readers above a threshold fixed in advance"). It carries the
induced sub-scenario (D_θ(e), {C ∩ D_θ(e) : C ∈ M}, O) with the restriction
maps inherited from the event presheaf ℰ ([CASE-368](../cases.d/CASE-368.md)).

This term exists to do the job [CLAIM-251](../claims.d/CLAIM-251.md) asked for: give the operational
notion its own name, so that an entry using "cover" can say whether it means
this or the sheaf-theoretic cover. [CLAIM-201](../claims.d/CLAIM-201.md), [CLAIM-257](../claims.d/CLAIM-257.md), [CLAIM-256](../claims.d/CLAIM-256.md) and
[CLAIM-125](../claims.d/CLAIM-125.md) use "cover" in this operational sense.

## What it is not

- **Not the cover M of the scenario** ([TERM-042](TERM-042.md), [THEORY-012](../theory.d/THEORY-012.md)). M is the
  family of jointly-measurable contexts, part of the scenario and prior to any
  responses. The determinacy cover is selected *from* a scenario by a property
  of the responses. On a fixed scenario, changing e changes D_θ(e) while M
  stays put ([CASE-368](../cases.d/CASE-368.md), fact 3).
- **Not contextuality.** Contextuality is a property of the empirical model on
  a fixed cover (whether the e_C glue). The determinacy cover concerns which
  single questions have a sharp answer, a weaker and prior condition
  ([CLAIM-201](../claims.d/CLAIM-201.md): "changed which questions can be asked, not shown that the
  answers cannot be glued").
- **Not a canonical functor of the model.** The map e ↦ D_θ(e) is a
  thresholded readout: it depends on θ, shrinks as θ rises, and is not
  injective ([CASE-368](../cases.d/CASE-368.md), fact 4). It yields a genuine induced sub-site
  but is not structure-preserving in e.
- **Not the whole fidelity profile.** The observational distortion D_obs
  ([TERM-021](TERM-021.md), [TERM-043](TERM-043.md), [CLAIM-257](../claims.d/CLAIM-257.md)) is summed over contexts that are
  determinate for both sides; the determinacy cover is the set those sums range
  over, and the questions only one side can decide are reported apart from it.

The wording is the assistant's (Claude, in this session); adopting it is the
owner's call.
