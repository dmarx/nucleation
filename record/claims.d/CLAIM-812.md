---
number: 812
status: Proposed
formerly:
- CLAIM-tmpcg4uu
title: 'Sloppiness and singular strata meet in two places and part in one: a sloppy eigenvalue near a stratum measures the squared distance to it, and at a finite sample size a direction too sloppy to resolve contributes to the learning coefficient no more than a flat one; they part in how the coefficient moves with sample size, rising about ½ for each direction resolved in a regular sloppy model toward d/2, and held below d/2 at every size in a singular one'
version: 3
history:
- version: 2
  date: '2026-11-21'
  note: >-
    Two corrections in place, the claim having been filed in this pull
    request, after the readings of LIT-3009 (NOTE-2247) and
    LIT-2995 (NOTE-2239). The hyperribbon's widths are ≈ √λ (the
    Jacobian's singular values), not "the inverse square roots of local
    Fisher eigenvalues". A local learning-coefficient estimate is made at
    inverse temperature β* = 1/log n, an effective sample size n/log n, not
    at "an inverse temperature of order n", and its localizer's precision γ
    is a second cut-off. The title and the thesis are unchanged. See the
    Note of 2026-11-21.
- version: 3
  date: '2026-11-21'
  note: >-
    After the reading of Hoogland et al. (LIT-2966, NOTE-tmp2pgi8): the
    sentence calling the work unread updated, and a dated note added
    applying the claim's formula to the paper's estimator settings. Title
    and thesis unchanged.
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
- CLAIM-813
grounds:
- THEORY-1253
- THEORY-087
- CASE-302
- CASE-152
bears_on:
- QUESTION-511
complements:
- CLAIM-825
summary: >-
  The careful statement that the owner's U24 ("i bet wattanabe's
  stratification account connects nicely to that hyperribbon account from
  earlier") needs, in the exchange "Rich Get Richer Power Laws"
  (2026-11-21): where a hyperribbon and Watanabe's strata meet and where
  they do not. It fills the ledger's gap that A39's bridge rested on a
  hyperribbon reading the record does not hold, by stating the bridge in
  quantities the record does hold ([THEORY-1253](../theory.d/THEORY-1253.md)'s learning capacity,
  [THEORY-087](../theory.d/THEORY-087.md)'s learning coefficient), each checked numerically. The
  wording is the assistant's (Claude, in this session); adopting it is
  the owner's call.
---
<!-- inactive-ok-file: THEORY-tmpm3ux2 — Proposed; the reading of Lee et al. filed 2026-11-22 -->

<!-- inactive-ok-file: THEORY-tmpt1tw7 — new; the reading of 2026-11-21 -->
<!-- inactive-ok-file: CLAIM-813 CASE-302 CLAIM-825 THEORY-tmpr9w2r — Proposed, new or Deferred; filed with this claim, or works registered from the exchange and not yet read -->
<!-- inactive-ok-file: ARG-134 THEORY-2155 THEORY-2157 — Proposed or Rejected entries filed on 2026-11-21 from the exchange "Rich Get Richer Power Laws" and from the readings of its works, or Deferred works not yet read -->

<!-- inactive-ok-file: THEORY-tmpx26x7 — Proposed or new; the reading of the 2023 review by Quinn and colleagues, 2026-11-22 -->

# CLAIM-812: Sloppiness and singular strata meet in two places and part in one: a sloppy eigenvalue near a stratum measures the squared distance to it, and at a finite sample size a direction too sloppy to resolve contributes to the learning coefficient no more than a flat one; they part in how the coefficient moves with sample size, rising about ½ for each direction resolved in a regular sloppy model toward d/2, and held below d/2 at every size in a singular one

## The claim

[CLAIM-813](CLAIM-813.md) holds that sloppiness and singularity are different
properties. This claim says where they nevertheless meet, and how to
tell them apart where they look alike. It answers U24, the owner's bet
that the two accounts connect, and gives it a precise form.

**Where they meet (1): at the edges.** Near a stratum where two mechanisms
merge, the small Fisher eigenvalue is proportional to the squared
distance from the stratum: 4v²/(1 + u²) in F(a, b) = (a + b, ab), and about
5.6 v² in a sum of two exponentials with rates u ± v ([CASE-302](../cases.d/CASE-302.md)).
The sum of exponentials is the textbook sloppy model, and equal rates
are a fold edge of its image. So at least some of a hyperribbon's thin
directions end at singular strata, and near them the hyperribbon's
eigenvalue reads off the distance to the stratum. This is the part of
the owner's bet that holds as stated.

**Where they meet (2): at a finite sample size.** Treat the slope
λ(n) = −d log Z_n/d log n as a learning coefficient at scale n. This is the
learning capacity of [THEORY-1253](../theory.d/THEORY-1253.md). A local learning-coefficient estimate
(Lau et al., [LIT-2995](../literature.d/LIT-2995.md), [THEORY-2157](../theory.d/THEORY-2157.md)) measures the same kind of
slope of a localized free energy, at effective sample size n/log n
(inverse temperature β* = 1/log n), with its localizing prior of
precision γ in the role of the prior (corrected 2026-11-21; see the note
below). In a regular model with Fisher eigenvalues e_i
and a Gaussian prior of variance s², each direction contributes exactly

  n e_i s² / (1 + 2 n e_i s²),

which is about 0 while n e_i s² ≪ 1 and ½ once n e_i s² ≫ 1. A sloppy
direction that the data cannot yet resolve contributes to λ(n) what a flat
direction contributes: nothing. So, at one n, a sloppy regular model and
a singular model both show λ(n) < d/2. LaMont and Wiggins already call a
model "predictively sloppy" when its capacity falls below ½ dim Θ, and
give freeze-out as the mechanism ([THEORY-1253](../theory.d/THEORY-1253.md); [NOTE-1481](../notes.d/NOTE-1481.md), their C3).
[CLAIM-825](CLAIM-825.md), filed from the same exchange, counts the directions a
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
  λ − (m − 1)/log n ([THEORY-1253](../theory.d/THEORY-1253.md)), at a rate of (m − 1)/(log n)²: about
  0.006 to 0.008 per unit of log n between 10⁴ and 10⁶ for a²b², 30 to 40
  times slower than the sloppy climb.

So a single learning-coefficient estimate cannot tell a hyperribbon from
a singularity. Its dependence on sample size, or on the inverse
temperature of the estimator, can. A sloppy model's coefficient keeps
rising toward d/2 at about ½ per resolved direction. A singular one
levels off below it.

## What it does not say

- It does not say the hyperribbon's widths, which are geodesic widths of
  the model image, equal the square roots of local Fisher eigenvalues
  (corrected 2026-11-21 from "inverse square roots"). Transtrum, Machta
  and Sethna find widths ≈ √λ, the Jacobian's singular values, in natural
  or log units, from a central point, and not in magnitude for every model
  ([THEORY-2155](../theory.d/THEORY-2155.md)); 1/√λ is the width in parameter space of the ellipse
  of good fits. The claim is stated in eigenvalues, which the record holds.
- It does not say every sloppy direction ends at a stratum. A linear
  model is sloppy and never singular ([CLAIM-813](CLAIM-813.md)).
- It does not apply as stated to deep networks, where n, d and the
  spectrum grow together ([QUESTION-510](../questions.d/QUESTION-510.md)). Hoogland et al.
  ([LIT-2966](../literature.d/LIT-2966.md), read 2026-11-21: [THEORY-tmpr9w2r](../theory.d/THEORY-tmpr9w2r.md)) report
  learning-coefficient estimates changing across stages. On this claim, a rise in an estimate over training could
  be a sloppy direction coming into resolution as much as a change of
  singular stratum. The estimate's dependence on its inverse temperature
  is what would separate the two.
- The checks use a Gaussian prior for the regular model, where the slope
  has the closed form above, and numerical quadrature for the singular
  ones (`t5/check1.py`). Data fluctuations are not included.

## Note of 2026-11-21: Transtrum, Machta & Sethna and Lau et al., read

**Corrections.** (1) "The inverse square roots of local Fisher
eigenvalues" inverted the papers' relation: the 2011 paper finds the
geodesic widths tracking the singular values of J, √λ, in natural or log
units from a central point, exactly for polynomial fitting on a ball,
within √(2/M) for exponentials in a continuum limit, and failing in
magnitude for PC12 ([NOTE-2247](../notes.d/NOTE-2247.md)); the 2010 letter takes "the square root
to match units" ([NOTE-2240](../notes.d/NOTE-2240.md)). Corrected in place. (2) In Lau et al. "the inverse temperature is deliberately set to
β∗ = 1/ log n" ([NOTE-2239](../notes.d/NOTE-2239.md)), so the estimate is nβ*·(excess loss), a slope at effective
sample size t = n/log n, not at "an inverse temperature of order n". On a
quadratic loss ½Σe_i x_i² the estimate is Σ ½·te_i/(te_i + γ): a direction
contributes ½ when e_i ≫ γ log n/n and nothing when e_i ≪ γ log n/n. The
filer checked this by Monte Carlo (nine directions spanning eight
decades, n = 10⁵, γ = 1: 2.212 against 2.219 from the formula, d/2 = 4.5;
at γ = 100 the formula gives 1.22). So the localizer's precision γ is a
second cut-off beside the sample size, which this claim and its test had
not named: a direction counts as flat if the data or the localizer leave
it unresolved. The test the claim proposes, the estimate's dependence on
its inverse temperature, should also vary γ ([LEAD-207](../leads.d/LEAD-207.md)).

**Support.** The fold-edge half is corroborated by the 2011 paper: the
equal-rate "fold line" of the sum of exponentials is a boundary where "No
parameters were at extreme values, but the model behavior was nonetheless
singular" ([THEORY-2155](../theory.d/THEORY-2155.md); the 2010 letter lists θ₁ = θ₂ among the
boundaries). The finite-n half is not tested by Lau et al.: their
calibration mostly underestimates, which would fit, but they attribute
underestimation to an unsettled sampler ([ARG-134](../arguments.d/ARG-134.md), Rejected as
evidence). The estimator's form supports the claim's reading by
derivation, the filer's, not by the paper's data.

