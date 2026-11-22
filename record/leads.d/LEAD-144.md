---
number: 144
status: Open
formerly:
- LEAD-tmpq1z2m
title: 'Fit the dynamic beta-Bernoulli feature model to a mechanistic organizational simulator that does not assume its prior, with a shared-driver null, and score it on held-out interventions on the coupling'
version: 1
stage: specified
priority: high
method:
- empirical
- formal
tags:
- probabilistic-modeling
- social-ontology
date: '2026-11-19'
line:
- distributed-agency
advances:
- QUESTION-276
operationalized_in:
- CASE-165
- CASE-tmpshw39
summary: >-
  The question states that recovery under the model's own prior is not
  enough. Named in [QUESTION-276](../questions.d/QUESTION-276.md). Filed by the backlog audit of 2026-11-19.
---

# LEAD-144: Fit the dynamic beta-Bernoulli feature model to a mechanistic organizational simulator that does not assume its prior, with a shared-driver null, and score it on held-out interventions on the coupling

## What it would do

Build the simulator, fit [CASE-165](../cases.d/CASE-165.md)'s model, compare with modes a shared
exogenous driver produces without interaction, and predict held-out
interventions.

Where the record names it:

- [QUESTION-276](../questions.d/QUESTION-276.md): "feature discovery can be tested against a world that did
  not itself assume IBP-distributed employees"
- [QUESTION-276](../questions.d/QUESTION-276.md): "predicts the effect of intervening on the coupling"

## What would count

Features that beat the shared-driver null and predict interventions answer
[QUESTION-276](../questions.d/QUESTION-276.md); features no better than the null do not.

## Note of 2026-11-22: run, in one linear family, and what remains

<!-- inactive-ok-block: CASE-tmpshw39 CLAIM-tmpp56wv — new; this date's study and its finding -->
Done by the assistant on this date ([CASE-tmpshw39](../cases.d/CASE-tmpshw39.md); code, tests and
outputs under scratch/studies/lead-144/, about twenty minutes of CPU). The
simulator has 24 members in six overlapping groups and three worlds:
coupling along the communication graph, a shared driver per group with no
interaction (the null, its gain tuned to match the within-group
correlation), and half of each. [CASE-165](../cases.d/CASE-165.md)'s finite beta-Bernoulli model
was fitted beside a graph-restricted autoregression, the two combined, the
graph with the true driver observed, and the graph fitted with shocks to
half the members, and every model was scored on held-out pulses and cuts.
By the lead's test the features fail: they are no better than the null
(more of them, better aligned, under the null), and with the graph they
predict interventions no better than the graph alone, which is itself
wrong under the driver ([CLAIM-tmpp56wv](../claims.d/CLAIM-tmpp56wv.md)). Choices made where the lead
left them open: a linear-Gaussian simulator with scalar activity; the
allocation held fixed over 600 days; communication only, no authorization
layer; the null matched on within-group correlation; and two intervention
readings of the features (cause of holders, realized by holders) run as
alternatives, since the model itself fixes neither.

<!-- inactive-ok-block: CASE-166 — Proposed; cited for the design a nonlinear simulator would follow -->
What remains: a joint state-space fit with the features as persistent
latent drivers beside the graph (the arm most likely to defeat the claim);
a nonlinear simulator with team records and authorization, as [CASE-165](../cases.d/CASE-165.md)
§7–8 and [CASE-166](../cases.d/CASE-166.md) describe; and the dynamic parts of [CASE-165](../cases.d/CASE-165.md) (sticky
allocation, per-member activations, social and team terms). Status and
stage are the owner's.
