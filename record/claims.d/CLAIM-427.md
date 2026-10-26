---
number: 427
status: Proposed
formerly:
- CLAIM-tmpcp1lb
title: 'Evidence for the organizational-perspective framework comes in three grades: that different organizations produce the same ordinary behaviour, that they respond differently to independently specified interventions, and that a model representing the coupling of significance, authority and reproduction predicts those responses better than the strongest existing alternatives at matched complexity; only the third bears on the framework''s defeater, and no grade counts if success is defined in the framework''s own terms'
version: 2
history:
- version: 2
  date: '2026-10-26'
  note: >-
    A dated note added: the lab's later versions meet the first two
    grades within synthetic constructions and not the third, and a
    comparator pilot (dmarx/PerspectiveLab@dce302b) shows why fit alone
    cannot. Extended the same day with the lab's v2.3 matched comparator
    (dmarx/PerspectiveLab@e9efcf4), which equalizes data and parameter
    count and still does not reach the third grade, and with v2.5's
    adequacy guard (dmarx/PerspectiveLab@f392084), whose same-kernel
    conventional control takes every action the guard takes. Extended
    again with v2.6's affective dissociation
    (dmarx/PerspectiveLab@74621fb), which meets the first two grades in a
    new domain within a supplied catalog, ties a same-kernel conventional
    predictor and misassigns an unmodelled hybrid in every test world.
    The claim is unchanged.
role: thesis
warrant: interpretive
defeated_if: >-
  A form of evidence that would rightly count for the framework against
  established accounts (habitus, adaptive networks, reflected appraisal,
  mixture-of-experts routing, organizational learning) without
  out-predicting them under intervention: for instance, if a unification
  that predicts nothing new is itself enough to prefer a theory; or a
  showing that the third grade cannot be met even in principle, because
  any model that represents the coupling is matched by an alternative of
  equal complexity.
tags:
- philosophy-of-science
- complex-systems
date: '2026-10-23'
line:
- distributed-agency
works:
- organization-of-perspective
rests_on:
- CLAIM-414
complements:
- CLAIM-417
- CLAIM-342
summary: >-
  From the exchange of 2026-10-23, "Framework Overview Request": the
  owner's U3, "what's the value add here? be it achieved or just
  intended", and U4, on experiments. A3: "Its strongest achieved
  contribution is conceptual disentanglement", and the test is "whether it
  changes what we can infer, distinguish, explain, or discover". A4 set
  the grades and the rule "not to use the framework itself to define
  experimental success". [CLAIM-414](CLAIM-414.md) already meets the first grade for two
  constructions. Nothing in the record meets the third.
---

# CLAIM-427: Evidence for the organizational-perspective framework comes in three grades: that different organizations produce the same ordinary behaviour, that they respond differently to independently specified interventions, and that a model representing the coupling of significance, authority and reproduction predicts those responses better than the strongest existing alternatives at matched complexity; only the third bears on the framework's defeater, and no grade counts if success is defined in the framework's own terms

## The claim

A4's table, which the claim adopts:

| Finding | What it establishes |
|---|---|
| "Different organizational mechanisms can produce identical ordinary behavior" | Non-identifiability from passive observation |
| "Those mechanisms predict different responses to independently specified interventions" | That the organizational distinctions matter |
| "The proposed framework predicts these differences better than established alternatives" | A distinctive theoretical contribution |

- **Where the record stands.** [CLAIM-414](CLAIM-414.md) (Active) meets the first grade for
  two constructions, and its intervention meets the second within them.
  No entry meets the third. A3: "the current work has earned the status of
  a potentially useful conceptual synthesis, not yet an independent
  explanatory framework."
- **Why only the third.** [CLAIM-417](CLAIM-417.md)'s defeater is that established
  accounts "explain the same transitions as well with fewer assumptions".
  Showing that organizations differ under intervention does not touch it,
  since the established accounts may predict the same differences. A4:
  "beating a deliberately weak baseline is not evidence for a unifying
  theory." The baselines that count are the mature theories already
  covering each phenomenon.
- **The measure.** A4 proposed one: the drop in predictive risk over a
  prespecified distribution of interventions when the coupling is
  represented, at comparable complexity and information budgets. The
  claim takes the form, not the formula.
- **No success in the framework's own terms.** A4: "Suppose a system is
  described as possessing a perspective because its processes are
  mutually influential, and the experiment then demonstrates that its
  processes are mutually influential. Nothing substantive has been
  learned." It is [CLAIM-342](CLAIM-342.md)'s rule for a self-confirming loop applied to
  the record's own programme: the test must be scored by evidence whose
  scoring does not pass through the framework.

## What it does not say

- **Not that the framework fails.** It says what would show it succeeds.
  A3's assessment, "Achieved", "Plausible", "Not yet shown", is the
  exchange's, and the claim does not adopt its verdicts.
- **Not that the conceptual work is worthless.** A3 counted "preventing
  invalid inferences" as real, if "primarily *negative* or
  *diagnostic*". The claim is about the further, positive contribution.