## Note of 2026-11-21: Hoogland, Wang, Farrugia-Roberts, Carroll, Wei & Murfet, read

Leaves the claim open, and sharpens the alternative it names
([NOTE-tmp2pgi8](../notes.d/NOTE-tmp2pgi8.md), [THEORY-tmpr9w2r](../theory.d/THEORY-tmpr9w2r.md)). The paper estimates at fixed settings
per setting, departing from Lau et al.'s β*: "Instead of nβ = n/ log n, we
perform LLC estimation at nβ = m/ log m, where m is the SGLD batch size"
(A.5.1). The language model uses nβ = 21.7 and γ = 100; the regression
model nβ = 66.7 and γ = 13.3 (Tables 1–2). By this claim's formula,
Σ ½·te_i/(te_i + γ) with t = nβ, a direction counts fully only when
e_i ≫ γ/(nβ): about 100/21.7 ≈ 4.6 in the language model and
13.3/66.7 ≈ 0.20 in the regression model. The estimates (about 80 to 150,
and up to about 165) are far below d/2 (about 1.68 million and 25.9
thousand), as most directions unresolved at those settings would make
them. So a rise in λ̂ over a stage could be directions stiffening past
the cut-off as much as a change of stratum; the paper varies neither nβ
nor γ across stages, so the stiffening alternative is not ruled out. Its
Hessian comparison (B.5: the trace and top eigenvalue miss three of four
boundaries) tells weakly against a pure-curvature reading, but those
statistics are dominated by the largest eigenvalues, not by those near the
cut-off. The paper's estimates are not at β*. No relation written: the
paper does not test the claim.

