---
status: Proposed
title: 'Information-bottleneck nesting computed by lower convex envelopes on simplex grids: decoder intervals widened with β on all 300 random sources with two distinct rows of p(Y|x) and up to six outputs, consecutive optima of random three-row sources failed the hull test for 28 of 150 at an L1 distance above 0.05, and grid envelopes of twelve products never fell below the sum of their factors'' envelopes'
version: 1
standing: documented
kind: executed-study
tags:
- information-theory
- mathematics
date: '2026-11-22'
line:
- learned-structure
- formal-apparatus
bears_on:
- QUESTION-220
illustrates:
- CLAIM-tmp8xj7x
- CLAIM-tmplxbtx
draws_on:
- THEORY-753
summary: >-
  Run on 2026-11-22 for [LEAD-039](../leads.d/LEAD-039.md) (scratch/studies/lead-039/, on the branch
  claude/lead-039-ib-nesting), with numpy and scipy; six pytest checks
  pass, one of them reproducing [CLAIM-392](../claims.d/CLAIM-392.md)'s optima and failed hull test.
  It checks [CLAIM-tmp8xj7x](../claims.d/CLAIM-tmp8xj7x.md) on random two-row sources, measures how often
  three-row sources fail to nest, and checks the tensorization step of
  [CLAIM-tmplxbtx](../claims.d/CLAIM-tmplxbtx.md). The optima are exact on the grid and not certified
  unique, so the failure counts are evidence, not proofs. The wording is
  the assistant's (Claude, in this session); adopting it is the owner's
  call.
---
<!-- inactive-ok-file: CLAIM-tmp8xj7x CLAIM-tmplxbtx CLAIM-tmpzohh5 — new; the claims this study checks or cites, filed with it from LEAD-039 -->

# CASE-tmpo9u3y: Information-bottleneck nesting computed by lower convex envelopes on simplex grids: decoder intervals widened with β on all 300 random sources with two distinct rows of p(Y|x) and up to six outputs, consecutive optima of random three-row sources failed the hull test for 28 of 150 at an L1 distance above 0.05, and grid envelopes of twelve products never fell below the sum of their factors' envelopes

## The case

**Method.** A Lagrangian optimum at β is a decomposition of p(X) on the
lower convex envelope of F_β(r) = H(κᵀr) − H(r)/β ([THEORY-753](../theory.d/THEORY-753.md), step 5).
On a grid of the simplex of X, the envelope is the lower hull of the lifted
grid points (scipy's Qhull; a monotone chain in one dimension), and the
facet containing p(X) gives the decoder points. Nesting between two optima
is [THEORY-753](../theory.d/THEORY-753.md)'s hull test, here the L1 distance of the coarse decoder
points from the fine hull, by linear programming. On [CLAIM-387](../claims.d/CLAIM-387.md)'s source,
reduced to its three distinct rows, the grid of spacing 1/240 reproduces
[CLAIM-392](../claims.d/CLAIM-392.md)'s figures (I(X; T) = 0.546 and 0.952 bits, I(T; Y) = 0.097 and
0.139 bits at β = 8 and 12) and its failed test.

**Results** (scratch/studies/lead-039/results.md):

1. **Two distinct rows (S1).** 300 random sources, two rows drawn from a
   Dirichlet(0.7) on two to six outputs (30% with a zero entry), P(C = 1)
   uniform on [0.05, 0.95], 40 values of β from 1.05 to 80, grid 1/4000.
   The decoder interval at each β contained the one before it on every
   source, with largest violation 0 (tolerance two grid steps). On average
   27.7 of the 40 values of β had a nontrivial optimum. This is what
   [CLAIM-tmp8xj7x](../claims.d/CLAIM-tmp8xj7x.md) predicts. The concavity of φ on which it rests held on
   200 random channels of two to six outputs, in the test suite.
2. **Three distinct rows (S2).** 150 random sources, p(X) from
   Dirichlet(2), rows from Dirichlet(0.7), half with binary Y and half
   with ternary Y, 16 values of β from 1.5 to 60, grid 1/300. Sources with
   some consecutive pair failing the hull test:

   | L1 threshold | binary Y (75) | ternary Y (75) |
   |---|---|---|
   | 0.01 | 45 | 41 |
   | 0.02 | 26 | 27 |
   | 0.05 | 13 | 15 |

   At 0.05, 2 and 0 sources failed for pairs five steps of β apart, and 61
   and 60 had no failure at all. The three largest failures kept their
   size on a grid of 1/700 (0.30 → 0.27, 0.18 → 0.18, 0.16 → 0.16). In
   them the optimum has two decoder points, a segment through p(X), and the
   segment turns as β grows: the hull grows in one direction and loses
   another.
3. **Products (S3).** Twelve products of two independent two-row pairs,
   four inputs and four to nine outputs, at β = 2, 4, 8 and 16, on a grid
   of 1/40 of the three-dimensional simplex. The grid envelope at p(X)
   minus the sum of the factors' envelopes (each on a grid of 1/4000)
   ranged from −2 × 10⁻¹⁶ to 1.9 × 10⁻³: never below, as the
   tensorization in [CLAIM-tmplxbtx](../claims.d/CLAIM-tmplxbtx.md) requires, and within the coarse grid's
   error above.

## What it shows and does not

- It is consistent with both theorems and found no exception to either.
  The theorems do not rest on it.
- **Failure with three rows is common, not exotic.** Between a fifth and
  a third of random three-row sources showed a clear failure between
  consecutive budgets on this coarse grid of β, mostly at nearby budgets,
  as [CLAIM-392](../claims.d/CLAIM-392.md)'s reader found. This is why the structural condition stops
  at two rows or products.
- **Not certified.** The optima are grid-exact, not proved globally
  unique as [CLAIM-392](../claims.d/CLAIM-392.md)'s are, and a failure below about 0.01 is within grid
  error. A source counted as never failing was checked only at 16 values
  of β.
- The size of the loss in the failing sources was not computed.
  [CLAIM-tmpzohh5](../claims.d/CLAIM-tmpzohh5.md) bounds it.
