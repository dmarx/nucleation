---
status: Proposed
promote_when: >-
  A second, independent proof of the general (arbitrary outcome space) case
  is read and checked, such as the treatment in Torgersen's book or Le
  Cam's deficiency theory specialised to deficiency zero, or the 1953 proof
  is checked together with the 1951 proofs of the two results it quotes.
  Restatements in surveys do not count.
title: 'For experiments on a finite parameter set, being at least as informative for every decision problem is the same as being able to simulate the other by a randomisation'
version: 1
tags:
- mathematical-statistics
- information-theory
- mathematics
date: '2026-10-30'
source:
- LIT-781
extends:
- THEORY-156
bears_on:
- QUESTION-321
summary: >-
  The wide form [THEORY-156](THEORY-156.md) held before the twelfth status review narrowed
  it, kept as a Proposed reading by the [ADR-047](../decisions.d/ADR-047.md) kind-1 sweep of 2026-10-30:
  the source asserts it, and [THEORY-156](THEORY-156.md), Active, is its evidence.
  Blackwell (1953), [LIT-781](../literature.d/LIT-781.md), claims the equivalence for any outcome space,
  through Theorem 2, quoted from his 1951 paper. The record's
  re-derivation reaches only outcome spaces that are standard Borel, since
  its last step needs a regular conditional distribution.
---

# THEORY-tmp93zbe: For experiments on a finite parameter set, being at least as informative for every decision problem is the same as being able to simulate the other by a randomisation

## Source

Blackwell (1953), [LIT-781](../literature.d/LIT-781.md), Theorems 1 to 8, as read in [NOTE-595](../notes.d/NOTE-595.md). The
finite-outcome case is [THEORY-717](THEORY-717.md), and the case of a simulated experiment
whose outcome space is standard Borel is [THEORY-156](THEORY-156.md), which this entry
extends. Both are Active.

## The claim

For experiments with finitely many states and decision problems with
bounded losses, α does at least as well as β in every problem exactly
when a Markov kernel turns α's observation into one distributed as β's
under every state, whatever the outcome spaces. The paper reaches the
general case by reducing both orders to a comparison of standard measures
on the simplex (Theorems 1 and 2, quoted from Blackwell 1951), and proving
in Theorem 8 that the convex order there gives a mean-preserving
transformation.

[THEORY-156](THEORY-156.md)'s note of 2026-10-29 re-derives the converse without the 1951
results. Its last step composes a martingale coupling with the
conditional law of β's outcome given its posterior, which is a kernel
when β's outcome space is standard Borel. Without that regularity the
record has only the paper's word, resting on a theorem it holds as
quoted.

## What would settle it

The promote_when, carried over unchanged: a second, independent proof of
the arbitrary-outcome case read and checked, or the 1953 proof checked
together with the 1951 proofs of the two results it quotes. [QUESTION-321](../questions.d/QUESTION-321.md)
asks the same thing as a question, and adds that a counterexample, an
outcome space that is not standard Borel where no Markov kernel exists,
would answer it the other way.
