---
status: Open
title: 'For finitely many states, does "at least as informative in every bounded decision problem" imply simulation by a Markov kernel when the simulated experiment''s outcome space is not standard Borel?'
version: 1
tags:
- mathematical-statistics
- mathematics
date: '2026-10-29'
line: pragmatic-transport
summary: >-
  The part of the promotion condition formerly on [THEORY-156](../theory.d/THEORY-156.md) that the
  twelfth status review's re-derivation does not reach. Blackwell (1953),
  [LIT-781](../literature.d/LIT-781.md), claims the equivalence for arbitrary outcome spaces through its
  Theorem 2, quoted from Blackwell (1951), which the record has not read.
  The record's proof needs a regular conditional distribution of the
  simulated experiment's outcome given its posterior, so [THEORY-156](../theory.d/THEORY-156.md) was
  narrowed to standard Borel spaces and promoted.
---
<!-- inactive-ok-file: LIT-778 — Unavailable; named as a route to an answer, not leaned on -->

# QUESTION-tmpeep5e: For finitely many states, does "at least as informative in every bounded decision problem" imply simulation by a Markov kernel when the simulated experiment's outcome space is not standard Borel?

## Why it is a question

[THEORY-156](../theory.d/THEORY-156.md)'s note of 2026-10-29 re-derives Blackwell's converse in three
steps: the convex order of the standard measures, a martingale coupling of
them, and a garbling built from the coupling. Only the last step uses the
outcome space: it composes the coupling's kernel with the conditional law of
the simulated experiment's outcome given its posterior, and that law exists
as a kernel when the space is standard Borel. Blackwell (1953) claims the
equivalence for any measurable space, resting on Theorem 2 of his 1951
paper, which the record holds only as quoted. Whether a Markov kernel always
exists without that regularity, or only a randomisation in Le Cam's
operator sense, is open here.

## What would answer it

Blackwell (1951)'s proof of Theorem 2 read and checked, or a treatment of
randomisations that settles when they are given by kernels, such as
Torgersen's book ([LIT-778](../literature.d/LIT-778.md)) or Le Cam's. A counterexample would also answer
it: two experiments on finitely many states, the second on a space that is
not standard Borel, where the first does at least as well in every bounded
problem and no Markov kernel turns its outcome into the second's.
Restatements in surveys do not count.
