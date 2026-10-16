---
number: 285
status: Proposed
formerly:
- THEORY-tmpta57o
promote_when: >-
  Evidence from people, not from the model. Either of two kinds would
  support it. First, the authors' own prediction confirmed: after cued
  traumatic recall, people with PTSD attenuate peripheral evidence about
  context more than focal evidence, against matched trauma-exposed
  controls, with context-sampling measured directly (for example by eye
  movements toward disambiguating periphery). Second, an intervention
  contrast matched on exposure: restoring context sampling during the same
  exposure produces lasting change that the same exposure without it does
  not, while a precision-lowering drug reduces symptoms that return on
  withdrawal. The account is refuted if people with persistent PTSD sample
  disambiguating context as much as resilient controls and still keep the
  harmful-context belief. More simulations with other parameters cannot
  settle it, and nor can symptom improvement alone.
title: 'In an active-inference model of post-traumatic context inference, an overly precise prior that one is in a harmful context makes exploratory sampling look uninformative, so the agent attenuates the periphery, never receives the evidence that would correct the prior, and the belief sustains itself; lowering precision removes the symptoms without correcting the prior'
version: 1
tags:
- psychopathology-and-treatment
- neuroscience
- complex-systems
date: '2026-10-14'
source:
- LIT-983
summary: >-
  Linson, Anderson, Markham, Friston & Moutoussis (2025), [LIT-983](../literature.d/LIT-983.md), read
  in version 2 in [NOTE-766](../notes.d/NOTE-766.md). A mechanism shown in illustrative
  simulation: policy selection by expected information gain, plus a
  confident prior, withholds the only disambiguating observations, so the
  prior keeps itself up. Exposure that restores sampling rebalances it; a
  precision-lowering drug only suppresses symptoms. No data are fitted,
  parameters are unreported, and the two intervention arms differ in
  environment as well as mechanism.
answers:
- QUESTION-045
supports:
- CLAIM-tmpki5gp
---
<!-- inactive-ok-file: THEORY-058 — Proposed; the loop account this model gives a mechanism for -->

# THEORY-285: In an active-inference model of post-traumatic context inference, an overly precise prior that one is in a harmful context makes exploratory sampling look uninformative, so the agent attenuates the periphery, never receives the evidence that would correct the prior, and the belief sustains itself; lowering precision removes the symptoms without correcting the prior

## Source

Linson, Anderson, Markham, Friston & Moutoussis (2025), bioRxiv,
[LIT-983](../literature.d/LIT-983.md), version 2, read in [NOTE-766](../notes.d/NOTE-766.md): Overview, Results (Figs. 4–7),
Discussion and Online Methods.

## What was actually shown

**The model.** A partially observed Markov decision process with two
hidden contexts, harmful and harmless. They share an ambiguous first
observation and differ only in what the periphery shows. At each step the
agent either samples the periphery (exploratory) or attenuates it and
keeps to the foreground, which "generates the same observation
irrespective of context". Context priors are learned Dirichlet counts
with forgetting. Policies are chosen by expected free energy, so the
agent explores only when it expects exploring to resolve uncertainty.

**The loop (Figs. 6, 7a).** After a short run of harmful trials, a
"vulnerable" agent's harmful-context prior becomes precise enough that
exploration is "falsely believed to be uninformative due to overly
informative prior beliefs". It selects sensory attenuation, learns
nothing about the harmless context, and so keeps selecting attenuation:
"no amount of observations will render prior beliefs obsolete". A
"resilient" agent, given the same trials but different learning and
forgetting weights, keeps exploring and rebalances. By trials 50–60 the
vulnerable agent attenuates "under any condition".

**The interventions (Fig. 7b–f).** Sixty harmless-only trials restored
exploration near the end of the block, and the priors rebalanced and
stayed balanced. Lowering the precision of the A and B tensors under
random trials made policy selection less vigorous, read as fewer
symptoms. But the priors did not rebalance, and when precision was
restored the attenuation policy returned even on harmless trials.

What could have come out otherwise: exploration could have been chosen
anyway, if the information gain from the periphery outweighed a confident
prior; the drug arm could have let enough evidence through to rebalance.
Within the chosen parameters, neither happened.

## What this does not say

- **It does not show that PTSD works this way.** Nothing is fitted to
  patient data. The vulnerable and resilient phenotypes are defined by
  learning and forgetting weights that the main text does not report. The
  match to the EMDR–fluoxetine trial (van der Kolk et al. 2007) is
  asserted by citation.
- **It does not show the loop is inevitable.** Whether it forms depends on
  parameters. The paper shows one run per phenotype, not where in
  parameter space the tipping point lies.
- **It does not isolate the maintaining link.** The exposure arm is
  harmless-only and the drug arm is random, so the arms differ in
  environment as well as in what they act on. The comparison [QUESTION-045](../questions.d/QUESTION-045.md)
  asks for, the same exposure with and without restored sampling, is not
  run.
- **It does not test the circuit.** The acetylcholine–noradrenaline and
  serotonergic-brake account, and the flashback account, are narrative and
  do not drive the simulations.
- **It is about version 2.** The current version 3 (2026-05-13) was not
  read.

## Connections

- **[QUESTION-045](../questions.d/QUESTION-045.md)** asks whether a disorder that outlasts its trigger is a
  protective lock-in, kept up by behaviour that blocks its own
  disconfirmation while the capacity to leave it degrades. This account
  gives the structure in model form: attenuation is the blocking
  behaviour, and the collapse of two basins to one is the lost capacity
  to leave. It answers the "is it" half only for a model. The "what would
  show it" half is answered by the paper's predictions (peripheral against
  focal attenuation after cued recall), not by its results.
- **[THEORY-058](THEORY-058.md)** holds that disorders are kept up by self-reinforcing loops
  and outlast their triggers. This is a mechanism for one such loop, with
  the loop running through what the agent chooses to observe.
- **[THEORY-053](THEORY-053.md)** says only change in the theorised process, ahead of the
  outcome, bears on a theory of change. The drug arm is a modelled
  instance of outcome without process, and it relapses.
