---
number: 61
status: Proposed
formerly:
- THEORY-tmp2002z
promote_when: >-
  Selective influence shown in individuals and beyond the three
  manipulations that have it. Ratcliff and McKoon's experiments
  (LIT-576) show that difficulty moves drift alone, speed or
  accuracy instructions boundary separation alone, and stimulus
  proportions mainly the starting point, but on group-averaged fits. The
  account would be promoted by the same mapping in hierarchical fits to
  individuals (as LIT-563 makes possible), extended to goals that are
  not instructions: payoffs, effort costs, urgency set by a deadline. For
  the when-to-act half, it would be promoted by showing that manipulating
  urgency in a Schurger-type task shifts the baseline of premovement
  activity and the waiting-time distribution together, as one fitted
  parameter predicts. It is refuted if a manipulation of goals, with the
  options held fixed, changes choices or response times in a way no
  setting of drift, starting point, threshold and non-decision time
  reproduces; or if instructions about speed reliably change drift as
  much as threshold, so that the parameters do not separate goal from
  evidence. What cannot settle it: a good fit of the full model with all
  parameters free in every condition, since a flexible model absorbs
  anything; the test is which parameter moves.
title: 'In evidence-accumulation tasks, goals and instructions act on a decision by setting the parameters of the accumulation (drift, starting point or baseline, and threshold), not by specifying the response, and this holds for when to act as well as for which'
version: 1
tags:
- behavioral-integration
- agency
- cognition
- psychometrics
date: '2026-10-03'
source:
- LIT-569
- LIT-576
- LIT-605
summary: >-
  Bogacz et al. ([LIT-569](../literature.d/LIT-569.md)) define cognitive control, in a two-choice
  task, as the adjustment of drift, starting point and threshold to
  maximise a utility. Ratcliff and McKoon ([LIT-576](../literature.d/LIT-576.md)) find that the
  manipulations behave that way: speed or accuracy instructions are fitted
  by boundary separation alone, stimulus proportions mainly by starting
  point, difficulty by drift alone. Schurger et al. ([LIT-605](../literature.d/LIT-605.md)) carry
  the picture to the decision of when to move: the task goal raises the
  baseline toward threshold and leaves the moment to fluctuation. The
  convergence is real; the evidence is group fits on a few paradigms, so
  Proposed. It does not say who sets the parameters, or how.
---
<!-- inactive-ok-file: LIT-600 LIT-604 — Deferred, unread; Norman & Shallice and Carver & Scheier named as the older traditions, not leaned on -->
<!-- inactive-ok-file: THEORY-059 THEORY-070 — Proposed; companion accounts in this batch, named for what each adds -->

# THEORY-061: In evidence-accumulation tasks, goals and instructions act on a decision by setting the parameters of the accumulation (drift, starting point or baseline, and threshold), not by specifying the response, and this holds for when to act as well as for which

## Source

- Bogacz et al. (2006), [LIT-569](../literature.d/LIT-569.md), read in [NOTE-461](../notes.d/NOTE-461.md): optimal
  thresholds and starting points (Figs. 12–16), and the closing section
  "Optimization and Cognitive Control".
- Ratcliff & McKoon (2008), [LIT-576](../literature.d/LIT-576.md), read in [NOTE-445](../notes.d/NOTE-445.md):
  Experiments 1–3 and §8 on individual differences.
- Schurger, Sitt & Dehaene (2012), [LIT-605](../literature.d/LIT-605.md), read in [NOTE-462](../notes.d/NOTE-462.md): the
  model's urgency term and the Discussion.

## What was actually shown

**The proposal, stated by Bogacz et al.** The closing section of
[LIT-569](../literature.d/LIT-569.md) says: "Within the framework of the DDM, we can think of control
as the adjustment of these parameters to optimize performance", drift for
attention, starting point for expectancy, threshold for the speed–accuracy
trade-off. The paper makes this precise where it can. For reward rate the
optimal threshold is unique and depends on the delays only through their
sum. With unequal priors the optimal starting point is proportional to the
log prior odds, and the data of Laming, Link and Van Zandt lie closer to
that rule than to the alternative (significantly so for one data set). In
their own dot-motion experiment, one reported participant's fitted
threshold rose from 0.16 to 0.26 as the delay between trials grew.

**Selective influence, from Ratcliff and McKoon.** In [LIT-576](../literature.d/LIT-576.md)'s three
experiments (14 to 17 participants each), a change of goal moved one
parameter and the stimulus moved another:

- speed versus accuracy instructions changed median RT by 120–200 ms and
  were fitted by boundary separation alone (0.109 against 0.152), and a
  separate non-decision time for the two instructions differed by 6 ms;
- a 75:25 stimulus proportion moved the starting point about a third of the
  way toward the likelier boundary, and letting the drift criterion vary as
  well improved the fit by 1%;
- coherence, which is the evidence and not a goal, was fitted by drift
  alone.

This is what could have come out otherwise. If instructions moved drift,
the parameters would not separate what the person wants from what the
stimulus gives. They did not.

**When to act.** Schurger et al. ([LIT-605](../literature.d/LIT-605.md)) model Libet's task, where
the instruction is to move at no particular time, with a constant urgency
input to a leaky accumulator. Because of the leak, urgency does not ramp
the trace to threshold. It "simply moves the baseline level of activity
closer to the threshold so that a crossing is very likely to happen soon".
They say of the goal: it "is effected by setting up circumstances (moving
baseline premotor activation up closer to threshold) that favor the
spontaneous initiation of a movement … However, the precise moment is not
directly decided by a goal-directed operation". The fitted model reproduces
waiting times and the readiness potential ([THEORY-059](THEORY-059.md)).

**The synthesis is the record's.** Each source states its own part. None
states the general claim that goals act through parameters for both which
and when.

## What this does not say

- **Not who sets the parameters, or how.** Ratcliff and McKoon say the
  model is silent on how criteria are set, and object that Bogacz et al.'s
  learning account cannot explain calibration from a verbal instruction in
  one trial (§7.1). The account is about where goals act, not about the
  process that puts them there. [THEORY-070](THEORY-070.md) is one proposal for that
  process.
- **Not that every goal is a parameter.** It is scoped to tasks the
  accumulation models fit: fast decisions among a fixed set of options.
  Choosing what the options are, or forming a plan, is outside it.
- **Not optimality.** That a parameter is what moves does not mean it moves
  to the optimum. Bogacz et al. predict that learners will set thresholds
  too high, and offer this as the explanation of people's apparent bias
  toward accuracy.

## Connections

- **The unity it is about.** `behavioral-integration`: the interface
  between a goal and the decision machinery. It says nothing about
  self-governance; a goal here is whatever sets a parameter, endorsed or
  not ([ADR-024](../decisions.d/ADR-024.md)).
- **[THEORY-068](THEORY-068.md)** says what comparison the parameters are parameters
  of, and when it is lossless.
- **[THEORY-070](THEORY-070.md).** The EVC account's control signals have an identity
  and an intensity, and its list of identities includes thresholds and
  attention. So it is compatible with this one and adds a decider. The two
  are not rivals.
- **The supervisory-attention and control-theory traditions.** Norman and
  Shallice's account of willed control ([LIT-600](../literature.d/LIT-600.md)) and Carver and
  Scheier's feedback-control framework ([LIT-604](../literature.d/LIT-604.md)) are in the record
  unread. As they are usually described, the supervisory system acts by
  biasing the activation of competing schemas, which would be this
  account's picture. That is not checked, and nothing here rests on it.
