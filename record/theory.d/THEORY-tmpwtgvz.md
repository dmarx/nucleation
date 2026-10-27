---
status: Active
title: 'In a 16-layer transformer language model trained on WikiText-103, the training prefixes that most activate a sampled feed-forward hidden unit share patterns that human annotators recognize, mostly shallow in layers 1–9 and semantic in layers 10–16; projected through the output embedding, a unit''s output weights put the next token of its top prefix first in up to about 3.5% of units in the upper layers and almost none below; and a layer''s top prediction differs from every unit''s in at least about 68% of examples'
version: 1
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Filed Active from NOTE-tmpvd0mr, the reading of Geva et al. (2021)
    in full. One study, but the title claims only what it measured in
    the one model studied, and nothing in the record contradicts the
    measurements (ADR-047 v3). The general reading of feed-forward layers
    as key–value memories is the Proposed THEORY-tmpt0fr3.
tags:
- representation-learning
date: '2026-10-27'
source:
- LIT-tmpe8ypo
summary: >-
  Geva et al. (2021), LIT-tmpe8ypo, read in NOTE-tmpvd0mr: §§3–5. 160
  keys annotated, one annotator each: every key had a pattern (3.6 on
  average), covering 65–80% of top prefixes. Agreement between value and
  key rises to about 3.5% by the top layers, against 0.0004% for a random
  token. It says nothing causal: no unit was ablated or edited, and the
  patterns were not compared with those of random directions.
---
<!-- inactive-ok-file: THEORY-tmpt0fr3 THEORY-1011 — Proposed; the general reading drawn from these results and the storage hypothesis it is not evidence for, cited as open -->

# THEORY-tmpwtgvz: In a 16-layer transformer language model trained on WikiText-103, the training prefixes that most activate a sampled feed-forward hidden unit share patterns that human annotators recognize, mostly shallow in layers 1–9 and semantic in layers 10–16; projected through the output embedding, a unit's output weights put the next token of its top prefix first in up to about 3.5% of units in the upper layers and almost none below; and a layer's top prediction differs from every unit's in at least about 68% of examples

## Source

Geva, Schuster, Berant and Levy (2021), EMNLP 2021, arXiv:2012.14913,
LIT-tmpe8ypo, read in full in NOTE-tmpvd0mr.

## What was actually shown

**Model.** Baevski and Auli's adaptive-input language model on
WikiText-103: 16 layers, d = 1024, 4,096 hidden units per feed-forward
layer.

**Keys.** For 10 random units per layer, every prefix of every training
sentence was scored by the unit's activation, and the top 25 were given to
one annotator, who marked patterns shared by at least three and labelled
them shallow or semantic. Every key had at least one (3.6 on average);
65–80% of prefixes were covered. Shallow patterns dominate layers 1–9,
semantic ones 10–16. For 100 units per layer, removing the last token of a
top prefix lowers the activation more than removing the first or a random
token, less so in upper layers.

**Values.** Each unit's output row, multiplied by the output embedding and
softmaxed, is compared with the next token of the unit's top prefix. They
agree in near 0% of units in layers 1–10 and in up to about 3.5% at the
top (0.0004% by chance). The 100 most peaked values are almost all in
layers 11–16, and 46 of them agree with at least one of their top 50
prefixes.

**Composition.** On 4,000 validation prefixes, hundreds of units are
active per layer, and in at least about 68% of examples, at every layer,
the layer's top token is none of its active units' top tokens.

**What could have come out otherwise.** Top prefixes could have shared no
pattern beyond chance; the shallow-to-semantic gradient could have been
absent; values could have agreed with keys no more than chance; a layer's
prediction could usually have been one unit's.

## What this does not say

- **Not that units store these associations causally.** Nothing was
  ablated, patched or edited.
- **Not that the patterns are the units' function.** Maximum activation
  over a corpus finds what most excites a unit, not what it does at
  typical activations, and no random-direction control was run.
- **Not about facts.** The associations studied are pattern-to-next-token
  statistics in WikiText, not subject–attribute facts, so this is not the
  evidence for ROME's storage hypothesis (THEORY-1011), which reads
  keys and values at the level of whole activation vectors.
- **Not beyond this model.** One 247M-parameter model.
- **Not that most values predict their key's next token.** At most about
  3.5% of units do.
