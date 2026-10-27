---
number: 1000
status: Proposed
formerly:
- THEORY-tmpq26u7
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
version: 2
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed Proposed from NOTE-1190, as the wider claim that
    THEORY-996 leaves out (ADR-047 v4). The authors state it as an
    expectation: "we think it likely that our results on the Pythia model
    family will transfer to other LLM families", but "cannot rule out
    qualitatively different behavior without further evidence".
- version: 2
  date: '2026-10-27'
  note: >-
    A dated note added: Nanda's post, registered and read on
    2026-10-27, gives the method author's own account of where
    attribution patching should fail (THEORY-tmp52c5a), compatible
    with this one. Status unchanged.
tags:
- representation-learning
- causality
date: '2026-10-26'
source:
- LIT-1531
extends:
- THEORY-996
summary: >-
  Kramár, Lieberum, Shah & Nanda (2024), [LIT-1531](../literature.d/LIT-1531.md), read in
  [NOTE-1190](../notes.d/NOTE-1190.md). The measured case is four Pythia models, three prompt
  pairs and two small distributions. The paper's own diagnostic is what
  would let a single new setting be checked without exhaustive patching.
---
<!-- inactive-ok-file: THEORY-tmp52c5a — Proposed; the method author's account, set beside this one -->
# THEORY-1000: For fine-grained nodes of transformer language models generally, attribution patching corrected for attention saturation is a reliable prefilter for activation patching: nodes it ranks low rarely have large single-node patching effects, so verifying nodes in its order finds the important ones at a small multiple of the cost of an oracle, as Kramár et al. expect

## Source

Kramár, Lieberum, Shah and Nanda (2024), [LIT-1531](../literature.d/LIT-1531.md), read in full in
[NOTE-1190](../notes.d/NOTE-1190.md): §5.1 (limitations) and §5.4 (recommendations).

## What is asserted

That what [THEORY-996](THEORY-996.md) measured in Pythia holds for transformer
language models of other families and larger sizes, on tasks beyond the
five tried: gradient-ordered verification, with the softmax corrected,
misses few large-effect nodes.

## What the record holds toward it

- [THEORY-996](THEORY-996.md) (Active): four Pythia sizes, five settings.
- The failure modes are understood mechanistically (saturation,
  cancellation), which is a reason to expect transfer and also names
  where it could fail: models with sharper attention or more cancellation.
- Nothing in the record measures another family.

## What would confirm or reject it

The promote_when above.

## Note of 2026-10-27: the method author's account

Nanda's post (LIT-tmpo09rn, NOTE-tmpxnucs), read on 2026-10-27, gives the
method author's own account of where attribution patching agrees and
disagrees with activation patching, filed Proposed as THEORY-tmp52c5a. Its
promote_when is compatible with this one's; it adds the size of a patch and
a node's depth in the circuit as conditions to vary. The estimate itself
is THEORY-tmpeqz27.
