---
number: 2150
status: Proposed
formerly:
- THEORY-tmp23821
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
- LIT-3003
corroborates:
- CLAIM-817
- CLAIM-824
- CLAIM-830
- CLAIM-795
bears_on:
- QUESTION-505
summary: >-
  Mitzenmacher (2004), [LIT-3003](../literature.d/LIT-3003.md), read in [NOTE-2237](../notes.d/NOTE-2237.md). A survey: its
  results are other people's, given intuitively. What the record uses is
  the map of small changes (a floor, a random observation time) that turn
  multiplicative growth's lognormal into a power law, and the warning that
  one law has several mechanisms. Its floor is a reflecting minimum, not
  Kesten's additive term, and it treats only linear attachment kernels.
  Proposed until the reading is confirmed.
---
<!-- inactive-ok-file: THEORY-2169 THEORY-2172 — Proposed; the readings of 2026-11-22 cited in the notes -->
<!-- inactive-ok-file: TERM-144 — Proposed; the term on the name Gibrat -->
<!-- inactive-ok-file: THEORY-2177 THEORY-2175 — Proposed; the readings of 2026-11-22 -->

# THEORY-2150: Mitzenmacher traces preferential attachment from Yule and Simon to the Web-graph models and Gibrat's multiplicative process to the lognormal, and shows that a lognormal can look straight on a log-log plot and that a lower reflecting barrier or an exponentially distributed observation time turns the multiplicative process's lognormal into a power law

## Source

Mitzenmacher (2004), Internet Mathematics 1(2): 226–251, [LIT-3003](../literature.d/LIT-3003.md), read
in full in [NOTE-2237](../notes.d/NOTE-2237.md).

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

## Note of 2026-11-22: Newman; Broido and Clauset, read

**Parallels.** Newman ([LIT-2976](../literature.d/LIT-2976.md), [NOTE-2261](../notes.d/NOTE-2261.md), [THEORY-2169](THEORY-2169.md)) cites
this survey as a companion review (his ref. 19). Both have Miller, Yule
and Simon, and the lognormal against the power law; Newman adds
percolation, self-organized criticality, highly optimized tolerance,
coherent noise, inverses and record dynamics; this survey adds
Mandelbrot's optimization and Reed's double Pareto. Newman reports that
Simon called the rich-get-richer rule "the Gibrat principle" (p. 18),
where this survey keeps Gibrat for the multiplicative lineage of the
lognormal ([TERM-144](../terms.d/TERM-144.md)). Broido and Clauset ([LIT-2963](../literature.d/LIT-2963.md), [NOTE-2263](../notes.d/NOTE-2263.md),
[THEORY-2172](THEORY-2172.md)) give the corpus-scale empirical side of the
lognormal-against-power-law confusion: a lognormal fits at least as well
as the power law for 88% of degree distributions. No edge.

## Note of 2026-11-22: Reed and Hughes; Corominas-Murtra, Hanel and Thurner, read

- **Reed and Hughes** ([LIT-3007](../literature.d/LIT-3007.md), read in [NOTE-2264](../notes.d/NOTE-2264.md); [THEORY-2177](THEORY-2177.md)),
  the source §7 reports, **corroborate** the account's double Pareto: their
  eq. 9 at zero log drift (μ = ½σ²) gives exponents ±√(2ν)/σ, §7's √(2λ) with
  unit variance. Reed and Hughes cite Mitzenmacher for the lognormal file
  size model. This account's `promote_when` asks for a second reading of
  Mitzenmacher's own text, so it is not met.
- **Corominas-Murtra, Hanel and Thurner** ([LIT-2997](../literature.d/LIT-2997.md), read in
  [NOTE-2266](../notes.d/NOTE-2266.md); [THEORY-2175](THEORY-2175.md)): a **parallel**, with no edge. Their
  noisy sample-space reduction has frequency survival exponent 1/λ, λ the
  share of nested steps; §3's attachment with a uniform share α has
  survival exponent 1/(1 − α). In both a mix of a structured and a uniform
  choice sets the exponent, by the same formula ([QUESTION-505](../questions.d/QUESTION-505.md)'s note of
  this date). They cite this work for "other mechanisms".
