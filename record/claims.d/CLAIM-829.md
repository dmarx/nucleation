---
number: 829
status: Proposed
formerly:
- CLAIM-tmplb1ow
title: 'Read as a separation of scales, a bulk separated from a sparse tail is what a continuous transition shows from below: the bulk keeps a fixed small scale while the cutoff of the tail grows without bound as the transition nears, and at the transition the separating scale is gone, so that no size marks off the extraordinary'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  A standard model of a continuous transition in which, as the
  transition is approached from below, the typical size grows as fast as
  the cutoff, so that their ratio stays bounded; or one in which, at the
  transition, the chance of a further tenfold increase given a size
  already reached still depends on that size across the scaling range; or
  the objection that this reading only restates what the record already
  holds as critical slowing down (THEORY-1315), which would need the size
  cutoff to carry no information beyond the relaxation time.
tags:
- complex-systems
- probabilistic-modeling
date: '2026-11-21'
line:
- formal-apparatus
grounds:
- CASE-303
- THEORY-1315
complements:
- CLAIM-832
summary: >-
  Reading (b) of the owner's conjecture [CLAIM-840](CLAIM-840.md) (U5 of the exchange
  "Rich Get Richer Power Laws"), filed as the alternative to reading (a),
  [CLAIM-845](CLAIM-845.md). "Separated" is taken as two scales, not a gap. In the
  Poisson cascade the median stays at 2 while the cutoff grows as
  2/(1 − R)^2, so the ratio of tail scale to bulk scale is about 93 at
  R = 0.9, 9,900 at 0.99 and a million at 0.999. At R = 1 the
  chance of a further tenfold increase is 0.316 from any size, where at
  R = 0.99 it falls from 0.30 to 0.001 as the size passes the cutoff. A
  reached the same reading at the end of A7 and in A8. The separation
  "closes" at the transition only in the sense that the separating scale
  disappears; as a ratio it diverges. The wording is the assistant's
  (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-840 CLAIM-845 CLAIM-832 CASE-303 CLAIM-769 THEORY-2131 — Proposed or new; the owner's conjecture, the other reading, the claims, case, argument and lead filed with it, and held entries cited as contrasts -->
<!-- inactive-ok-file: THEORY-tmpczldx — Proposed; the reading of Beck and Cohen, 2026-11-22 -->

# CLAIM-829: Read as a separation of scales, a bulk separated from a sparse tail is what a continuous transition shows from below: the bulk keeps a fixed small scale while the cutoff of the tail grows without bound as the transition nears, and at the transition the separating scale is gone, so that no size marks off the extraordinary

**This is reading (b) of [CLAIM-840](CLAIM-840.md), one of two alternatives.** The
other, reading (a), is [CLAIM-845](CLAIM-845.md). The owner chooses.

## The claim

Take "a bulk mass separated by a low mass long tail" to mean that the bulk
and the tail are set by different scales. The bulk's scale is the typical
size, which stays small. The tail's scale is the cutoff s_c, beyond which
sizes are exponentially suppressed.

**Below the transition the two scales pull apart.** In the Poisson
cascade ([CASE-303](../cases.d/CASE-303.md)), the law is C(R)·s^(−3/2)·e^(−s/s_c) with
s_c = 1/(R − 1 − ln R) ≈ 2/(1 − R)^2, while the bulk does not move:

| R | P(S = 1) | median | 90th percentile | s_c | s_c / median |
|---|---:|---:|---:|---:|---:|
| 0.9 | 0.407 | 2 | 21 | 187 | 93 |
| 0.99 | 0.372 | 2 | 54 | 19,867 | 9,933 |
| 0.999 | 0.368 | 2 | 62 | 1,998,667 | 999,333 |

So the owner's "bulk mass … low mass long tail" is exact in this reading:
the fraction of cascades beyond s_c is about 0.05·(1 − R), which is 5.8 ×
10⁻³, 5.1 × 10⁻⁴ and 5.0 × 10⁻⁵ at the three values. The tail is
low-mass and getting lower even as it lengthens.

**At the transition the separating scale is gone.** At R = 1 the cutoff
is infinite, and the chance of a further tenfold increase from a size
already reached, P(S > 10s | S > s), is the same from every size:
0.324, 0.317, 0.316, 0.316 and 0.316 for s = 10 to 100,000, the pure
tail's 10^(−1/2). Below the transition it depends on where one starts.
At R = 0.99 it is 0.297, 0.235, 0.101 and 0.001 for s = 10, 100, 1,000
and 10,000. At R = 0.999 it is 0.321, 0.308, 0.289, 0.234 and 0.099 for
s = 10 to 100,000. Below, a size near s_c marks off the extraordinary
event. At the transition no size does. This is A's closing line at A7,
"At the transition, the scale separating ordinary from extraordinary
behavior ceases to be fixed", and A8 §4, where the conditional
exceedance at criticality is A's own example (checked). The owner's U6 quoted that closing line
back and asked A to "elaborate"; the line it picked out bears on this
reading.

**What "closes" means.** As a ratio, the separation of scales does not
close at the transition. It diverges, as the table shows. What closes is
the boundary. There is no longer a size at which the law changes, so the
tail is no longer a separate regime from the bulk; it is the bulk's own
law continued. Both phrasings appear in the exchange (A7 §5, A8 §0, "the
system loses its characteristic scale, but it doesn't lose its small-scale
structure"), and this entry keeps them apart.

## Checked against the record

- **[CLAIM-769](CLAIM-769.md)** (a power law from averaging exponentials over a spread of
  rates; [THEORY-2131](../theory.d/THEORY-2131.md)'s gamma mixture). It gives a bulk with a power-law
  tail and no transition at all. So a bulk with a long tail does not by
  itself mark the near side of a transition. What reading (b) adds is the
  *movement*: a cutoff that runs away as a control parameter changes,
  with the bulk held fixed. A fixed mixture has no such parameter.
- **[THEORY-1315](../theory.d/THEORY-1315.md)** (critical slowing down: variance σ²/(2|λ|) and lag-1
  autocorrelation e^(λΔ) rise as the dominant eigenvalue goes to zero).
  The cutoff is the size-domain counterpart. In the cascade, the mean
  1/(1 − R), the variance R/(1 − R)^3 and the cutoff ≈ 2/(1 − R)^2 all
  diverge at R = 1, at different rates. The variance rises *because* the
  cutoff does, since the variance is carried by the tail. So the record's
  variance warning and this reading are not independent evidence of
  nearness to a transition. [LEAD-211](../leads.d/LEAD-211.md) asks what the cutoff adds.

## Checked, and how

With `python3 -I`, from the Borel law in closed form, with tail sums to
5 × 10⁶ and the analytic remainder sqrt(2/(πN)) beyond at R = 1. The
code is in [CASE-303](../cases.d/CASE-303.md).

## What it does not say

- Not that this holds for every transition. It is checked for the
  mean-field (Poisson) cascade. In low-dimensional percolation the
  exponents differ, and the power that multiplies the exponential far
  beyond s_ξ is not τ. This is the lattice-animal exponent, a standard
  result not checked here. Neither changes the separation of scales.
- Not that the tail is negligible. With τ = 3/2 < 2 it carries most of
  the total size ([CLAIM-832](CLAIM-832.md)).

## Note of 2026-11-22: Beck and Cohen, read

Beck and Cohen ([LIT-2962](../literature.d/LIT-2962.md), read in [NOTE-tmpj8ro5](../notes.d/NOTE-tmpj8ro5.md); [THEORY-tmpczldx](../theory.d/THEORY-tmpczldx.md))
**support this reading's contrast with a mixture**, a parallel with no
edge. "A fixed mixture has no such parameter": in superstatistics the only
knob is the variance of the fluctuating parameter (q), which fattens the
power-law tail of the gamma case without any cutoff growing, and the bulk
and the tail come from one average, with no separating scale that closes.
The claim is unchanged.
