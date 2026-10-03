---
number: 70
status: Proposed
formerly:
- THEORY-tmpkujus
promote_when: >-
  A fitted model and a dissociation. The paper states the model and
  matches it case by case to published findings; it is neither fitted
  nor simulated. It would be promoted by (1) a fit of the EVC
  computation to behaviour in which control intensity, measured by an
  accumulator parameter or by conflict adaptation, rises with the payoff
  for control at fixed difficulty and falls with its cost, better than a
  model without the cost term; and (2) a dissociation between specifying
  and implementing: damage or disruption of dACC that removes the
  adjustment of control to incentive and conflict while the implemented
  control, once cued from outside, stays intact, with the converse for
  lateral prefrontal cortex. The cingulotomy result (loss of conflict
  adaptation) is one half of one such dissociation. It is refuted if the
  allocation of control is fully predicted by the reliability of the
  competing estimates or by the strength of the competing tendencies,
  with no cost-benefit term; or if specification and regulation cannot
  be separated by any method, so that the dedicated system is a
  relabelling of the regulators. What cannot settle it: more reports
  that dACC responds to conflict, errors, pain or reward, which every
  account of dACC accommodates.
title: 'How much cognitive control to exert, and on what, is decided by a cost-benefit computation (the expected value of control) in a specification system distinct from the structures that implement the control'
version: 1
tags:
- behavioral-integration
- neuroscience
- cognition
- motivation
date: '2026-10-03'
source:
- LIT-585
summary: >-
  Shenhav, Botvinick & Cohen ([LIT-585](../literature.d/LIT-585.md)) unify dACC's many reported
  functions as one: deciding whether, where and how much control to
  allocate. A control signal has an identity (a task set, a threshold, an
  attention template) and an intensity; its expected value is its
  probability-weighted payoff, with future value discounted, minus an
  intrinsic cost rising with intensity. dACC monitors and specifies;
  lateral prefrontal and subcortical structures implement. The paper
  reviews evidence and fits nothing, so Proposed. It does not say what
  the cost is, how EVC is computed, or that it governs emotion
  regulation.
---
<!-- inactive-ok-file: THEORY-056 THEORY-029 — Proposed; THEORY-056 is the account this one is weighed against, THEORY-029 is named to say this one does not bear on it -->
<!-- inactive-ok-file: LIT-600 — Deferred, unread; Norman & Shallice named as the tradition EVC formalises, not leaned on -->
<!-- inactive-ok-file: THEORY-067 THEORY-062 THEORY-061 — new in this batch; accounts this one is set beside -->

# THEORY-070: How much cognitive control to exert, and on what, is decided by a cost-benefit computation (the expected value of control) in a specification system distinct from the structures that implement the control

## Source

Shenhav, Botvinick & Cohen (2013), [LIT-585](../literature.d/LIT-585.md), read in [NOTE-446](../notes.d/NOTE-446.md):
the model (Eqs. 1–3), §§4–7, and the open questions.

## What was actually shown

**The model.** Shenhav et al. ([LIT-585](../literature.d/LIT-585.md)) separate deciding on control
from exerting it. A control signal has an identity, the parameter it
targets, and an intensity, how far it displaces that parameter from its
default. Its expected value of control is the sum over outcomes of their
probability given the signal and the state, times their value, minus a cost
that rises with intensity. Value is recursive, immediate reward plus
discounted future EVC, so it "generalizes what is referred to as a
Q-value". The optimal signal maximises EVC. The cost is intrinsic: "like
physical effort, mental effort is assumed to carry intrinsic disutility".

**The mapping.** dACC monitors control-relevant states and outcomes and
specifies the signal. Lateral prefrontal cortex and subcortical structures
implement it. The review collects evidence for each part:

- dACC responds to conflict, errors, pain, loss and reward, and its
  responses fall as practice lowers the demand for control;
- dACC activity predicts post-error adjustment and the engagement of
  task-relevant regions, and cingulotomy abolished behavioural conflict
  adaptation;
