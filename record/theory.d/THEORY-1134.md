---
number: 1134
status: Active
formerly:
- THEORY-tmpa9y98
title: 'A translation metric that predicts a sentence score and token-level error spans from one shared encoder reaches segment-level agreement with expert MQM annotation of Kendall τ about 0.4 and span F1 under 0.33, the best among open metrics and GPT-4 prompting at the time, while the score computed from its own spans correlates with its regression scores at Pearson 0.73 to 0.82, and at 0.90 to 0.92 with its final score, which includes the span score by construction'
version: 2
history:
- version: 2
  date: '2026-10-30'
  note: >-
    Narrowed and promoted by the twenty-second status review, at the
    status review's ruling (the owner delegated these rulings;
    ADR-065; ADR-047 kind 2): NOTE-1341 read the paper in full, and
    the title now reports Tables 2a, 4 and 5 and says that the top
    correlation is partly by construction. Its last clause, the
    record's reading that the explanation is far more coherent with
    the score than either is with human judgement, moves to
    CLAIM-507, Proposed, grounded in this entry, without "far":
    converted to one scale under normality, Kendall τ of 0.39 to 0.47
    is Pearson of about 0.58 to 0.67, against the heads' 0.73 to 0.82.
    The old title: "A translation metric that predicts a sentence
    score and token-level error spans from one shared encoder reaches
    segment-level agreement with expert MQM annotation of Kendall τ
    about 0.4 and span F1 under 0.33, the best among open metrics and
    GPT-4 prompting at the time, while its score and its own spans
    agree with each other at Pearson 0.73 to 0.92, so the explanation
    it gives is far more coherent with its score than either is with
    the human judgement" The old promote_when: "A held-out evaluation,
    on expert MQM from a domain and year the metric was not trained
    near, that reports for the same segments both the agreement
    between the metric's score and its own error spans and the
    agreement of each with the human annotation, and finds the first
    reliably larger than the second; or one that finds them
    comparable. Further correlations with humans alone do not settle
    it, since the claim is about the gap."
tags:
- translation
date: '2026-10-29'
source:
- LIT-1816
summary: >-
  Guerreiro, Rei, van Stigt, Coheur, Colombo and Martins (TACL 2024),
  [LIT-1816](../literature.d/LIT-1816.md), Tables 2, 4 and 5, read in [NOTE-1341](../notes.d/NOTE-1341.md). The numbers are
  the paper's, on WMT22 News MQM (zh-en, en-de, en-ru). The paper reads
  the heads' agreement as support for the spans as explanation; the
  record reads it as coherence. The top of the agreement, 0.90–0.92, is
  partly arithmetic, since the final score includes the span score with
  weight 2/9. Active as a report of one test set (ADR-065); the record's
  reading of the gap, across different statistics, is CLAIM-507.
---

<!-- inactive-ok-file: CLAIM-507 — Proposed; the record's reading split from this entry, cited as open -->

# THEORY-1134: A translation metric that predicts a sentence score and token-level error spans from one shared encoder reaches segment-level agreement with expert MQM annotation of Kendall τ about 0.4 and span F1 under 0.33, the best among open metrics and GPT-4 prompting at the time, while the score computed from its own spans correlates with its regression scores at Pearson 0.73 to 0.82, and at 0.90 to 0.92 with its final score, which includes the span score by construction

## Source

Guerreiro et al. (2024), [LIT-1816](../literature.d/LIT-1816.md), §6 and Tables 2a, 4 and 5 (pp.
985–987) of TACL 12; read in [NOTE-1341](../notes.d/NOTE-1341.md).

## What was actually shown

**Agreement with experts.** On WMT22 News MQM, xCOMET-XXL's segment-level
Kendall τ is 0.390 (zh-en), 0.435 (en-de) and 0.470 (en-ru), average
0.432; XL averages 0.421 (Table 2a). The best other metric, METRICX, is at
0.421. Character-level F1 of predicted error spans against human spans is
0.237–0.320 per pair, average 0.269 (XL) and 0.280 (XXL), against 0.262
for GPT-4 AutoMQM (Table 4).

**Agreement between heads.** The MQM score recomputed from xCOMET-XXL's own
spans, ŷ_MQM, correlates with its three regression outputs at Pearson
0.73–0.82 per pair and with its final score at 0.90–0.92 (Table 5). The
final score is ŷ_SL = wᵀ[ŷ_SRC, ŷ_REF, ŷ_SRC+REF, ŷ_MQM] with w_MQM = 2/9
(eq. 7), so the last figure includes ŷ_MQM's correlation with itself in
part. The authors: the heads' correlations "are obtained despite no
explicit alignment mechanism", and "it is thus the shared encoder that,
during the multi-task training, aligns the representations" (pp.
986–987).

**What could have failed.** The spans could have tracked human spans as
well as they track the model's own score, or the heads could have
disagreed while each tracked humans.

## What this does not say

- **That the spans are wrong or useless.** They match human spans better
  than GPT-4 prompting did, and their MQM score alone beats BLEURT-20 and
  COMET-22 at segment level (Table 2a).
- **That the statistics are directly comparable.** Pearson between two
  model outputs and Kendall or F1 against humans measure different
  things; the gap is large enough to read, not to quantify.
- **That the shared encoder is the mechanism.** That is the authors'
  hypothesis; no experiment isolates it.
- **Anything about use as a selection criterion.** Agreement on given
  translations does not bound the bias a metric shows when it picks the
  translations it scores ([CASE-071](../cases.d/CASE-071.md)).
- **For other domains.** One news test set, three pairs, all with English
  on one side.

## Note of 2026-10-30: narrowed and promoted

Promoted as a report of what the paper measured ([ADR-065](../decisions.d/ADR-065.md)). The record's
reading, that the spans are more coherent with the score than either is
with expert judgement, is [CLAIM-507](../claims.d/CLAIM-507.md), Proposed, grounded in this
entry; its body states the conversion of τ to a Pearson scale.
