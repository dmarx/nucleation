---
status: Proposed
promote_when: >-
  A second reading of the published text, or the owner, confirms that
  §§3, 5, 5.1 and 7 state what the title says: the Yule–Simon lineage of
  preferential attachment and the Gibrat lineage of the lognormal; that a
  lognormal of large variance may look linear on a log-log plot over
  several orders of magnitude; that a lower reflecting barrier turns the
  multiplicative process's lognormal into a power law; and that an
  exponentially distributed observation time does the same, with tails
  x^(−1∓√(2λ)) in the zero-drift case. Not met by a proof of Kesten's
  theorem, which the title does not assert.
title: "Mitzenmacher traces preferential attachment from Yule and Simon to the Web-graph models and Gibrat's multiplicative process to the lognormal, and shows that a lognormal can look straight on a log-log plot and that a lower reflecting barrier or an exponentially distributed observation time turns the multiplicative process's lognormal into a power law"
version: 1
tags:
- probabilistic-modeling
- network-science
- complex-systems
date: '2026-11-21'
source:
- LIT-tmpwdtfj
corroborates:
- CLAIM-tmpepx9m
- CLAIM-tmpiervv
- CLAIM-tmply70l
- CLAIM-tmp1dlyp
bears_on:
- QUESTION-tmp21jtb
summary: >-
  Mitzenmacher (2004), [LIT-tmpwdtfj](../literature.d/LIT-tmpwdtfj.md), read in [NOTE-tmp0rhkc](../notes.d/NOTE-tmp0rhkc.md). A survey: its
  results are other people's, given intuitively. What the record uses is
  the map of small changes (a floor, a random observation time) that turn
  multiplicative growth's lognormal into a power law, and the warning that
  one law has several mechanisms. Its floor is a reflecting minimum, not
  Kesten's additive term, and it treats only linear attachment kernels.
  Proposed until the reading is confirmed.
---

# THEORY-tmp23821: Mitzenmacher traces preferential attachment from Yule and Simon to the Web-graph models and Gibrat's multiplicative process to the lognormal, and shows that a lognormal can look straight on a log-log plot and that a lower reflecting barrier or an exponentially distributed observation time turns the multiplicative process's lognormal into a power law

## Source

Mitzenmacher (2004), Internet Mathematics 1(2): 226–251, [LIT-tmpwdtfj](../literature.d/LIT-tmpwdtfj.md), read
in full in [NOTE-tmp0rhkc](../notes.d/NOTE-tmp0rhkc.md).

## The account

"Very similar basic generative models can lead to either power law or
lognormal distributions, depending on seemingly trivial variations" (§1).
Preferential attachment, from Yule (1925) and Simon (1955) to the Web
models, gives c_j ∼ c·j^(−(2−α)/(1−α)) when a new page links uniformly with
probability α and by indegree otherwise (§3). Multiplicative growth with
independent, identically distributed log-factors of finite variance gives a
lognormal (§5). Put a minimum under it that "acts as a lower reflective
barrier" and it "will yield a power law instead" (§5.1, by Champernowne's
example, Pr[X ≥ x] = m/x). Observe it at an exponentially distributed time
instead of a fixed one and the result is Reed's double Pareto, with density
∝ x^(−1−√(2λ)) above 1 and x^(−1+√(2λ)) below in the zero-drift case (§7).
And since a lognormal "may appear linear on a log-log plot for several
orders of magnitude" (§2), "it is not clear that a definitive answer is
possible" between the two (§8).

What could have come out otherwise: little, since the paper derives known
results again. The filer's checks did: Champernowne's chain, simulated with
its floor, gives Pr[class ≥ k] = 0.500, 0.251 and 0.063 at k = 2, 3 and 5
against 2^(−(k−1)); and the stopped-lognormal integral at λ = ½ gives
0.00500 and 0.0000500 at x = 10 and 100, against √(λ/2)·x^(−1−√(2λ))
(python3 -I).

## What this does not say

- Not Kesten's theorem. The floor is a reflecting minimum; the exponent
  equation E[A^κ] = 1 and the conditions are not in the paper, which
  defers to Kesten (1973) and Gabaix (1999). Champernowne's example
  satisfies the equation at κ = 1, but the paper does not say so.
- Not anything about nonlinear attachment kernels. Its α is a mixing
  probability.
- Not that preferential attachment is an age effect. §3 and §7 are kept
  apart.
- Not a method for telling the two laws apart from data.
