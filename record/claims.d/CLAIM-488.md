---
number: 488
status: Proposed
formerly:
- CLAIM-tmpqmsav
title: 'Le Cam deficiency, after Torgersen, would quantify the approximate case of the Blackwell order for translation, and decoder-only audience knowledge would make the coding problem a Wyner-Ziv problem'
version: 2
history:
- version: 2
  date: '2026-10-30'
  note: >-
    The twentieth status review (ADR-058; an unread work takes no edge),
    at the status review's ruling (the owner delegated these rulings).
    LIT-778, Torgersen, and LIT-767, Wyner and Ziv, both Unavailable and
    read by no NOTE, leave grounds. The first step now rests on
    CLAIM-381, which defines Le Cam's deficiency between the item-
    indexed tables of source and rendering and shows it a finite
    computation; Torgersen is cited as the manuscript's source. The
    second step applies the definition of a Wyner–Ziv problem, source
    coding with side information at the decoder only, under its own
    condition; Wyner and Ziv are cited for the name. The body keeps both
    citations. 'Why it is Proposed' ended: 'It goes Active when the two
    works, or readings of them, are held and the steps are checked
    against them.'
role: thesis
warrant: interpretive
defeated_if: >-
  On a designed distribution of situations, the Q-restricted deficiency
  between source and rendering procedures, computed on receivers'
  judgement outcomes, predicts their fidelity verdicts no better than
  static pragmatic similarity does; or the audience knowledge a rendering
  can rely on is available to the encoder as well, so that the side
  information is not decoder-only.
tags:
- mathematical-statistics
- information-theory
date: '2026-10-28'
line: pragmatic-transport
works:
- what-survives-translation
rests_on:
- CLAIM-381
grounds:
- THEORY-602
complements:
- CLAIM-050
summary: >-
  The two steps of the manuscript's §5 that [CLAIM-050](CLAIM-050.md) carried until the
  status review of 2026-10-28 and that rest on works the record has not
  read: deficiency for the approximate case (Torgersen) and the Wyner-Ziv
  form of decoder side information. Split off when [CLAIM-050](CLAIM-050.md) was narrowed
  to what its read sources support ([ADR-047](../decisions.d/ADR-047.md)'s third ruling).
---
<!-- inactive-ok-file: LIT-778 LIT-767 until 2027-01-28 — Unavailable; the works these steps cite, unread here, which is why this claim is Proposed -->

# CLAIM-488: Le Cam deficiency, after Torgersen, would quantify the approximate case of the Blackwell order for translation, and decoder-only audience knowledge would make the coding problem a Wyner-Ziv problem

## The claim

The manuscript's §5, as [CLAIM-050](CLAIM-050.md) quoted it: for translation, Blackwell's
order is restricted to a family Q of tasks, and the manuscript "proposes
deficiency for the approximate case (Torgersen, [LIT-778](../literature.d/LIT-778.md))". Shannon
([THEORY-602](../theory.d/THEORY-602.md)) supplies rate-distortion, and "decoder-only audience knowledge
makes it a Wyner-Ziv problem ([LIT-767](../literature.d/LIT-767.md))".

Exact garbling is rare between two renderings, so a usable order needs a
measure of how far one is from being a garbling of the other. Le Cam's
deficiency is that measure. The audience brings knowledge the translator
cannot condition on in the text, which is the decoder-side information of
Wyner and Ziv.

## Why it is Proposed

Both steps rest on works cited without a reading: Torgersen and Wyner-Ziv
are Unavailable here. [CLAIM-050](CLAIM-050.md) said so in its own body. When [CLAIM-050](CLAIM-050.md) was
narrowed on 2026-10-28 to what its read grounds carry, these steps moved
here, so that the narrowing drops nothing silently.

It goes Active when the first step's link from deficiency to the order is
held; the note of 2026-10-30 says what that needs.

## Note of 2026-10-29: what holds it back

Both steps rest on works the record has not read: Torgersen ([LIT-778](../literature.d/LIT-778.md)) for
deficiency as the approximate Blackwell order, and Wyner and Ziv ([LIT-767](../literature.d/LIT-767.md))
for decoder-only side information. It goes Active on readings of them, or on
a checked re-derivation of Le Cam's randomization criterion for finite
experiments, which would hold the first step.

## Note of 2026-10-30: what holds it back

Its first step still lacks Le Cam's randomization criterion for finite
experiments. [CLAIM-381](CLAIM-381.md) defines the deficiency and computes it, and that a
deficiency of ε bounds every [0, 1]-loss risk gap by ε follows in two
lines from that definition; the converse, which makes deficiency the
approximate Blackwell order and not only a bound on it, is neither read
nor re-derived. The wait on Wyner and Ziv in the note of 2026-10-29 no
longer applies: the second step is that problem's definition.
