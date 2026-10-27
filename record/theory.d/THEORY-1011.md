---
number: 1011
status: Proposed
formerly:
- THEORY-tmpvugrm
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
version: 2
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed Proposed from NOTE-1166, the reading of Meng et al. (2022) in
    full, as the hypothesis the paper draws from what it measured
    (THEORY-998). The record already holds the argument that the
    edits do not establish it (LIT-968).
- version: 2
  date: '2026-10-27'
  note: >-
    A dated note added: Hase et al. (2023), registered and read on
    2026-10-27 as LIT-tmpg22tp, meet this entry's own refutation
    clause for its localization part; the conjecture that any middle
    layer could store a fact is not refuted. Geva et al. and MEMIT,
    also now held, are placed. Status and title unchanged; the
    disposition is left for the owner.
tags:
- representation-learning
- causality
date: '2026-10-26'
source:
- LIT-1536
summary: >-
  Meng et al. (2022), [LIT-1536](../literature.d/LIT-1536.md), read in [NOTE-1166](../notes.d/NOTE-1166.md), §2.3 and §3:
  "the localized factual association hypothesis". It localizes recall
  along three dimensions, "(i) in the MLP modules (ii) at specific middle
  layers (iii) and specifically at the processing of the subject's last
  token", and conjectures "that any fact could be equivalently stored in
  any one of the middle MLP layers". The support is causal tracing and the
  success of rank-one edits at the traced site.
---
<!-- inactive-ok-file: THEORY-tmpiz2n7 — Proposed; Hase et al.'s account of why tracing and editing come apart, cited beside the conjecture it resembles -->

# THEORY-1011: In autoregressive transformer language models, factual associations are stored in middle-layer MLP modules as linear key–value memories: the MLP takes a key encoding the subject at its last token and returns a value encoding its attributes, which late attention moves to the prediction, and any middle layer could store a given fact equally, as Meng, Bau, Andonian and Belinkov propose

## Source

Meng et al. (2022), [LIT-1536](../literature.d/LIT-1536.md), read in full in [NOTE-1166](../notes.d/NOTE-1166.md).

## What is asserted

A mechanism, not a measurement: mid-layer MLPs at the subject's last token
act as linear associative memories, W_proj k ≈ v, from a subject key to an
attribute value; "middle layer MLP outputs accumulate information, then
the summed information is copied to the last token by attention at high
layers"; and, from Zhao et al.'s finding that BERT's layers can be
reordered, "there is no further special role for the particular choice or
arrangement of individual layers in the middle range".

## What the record holds toward it

- **For:** the traces and edits of [THEORY-998](THEORY-998.md). Restoring mid-layer
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

## Note of 2026-10-27: Hase et al. meet the refutation clause for the localization part

Three works this entry leans on or names were registered and read on
2026-10-27, at the owner's request ("get started on the seven works and
markov IBP").

**Hase et al. ([LIT-tmpg22tp](../literature.d/LIT-tmpg22tp.md), [NOTE-tmpg0dnu](../notes.d/NOTE-tmpg0dnu.md), [THEORY-tmpg87ki](THEORY-tmpg87ki.md)).** The
promote_when above says this account is "refuted if edits of equal
quality are available at layers that tracing does not implicate". Hase,
Bansal, Kim and Ghandeharioun report exactly that, in GPT-J on 652
CounterFact facts the model knows:

- ROME's mean rewrite score is 99% at layer 6 and above 96% at every
  edited layer but the last (28), including layers where causal tracing
  does not place the fact.
- For ROME at layer 6, the per-fact tracing effect and the rewrite score
  correlate at ρ = −0.13. A regression of edit success on the edit layer
  alone gives R² 0.947; adding the per-fact tracing effect gives 0.948, a
  gain of 0.1 point.
- Across ROME, MEMIT and constrained fine-tuning on one or five layers,
  and five editing objectives, the largest gain from tracing is 3.2 points
  of R² (fine-tuning on five layers under Fact Forcing, the one objective
  that edits on the noised input tracing uses).

So the localization part of this account ("stored in middle-layer MLP
modules … at the subject's last token", read as the traced site being
where the fact is) meets the account's own refutation condition, for the
rewrite score, in the one model and dataset measured (GPT-2 XL and zsRE
are reported to agree). The layer still explains most of the variance,
and ROME is best on average near where tracing peaks on average
([THEORY-998](THEORY-998.md) is not contradicted). What fails is the per-fact link from
trace to edit.

The conjecture that "any middle layer could store a given fact equally" is
not refuted. It is close to Hase et al.'s own reading that "many layers
could store a fact", filed Proposed as [THEORY-tmpiz2n7](THEORY-tmpiz2n7.md), and the result
is if anything friendly to it.

**Status left for the owner.** Under [ADR-047](../decisions.d/ADR-047.md) the result would support a
disposition of split (the localization claim against the
equal-storage conjecture) or needs-correction, rather than a flat
rejection; which, if any, is the owner's decision, and this note changes
neither the status nor the title. The "Untested" line under "What the
record holds toward it" now reads, for the conjecture, as tested
indirectly and not refuted; and the localization part has a measured
Against case beside [LIT-968](../literature.d/LIT-968.md)'s argument.

**Geva et al. ([LIT-tmpe8ypo](../literature.d/LIT-tmpe8ypo.md), [NOTE-tmpvd0mr](../notes.d/NOTE-tmpvd0mr.md)).** The key–value reading this
account takes from Geva et al. is borrowed as an idea, not as a form.
Geva's memories are unit-level: each of a feed-forward layer's hidden
units has a key (a row of the input matrix) and a value (a row of the
output matrix), and the values promote next tokens ([THEORY-tmpwtgvz](THEORY-tmpwtgvz.md),
measured in one WikiText-103 model). ROME's memory is matrix-level: the
whole output matrix W_proj as a linear associative memory keyed by an
activation vector, holding a subject–attribute fact. Geva supports this
account only at the level of "MLPs can be read as memories".

**MEMIT ([LIT-tmpsrubd](../literature.d/LIT-tmpsrubd.md), [NOTE-tmpt77xq](../notes.d/NOTE-tmpt77xq.md), [THEORY-tmpukwxl](THEORY-tmpukwxl.md))** spreads an edit
over layers 3–8 of GPT-J and inserts 10,000 facts at once. It adds no
support toward promotion: its layer range is chosen from averaged traces,
and its ablations compare averaged ranges, not facts.
