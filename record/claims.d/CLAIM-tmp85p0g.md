---
status: Proposed
title: 'An instantaneous ordering is a common currency on a finite set of options, where every complete preorder has a real-valued representation, but not in general: the lexicographic order on the unit square has no real-valued representation, while a continuous complete preorder on a connected separable space has a continuous one; so admitting an ordering is strictly weaker than admitting a currency, a graded lexicographic override lies in the gap while a threshold override does not, and even where each instant has a currency, successive currencies need not share exchange rates'
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
- LIT-tmp1hbb9
- LIT-tmpin6y6
- THEORY-101
- THEORY-090
summary: >-
  The formal half of the owner's reframing of 2026-10-23, that a "common
  currency" is better read as a negotiation admitting an (at least
  instantaneous) ordering. On finite option sets the two coincide at each
  instant. On a continuum they do not: a graded lexicographic order, one
  form ALARM's "100% weight" override could take, admits no numerical
  representation, while a continuous ordering, the form of Veit's
  proportional trade-offs, admits a continuous one (Eilenberg; Debreu). A
  threshold override admits a discontinuous one. Across instants,
  representations need not be related, so a sequence of currencies need
  not be one currency.
---
<!-- inactive-ok-file: THEORY-101 THEORY-090 — Proposed; the two accounts whose distinction the result draws formally, cited as open -->
<!-- inactive-ok-file: LIT-tmpin6y6 — Unavailable, no lawful full text; Debreu 1954, cited for the theorem as Debreu restates it in LIT-tmp1hbb9 -->

# CLAIM-tmp85p0g: An instantaneous ordering is a common currency on a finite set of options, where every complete preorder has a real-valued representation, but not in general: the lexicographic order on the unit square has no real-valued representation, while a continuous complete preorder on a connected separable space has a continuous one; so admitting an ordering is strictly weaker than admitting a currency, a graded lexicographic override lies in the gap while a threshold override does not, and even where each instant has a currency, successive currencies need not share exchange rates

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

**3. A continuous ordering is a currency.** A complete preorder on a
connected, separable topological space whose upper and lower contour sets
are closed has a continuous real-valued representation. The theorem is
essentially Eilenberg's (1941); Debreu (1954, LIT-tmpin6y6) removed the
connectedness assumption for second-countable spaces, and states both in
*Theory of Value* (1959, LIT-tmp1hbb9, read in NOTE-tmpsug0b, pp. 56,
72–73), with the lexicographic order of R² as his example of a complete
preordering that "cannot be represented by a real-valued function"
(p. 72). The lexicographic order of part 2 fails the hypothesis: its
contour sets are not closed.

**3a. Continuity is sufficient, not necessary.** A discontinuous
ordering can still have a representation. Take cost–resource pairs (c, r)
with c, r ∈ [0, 1], a continuous trade-off f(c, r) with values in [0, 1]
for costs at or below a threshold c*, and above it a ranking by cost
alone, resource ignored. Then u(c, r) = f(c, r) for c ≤ c* and
u(c, r) = −c for c > c* represents it: every option above the threshold
is worse than every option below, and the ordering is discontinuous at
c*. What has no representation is a *graded* override, in which the
overriding dimension decides at every level across a continuum and
another dimension still breaks its ties. Above the threshold, a ranking
by cost with resource breaking ties at equal cost is the order of
part 2 again.

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
  currency". A continuous trade-off, Veit's form (THEORY-101), has a
  continuous currency. An override, ALARM's "100% weight" (THEORY-090),
  has no currency only if it is graded, the alarm deciding at every
  level of its own intensity; a threshold override, alarm on or off, has
  a discontinuous one. CLAIM-tmp83ge2 draws the consequence for their
  rivalry.

## What it does not say

- That every ordering without a currency is lexicographic. Others exist
  (orders on non-separable spaces, among them); the claim says only that
  the graded lexicographic one lies in the gap.
- That every override lacks a currency. A threshold override has one
  (part 3a).
- That a negotiation always produces an ordering. It need not (THEORY-027,
  CLAIM-353); that is a separate fact, used in CLAIM-tmpz8lli.
- That anything here is new mathematics. Parts 1 to 3a are textbook
  results of utility theory (Eilenberg; Debreu), written out so the
  record can check them.
