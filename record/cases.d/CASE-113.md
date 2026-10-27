---
number: 113
status: Active
formerly:
- CASE-tmplvjrp
title: 'A deep network under conventional training: competing losses, an external optimizer and a scheduler, with three architectures that move governance inward and crossed interventions that locate it'
version: 2
history:
- version: 2
  date: '2026-10-26'
  note: >-
    A dated note added: T24 of the exchange "Experimental Infrastructure
    Review" re-derived this case without citing it, and added a third
    arm, training exposure, to its crossed interventions (QUESTION-
    tmpivbso). The case is unchanged.
standing: stipulated
kind: thought-experiment
tags:
- learning-theory
- agency
date: '2026-10-18'
line: learned-structure
summary: >-
  The owner's application case, U30–U31 of the exchange of 2026-10-17: a
  deep network during training, taken apart with the record's
  individuation and volition frameworks. A network is trained on tasks
  with conflicting gradients by an optimizer with its own state and a
  scheduler. A31's Systems A, B and C move the regulation of conflict from
  the optimizer into the learner by stages, and its crossed interventions
  say where a regulatory condition sits. Stipulated: the outcomes of the
  interventions are not known, except the optimizer arm in [THEORY-253](../theory.d/THEORY-253.md)'s
  solvable model.
supports:
- CLAIM-367
---
<!-- inactive-ok-file: CLAIM-367 CLAIM-157 CLAIM-288 — Proposed; the claim this case grounds and the claims and reading it uses, cited as open -->

# CASE-113: A deep network under conventional training: competing losses, an external optimizer and a scheduler, with three architectures that move governance inward and crossed interventions that locate it

## The case

A network with parameters θ_t, an optimizer with internal state m_t (momentum,
moments), a scheduler, a data process d_t and a loss L that sums two or more
task losses. A31's update:

  g_t = ∇_θ L(θ_t; d_t),  m_{t+1} = F(m_t, g_t),  θ_{t+1} = θ_t + U(m_{t+1}, g_t).

The task gradients have a negative Euclidean inner product, g_1ᵀg_2 < 0,
for part of training, in the stipulated parameterization. That is one
heuristic indicator of competing update directions, not a finding of
conflict: its sign is not invariant under smooth invertible
reparameterization, and a negative inner product does not exclude a
common descent direction ([CLAIM-366](../claims.d/CLAIM-366.md)). Whether the tasks are
actually frustrated is a separate test, against the declared acceptance
conditions and the admissible update set ([TERM-060](../terms.d/TERM-060.md)). The case needs
only the indicator; nothing below turns on its being frustration. The
trainer wants both losses low. Everything outside θ is fixed by the trainer: architecture,
loss weights, optimizer, schedule, parameter groups, what is frozen or
clipped.

Candidate bearers of any condition of training, A31 §1: a layer or
circuit; the network during one forward pass; the evolving parameterized
network; the network–optimizer pair; the full training process.

## The variations

A31 §9, "Three increasingly endogenous learning architectures":

- **System A, externally governed learner.** "Fixed network with ordinary
  optimizer. Conflict resolution is entirely external to the model." This
  is the base case.
- **System B, internally informed learner.** "Network computes a persistent
  regulatory signal that influences an external optimizer's update
  decisions."
- **System C, internally governed learner.** "A persistent subsystem
  monitors task conflicts and retained capabilities, then selects among
  admissible learning policies. Its own continuity depends on maintaining
  the capacities it regulates."

A31 §6 gives the matching attributions: A, "Optimization strain in the
training process"; B, "Potential functional regulatory distress of the
learning organization"; C, "A candidate integrated affect-like state".
In none is phenomenal experience established.

## The interventions

A31 §4:

- **Change the optimizer, hold the network fixed.** "If we hold the network
  fixed and change the optimizer, which aspects of its apparent
  preferences, priorities, and regulatory responses change?" If the
  candidate regime changes mainly here, it belongs to the training
  organization.
- **Disrupt a learned state, hold the optimizer fixed.** "If we hold the
  optimizer fixed and disrupt an internal regulatory representation learned
  by the network, does the system change how it responds to conflicting
  learning demands?" A positive result supports an internal causal role.
- **Crossed.** Change the optimizer, the network's regulatory state and the
  environment independently. A31: "That separates imposed regulation from
  learned regulation more effectively than inspecting a loss curve."

For System C, A31 adds an intervention on the candidate regulatory variable
with task errors held fixed, ablation of the subsystem that maintains it,
and a comparison of threats to continuing capabilities with "superficially
similar errors" that threaten none. "That last comparison is crucial: it
distinguishes a candidate endogenous evaluative state from a generic error
monitor."

## What it can show

- Where, under a stated setup, the record places a condition of training:
  in System A, with the network–optimizer pair or the training process
  ([CLAIM-367](../claims.d/CLAIM-367.md)), because the relations that decide which updates take
  effect are set outside the network.
- What evidence would move it inward: the second intervention coming out
  positive, or System C's ablations breaking its regulation.
- The optimizer arm has a documented instance in a solvable model. Under
  gradient descent, independent skills are learned together; under sign
  descent, they compete and emerge in sequence ([THEORY-253](../theory.d/THEORY-253.md)). The network's
  tasks are the same in both, so the order of learning is the optimizer's.

## What it cannot show

- Given its standing, how any real run comes out. The case states the
  design and the reading of each outcome, not the results.
- That System C, if built, sets its own norms. Its tasks and the
  capacities it protects are still chosen by the modeller ([CLAIM-288](../claims.d/CLAIM-288.md)).
- That the unit picked for the training dynamics is the right unit for
  every question. For output prediction the network is a natural unit
  ([CLAIM-152](../claims.d/CLAIM-152.md), [CLAIM-157](../claims.d/CLAIM-157.md)).
- Anything about feeling.

## Note of 2026-10-26: a second appearance, with an exposure arm

The reply at T24 of the exchange "Experimental Infrastructure Review"
re-derived this case without citing it, when the owner asked whether the
record's setup could interpret transformer learning dynamics
([QUESTION-275](../questions.d/QUESTION-275.md)). It wrote the update as
(θ_{s+1}, m_{s+1}) = 𝒰(θ_s, m_s, ℬ_s), cited [CLAIM-367](../claims.d/CLAIM-367.md) and [THEORY-253](../theory.d/THEORY-253.md) for the
external governance and the optimizer arm, and proposed as "the stronger
causal test" to "clone the full training state, modify a particular
training exposure or update pathway, and observe the subsequent
development of identified circuits".

That adds a third arm to the two this case crosses (optimizer, learned
state): training exposure, meaning task mix and curriculum, which the
reply's governance table reads as which capacities receive opportunities
to develop. The reply also used g_kᵀg_j as "one local measure" of whether
task pressures reinforce or oppose one another. This case already calls
it a heuristic indicator, and [CLAIM-366](../claims.d/CLAIM-366.md) says why: its sign is not
invariant under reparameterization. The case is unchanged.
