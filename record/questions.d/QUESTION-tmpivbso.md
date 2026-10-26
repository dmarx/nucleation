---
status: Open
title: 'Can the development of a transformer''s circuits in training be described as organizational regimes forming over shared, overlapping latent features, so that a model coupling feature allocation to circuit interaction, fitted to early checkpoints, predicts the effects of held-out training interventions that feature-only and circuit-only descriptions fitted to the same checkpoints miss?'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed from T24 of the exchange "Experimental Infrastructure Review",
    the owner's question, with the reply's research question as its test.
    The page did not render the reply ("Message delivery timed out"); the
    owner pasted it. The reply reports no simulation.
tags:
- learning-theory
- representation-learning
date: '2026-10-26'
line: learned-structure
refines:
- QUESTION-039
summary: >-
  The owner, at T24: "could we potentially apply this setup as an
  interpretive framework for understanding the learning dynamics of
  transformers?" "This setup" is the dynamic latent-feature model of T23
  ([CASE-tmplcm41](../cases.d/CASE-tmplcm41.md)). The reply answered with a test: "Can the emergence,
  specialization, overlap, and persistence of transformer circuits be
  explained by modeling them as developing organizational regimes over
  shared latent features—and does that description predict training
  responses that existing feature- or circuit-based analyses miss?" It is
  the second time the owner has applied the record's frameworks to a
  network in training. The first was [CASE-113](../cases.d/CASE-113.md) and [CLAIM-367](../claims.d/CLAIM-367.md), and [CASE-117](../cases.d/CASE-117.md)
  is the population form. The sharp edge is [CLAIM-427](../claims.d/CLAIM-427.md)'s third grade:
  positive results would have to be prospective, against strong
  conventional baselines at matched complexity. Nothing here says that a
  circuit is a perspective.
---
<!-- inactive-ok-file: CLAIM-367 CLAIM-329 CLAIM-118 CLAIM-427 CLAIM-278 CLAIM-263 CLAIM-286 CLAIM-287 THEORY-783 THEORY-039 THEORY-481 TERM-072 — Proposed; the claims and readings the question is framed by or re-derives, cited as open, nothing here rests on their being settled -->
<!-- inactive-ok-file: CLAIM-tmpwr001 CASE-tmplcm41 — Proposed; filed with this question from the same exchange -->

# QUESTION-tmpivbso: Can the development of a transformer's circuits in training be described as organizational regimes forming over shared, overlapping latent features, so that a model coupling feature allocation to circuit interaction, fitted to early checkpoints, predicts the effects of held-out training interventions that feature-only and circuit-only descriptions fitted to the same checkpoints miss?

## Why it is a question

The reply's construction runs over checkpoints θ_0 … θ_S of a small
transformer trained on two or three synthetic task families. It has three
layers.

- **Features.** A binary allocation B_{ck,s} of components c (head
  outputs, MLP channels) to latent features k at checkpoint s, with
  r_{c,s}(x) ≈ Σ_k B_{ck,s} a_{k,s}(x) v_{ck,s} and an Indian buffet prior
  on B: "several components can participate in the same feature, and one
  component can participate in several features". This is [CASE-tmplcm41](../cases.d/CASE-tmplcm41.md)'s
  model with components for employees. "This factorization is an
  approximation, not an exact decomposition of transformer computation."
- **Development.** A temporal prior p(B_s | B_{s−1}, θ_s, 𝒟_s) allowing
  features to be born, persist, redistribute and disappear.
- **Regimes.** Above the features, candidate regimes of participating
  features, their routing, and the contexts in which they are
  consequential: "an inferred structure, not a primitive in the
  transformer or the initial probabilistic model". That is
  [CLAIM-tmpwr001](../claims.d/CLAIM-tmpwr001.md) in a new setting (its sixth appearance).

Three analyses are to be compared: feature-only, circuit-only, and coupled
feature–circuit dynamics, against "standard sparse dictionaries or
crosscoders, direct circuit localization, and simpler checkpoint-level
state-space models". The reply: "The dynamic IBP must earn its
complexity."

## What the record already holds

Most of the reply's apparatus is on file, and it cited four codes
([CLAIM-367](../claims.d/CLAIM-367.md), [THEORY-169](../theory.d/THEORY-169.md), [CLAIM-329](../claims.d/CLAIM-329.md), [THEORY-253](../theory.d/THEORY-253.md)).

- **Who governs training.** "The transformer itself is not necessarily
  governing this development" is [CLAIM-367](../claims.d/CLAIM-367.md): individuated for training, the
  unit is at least the network–optimizer pair, and its six relations map
  onto the reply's governance table (routing, gradient allocation,
  optimizer, curriculum).
- **Inference is not training.** "That does not mean the network's
  persistent parameters change during an ordinary forward pass" is
  [THEORY-169](../theory.d/THEORY-169.md)'s reading of in-context conditioning. The reply's three
  timescales (training, layer, token) are [CLAIM-118](../claims.d/CLAIM-118.md)'s sources of change.
