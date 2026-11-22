---
number: 2173
status: Proposed
formerly:
- THEORY-tmpw4qgu
promote_when: >-
  A second reading, or a check against the SIAM Review text (51(4),
  661–703), confirms what the title says: the procedure as stated (the
  maximum-likelihood exponent above an x_min chosen by minimum
  Kolmogorov–Smirnov distance, a bootstrap goodness-of-fit p-value with
  rejection at p ≤ 0.1, and Vuong likelihood-ratio tests against
  alternatives); the tallies of Tables 6.1–6.3 (7 of 24 rejected, only
  word frequencies rated good, the lognormal excluded only for HTTP
  sizes); and the sentence of §6 deferring inconclusive cases to "a
  mechanistic or other nonstatistical argument".
title: "Clauset, Shalizi and Newman hold that a straight line on a log-log plot is necessary but not sufficient for a power law, replace least-squares fits with a maximum-likelihood exponent above a lower bound chosen by minimum Kolmogorov-Smirnov distance, a bootstrap goodness-of-fit test and likelihood-ratio tests against alternatives, and, applying them to 24 data sets, reject 7, find only word frequencies convincing and exclude the lognormal for only one, so that where the tests cannot decide the choice must rest on mechanism"
version: 1
tags:
- mathematical-statistics
- complex-systems
date: '2026-11-22'
source:
- LIT-2987
bears_on:
- QUESTION-506
summary: >-
  Clauset, Shalizi & Newman (2009), [LIT-2987](../literature.d/LIT-2987.md), read in [NOTE-2262](../notes.d/NOTE-2262.md). The
  record's standard for fitting a tail, and the ground of [CLAIM-803](../claims.d/CLAIM-803.md)'s
  "fit first" clause. Its empirical lesson is that a power law and a
  lognormal are seldom distinguishable at realistic sample sizes (US city
  sizes among the undecided), and it defers the choice to mechanism
  without supplying dynamical tests. Proposed until the reading is
  confirmed.
---
<!-- inactive-ok-file: CLAIM-803 — Proposed; the claim this reading grounds -->

# THEORY-2173: Clauset, Shalizi and Newman hold that a straight line on a log-log plot is necessary but not sufficient for a power law, replace least-squares fits with a maximum-likelihood exponent above a lower bound chosen by minimum Kolmogorov-Smirnov distance, a bootstrap goodness-of-fit test and likelihood-ratio tests against alternatives, and, applying them to 24 data sets, reject 7, find only word frequencies convincing and exclude the lognormal for only one, so that where the tests cannot decide the choice must rest on mechanism

## Source

Clauset, Shalizi & Newman (2009), "Power-law distributions in empirical
data", SIAM Review 51(4), 661–703, [LIT-2987](../literature.d/LIT-2987.md), read from the arXiv v2 in
[NOTE-2262](../notes.d/NOTE-2262.md).

## The account

"being roughly straight on a log-log plot is a necessary but not
sufficient condition for power-law behavior" (§4, p. 15). The procedure
(Box 1, p. 3): estimate α by maximum likelihood above the x_min that
minimizes the Kolmogorov–Smirnov distance (§3.3); compute a bootstrap
p-value and reject at p ≤ 0.1 (§4.1); compare with the lognormal,
exponential, stretched exponential, cutoff and Poisson forms by Vuong's
likelihood ratio, which can also say the data cannot decide (§5). On 24
data sets "17 of the 24 data sets are consistent with a power-law
distribution" (p. 23); only word frequencies is "truly convincing"; the
lognormal "is not ruled out for any of our data sets except the HTTP
connections" (p. 26). Where the tests are inconclusive, "we must consider
whether there is a mechanistic or other nonstatistical argument favoring
one distribution or another" (p. 26).

What could have come out otherwise: the tallies. More data sets could have
excluded the lognormal; they did not.

## What this does not say

- Not that a power law fails to identify its mechanism, in those words,
  and not any dynamical test of mechanism: gain proportional to size,
  floors and resets, a cutoff that moves with system size are absent.
- Not that shape is uninformative: the form "may matter greatly" for
  inferring mechanisms (§7, p. 30).
- Nothing about the body below x_min.
