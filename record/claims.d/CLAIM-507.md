---
number: 507
status: Proposed
formerly:
- CLAIM-tmp2um57
title: 'On WMT22 News MQM, xCOMET''s error spans are more coherent with its own regression scores than either is with expert judgement: the agreement between its heads is coherence between two outputs of one model, and adds little to what the spans'' own agreement with experts shows'
version: 2
history:
- version: 2
  date: '2026-10-30'
  note: >-
    Revised and kept Proposed by the twenty-third status review, at the
    status review's ruling (the owner delegated these rulings; ADR-057).
    The title's "coherence through one encoder" asserted the mechanism
    the body disclaims, and now reads "between two outputs of one model".
    It is scoped to WMT22 News MQM, the one test set measured. "Not
    evidence" becomes "adds little", since with the heads at 0.82 and
    the score at about 0.67 on one scale the bound on the spans'
    agreement with experts is weak but not nil. The body gives the
    per-pair figures, the spans' own τ, and what ties do to the
    conversion. The old title: "xCOMET's error spans are more coherent
    with its own score than either is with expert judgement: the
    agreement between its heads is coherence through one encoder, not
    evidence that the spans explain human-judged quality".
role: thesis
warrant: interpretive
defeated_if: >-
  A held-out evaluation that reports, for the same segments and on one
  scale, the agreement between the score and the spans and the agreement
  of each with expert MQM, and finds them comparable.
tags:
- translation
date: '2026-10-30'
line:
- pragmatic-transport
grounds:
- THEORY-1134
summary: >-
  The record's reading of Guerreiro et al.'s Table 5, split from
  [THEORY-1134](../theory.d/THEORY-1134.md) when the twenty-second status review narrowed it to the
  measurements and promoted it ([ADR-065](../decisions.d/ADR-065.md); [ADR-047](../decisions.d/ADR-047.md) kind 2). An instance of
  [CLAIM-496](CLAIM-496.md)'s distinction between coherence and fidelity. The statistics
  compared differ (Pearson between heads; Kendall and F1 against humans),
  and converted to one scale the gap is smaller than it looks.
---

# CLAIM-507: On WMT22 News MQM, xCOMET's error spans are more coherent with its own regression scores than either is with expert judgement: the agreement between its heads is coherence between two outputs of one model, and adds little to what the spans' own agreement with experts shows

## The claim

xCOMET ([LIT-1816](../literature.d/LIT-1816.md), read in [NOTE-1341](../notes.d/NOTE-1341.md)) gives a sentence score and error spans
from one shared encoder. The MQM score computed from its own spans
correlates with its regression scores at Pearson 0.73 to 0.82 per pair,
and at 0.90 to 0.92 with its final score, which includes the span score
with weight 2/9 by construction ([THEORY-1134](../theory.d/THEORY-1134.md)). Against expert MQM its
final score's segment-level Kendall τ is 0.39 to 0.47, the span score's 0.33
to 0.44 (NOTE-1341), and its span F1 0.24 to 0.32. The
paper presents the heads' agreement as support for the spans as an
explanation of the score. The record reads it as [CLAIM-496](CLAIM-496.md) reads agreement
between routes: two outputs of one encoder agreeing is coherence, and its
size says nothing about how often either is right.

## How large the gap is

The figures are on different scales. Under bivariate normality Kendall's
τ and Pearson's r are related by r = sin(πτ/2). Per pair (Table 2a,
xCOMET-XXL), the final score's τ of 0.390, 0.435 and 0.470 (zh-en, en-de,
en-ru) corresponds to r of about 0.58, 0.63 and 0.67, and the span score's
τ of 0.332, 0.415 and 0.439 to about 0.50, 0.61 and 0.64. Table 5 gives the
span score against the three regression outputs at 0.73–0.78, 0.74–0.79
and 0.75–0.82 for the same pairs. Every pair keeps a gap, of 0.08 (en-ru)
to 0.16 (zh-en), between the lowest head correlation and the higher expert
one. The large gaps are against the final score, whose 0.90 to 0.92 is
partly arithmetic, and against span F1 of about 0.28, which is not a
correlation.

MQM scores are skewed and heavily tied: in WMT22 a fifth to a third of
segment pairs are tied in human MQM, most at zero errors (Deutsch, Foster
and Freitag 2023, not in the record). In the status review's simulation of
2026-10-30, a normal latent quality cut into MQM-like scores at that tie
rate, sin(πτ_b/2) stays within about 0.04 of the latent r while
sin(πτ_a/2) understates it by about 0.1; and ties in the span score lower
its observed Pearson with a continuous head below the latent value, which
widens the gap. Hence "more coherent", not "far more", and only if Table
2a's τ is τ_b.

## What would settle it

A held-out evaluation, on expert MQM from a domain and year the metric was
not trained near, that reports for the same segments both the agreement
between the metric's score and its own error spans and the agreement of
each with the human annotation, and finds the first reliably larger than
the second; or one that finds them comparable. Further correlations with
humans alone do not settle it, since the claim is about the gap.

## What it does not say

- **That the spans are wrong or useless.** They match human spans better
  than GPT-4 prompting did ([THEORY-1134](../theory.d/THEORY-1134.md)).
- **That the shared encoder is the mechanism.** That is the authors'
  hypothesis; no experiment isolates it.

## Note of 2026-10-30: what holds it back

The comparison puts Kendall τ and Pearson r on one scale, and under MQM's
ties that holds only for τ_b, which WMT22 used; neither the paper nor
NOTE-1341 says which τ Table 2a reports. Under τ_a the en-ru score's gap
can close. A reading that records the variant, or a recomputation on the
released WMT22 scores, would free it.
