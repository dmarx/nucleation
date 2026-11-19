---
status: Proposed
title: 'Geiger and colleagues define a high-level causal model as a constructive abstraction of a network when, under an alignment that partitions the network''s variables into cells mapped onto high-level variables, translating the network''s solutions under each aligned intervention gives the high-level model''s solutions under the corresponding intervention, and they test this with interchange interventions that set aligned variables to the values a different source input would give, scored as interchange intervention accuracy'
version: 1
source:
- LIT-tmp6x1cq
tags:
- causality
- representation-learning
date: '2026-11-19'
bears_on:
- QUESTION-tmpcb0bf
- QUESTION-tmpex36a
promote_when: >-
  The record checks Definitions 25, 31, 33, 44, 46 and 48 against the
  paper and reproduces the handcrafted hierarchical-equality example
  (§2.6) as an exact constructive abstraction
summary: >-
  From the reading of LIT-tmp6x1cq in NOTE-tmp1nqoj. Geiger, Ibeling, Zur,
  Chaudhary et al. (2025), arXiv 2301.04709, published in JMLR 26 (2025).
  It sets out causal abstraction as a foundation for mechanistic
  interpretability. A high-level algorithm abstracts a network when, under
  an alignment partitioning the network's variables into cells mapped onto
  the algorithm's variables, intervening and then translating commutes
  with translating and then intervening. This is tested by interchange
  interventions that patch in values from a source input, distributed ones
  in rotated coordinates, and scored by interchange intervention accuracy.
  Interventions are generalized to "interventionals" so distributed
  features can be targeted, and many interpretability methods are recast
  in these terms. Here because A15 named it as the interventional
  criterion in QUESTION-tmpcb0bf; it complements the held approximate
  causal abstraction (LIT-1310) and DAS (LIT-1551), and THEORY-1002's
  random-network control applies to it. Skimmed for its definitions; read
  in its NOTE.
---

# THEORY-tmp1cus0: Geiger and colleagues define a high-level causal model as a constructive abstraction of a network when, under an alignment that partitions the network's variables into cells mapped onto high-level variables, translating the network's solutions under each aligned intervention gives the high-level model's solutions under the corresponding intervention, and they test this with interchange interventions that set aligned variables to the values a different source input would give, scored as interchange intervention accuracy

## The account

A causal model is an exact transformation of another under a map of total settings τ and a map of interventions ω when τ of the low-level solutions under each intervention equals the high-level solutions under its image (Definition 25). An alignment partitions the low-level variables into cells, one per high-level variable plus a forgotten cell, with partial surjective maps from cell values to high-level values (Definition 31). Constructive abstraction is exact transformation under the maps the alignment induces (Definition 33). It decomposes into marginalization, variable merge and value merge. An interchange intervention runs the network on a base input with aligned variables fixed to the values they take on a source input (Definition 44). A distributed one does this in translated, for example rotated, coordinates (Definition 46). Interchange intervention accuracy is the fraction of such interventions on which network and algorithm agree on outputs (Definition 48). It is one instance of graded, approximate abstraction (Definition 41). Because the alignment's intermediate values are fixed by the inputs that realize them, only interventions to realized values are tested (Remark 47).

## What it does not show

- How to find an alignment, or that a found one is not an artefact of search. The record's THEORY-1002 shows that distributed alignment search reaches above-chance accuracy on frozen random networks.
- Which similarity, distribution and statistic make graded faithfulness adequate for a given claim.
- The skimmed sections' unification of specific methods (patching, ablation, scrubbing, SAEs, steering), which this reading does not assess.
