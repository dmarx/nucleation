---
status: Proposed
promote_when: >-
  A re-analysis of the same or a comparable curated protein-interaction
  network, with the accuracy measure defined, showing that mixed
  memberships fitted to the interactions alone predict held-out functional
  annotations better than predicting from the annotations' base rates,
  including the all-absent prediction, by a margin that holds when the
  mapping of blocks to functions and the threshold are chosen on the
  training proteins. It is refuted if the memberships do no better than
  that baseline. A further comparison against random guessing at the right
  proportions cannot settle it.
title: 'Mixed memberships fitted by a fifteen-block MMSB to 871 yeast proteins'' curated physical interactions carry information about the proteins'' top-level MIPS functions beyond what the functions'' base rates give: after mapping blocks to functions on 87 proteins, thresholded memberships predicted the other proteins'' annotations with about 87% accuracy, against about 70% for random guessing at the right proportions'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed Proposed from NOTE-tmphwzim. The measurement was read in full,
    but the paper does not define its accuracy, and on the likely
    per-entry reading predicting no function at all would score about
    84%, so the design does not support "beyond the base rates" as
    stated. The record's arithmetic, in the body.
tags:
- network-science
- natural-sciences
- probabilistic-modeling
date: '2026-10-26'
source:
- LIT-tmpt5wer
summary: >-
  Airoldi, Blei, Fienberg and Xing (2008), [LIT-tmpt5wer](../literature.d/LIT-tmpt5wer.md), §4.3.2 and Figs.
  10–12, read in [NOTE-tmphwzim](../notes.d/NOTE-tmphwzim.md). The batch's one check of inferred mixed
  memberships against labels the model never saw. The reported margin is
  over a weak baseline, so it shows less than it seems: probably some
  information, not yet how much. It says nothing about whether the
  fifteen blocks are the fifteen functions.
---
<!-- inactive-ok-file: CLAIM-427 — Proposed; the claim whose standard for recovered modes this is set against, open -->

# THEORY-tmpuvkbn: Mixed memberships fitted by a fifteen-block MMSB to 871 yeast proteins' curated physical interactions carry information about the proteins' top-level MIPS functions beyond what the functions' base rates give: after mapping blocks to functions on 87 proteins, thresholded memberships predicted the other proteins' annotations with about 87% accuracy, against about 70% for random guessing at the right proportions

## Source

Airoldi, Blei, Fienberg and Xing (2008), [LIT-tmpt5wer](../literature.d/LIT-tmpt5wer.md), §4.3.1–4.3.2,
Table 2 and Figs. 10–12, read in full in [NOTE-tmphwzim](../notes.d/NOTE-tmphwzim.md).

## What was actually shown

871 proteins from MIPS's hand-curated physical interactions, which exclude
high-throughput data, were fitted with K = 15. MIPS also gives each
protein its top-level functions, 15 in all, "with an average of ≈ 2.4
functional annotations for each protein". The annotations were not used in
fitting. Because "the K = 15 blocks in the blockmodel B are not directly
identifiable in terms of functional categories", a permutation from blocks
to functions was estimated greedily, to maximize accuracy on a sample of
87 proteins, with memberships thresholded at τ, the 95th percentile of
those proteins' membership values. Applied to the remaining 90% of the
proteins: "The accuracy on the 90% testing set is about 87%. An algorithm
that randomly guesses annotations, knowing the right proportions of
annotations in each category, leads to a baseline accuracy of about 70%."

What could have come out otherwise: memberships fitted to interactions
alone could have carried no functional information, and scored at the
baseline.

## Why it is Proposed

The paper does not define accuracy. If it is the share of correct
protein–function entries, the base rate of an annotation is about
2.4/15 = 0.16. Then random guessing at the right proportions scores about
0.16² + 0.84² ≈ 0.73, close to the paper's "about 70%", which makes the
per-entry reading likely. But predicting that no protein has any function
scores about 0.84 on that reading, so "about 87%" is three points above
the trivial predictor, not seventeen. The threshold at the 95th percentile
predicts about 5% of entries present, against 16% true, which also bounds
what any mapping could reach. The record's arithmetic, from the paper's
own numbers. The direction of the result may well stand. Its size is not
shown.

## What this does not say

- **Not that blocks are functions.** The mapping is chosen to fit, and
  proteins have several functions each, so a block can match a function
  partly.
- **Not about §4.3.3.** The K = 50 analysis of predicted interactions'
  functional precision is a separate result, and not filed.
- **Not that memberships are identified.** The permutation the paper
  estimates is the part of the gauge it admits ([THEORY-tmplo0xb](THEORY-tmplo0xb.md)).

## Connections

- **[CLAIM-427](../claims.d/CLAIM-427.md).** Recovering structure in the model's own terms counts for
  nothing there. This is the right kind of check, structure against
  labels the model never saw, done with too weak a baseline to count for
  much yet.
- **[QUESTION-tmpixgs8](../questions.d/QUESTION-tmpixgs8.md).** An inferred mixed membership of an organization's
  members would need the same kind of external test, against a stated
  trivial predictor.
