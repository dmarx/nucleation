---
number: 367
status: Proposed
formerly:
- CLAIM-tmpw4w7a
title: 'Whether a training-time regulatory condition belongs to a network depends on which unit is individuated for the training dynamics and whose jurisdiction governs the updates; in conventional training most of that governance falls to the optimizer–model–data system, so a condition of training is not thereby a condition of the network'
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  A31's crossed intervention coming out the other way on a conventionally
  trained network (CASE-113): holding the network fixed and changing
  the optimizer leaves its characteristic responses to conflicting
  learning demands unchanged, while holding the optimizer fixed and
  disrupting a state the network learned abolishes or alters them, so that
  the regulation of conflict sits in the network even under an external
  optimizer. Not defeated by a learner with an internal adaptive
  controller (A31's System B or C), which the claim already allows to
  carry more of the governance.
tags:
- agency
- learning-theory
- individuation
date: '2026-10-18'
line:
- learned-structure
- distributed-agency
rests_on:
- CLAIM-152
- CLAIM-170
- CLAIM-174
- CLAIM-027
grounds:
- THEORY-253
- CASE-113
complements:
- CLAIM-288
- CLAIM-194
- CLAIM-356
uses:
- TERM-017
summary: >-
  The owner's correction, U31 of the exchange of 2026-10-17: "it might
  help clarify things if we apply our individuation and volition
  frameworks to this system", the system being a deep network during
  training (U30). A31 granted it: "applying individuation first, then
  volition, then affect exposes a problem in our previous discussion".
  Individuated for the training dynamics, the unit is at least the
  network–optimizer pair; mapped through the six relations of
  will-organization, most of the governance of updates is outside the
  network's jurisdiction. So optimization difficulty in conventional
  training is real and belongs to the training system. The sharp edge: it
  does not say the governance is unreal, or that a network cannot come to
  hold some of it.
---
<!-- inactive-ok-file: CLAIM-170 CLAIM-174 CLAIM-027 CLAIM-288 CLAIM-194 CLAIM-157 CLAIM-284 THEORY-253 CASE-113 QUESTION-122 CLAIM-368 — Proposed; open claims and readings, cited as open -->

# CLAIM-367: Whether a training-time regulatory condition belongs to a network depends on which unit is individuated for the training dynamics and whose jurisdiction governs the updates; in conventional training most of that governance falls to the optimizer–model–data system, so a condition of training is not thereby a condition of the network

## The claim

At U30 the owner asked to "discuss the possibility of meaningful affective
states attributable to a deep neural network specifically during training"
([QUESTION-122](../questions.d/QUESTION-122.md)). A30 answered by grading training phenomena as
ingredients of distress. At U31 the owner redirected: "it might help
clarify things if we apply our individuation and volition frameworks to
this system". A31 granted that this was a correction: "applying
**individuation first, then volition, then affect** exposes a problem in our
previous discussion: we were asking whether a neural network experiences
something during training before establishing precisely *which system*
could possess that state."

A31's conclusion: "Conventional deep-network training is a genuine adaptive
dynamical process, but most of its apparent goal-directedness and
regulation belong to the larger optimizer–model–data system rather than to
the neural network considered separately."

The argument has three steps.

1. **Individuation is relative to the target** ([CLAIM-152](CLAIM-152.md)). In A31's
   setup, g_t = ∇_θ L(θ_t; d_t), m_{t+1} = F(m_t, g_t), θ_{t+1} = θ_t +
   U(m_{t+1}, g_t). For predicting outputs, y = f_θ(x), the network is a
   natural unit. For predicting training, (θ_{t+1}, m_{t+1}) = F(θ_t, m_t,
   d_t), the joint state is needed: "The same parameter configuration can
   evolve differently depending on optimizer momentum, moments, or
   scheduler state." A31 counts five candidates, from a circuit to the full
   training process, and "there is no entitlement to treat all five as the
   same individual". [CLAIM-157](CLAIM-157.md)'s block criterion, which A31 also cites,
   gives the same answer for the same reason.
2. **Agency and will are located by jurisdiction** ([CLAIM-170](CLAIM-170.md), [CLAIM-174](CLAIM-174.md)).
   [CLAIM-174](CLAIM-174.md)'s third test asks whether the candidate's policy would adapt
   if its actions' consequences changed. "At the level of the entire
   training loop, adaptation is clear. At the level of the network alone,
   autonomous adaptation is much less clear." A willed agent is the
   jurisdiction of a will-organization ([CLAIM-170](CLAIM-170.md)).
3. **The relations that select what becomes effective sit outside the
   network** ([CLAIM-027](CLAIM-027.md), [TERM-017](../terms.d/TERM-017.md)). A31's mapping of the six relations onto
   training: accessibility to architecture, data selection and optimizer;
   precedence to loss weights and optimizer geometry; jurisdiction to the
   computational graph and parameter groups; persistence to parameters plus
   training dynamics; suspension to optimizer, scheduler and training
   controller; transformation to the training algorithm or a
   meta-controller. "much of that arrangement is *outside the neural
   network's jurisdiction*. That doesn't make the governance unreal. It
   means it belongs to a larger system."

[THEORY-253](../theory.d/THEORY-253.md) is the documented ground for step 3 in a solvable model: with
the network's task structure fixed, the optimizer alone decides whether
independent skills are learned together (gradient descent) or compete and
emerge in sequence (sign descent).

## The methodological rule

A31 §10: "**Before attributing affect to a trained system, determine
whether the proposed affective state belongs to the network, the learning
controller, the larger training apparatus, or some emergent organization
spanning them.**" This claim is the rule applied to conventional training.
It is kept here and not filed as a separate entry.

## Acquiring and governing

A31 §7: "acquiring capacities ≠ governing the acquisition of capacities".
"During ordinary training, the neural network becomes more capable
*because it is being governed by something outside itself*", and "The
network's development can be highly organized without being self-directed."
This is a second appearance of the record's distinction between effective
action and the capacity to govern among regimes ([ARG-007](../arguments.d/ARG-007.md)), and of
[CLAIM-284](CLAIM-284.md)'s self as one that takes part in governing its own persistence
and transformation. A31's own three achievements make the same cut:
learning a representation, maintaining a learned capability, and
"Maintaining the learning organization itself", of which "Only the third
directly approaches the stronger organizational-autonomy criterion."

For affect it matters because, A31: "frustration normally presupposes a
relevant demand or commitment belonging to the affected system. External
optimization failure alone does not establish such a commitment." A31's
Case A, conflicting gradients g_1ᵀg_2 < 0 under a trainer who wants both
losses minimized, is "Optimization strain in the training process". (The
sign of g_1ᵀg_2 is a coordinate-dependent indicator of competing
directions, not a test of frustration; [CLAIM-366](CLAIM-366.md).) U33
later made frustration, not distress, the primitive ([CLAIM-368](CLAIM-368.md)); the
claim is stated for any regulatory condition, so it holds of either.

## What it does not say

- It does not say training-time governance is unreal, or merely
  metaphorical. It says whose it is.
- It does not say a network cannot come to hold it. A31 §8: "The relevant
  transition would be in **who or what governs adaptation**", and "I
  wouldn't assume such a transition occurs in ordinary deep learning. But
  it is a clear hypothesis for systems with internal adaptive
  controllers." Systems B and C of [CASE-113](../cases.d/CASE-113.md) are where it would occur.
- It does not say the training system is an agent with its own norms. Its
  objectives are the trainer's: "its normative significance derives from
  the training objective chosen by the trainer." [CLAIM-288](CLAIM-288.md) says a
  modeller-fixed objective cannot show self-constitution, and the training
  system inherits that limit. A31's "Unity of optimization" is not its
  "Unity of self-governance".
- It does not decide anything about feeling. A31: "None of these
  capacities, individually or jointly, establishes phenomenal
  consciousness."
- It does not supply the boundary test. [CLAIM-194](CLAIM-194.md) objects that a coupling
  criterion cannot tell a boundary a system makes from one imposed on it,
  and in conventional training the boundary is imposed.
