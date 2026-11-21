---
status: Proposed
title: 'Sloppiness and singular strata meet in two places and part in one: a sloppy eigenvalue near a stratum measures the squared distance to it, and at a finite sample size a direction too sloppy to resolve contributes to the learning coefficient no more than a flat one; they part in how the coefficient moves with sample size, rising about ½ for each direction resolved in a regular sloppy model toward d/2, and held below d/2 at every size in a singular one'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  A regular model whose free-energy slope −d log Z/d log n, at sample
  sizes below the inverse of its smallest Fisher eigenvalue times the prior
  variance, does not fall short of d/2 by about ½ for each unresolved
  direction; or a singular model whose slope, at sample sizes well past
  its resolution of every direction, keeps rising at the rate a regular
  sloppy model of the same dimension shows (about ½ per resolved
  direction) rather than approaching its learning coefficient from below
  at the rate (m − 1)/(log n)². A model in which the two are hard to tell
  apart at one sample size does not defeat it; that is part of what it
  says.
tags:
- information-geometry
- learning-theory
- model-comparison
date: '2026-11-21'
line:
- formal-apparatus
- learned-structure
rests_on:
- CLAIM-tmpcgvcp
grounds:
- THEORY-1253
- THEORY-087
- CASE-tmpb2gly
- CASE-152
bears_on:
- QUESTION-tmp82zpm
complements:
- CLAIM-tmpj0k4q
summary: >-
  The careful statement that the owner's U24 ("i bet wattanabe's
  stratification account connects nicely to that hyperribbon account from
  earlier") needs, in the exchange "Rich Get Richer Power Laws"
  (2026-11-21): where a hyperribbon and Watanabe's strata meet and where
  they do not. It fills the ledger's gap that A39's bridge rested on a
  hyperribbon reading the record does not hold, by stating the bridge in
  quantities the record does hold (THEORY-1253's learning capacity,
  THEORY-087's learning coefficient), each checked numerically. The
  wording is the assistant's (Claude, in this session); adopting it is
  the owner's call.
---

<!-- inactive-ok-file: CLAIM-tmpcgvcp CASE-tmpb2gly CLAIM-tmpj0k4q LIT-tmpnbl2d LIT-tmp3njir — Proposed, new or Deferred; filed with this claim, or works registered from the exchange and not yet read -->

# CLAIM-tmpcg4uu: Sloppiness and singular strata meet in two places and part in one: a sloppy eigenvalue near a stratum measures the squared distance to it, and at a finite sample size a direction too sloppy to resolve contributes to the learning coefficient no more than a flat one; they part in how the coefficient moves with sample size, rising about ½ for each direction resolved in a regular sloppy model toward d/2, and held below d/2 at every size in a singular one

## The claim

CLAIM-tmpcgvcp holds that sloppiness and singularity are different
properties. This claim says where they nevertheless meet, and how to
tell them apart where they look alike. It answers U24, the owner's bet
that the two accounts connect, and gives it a precise form.

**Where they meet (1): at the edges.** Near a stratum where two mechanisms
merge, the small Fisher eigenvalue is proportional to the squared
distance from the stratum: 4v²/(1 + u²) in F(a, b) = (a + b, ab), and about
5.6 v² in a sum of two exponentials with rates u ± v (CASE-tmpb2gly).
The sum of exponentials is the textbook sloppy model, and equal rates
are a fold edge of its image. So at least some of a hyperribbon's thin
directions end at singular strata, and near them the hyperribbon's
eigenvalue reads off the distance to the stratum. This is the part of
the owner's bet that holds as stated.

**Where they meet (2): at a finite sample size.** Treat the slope
λ(n) = −d log Z_n/d log n as a learning coefficient at scale n. This is the
learning capacity of THEORY-1253, and what a local learning-coefficient
estimate at an inverse temperature of order n measures (Lau et al.,
LIT-tmpnbl2d, unread). In a regular model with Fisher eigenvalues e_i
and a Gaussian prior of variance s², each direction contributes exactly

  n e_i s² / (1 + 2 n e_i s²),

which is about 0 while n e_i s² ≪ 1 and ½ once n e_i s² ≫ 1. A sloppy
direction that the data cannot yet resolve contributes to λ(n) what a flat
direction contributes: nothing. So, at one n, a sloppy regular model and
a singular model both show λ(n) < d/2. LaMont and Wiggins already call a
model "predictively sloppy" when its capacity falls below ½ dim Θ, and
give freeze-out as the mechanism (THEORY-1253; NOTE-1481, their C3).
CLAIM-tmpj0k4q, filed from the same exchange, counts the directions a
data set resolves, logarithmic in n for a geometric spectrum. This claim
reads that count in the learning coefficient and adds the contrast with
the singular case and the test that separates them.

**Where they part: in how λ(n) moves with n.** The assistant's checks:

| n | 10⁰ | 10² | 10⁴ | 10⁶ | 10⁸ | 10¹⁰ |
|---|---|---|---|---|---|---|
| sloppy regular, d = 8, e_i = 10⁰ … 10⁻⁷, s = 1 | 0.43 | 1.40 | 2.40 | 3.39 | 3.97 | 4.00 |

| n | 10² | 10³ | 10⁴ | 10⁵ | 10⁶ |
|---|---|---|---|---|---|
| singular, u² + v⁴ on [−1, 1]² (λ = 3/4, m = 1) | 0.754 | 0.751 | 0.750 | 0.750 | 0.750 |
| singular, a²b² on [−1, 1]² (λ = ½, m = 2) | 0.348 | 0.387 | 0.411 | 0.426 | 0.437 |

- In the sloppy regular model λ(n) climbs by about ½ for each direction
  resolved: by ½ per decade here, since the eigenvalues are a decade
  apart, about 0.22 per unit of log n. It reaches d/2 = 4 once n exceeds
  the inverse of the smallest eigenvalue.
- In a singular model λ(n) stays below its learning coefficient, below
  d/2, at every n. With multiplicity m > 1 it creeps up as
  λ − (m − 1)/log n (THEORY-1253), at a rate of (m − 1)/(log n)²: about
  0.006 to 0.008 per unit of log n between 10⁴ and 10⁶ for a²b², 30 to 40
  times slower than the sloppy climb.

So a single learning-coefficient estimate cannot tell a hyperribbon from
a singularity. Its dependence on sample size, or on the inverse
temperature of the estimator, can. A sloppy model's coefficient keeps
rising toward d/2 at about ½ per resolved direction. A singular one
levels off below it.

## What it does not say

- It does not say the hyperribbon's widths, which are geodesic widths of
  the model image, equal the inverse square roots of local Fisher
  eigenvalues. The record holds neither the widths nor that relation
  (CLAIM-tmpcgvcp). The claim is stated in eigenvalues, which the record
  holds.
- It does not say every sloppy direction ends at a stratum. A linear
  model is sloppy and never singular (CLAIM-tmpcgvcp).
- It does not apply as stated to deep networks, where n, d and the
  spectrum grow together (QUESTION-tmp7d1ws). Hoogland et al.
  (LIT-tmp3njir, unread) report learning-coefficient estimates changing
  across stages. On this claim, a rise in an estimate over training could
  be a sloppy direction coming into resolution as much as a change of
  singular stratum. The estimate's dependence on its inverse temperature
  is what would separate the two.
- The checks use a Gaussian prior for the regular model, where the slope
  has the closed form above, and numerical quadrature for the singular
  ones (`t5/check1.py`). Data fluctuations are not included.
