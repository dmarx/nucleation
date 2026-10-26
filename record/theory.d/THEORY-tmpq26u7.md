---
status: Proposed
promote_when: >-
  An evaluation of attribution patching with the softmax correction
  against exhaustive single-node activation patching on transformer
  language models outside the Pythia family and above 12B parameters, on
  tasks and prompt distributions chosen independently of the method's
  authors, in which the nodes it ranks below its top K rarely have large
  effects: the cost of verified recall stays within a small multiple of
  the oracle's, or the subsampling diagnostic's upper bound on missed
  effects is small relative to the top effects. It is refuted by such a
  model or task in which large-effect nodes routinely rank low, so that
  ordered verification costs about as much as unordered patching. More
  settings in Pythia cannot settle it, nor can comparisons in which the
  ground truth is not exhaustive patching.
title: 'For fine-grained nodes of transformer language models generally, attribution patching corrected for attention saturation is a reliable prefilter for activation patching: nodes it ranks low rarely have large single-node patching effects, so verifying nodes in its order finds the important ones at a small multiple of the cost of an oracle, as Kramár et al. expect'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed Proposed from NOTE-tmpz2cvc, as the wider claim that
    THEORY-tmpo1u9l leaves out (ADR-047 v4). The authors state it as an
    expectation: "we think it likely that our results on the Pythia model
    family will transfer to other LLM families", but "cannot rule out
    qualitatively different behavior without further evidence".
tags:
- representation-learning
- causality
date: '2026-10-26'
source:
- LIT-tmp4de8g
extends:
- THEORY-tmpo1u9l
summary: >-
  Kramár, Lieberum, Shah & Nanda (2024), LIT-tmp4de8g, read in
  NOTE-tmpz2cvc. The measured case is four Pythia models, three prompt
  pairs and two small distributions. The paper's own diagnostic is what
  would let a single new setting be checked without exhaustive patching.
---
# THEORY-tmpq26u7: For fine-grained nodes of transformer language models generally, attribution patching corrected for attention saturation is a reliable prefilter for activation patching: nodes it ranks low rarely have large single-node patching effects, so verifying nodes in its order finds the important ones at a small multiple of the cost of an oracle, as Kramár et al. expect

## Source

Kramár, Lieberum, Shah and Nanda (2024), LIT-tmp4de8g, read in full in
NOTE-tmpz2cvc: §5.1 (limitations) and §5.4 (recommendations).

## What is asserted

That what THEORY-tmpo1u9l measured in Pythia holds for transformer
language models of other families and larger sizes, on tasks beyond the
five tried: gradient-ordered verification, with the softmax corrected,
misses few large-effect nodes.

## What the record holds toward it

- THEORY-tmpo1u9l (Active): four Pythia sizes, five settings.
- The failure modes are understood mechanistically (saturation,
  cancellation), which is a reason to expect transfer and also names
  where it could fail: models with sharper attention or more cancellation.
- Nothing in the record measures another family.

## What would confirm or reject it

The promote_when above.
