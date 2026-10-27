---
number: 1026
status: Proposed
formerly:
- THEORY-tmpiz2n7
promote_when: >-
  A test that separates the two questions directly. For instance: in a
  model where a fact's tracing effect is confined to a few layers, an edit
  at a layer outside them is shown to work by writing into the residual
  stream a signal that later layers read in place of the original (the
  original's contribution still present, and outweighed), with that
  override mechanism measured, not inferred from the edit's success; and
  a localization on the clean run, not on a noised one, that does predict
  where edits work, or is shown not to. Refuted if, on a localization
  method that measures the clean computation, per-fact localization does
  predict per-fact edit success, so that the gap was causal tracing's and
  not a general difference between localizing and editing. More
  regressions of edit success on tracing cannot settle it: that is the
  evidence it already rests on.
title: 'In transformer language models, locating where a forward pass carries information about a fact and finding where a weight edit best changes the expressed fact are different questions, because an edit at one layer can override information accumulated across other layers, so that many layers could hold a fact and some happen to, as Hase, Bansal, Kim and Ghandeharioun propose'
version: 1
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Filed Proposed from NOTE-1194, the reading of Hase et al.
    (2023) in full, as the account the paper offers in §6 for its
    measured result (THEORY-1024). The paper offers it as a
    hypothesis and leaves it "to future work".
tags:
- representation-learning
- causality
date: '2026-10-27'
source:
- LIT-1578
extends:
- THEORY-1024
summary: >-
  Hase et al. (2023), [LIT-1578](../literature.d/LIT-1578.md), read in [NOTE-1194](../notes.d/NOTE-1194.md), §6: "Causal
  Tracing answers a question about where factual information is carried in
  representations in a Transformer forward pass, and this question turns
  out to be a different question than the editing question of where is
  best to intervene"; and, for why edits work where facts are not traced,
  "Many layers could store a fact, and it happens that some do". The
  authors note that this would be surprising, since layers cannot be
  swapped freely.
---
<!-- inactive-ok-file: THEORY-1011 — Proposed; the storage hypothesis this account bears on, cited as open -->

# THEORY-1026: In transformer language models, locating where a forward pass carries information about a fact and finding where a weight edit best changes the expressed fact are different questions, because an edit at one layer can override information accumulated across other layers, so that many layers could hold a fact and some happen to, as Hase, Bansal, Kim and Ghandeharioun propose

## Source

Hase et al. (2023), [LIT-1578](../literature.d/LIT-1578.md), read in full in [NOTE-1194](../notes.d/NOTE-1194.md), §6.

## What is asserted

Two things. First, a conceptual separation: causal tracing measures
where the information that restores a fact is carried in one forward
pass; editing asks where a weight change will alter the fact the model
expresses; and the answer to one need not be the answer to the other.
Second, a mechanism for the gap: information about a fact accumulates
across layers, and a single-layer edit, before or after that range, can
override what was accumulated. Hence "many layers could store a fact, and
it happens that some do".

## What the record holds toward it

- **For the separation:** the measured result, [THEORY-1024](THEORY-1024.md). Edit
  success does not follow per-fact tracing, and the one setting where it
  does a little (Fact Forcing) is the one that edits on tracing's own
  noised input.
- **For the mechanism, from another direction:** Makelov et al.
  ([LIT-968](../literature.d/LIT-968.md), [THEORY-282](THEORY-282.md)). Any one-dimensional fact patch in an MLP has a
  rank-one edit with the same output at that token, and their fact patches
  work through the null space of W_out. So an edit can produce the output
  without the layer holding the fact, which is one way an override could
  work.
- **Against the mechanism, as the authors note:** layers cannot be
  reordered without damage (Zhao et al., cited), so it "should matter
  where information enters the residual stream". ROME cites the same
  paper for the opposite point, that the middle layers are
  interchangeable ([THEORY-1011](THEORY-1011.md)).
- **Untested:** the override itself. No experiment in the paper shows an
  edit outweighing a fact's original contribution in later layers.

## Why it stays Proposed

The separation is a reading of one negative result, with one localization
family (denoising and zeroing) and one kind of edit. The mechanism is a
hypothesis the authors offer and do not test. A localization that measures
the clean computation might still predict edits, in which case the gap is
the noised-run method's, not a general one.

## What would confirm or reject it

The promote_when above.
