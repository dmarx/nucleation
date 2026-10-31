---
status: Active
title: 'Recovery under interventions on state cannot show where maintenance is realized: an outside controller that measures the constraint capacities and supplies the internal production law as state feedback yields the same trajectory under every perturbation of state, damage and recovery included, even with every capacity observed exactly; only interventions on the production mechanisms, relative to a declared boundary, separate the two'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An intervention on state alone that separates the two systems when the
  controller supplies u_ext = P(c) exactly, with no delay, saturation or
  noise. The claim's limit is that ideal controller: a real one with lag or
  saturation may be detectable by state probes, and that is not a
  counterexample.
tags:
- causality
- individuation
- self-governance
date: '2026-10-31'
line:
- distributed-agency
- formal-apparatus
complements:
- CLAIM-414
- CLAIM-194
- CLAIM-407
bears_on:
- QUESTION-093
grounds:
- 'CASE-tmpwxags'
summary: >-
  From A10 §4 (its Proposition 5) of the exchange "Analyze nucleation
  concepts" (2026-10-31). Close to definitional, and checked: substituting
  the controller gives the same differential equation. It extends
  CLAIM-414 from passive observation to every intervention on state. As
  the reader noted, the causal dependence among the capacities is the same
  in both systems; only where the mechanism sits relative to the boundary
  differs, which is CLAIM-194's point about boundaries.
---
<!-- inactive-ok-file: QUESTION-093 — Open; the question of separable autonomy conditions, cited as open -->

# CLAIM-tmpr8p2x: Recovery under interventions on state cannot show where maintenance is realized: an outside controller that measures the constraint capacities and supplies the internal production law as state feedback yields the same trajectory under every perturbation of state, damage and recovery included, even with every capacity observed exactly; only interventions on the production mechanisms, relative to a declared boundary, separate the two

## The claim

System A maintains its capacities by its own production: ċ = P(c) − D(c).
System B has no internal production. An outside controller observes c
exactly and supplies u_ext = P(c): ċ = −D(c) + u_ext. For every initial
state, every perturbation of state applied at any time, and every damage
schedule acting through D, the two satisfy the same equation and so have
the same trajectory. Full observation of c changes nothing.

A10's words: "Complete state observability ⇏ identifiability of
maintenance provenance", and "A physical-coupling probe establishes that
the constraints are operative. A productive-mechanism intervention
establishes how those constraints are maintained. Neither substitutes for
the other."

What separates them is an intervention on the mechanism: disabling a
production pathway inside the declared boundary (A loses it, B does not),
or interrupting the controller (B loses it, A does not). CASE-161 and
CASE-163 are the record's runs of such interventions.

## What it does not say

- **That the two are the same organization.** The point is that they differ
  only in where the producer sits relative to a boundary, and that state
  interventions cannot see it.
- **That every controller mimics perfectly.** Delay, saturation and noise
  may leave signatures. The claim is the ideal case, which is the one that
  shows the limit is in principle.
- **That the boundary is given.** Which mechanism is "inside" is fixed by a
  declared boundary, and a gap criterion cannot supply it (CLAIM-194).
