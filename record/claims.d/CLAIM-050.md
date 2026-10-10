---
number: 50
status: Proposed
formerly:
- CLAIM-tmpek80j
title: 'Fidelity is relative to the communicative decisions the receiver must make, and Blackwell''s order of experiments makes that comparison precise'
version: 2
history:
- version: 2
  date: '2026-10-10'
  note: >-
    Restated on 2026-10-10 after CLAIM-tmpdt857 and CLAIM-tmpflbi3.
    Version 1's condition read: 'A case where one rendering is a
    garbling of another yet is judged better on every communicative
    task the manuscript names, which would show the Blackwell order is
    the wrong standard rather than an incomplete one.' Its 'a case
    where one rendering is a garbling of another' is not well typed,
    since garbling relates procedures, not texts, and the case it
    describes is met by bounded receivers without touching the order
    (CLAIM-tmp0jq5k). The scope is report fidelity (CLAIM-tmp95pjv).
    The manuscript's text quoted below is unchanged.
role: thesis
defeated_if: >-
  Receivers' task-indexed fidelity verdicts rank the same rendering
  procedures the same way whatever task in Q is named, so that fidelity
  is not relative to the decisions; or, on a designed distribution of
  situations, the Q-restricted deficiency between the source and
  rendering procedures, computed on receivers' judgement outcomes,
  predicts those verdicts no better than static pragmatic similarity
  does.
tags:
- mathematical-statistics
- information-theory
date: '2026-10-09'
line: pragmatic-transport
works:
- what-survives-translation
grounds:
- THEORY-156
- LIT-781
- LIT-778
- LIT-764
- LIT-767
supersedes:
- CLAIM-051
uses:
- TERM-028
summary: >-
  The manuscript's §5: rate–distortion makes coding cost explicit,
  Blackwell comparison (restricted to a family Q of communicative
  decision problems) makes fidelity operational, and decoder side
  information is a Wyner–Ziv problem.
supports:
- CLAIM-115
- CLAIM-014
- CLAIM-126
- CLAIM-133
- CLAIM-139
- CLAIM-tmp3wo5j
- CLAIM-tmpc1o4m
complements:
- CLAIM-142
- CLAIM-tmp0jq5k
- CLAIM-tmp95pjv
- CLAIM-tmpz239h
objected_by:
- CLAIM-tmpbi9eb
- CLAIM-tmpdt857
- CLAIM-tmpflbi3
- CLAIM-tmpyeik3
---
<!-- inactive-ok-file: THEORY-161 — Proposed; semantic rate–distortion as indirect coding, cited for what it implies here, not as settled -->
<!-- inactive-ok-file: CLAIM-051 — Superseded; replaced, and cited as the history this entry answers or replaces -->
<!-- inactive-ok-file: CLAIM-tmp0jq5k CLAIM-tmp95pjv — Proposed; the record's replies that scope this claim's restated condition, cited as open -->

# CLAIM-050: Fidelity is relative to the communicative decisions the receiver must make, and Blackwell's order of experiments makes that comparison precise

## The claim

If P(V₂|Z) = G P(V₁|Z) for a source-independent garbling G, then V₁ is at
least as good as V₂ for every bounded decision problem over Z (Blackwell,
[LIT-781](../literature.d/LIT-781.md)). For translation the manuscript restricts this to a family Q of tasks
— tell teasing from reproach, recognize a position, choose a reply — and
proposes deficiency for the approximate case (Torgersen, [LIT-778](../literature.d/LIT-778.md)). Shannon
([LIT-764](../literature.d/LIT-764.md)) supplies rate–distortion; decoder-only audience knowledge makes it a
Wyner–Ziv problem ([LIT-767](../literature.d/LIT-767.md)).

## What it does not say

The direction the manuscript uses (garbling implies no worse) is the easy one:
Blackwell 1951's, restated as Theorem 3 of the 1953 paper ([NOTE-595](../notes.d/NOTE-595.md)). The 1953
equivalence is proved for finitely many states, so Z must be finite or the
general case cited. Its restricted family Q has a precedent in the paper
itself: Blackwell's k-decision orders ≻_k, and for two states ≻_2 already
decides the full order (Theorem 10). Torgersen and Wyner–Ziv are unread here,
so those steps rest on works cited without a reading.

## Prior art for decision-relative fidelity

Zhao et al. ([LIT-793](../literature.d/LIT-793.md), [THEORY-161](../theory.d/THEORY-161.md)): with total variation, the
posterior distortion bounds the extra Bayes risk of every bounded-loss
decision. That is a decision-relative fidelity close to this claim's.
