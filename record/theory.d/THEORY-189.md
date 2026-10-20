---
number: 189
status: Active
formerly:
- THEORY-tmp5l4pi
title: 'Nested angular cones in the Poincaré ball, symmetric about the outward ray with an aperture depending only on the apex''s radius, are transitive only if the aperture is at most π/2 and r sin ψ(r)/(1 − r²) does not increase outward; so no such cone can be defined near the origin, the widest admissible family is sin ψ = K(1 − r²)/r, and every point a cone contains lies farther from the origin than its apex'
version: 2
history:
- version: 2
  date: '2026-10-19'
  note: >-
    Promoted, carrying out the promotion audit's decision for THEORY-189
    (batch 043, ADR-047 v2). The source asserts the transitivity of the
    closed-form family (its Theorem 4) without proof; the proof, for every
    dimension, is in the dated note below, and meets the promote_when. The
    bound on K is corrected to ε/(1 − ε²), as the source's Eq. 25 reads.
    Title unchanged.
tags:
- mathematics
- representation-learning
date: '2026-10-09'
source:
- LIT-866
summary: >-
  Ganea, Bécigneul and Hofmann (2018), [LIT-866](../literature.d/LIT-866.md): Lemma 2 and
  Theorem 3 prove the necessity half under four stated requirements on the
  cones; the transitivity of the closed-form family (Theorem 4), which
  the source asserts without proof, is proved in this record's note of
  2026-10-19; the radial monotonicity is this record's derivation from
  the hyperbolic law of cosines. It says what a cone
  order on the ball can be, not which posets embed in it, and nothing
  about meets, joins or learned embeddings.
answers:
- QUESTION-025
---
<!-- inactive-ok-file: THEORY-196 QUESTION-025 CLAIM-119 — Proposed or open; cited as the accounts this one sits beside -->

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
  apertures are sin ψ = K(1 − r²)/r, with K ≤ ε/(1 − ε²), which is what
  sin ψ(ε) ≤ 1 requires. Cones narrow
  toward the boundary at that rate.

**Sufficiency, proved here.** The source states that this family is
transitive (Theorem 4) and gives no proof. The proof is in the note of
2026-10-19 below, for every dimension n ≥ 2. Numerical checks found no
violation, in 3,539 sampled chains in two dimensions and in 35,862 in
two, three and five.

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

## Note of 2026-10-19: Theorem 4 proved, in every dimension

The promotion audit (batch 043, [ADR-047](../decisions.d/ADR-047.md) v2) proved the source's Theorem 4: the
family sin ψ(x) = K(1 − ‖x‖²)/‖x‖ on Dⁿ \ B(O, ε), with
K ≤ ε/(1 − ε²), is transitive in every dimension n ≥ 2. The source
asserts this and gives no proof.

**Setting.** Write a = d(O, x). Then sinh a = 2r/(1 − r²), so the family
is sinh(d(O, x)) sin ψ(x) = 2K =: c, a constant. For a point w, θ_x(w) is
the angle at x between the outward ray and the geodesic to w. S_x is the
image under exp_x of the closed solid cone θ ≤ ψ(x). Since exp_x is a
diffeomorphism, S_x is closed, and ∂S_x \ {x} is a smooth hypersurface,
the image of the cone's lateral surface.

1. **Law of sines.** In the triangle O, x, w, the angle at x is π − θ and
   the angle at w is α. Then sin α = sinh(d(O, x)) sin θ / sinh(d(O, w)).
   If θ ≤ π/2, the angle at x is at least π/2, so α < π/2.
2. **Continuation.** Let z ∈ S_y with z ≠ y, and let δ be the direction at
   z that continues the geodesic from y. The angle between δ and z's
   outward ray is the triangle's angle α at z. By step 1 and z ∈ S_y,
   sin α ≤ sinh(d(O, y)) sin ψ(y) / sinh(d(O, z)) = c / sinh(d(O, z)) =
   sin ψ(z). Both angles are acute, so α ≤ ψ(z): δ lies in z's cone of
   directions.
3. **Tangency on the boundary.** Let z ≠ x lie on ∂S_x, on the generator
   from x, and let g be the direction continuing it. By rotational
   symmetry about the axis through O and x, the tangent hyperplane of
   ∂S_x at z is spanned by g and the directions orthogonal to the plane of
   O, x and z. z's outward ray lies in that plane at angle α from g, and
   by step 1 sin α = c / sinh(d(O, z)) = sin ψ(z), so α = ψ(z). So z's
   cone of directions lies in the closed half-space on S_x's side and
   touches the hyperplane only along g.
4. **Transitivity.** Let y ∈ S_x and w ∈ S_y, and suppose w ∉ S_x. Every
   point of the segment from y to w after y lies in S_y, so it is farther
   from O than y (radial monotonicity above) and is not x. Let z be the
   segment's last point in S_x. Then z ∈ ∂S_x and z ≠ x, and by step 2 the
   segment's direction δ at z lies in z's cone. By step 3, either δ points
   strictly into S_x, so the segment is inside S_x just after z, or δ = g,
   so the segment runs along the generator from x, which lies in S_x.
   Either way z is not the last point, a contradiction. So w ∈ S_x.

With Theorem 4 proved, the family is admissible. Theorem 3 bounds every
transitive family with the same K = h(ε) pointwise by this one, so it is
the widest. A numerical check in D², D³ and D⁵ (K = 0.02, 0.1 and 0.3;
35,862 random chains, 30% with points on cone edges) found no violation.
The largest excess θ − ψ was 5 × 10⁻¹², the tangency of step 3. A control
in which h increases with r gave 2,249 violations.

The same review corrected the bound on K. Eq. 25 of the source reads
K ≤ ε/(1 − ε²), equivalently ε ≥ 2K/(1 + √(1 + 4K²)). The earlier
2ε/(1 − ε²) was a misreading.
