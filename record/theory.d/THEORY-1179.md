---
number: 1179
status: Proposed
formerly:
- THEORY-tmpdw1un
title: 'In an active-inference model of post-traumatic context inference, an overly precise prior that one is in a harmful context makes exploratory sampling look uninformative, so the agent attenuates the periphery, never receives the evidence that would correct the prior, and the belief sustains itself; lowering precision removes the symptoms without correcting the prior'
version: 1
tags:
- psychopathology-and-treatment
- neuroscience
- complex-systems
date: '2026-10-30'
source:
- LIT-983
extends:
- THEORY-285
bears_on:
- QUESTION-303
promote_when: >-
  Evidence from people, not from the model. Either of two kinds would
  support it. First, the authors' own prediction confirmed: after cued
  traumatic recall, people with PTSD attenuate peripheral evidence about
  context more than focal evidence, against matched trauma-exposed controls,
  with context-sampling measured directly (for example by eye movements
  toward disambiguating periphery). Second, an intervention contrast matched
  on exposure: restoring context sampling during the same exposure produces
  lasting change that the same exposure without it does not, while a
  precision-lowering drug reduces symptoms that return on withdrawal. The
  account is refuted if people with persistent PTSD sample disambiguating
  context as much as resilient controls and still keep the harmful-context
  belief. More simulations with other parameters cannot settle it, and nor
  can symptom improvement alone.
summary: >-
  The wide form [THEORY-285](THEORY-285.md) held before the eighth status review narrowed
  it, kept as a Proposed reading by the [ADR-047](../decisions.d/ADR-047.md) kind-1 sweep of
  2026-10-30: the source asserts it, and [THEORY-285](THEORY-285.md), Active, is its
  evidence. Linson et al. (2025), [LIT-983](../literature.d/LIT-983.md), recast post-traumatic stress
  as lost context disambiguation and offer the loop as its mechanism;
  their simulations show it once per phenotype, with unreported
  parameters, and fit no patient data.
---
<!-- inactive-ok-file: ADR-047 — Superseded by ADR-057, which keeps its evidence rulings; cited for the kind-1 rule this entry is filed under -->

# THEORY-1179: In an active-inference model of post-traumatic context inference, an overly precise prior that one is in a harmful context makes exploratory sampling look uninformative, so the agent attenuates the periphery, never receives the evidence that would correct the prior, and the belief sustains itself; lowering precision removes the symptoms without correcting the prior

## Source

Linson, Anderson, Markham, Friston & Moutoussis (2025), bioRxiv, [LIT-983](../literature.d/LIT-983.md),
version 2, read in [NOTE-766](../notes.d/NOTE-766.md) (Results, Discussion and Online Methods; not
the figures or the supplement). What the simulations showed is
[THEORY-285](THEORY-285.md), which this entry extends.

## The claim

The paper recasts post-traumatic stress disorder as a failure to tell which
context one is in, not a failure of fear extinction. Under active
inference an agent chooses policies by expected information gain, so a
prior already confident that the context is harmful makes looking at the
periphery seem pointless: exploration is "falsely believed to be
uninformative due to overly informative prior beliefs". The agent
attenuates the periphery, learns nothing about the harmless context, and
keeps the prior: "As long as the sensory attenuation policy is selected,
no amount of observations will render prior beliefs obsolete." The
collapse to one basin is "self-maintaining because it precludes epistemic
foraging". Exposure that restores sampling rebalances the prior, while a
precision-lowering drug suppresses symptoms that return when precision
does, a contrast the authors say "closely matches" the EMDR–fluoxetine
trial. They state predictions for people: after cued traumatic recall,
peripheral sensing is attenuated more than focal sensing.

What [THEORY-285](THEORY-285.md) holds is narrower: one illustrative run per phenotype,
under learning and forgetting weights the paper does not report, and a
drug arm that makes the attenuation policy less vigorous rather than
removing it. The match to the trial is asserted by citation, not fitted.

## What would settle it

The promote_when, which [QUESTION-303](../questions.d/QUESTION-303.md) also asks: the authors' prediction
confirmed in people with context sampling measured directly, or an
exposure-matched contrast in which restoring sampling produces lasting
change and a precision-lowering drug does not. More simulations cannot
settle it.
