---
number: 13
status: Proposed
formerly:
- CLAIM-tmp33gkh
title: 'Existing text-to-image benchmarks evaluate object presence, attributes and whether spatial or interactive relations are depicted, not the stance, social alignment or uptake an image conveys, and need extending to pragmatically consequential relations and social uptake'
version: 2
history:
- version: 2
  date: '2026-10-29'
  note: >-
    Narrowed at the seventh status review (ADR-057, ADR-059) to record
    CLAIM-097's concession: T2I-CompBench's non-spatial relation
    category already probes interactions, and Fu et al. (LIT-938) is a
    human-rated relational benchmark, so not every existing benchmark
    is object-centred. What none the record has read measures is
    stance, social alignment or uptake. Version 1's title read:
    Existing text-to-image benchmarks evaluate object presence and
    attributes, and need extending to pragmatically consequential
    relations and social uptake. THEORY-522 joins the grounds. The
    defeated_if is unchanged; it already names what the narrowed title
    says is missing.
role: thesis
warrant: interpretive
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
- THEORY-522
summary: >-
  The manuscript's §10, Case III, which calls T2I-CompBench and GenEval
  object-centered baselines. [CLAIM-097](CLAIM-097.md) qualifies that for
  T2I-CompBench.
objected_by:
- CLAIM-097
illustrated_by:
- CASE-004
---
<!-- inactive-ok-file: THEORY-250 — Proposed; filed today, cited for what LIT-938 measures, not leaned on -->

# CLAIM-013: Existing text-to-image benchmarks evaluate object presence, attributes and whether spatial or interactive relations are depicted, not the stance, social alignment or uptake an image conveys, and need extending to pragmatically consequential relations and social uptake

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

Fu et al. ([LIT-938](../literature.d/LIT-938.md), read in [NOTE-813](../notes.d/NOTE-813.md); [THEORY-250](../theory.d/THEORY-250.md)) qualify it as
[CLAIM-097](CLAIM-097.md) does. Theirs is a relational benchmark scored by human raters,
including agentic relations (helping, hindering, chasing), so not every
existing benchmark is object-centered. It does not reach the pragmatic
consequence or social uptake this claim asks for.

## Note of 2026-10-29: narrowed

The manuscript's §10 calls GenEval and T2I-CompBench object-centred. That
holds of GenEval and of T2I-CompBench's attribute and spatial categories. It
does not hold of its non-spatial category, whose rubric asks only whether
"actions, events and relationships" are portrayed (THEORY-522) and whose
human scores sit at 0.95–0.99, nor of Fu et al.'s agentic relations. The gap
the claim names is narrower, and it is still open.

## Note of 2026-10-29: what holds it back

The claim generalises over "existing benchmarks" from the four the record has
read (GenEval, T2I-CompBench and its journal version, Fu et al.), and no
survey in the record meets or rules out its defeat condition. Scoped to the
benchmarks the record has read, it would be a candidate for Active.
