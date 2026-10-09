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
---
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
