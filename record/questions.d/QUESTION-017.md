---
number: 17
status: Open
formerly:
- QUESTION-tmpklhva
title: 'What bound on accumulated drift holds when distortion is directed and need not satisfy the triangle inequality?'
version: 1
tags:
- mathematics
- philosophy-of-language
date: '2026-10-08'
line: pragmatic-transport
refines:
- QUESTION-002
summary: >-
  A50 derived drift bounds assuming a metric, and in the same reply
  dropped symmetry and the triangle inequality for distortion. The
  tension was never resolved; the manuscript states its recursion "in
  the chosen metric".
answered_by:
- CLAIM-260
refined_by:
- QUESTION-074
---
<!-- inactive-ok-file: CLAIM-059 CLAIM-106 CLAIM-186 THEORY-161 — listed as material that may bear on this question, not as settled -->
<!-- inactive-ok-file: CLAIM-056 — Proposed; open, and cited as open: the claim, argument or reading is under test, not settled -->

# QUESTION-017: What bound on accumulated drift holds when distortion is directed and need not satisfy the triangle inequality?

## Why it is a question

A50 §2 bounded drift "assuming a metric": d(u_0,u_2) ≤ 2ε, and the recursion
e_(i+1) ≤ L_i e_i + ε_i ([CLAIM-056](../claims.d/CLAIM-056.md)). A50 §4, a few paragraphs later, argued that
pragmatic distortion is directed, D(u⇝v) ≠ D(v⇝u), and "I'd also avoid
requiring a triangle inequality unless a particular operational distance
actually satisfies one." A52 4.2 hedged with "observational pseudometric or
explicitly defined divergence", and 5.2 kept "Under a metric". The manuscript
§8 says "Lipschitz with constant κ_i in the chosen metric" and, for stochastic
kernels, uses total variation.

C6 Appendix B (U32) stated the directed case outright: the distortion "is
directed, need not be invertible, and does not obey a triangle inequality unless
the chosen constructions guarantee one", while its Appendix D bound assumes "d a
metric on target probability distributions". The manuscript drops the first
sentence and keeps the second.

## What would count as an answer

A bound stated for a named class of divergences: for instance a weak triangle
inequality with a constant, or a statement that the recursion needs only a
metric on the target state-distributions while the communicative distortion
may be directed. Or a showing that no useful compositional bound survives
without one.

## Note of 2026-10-11: material in the record that may bear on this

A synthesis review of 2026-10-11 found these entries bearing on this
question without being linked to it. Each is listed for what its title
says; none has yet been assessed as an answer, and none is linked by
`answers`.

- [CLAIM-106](../claims.d/CLAIM-106.md): Pragmatic fidelity is a graded, potentially asymmetric
  property of transport, not an equivalence relation;…
- [CLAIM-059](../claims.d/CLAIM-059.md): Repeated reconstruction has three regimes, contracting toward
  conventions, neutral accumulation and…
- [CLAIM-186](../claims.d/CLAIM-186.md): How fast an argument grows sets how it grows: drift tracks
  how fast new material arrives relative to how…
- [THEORY-161](../theory.d/THEORY-161.md): In the semantic rate–distortion frameworks of 2021–2025,
  meaning is a latent variable with a known joint…

## Note of 2026-10-12: a partial answer filed on 2026-10-10

[CLAIM-260](../claims.d/CLAIM-260.md), granted in PR [#121](https://github.com/dmarx/nucleation/issues/121), is now linked as a partial answer. It
shows that the composite of an ε₁-transport and an ε₂-transport is an (ε₁
+ ε₂)-transport when the distortion obeys a triangle inequality and the
later kernel is nonexpansive, and that in total variation both hold.
Without a triangle inequality the additive bound can fail: under squared
Hellinger distance two steps of about 0.29 compose to 1. It is partial: it
says where the additive bound fails, not what weaker bound holds there,
and it does not treat directed distortion.
