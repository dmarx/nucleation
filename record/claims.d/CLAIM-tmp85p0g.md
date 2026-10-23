---
status: Proposed
title: 'An instantaneous ordering is a common currency on a finite set of options, where every complete preorder has a real-valued representation, but not in general: the lexicographic order on the unit square has no real-valued representation, while a continuous complete preorder on a connected separable space has a continuous one; so admitting an ordering is strictly weaker than admitting a currency, a lexicographic override lies in the gap, and even where each instant has a currency, successive currencies need not share exchange rates'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the finite construction or in the lexicographic argument
  below, or a misstatement of Debreu's theorem's hypotheses.
tags:
- mathematics
- emotion-and-affect
date: '2026-10-23'
line:
- formal-apparatus
- organizational-affect
grounds:
- THEORY-101
- THEORY-090
summary: >-
  The formal half of the owner's reframing of 2026-10-23, that a "common
  currency" is better read as a negotiation admitting an (at least
  instantaneous) ordering. On finite option sets the two coincide at each
  instant. On a continuum they do not: a lexicographic order, the form of
  ALARM's "100% weight" override, admits no numerical representation,
  while a continuous ordering, the form of Veit's proportional trade-offs,
  admits a continuous one (Debreu). Across instants, representations need
  not be related, so a sequence of currencies need not be one currency.
---
<!-- inactive-ok-file: THEORY-101 THEORY-090 — Proposed; the two accounts whose distinction the result draws formally, cited as open -->

# CLAIM-tmp85p0g: An instantaneous ordering is a common currency on a finite set of options, where every complete preorder has a real-valued representation, but not in general: the lexicographic order on the unit square has no real-valued representation, while a continuous complete preorder on a connected separable space has a continuous one; so admitting an ordering is strictly weaker than admitting a currency, a lexicographic override lies in the gap, and even where each instant has a currency, successive currencies need not share exchange rates

## The claim

Read a **currency** on a set X as a function u : X → ℝ that represents a
relation ⪰ on X: x ⪰ y exactly when u(x) ≥ u(y). Read an **ordering** as
a complete preorder (complete and transitive).

**1. On a finite set, every ordering is a currency.** Let ⪰ be a complete
preorder on a finite X and put u(x) = |{z ∈ X : x ⪰ z}|. If x ⪰ y, then
y ⪰ z gives x ⪰ z by transitivity, so {z : y ⪰ z} ⊆ {z : x ⪰ z} and
u(x) ≥ u(y). If not x ⪰ y, completeness gives y ⪰ x, so by the same
argument {z : x ⪰ z} ⊆ {z : y ⪰ z}. The inclusion is strict: y is in
{z : y ⪰ z}, since a complete relation is reflexive, and y is not in
{z : x ⪰ z}, since not x ⪰ y. So u(y) > u(x), and u represents ⪰.

**2. On the unit square, the lexicographic order is not a currency.**
Let (a, b) ⪰ (a′, b′) when a > a′, or a = a′ and b ≥ b′, on [0, 1]².
Suppose u represented it. For each a ∈ [0, 1], (a, 1) ≻ (a, 0), so the
open interval I_a = (u(a, 0), u(a, 1)) is non-empty. If a < a′, then
(a′, 0) ≻ (a, 1), so u(a′, 0) > u(a, 1): the intervals are pairwise
disjoint. Each contains a rational, and distinct intervals contain
distinct rationals, so there would be uncountably many rationals. No
such u exists.

**3. A continuous ordering is a currency.** By Debreu's representation
theorem, a complete preorder on a connected, separable topological space
whose upper and lower contour sets are closed has a continuous
real-valued representation. The lexicographic order of part 2 fails the
hypothesis: its contour sets are not closed.

**4. Successive currencies need not share exchange rates.** If R_t is an
ordering at each t with representation u_t, nothing relates u_t to u_s:
any strictly increasing transformation of u_t represents R_t equally
well, and R_t and R_s may disagree. A sequence of orderings can even
cycle across time, x above y at t, y above z at s, z above x at r, with
each instant's ordering a currency. A currency that holds its exchange
rates over time is a further fact, not a consequence of having one at
each instant.

## What it means for the reframing

- **Where options are few and discrete, the reframing is a
  relabelling** at any single instant, by part 1. Its content there is
  part 4: the record's word "ordering" does not promise stable rates.
- **Where magnitudes are continuous**, as in the trade-off experiments
  Veit's criterion uses (a noxious cost against a resource, in proportion
  to both), "admits an ordering" is strictly weaker than "admits a
  currency". A lexicographic override, the form ALARM's "100% weight"
  takes ([THEORY-090](../theory.d/THEORY-090.md)), is an ordering with no currency. A continuous
  trade-off, Veit's form ([THEORY-101](../theory.d/THEORY-101.md)), is an ordering with a continuous
  currency. [CLAIM-tmp83ge2](CLAIM-tmp83ge2.md) draws the consequence for their rivalry.

## What it does not say

- That every ordering without a currency is lexicographic. Others exist
  (orders on non-separable spaces, among them); the claim says only that
  the lexicographic one lies in the gap.
- That a negotiation always produces an ordering. It need not ([THEORY-027](../theory.d/THEORY-027.md),
  [CLAIM-353](CLAIM-353.md)); that is a separate fact, used in [CLAIM-tmpz8lli](CLAIM-tmpz8lli.md).
- That anything here is new mathematics. Parts 1 to 3 are textbook
  results of utility theory, written out so the record can check them.
