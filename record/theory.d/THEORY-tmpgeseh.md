---
status: Proposed
promote_when: >-
  The original (Jordan & Graves 1995) is read and states that a chaining configuration of limited flexibility attains nearly all the expected sales of full flexibility in its simulations.
title: 'Jordan and Graves: in a plant–product network facing uncertain demand, limited flexibility in which each plant makes a few products, configured to chain all plants and products together, gives nearly all the expected sales of full flexibility'
version: 1
tags:
- operations-research
- probabilistic-modeling
date: '2026-11-04'
source:
- LIT-tmptozb9
summary: >-
  Jordan and Graves (1995), [LIT-tmpaku09](../literature.d/LIT-tmpaku09.md), unread, as reported by Chou, Chua, Teo and Zheng (2010), [LIT-tmptozb9](../literature.d/LIT-tmptozb9.md), skimmed in [NOTE-tmpsnl7o](../notes.d/NOTE-tmpsnl7o.md) (§§1–2, Theorems 1–2, §§5–6). Jordan and Graves found it by simulation (about 95% in a 10 by 10 example); Chou et al. prove it asymptotically for balanced, independent demand (at least 89% for uniform, about 96% for normal). Proposed until the original is read. It does not hold for every demand: with correlated demand a sparse structure can serve almost none of it.
---
<!-- inactive-ok-file: LIT-tmpaku09 NOTE-tmpsnl7o — Unfetched or Skimmed, and new; the unread original and the reading of the neighbour that stands in for it, cited as open -->

# THEORY-tmpgeseh: Jordan and Graves: in a plant–product network facing uncertain demand, limited flexibility in which each plant makes a few products, configured to chain all plants and products together, gives nearly all the expected sales of full flexibility

## Source

Jordan and Graves (1995), [LIT-tmpaku09](../literature.d/LIT-tmpaku09.md), the original, which was not read: the working-paper copies located at MIT DSpace and CORE could not be fetched. Sourced to Chou, Chua, Teo and Zheng (2010), [LIT-tmptozb9](../literature.d/LIT-tmptozb9.md), read in part in [NOTE-tmpsnl7o](../notes.d/NOTE-tmpsnl7o.md), which stands in for it at the owner's request.

## What was actually shown

- **By simulation, as reported** (§2, p. 45): Jordan and Graves "observe,
  through extensive simulation, that limited flexibility, configured the
  right way, yields most of the benefits (in terms of expected sales) of
  full flexibility". The configuration is chaining, in which "every
  facility can produce two products and every product can be produced by
  two facilities", and in a 10×10 example "chaining achieves about 95% of
  the" benefits (p. 46).
- **Analytically, by the neighbour** (§1, p. 45; Theorem 2, p. 49): for
  balanced, identical systems with i.i.d. demand symmetric about its mean,
  the long chain reaps "at least 89% and 96%, respectively" of full
  flexibility's benefit for uniform and normal demand, as the number of
  plants grows without bound. This is the neighbour's result, not Jordan
  and Graves's; it could have come out lower, and is the part of the
  account checked here.

## What this does not say

- That the original states the principle in these words: it was not read,
  and the neighbour gives only paraphrase.
- That chaining works for any demand: "If demands are correlated, the
  situation can be very different" (§1, p. 44), and in the authors'
  extreme example a sparse structure serves only O(1) of n units of
  expected demand.
- Anything beyond a single period with lost sales, or about the cost of
  links, which the neighbour does not report from the original.
- That flexibility of this kind is a reserve for rare events: it is
  standing capacity to re-route work under realised demand.
