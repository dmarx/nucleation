---
number: 50
status: Active
formerly:
- CLAIM-tmpek80j
title: 'For report fidelity, fidelity is relative to the communicative decisions receivers make, and Blackwell''s order on rendering procedures, over a designed distribution of situations, makes precise the ceiling a rendering sets on those decisions'
version: 6
history:
- version: 2
  date: '2026-10-10'
  note: >-
    Restated on 2026-10-10 after CLAIM-225 and CLAIM-230.
    Version 1's condition read: 'A case where one rendering is a
    garbling of another yet is judged better on every communicative
    task the manuscript names, which would show the Blackwell order is
    the wrong standard rather than an incomplete one.' Its 'a case
    where one rendering is a garbling of another' is not well typed,
    since garbling relates procedures, not texts, and the case it
    describes is met by bounded receivers without touching the order
    (CLAIM-199). The scope is report fidelity (CLAIM-212).
    The manuscript's text quoted below is unchanged.
- version: 3
  date: '2026-10-16'
  note: >-
    Grounded also on THEORY-602, which states Shannon's coding
    theorems, including the fidelity theorem (a source is reproducible at
    a fidelity iff its rate for it does not exceed capacity) that the
    claim takes rate–distortion from. LIT-764 is kept.
- version: 4
  date: '2026-10-28'
  note: >-
    Narrowed and promoted at the status review of 2026-10-28 (ADR-057).
    Version 3's title read 'Fidelity is relative to the communicative
    decisions the receiver must make, and Blackwell's order of
    experiments makes that comparison precise'. The title now states the
    concessions its condition had made only in defeated_if: the order
    sets a ceiling, not what a given receiver does (CLAIM-225); it
    compares procedures over a designed distribution, not single
    renderings (CLAIM-230); and its scope is report fidelity, leaving
    re-performance to CLAIM-258. The deficiency and Wyner-Ziv steps,
    which rest on unread works, move to CLAIM-488, and LIT-778 and
    LIT-767 leave the grounds.
- version: 5
  date: '2026-10-29'
  note: >-
    Eleventh status review (ADR-057, ADR-059). CLAIM-218, granted on
    2026-10-10, was written in at version 4 without being named in its
    history. The note of 2026-10-28 ('The measure') says the record's
    D_Q is not the order this claim names and that the claim does not
    say D_Q realizes it. The defeat condition's second clause uses the
    Q-restricted deficiency, not D_Q. No other change.
- version: 6
  date: '2026-10-30'
  note: >-
    CLAIM-488 was promoted at the twenty-first status review (ADR-057), so
    the body's "are CLAIM-488, Proposed" now reads Active. No other change.
role: thesis
warrant: interpretive
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
- WORK-002
grounds:
- THEORY-1096
- LIT-781
- LIT-764
- THEORY-602
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
- CLAIM-204
- CLAIM-220
complements:
- CLAIM-142
- CLAIM-199
- CLAIM-212
- CLAIM-259
- CLAIM-488
objected_by:
- CLAIM-218
- CLAIM-225
- CLAIM-230
- CLAIM-258
---
<!-- ref::uses-file: TERM-028 — stated in "fidelity, as inferential sufficiency", which the claim restates through Blackwell's order of experiments; the body names fidelity only in its prior-art comparison -->
<!-- inactive-ok-file: LIT-778 LIT-767 — Unavailable; quoted as the manuscript's steps, which moved to CLAIM-488 -->
<!-- inactive-ok-file: CLAIM-199 CLAIM-212 — Proposed; the record's replies that scope this claim's restated condition, cited as open -->

# CLAIM-050: For report fidelity, fidelity is relative to the communicative decisions receivers make, and Blackwell's order on rendering procedures, over a designed distribution of situations, makes precise the ceiling a rendering sets on those decisions

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

## Note of 2026-10-27: grounded in what it uses of Blackwell

The status review of this date ([ADR-057](../decisions.d/ADR-057.md)) moved this claim's ground from
[THEORY-156](../theory.d/THEORY-156.md) to [THEORY-1096](../theory.d/THEORY-1096.md). It uses Blackwell's definitions (an experiment, a
garbling, the informativeness order) or the easy direction, that a
garbling never helps a decision-maker free to choose any rule. Both hold
on any outcome spaces, with the proof written out there. [THEORY-156](../theory.d/THEORY-156.md)'s
general converse, which stays Proposed, is not used. Quotations of
[THEORY-156](../theory.d/THEORY-156.md) above are of the definitions it states.

## Note of 2026-10-28: narrowed and promoted

The status review of this date narrowed the title to what the claim's
condition already conceded, and promoted it ([ADR-057](../decisions.d/ADR-057.md)).

- **A ceiling, not a receiver.** [CLAIM-225](CLAIM-225.md) showed the order says what an
  ideal decision-maker could do with a rendering, not what a given
  receiver does. The title says ceiling ([CLAIM-199](CLAIM-199.md)'s first half).
- **Procedures.** [CLAIM-230](CLAIM-230.md) showed the order relates procedures over a
  distribution of situations, not two texts. The title says so.
- **Report fidelity.** [CLAIM-258](CLAIM-258.md)'s objection, that re-performance is the
  normal case of translation, is not answered, since [CLAIM-212](CLAIM-212.md) is
  Proposed. The claim concedes it by scope: it is about report fidelity,
  and re-performance stays open there and in [QUESTION-005](../questions.d/QUESTION-005.md).
- **The measure.** [CLAIM-218](CLAIM-218.md) says the record's D_Q is not the order this
  claim names. This claim does not say D_Q realizes the order.

What the claim uses of Blackwell is the definitions and the easy
direction, held in [THEORY-1096](../theory.d/THEORY-1096.md) with the proof written out. The steps that
rested on unread works, deficiency for the approximate case and the
Wyner-Ziv form of side information, are [CLAIM-488](CLAIM-488.md), Active. The
second clause of defeated_if stays as a test; it does not lean on
Torgersen's results.

## Note of 2026-10-31: a different information, not a rival

<!-- inactive-ok-file: THEORY-1276 CLAIM-525 — Proposed; a reading filed on 2026-10-31 and the record's claim placing it -->

The Simondon readings filed on 2026-10-31 (Iliadis, [LIT-1911](../literature.d/LIT-1911.md);
Bencherki and Iliadis, [LIT-1922](../literature.d/LIT-1922.md); read together in [THEORY-1276](../theory.d/THEORY-1276.md))
hold that information is "never a given thing". On their account it is a
disparity whose resolution produces a new structure in the system that
takes it up. That could be read as a rival to this claim's information,
evidence about a situation compared by Blackwell's order. [CLAIM-525](CLAIM-525.md)
argues that it is not. The readings' information is a change in the
interpreter ([CLAIM-118](CLAIM-118.md)) or in the questions a receiver can decide
([CLAIM-257](CLAIM-257.md)), and the order holds both fixed by construction. This claim's
scope, report fidelity for receivers whose decision problems are given,
is unaffected.

No status, title or warrant changes.
