---
number: 1392
status: Active
formerly:
- THEORY-tmpgeseh
title: 'Chou, Chua, Teo and Zheng report that Jordan and Graves found by simulation that limited flexibility configured as a chain gives most of the expected sales of full flexibility, and prove that for balanced plants with independent, identically distributed symmetric demand the long chain keeps about 89.6% (uniform) and 96% (normal, coefficient of variation 0.33) of full flexibility''s expected sales as the system grows, a smaller share of its gain over dedicated plants, and less for more variable demand'
version: 2
history:
- version: 1
  date: '2026-11-04'
  note: >-
    Filed Proposed from NOTE-1604, the reading in part of Chou, Chua, Teo
    and Zheng (LIT-2101), standing in for the unread Jordan and Graves
    (1995), LIT-2045.
- version: 2
  date: '2026-11-06'
  note: >-
    Narrowed and promoted by the twenty-ninth status review, at the status
    review's ruling (the owner delegated these rulings); ADR-065; ADR-047,
    kind 3. NOTE-1604 v2 reads §§1–3 and §6 of the neighbour in full. The
    title now reports what the neighbour reports of Jordan and Graves and
    what it proves. The old title's "nearly all the expected sales"
    overstated even the report, which says "most" and "about 95%". The
    old title also asserted Jordan and Graves's finding directly; the
    attribution is recorded in LIT-2045's status note, and the original
    stays unread. The body's "at least 89% and 96% ... of full
    flexibility's benefit" conflated the paper's two measures, the ratio
    of expected sales and the normalized gain over dedicated plants, and
    is corrected. The old title: Jordan and Graves: in a plant–product
    network facing uncertain demand, limited flexibility in which each
    plant makes a few products, configured to chain all plants and
    products together, gives nearly all the expected sales of full
    flexibility. The old promote_when: "The original (Jordan & Graves
    1995) is read and states that a chaining configuration of limited
    flexibility attains nearly all the expected sales of full flexibility
    in its simulations."
tags:
- operations-research
- probabilistic-modeling
date: '2026-11-04'
source:
- LIT-2101
summary: >-
  Jordan and Graves (1995), [LIT-2045](../literature.d/LIT-2045.md), unread, as reported by Chou, Chua,
  Teo and Zheng (2010), [LIT-2101](../literature.d/LIT-2101.md), read in [NOTE-1604](../notes.d/NOTE-1604.md) (§§1–3, §6; §4 to
  Theorem 3). Jordan and Graves found by simulation that chaining yields
  most of full flexibility's expected sales, about 95% in a 10 by 10
  example. Chou et al. prove results for balanced, independent, symmetric
  demand as the system grows. The chain's expected sales are 43/48 of full
  flexibility's for uniform demand and 0.96 for normal demand with CV 0.33.
  Its gains over dedicated plants are 58% and about 70% of full
  flexibility's. Two-point demand gives 75% of sales. Active as a report of
  the neighbour. With correlated demand a sparse structure can serve almost
  none of it.
---
<!-- inactive-ok-file: LIT-2045 — Unfetched; the unread original the neighbour reports, cited as open -->

# THEORY-1392: Chou, Chua, Teo and Zheng report that Jordan and Graves found by simulation that limited flexibility configured as a chain gives most of the expected sales of full flexibility, and prove that for balanced plants with independent, identically distributed symmetric demand the long chain keeps about 89.6% (uniform) and 96% (normal, coefficient of variation 0.33) of full flexibility's expected sales as the system grows, a smaller share of its gain over dedicated plants, and less for more variable demand

## Source

Jordan and Graves (1995), [LIT-2045](../literature.d/LIT-2045.md), the original, which was not read: the
working-paper copies located at MIT DSpace and CORE could not be fetched.
Sourced to Chou, Chua, Teo and Zheng (2010), [LIT-2101](../literature.d/LIT-2101.md), read in [NOTE-1604](../notes.d/NOTE-1604.md),
which stands in for it at the owner's request.

## What was actually shown

- **By simulation, as reported** (§2, p. 45): Jordan and Graves "observe,
  through extensive simulation, that limited flexibility, configured the
  right way, yields most of the benefits (in terms of expected sales) of
  full flexibility". The configuration is chaining, in which "every
  facility can produce two products and every product can be produced by
  two facilities", and in a 10×10 example "chaining achieves about 95% of
  the" benefits (p. 46).
- **Analytically, by the neighbour** (§3.2, pp. 49–50; Theorem 2, p. 49):
  the setting is balanced, identical systems with i.i.d. demand symmetric
  about its mean, as the number of plants grows. The long chain's expected
  sales are then 43/48 ≈ 89.6% of full flexibility's for uniform demand and
  0.9614 for normal demand with CV 0.33 (Table 2). Its gain over dedicated
  plants, as a share of full flexibility's gain (the asymptotic chaining
  efficiency, ACE), is 7/12 ≈ 58% and about 0.70 (Table 1). Two-point
  demand gives 75% of sales and an ACE of 0.5 (p. 49). The conclusion:
  "our method returns an efficiency measurement ACE of at least 58% and
  70%, respectively. The ratio of the expected sales from chaining to the
  full flexibility system is even more impressive" (p. 57). This is the
  neighbour's result, not Jordan and Graves's. It is reproduced by
  simulation in scratch/formal/chou_chain_check.py.

## What this does not say

- That the original states the principle in these words: it was not read,
  and the neighbour gives only paraphrase.
- That the chain keeps nearly all of full flexibility's value whatever the
  yardstick: of the gain over dedicated plants it keeps 58–70% for the
  distributions computed.
- That chaining works for any demand: "If demands are correlated, the
  situation can be very different" (§1, p. 44), and in the authors'
  extreme example a sparse structure serves only O(1) of n units of
  expected demand.
- Anything beyond a single period with lost sales, or about the cost of
  links, which the neighbour does not report from the original.
- That flexibility of this kind is a reserve for rare events: it is
  standing capacity to re-route work under realised demand.
