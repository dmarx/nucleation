---
status: Proposed
promote_when: >-
  Causal evidence in large transformers with MLPs, not co-occurrence:
  ablating or patching the induction heads (identified by the prefix-matching
  and copying definition) at checkpoints across and after the transition
  removes most of the in-context learning score, with interactions with MLP
  layers controlled for, for example by path patching. Or an architecture in
  which heads can compose but induction is blocked, which then shows no jump
  in a large model. It is refuted by a large model in which removing every
  induction head leaves most of the score, or in which non-induction
  composition heads formed in the same window account for more of it.
  Further co-occurrence across sizes, or more examples of abstract
  induction heads, cannot settle it: that is the evidence it already rests
  on.
title: 'In transformer language models of every size, including large ones with MLPs, induction heads, extended to fuzzy matching of similar tokens and abstract patterns, are the mechanism of most in-context learning, as Olsson et al. propose'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed Proposed from NOTE-tmpabelf, as the wider thesis that
    THEORY-tmp8cat0 leaves out (ADR-047 v4). The paper itself calls its
    evidence for this "preliminary and indirect".
tags:
- representation-learning
- learning-theory
date: '2026-10-26'
source:
- LIT-tmpe7b5o
extends:
- THEORY-tmp8cat0
summary: >-
  Olsson et al. (2022), [LIT-tmpe7b5o](../literature.d/LIT-tmpe7b5o.md), read in [NOTE-tmpabelf](../notes.d/NOTE-tmpabelf.md). The paper's
  thesis: circuits with the induction head's mechanism, matching
  "[A*][B*] … [A] → [B], where A* ≈ A and B* ≈ B are similar in some
  space", "implement most in-context learning in large models". For large
  models the authors grade their own evidence correlational (Argument 1),
  weakly interventional (Argument 2), plausibility (Argument 4) and
  analogy (Argument 6). Their strongest alternative is that other
  composition heads, formed in the same window, carry more of it above some
  size.
---
<!-- inactive-ok-file: THEORY-783 — Proposed; a neighbouring account, cited as open -->
# THEORY-tmpkd3fq: In transformer language models of every size, including large ones with MLPs, induction heads, extended to fuzzy matching of similar tokens and abstract patterns, are the mechanism of most in-context learning, as Olsson et al. propose

## Source

Olsson et al. (2022), [LIT-tmpe7b5o](../literature.d/LIT-tmpe7b5o.md), read in full in [NOTE-tmpabelf](../notes.d/NOTE-tmpabelf.md):
Arguments 1, 2, 4 and 6, the full-scale rows of the Model Analysis Table,
and the Discussion.

## What is asserted

That the circuit shown to carry in-context learning in small attention-only
models ([THEORY-tmp8cat0](THEORY-tmp8cat0.md)) carries most of it in large transformers too. In
large models the same heads that copy literal random sequences are taken to
do "fuzzy" or "nearest neighbor" completion over abstract representations,
such as translation and template matching.

## What the record holds toward it

- **Co-occurrence at every size.** In the full-scale series (4 to 40
  layers, 13M to 13B parameters) the score jumps in the same early window,
  induction heads form in it, and the after-score is about 0.4 nats at
  every size. There are 14 or 15 snapshots per model and no ablations.
- **One architectural intervention**, the smeared keys, run only at one and
  two layers.
- **Three heads in the 13B model** that are induction heads by the
  definition and also translate or match patterns. Anecdotal by design.
- **The mechanism** is reverse-engineered only for attention-only models.

[THEORY-tmp8cat0](THEORY-tmp8cat0.md) holds the small attention-only case as measured. Nothing in
the record measures the large case causally.

## Why it stays Proposed

The authors' own grading: "For small attention-only models, we present
strong, causal evidence; for larger models with MLPs, we present
correlational evidence." And their alternative: "If all 'composition heads'
form simultaneously during the phase change, then it's possible that above
some size, non-induction composition heads could together account for more
of the phase change and in-context learning improvement than induction
heads do."

## What would confirm or reject it

The promote_when above.
