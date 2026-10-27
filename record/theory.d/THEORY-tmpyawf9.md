---
status: Proposed
promote_when: >-
  A quantitative test that a behaviour picked out as one (one contrast
  family, or one cluster of next-token predictions) is carried by more than
  one separable mechanism: in a feature circuit, ablating each pathway
  alone removes only part of the behaviour, ablating both removes nearly
  all, and the two pathways have disjoint inputs on inputs constructed to
  engage one and not the other; or the same shown across several
  behaviours, in more than one model, scored by an analyst who did not
  annotate the circuit. It is refuted if such pathways turn out redundant
  copies of one mechanism, or if one carries nearly all the effect. More
  annotated circuit diagrams cannot settle it: that is the evidence it
  rests on.
title: 'In a language model, a behaviour that looks like one mechanism, whether picked out by one contrast or by one cluster of next-token predictions, is often carried by several distinct pathways of sparse features that converge on the output without fully intersecting, as in Pythia-70M''s agreement across a relative clause, its prediction of "to" before an infinitival object, and its incrementing of sequences'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed Proposed from NOTE-tmpr0gdc, as the reading of the paper's
    annotated circuits that THEORY-tmpuogp2 leaves out (ADR-047 v4). The
    evidence is the authors' annotation of three circuits (and Gemma's for
    agreement), at thresholds chosen to keep annotation manageable, with no
    pathway-level ablation.
tags:
- representation-learning
- causality
date: '2026-10-26'
source:
- LIT-tmp5b0z9
extends:
- THEORY-tmpuogp2
summary: >-
  Marks et al. (2025), [LIT-tmp5b0z9](../literature.d/LIT-tmp5b0z9.md), read in [NOTE-tmpr0gdc](../notes.d/NOTE-tmpr0gdc.md): §3.3, §5 and
  Appendix C. Agreement across a relative clause: subject-number features
  promote verb forms directly, and a second pathway carries the number to
  the clause's end through PP/RC boundary features. Cluster 475: one
  mechanism detects verbs and adjectives that take infinitival objects,
  another nominal objects before an object complement. Cluster 382:
  general succession features and token-specific induction features.
  "While the clusters … seem at first to each represent a single
  mechanism, circuit-level analysis reveals in both cases a union of
  distinct mechanisms."
---
<!-- inactive-ok-file: CLAIM-tmpwr001 — Proposed; the claim this bears on, cited as open -->
# THEORY-tmpyawf9: In a language model, a behaviour that looks like one mechanism, whether picked out by one contrast or by one cluster of next-token predictions, is often carried by several distinct pathways of sparse features that converge on the output without fully intersecting, as in Pythia-70M's agreement across a relative clause, its prediction of "to" before an infinitival object, and its incrementing of sequences

## Source

Marks et al. (2025), [LIT-tmp5b0z9](../literature.d/LIT-tmp5b0z9.md), read in full in [NOTE-tmpr0gdc](../notes.d/NOTE-tmpr0gdc.md): §3.3
and Figure 4, §5 and Figure 5, and Appendix C (Figures 7–18, from captions
and text).

## What is asserted

That behaviours are typically unions of mechanisms at the feature level,
so that a behaviour's "circuit" is an arrangement of pathways rather than
one chain. The authors make the point of their two clusters, and their
agreement circuits have the same shape.

## What the record holds toward it

- **Agreement across a relative clause** (Pythia-70M, 86 nodes; Gemma-2-2B,
  223 nodes; faithfulness 0.21 each): a direct pathway from
  subject-number features to verb-form features, and a second that moves
  the number to the end of the clause through boundary detectors; Gemma
  adds noun-phrase number trackers.
- **"To" as an infinitival object** (cluster 475, Pythia-70M): two
  mechanisms, one on verbs, participles and predicate adjectives that take
  infinitival objects, one on nominal objects before an object complement,
  which "both influence the output in layer 5 without fully intersecting".
- **Incrementing sequences** (cluster 382): general succession features
  in layer-3 attention and narrow induction features for specific tokens,
  composing into a layer-5 feature that increments "3" to "4".
- **Against or qualifying.** The circuits are small, chosen at thresholds
  that keep annotation manageable, and the agreement circuits recover only
  0.21 of the behaviour. No pathway was ablated on its own. The
  annotations are the authors'.

## What it would take

See promote_when.

## Connections

- **[CLAIM-tmpwr001](../claims.d/CLAIM-tmpwr001.md).** If behaviours are unions of feature pathways, then
  what does the work is an organization of features, which is the claim's
  thesis transposed to a network.
- **[QUESTION-tmpivbso](../questions.d/QUESTION-tmpivbso.md).** A developmental account would have to track
  pathways, not features: whether the two agreement pathways form
  together or one after the other.
- **[THEORY-tmp8cat0](THEORY-tmp8cat0.md).** Induction at feature level comes in token-specific
  pieces composed with succession, where Olsson et al. found heads.
