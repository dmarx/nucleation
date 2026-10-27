---
number: 1011
status: Rejected
status_note: Hase et al. (LIT-1578, THEORY-1024) meet this entry's own refutation clause for its localization part, in GPT-J on 652 CounterFact facts. ROME rewrites a fact at over 96% at every layer but the last, and the per-fact tracing effect adds at most 3.2 points of R² to edit success. The conjecture that any middle layer could store a fact equally was split out to THEORY-tmpanm57 and stays Proposed
formerly:
- THEORY-tmpvugrm
promote_when: >-
  To be reinstated, the localization part needs a clean-run localization,
  not causal tracing on noised inputs, whose per-fact layer predicts
  where an edit of that fact succeeds, with edits at other layers
  failing. Ablating the identified mid-layer MLP directions on clean
  inputs would also have to remove the fact while sparing others, with a
  control against a direction in the null space of the output matrix.
  The refuter this entry named is met: Hase et al. (LIT-1578,
  THEORY-1024) find edits of equal quality at layers that tracing does
  not implicate. More successful rank-one edits cannot reinstate it
  (Makelov et al.'s Lemma D.2).
title: 'In autoregressive transformer language models, factual associations are stored in middle-layer MLP modules as linear key–value memories: the MLP takes a key encoding the subject at its last token and returns a value encoding its attributes, which late attention moves to the prediction, and any middle layer could store a given fact equally, as Meng, Bau, Andonian and Belinkov propose'
version: 3
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
    2026-10-27 as LIT-1578, meet this entry's own refutation
    clause for its localization part; the conjecture that any middle
    layer could store a fact is not refuted. Geva et al. and MEMIT,
    also now held, are placed. Status and title unchanged; the
    disposition is left for the owner.
- version: 3
  date: '2026-10-27'
  note: >-
    Rejected at the owner's decision (2026-10-27, "make em so"), on the
    note of version 2. The localization part met the entry's own
    refutation clause (Hase et al., THEORY-1024). Rejected, not
    Superseded, because nothing replaces that claim. The conjecture
    that any middle layer could store a fact equally is split out to
    THEORY-tmpanm57, Proposed, under ADR-047's rule on dropped claims
    (kind 1). The promote_when now states what would reinstate the
    entry. Title and body are unchanged.
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
<!-- inactive-ok-file: THEORY-1026 — Proposed; Hase et al.'s account of why tracing and editing come apart, cited beside the conjecture it resembles -->
<!-- inactive-ok-file: THEORY-tmpanm57 — Proposed; the conjecture split out of this entry when it was rejected -->

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

**Hase et al. ([LIT-1578](../literature.d/LIT-1578.md), [NOTE-1194](../notes.d/NOTE-1194.md), [THEORY-1024](THEORY-1024.md)).** The
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
could store a fact", filed Proposed as [THEORY-1026](THEORY-1026.md), and the result
is if anything friendly to it.

**Status left for the owner.** Under [ADR-047](../decisions.d/ADR-047.md) the result would support a
disposition of split (the localization claim against the
equal-storage conjecture) or needs-correction, rather than a flat
rejection; which, if any, is the owner's decision, and this note changes
neither the status nor the title. The "Untested" line under "What the
record holds toward it" now reads, for the conjecture, as tested
indirectly and not refuted; and the localization part has a measured
Against case beside [LIT-968](../literature.d/LIT-968.md)'s argument.

**Geva et al. ([LIT-1576](../literature.d/LIT-1576.md), [NOTE-1200](../notes.d/NOTE-1200.md)).** The key–value reading this
account takes from Geva et al. is borrowed as an idea, not as a form.
Geva's memories are unit-level: each of a feed-forward layer's hidden
units has a key (a row of the input matrix) and a value (a row of the
output matrix), and the values promote next tokens ([THEORY-1033](THEORY-1033.md),
measured in one WikiText-103 model). ROME's memory is matrix-level: the
whole output matrix W_proj as a linear associative memory keyed by an
activation vector, holding a subject–attribute fact. Geva supports this
account only at the level of "MLPs can be read as memories".

**MEMIT ([LIT-1582](../literature.d/LIT-1582.md), [NOTE-1197](../notes.d/NOTE-1197.md), [THEORY-1031](THEORY-1031.md))** spreads an edit
over layers 3–8 of GPT-J and inserts 10,000 facts at once. It adds no
support toward promotion: its layer range is chosen from averaged traces,
and its ablations compare averaged ranges, not facts.

## Note of 2026-10-27 (later): rejected, and the conjecture split out

At the owner's decision on the note above, this entry is Rejected. Its
defining claim is that the middle layers causal tracing implicates are
where a fact is stored, so that editing there succeeds and editing
elsewhere does not. That claim met the refutation clause the entry wrote
for itself: Hase et al. ([LIT-1578](../literature.d/LIT-1578.md), [THEORY-1024](THEORY-1024.md)) find edits of equal
quality at layers tracing does not implicate.

The entry was also inconsistent with itself, which is why it is split
rather than simply rejected. Its title includes Meng et al.'s conjecture
that "any middle layer could store a given fact equally", and that
conjecture predicts exactly the result the promote_when counted as a
refutation. The conjecture is not refuted, and the source asserts it, so
under [ADR-047](../decisions.d/ADR-047.md) (kind 1) it is filed as its own Proposed entry,
[THEORY-tmpanm57](THEORY-tmpanm57.md). Its promote_when carries over this entry's clean-input
ablation test and adds a control for edits that create an association
wherever they are made ([LIT-968](../literature.d/LIT-968.md)). Hase et al.'s own account, that
localizing and editing are different questions, stays [THEORY-1026](THEORY-1026.md).

What stands from the paper is the measurement, [THEORY-998](THEORY-998.md): the traces and
the edits as measured. Only the inference from them to localized storage
is rejected.

