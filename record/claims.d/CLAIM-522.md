---
number: 522
status: Active
formerly:
- CLAIM-tmpr8p2x
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
works:
- WORK-010
complements:
- CLAIM-414
- CLAIM-194
- CLAIM-407
bears_on:
- QUESTION-093
grounds:
- 'CASE-189'
summary: >-
  From A10 §4 (its Proposition 5) of the exchange "Analyze nucleation
  concepts" (2026-10-31). Close to definitional, and checked: substituting
  the controller gives the same differential equation. It extends
  [CLAIM-414](CLAIM-414.md) from passive observation to every intervention on state. As
  the reader noted, the causal dependence among the capacities is the same
  in both systems; only where the mechanism sits relative to the boundary
  differs, which is [CLAIM-194](CLAIM-194.md)'s point about boundaries.
---
<!-- inactive-ok-file: QUESTION-093 — Open; the question of separable autonomy conditions, cited as open -->

# CLAIM-522: Recovery under interventions on state cannot show where maintenance is realized: an outside controller that measures the constraint capacities and supplies the internal production law as state feedback yields the same trajectory under every perturbation of state, damage and recovery included, even with every capacity observed exactly; only interventions on the production mechanisms, relative to a declared boundary, separate the two

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
or interrupting the controller (B loses it, A does not). [CASE-161](../cases.d/CASE-161.md) and
[CASE-163](../cases.d/CASE-163.md) are the record's runs of such interventions.

## What it does not say

- **That the two are the same organization.** The point is that they differ
  only in where the producer sits relative to a boundary, and that state
  interventions cannot see it.
- **That every controller mimics perfectly.** Delay, saturation and noise
  may leave signatures. The claim is the ideal case, which is the one that
  shows the limit is in principle.
- **That the boundary is given.** Which mechanism is "inside" is fixed by a
  declared boundary, and a gap criterion cannot supply it ([CLAIM-194](CLAIM-194.md)).

## Note of 2026-11-01: constitutive relevance needs the boundary too

<!-- inactive-ok-file: CLAIM-530 THEORY-1292 LIT-1931 LIT-1930 — Proposed, Unfetched or Unavailable; the claim and readings filed from the mechanism literature, cited as open -->

Read beside Craver and Bechtel ([LIT-1928](../literature.d/LIT-1928.md), [NOTE-1491](../notes.d/NOTE-1491.md)) and Bechtel
and Abrahamsen ([LIT-1936](../literature.d/LIT-1936.md), [NOTE-1492](../notes.d/NOTE-1492.md)). Craver's own statements of
the criterion ([LIT-1930](../literature.d/LIT-1930.md), [LIT-1931](../literature.d/LIT-1931.md)) were not reached.

- **Is "where maintenance is realized" a question of constitutive
  relevance? Yes, but the criterion does not answer it without this
  claim's declared boundary.** Take this claim's producer and controller
  as candidate components for "c is maintained". Both meet mutual
  manipulability's bottom-up and top-down conditions with identical
  responses. Disabling or stimulating either changes c, and intervening
  on c changes either's activity, because the equations coincide.
  Craver and Bechtel's one marker of a component against a background
  condition, being "interactively integrated" (p. 553, n. 10), is met by
  a controller that reads c and acts on it ([THEORY-1287](../theory.d/THEORY-1287.md)). What
  separates them is the criterion's parthood condition, which is this
  claim's boundary. Filed as [CLAIM-530](CLAIM-530.md), Proposed until Craver's
  texts are read. What the criterion needs is what this claim says:
  ideal interventions on the parts, relative to a mechanism boundary
  declared beforehand.
- **A candidate source for the boundary.** Closure in [TERM-070](../terms.d/TERM-070.md)'s sense
  would count a producer as inside when it is itself maintained by what
  it produces. This claim's one-variable model has no term for the
  producer's own maintenance, so it cannot test that. A construction
  that could would intervene one level down.
- **A biological case at the claim's edge.** Peripheral circadian clocks
  posed this claim's question: are they self-sustained, or damped
  oscillators driven by the SCN ([LIT-1936](../literature.d/LIT-1936.md), p. 328)? There the outside
  drive does not reproduce the inside law, and a model predicts different
  responses to a phase shift ([THEORY-1292](../theory.d/THEORY-1292.md)). That is the case the
  claim's defeated_if sets aside, a controller unlike the ideal one, which
  state probes may expose.
- **The same structure in a model of memory.** McClelland et al. supply
  the hippocampus's training signal to a neocortex model from outside the
  model, and stopping it stands for a lesion ([LIT-1936](../literature.d/LIT-1936.md), p. 331). Same
  structure, not shown same mechanism: inside the model, nothing
  distinguishes a part's output from one the modeller supplies.

No status, title or warrant changes.
