---
status: Proposed
title: 'Competent behaviour does not establish an internal world model: over a fixed interface and a finite horizon, an agent with no model, whose actions are looked up from the history so far, reproduces the interaction distribution of an agent that has one exactly, so ascribing a world model is an explanation of the behaviour, and it names a realized mechanism only where compression, generalization beyond the interface or intervention on internals shows one'
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  A result that competence over a stated family of tasks entails an
  internally realized predictive component that can be identified by
  intervention, under matched memory, computation, intervention
  repertoire and developmental history: for instance a behavioural
  signature over the declared tests (transfer to new objectives,
  counterfactual generalization) that no organization of the same
  resources without such a component reproduces. It is not defeated by
  showing that some agents do contain world models, nor by Richens et
  al.'s theorem (LIT-tmplzs0t), which holds of every implementation of a
  competent goal-conditioned policy, a lookup table included (CLAIM-tmp4htg4).
tags:
- agency
- cognition
- philosophy-of-science
date: '2026-10-31'
line:
- distributed-agency
rests_on:
- CLAIM-414
grounds:
- THEORY-092
- THEORY-689
- THEORY-624
complements:
- CLAIM-355
- CLAIM-447
bears_on:
- QUESTION-086
summary: >-
  The owner's thesis at U20 of the exchange "Analyze nucleation
  concepts" (2026-10-31): that under the record's framework a world model
  is "essentially a 'folk' explanatory tool and that no such thing need
  explicitly be present for the external behavior to be indistinguishable
  from a comparable black box agent which actually did contain a world
  model". A20 agreed and gave the construction, with a limit the claim
  keeps: the attribution "sometimes ... names a genuine, interventionally
  identifiable computational mechanism". The construction is Block's
  lookup-table argument ([THEORY-092](../theory.d/THEORY-092.md)) applied to agency, so it is
  elementary; the thesis is the reading of it.
---
<!-- inactive-ok-file: THEORY-092 QUESTION-086 — Proposed or Open; Block's argument and the question of endogenous revision, cited as open -->

# CLAIM-tmph29mx: Competent behaviour does not establish an internal world model: over a fixed interface and a finite horizon, an agent with no model, whose actions are looked up from the history so far, reproduces the interaction distribution of an agent that has one exactly, so ascribing a world model is an explanation of the behaviour, and it names a realized mechanism only where compression, generalization beyond the interface or intervention on internals shows one

## The claim

Fix an interface: the agent's actions, the environment's observations,
and a horizon T. Let agent A maintain an explicit predictive model of
its environment and act on it; its policy, marginalized over its internal
state, is a kernel π_A(a | h) from histories to actions. Let agent B hold
no model, only the table π_B(a | h) = π_A(a | h) for every history h of
length below T. Then for any environment the probability of every
interaction history h₀:T is the same for A and B, by the chain rule, since
each step's action law and the environment's response law are the same.
No experiment confined to that interface and horizon can tell them apart
(A20 §1).

So competence on the interface is not evidence that a world model is
present. "World model" ascribes an organization that explains the
behaviour, as "the self" ascribes an owner to it ([CLAIM-355](CLAIM-355.md)). That is
the owner's U20 point. Brooks's robots are the standing example that
competent action can run on the world as "its own best model"
([THEORY-689](../theory.d/THEORY-689.md)).

The ascription can still name something real, and the claim says when.
Three kinds of evidence go beyond the interface:

- **Compression.** The table grows with the number of histories, and a
  model can be exponentially smaller. Where resources are bounded, as in
  every physical agent, matched competence under a resource bound can
  favour the model ([THEORY-624](../theory.d/THEORY-624.md) casts this as model comparison
  relative to a prior).
- **Generalization beyond what the implementation was built to cover.**
  A model can serve new objectives or new horizons without relearning. A
  table cannot go beyond its domain. A table whose domain already includes
  the goals generalizes across them, so generalization within the covered
  family does not discriminate.
- **Intervention on internals.** Altering a component and finding the
  behaviour change as a predictive model's would. Matched trajectories
  conceal differences that intervention exposes ([CLAIM-414](CLAIM-414.md)).

## What it does not say

- **That no agent has a world model.** Some do, and an intervention can
  show it.
- **That the table encodes nothing.** Functionally, B's table determines
  every prediction A's model would make that the interface can reveal.
  Whether that counts as "containing" a model is the question Richens et
  al. ([LIT-tmplzs0t](../literature.d/LIT-tmplzs0t.md)) answer yes, for goal-conditioned agents competent
  across a family of composite goals. On that functional reading their
  theorem holds and is filed as the counter [CLAIM-tmp4htg4](CLAIM-tmp4htg4.md). On the explicit-component
  reading, the claim stands.
- **That causal model, wanting and efficacy go together.** They are
  separable ([CLAIM-447](CLAIM-447.md)); this claim is about the first only.
