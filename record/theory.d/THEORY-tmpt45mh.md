---
status: Proposed
promote_when: >-
  The same crosscoder analysis with the trend measured rather than
  annotated: a quantitative token-specificity score for each important
  feature (for example the entropy of its activations over token types, or
  the share of its activation mass on one token) that falls from early to
  late checkpoints, over more than the top-10 features, across crosscoder
  seeds and at more than one layer. And for the post-plateau claim, a null:
  crosscoders on pairs of nearby checkpoints of equal accuracy, whose share
  of checkpoint-specific important features is smaller than between the
  plateau checkpoints the paper used. It is refuted if a measured
  token-specificity score shows no trend, or if nearby-checkpoint nulls
  show as much redistribution as the paper's pairs. More annotated
  examples cannot settle it.
title: 'In Pythia-1B, OLMo-1B and BLOOM-1B, the crosscoder features that most affect subject–verb agreement change over pretraining: at early checkpoints they detect particular tokens and subtokens, at later ones grammatical categories; in BLOOM, language-specific features give way to features shared across English, French, Spanish and Portuguese while Hindi and Arabic keep language-specific ones; and which features matter keeps shifting after task accuracy has stopped improving'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed Proposed from NOTE-tmpq065x. The token-to-category trend rests on
    the authors' annotation of a few top features, and the post-plateau
    shift on a scatter plot without counts or a null.
tags:
- representation-learning
- linguistics
date: '2026-10-26'
source:
- LIT-tmpuuwok
summary: >-
  Bayazit, Mueller and Bosselut (2025, ACL 2026), [LIT-tmpuuwok](../literature.d/LIT-tmpuuwok.md), read in
  [NOTE-tmpq065x](../notes.d/NOTE-tmpq065x.md). Crosscoders trained jointly on the middle layer of two or
  three checkpoints, with features scored by their relative indirect effect
  on agreement minimal pairs at each. The reconstruction quality (C1) and
  RelIE's agreement with single-feature ablations (C2) are measured; the
  trends in this title are read by the authors from annotated features.
  It describes; it does not predict later checkpoints, and it cannot tell a
  feature carried forward from one re-learned in the same direction.
---
<!-- inactive-ok-file: CLAIM-329 THEORY-279 CASE-tmplcm41 — Proposed; the thesis on continuity by transmission and a neighbouring account, cited as open -->
# THEORY-tmpt45mh: In Pythia-1B, OLMo-1B and BLOOM-1B, the crosscoder features that most affect subject–verb agreement change over pretraining: at early checkpoints they detect particular tokens and subtokens, at later ones grammatical categories; in BLOOM, language-specific features give way to features shared across English, French, Spanish and Portuguese while Hindi and Arabic keep language-specific ones; and which features matter keeps shifting after task accuracy has stopped improving

## Source

Bayazit, Mueller and Bosselut (2025), [LIT-tmpuuwok](../literature.d/LIT-tmpuuwok.md), read in full in
[NOTE-tmpq065x](../notes.d/NOTE-tmpq065x.md) from arXiv v2: §§5–8, Tables 1–2 and 6–7, Figs. 2–5, and
appendices D–G.

## What is asserted

That in these three model families, at the middle layer, the features a
model uses for subject–verb agreement are replaced over pretraining by more
general ones, in two directions: from particular tokens to grammatical
categories, and, in a multilingual model, from one language to several
with similar agreement systems. And that the replacement continues after
the task is learned.

## What the paper shows toward it

- **Measured.** Crosscoders reconstruct each checkpoint's activations with
  a small rise in loss (Table 6). RelIE agrees with single-feature
  ablations on the top-10 features (ρ about 0.95). In Pythia's three-way
  analysis, many of the top-100 features are specific to the 4B or the
  286B checkpoint although accuracy is the same at both (Fig. 4, no
  counts). In BLOOM the overlap of top-10 features across the four
  Latin-script languages rises by 341B, and Hindi and Arabic overlap
  little (Fig. 5).
- **Annotated.** That the early features are token-specific and the late
  ones categorical is the authors' description of top-activating
  sequences for a few features per checkpoint (Tables 1, 2 and the
  appendix tables), done blind to RelIE but by the authors.

## Why it stays Proposed

The central trend is an annotation. The post-plateau shift has no null:
two crosscoders, or two nearby checkpoints, might also disagree on which
features matter. And the analysis is one layer and a handful of
checkpoints per model.

## What this does not say

- **Not that a later feature descends from an earlier one.** Shared
  features share an index in a jointly trained dictionary; that is
  resemblance, which [CLAIM-329](../claims.d/CLAIM-329.md) distinguishes from continuity.
- **Not a mechanism.** Features are scored one at a time; how they combine
  into a circuit is the authors' future work.
- **Not a prediction.** Checkpoints are chosen after the transitions are
  seen.

## Connections

- **[QUESTION-tmpivbso](../questions.d/QUESTION-tmpivbso.md).** The feature-only description the question's
  coupled model has to beat.
- **[THEORY-279](THEORY-279.md).** Low-level structure first, at the level of features in
  large language models, by annotation.
- **[CASE-tmplcm41](../cases.d/CASE-tmplcm41.md).** Presence (decoder norm) and use (indirect effect) are
  measured separately here, which the case's model could not do from its
  outputs.
- **LIT-tmp5b0z9.** The indirect effects and their integrated-gradient
  approximation come from Marks et al.'s sparse feature circuits, which
  ran them on the same subject–verb agreement tasks in one checkpoint
  (THEORY-tmpuogp2).
