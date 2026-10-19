---
status: Open
title: "Outside finite alphabets, is a variable-rate covering argument, rather than a change of measure alone, what yields data-dependent PAC-Bayes bounds?"
version: 1
tags:
- learning-theory
- information-theory
date: '2026-10-19'
line: 'learned-structure'
summary: >-
  Filed when the promotion audit (batch 036, [ADR-047](../decisions.d/ADR-047.md) v2) promoted
  [THEORY-263](../theory.d/THEORY-263.md). Its second clause was re-derived in general spaces by the
  disintegrated change of measure, with no coding argument. The former
  promote_when also asked for a second source deriving a PAC-Bayes bound
  from a variable-rate covering outside finite alphabets; this question
  holds that request.
---

# QUESTION-tmpk63cw: Outside finite alphabets, is a variable-rate covering argument, rather than a change of measure alone, what yields data-dependent PAC-Bayes bounds?

## Why it is a question

Sefidgaran and Zaidi ([LIT-233](../literature.d/LIT-233.md)) build their variable-size codes only for
finite alphabets (Theorem 2). Their general Theorems 3–5 are change of
measure plus Donsker–Varadhan, to which they give a compression reading
([NOTE-806](../notes.d/NOTE-806.md)). The audit's re-derivation of [THEORY-263](../theory.d/THEORY-263.md) shows that, with the
rate set to the pointwise information density against a fixed prior,
Theorem 1's bound follows from the disintegrated change of measure and a
subgaussian moment bound, in any measurable space. So in general spaces
the bound does not need the covering. Whether compression is nevertheless
the mechanism, in the sense that a covering construction exists there and
yields the same or a tighter bound, is open.

## What would answer it

A source that builds a variable-rate covering for continuous outputs and
derives a PAC-Bayes bound from it, with constants matching or improving
the change-of-measure bound, would answer it yes. A proof that no such
covering can match the change-of-measure bound outside finite alphabets
would answer it no. Whether either bound is tight or non-vacuous for
networks does not settle it.
