---
status: Proposed
promote_when: >-
  An out-of-sample test of active causal learning across related tasks
  finds three things. First, a model that values information about the
  functional form as well as about structure predicts intervention choices
  better than a structure-only information-gain model. Second, a model
  that carries the learned form beliefs into the next task predicts them
  better than one that resets its prior, both at the group level and for
  most individuals. Third, the fitted weight on form information exceeds
  the weight on structure information when the two disagree.
title: 'Jiang and Lucas propose that, when people choose interventions across a series of related causal-learning tasks, they seek information about overhypotheses about how causes combine as well as about which objects are causes in the task at hand, carry the overhypotheses they learn into later tasks, and accept less information about the immediate causal structure in exchange'
version: 1
history:
- version: 1
  date: '2026-11-04'
  note: >-
    Filed Proposed from NOTE-tmpm6c07, the reading of Jiang & Lucas (2024)
    registered from the owner's pasted synthesis of 2026-11-04. The
    wording is the reader's; adopting it is the owner's call.
tags:
- causality
- cognition
- probabilistic-modeling
date: '2026-11-04'
source:
- LIT-tmpjrcmk
summary: >-
  Jiang & Lucas (2024), [LIT-tmpjrcmk](../literature.d/LIT-tmpjrcmk.md), read in [NOTE-tmpm6c07](../notes.d/NOTE-tmpm6c07.md) (appendices
  not read). Two preregistered online blicket experiments. Learners that
  ignore form information or hold one fixed form barely beat random at
  predicting interventions; the model that does not transfer edges the
  full model on average (.059 against .055), while per participant the
  full model is best for the largest group, whose fitted weights mostly
  favour form information. Proposed: the transfer clause is the weakest,
  failing at the group level. The wording is the reader's; adopting it is
  the owner's call.
---

# THEORY-tmpbgkfv: Jiang and Lucas propose that, when people choose interventions across a series of related causal-learning tasks, they seek information about overhypotheses about how causes combine as well as about which objects are causes in the task at hand, carry the overhypotheses they learn into later tasks, and accept less information about the immediate causal structure in exchange

## Source

Jiang & Lucas (2024), *Computational Brain & Behavior* 7(1): 80–105,
arXiv:2206.09777, [LIT-tmpjrcmk](../literature.d/LIT-tmpjrcmk.md); read in [NOTE-tmpm6c07](../notes.d/NOTE-tmpm6c07.md).

## What was actually shown

- **Seeking form information, with rich forms.** In Experiment 2 (MTurk,
  N = 250, conjunctive transfer task, 20 interventions each), Fixed-Form
  and Structure-Only-EIG predicted interventions at .018, barely above
  random at .016, against .055–.059 for the models that value form
  information over a rich space of forms.
- **Transfer, mixed.** "The No-Transfer ablation model had the highest
  mean predictive likelihood"; per participant, "our full model was the
  best predictor for the highest number of participants". In Experiment 1
  (N = 212), training form changed the first transfer intervention (more
  blocks after conjunctive training, p < .001), but accuracy match effects
  were trends in the full data and null on the conjunctive transfer task.
- **Giving up structure information.** Among participants best fit by
  the full model, "81.63% of fits have overhypothesis weight > 0.5", 45.41%
  at w = 1.

## What this does not say

- That transfer beats no transfer for the population: at the group level
  it does not.
- That w measures a trade-off on a fixed scale: the two gains are min-max
  normalized before weighting, and the combination only approximates
  joint information gain; the unnormalized replication (Appendix A) was
  not read.
- That people choose Bayes-optimal interventions in general: the authors
  "do not argue that people choose Bayes-optimal interventions in general
  and for arbitrarily complex problems".
- Anything beyond monotone generative causes, one conjunctive target form
  in Experiment 2, and MTurk samples.
