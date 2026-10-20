---
# Don't copy this file by hand — run `luria new question`. A QUESTION is an
# open question the record's own argument is organised around. Claims and
# THEORY readings name it in `answers`, and its page shows both (ADR-032).

# Open | Answered | Dissolved | Deferred | Superseded
status: Open

# The question, as a question. Repeat it as the `# QUESTION-…:` heading.
title: 'Does fixed-feature transfer to new classes fall as penultimate class separation rises outside ImageNet-trained ResNet-50s, and does it move with within-class spread when the loss is held fixed?'

version: 1
tags:
- representation-learning
- learning-theory
date: '2026-10-20'

# REQUIRED: the line of inquiry, from `lines` in luria.yaml.
line: 'learned-structure'
summary: >-
  The promotion condition formerly on [THEORY-246](../theory.d/THEORY-246.md), moved unchanged when that
  account was narrowed to what Kornblith et al. (2021) measured and
  promoted on 2026-10-20 ([ADR-047](../decisions.d/ADR-047.md) v3). Open: whether the inverse relation
  between penultimate class separation and new-class transfer holds in
  other pretraining settings, and whether separation, rather than the
  loss, is what moves transfer.

refines:
- QUESTION-051
---
<!-- inactive-ok-file: THEORY-104 — Proposed; the same-class-shift account, named to say what cannot settle this -->

# QUESTION-tmpu3u0x: Does fixed-feature transfer to new classes fall as penultimate class separation rises outside ImageNet-trained ResNet-50s, and does it move with within-class spread when the loss is held fixed?

## Why it is a question

[THEORY-246](../theory.d/THEORY-246.md) holds what Kornblith et al. ([LIT-1044](../literature.d/LIT-1044.md)) measured. Among
ResNet-50s trained on ImageNet with nine objectives and early-stopped,
fixed penultimate features with more class separation transfer worse to
datasets whose classes are mostly not ImageNet's (Spearman ρ = −0.93 across
the nine). One temperature knob moves both, and full fine-tuning removes
most of the gap. Two things that study cannot settle were [THEORY-246](../theory.d/THEORY-246.md)'s
promote_when until 2026-10-20. One is generality: it is one pretraining
set, two architectures, and networks stopped near 92% training accuracy.
The other is mechanism: across losses the relation is a correlation of
nine points, and no experiment holds separation fixed while changing the
loss. The authors themselves expect a larger, richer label space might
soften or reverse the trade (§5).

## What would answer it

The condition as it stood, unchanged:

- **For generality.** The same comparison, fixed-feature readout of
  new-class tasks against penultimate class separation, in a pretraining
  setting [LIT-1044](../literature.d/LIT-1044.md) did not test: a much larger label space, a transformer,
  or a network trained past zero training error, with the inverse relation
  holding.
- **For the mechanism.** An intervention that changes within-class spread
  in the last layers with the loss held fixed, or holds it fixed while the
  loss changes, and shows new-class transfer moving with the spread and
  not with the loss.

**Against it.** At matched class separation, different losses giving
clearly different new-class transfer, or, with a large and diverse
pretraining label space, more separation ceasing to cost new-class
transfer.

**What cannot settle it.** More losses on ResNet-50 and ImageNet repeat the
measured correlation. More same-class shift benchmarks answer a different
question ([THEORY-104](../theory.d/THEORY-104.md)).
