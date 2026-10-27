---
status: Proposed
promote_when: >-
  Evidence that separates storage from editability. For instance: the
  layer where causal tracing finds a fact's effect predicts, fact by fact,
  where an edit of that fact succeeds, and edits at layers tracing does not
  implicate fail; or ablating or perturbing the identified mid-layer MLP
  directions on clean (uncorrupted) inputs removes the fact while sparing
  others, with a control showing that the effect is not carried by a
  direction in the null space of the output matrix. Refuted if edits of
  equal quality are available at layers that tracing does not implicate,
  or if a fact's recall survives removing its supposed key–value pair.
  More successful rank-one edits cannot settle it: by Makelov et al.'s
  Lemma D.2, such an edit exists for any one-dimensional fact patch.
title: 'In autoregressive transformer language models, factual associations are stored in middle-layer MLP modules as linear key–value memories: the MLP takes a key encoding the subject at its last token and returns a value encoding its attributes, which late attention moves to the prediction, and any middle layer could store a given fact equally, as Meng, Bau, Andonian and Belinkov propose'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed Proposed from NOTE-tmp0p8a7, the reading of Meng et al. (2022) in
    full, as the hypothesis the paper draws from what it measured
    (THEORY-tmpom5gw). The record already holds the argument that the
    edits do not establish it (LIT-968).
tags:
- representation-learning
- causality
date: '2026-10-26'
source:
- LIT-tmpajpeb
summary: >-
  Meng et al. (2022), [LIT-tmpajpeb](../literature.d/LIT-tmpajpeb.md), read in [NOTE-tmp0p8a7](../notes.d/NOTE-tmp0p8a7.md), §2.3 and §3:
  "the localized factual association hypothesis". It localizes recall
  along three dimensions, "(i) in the MLP modules (ii) at specific middle
  layers (iii) and specifically at the processing of the subject's last
  token", and conjectures "that any fact could be equivalently stored in
  any one of the middle MLP layers". The support is causal tracing and the
  success of rank-one edits at the traced site.
---

# THEORY-tmpvugrm: In autoregressive transformer language models, factual associations are stored in middle-layer MLP modules as linear key–value memories: the MLP takes a key encoding the subject at its last token and returns a value encoding its attributes, which late attention moves to the prediction, and any middle layer could store a given fact equally, as Meng, Bau, Andonian and Belinkov propose

## Source

Meng et al. (2022), [LIT-tmpajpeb](../literature.d/LIT-tmpajpeb.md), read in full in [NOTE-tmp0p8a7](../notes.d/NOTE-tmp0p8a7.md).

## What is asserted

A mechanism, not a measurement: mid-layer MLPs at the subject's last token
act as linear associative memories, W_proj k ≈ v, from a subject key to an
attribute value; "middle layer MLP outputs accumulate information, then
the summed information is copied to the last token by attention at high
layers"; and, from Zhao et al.'s finding that BERT's layers can be
reordered, "there is no further special role for the particular choice or
arrangement of individual layers in the middle range".

## What the record holds toward it

- **For:** the traces and edits of [THEORY-tmpom5gw](THEORY-tmpom5gw.md). Restoring mid-layer
  MLP outputs at the last subject token recovers recall; editing there
  generalizes and stays specific; editing late attention only regurgitates.
- **Against the inference:** Makelov et al. ([LIT-968](../literature.d/LIT-968.md), [THEORY-282](THEORY-282.md)). Fact
  patches in GPT2-XL's MLPs found by distributed alignment search depend
  on the null space of W_out, the illusion's signature; any such patch has
  a rank-one edit with the same output at that token (their Lemma D.2);
  and ROME edits are approximated by subspace interventions across layers
  20–35. An edit at a layer can work because the layer can write the
  needed output, whether or not it holds the fact.
- **Untested:** the conjecture that any middle layer could hold any fact.

## Why it stays Proposed

The paper's own warrant for "how" as well as "where" is that edits at the
traced site work: "This evidence suggests that we have an accurate
understanding not only of where factual associations are stored, but also
how." That step is the one [LIT-968](../literature.d/LIT-968.md) shows does not follow. The tracing
result is about sufficiency of restored states in a noised run, not about
where recall happens in a clean one.

## What would confirm or reject it

The promote_when above.
