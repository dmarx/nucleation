---
status: Open
title: 'Which predictive and causal query capabilities are implied by competence across specified goal families, which are available to the agent under its actual resource constraints, and which require distinct internal modeling mechanisms; and under what conditions can those mechanisms and capabilities be maintained, revised or reconstructed endogenously?'
version: 1
tags:
- agency
- cognition
- philosophy-of-science
date: '2026-10-31'
line: distributed-agency
summary: >-
  The owner's question at the second review of the filing of the exchange
  "Analyze nucleation concepts" (2026-10-31). The record's world-model
  thesis (CLAIM-tmph29mx) and its counter from Richens et al.
  (CLAIM-tmp4htg4) disagree less than they seem, because "world model"
  names several things. This question separates them so that the record
  can investigate each without presupposing that one is fundamental.
---
<!-- inactive-ok-file: CLAIM-tmph29mx TERM-086 — Proposed; the thesis and the term this question sorts, cited as open -->

# QUESTION-tmp6e1nh: Which predictive and causal query capabilities are implied by competence across specified goal families, which are available to the agent under its actual resource constraints, and which require distinct internal modeling mechanisms; and under what conditions can those mechanisms and capabilities be maintained, revised or reconstructed endogenously?

## Why it is a question

"Does competent agency entail a world model?" changes meaning with what
"world model" and "having" mean. NOTE-136, on Safron et al., already
separates three senses: information about the world, representation of
causal structure, and causal prediction serving agency. The Richens et al.
result adds a sense that fits none of the three. The owner's review
distinguished five:

| notion | what is attributed | what would establish it |
|---|---|---|
| explanatory world model | a model an observer uses to explain the behaviour | its predictive usefulness to the observer |
| behaviourally encoded world model | dynamics recoverable from the agent's full policy | an identification theorem over a stated family of behavioural queries (CLAIM-tmp4htg4) |
| world-modeling competence | the organization's ability to answer predictive or causal questions with its actual resources | accurate answers to held-out queries within budget and deadline |
| realized world-model mechanism | an internal arrangement implementing predictive dynamics | architectural and causal evidence, ideally interventions that discriminate implementations (CLAIM-tmph29mx) |
| self-maintaining world-modeling organization | machinery that maintains and revises predictive competence and its own diagnostics | recovery and revision after changes to the world and to the machinery |

Four things are kept apart:

  behavioural recoverability ≠ internally accessible predictive capability
  ≠ mechanistically realized representation ≠ self-maintained and
  revisable modeling capacity.

**Recoverable is not available.** Richens et al.'s result is a map from
the whole goal-conditioned policy to the transition function, run by an
external algorithm over counterfactual goal queries. It does not show
three things:
- that the agent can produce the model on demand;
- that the agent simulates with it;
- that the agent can update it when wrong.

What an investigator can recover from an agent is not what the agent can
recover from itself. That is the record's legibility distinction
(TERM-064), turned on agency.

**Four counterexamples** show the notions come apart. They are not levels
of one scale:
- **A reactive controller.** It avoids obstacles from immediate feedback
  and cannot say where obstacles would have been on other paths, so it has
  control without the query competence. Brooks's robots are the standing
  case (THEORY-689).
- **A full goal-conditioned lookup policy.** It encodes the dynamics in
  Richens et al.'s sense, but has no affordable procedure to extract them
  for arbitrary queries.
- **An unused simulator.** It is an explicit model that the operative
  controller never consults: a mechanism without a contribution to
  present agency.
- **A distributed predictive controller.** It answers many
  action-conditioned queries through specialized processes, with no
  central latent-state simulator: competence without a unitary model.

**As an organizational achievement** (TERM-086), world-modeling has three
forms:
- **episodic:** predicting an outcome correctly once;
- **dispositional:** reliably answering a declared family of queries;
- **reproductive:** maintaining and rebuilding the machinery that makes
  those answers possible.

Revising the modeling repertoire is a fourth thing, distinct from
reproduction. An organization can reproduce a mistaken model indefinitely.
Another can revise its model accurately using computation supplied from
outside. So model maintenance and model corrigibility can come apart. A
system can also be corrigible about its task policy without a rich world
model, swapping one local control rule for another. This is the
partially ordered space of achievements in CLAIM-474.

Four achievements are distinct:
- having a predictive repertoire;
- recognizing that it is inadequate;
- reconstructing its realization;
- revising the questions it can answer.

The last ties world-modeling to the record's frontier of inquiry
(QUESTION-285).

## What would count as an answer

For stated goal and query families:
- which query capabilities competence implies, as theorems or
  counterexamples;
- which of those an agent of stated resources can exercise;
- which require a distinct internal mechanism, shown by interventions that
  discriminate implementations matched in behaviour;
- for each, whether the organization can maintain, revise or rebuild it
  after damage.

The proposed study CASE-tmp1a9u5 is one route.
