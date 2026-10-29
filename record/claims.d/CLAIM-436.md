---
number: 436
status: Active
formerly:
- CLAIM-tmp85p0g
title: 'An instantaneous ordering is a common currency on a finite set of options, where every complete preorder has a real-valued representation, but not in general: the lexicographic order on the unit square has no real-valued representation, while a continuous complete preorder on a connected separable space has a continuous one; so admitting an ordering is strictly weaker than admitting a currency, a graded lexicographic override lies in the gap while an exact threshold override does not, a threshold override with a discrimination threshold is a lexicographic semiorder whose choices can cycle and so is no ordering at all, and even where each instant has a currency, successive currencies need not share exchange rates'
version: 3
history:
- version: 2
  date: '2026-10-29'
  note: >-
    The eighth status review (ADR-058). THEORY-101 and THEORY-090
    leave grounds: the result is a demonstration and does not stand on
    either reading; they are cited to say which trade-off form is
    Veit's and which ALARM's, and the body's citation is the link. The
    text is unchanged.
- version: 3
  date: '2026-10-29'
  note: >-
    The ninth status review (ADR-057; ADR-047's ruling that a checked
    re-derivation meets a request for a proof). Parts 1, 2, 3, 3b and
    4 re-derived step by step and found correct. Part 3a said "and the
    ordering is discontinuous at c*", which fails when f takes its
    least value all along c = c*; it now says when, with an example,
    checked again by hand. The defeat condition covered only the
    finite construction and the lexicographic argument; it was: "An
    error in the finite construction or in the lexicographic argument
    below, or a misstatement of Debreu's theorem's hypotheses." Status
    Proposed to Active.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the finite construction, in the lexicographic argument, or in
  the constructions of parts 3a and 3b below, or a misstatement of the
  hypotheses of Eilenberg's or Debreu's theorem.
tags:
- mathematics
- emotion-and-affect
date: '2026-10-23'
line:
- formal-apparatus
- organizational-affect
grounds:
- LIT-1435
- LIT-1454
summary: >-
  The formal half of the owner's reframing of 2026-10-23, that a "common
  currency" is better read as a negotiation admitting an (at least
  instantaneous) ordering. On finite option sets the two coincide at each
  instant. On a continuum they do not: a graded lexicographic order, one
  form ALARM's "100% weight" override could take, admits no numerical
  representation, while a continuous ordering, the form of Veit's
  proportional trade-offs, admits a continuous one (Eilenberg; Debreu). A
  threshold override admits a discontinuous one, and one with a
  discrimination threshold, a lexicographic semiorder, can cycle and
  admits no ordering at all (Luce; Tversky). Across instants,
  representations need not be related, so a sequence of currencies need
  not be one currency.
supports:
- CLAIM-435
---
<!-- inactive-ok-file: THEORY-101 THEORY-090 — Proposed; the two accounts whose distinction the result draws formally, cited as open -->
<!-- inactive-ok-file: LIT-1454 — Unavailable, no lawful full text; Debreu 1954, cited for the theorem as Debreu restates it in LIT-1435 -->

# CLAIM-436: An instantaneous ordering is a common currency on a finite set of options, where every complete preorder has a real-valued representation, but not in general: the lexicographic order on the unit square has no real-valued representation, while a continuous complete preorder on a connected separable space has a continuous one; so admitting an ordering is strictly weaker than admitting a currency, a graded lexicographic override lies in the gap while an exact threshold override does not, a threshold override with a discrimination threshold is a lexicographic semiorder whose choices can cycle and so is no ordering at all, and even where each instant has a currency, successive currencies need not share exchange rates

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
essentially Eilenberg's (1941); Debreu (1954, [LIT-1454](../literature.d/LIT-1454.md)) removed the
connectedness assumption for second-countable spaces, and states both in
*Theory of Value* (1959, [LIT-1435](../literature.d/LIT-1435.md), read in [NOTE-1112](../notes.d/NOTE-1112.md), pp. 56,
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
is worse than every option below. The ordering is discontinuous at c*
unless f takes its least value at every point of the line c = c*; with
f(c, r) = (1 + r − c)/2 and c* < 1, for instance, the lower contour set of
(0, 0) contains every option above the threshold but not (c*, 1), which
they approach. What has no representation is a *graded* override, in which the
overriding dimension decides at every level across a continuum and
another dimension still breaks its ties. Above the threshold, a ranking
by cost with resource breaking ties at equal cost is the order of
part 2 again.

**3b. A threshold override with a discrimination threshold is not an
ordering.** Part 3a's threshold is exact. A real override decides by its
own dimension only when the difference on it is large enough to
register, and lets another dimension decide otherwise. With cost c,
resource r and a discrimination threshold δ > 0, let x be chosen over y
when c(y) − c(x) > δ, or when |c(x) − c(y)| ≤ δ and r(x) > r(y). This is
Tversky's lexicographic semiorder, built on Luce's semiorders, in which
indifference within a threshold is not transitive. Its choices can cycle.
Take x₀ = (0, 0), x₁ = (δ/2, 1/3), x₂ = (δ, 2/3), x₃ = (3δ/2, 1). Each
neighbour is within δ on cost and has more resource, so x₁ is chosen
over x₀, x₂ over x₁ and x₃ over x₂; but x₃ costs 3δ/2 more than x₀,
past the threshold, so x₀ is chosen over x₃. No complete preorder on the
four options agrees with all four choices, so the rule admits no
ordering of them, and so no currency. Every pairwise choice is still
decided: each pair, faced alone, is an ordering of two options. The
cycle shows only across choices, which is part 4's case.

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
  currency". A continuous trade-off, Veit's form ([THEORY-101](../theory.d/THEORY-101.md)), has a
  continuous currency. An override, ALARM's "100% weight" ([THEORY-090](../theory.d/THEORY-090.md)),
  has no currency if it is graded, the alarm deciding at every level of
  its own intensity; an exact threshold override has a discontinuous
  one; and a threshold override with a discrimination threshold, the
  realistic case, admits no ordering at all over a chain of nearby
  options, and shows itself as cycles in choice (part 3b). [CLAIM-435](CLAIM-435.md) draws the consequence for their
  rivalry.

- **"Currency" has four senses, and this claim separates two.** Ordinal
  extendibility, ordinal comparability, scalar currency and cardinal
  trade-off structure are successively stronger ([TERM-077](../terms.d/TERM-077.md)).
  "Ordering" here is the second, a complete preorder; a potential needs
  only the first, acyclic wins that some complete ordering extends.
  "Currency" here is the third. Part 4's exchange rates belong to the
  fourth: a representation fixed up to an affine transform, which nothing
  in parts 1 to 3 supplies. [TERM-076](../terms.d/TERM-076.md) once defined a common currency as
  a complete, transitive relation, running the second and third
  together; it was revised before merge to use only the first.

## What it does not say

- That every ordering without a currency is lexicographic. Others exist
  (orders on non-separable spaces, among them); the claim says only that
  the graded lexicographic one lies in the gap.
- That every override lacks a currency. An exact threshold override
  has one (part 3a); with a discrimination threshold it has no ordering
  (part 3b).
- That a negotiation always produces an ordering. It need not ([THEORY-027](../theory.d/THEORY-027.md),
  [CLAIM-353](CLAIM-353.md)); that is a separate fact, used in [CLAIM-440](CLAIM-440.md).
- That anything here is new mathematics. Parts 1 to 3b are textbook
  results of utility theory (Eilenberg; Debreu; Luce; Tversky), written
  out so the record can check them.
