---
number: 387
status: Active
formerly:
- CLAIM-tmphan8l
title: 'Optimal deterministic information-bottleneck partitions at two budgets need not be nested: with X uniform on four states and binary Y with P(Y=1|x) = (0, 0, 1/8, 3/8), the optimum is {0,1,2 | 3} for 6.91 < β < 9.26 and {0,1 | 2,3} for 9.26 < β < 16.06, two partitions neither of which refines the other'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the enumeration: for this joint distribution and the
  objective I(T;Y) − H(T)/β over deterministic encoders T = f(X), a β in
  either stated range at which some other partition scores higher.
tags:
- information-theory
- learning-theory
date: '2026-10-20'
line:
- learned-structure
- formal-apparatus
answers:
- QUESTION-220
grounds:
- LIT-1238
summary: >-
  Found by brute force in the reading of Equitz and Cover ([NOTE-988](../notes.d/NOTE-988.md))
  and re-run here from scratch. It answers the deterministic half of
  [QUESTION-220](../questions.d/QUESTION-220.md) in the negative: raising the budget can reorganize the
  optimal partition rather than split it. The two optima are not even
  laminar, so no fixed tree holds both as prunings, and [NOTE-676](../notes.d/NOTE-676.md)'s nesting
  is bought by its tree restriction. It says nothing about stochastic
  encoders, where finite-β optima generally live ([THEORY-743](../theory.d/THEORY-743.md)).
---
<!-- inactive-ok-file: THEORY-163 — Proposed; the annealed colour-naming hierarchy named for contrast, open -->
# CLAIM-387: Optimal deterministic information-bottleneck partitions at two budgets need not be nested: with X uniform on four states and binary Y with P(Y=1|x) = (0, 0, 1/8, 3/8), the optimum is {0,1,2 | 3} for 6.91 < β < 9.26 and {0,1 | 2,3} for 9.26 < β < 16.06, two partitions neither of which refines the other

## The claim

Let X be uniform on {0, 1, 2, 3}, and let Y be binary with
P(Y = 1 | x) = (0, 0, 1/8, 3/8). Over deterministic encoders T = f(X),
maximize I(T; Y) − H(T)/β. Since T is a function of X, H(T) = I(X; T),
so this is the information bottleneck restricted to partitions of X.
Enumerating all fifteen partitions, with β stepped by 0.01:

| β | optimal partition | H(T) | I(T; Y) |
|---|---|---|---|
| < 6.91 | {0,1,2,3} | 0 | 0 |
| 6.91 – 9.26 | {0,1,2 \| 3} | 0.811 | 0.1175 |
| 9.26 – 16.06 | {0,1 \| 2,3} | 1.000 | 0.1379 |
| > 16.06 | {0,1 \| 2 \| 3} | 1.500 | 0.1691 |

The second and third optima are incomparable: neither is a function of the
other. They also cross: {2} goes with {0, 1} in one and with {3} in the
other. So no rooted tree on the four states has both as prunings. The
reading reports that consecutive optima failed to nest for 8–36% of random
joint distributions with four to six states. That was not re-run here.

## What it does not say

- **Nothing about stochastic encoders.** The unrestricted information
  bottleneck at finite β generally has stochastic optima
  ([THEORY-743](../theory.d/THEORY-743.md)). The reading's heuristic search found no degrading
  channel between the stochastic optima of this example at β = 8, 10 and
  12, but it certified neither global optimality nor uniqueness. Whether
  stochastic optima nest stays open on [QUESTION-220](../questions.d/QUESTION-220.md).
- **Nothing about rate–distortion with block coding.** Equitz and Cover's
  successive refinability is asymptotic. Their own Gaussian example shows
  single-shot quantizers failing to nest for a source that is refinable
  ([NOTE-988](../notes.d/NOTE-988.md)).
- **Not that hierarchies of categories cannot nest.** Annealed category
  systems ([THEORY-163](../theory.d/THEORY-163.md)) may well nest. This shows only that optimality at
  each budget does not guarantee it.
