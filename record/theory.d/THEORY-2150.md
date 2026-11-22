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
<!-- inactive-ok-file: THEORY-tmp6jdas THEORY-tmphcnj3 — Proposed; the readings of 2026-11-22 cited in the notes -->
<!-- inactive-ok-file: TERM-tmpg1vx2 — Proposed; the term on the name Gibrat -->

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

**Parallels.** Newman ([LIT-2976](../literature.d/LIT-2976.md), [NOTE-tmpa7yd2](../notes.d/NOTE-tmpa7yd2.md), [THEORY-tmp6jdas](THEORY-tmp6jdas.md)) cites
this survey as a companion review (his ref. 19). Both have Miller, Yule
and Simon, and the lognormal against the power law; Newman adds
percolation, self-organized criticality, highly optimized tolerance,
coherent noise, inverses and record dynamics; this survey adds
Mandelbrot's optimization and Reed's double Pareto. Newman reports that
Simon called the rich-get-richer rule "the Gibrat principle" (p. 18),
where this survey keeps Gibrat for the multiplicative lineage of the
lognormal ([TERM-tmpg1vx2](../terms.d/TERM-tmpg1vx2.md)). Broido and Clauset ([LIT-2963](../literature.d/LIT-2963.md), [NOTE-tmpleyjh](../notes.d/NOTE-tmpleyjh.md),
[THEORY-tmphcnj3](THEORY-tmphcnj3.md)) give the corpus-scale empirical side of the
lognormal-against-power-law confusion: a lognormal fits at least as well
as the power law for 88% of degree distributions. No edge.