## Note of 2026-11-21: Transtrum and Qiu, read

Supporting, for the fold-edge half ([NOTE-tmphbnqd](../notes.d/NOTE-tmphbnqd.md), [THEORY-tmpt1tw7](../theory.d/THEORY-tmpt1tw7.md)). The manifold boundary approximation follows a geodesic to a boundary of the model manifold where the smallest Fisher eigenvalue goes to zero, and the merging of two terms is among the boundaries it follows. In the sum of exponentials it is the only finite one, the edge where this claim's sloppy eigenvalue goes to zero with the squared distance to the stratum. The method says nothing about the finite-sample half. Filer A reported this bearing (readings batch 2). The note is the assistant's (Claude, in this session).

## Note of 2026-11-22: Quinn, Abbott, Transtrum, Machta & Sethna (2023), read

A parallel, in Bayesian-prior terms, to the finite-sample half
([NOTE-tmp3keyy](../notes.d/NOTE-tmp3keyy.md), [THEORY-tmpx26x7](../theory.d/THEORY-tmpx26x7.md)). For the mutual-information-maximizing
prior, "Along a short dimension (say ≲1 standard deviations) the atoms
will lie only at the boundaries" (§5.1), and as noise falls dimensions
"smoothly pass from" the unresolved category to the resolved one: a
direction too sloppy for the data is treated as a choice among edge
models, not as a resolved parameter. That is the claim's "counts like a
flat one at finite n" seen through the prior, not through the learning
coefficient, and the review does not mention singular learning theory.
No relation is written.

## Note of 2026-11-22: Lee, Smith, Adam and Hoogland, read

The cautions apply. Lee et al. (THEORY-tmpm3ux2) estimate their Bayesian
influence with the same localized SGLD at fixed nβ and γ: in the toy,
settings chosen to maximize agreement with leave-one-out (C.2); in the
language models, nβ ∈ {256, 1024} and γ ∈ {500, 1000}, which "did not
vary substantially" (D.1.2). A direction below this claim's curvature
cut-off at those settings would be invisible to their covariance too.
