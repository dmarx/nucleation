---
status: Open
title: 'When a generator receives several conditions, what determines whether it preserves their conjunction and relational bindings?'
version: 1
tags:
- compositionality
- probabilistic-modeling
date: '2026-10-08'
line: pragmatic-transport
refines:
- QUESTION-tmp3lk3n
summary: >-
  The fourth of the five central questions (A110 §IX). The manuscript
  states the failure (§7) and its benchmarks (§10) but not the question.
---
<!-- inactive-ok-file: CLAIM-tmpzkhdr — Proposed; open, and cited as open: the claim, argument or reading is under test, not settled -->

# QUESTION-tmpklyn0: When a generator receives several conditions, what determines whether it preserves their conjunction and relational bindings?

## Why it is a question

A110 §IX.4: "When a generative model receives multiple conditions, what determines
whether it preserves their conjunction and relational bindings? Compare constraint
satisfaction, local empirical distributions, and compatibility across measurement
contexts."

## Where it stands

The manuscript §7 says each condition can be met while the conjunction fails, and
that score addition composes conditions only under conditional independence at
the noisy state ([CLAIM-tmpzkhdr](../claims.d/CLAIM-tmpzkhdr.md)). C7 Appendix D adds that the identity "is not a generic
identity for arbitrary prompt embeddings or finite-step diffusion
implementations", and that failures "may reflect estimator error, model
misspecification, or sampling limitations". Which of these explains a given
relational failure is the open part. [CASE-tmp4sjw7](../cases.d/CASE-tmp4sjw7.md) is the case.
