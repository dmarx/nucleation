---
status: Proposed
title: 'The governance-induced kind of frustration is not idle: some failures of an organization''s actual updates to meet demands that an admissible update would meet are explained by how influence is allocated, and not by step size, curvature, noise, conditioning or a fixed weighting rule'
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  A showing that every failure of actual updates to meet satisfiable
  demands is explained by known optimization mechanisms (step size,
  curvature, noise, conditioning, a fixed weighting rule) without
  modelling endorsement or the allocation of authority, so that the
  governance-induced category adds nothing an optimizer analysis does not
  already give. Not defeated by cases where the two kinds occur together.
tags:
- self-governance
- agency
- operations-research
date: '2026-10-30'
line:
- distributed-agency
- will-organization
rests_on:
- CLAIM-357
uses:
- TERM-060
complements:
- CLAIM-297
- CLAIM-330
- CLAIM-342
summary: >-
  Split from [CLAIM-357](CLAIM-357.md) by the eighteenth status review ([ADR-057](../decisions.d/ADR-057.md); [ADR-047](../decisions.d/ADR-047.md)'s
  kind 2, the record's own extrapolation). [CLAIM-357](CLAIM-357.md) separates structural
  infeasibility, realized violation and minimax suboptimality, and says
  none of them identifies thwarting. This claim is the thesis that its old
  defeat condition tested: that the governance-induced kind does work an
  optimizer analysis does not, because some satisfiable demands go unmet
  through the allocation of influence. Untested; A39's case study 2 on
  [CASE-099](../cases.d/CASE-099.md) would test it.
---

# CLAIM-tmp4u6xx: The governance-induced kind of frustration is not idle: some failures of an organization's actual updates to meet demands that an admissible update would meet are explained by how influence is allocated, and not by step size, curvature, noise, conditioning or a fixed weighting rule

## The claim

[CLAIM-357](CLAIM-357.md) gives the diagnostics: with m(d) the worst residual of an update,
Φ its minimum over the admissible set and Γ the actual update's excess over
Φ, a realized violation with Φ ≤ 0 means a jointly satisfactory update
existed and was not made. Neither Φ nor Γ says why. This claim is that, in
some such failures, the reason is the allocation of influence: the
satisfactory update exists, search and information would find it, and the
way authority is allocated among the organization's processes keeps it from
being chosen.

The mechanism the record already holds is a loop of the kind [CLAIM-297](CLAIM-297.md)
describes: authority updated on the interpretation it helped make dominant
can amplify without gaining fidelity. [CLAIM-330](CLAIM-330.md) gives the instability
threshold βγ > (1 − α)(1 − δ) in [CASE-099](../cases.d/CASE-099.md)'s linearization, and [CLAIM-342](CLAIM-342.md)
says what keeps such a loop honest is evidence that does not pass through
the interpretation it tests. A captured allocation of that kind leaves the
satisfactory update unchosen, which is governance-induced frustration.

## How it would be tested

A39's case study 2: [CASE-099](../cases.d/CASE-099.md) with declared demands and a feasible-update
oracle. A39 called it "the best candidate for an early discriminating
experiment". The test intervenes on the allocation of influence with
search and information held fixed, and asks whether realized violations
fall when only the allocation changes, beyond what changes to step size,
curvature, noise, conditioning or a fixed weighting rule produce.

## What it does not say

- That governance-induced frustration is common, or worse than the
  structural kind.
- That the declared demands are the organization's own standard
  ([QUESTION-087](../questions.d/QUESTION-087.md)).
- That the multipliers certifying infeasibility should be governance's
  weights ([QUESTION-126](../questions.d/QUESTION-126.md)).

## Note of 2026-10-30: what holds it back

No case has been tested. The discriminating experiment A39 proposed,
[CASE-099](../cases.d/CASE-099.md) with declared demands and a feasible-update oracle, intervening on
the allocation of influence with search and information held fixed, has not
been run.
