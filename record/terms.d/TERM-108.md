---
number: 108
status: Proposed
formerly:
- TERM-tmp4gc9h
title: 'proxy objective, in an allocation model: an operational measure optimized in place of the outcome it stands for, whose optimum can differ from the outcome''s with no reaction of the measured to the measure'
version: 2
history:
- version: 2
  date: '2026-11-12'
  note: >-
    Now draws on THEORY-1384, coverage as "a proxy for the real objective"
    of survival: "Misalignment can be large". First application of
    draws_on (ADR-095). No other change.
tags:
- operations-research
- society-and-governance
- philosophy-of-science
date: '2026-11-04'
line:
- readiness
summary: >-
  Filed at the owner's request on 2026-11-04, to account for an idea the
  readings of the pasted bibliography on emergency readiness surfaced and
  the record lacked or described poorly. The record speaks of proxies in
  passing and holds measures that change what they measure ([LIT-1330](../literature.d/LIT-1330.md)),
  but has no word for a measure whose optimum differs from the outcome's
  while nobody reacts to it. Sources: McLay and Mayorga ([LIT-2090](../literature.d/LIT-2090.md),
  Unavailable; abstract only) and Erkut, Ingolfsson and Erdoğan
  ([LIT-2089](../literature.d/LIT-2089.md)), on response-time coverage standing in for survival. The
  wording is the filer's; adopting it is the owner's call.
draws_on:
- THEORY-1384
---
<!-- inactive-ok-file: ADR-095 — Proposed; the decision this entry's history note of 2026-11-12 applies -->
<!-- inactive-ok-file: LIT-2090 — Unavailable; cited for its published abstract, nothing here rests on it -->
<!-- inactive-ok-file: THEORY-1384 TERM-110 — Proposed; Erkut and colleagues' account and the ratchet term of the same filing, cited as filed -->
<!-- inactive-ok-file: THEORY-1775 — filed from the exchange "luria experiment design", Proposed or Deferred; cited as filed alongside this entry -->

# TERM-108: proxy objective, in an allocation model: an operational measure optimized in place of the outcome it stands for, whose optimum can differ from the outcome's with no reaction of the measured to the measure

## Definition

A **proxy objective** is a measure that an allocation is chosen to
optimize because it is easier to obtain or understand than the outcome it
stands for, when the outcome, not the measure, is what the allocation is
for. Its **misalignment** is the gap between the outcome at the proxy's
optimum and the outcome at the outcome's own optimum.

The term separates misalignment from reactivity. A proxy can be
misaligned with nobody gaming it: the measure does not change what it
measures, it only selects a different allocation. The readers of both
sources drew this line against the record's nearest held work, Espeland
and Sauder on rankings ([LIT-1330](../literature.d/LIT-1330.md), [NOTE-1050](../notes.d/NOTE-1050.md)), which is about reactivity.

## From the readings

- **Why the proxy is used.** McLay and Mayorga's abstract ([LIT-2090](../literature.d/LIT-2090.md),
  unread): emergency medical services are judged by the share of calls
  reached within a fixed time, not by patient outcomes, and "These
  response time thresholds are used because they are easy to obtain and
  to understand."
- **Misalignment can be large.** Erkut, Ingolfsson and Erdoğan
  ([LIT-2089](../literature.d/LIT-2089.md), [NOTE-1556](../notes.d/NOTE-1556.md); [THEORY-1384](../theory.d/THEORY-1384.md)) "take as given that the real objective
  for an EMS system is to maximize the number of patients that survive
  and that coverage is used as a proxy for the real objective", and give a
  constructed example in which "covering models can result in arbitrarily
  poor location decisions for emergency facilities". On their data,
  "just changing the objective function to expected number of survivors
  achieves all of the benefits".
- **Misalignment can also be nil.** McLay and Mayorga's abstract: "The
  results indicate that locating ambulances to maximize seven and eight
  min response time thresholds simultaneously maximize patient survival",
  while nine- and ten-minute thresholds give more equitable outcomes. In
  Erkut and colleagues' comparison, an expected-coverage model with
  server availability reaches the best-known number of survivors. So a
  proxy is not misaligned as such; how far it is depends on the threshold
  and on what else the model holds.

## Bearing on emergency readiness

A readiness measure is usually a proxy of this kind: a response-time
standard, or a fraction of calls covered, chosen in place of what the
response is for. The term lets the record say that such a standard can
select the wrong allocation before anyone responds to it strategically,
which is a different failure from a ratchet ([TERM-110](TERM-110.md), filed the
same day), where the measured party acts on the measure.

## What it is not

- **Reactivity, or Goodhart's law** ([LIT-1330](../literature.d/LIT-1330.md); [CASE-023](../cases.d/CASE-023.md)'s Goodhart
  metric): a measure that changes the behaviour it measures once it is a
  target.
- **A probe that is also the training signal** ([CLAIM-266](../claims.d/CLAIM-266.md)): a system
  optimized on its own evaluation, which becomes good at the probes
  without the intended capacity. There the misalignment is produced by the
  optimization; here it is fixed by the choice of measure.
- **A proxy in an organization's own ordering** ([QUESTION-267](../questions.d/QUESTION-267.md)): whether a
  negotiation that ranks states by a proxy for maintenance is valence.
  That is about an organization's own concern; this is about a planner's
  chosen objective.

## What would settle it

A claim of the record's own stated in it, or a reading of McLay and
Mayorga's paper confirming its result against the abstract. Adopting it is
the owner's call.

## Note of 2026-11-12: Moats et al. (2026), read

From the reading in [NOTE-1760](../notes.d/NOTE-1760.md) ([LIT-2361](../literature.d/LIT-2361.md)), the reader's assessment as
checked by the filer: value narrowing is the discursive counterpart, where
the proxy keeps the outcome's name. Not cited by the LIT.

## Note of 2026-11-12: Yu, Kim and Kim (2026), read

From the reading in [NOTE-1752](../notes.d/NOTE-1752.md) ([LIT-2371](../literature.d/LIT-2371.md)), the reader's assessment as
checked by the filer: the paper's "deceptively healthy" state is accuracy as
a proxy for evidential health diverging from provenance; the authors do not
frame it so.

## Note of 2026-11-12: Jackson et al., read

Read on 2026-11-12 among the works of the exchange "luria experiment design"; each reading's NOTE and THEORY hold the detail.

- **Jackson et al.** ([THEORY-1775](../theory.d/THEORY-1775.md)): The Maintenance check (date-format version IRI) is the authors' own example of a proxy check they say does not establish the principle. Illustrates it.

The term is unchanged.
