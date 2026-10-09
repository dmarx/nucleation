---
number: 156
status: Proposed
formerly:
- THEORY-tmpl07kz
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
date: '2026-10-09'
source:
- LIT-781
summary: >-
  Blackwell (1953), [LIT-781](../literature.d/LIT-781.md), Theorem 8 with Theorems 1–3: for
  experiments with finitely many states and decision problems with bounded
  losses, α attains every loss vector β attains, in every problem, exactly
  when a Markov kernel turns α's observation into β's under every state.
  The direction from simulation to informativeness is Blackwell (1951); the
  finite converse is Sherman and Stein (1951); the general converse is
  proved in 1953. It is a qualitative order and says nothing about how much
  worse an incomparable experiment is.
supports:
- CLAIM-tmpek80j
---

# THEORY-156: For experiments on a finite parameter set, being at least as informative for every decision problem is the same as being able to simulate the other by a randomisation

## Source

Blackwell (1953), [LIT-781](../literature.d/LIT-781.md), Theorems 1–8, as read in [NOTE-595](../notes.d/NOTE-595.md).

## What was actually shown

An experiment is an n-tuple of probability measures on a common space, one
per state. α is "more informative" than β (α ⊃ β) if, for every closed
bounded convex set A of loss vectors, every risk vector attainable with β
is attainable with α. α is "sufficient for" β (α ≻ β) if there is a
stochastic transformation T with T m_i = M_i for every state i: β is a
garbling of α.

≻ implies ⊃ by Jensen's inequality (Theorem 3, from Blackwell 1951). For
finite outcome spaces the converse is a minimax argument: the defect
Q − PM of the best Markov matrix M costs nothing against any decision
matrix, so it vanishes (Theorem 6, Sherman–Stein, new proof). For arbitrary
outcome spaces, both orders reduce to a comparison of standard measures on
the simplex (Theorems 1 and 2, quoted), where ⊃ is the convex order and ≻
is a mean-preserving transformation; Theorem 8 proves convex order implies
such a transformation on any bounded subset of ℝⁿ by finite approximation
and martingale convergence. The support is proof, not experiment: what
could show it wrong is an error in a step, so the promotion condition asks
for a checked second proof, and for the two quoted results to be checked
at their source.

For two states the order is decided by testing problems alone: α ≻ β iff
α's least type II error at every level t is at most β's (Theorem 10 and its
Corollary).

## What this does not say

- **Not a measure.** Most pairs of experiments are incomparable; the
  theorem says nothing about how much information is lost when neither
  simulates the other. That quantitative question is Le Cam's deficiency
  ([LIT-778](../literature.d/LIT-778.md), not read).
- **Not for infinitely many states**, and not for unbounded losses, as
  proved here.
- **Not "finitely many decision problems suffice".** The k-action
  comparisons ≻_k are weaker than ≻ in general (asserted from Stein's
  unpublished work); only for two states does k = 2 suffice.
- **Not that the simulating kernel is constructive or unique**; Theorem 8's
  kernel comes from a compactness and limit argument.
- **Not a statement about any particular informativeness functional.**
  That a quantity such as mutual information or an f-divergence is
  monotone under garbling is a consequence one may draw, but the paper
  states only the convex-function criterion of Theorem 1.
