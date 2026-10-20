---
number: 197
status: Open
formerly:
- QUESTION-tmpucqdf
title: "Is there a variant of the Döring–Isham rules, or of the context category, under which tensor-product composites of quantum systems satisfy the translation condition?"
version: 1
tags:
- quantum-foundations
- mathematics
- mereology
date: '2026-10-19'
line: 'formal-apparatus'
summary: >-
  Filed when the promotion audit (batch 044, [ADR-047](../decisions.d/ADR-047.md) v2) proved, for
  finite dimensions, the failure that THEORY-585 had held as asserted: along
  a tensor product the pull-back of a non-scalar quantity disagrees with the
  composite's quantity at some context, and no operator realises it. The
  former promote_when's refutation route, a variant of the rules that
  repairs the composite, is held here.
---

# QUESTION-197: Is there a variant of the Döring–Isham rules, or of the context category, under which tensor-product composites of quantum systems satisfy the translation condition?

## Why it is a question

[THEORY-585](../theory.d/THEORY-585.md) now states a theorem about Döring and Isham's scheme ([LIT-310](../literature.d/LIT-310.md)):
for finite-dimensional systems, the pull-back of a constituent's quantity
agrees with the composite's own quantity at a context exactly when every
projection in the context with proper support on the first factor has the
form P⊗1, so it fails for every non-scalar quantity, and no operator on the
composite realises the pull-back. That is a result about these rules: the
functor W ↦ V_W, outer daseinisation, and a context category augmented with
the trivial algebra. The authors call the rules "partly experimental", and
the trivial-system rule conflicts with the series' own definition of
contexts. Whether some other choice repairs the composite is open, and so
is the infinite-dimensional case.

## What would answer it

A variant of the rules or of the context category, for instance a
different pull-back functor or a different daseinisation, under which the
translation condition holds for tensor products would answer it yes, and
would bear on what [THEORY-585](../theory.d/THEORY-585.md)'s failure is a failure of. A proof that no
pull-back of the scheme's general kind satisfies the condition for
H₁⊗H₂ would answer it no. A further check on disjoint sums cannot settle
it: they already compose exactly.
