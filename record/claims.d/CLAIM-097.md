---
number: 97
status: Active
formerly:
- CLAIM-tmpscv6b
title: 'T2I-CompBench is not purely object-centered: its non-spatial relation category already probes interactions, but scores them with CLIPScore and near human ceiling'
version: 1
role: granted
warrant: empirical
tags:
- compositionality
date: '2026-10-09'
line: pragmatic-transport
works:
- what-survives-translation
grounds:
- LIT-783
objects_to:
- CLAIM-013
summary: >-
  From the reading of T2I-CompBench ([NOTE-592](../notes.d/NOTE-592.md)). The benchmark's
  interaction category is the nearest existing measurement of what Case
  III proposes, and its weaknesses are the manuscript's argument.
---
<!-- inactive-ok-file: THEORY-250 — Proposed; filed today, cited for what LIT-938 measures, not leaned on -->

# CLAIM-097: T2I-CompBench is not purely object-centered: its non-spatial relation category already probes interactions, but scores them with CLIPScore and near human ceiling

## The claim

T2I-CompBench has a non-spatial relation category (interactions such as
holding, wearing, looking at). Unlike its attribute and spatial categories, it
is scored by CLIPScore, which the same paper shows tracks human judgement
poorly, and human scores on it are near ceiling (0.95–0.99 for five of six
models). So an interaction benchmark exists, but one that cannot separate a
complicit exchange from a reprimand.

## What it does not say

It does not weaken Case III; it sharpens its positioning. The manuscript
should cite the non-spatial category as the baseline it extends, not describe
the benchmark as object-centered throughout.

## Since the journal version

In T2I-CompBench++ ([LIT-798](../literature.d/LIT-798.md)) the interaction category is judged by
GPT-4V, which matches human rankings better than CLIPScore (Kendall τ 0.48
against 0.25). The "scored by CLIPScore" half of this claim is true of the
conference version only. Human scores on the category are still 0.95–0.99,
so the near-ceiling half stands.

Fu et al. ([LIT-938](../literature.d/LIT-938.md), read in [NOTE-813](../notes.d/NOTE-813.md); [THEORY-250](../theory.d/THEORY-250.md)) extend the
point about automatic scoring to vision-language-model judges. In their
App. A.6, VLM judges correlate with human ratings of relational images at
r ≈ 0.43–0.56, against a human split-half reliability of 0.91.
