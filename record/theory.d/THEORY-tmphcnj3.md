---
status: Proposed
promote_when: >-
  A rerun of the paper's published pipeline on the Index of Complex
  Networks corpus, or an independent reimplementation of the same fitting,
  goodness-of-fit and likelihood-ratio procedure and category thresholds,
  reproduces the proportions in the title (29% of data sets Weakest, 4%
  Strongest, a lognormal at least as good as the power law for 88%) within
  a few percentage points, and the paper's Discussion is confirmed to draw
  the two conclusions the title gives. Not met, and not defeated, by a
  reanalysis under a different definition of a power law, which the title
  does not assert.
title: "Broido and Clauset, fitting a discrete power law to the upper tail of the degree sequences of 928 network data sets and comparing it by likelihood ratio with exponential, lognormal, Weibull and cutoff alternatives, find a power law plausible for 29% of data sets and strongly supported for 4%, and a lognormal at least as good for 88% of degree distributions, and conclude that a mechanism which necessarily yields power-law degrees has a limited role and that the degree distribution weakly discriminates between mechanisms"
version: 1
tags:
- network-science
- mathematical-statistics
date: '2026-11-22'
source:
- LIT-2963
bears_on:
- QUESTION-505
summary: >-
  Broido & Clauset (2019), [LIT-2963](../literature.d/LIT-2963.md), read in [NOTE-tmpleyjh](../notes.d/NOTE-tmpleyjh.md). The record's
  network-scale evidence that a power-law shape is weak evidence of
  mechanism, and a ground of [CLAIM-803](../claims.d/CLAIM-803.md). Its test is of a pure power law
  above k_min; the verdict is disputed by Voitalov and others
  ([LIT-tmpvmrkv](../literature.d/LIT-tmpvmrkv.md), unread), who define a power law as a regularly varying
  tail, [TERM-142](../terms.d/TERM-142.md)'s sense 1. Proposed until the reading is confirmed.
---
<!-- inactive-ok-file: CLAIM-803 TERM-142 — Proposed; the claim this reading grounds and the term whose sense the dispute turns on -->
<!-- inactive-ok-file: LIT-tmpvmrkv — Deferred; the reply, registered and unread -->

# THEORY-tmphcnj3: Broido and Clauset, fitting a discrete power law to the upper tail of the degree sequences of 928 network data sets and comparing it by likelihood ratio with exponential, lognormal, Weibull and cutoff alternatives, find a power law plausible for 29% of data sets and strongly supported for 4%, and a lognormal at least as good for 88% of degree distributions, and conclude that a mechanism which necessarily yields power-law degrees has a limited role and that the degree distribution weakly discriminates between mechanisms

## Source

Broido & Clauset (2019), "Scale-free networks are rare", Nature
Communications 10, 1017, [LIT-2963](../literature.d/LIT-2963.md), read in the published version through
Europe PMC in [NOTE-tmpleyjh](../notes.d/NOTE-tmpleyjh.md).

## The account

Using the procedure of [LIT-2987](../literature.d/LIT-2987.md) on 3662 simple graphs from 928 data sets,
"fully 49% of networks fall into the Not Scale Free category"; Weakest
and Weak "account for only 29 and 19% of networks", and "only 10 and 4%
... belonging to the Strong or Strongest categories". "the log-normal is
at least as good a fit as the power law for the vast majority of degree
distributions (88%)". Social networks are "at best only weakly scale
free"; a few technological and biological networks are strongly so. From
this, "a generally limited role for any mechanism that necessarily
produces power-law degree distributions", and the degree distribution is
"a weak discriminator between mechanisms" (Discussion).

What could have come out otherwise: the proportions. The synthetic
preferential-attachment controls "should and do fall into the Strongest
category", so the test can find scale-free networks when they are there.

## The verdict is disputed

Voitalov, van der Hoorn, van der Hofstad and Krioukov ([LIT-tmpvmrkv](../literature.d/LIT-tmpvmrkv.md),
registered, unread) define a power law as a regularly varying
distribution, which "allows the distribution to deviate from a pure power
law arbitrarily but without affecting the power-law tail exponent", and
conclude by their abstract that real scale-free networks "are definitely
not as rare" as the pure-power-law assumption makes them. The hinge is the
definition: an exact power law above k_min here, a regularly varying tail
([TERM-142](../terms.d/TERM-142.md) sense 1) there. The proportions in the title are this paper's
under its own definition, and stand or fall as a measurement under it.

## What this does not say

- Not that the networks are not heavy tailed, or that they are lognormal:
  "may in fact be log-normal networks".
- Not anything about criticality.
- Not a dynamical test of mechanism; it asks for one "that goes beyond
  static degree distributions" and names none.
