---
status: Proposed
title: 'When event sizes fall as s^(−τ) with τ < 2, small events make up most of the count and rare large events most of the total, so the typical event misrepresents the aggregate; near a critical cascade most cascades stay tiny while the mean size diverges'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  A size density s^(−τ) with 1 < τ < 2 on [1, s_max] in which the share
  of the total carried by sizes above any fixed fraction of s_max does not
  tend to a positive constant as s_max grows; or a Poisson cascade near
  R = 1 in which the largest few per cent of cascades do not carry most
  of the events.
tags:
- probabilistic-modeling
- complex-systems
date: '2026-11-21'
line:
- formal-apparatus
grounds:
- CASE-tmpi5vfh
summary: >-
  A's, from A7 §3 and A8 §3 and §7 of the exchange "Rich Get Richer Power
  Laws" (2026-11-20), developing the owner's U5. Probability per
  logarithmic bin goes as s^(1−τ) and total size per bin as s^(2−τ). For
  τ < 2 the large scales carry the aggregate. "Most observations are
  small" differs from "most of the total activity comes from small
  observations". At R = 1, 37% of Poisson cascades are single events
  while the mean is infinite. The assistant adds the finite numbers A
  does not give (ledger gap): at R = 0.99 the cascades above 1,000 are
  1.7% of cascades and 76% of all events. The wording is A's (the other
  assistant in the exchange "Rich Get Richer Power Laws", A7 and A8);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-tmpi5vfh CLAIM-tmpr9au6 CLAIM-tmplb1ow — Proposed or new; the case and claims filed with this one from the same exchange -->

# CLAIM-tmpninc2: When event sizes fall as s^(−τ) with τ < 2, small events make up most of the count and rare large events most of the total, so the typical event misrepresents the aggregate; near a critical cascade most cascades stay tiny while the mean size diverges

## The claim (A7, A8)

A7 §3: "A sparse tail need not be insignificant." For a density
p(s) ∝ s^(−τ), the probability in a logarithmic interval goes as
s·p(s) ∝ s^(1−τ). The total magnitude in it goes as "**s²p(s) ∝
s^(2−τ)**". For 1 < τ < 2, "Larger scales increasingly dominate total
magnitude". At τ = 2, "Each logarithmic size interval contributes roughly
equally". For τ > 2, "Smaller scales contribute more total magnitude".
Critical branching has τ = 3/2, and its mean below criticality,
E[S] = 1/(1 − R), diverges as R → 1⁻. So two readings of the owner's U5
(CLAIM-tmpr9au6) part:

- "**Most observations are small:** Often true near criticality."
- "**Most of the total activity comes from small observations:** Not
  necessarily true."

A8 §3 gives the cascade numbers: at R = 1, "about 37% of all cascades
consist of a single event. Yet the expected total cascade size is
infinite." Between R = 0.99 and 0.999, "the probability of a single-event
cascade barely changes, yet the average cascade size increases tenfold.
**The approaching transition is much more apparent in the extreme events
than in the most common ones.**" A8 §7: "Its modal behavior and its
aggregate behavior can be dominated by completely different parts of the
distribution … characterizing a system by a representative event can be
misleading."

## Checked, with the finite numbers (the assistant's)

A says a system "may" be dominated by rare large events but gives no
finite estimate. For the Poisson cascade at R = 0.99 (CASE-tmpi5vfh),
computed from the Borel law:

| cascades larger than | share of cascades | share of all events |
|---|---:|---:|
| 10 | 23.8% | 98.0% |
| 100 | 7.1% | 92.6% |
| 1,000 | 1.7% | 75.6% |
| 10,000 | 0.17% | 31.8% |

For a pure power law with τ = 3/2 cut off at s_max, the share of the
total from sizes above s_max/100 is (s_max^(1/2) − (s_max/100)^(1/2)) /
(s_max^(1/2) − 1), which tends to 0.9 as s_max grows. A tenth of the
log-range carries most of the total, however large the system. A8 §7's
"In a finite system, those moments become strongly dependent on the
largest accessible scales" is this.

## What it does not say

- Not that every near-critical system is dangerous. A8 §7: "That doesn't
  mean every critical system is dangerous or unstable".
- Not that τ < 2 is general. Percolation clusters in two dimensions have
  τ ≈ 2.055 (A5 §2). There the sites per logarithmic bin fall slowly with
  size, though the mean size of the cluster a given site belongs to still
  diverges at p_c, since s³n_s ∝ s^(3−τ) grows.
- The complement on the scale side is CLAIM-tmplb1ow: the bulk stays put
  while the tail lengthens.
