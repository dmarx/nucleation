---
status: Proposed
title: 'Le Cam deficiency, after Torgersen, would quantify the approximate case of the Blackwell order for translation, and decoder-only audience knowledge would make the coding problem a Wyner-Ziv problem'
version: 1
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
grounds:
- LIT-778
- LIT-767
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

# CLAIM-tmpqmsav: Le Cam deficiency, after Torgersen, would quantify the approximate case of the Blackwell order for translation, and decoder-only audience knowledge would make the coding problem a Wyner-Ziv problem

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

It goes Active when the two works, or readings of them, are held and the
steps are checked against them.
