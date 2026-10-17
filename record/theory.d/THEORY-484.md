---
number: 484
status: Proposed
formerly:
- THEORY-tmpal7n3
promote_when: >-
  Recordings in a task with explicit subtasks that find phasic dopamine at
  subtask boundaries scaling with option-level prediction error, a signal
  at subgoal attainment that behaves as pseudo-reward (present for
  subgoals that carry no external reward), and prefrontal activity coding
  discrete subtask segments, with each signal dissociable from external
  reward. It is refuted if dopamine at boundaries tracks only external
  reward, or if no signal at subgoals separates from reward expectation.
  More correlational findings of task-set coding in DLPFC or
  context-dependent action coding in the striatum cannot settle it: they
  were the basis of the proposal.
title: "The brain implements hierarchical reinforcement learning with options: dorsolateral prefrontal cortex represents which option is active, dorsolateral striatum holds option-specific policies, orbitofrontal cortex holds option-specific values, and dopamine carries option-level prediction errors at subtask boundaries"
version: 1
tags:
- behavioral-integration
- neuroscience
- learning-and-conditioning
date: '2026-10-16'
source:
- LIT-581
presupposes:
- THEORY-688
summary: >-
  Botvinick, Niv and Barto (2009), [LIT-581](../literature.d/LIT-581.md), read in [NOTE-451](../notes.d/NOTE-451.md). Four
  proposed extensions of the actor-critic mapping, each matched to existing
  correlational findings, and predictions the authors say "call for
  further experimental scrutiny". The evidence for prefrontal coding of
  subtask segments is "only indirect". The mapping assumes pseudo-reward;
  other frameworks (HAM, MAXQ) would predict differently.
---
<!-- inactive-ok-file: THEORY-056 THEORY-062 — Proposed; named in Connections, not leaned on -->

# THEORY-484: The brain implements hierarchical reinforcement learning with options: dorsolateral prefrontal cortex represents which option is active, dorsolateral striatum holds option-specific policies, orbitofrontal cortex holds option-specific values, and dopamine carries option-level prediction errors at subtask boundaries

## Source

Botvinick, Niv and Barto (2009), [LIT-581](../literature.d/LIT-581.md) (*Cognition* 113(3): 262–280),
read in full in [NOTE-451](../notes.d/NOTE-451.md), "Neuroscientific Implications" and Discussion.

## What was actually shown

**The starting point.** The actor-critic model is already mapped onto the
brain: the critic's prediction error to phasic dopamine, the actor to the
striatum. The paper asks what the options framework would add (Fig. 2C–D).

**Four extensions, each with a candidate substrate.**

1. **Option identity** to dorsolateral prefrontal cortex, which represents
   task sets; pre-SMA, SMA and premotor cortex are candidates too.
2. **Option-specific policies** to dorsolateral striatum, which receives
   frontal input and shows context-dependent action coding, as in
   grooming-sequence neurons.
3. **Option-specific values** to orbitofrontal cortex, whose value
   representations shift with strategy.
4. **Prediction errors over whole options** to orbitofrontal sustained
   reward-predictive activity and to semi-Markov accounts of dopamine.

**Predictions.** Phasic dopamine at subtask boundaries scaling with
option-level prediction errors; a possible neural correlate of
pseudo-reward; prefrontal coding of discrete subtask segments.

**What could have come out otherwise.** Nothing here was tested. The
mappings are fits to prior findings, so they could not have failed in this
paper.

## What this does not say

- **That the mapping is shown.** The correspondences are drawn from
  correlational findings and are proposals (C3, weak to moderate).
- **That there is a neural pseudo-reward.** That is an open question and
  depends on the HRL framework assumed. HAM does without pseudo-reward, and
  MAXQ decomposes value differently.
- **That planning over options is covered.** The model is model-free;
  option models are discussed, not implemented.
- **That behaviour is strictly hierarchical.** The paper itself says
  everyday behaviour is only quasi-hierarchical (C6).

## Connections

- It presupposes the computational result [THEORY-688](THEORY-688.md), that options
  help only when they fit, as the reason a brain would need them and the
  source of the option-discovery problem.
- [THEORY-062](THEORY-062.md) (model-based and model-free control by relative reliability)
  is the division the paper adopts, with HRL placed in the model-free
  system.
- [NOTE-451](../notes.d/NOTE-451.md) observes that HRL is control without a distinct regulator: the
  controller at each level is a policy over options, learned by the same
  prediction-error rule as the level below. That is the shape [THEORY-056](THEORY-056.md)
  claims for emotion regulation, and it bears on [QUESTION-054](../questions.d/QUESTION-054.md)'s governing
  level. The paper does not draw either parallel.
