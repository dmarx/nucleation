---
status: Proposed
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
  object-centered baselines. [CLAIM-tmpscv6b](CLAIM-tmpscv6b.md) qualifies that for
  T2I-CompBench.
objected_by:
- CLAIM-tmpscv6b
illustrated_by:
- CASE-tmp4sjw7
---

# CLAIM-tmp33gkh: Existing text-to-image benchmarks evaluate object presence and attributes, and need extending to pragmatically consequential relations and social uptake

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

T2I-CompBench++ (LIT-tmp76md3) adds numeracy and 3D spatial relations, and
nothing social or pragmatic. The gap this claim names is still open.