- dACC activity tracked both trial difficulty and block-level incentive,
  and greater dACC response during a demanding task predicted later
  avoidance of it;
- dACC task selectivity leads lateral prefrontal cortex after a switch and
  lags it with repetition;
- exploration, foraging and patient intertemporal choice recruit dACC and
  are treated as overriding a default.

**What could have come out otherwise.** The account predicts dACC
activity that rises with stakes as well as with difficulty, and apathy, not
loss of control capacity, when the specifier is damaged. The cited
incentive and lesion findings are of that kind. But the paper runs no test
of its own. Its results are mappings onto existing findings, the model is
stated and not fitted, and the paper calls control-relevance selectivity "not
well-tested" and the dissociation of specification from regulation "not
definitive".

## What this does not say

- **Not what the cost is.** "What exact form does the cost function
  assume?" is left open, as is whether it is intrinsic or a proxy for
  opportunity cost.
- **Not how EVC is computed**, or what computing it costs.
- **Not that it governs emotion regulation.** The paper lists "modulators of
  emotion" among the parameters a signal can set, and treats override of
  emotion-driven responses as within dACC's remit. It does not show either.
- **Not that the specifier is of a different kind from what it governs.**
  It weighs value, as the competing tendencies do. What makes it distinct
  is that it is dedicated, and that it decides about control rather than
  about the task.

## Whether it rivals [THEORY-056](THEORY-056.md)

[THEORY-056](THEORY-056.md) holds that most emotion regulation is one motive state checking
another, with no distinct regulating system above them, and says that "a
distinct system that does the work generally would" refute it. This account
posits a distinct system, though a specifying one and not a regulating one.
On the record's reading the two can both be right, so no `rivals` is
declared:

- **They divide the cases.** [THEORY-056](THEORY-056.md)'s claim is about "most" regulation,
  which it says proceeds effortlessly, by concurrent impulses. EVC is about
  effortful control, the override of a default. [THEORY-056](THEORY-056.md) keeps a role for
  reflection, and its own `promote_when` presupposes that deliberate
  regulation recruits control networks.
- **The collision is conditional.** They would be rivals if EVC's
  specification were shown to decide emotion regulation generally,
  including the effortless kind. The paper asserts its reach to emotion and
  does not show it, and asks it as an open question.
- **Both deny a regulator of a different kind.** [THEORY-056](THEORY-056.md) denies reason
  governing emotion. EVC's decider is a value-maximiser, not reason. What
  divides them is whether control is dedicated, not whether it is of
  another kind.

So the test is the one [THEORY-056](THEORY-056.md) already names: whether effortless
regulation by a competing emotion works without recruiting the networks
this account describes.

## Connections

- **The unity it is about.** `behavioral-integration`: how control is
  allocated among tasks. It is silent on whose control it is, so it does not
  bear on self-governance or on [THEORY-029](THEORY-029.md) ([ADR-024](../decisions.d/ADR-024.md)).
- **[THEORY-067](THEORY-067.md) (Ainslie).** The précis rejects "organ" models of
  will, and EVC's treatment of patience as costly default override is close
  to one. For patience the two cannot both give the mechanism. That
  collision is in one application of this account, so it is stated here and
  not declared.
- **[THEORY-062](THEORY-062.md) (model-based and model-free control by reliability).**
  Different reasons for the same prediction, that concurrent demands favour
  habit: cost here, unreliability there.
- **[THEORY-061](THEORY-061.md).** EVC's control signals have identities that include
  thresholds and attention, which are that account's accumulation
  parameters. This account says who sets them; that one says what is set.
- **Self-determination theory.** EVC has one cost function of intensity,
  with no term for whether the regulation is endorsed. SDT reports that
  "true choice was not depleting" ([LIT-560](../literature.d/LIT-560.md), as read in [NOTE-441](../notes.d/NOTE-441.md)). Neither
  text addresses the other.
- **Norman and Shallice** ([LIT-600](../literature.d/LIT-600.md), unread). The supervisory override
  of habitual responses that EVC formalises descends from that tradition;
  the paper as retrieved does not cite them.