- **The update rule and its interventions.** (θ_{s+1}, m_{s+1}) =
  𝒰(θ_s, m_s, ℬ_s), and "clone the full training state, modify a particular
  training exposure or update pathway", are [CASE-113](../cases.d/CASE-113.md)'s update and crossed
  interventions. What the reply adds is a third arm, training exposure
  (task mix and curriculum), beside [CASE-113](../cases.d/CASE-113.md)'s optimizer and learned
  state.
- **The optimizer arm.** [THEORY-253](../theory.d/THEORY-253.md): in the Geometry model, gradient
  descent learns independent skills together and sign descent in
  sequence. That is a simulation in a solvable model. That Adam-like
  optimizers cause sequential onset in trained networks is the Proposed
  [THEORY-783](../theory.d/THEORY-783.md), and its test is the open [QUESTION-193](QUESTION-193.md). The reply cites
  [THEORY-253](../theory.d/THEORY-253.md) for transformers without that scope.
- **Task interaction.** The reply's g_kᵀg_j "under ordinary Euclidean
  gradient descent" is [CLAIM-366](../claims.d/CLAIM-366.md)'s object: its sign is not invariant under
  reparameterization, and a negative product does not exclude common
  descent. The reply's two caveats, Euclidean geometry and Adam, are one
  fact ([CLAIM-366](../claims.d/CLAIM-366.md)'s note of 2026-10-26).
- **Continuity.** The reply's "representational" and "computational"
  continuity are [TERM-071](../terms.d/TERM-071.md)'s state and dynamical senses. It cited [CLAIM-329](../claims.d/CLAIM-329.md)
  for "distinct forms of organizational persistence", which is [TERM-071](../terms.d/TERM-071.md)'s
  job. [CLAIM-329](../claims.d/CLAIM-329.md) is the thesis that persistence through turnover is by
  causal transmission, not resemblance, and the reply's §6 asks its
  question without it: "Can we distinguish a continuing computation from a
  newly learned replacement with similar output behavior?"
  ([CLAIM-329](../claims.d/CLAIM-329.md)'s note of 2026-10-26).
- **Influence on inference against influence on learning.** "A component
  might have a large effect on current predictions but receive little
  additional training signal" is [QUESTION-134](QUESTION-134.md)'s split of influence,
  competence and access, and [CASE-117](../cases.d/CASE-117.md)'s coupled and decoupled training
  exposure ([QUESTION-134](QUESTION-134.md)'s note of 2026-10-26). The rigidity and recovery
  material is [CLAIM-286](../claims.d/CLAIM-286.md), and the dormant-alternative caveat is [CLAIM-287](../claims.d/CLAIM-287.md)'s
  reinstatable capacity.
- **Acquisition.** "Does a circuit emerge by acquiring new features,
  reorganizing existing features, or both?" is [QUESTION-039](QUESTION-039.md)'s second half,
  whether acquisition is one kind of event or several. [THEORY-039](../theory.d/THEORY-039.md), [THEORY-481](../theory.d/THEORY-481.md)
  and [THEORY-229](../theory.d/THEORY-229.md) answer parts of it.

What is new is the coupling: an organizational reading of circuits over a
developing feature allocation, with a stated way to lose.

## What would answer it

A prospective test, as the reply puts it: "fit the model using early
training checkpoints, then test its predictions about later functional
changes, including changes under held-out training interventions". The
interventions are [CASE-113](../cases.d/CASE-113.md)'s arms plus training exposure. The reply's
induction-circuit setting is a natural first case: which partial
capacities exist before the circuit is effective, and whether it forms by
acquiring features or by reorganizing them. The answer is yes if the
coupled description out-predicts the feature-only and circuit-only ones
at matched complexity ([CLAIM-427](../claims.d/CLAIM-427.md)'s third grade), and no if it does not.

Two conditions come from checks made when this was filed ([CASE-tmplcm41](../cases.d/CASE-tmplcm41.md)):

- The temporal prior must not condition on θ_s, from which B_s is read.
  Otherwise it predicts nothing, and the prospective test is empty.
- Births and splits must be told apart from the model's free symmetries.
  Rescaling, splitting a feature into copies and a zero contribution vector
  all leave the reconstruction unchanged.

## What would not answer it

- "Merely recovering visually plausible circuits from already-trained
  models" (the reply).
- A tie with a state-space model built on the same kernels, which is an
  identity. The lab's comparator pilot (dmarx/PerspectiveLab@dce302b)
  already showed this for its own models ([CLAIM-427](../claims.d/CLAIM-427.md)'s note of 2026-10-26).
- Feature births or splits that a change of basis or the buffet's split
  symmetry produces ([CLAIM-263](../claims.d/CLAIM-263.md)'s quotient, [THEORY-018](../theory.d/THEORY-018.md)).
- Continuity of a feature judged by resemblance alone ([CLAIM-329](../claims.d/CLAIM-329.md),
  [TERM-071](../terms.d/TERM-071.md)).
- Success defined in the framework's own terms ([CLAIM-278](../claims.d/CLAIM-278.md)).

## Not in scope

Instructions for training transformers, which are the anthology's
([ADR-048](../decisions.d/ADR-048.md)). Whether a circuit regime is a perspective in any sense beyond
[TERM-072](../terms.d/TERM-072.md)'s organizational one: the reply itself says "satisfying this
organizational definition would say nothing by itself about phenomenal
experience or autonomous agency".
