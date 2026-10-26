---
number: 270
status: Open
formerly:
- QUESTION-tmponjie
title: 'When can an organization hold an evaluation that is accurate, a consummatory process registering that an outcome no longer pleases or a process whose belief keeps predicting well, and still deny it the authority to revise pursuit or the collective judgement, and how is that told apart from the evaluation''s not being recognized at all?'
version: 3
history:
- version: 2
  date: '2026-10-25'
  note: >-
    A dated note added: four rival mechanisms and their separating
    interventions, from A31. The question is unchanged.
- version: 3
  date: '2026-10-26'
  note: >-
    A dated note added: the lab's v2.6 (dmarx/PerspectiveLab@74621fb)
    separates a registered evaluation denied authority from one never
    registered, by intervention, in a stipulated synthetic model. It meets
    the question's test for the hedonic instance only within that model,
    and no Active entry answers the question. The question is unchanged.
tags:
- self-governance
- emotion-and-affect
- epistemology
date: '2026-10-24'
line: will-organization
summary: >-
  From the exchange of 2026-10-24 (workbench entry of 2026-10-24,
  U23–U25). The owner asked "where does hedonic drive fit into our model?"
  and then "we have an operational characterization of feeling, wanting,
  liking... how about belief?" Both answers ended on the same question:
  an evaluation that is right, registered, and not consequential. It joins
  [CLAIM-437](../claims.d/CLAIM-437.md)'s wanting and liking, [CLAIM-403](../claims.d/CLAIM-403.md)'s ladder from access to uptake,
  and [CASE-124](../cases.d/CASE-124.md)'s legibility.
---
<!-- inactive-ok-file: CLAIM-403 — Proposed; cited in the note of 2026-10-25, nothing here rests on their being settled -->

# QUESTION-270: When can an organization hold an evaluation that is accurate, a consummatory process registering that an outcome no longer pleases or a process whose belief keeps predicting well, and still deny it the authority to revise pursuit or the collective judgement, and how is that told apart from the evaluation's not being recognized at all?

## The question

Two instances from one exchange.

**Hedonic.** A pursuit process keeps selecting a reward and reaching it,
while the consummatory evaluation of the reward declines. In an adaptive
organization that evaluation can inform pursuit and, where apt, change the
authority of the processes responsible. In a captured one the pursuit
process keeps its authority despite evidence that the outcome no longer
rewards. [CLAIM-437](../claims.d/CLAIM-437.md)'s wanting and liking then differ not only as two
evaluations but in their capacity to govern. Incentive sensitization
already explains persistent wanting by a change in the incentive mechanism
([THEORY-895](../theory.d/THEORY-895.md)). The question is whether divergence can also be maintained by
asymmetries of evidential access and governance, which would be the
record's addition and is not established by the sensitization literature.

**Epistemic.** A process can hold a belief ([TERM-079](../terms.d/TERM-079.md)) that keeps
predicting and inferring accurately while the organization denies it
enough authority to change collective judgements or actions: a specialist
right and unheeded.

## Why the record needs it

It is the point where the will line, the affect line and the legibility
line meet. [CLAIM-403](../claims.d/CLAIM-403.md) separates access, recognition, credibility, uptake and
participation in revising standards. The cases here sit past recognition
and short of uptake, and an account that cannot tell them from failures of
recognition will read every unheeded evaluation as an unregistered one.

## What would answer it

A model or study with the evaluation measured independently of choice
(hedonic reactivity or experienced-utility reports; independently scored
forecasts), the organization's registration of it measured separately
(its self-model, its record, its reports), and an intervention on the
authority of the evaluating process with the evaluation and its
registration held fixed. The hedonic version: an outcome that becomes
progressively less pleasant, or a dangerous activity that becomes safely
enjoyable, with wanting, liking and governance responsiveness recorded
separately, compared across an ordinary adaptive learner, a learner with
persistent pursuit salience, and one whose pursuit authority also shapes
the evidentiary regime.

## Related

- The hedonic quantities as the exchange separated them ([CLAIM-437](../claims.d/CLAIM-437.md)'s note
  of 2026-10-24): hedonic impact, anticipated pleasure, incentive wanting,
  hedonic authority.
- Relief after avoidance is reduced distress, not positive pleasure and not
  evidence of danger ([CLAIM-446](../claims.d/CLAIM-446.md)); safe engagement's pleasure is often
  counterfactual and unsampled.

