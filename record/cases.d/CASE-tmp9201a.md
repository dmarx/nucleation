---
status: Proposed
title: 'A proposed study: small transformers trained on randomized subject–relation–object facts, with matched training worlds, measured across query variants, inference budgets, interventions and merges, to find whether apparent forgetting is loss, readdressing, interference or downstream suppression, and whether a model of the network''s response geometry predicts which associations come back under unseen queries, compute and interventions better than feature similarity, activation strength and attribution'
version: 1
standing: stipulated
kind: proposed-study
tags:
- representation-learning
- learning-theory
- anthology-candidate
date: '2026-11-15'
line:
- learned-structure
- realizability
bears_on:
- QUESTION-274
- QUESTION-275
- QUESTION-010
draws_on:
- THEORY-281
- THEORY-tmpi5d5l
- THEORY-tmp2ly83
- THEORY-tmpmapw3
- THEORY-tmp9rnyv
summary: >-
  A's design, assembled from A17, A21–A22, A25 and A26 of the
  continuation of the exchange "Explain String Theory" (2026-11-15). It
  joins the owner's questions on concept erasure, sleeper agents, the
  hologram, test-time compute and RL into one experiment. Not run.
  Proposed because the design is A's; adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-tmp6214r CLAIM-tmps7g72 CLAIM-tmpumro8 THEORY-tmpi5d5l THEORY-tmp2ly83 — Proposed or new; the construction and claims the design tests, and the erasure bound it uses -->

# CASE-tmp9201a: A proposed study: small transformers trained on randomized subject–relation–object facts, with matched training worlds, measured across query variants, inference budgets, interventions and merges, to find whether apparent forgetting is loss, readdressing, interference or downstream suppression, and whether a model of the network's response geometry predicts which associations come back under unseen queries, compute and interventions better than feature similarity, activation strength and attribution

## The design

- **Facts and worlds.** Imaginary entities with independently assigned
  attributes and some compositional relations, counterbalanced across
  training runs. Matched training worlds differ in one target association,
  so "the model retains f" has a counterfactual to be measured against.
- **Interventions.** A projection that erases one linear feature;
  closed-form linear erasure at one layer and across layers; cue remapping;
  a targeted parameter edit; merging in a second task vector; RL with a
  verifiable reward.
- **Readouts at each layer.** Answer margins over held-out query variants;
  linear and nonlinear probes, validated against matched worlds;
  activation patching; local transfer coefficients
  R(q) = vᵀ J_{L−1}(q)⋯J_ℓ(q) u, checked by finite interventions.
- **Budget axis.** Single sample, repeated sampling (coverage and
  delivery reported separately), self-consistency, verifier-guided search
  and extended reasoning, each with its cost ([CLAIM-tmps7g72](../claims.d/CLAIM-tmps7g72.md)).

## The outcomes it separates

| apparent forgetting | signature |
|---|---|
| readdressing | another cue recovers it; the response peak moves ([CASE-tmp6214r](CASE-tmp6214r.md)) |
| interference | removing distractors or competing contributions restores it |
| downstream suppression | internal readers and interventions find a signal blocked before the output |
| higher realization cost | the capability curve shifts to the right: recovered at a larger budget |
| loss | strong readers, other cues and interventions all fail, with every other source of the information controlled |

Recovery after an erasure, as Amnesic Probing ([THEORY-tmpi5d5l](../theory.d/THEORY-tmpi5d5l.md)) and
mechanistic shaping ([THEORY-tmp2ly83](../theory.d/THEORY-tmp2ly83.md)) observe, does not by itself show the original trace
survived. It may have been rebuilt from other retained information, which
[THEORY-281](../theory.d/THEORY-281.md)'s bound limits.

## What would count

The prediction must come before the recovery tests: which unseen queries,
budgets and interventions restore which associations. The test is against
static feature similarity, activation strength, attribution and plain
compute-scaling fits. If those predict as well, the response-geometry
account adds nothing ([CLAIM-tmpumro8](../claims.d/CLAIM-tmpumro8.md)).

## Its limits

Synthetic facts in small models. Natural facts have unknown training
histories, which this design avoids on purpose.
