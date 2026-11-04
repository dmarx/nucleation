---
status: Proposed
promote_when: >-
  A preregistered replication, using a test block identical across
  conditions and objects not seen in training, finds that training evidence
  suggesting conjunctive versus disjunctive form reliably changes judgments
  about which new objects are causes. The direction must be the one the
  hierarchical account predicts, and the effect must be larger when the
  test belongs to the same kind of causal system as the training.
title: 'Lucas and Griffiths propose that people learn the functional form of causal relationships, such as whether causes act disjunctively or conjunctively and how reliably, as abstract theories in a hierarchical Bayesian model, and transfer them to new objects of the same kind, so that evidence about one set of objects changes their causal judgments about a different set'
version: 1
history:
- version: 1
  date: '2026-11-04'
  note: >-
    Filed Proposed from NOTE-tmp8uiyl, the reading of Lucas & Griffiths
    (2010) registered from the owner's pasted synthesis of 2026-11-04. The
    wording is the reader's; adopting it is the owner's call.
tags:
- causality
- cognition
- probabilistic-modeling
date: '2026-11-04'
source:
- LIT-tmpzamp4
summary: >-
  Lucas & Griffiths (2010), [LIT-tmpzamp4](../literature.d/LIT-tmpzamp4.md), read in full in [NOTE-tmp8uiyl](../notes.d/NOTE-tmp8uiyl.md).
  Five blicket-meter experiments: training that suggests a conjunctive,
  noisy-disjunctive or deterministic form changes judgments of new objects
  in an identical test block, and more within a domain than across; a
  two-parameter sigmoid model fits the mean ratings (r = 0.98–0.99).
  Proposed: small samples, in-sample fits against rivals that cannot vary
  between conditions, one reversed prediction, one marginal effect, and no
  preregistered replication read. The wording is the reader's; adopting it
  is the owner's call.
---

# THEORY-tmp1n0rh: Lucas and Griffiths propose that people learn the functional form of causal relationships, such as whether causes act disjunctively or conjunctively and how reliably, as abstract theories in a hierarchical Bayesian model, and transfer them to new objects of the same kind, so that evidence about one set of objects changes their causal judgments about a different set

## Source

Lucas & Griffiths (2010), *Cognitive Science* 34(1): 113–147,
[LIT-tmpzamp4](../literature.d/LIT-tmpzamp4.md); read in full in [NOTE-tmp8uiyl](../notes.d/NOTE-tmp8uiyl.md).

## What was actually shown

- **Transfer to new objects.** In Experiments 1–4 (live blicket-meter
  demonstrations, Berkeley undergraduates, N = 41–102), a training block
  suggesting a conjunctive, noisy-disjunctive or deterministic-disjunctive
  form changed ratings of new objects in a test block identical across
  conditions. The hierarchical model predicts this "because the events in d
  (1) do not involve any of the prospective causes in d (2)" (§5).
- **Fits.** A two-parameter sigmoid theory space with two hyperparameters
  fit across all experiments: MSE 0.29–0.55, r = 0.98–0.99, against MSE
  5.83 for ΔP and causal power and 3.97 for the best training-blind
  predictions in Experiment 1, and 0.63 for the training-blind
  predictions in Experiment 2.
- **Reliability matters.** Stated or shown noise (Experiment 3) and
  failure rates (Experiment 4) shifted judgments as predicted; the
  aggregated Experiment 3 effect is marginal (p = 0.049).
- **Kind matters.** Transfer was larger within a domain than across
  (Experiment 5, survey, N = 60; F[1,56] = 12.8).
- **Against the account.** One predicted contrast reversed (Experiment 2);
  the fits need a prior that favours disjunctive forms (§11.1).

## What this does not say

- That the sigmoid family is how people represent form: the authors say
  their model was not "a general purpose model that could explain all
  instances of learning of functional form" (§5).
- That the fits are predictions: the hyperparameters were tuned on the
  ratings scored, with no held-out test.
- That a generic Bayesian learner would do as well or worse in general:
  the rivals are mostly fixed-form models that cannot vary between
  conditions, and one generic prior in the same hierarchy.
- Anything about individuals beyond the match of simulated to observed
  rating distributions (§11.2), or about populations beyond Berkeley
  undergraduates.
