---
number: 1396
status: Active
formerly:
- THEORY-tmphqo3c
title: 'Mukhopadhyay and colleagues present static coverage models for emergency response as moving from deterministic models that treat a facility as always available, through multiple coverage as a partial hedge against busy stations, to probabilistic models that represent station availability explicitly, beginning with the maximum expected covering and maximum availability models'
version: 3
history:
- version: 1
  date: '2026-11-04'
  note: >-
    Filed Proposed from NOTE-1583, the reading of §6.1 and Table 1 of the
    review.
- version: 2
  date: '2026-11-06'
  note: >-
    Promoted by the twenty-ninth status review, at the status review's
    ruling (the owner delegated these rulings); ADR-065. NOTE-1583 v2
    re-reads §6.1 and Table 1 in full and checks every quotation. The
    review presents the deterministic models as treating a facility's
    resources as always available, multiple coverage as a partial remedy,
    and MEXCLP and MALP as the foundational probabilistic models. The old
    promote_when: "§6.1 and Table 1 of the review confirmed as presenting
    the deterministic coverage models as treating a facility's resources as
    always available, multiple coverage as a partial remedy for station
    unavailability, and the probabilistic models, from MEXCLP and MALP on,
    as modelling station availability explicitly." It is met. The summary's
    "Proposed until the owner judges whether a review's ordering of a
    literature is worth an account at all" was not a condition on the
    title, and is dropped.
- version: 3
  date: '2026-11-11'
  note: >-
    Reading review of 2026-11-11 (by topic, second run, part P), under
    ADR-091 and ADR-093. corroborates CLAIM-296 and CLAIM-312 added.
    Both cite Mukhopadhyay et al. (NOTE-1583) for coverage models in which
    "Resources at a facility are considered to be always available", set
    against probabilistic ones, as a case of having a resource without
    being able to deploy it. No other change.
tags:
- operations-research
- social-science
date: '2026-11-04'
source:
- LIT-2107
summary: >-
  Mukhopadhyay et al. (2020), [LIT-2107](../literature.d/LIT-2107.md), read in [NOTE-1583](../notes.d/NOTE-1583.md) (§6.1 and Table
  1). An account of how the review organizes the coverage literature, not
  of any model's correctness; it is limited to what that taxonomy states.
  Active as a report of how §6.1 orders the literature.
corroborates:
- CLAIM-296
- CLAIM-312
---

# THEORY-1396: Mukhopadhyay and colleagues present static coverage models for emergency response as moving from deterministic models that treat a facility as always available, through multiple coverage as a partial hedge against busy stations, to probabilistic models that represent station availability explicitly, beginning with the maximum expected covering and maximum availability models

## Source

Mukhopadhyay et al. (2020), [LIT-2107](../literature.d/LIT-2107.md); read in [NOTE-1583](../notes.d/NOTE-1583.md).

## What was actually shown

- **Deterministic models** (§6.1): LSCP, MCLP and many extensions "assume
  deterministic system behavior in regards to response. Resources at a
  facility are considered to be always available".
- **Multiple coverage** (§6.1): the double standard model "helps mitigate
  the issue of station unavailability", but both covering facilities can
  still be busy, and "Accounting for such situations requires modeling
  facility availability explicitly."
- **Probabilistic models** (§6.1): "Two foundational probabilistic models
  are the Maximum Expected Covering Location Model (MEXCLP) and Maximum
  Availability Location Problem (MALP)", followed by extensions that relax
  their assumptions (TIMEXCLP, AMEXCLP, QPLSCP).

## What this does not say

- Anything about the formulations or results of the models it orders; the
  review gives a line each and no formulas.
- That the order is historical in every case, or that later models
  dominate earlier ones.
- Anything about the value of a reserve or rarely used unit.
