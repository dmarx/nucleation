---
status: Proposed
title: 'Crutchfield and Feldman show that for a stationary process on a finite alphabet the excess entropy, the summed excess of the finite-L entropy-rate estimates over the entropy rate, equals both the subextensive part of the block entropy and the mutual information between past and future, is bounded below by its finite-block estimates, and is finite for finitary processes, whose estimates fall faster than 1/L; that an observer who ignores it at block length L overestimates the entropy rate by E/L; and that it does not fix the structure of a process, which the transient information and the number of causal states can separate where the excess entropy cannot'
promote_when: >-
  A second reading (Shalizi and Crutchfield, LIT-1126, or a textbook
  treatment) confirms the identities E = lim [H(L) − hµL] = I(past;
  future) and the E/L overestimate, and Theorem 1 is checked on one
  example (for instance the golden mean process, R = 1: S = T + hµ).
version: 1
tags:
- information-theory
- complex-systems
date: '2026-11-22'
source:
- LIT-3010
bears_on:
- QUESTION-517
corroborates:
- CLAIM-805
summary: >-
  Crutchfield and Feldman (2003), LIT-3010, read from the 2001 arXiv
  preprint in NOTE-tmpe86ty. One derivative-and-integral hierarchy of the
  block entropy gathers the entropy rate, the predictability gain, the
  excess entropy and a new transient information. Excess entropy is "one
  kind of memory": equal for processes the transient information tells
  apart, and small for a source whose optimal predictor has infinitely
  many states. Drawn on by TERM-141; corroborates CLAIM-805's separation
  of entropy from memory.
---
<!-- inactive-ok-file: TERM-141 CLAIM-805 — Proposed; the term that draws on this reading and the claim it corroborates -->
<!-- inactive-ok-file: THEORY-2151 THEORY-784 — Proposed; readings this account parallels -->

# THEORY-tmpl7rgc: Crutchfield and Feldman show that for a stationary process on a finite alphabet the excess entropy, the summed excess of the finite-L entropy-rate estimates over the entropy rate, equals both the subextensive part of the block entropy and the mutual information between past and future, is bounded below by its finite-block estimates, and is finite for finitary processes, whose estimates fall faster than 1/L; that an observer who ignores it at block length L overestimates the entropy rate by E/L; and that it does not fix the structure of a process, which the transient information and the number of causal states can separate where the excess entropy cannot

## Source

Crutchfield and Feldman, "Regularities Unseen, Randomness Observed:
Levels of Entropy Convergence", Chaos 13, 25–54 (2003), LIT-3010, read
from the arXiv v1 preprint of cond-mat/0102181 (2001) in NOTE-tmpe86ty.

## What was actually shown

- E ≡ Σ_L [hµ(L) − hµ] (Eq. 48); "The excess entropy is the subextensive
  part of H(L): E = lim [H(L) − hµL]" (Prop. 7); E is the mutual
  information between the semi-infinite past and future, when the limit
  exists (Prop. 8).
- E′(L) ≤ E(L) ≤ E (Lemma 3), for the half-block mutual information
  E′(L) and E(L) = H(L) − L hµ(L).
- Finitary (E finite, Def. 1): hµ(L) − hµ < A/L (Prop. 9); "For
  infinitary processes hµ(L) decays at or slower than 1/L".
- Period p gives E = log2 p (Prop. 10); order-R Markov gives E = H(R) −
  Rhµ (Prop. 11).
- When synchronized, h′µ(L) − hµ = E/L: "E bits of memory are converted
  into additional, apparent randomness" (Prop. 13); assuming
  synchronization too early understates both hµ and E (Prop. 15).
- Theorem 1: for block-Markov processes the synchronization information
  is S = T + ½R(R + 1)hµ.
- E does not fix structure: the three period-5 processes share E = log2 5
  and differ in T (4.073, 5.273, 4.873 bit-symbols); the golden mean,
  RRXOR and even processes share hµ and differ in E (about 0.2516, 2 and
  0.902 bits); the simple nondeterministic source has E ≈ 0.147 bits and
  an optimal deterministic predictor with "an infinite number of states".
- Thue–Morse: hµ = 0, "the excess entropy diverges; E(L) ∝ log2 L,
  indicating an infinite-memory process".

What could have failed: the identities are proved; the claims about
structure could have failed if processes with equal E had equal T, or if
every finite-E source had finitely many causal states; the examples show
neither holds.

## What this does not say

- Nothing on estimation from data: block probabilities are assumed known.
- Not exponential convergence for finitary hidden Markov processes in
  general: "there is not a direct proof of exponential decay for more
  general finitary processes".
- Not the structure itself: "specifying how this memory is organized
  cannot be done within the framework of information theory".
- Not criticality: the Ising exponents it reports are Bialek and
  colleagues'.
- Not two dimensions, where the expressions "yield different results".

## Connections

Drawn on by TERM-141. Corroborates CLAIM-805 (entropy and memory are
distinct). Parallel to NOTE-1372 (Shalizi and Crutchfield, excess entropy
a lower bound on stored memory) and to THEORY-2151 (Bialek and
colleagues' predictive information, the same quantity). Bears on
QUESTION-517 and LEAD-208 (two-dimensional definitions diverge), and on
NOTE-689 and THEORY-784 (language's power-law entropy convergence is
infinitary).
