---
number: 519
status: Proposed
formerly:
- CLAIM-tmph29mx
title: 'Competent behaviour does not establish an internal world model: over a fixed interface and a finite horizon, an agent with no model, whose actions are looked up from the history so far, reproduces the interaction distribution of an agent that has one exactly; a policy can identify predictive structure without any particular internal component realizing it, so compression and generalization support comparing candidate architectures, and establishing an internal mechanism needs evidence that discriminates candidate implementations, such as targeted interventions'
version: 2
history:
- version: 2
  date: '2026-10-31'
  note: >-
    At the owner's review. Version 1 said compression, generalization or
    intervention on internals can show a realized mechanism. Exceptional
    compression and generalization favour a model-based explanation over a
    particular lookup-table explanation. They do not identify the internal
    architecture, since many compact controllers are not explicit
    generative world models. The title and the evidence list now separate
    a policy identifying predictive structure, where Richens et al.'s
    result (CLAIM-513) belongs, from a particular component realizing
    it, which needs evidence that discriminates implementations.
    At the owner's second review the same day, "not evidence" became
    "not sufficient to establish": the equivalence shows competence does
    not establish or identify an explicit world model, not that it gives no
    Bayesian evidence for a model-based architecture.
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
  al.'s theorem (LIT-1891), which holds of every implementation of a
  competent goal-conditioned policy, a lookup table included (CLAIM-513).
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

# CLAIM-519: Competent behaviour does not establish an internal world model: over a fixed interface and a finite horizon, an agent with no model, whose actions are looked up from the history so far, reproduces the interaction distribution of an agent that has one exactly; a policy can identify predictive structure without any particular internal component realizing it, so compression and generalization support comparing candidate architectures, and establishing an internal mechanism needs evidence that discriminates candidate implementations, such as targeted interventions

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

So competence on the interface is not sufficient to establish that a
world model is present, or to identify one. That is not to say it is no
evidence: under relevant priors and resource assumptions, competence can
still favour a model-based architecture, as the compression point below
says. "World model" ascribes an organization that explains the
behaviour, as "the self" ascribes an owner to it ([CLAIM-355](CLAIM-355.md)). That is
the owner's U20 point. Brooks's robots are the standing example that
competent action can run on the world as "its own best model"
([THEORY-689](../theory.d/THEORY-689.md)).

Two things must be kept apart:

  policy identifies predictive structure  ⇏  a particular internal
  component realizes it.

Richens et al.'s result belongs on the left ([CLAIM-513](CLAIM-513.md)). Mechanistic
identification belongs on the right. The evidence for each differs.

- **Compression.** A table grows with the number of histories, and a model
  can be exponentially smaller. Where resources are bounded, as in every
  physical agent, matched competence under a resource bound can favour a
  model-based explanation ([THEORY-624](../theory.d/THEORY-624.md) casts this as model comparison
  relative to a prior). It favours that explanation over a particular
  table. It does not identify the architecture: many compact controllers
  are not explicit generative world models.
- **Generalization beyond what the implementation was built to cover.**
  A model can serve new objectives or new horizons without relearning, and
  a table cannot go beyond its domain. This too supports comparing
  architectures, and no more. A table whose domain already includes the
  goals generalizes across them, so generalization within the covered
  family does not discriminate.
- **Evidence that discriminates implementations.** Establishing an internal
  mechanism needs observations that candidate implementations, matched in
  behaviour, predict differently. Targeted interventions on internals are
  the main source: alter a component and find the behaviour change as a
  predictive model's would, and not as the rivals' would. Matched
  trajectories conceal differences that intervention exposes ([CLAIM-414](CLAIM-414.md)).

## What it does not say

- **That no agent has a world model.** Some do, and an intervention can
  show it.
- **That the table encodes nothing.** Functionally, B's table determines
  every prediction A's model would make that the interface can reveal.
  Whether that counts as "containing" a model is the question Richens et
  al. ([LIT-1891](../literature.d/LIT-1891.md)) answer yes, for goal-conditioned agents competent
  across a family of composite goals. On that functional reading their
  theorem holds and is filed as the counter [CLAIM-513](CLAIM-513.md). On the explicit-component
  reading, the claim stands.
- **That causal model, wanting and efficacy go together.** They are
  separable ([CLAIM-447](CLAIM-447.md)); this claim is about the first only.

## Note of 2026-11-01: a precedent in cognitive modelling

Bechtel and Abrahamsen ([LIT-1936](../literature.d/LIT-1936.md), [NOTE-1492](../notes.d/NOTE-1492.md), [THEORY-1290](../theory.d/THEORY-1290.md))
make this claim's methodological point about cognitive models in
general. Such models are proposed de novo and checked only by fit, and
"Empirical evidence can rule out specific models, but usually cannot
decide between competing architectures" (p. 332). Their example is the
past-tense debate, "irresolvable" without constraint from identified
parts (p. 330). Their footnote 5 (p. 329) bears on the claim's two
readings of "contains a model". A model whose variables track a
mechanism describes it and does not perform its operations. A system
whose behaviour a predictive model describes need not contain a
component that performs prediction. Their remedy is anchoring variables
to parts found by experiment. That is the claim's "evidence that
discriminates candidate implementations".

No status, title or warrant changes.
