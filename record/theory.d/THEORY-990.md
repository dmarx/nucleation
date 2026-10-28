---
number: 990
status: Proposed
formerly:
- THEORY-tmpkd3fq
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
version: 2
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed Proposed from NOTE-1173, as the wider thesis that
    THEORY-973 leaves out (ADR-047 v4). The paper itself calls its
    evidence for this "preliminary and indirect".
- version: 2
  date: '2026-10-27'
  note: >-
    A dated note added: the causal scrubbing induction result,
    registered and read on 2026-10-27, qualifies the small-model
    anchor this account argues from. Status unchanged.
tags:
- representation-learning
- learning-theory
date: '2026-10-26'
source:
- LIT-1538
extends:
- THEORY-973
summary: >-
  Olsson et al. (2022), [LIT-1538](../literature.d/LIT-1538.md), read in [NOTE-1173](../notes.d/NOTE-1173.md). The paper's
  thesis: circuits with the induction head's mechanism, matching
  "[A*][B*] … [A] → [B], where A* ≈ A and B* ≈ B are similar in some
  space", "implement most in-context learning in large models". For large
  models the authors grade their own evidence correlational (Argument 1),
  weakly interventional (Argument 2), plausibility (Argument 4) and
  analogy (Argument 6). Their strongest alternative is that other
  composition heads, formed in the same window, carry more of it above some
  size.
---
# THEORY-990: In transformer language models of every size, including large ones with MLPs, induction heads, extended to fuzzy matching of similar tokens and abstract patterns, are the mechanism of most in-context learning, as Olsson et al. propose

## Source

Olsson et al. (2022), [LIT-1538](../literature.d/LIT-1538.md), read in full in [NOTE-1173](../notes.d/NOTE-1173.md):
Arguments 1, 2, 4 and 6, the full-scale rows of the Model Analysis Table,
and the Discussion.

## What is asserted

That the circuit shown to carry in-context learning in small attention-only
models ([THEORY-973](THEORY-973.md)) carries most of it in large transformers too. In
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

- **An earlier statement, with no added evidence.** Elhage et al.'s
  framework ([LIT-1534](../literature.d/LIT-1534.md), [NOTE-1189](../notes.d/NOTE-1189.md)), written before the
  induction-heads paper, already calls induction heads "a central driver
  of in-context learning in language models of all sizes".
- **No test from attribution graphs.** Attribution graphs freeze
  attention patterns, so they cannot see an induction head's QK step.
  Circuit Tracing's Limitations section ([LIT-1552](../literature.d/LIT-1552.md), [NOTE-1185](../notes.d/NOTE-1185.md))
  says that on "Aunt Sally … Aunt" the graph shows only that "Sally"
  came earlier, "a kind of regression" against the attention-only
  analyses. The record's attribution-graph studies of a large
  model therefore neither support nor undercut this thesis.

[THEORY-973](THEORY-973.md) holds the small attention-only case as measured, and
[THEORY-977](THEORY-977.md) the two-layer model's mechanism in its weights. Nothing in
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

## Note of 2026-10-27: the small-model anchor, qualified

This account argues from the small attention-only case ([THEORY-973](THEORY-973.md),
[THEORY-977](THEORY-977.md)). Causal scrubbing's induction post ([LIT-1579](../literature.d/LIT-1579.md),
[NOTE-1196](../notes.d/NOTE-1196.md)), read on 2026-10-27, qualifies that anchor: in a two-layer
attention-only model, the textbook induction circuit accounts for only 35%
of the two induction heads' contribution on induction-favouring tokens,
and 86% needs three-token matching and three layer-0 heads that attend to
copies of the current token ([THEORY-1020](THEORY-1020.md)). Even where the mechanism is
best understood, "induction heads" as the textbook describes them are a
part of what those heads do. It adds no evidence about large models, so
the account stays Proposed.