## Note of 2026-10-25: four rivals for failed uptake

A31 of the exchange of 2026-10-24, continued, proposed this question's
probe as its Experiment 6, without citing it, with four mechanisms and the
intervention that tells each apart:

- incorrect hedonic prediction, separated by reliable outcome evidence;
- cue-triggered incentive salience, separated by reducing cue-driven drive;
- habitual control, separated by changed contingencies and retraining;
- governance-mediated suppression, separated by restoring the evaluation's
  access to decision.

A31: "A sophisticated habit or incentive-learning model may explain much of
the result without any extra governance state." It also adds an avowal
equivalent to "I no longer enjoy this", made available to the other
processes, to test whether an accurate report is enough to revise pursuit.
That is [CLAIM-403](../claims.d/CLAIM-403.md)'s step from recognition to uptake, inside one agent. Not
run. The question is unchanged.

## Note of 2026-10-26: a synthetic separation of denied uptake from nonregistration

<!-- inactive-ok-file: CLAIM-437 CLAIM-427 — Proposed; the claims the lab's v2.6 bears on, cited as open, nothing here rests on their being settled -->

The lab's v2.6 (dmarx/PerspectiveLab@74621fb
experiments/affective_dissociation/) runs the note of 2026-10-25's four
rivals, with a fifth class in which the negative evaluation is never
registered. Liking is an exogenous outcome value, −1 in every class after
devaluation, read by an assay that does not use action. Anticipated
pleasure and registration have readouts of their own, registration's
right nine times in ten. Pursuit is a Bernoulli choice whose logit adds
anticipated pleasure, cue drive, habit and another pursuit motive, and
subtracts 1.2 × negative liking × registration × authority. The
parameters are set by hand so that all five classes pursue with the same
one-step probability after devaluation, 0.668188, the logistic of 0.7.

- In the denied-uptake class the negative evaluation is registered and
  its authority is 0. In the unregistered class it is not registered and
  its authority is 1.
- Restoring authority to 1, with anticipated pleasure, liking and
  registration unchanged, lowers pursuit in the denied-uptake class to
  0.378 and leaves the unregistered class at 0.668. Restoring
  registration does the reverse. Each of the other three classes falls
  to 0.154 under its own intervention and under no other.
- Restoring authority moves no other class only because every other
  class already has authority 1. Halving authority, one of the held-out
  targets, raises pursuit from 0.668 to 0.786 in the three classes whose
  evaluation is registered with full authority, and lowers the
  denied-uptake class's to 0.525. Only the unregistered class is
  untouched. An intervention on authority moves pursuit wherever a
  registered evaluation enters action, not only where authority is
  blocked.
- With the probes and readouts, a Bayesian classifier over the five
  classes names 195 of 200 held-out worlds correctly. A hybrid of cue
  drive and denied uptake, left out of the catalog, is assigned to a
  catalog class in all 40 of its test worlds, 30 of them to denied
  uptake, with a mean top posterior of 0.868. The adequacy check alarms
  in 9 of the 40. A mixture is the case this question most needs told
  apart, and the construction does not tell it.
- In a longitudinal run of 60 seeds, with no resets and liking stepping
  from +1 to −1, the denied-uptake, unregistered and cue classes follow
  the same pursuit course, to within 10⁻⁹, for all 36 steps after
  devaluation. Passive history does not tell denied uptake from
  nonregistration here. Only the intervention does.

Within a specified synthetic class, then, the construction meets the
first test under "What would answer it" for the hedonic instance. The
evaluation is measured apart from choice, its registration apart from
both, and an intervention on authority holds them fixed. But the classes,
and what registration and authority mean, are written into the generator,
and the lab's test of the separation checks what the generator says.
Liking drops in one step, not progressively. No learner's pursuit
authority shapes the evidence it gets. The epistemic instance is not
touched. The lab bridges this question to [CLAIM-437](../claims.d/CLAIM-437.md), whose processes the
model does not represent (that claim's note of 2026-10-26), and its
same-kernel tie is [CLAIM-427](../claims.d/CLAIM-427.md)'s point (its note of 2026-10-26). No Active
claim or reading answers the question ([ADR-049](../decisions.d/ADR-049.md)), and nothing is split
from it. The question is unchanged.
