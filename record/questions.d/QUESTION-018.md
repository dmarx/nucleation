---
number: 18
status: Open
formerly:
- QUESTION-tmpklyn0
title: 'When a generator receives several conditions, what determines whether it preserves their conjunction and relational bindings?'
version: 1
tags:
- compositionality
- probabilistic-modeling
date: '2026-10-08'
line: pragmatic-transport
refines:
- QUESTION-002
summary: >-
  The fourth of the five central questions (A110 §IX). The manuscript
  states the failure (§7) and its benchmarks (§10) but not the question.
---
<!-- inactive-ok-file: CLAIM-013 — listed as material that may bear on this question, not as settled -->
<!-- inactive-ok-file: THEORY-250 — Proposed; filed today, cited as evidence about the explanandum, not as an answer -->

# QUESTION-018: When a generator receives several conditions, what determines whether it preserves their conjunction and relational bindings?

## Why it is a question

A110 §IX.4: "When a generative model receives multiple conditions, what determines
whether it preserves their conjunction and relational bindings? Compare constraint
satisfaction, local empirical distributions, and compatibility across measurement
contexts."

## Where it stands

The manuscript §7 says each condition can be met while the conjunction fails ([CLAIM-321](../claims.d/CLAIM-321.md)), and
that score addition composes conditions only under conditional independence at
the noisy state. [CLAIM-123](../claims.d/CLAIM-123.md), corrected on 2026-10-19, states the exact
condition: the scores add when p(y₁,y₂|x)/(p(y₁|x)p(y₂|x)) does not vary with
the noisy state x, which conditional independence is sufficient for but does
not require. C7 Appendix D adds that the identity "is not a generic
identity for arbitrary prompt embeddings or finite-step diffusion
implementations", and that failures "may reflect estimator error, model
misspecification, or sampling limitations". Which of these explains a given
relational failure is the open part. [CASE-004](../cases.d/CASE-004.md) is the case.

## Note of 2026-10-11: material in the record that may bear on this

A synthesis review of 2026-10-11 found these entries bearing on this
question without being linked to it. Each is listed for what its title
says; none has yet been assessed as an answer, and none is linked by
`answers`.

- [THEORY-117](../theory.d/THEORY-117.md): Compositional generalization comes from diversity of
  combinations, not data volume: in vision models…
- [CLAIM-097](../claims.d/CLAIM-097.md): T2I-CompBench is not purely object-centered: its non-spatial
  relation category already probes…
- [CLAIM-013](../claims.d/CLAIM-013.md): Existing text-to-image benchmarks evaluate object presence
  and attributes, and need extending to…

## Note of 2026-10-14: a measurement of the failure

[THEORY-250](../theory.d/THEORY-250.md), filed from [LIT-938](../literature.d/LIT-938.md), measures that DALL-E 3's relational
bindings fail when an asymmetric relation is reversed and when relations
are combined, and that the failures are mostly wrong or role-swapped
relations, not missing objects. Low prior plausibility correlates only
weakly (r = 0.09). It does not separate the candidate explanations above,
so it is evidence about the explanandum, not an answer, and it carries no
`answers` edge.
