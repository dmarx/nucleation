---
number: 189
status: Proposed
formerly:
- THEORY-tmp5l4pi
promote_when: >-
  A complete proof that the family sin ψ(x) = K(1 − ‖x‖²)/‖x‖ on
  Dⁿ \ B(O, ε) is transitive (y in S_x implies S_y inside S_x) in every
  dimension n ≥ 2, which the source asserts as "similar to" the proof of
  its necessity theorem and does not give. Or a pair of points with tight
  cones near the boundary of S_x for which nesting fails, which would
  refute it. More sampled chains without a violation cannot settle it,
  and nor can link-prediction scores, which test learned embeddings, not
  the geometry.
title: 'Nested angular cones in the Poincaré ball, symmetric about the outward ray with an aperture depending only on the apex''s radius, are transitive only if the aperture is at most π/2 and r sin ψ(r)/(1 − r²) does not increase outward; so no such cone can be defined near the origin, the widest admissible family is sin ψ = K(1 − r²)/r, and every point a cone contains lies farther from the origin than its apex'
version: 1
tags:
- mathematics
- representation-learning
date: '2026-10-09'
source:
- LIT-866
summary: >-
  Ganea, Bécigneul and Hofmann (2018), [LIT-866](../literature.d/LIT-866.md): Lemma 2 and
  Theorem 3 prove the necessity half under four stated requirements on the
  cones; the transitivity of the closed-form family (Theorem 4) is
  asserted without proof; the radial monotonicity is this record's
  derivation from the hyperbolic law of cosines. It says what a cone
  order on the ball can be, not which posets embed in it, and nothing
  about meets, joins or learned embeddings.
---
<!-- inactive-ok-file: THEORY-196 THEORY-185 QUESTION-025 CLAIM-119 — Proposed or open; cited as the accounts this one sits beside -->

# THEORY-189: Nested angular cones in the Poincaré ball, symmetric about the outward ray with an aperture depending only on the apex's radius, are transitive only if the aperture is at most π/2 and r sin ψ(r)/(1 − r²) does not increase outward; so no such cone can be defined near the origin, the widest admissible family is sin ψ = K(1 − r²)/r, and every point a cone contains lies farther from the origin than its apex

## Source

Ganea, Bécigneul and Hofmann (2018), [LIT-866](../literature.d/LIT-866.md): §3, Lemma 2,
Theorems 3–5 and Appendices E–G, as read in [NOTE-671](../notes.d/NOTE-671.md).

## What was actually shown

**The setting.** A cone at x in the Poincaré ball Dⁿ is the exponential
map of the tangent vectors within angle ψ(x) of the outward direction
through x. The source asks four things of a family of such cones:

1. symmetry about the outward ray;
2. an aperture depending only on ‖x‖;
3. a continuous aperture;
4. transitivity: if y lies in x's cone, y's cone lies inside x's.

Under the fourth, "y in S_x" is a transitive relation, and with the
radial point below it, a partial order.

**Necessity, proved.**

- **Lemma 2: the aperture is at most π/2.** If it were wider, the
  points on the cone's boundary would need apertures of at most π/2.
  Continuity along the boundary back to the apex then gives a
  contradiction.
- **Theorem 3: h(r) = r sin ψ(r)/(1 − r²) cannot increase with r.**
  The proof applies the hyperbolic law of sines in the triangle formed
  by the origin, an apex and a point on its cone's boundary.
- **Consequences.** h tends to 0 at the origin, so no family with
  non-zero apertures covers a neighbourhood of it. The order has no top
  element in the geometry, and the family lives outside a ball B(O, ε).
- **The widest family.** For a given K = h(ε), the pointwise widest
  apertures are sin ψ = K(1 − r²)/r, with K ≤ 2ε/(1 − ε²). Cones narrow
  toward the boundary at that rate.

**Sufficiency, asserted.** The source states that this family is
transitive (Theorem 4) and gives no proof. A numerical check in two
dimensions found no violation in 3,539 sampled chains. That is
consistent with the claim, but it is not a proof.

**Radial monotonicity, derived here.** Membership is the angle test
π − ∠Oxy ≤ ψ(x) ≤ π/2 (the source's Theorem 5), so ∠Oxy ≥ π/2. In a
hyperbolic triangle the side opposite an angle of at least π/2 is the
longest: cosh d(O, y) ≥ cosh d(O, x) cosh d(x, y) > cosh d(O, x). So every
point of x's cone is strictly farther from the origin than x. Along any
chain of the order, distance from the origin increases, and the relation
is antisymmetric.

**What could have come out otherwise.** The necessity results could
have left the aperture free near the origin, or allowed cones wider than
a half-space. They do not.

## What this does not say

- **It does not say which partial orders embed.** Cones of incomparable
  points can overlap, so a point may lie below two incomparable apexes,
  and a DAG with shared descendants is expressible. Nothing here bounds
  the dimension a given poset needs, or says that every finite poset
  embeds at all.
- **It does not give a lattice.** The intersection of two cones is not in
  general a cone, so meets and joins have no geometric counterpart. A
  concept lattice can at best be embedded as an order, not as a lattice
  ([CLAIM-119](../claims.d/CLAIM-119.md), [QUESTION-025](../questions.d/QUESTION-025.md)).
- **The constraints are conditional on the four requirements.** Drop
  rotation invariance or axial symmetry, and other families, including
  ones defined at the origin, are not excluded by these proofs. "Optimal"
  in the source means widest pointwise for a given K, not unique or best
  by any other measure.
- **It says nothing about learned embeddings.** That trained cones
  realise the order, or that the hyperbolic version outperforms because
  of curvature, are separate empirical claims. The source's own
  experiment leaves both open: it has single runs, a failure of every
  method when only the transitive reduction is trained on, and Euclidean
  cones that match hyperbolic ones when initialised alike.
- **It is not a statement about linear directions.** It neither supports
  nor contradicts [THEORY-185](THEORY-185.md). It describes a different encoding of
  implication, by region containment, beside the distance encoding of
  [THEORY-196](THEORY-196.md). The precision cost that THEORY describes applies to the
  narrow cones near the boundary, but that connection is the record's,
  not the source's.
