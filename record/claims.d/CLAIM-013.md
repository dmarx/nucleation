---
number: 13
status: Proposed
formerly:
- CLAIM-tmp33gkh
title: 'Existing text-to-image benchmarks evaluate object presence and attributes, and need extending to pragmatically consequential relations and social uptake'
version: 1
role: thesis
defeated_if: >-
  An existing benchmark that already measures social alignment, stance
  or uptake in generated images with metrics validated against human
  judgement.
tags:
- compositionality
- philosophy-of-language
date: '2026-10-09'
line: pragmatic-transport
works:
- what-survives-translation
grounds:
- LIT-782
- LIT-783
summary: >-
  The manuscript's §10, Case III, which calls T2I-CompBench and GenEval
  object-centered baselines. [CLAIM-097](CLAIM-097.md) qualifies that for
  T2I-CompBench.
objected_by:
- CLAIM-097
illustrated_by:
- CASE-004
---
<!-- inactive-ok-file: THEORY-tmp8v4zu — Proposed; filed today, cited for what LIT-938 measures, not leaned on -->

# CLAIM-013: Existing text-to-image benchmarks evaluate object presence and attributes, and need extending to pragmatically consequential relations and social uptake

## The claim

Case III holds people, objects and actions fixed and varies social alignment
and communicative purpose, then compares text→image→caption chains with
text-only chains. GenEval and T2I-CompBench are named as the object-centered
baselines the proposal extends.

## What it does not say

Both readings ([NOTE-593](../notes.d/NOTE-593.md) for GenEval, [NOTE-592](../notes.d/NOTE-592.md) for T2I-CompBench) support the
premise behind the proposal: embedding similarity (CLIPScore) tracks human
judgements of counting, position and binding worse than detector-based or
per-pair checks.

## Since the journal version

T2I-CompBench++ ([LIT-798](../literature.d/LIT-798.md)) adds numeracy and 3D spatial relations, and
nothing social or pragmatic. The gap this claim names is still open.

Fu et al. ([LIT-938](../literature.d/LIT-938.md), read in [NOTE-tmpv2vga](../notes.d/NOTE-tmpv2vga.md); [THEORY-tmp8v4zu](../theory.d/THEORY-tmp8v4zu.md)) qualify it as
[CLAIM-097](CLAIM-097.md) does. Theirs is a relational benchmark scored by human raters,
including agentic relations (helping, hindering, chasing), so not every
existing benchmark is object-centered. It does not reach the pragmatic
consequence or social uptake this claim asks for.