- **Not that simulation can settle it.** A5: "a simulation cannot
  independently validate the ontology it presupposes." A simulation can
  meet the third grade only for the class of systems it models.

## Note of 2026-10-26: where the lab stands on the grades

<!-- inactive-ok-file: CASE-164 CASE-161 CASE-163 — Proposed; the lab's runs filed 2026-10-26, cited as where the evidence stands, nothing here rests on them -->

The Perspective Population Lab's later versions meet the first two
grades within synthetic constructions and do not reach the third.
Matched ordinary behaviour with different responses to specified
interventions is [CASE-161](../cases.d/CASE-161.md) in a 32-member population and
[CASE-164](../cases.d/CASE-164.md) exactly. [CASE-163](../cases.d/CASE-163.md) predicts withheld interventions from
probes, but its forecaster is given the four candidate mechanisms and
their equations, and every probe runs on a counterfactual reset.

A comparator pilot (dmarx/PerspectiveLab@dce302b
experiments/comparator_pilot/) set rivals beside it under unequal
information. A generic state-space model with the same transition kernels
ties exactly, by construction. Boosted trees fitted only to the probe
trajectories fail (MSE about 0.2 against 0.002). A supervised model
trained on the candidates' target outcomes beats the structural
forecaster at nominal parameters (0.0013 against 0.0021). Its report says
it is "NOT CLAIM-427 grade-three evidence". The tie by construction puts
this claim's warning more sharply: renaming governing constraints as
latent state changes no prediction. So the third grade has to be won by
restriction, compression or transport, with the prior knowledge of
mechanisms priced, and not by fit. The claim is unchanged.

The lab's v2.3 (dmarx/PerspectiveLab@e9efcf4
experiments/matched_comparator/) removes the pilot's unequal
information. Every model is fitted on the same 208 source episodes of
96 uninterrupted updates, with the same intervention observations, and
the primary comparison holds the fitted coefficients at 8 each. Tested
on held-out production laws and a dependency graph absent from fitting,
the structural model wins in the familiar sigmoid regime and loses on
the bottleneck law with the mixed graph to a generic 20-coefficient
polynomial (MSE 0.004514 against 0.001865; paired seed-cluster
difference +0.0026, 95% interval [+0.0019, +0.0034]). A state-space
model with the same feature basis ties exactly. The structural model's
hand-chosen basis is not priced in description length, and every law
was written inside one experiment, so this is a better test of the
third grade that still does not meet it. Its report says so.

The lab's v2.5 (dmarx/PerspectiveLab@f392084
experiments/adequacy_guard/) adds a prequential check of model adequacy
that switches a misled adaptive design to a fixed probe schedule. On an
out-of-catalog bottleneck law it fires in all 16 test episodes and cuts
the cost-adjusted loss from 0.146 to 0.022, though the fixed schedule
alone does better (0.017). On an out-of-catalog cubic law it makes the
loss worse (0.018 to 0.022), and on valid mechanisms it false-alarms
above its nominal rate. A conventional Bayesian controller given the same
kernels, likelihood, detector and costs takes the same actions and makes
the same predictions in every episode. So what helps is ordinary
robust model checking, not anything specific to the organizational
description, and the third grade is still unmet.

<!-- inactive-ok-file: CLAIM-437 — Proposed; the claim the lab's v2.6 operationalizes, cited as open, nothing here rests on it -->

The lab's v2.6 (dmarx/PerspectiveLab@74621fb
experiments/affective_dissociation/) carries the grades into affect,
after [CLAIM-437](CLAIM-437.md) and [QUESTION-270](../questions.d/QUESTION-270.md). Five stipulated causes of pursuit after
an outcome is devalued share one pursuit probability, 0.668188, and are
separated by interventions written into the generator. That meets the
first two grades within a synthetic construction, the first only for the
one-step choice: over a longitudinal run two of the classes drift apart
from the other three. Four interventions are withheld as targets, three
of them combinations of the diagnostic arms and one a halved authority.
Predicted from the catalog's equations with the diagnostic probes and
readouts, they have a mean MSE across the catalog of 0.00230, against
0.03496 from passive choice alone. A ridge regression trained on the
source worlds' target outcomes reaches 0.00646. It is given different
information, and the structural predictor beats it with a bootstrap
interval excluding zero in three of the five classes. The study's
same-kernel conventional row ties exactly, but it is computed by the same
function as the structural row. The lab's tests check the equivalence
separately: a feature-table model of the same law gives the same
probabilities, to 14 places, in every class and arm. A hybrid of cue
drive and denied uptake, left out of the catalog, is assigned to a
catalog class in all 40 test worlds, 27 of them with a top posterior
above 0.9, and the adequacy check alarms in 9. The gain is a reward for
measuring the relevant variables inside a supplied catalog. It is not a
comparison at matched complexity and information, and the third grade is
still unmet.
