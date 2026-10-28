---
number: 1039
status: Proposed
formerly:
- THEORY-tmpanm57
promote_when: >-
  A test on the clean computation that tells distributed storage apart
  from an edit that writes the association wherever it is made. For
  instance: for facts the model knows, ablating or perturbing candidate
  key–value directions in each of several middle-layer MLPs on clean
  (uncorrupted) inputs removes the fact from the model's output while
  sparing other facts, with a control showing that the effect is not
  carried by a direction in the null space of the output matrix; and,
  for the "equally" clause, that the layers where a fact can be removed
  in this way are not predicted, fact by fact, by any one layer. Refuted
  if the fact survives every such ablation in the middle layers, or if a
  clean-run localization picks out, fact by fact, a single layer whose
  ablation alone removes it. More successful edits cannot settle it: an
  edit's success at a layer shows that the layer can write the needed
  output, not that it held the fact (Makelov et al.'s Lemma D.2).
title: 'In autoregressive transformer language models, factual associations are recalled through middle-layer MLP modules acting as key–value memories, and any fact could be stored equally in any one of the middle MLP layers, as Meng, Bau, Andonian and Belinkov conjecture'
version: 1
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Filed Proposed at the owner's decision (2026-10-27, "make em so"),
    from the rejection of THEORY-1011. THEORY-1011 bundled the localized
    factual association hypothesis with this conjecture, and Hase et al.
    (THEORY-1024) met its refutation clause for the localization part
    only. Under ADR-047's rule on where a narrowing's dropped claims go,
    this is kind 1, a generalization the source asserts, so it keeps
    the source's wording and gets its own entry. Its promote_when
    carries over THEORY-1011's clean-input ablation test and adds a
    control for edits that write an association wherever they are made.
tags:
- representation-learning
- causality
date: '2026-10-27'
source:
- LIT-1536
- LIT-1578
summary: >-
  Meng et al. (2022), [LIT-1536](../literature.d/LIT-1536.md), read in [NOTE-1166](../notes.d/NOTE-1166.md), §2.3: "we conjecture
  that any fact could be equivalently stored in any one of the middle MLP
  layers". It was one clause of [THEORY-1011](THEORY-1011.md), which is Rejected for its
  other part, the claim that the traced middle layers are where a fact
  is stored. Hase et al. (2023), [LIT-1578](../literature.d/LIT-1578.md), read in [NOTE-1194](../notes.d/NOTE-1194.md), measure
  edits succeeding at nearly every layer of GPT-J whatever tracing
  says ([THEORY-1024](THEORY-1024.md)). That is what this conjecture predicts, but it is
  not evidence of storage, since an edit can work wherever a layer can
  write the needed output ([LIT-968](../literature.d/LIT-968.md)).
---
<!-- inactive-ok-file: THEORY-1011 — Rejected; the entry this conjecture was split from, cited as its origin -->
<!-- inactive-ok-file: THEORY-1026 — Proposed; Hase et al.'s neighbouring account, cited as the nearest rival reading -->

# THEORY-1039: In autoregressive transformer language models, factual associations are recalled through middle-layer MLP modules acting as key–value memories, and any fact could be stored equally in any one of the middle MLP layers, as Meng, Bau, Andonian and Belinkov conjecture

## Source

Meng et al. (2022), [LIT-1536](../literature.d/LIT-1536.md), read in full in [NOTE-1166](../notes.d/NOTE-1166.md). Hase et al.
(2023), [LIT-1578](../literature.d/LIT-1578.md), read in full in [NOTE-1194](../notes.d/NOTE-1194.md), is the second source: it
measures what the conjecture predicts, though it does not establish it.

## What is asserted

Two things, both from Meng et al. §2.3. Mid-layer MLPs act as linear
associative memories from a subject key to an attribute value, and the
middle range has no privileged layer for a given fact: "any fact could
be equivalently stored in any one of the middle MLP layers". The paper
rests the second clause on Zhao et al.'s finding that BERT's layers can
be reordered.

It does not assert the claim [THEORY-1011](THEORY-1011.md) was rejected for: that the
middle layers where causal tracing peaks are where a given fact is
stored.

## What the record holds toward it

- **Consistent with it:** [THEORY-1024](THEORY-1024.md). In GPT-J, on 652 CounterFact
  facts, ROME rewrites a fact at over 96% at every layer but the last,
  and the per-fact tracing effect adds at most 3.2 points of R² to edit
  success once the edit layer is known.
- **Why that is not support:** [LIT-968](../literature.d/LIT-968.md) and [THEORY-282](THEORY-282.md). Any
  one-dimensional fact patch has a rank-one edit with the same output at
  that token, so an edit's success at a layer shows that the layer can
  write the output, not that it held the fact. Edits that work
  everywhere are what distributed storage predicts, and also what
  "edits create the association where they are made" predicts.
- **Nearest rival:** [THEORY-1026](THEORY-1026.md), Hase et al.'s account. Localizing and
  editing answer different questions, and "many layers could hold a
  fact and some happen to". It is weaker than "any … equally", and it
  rests on override, not storage.
- **Not yet tested:** no work in the record ablates candidate memories
  on clean inputs, layer by layer.

## Why it stays Proposed

Every piece of evidence for it so far is an edit, and edits cannot tell
storage from writing. The test it needs, a clean-run ablation layer by
layer, has not been run in any work the record holds.

## What would confirm or reject it

The promote_when above.
