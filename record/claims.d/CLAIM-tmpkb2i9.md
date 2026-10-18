---
status: Proposed
title: 'An objective that originates outside a learning system can become a goal of the training organization, through its causal role in selecting, stabilizing and reproducing the learned structure it rewards; exogenous origin does not disqualify a goal, but it does not show that the network governs or endorses the objective, and what is selected is performance on the updating distribution, not generalization'
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  A showing that, for the training organization, a goal-directed
  description adds nothing to a device description of its update rule:
  that it never beats the device model by more than the Occam cost
  (CLAIM-174's second test), or that what persists after training is
  passive retention only, so that a learned capability perturbed in
  training is not preferentially restored by the training dynamics
  (A36's first grade). Not defeated by the objective's having been
  written by the trainer, which is the premise the claim denies matters;
  and not defeated by goal misgeneralization, which is about which goal
  is maintained, not whether one is.
tags:
- agency
- motivation
- representation-learning
date: '2026-10-18'
line:
- learned-structure
- will-organization
objects_to:
- CLAIM-288
grounds:
- THEORY-047
- THEORY-054
- THEORY-616
complements:
- CLAIM-174
- CLAIM-tmpw4w7a
summary: >-
  The owner's, U35 of the exchange of 2026-10-17, against A34's guardrail
  that "Loss minimization does not automatically mean the model has its
  own goals": the externally assigned objective "can motivate
  identification and persistence of learned features", so the training
  process can be described as "having endogenous goals". A35 granted it:
  "Yes, in a qualified but important sense", and weakened the
  generalization half, since selection is for performance on "the
  encounters and feedback distribution actually used for updating". It
  objects in part to CLAIM-288: it grants that a modeller-fixed objective
  does not show self-constitution, and denies that exogenous origin bars
  a goal from becoming the training organization's own regulation. The
  sharp edge: the goal belongs to the training organization (CLAIM-tmpw4w7a),
  not to the network, and nothing here says the network endorses or
  governs it.
---

# CLAIM-tmpkb2i9: An objective that originates outside a learning system can become a goal of the training organization, through its causal role in selecting, stabilizing and reproducing the learned structure it rewards; exogenous origin does not disqualify a goal, but it does not show that the network governs or endorses the objective, and what is selected is performance on the updating distribution, not generalization

## The claim

A34 put a guardrail in its table: "Loss minimization does not automatically
mean the model has its own goals". The owner, at U35: "however, the
externally assigned objective can motivate identification and persistence
of learned features. if encountering high loss is appropriately
characterized as a systemic disturbance of the kind an organization is
motivated to avoid, then it seems reasonable to describe the training
process as having endogenous goals of identifying stable representations
that generalize, since that's the regime which reduces the likelihood of
encountering future disturbances. right? or am I maybe speaking too
strongly or missing something here?"

A35: "**Yes, in a qualified but important sense.** I think your objection
exposes a weakness in my earlier formulation. I was treating the *origin of
a goal* and the *organization through which it becomes effective* as though
they were the same question." Its form of the point: "An externally imposed
evaluative criterion can become internal to a persistent learning
organization through its causal role in selecting, stabilizing, and
reproducing adaptive structure. But the emergence of stable structure does
not alone show that the learned network governs or endorses the criterion
that selected it." And in §8: "the key is to distinguish **goal provenance,
goal realization, and goal governance**."

The claim holds those three apart:

- **Provenance.** Where the objective came from. Here, the trainer.
- **Realization.** Whether it organizes the system's activity. Each update
  changes how the system meets later batches, so the loss sets up "a
  history-dependent selection regime" (A35), and the features that survive
  are found by the interaction of architecture, data, initialization and
  optimizer, not written down by the trainer. The representational
  organization is endogenous though the criterion is not.
- **Governance.** Whether the system can regulate or revise the objective.
  Ordinary training gives no evidence of this.

Exogenous provenance does not settle realization. The record already holds
the human case: on self-determination theory a value taken in from outside
can be introjected or integrated, and how it was taken in fixes which
(THEORY-047); autonomy is then graded by integration, not by origin
(THEORY-054). The owner's thesis is the training-time counterpart of the
claim that external provenance can become internal regulation.

## The weakened half

A35 narrowed what is selected: "There is one part of your formulation I'd
weaken: that learning is necessarily motivated to discover representations
that generalize. Ordinary empirical-risk minimization can reward
memorization." So "the selection pressure is directly for performance under
the **encounters and feedback distribution actually used for updating**."
Generalization would be an emergent instrumental goal only if the
organization "protects performance across novel but relevant variations,
even when doing so imposes immediate costs". The owner did not dispute this
at U36.

A36 added a limit from goal misgeneralization (Langosco et al. 2022): a
trained agent can keep its competence off-distribution "yet continue
pursuing the wrong goal", so "**generalization of capability and
generalization of objective are separable**". That supports the owner's
thesis, since a goal-like structure persisted, and narrows it: "we need to
discover **which operative objective the resulting system actually
maintains**". The maintained goal need not be the trainer's.

## The test

A36's three grades of retention are the operational form. "**Passive
retention:** The representation persists because subsequent updates happen
not to disrupt it. **Selective retention:** Training dynamics systematically
favor configurations preserving the representation. **Regulated
retention:** A maintained mechanism detects threats to a capability
implemented by the representation and changes learning policy to protect
it." Its test is "**active causal maintenance**": perturb a capability and
see whether the endogenous dynamics reconstruct it, against a matched system
whose recovery is "supplied exclusively by an external trainer".

The claim needs selective retention. Regulated retention is what governance
would need. The admission test for an agent at a level (CLAIM-174) is the
standard a goal attribution here must meet: the goal-directed description
has to beat a device description of the update rule by more than its Occam
cost.

## Against CLAIM-288

CLAIM-288 says a simulation whose operators maximize modeller-fixed
objectives "cannot show self-constitution, because the norms the
organization appears to maintain are then the modeller's". A30 §8 applied
it to training without citing it: "the task loss is generally chosen by an
experimenter". This claim grants CLAIM-288 for self-constitution, which is
a claim about governance. It denies the further step, that a norm the
modeller supplied cannot become the organization's regulation. CLAIM-288's
own answer condition, operators whose objectives are "produced and revised
by the organization", is the governance grade, and it is not needed for a
goal to be realized. A40 §2.3 and A47 §2 restate the split ("The origin,
maintenance, integration, and ownership of a goal remain separate
questions").

## Whose goal

The bearer is the training organization, the optimizer, model and data
together, which is where CLAIM-tmpw4w7a puts training-time regulatory
conditions. Not the network alone: A37 said of a consolidation mechanism
supplied by the training algorithm that it shows "resolve-like organization
**of the training system**, not volition owned by the neural network alone".
For a deployed language model, Goldstein and Lederman put the bearer of
attitudes at the instance, not the model (THEORY-616). The attribution is
relative to the unit, and the three units differ.

The record's deferred claim that a will is its own to the degree its
commitments "arise through, remain integrated with, and are answerable to"
its organization (CLAIM-016, Deferred with the authenticity line) has the
same three parts as A35's provenance, realization and governance. Whether
that line reopens is the owner's decision, not made here.

## What it does not say

- It does not say the network has goals of its own, endorses its loss, or
  has any say over it. That is the governance grade, which ordinary
  training does not show.
- It does not say training aims at generalization. What is selected is
  performance on the updating distribution.
- It does not say high loss threatens the system. A35: high loss "ordinarily
  does not physically threaten the network's continued existence". It is a
  disturbance relative to the training organization's maintained
  objective, not to its viability.
- It does not answer CLAIM-288's objection to the constitutive thesis of
  CLAIM-284. It denies only that the objection reaches goal realization.
