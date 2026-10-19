---
number: 717
status: Active
formerly:
- THEORY-tmp2m4ke
title: 'For experiments with finitely many states and finitely many outcomes, being at least as informative in every decision problem is the same as being reproducible from the other by a Markov matrix'
version: 1
history:
- version: 1
  date: '2026-10-19'
  note: >-
    Split from THEORY-156 and filed Active at the owner's direction, from
    the second pass of the owner's promotion audit of 2026-10-19.
    THEORY-156's promote_when asks for a second proof of the arbitrary-
    outcome case, or a check of the 1951 results that the 1953 proof
    quotes. Neither is needed for finite outcome spaces, where Blackwell
    (1953) proves the converse in full by a minimax argument (Theorems 4–6),
    and NOTE-595 followed that proof step by step. The other direction is
    a one-line argument, given below in matrix form, so it does not rest on
    the quoted Theorems 1–2. THEORY-156 keeps the general case and extends
    this one.
tags:
- mathematical-statistics
- information-theory
- mathematics
date: '2026-10-19'
source:
- LIT-781
summary: >-
  Blackwell (1953), [LIT-781](../literature.d/LIT-781.md), Theorems 4–6, read in [NOTE-595](../notes.d/NOTE-595.md): the Sherman–
  Stein theorem, with a new minimax proof. With n states and finite
  outcome sets, write experiments as n × N Markov matrices P and Q. Every
  risk vector Q attains in every decision problem is attainable with P
  exactly when Q = PM for some Markov matrix M. The arbitrary-outcome
  extension is [THEORY-156](THEORY-156.md), still Proposed. A qualitative order: most pairs
  are incomparable, and it says nothing about how far apart they are.
extended_by:
- THEORY-156
supports:
- CLAIM-237
- CLAIM-323
- CLAIM-326
- CLAIM-tmpew698
- CLAIM-tmppwjei
---
<!-- inactive-ok-file: THEORY-156 — Proposed; the general case this one was split from and that extends it, cited as open -->
<!-- inactive-ok-file: LIT-778 — Unavailable; named as where the quantitative question lives, not read -->

# THEORY-717: For experiments with finitely many states and finitely many outcomes, being at least as informative in every decision problem is the same as being reproducible from the other by a Markov matrix

## Source

Blackwell (1953), [LIT-781](../literature.d/LIT-781.md), Theorems 4–6, as read in [NOTE-595](../notes.d/NOTE-595.md) (its claim
C1, "strong (proof)"). The finite converse is Sherman and Stein's (1951),
and the paper gives a new proof of it.

## What was actually shown

An experiment with n states and N outcomes is an n × N Markov matrix P,
whose row i is the outcome distribution under state i. A decision rule
with k actions is an N × k Markov matrix D, and with losses L its risk in
state i is (PDLᵀ)ᵢᵢ. P ⊃ Q (P is at least as informative) when every risk
vector attainable with Q is attainable with P, for every decision problem.
P ≻ Q when Q = PM for a Markov matrix M (Theorem 5).

- **≻ implies ⊃.** If Q = PM and D is a rule for Q, then MD is a rule for
  P, and PMD = QD, so it attains the same risks. The record writes this
  out directly, without the paper's Theorem 3, which runs through the
  quoted Theorems 1–2.
- **⊃ implies ≻ (Theorem 6).** The bilinear function
  h(D, M) = Trace((Q − PM)D), over Markov matrices M and matrices D with
  entries in [0, 1], has a saddle point (Bohnenblust, Karlin and Shapley).
  Theorem 4 uses P ⊃ Q to make its value at most 0. So, at the saddle point,
  U = Q − PM₀ has no positive entry. Its entries sum to 0, because Q and
  PM₀ are both Markov, so U = 0.

The support is a proof. What could show it wrong is an error in a step,
and [NOTE-595](../notes.d/NOTE-595.md) followed each step.

## What this does not say

- **Anything for infinite outcome spaces.** That case is Theorem 8, which
  rests on Theorems 1–2, quoted from 1951 and not proved in the paper. It
  is [THEORY-156](THEORY-156.md), which is Proposed until those results are checked or a
  second proof is read.
- **Not a measure.** It decides whether one experiment can simulate the
  other. When neither can, it says nothing about how much is lost, which
  is Le Cam's deficiency ([LIT-778](../literature.d/LIT-778.md), not read).
- **Not for infinitely many states.**
- **Not that M is unique or explicit.** M comes out of the saddle point.
- **Not a statement about a particular functional.** That mutual
  information or an f-divergence can only fall under garbling follows
  from ≻. It is not the order.
