---
number: 860
status: Proposed
formerly:
- CLAIM-tmpxcy5s
title: "In the Lorentz model every point of an entailment cone of the widest transitive family lies farther from the origin than the cone's apex, so a scheme that keeps each item's new embedding inside the cone of its old one must raise the item's norm at every update that moves it, which drives a norm-based uncertainty down whether or not the update is correct and accounts for the norm growth such schemes report"
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  A point satisfying the cone test π − ∠(O, x, y) ≤ ψ(x), with
  sinh(√K·d(O, x)) sin ψ(x) = 2ε and ψ(x) ≤ π/2, that lies no farther from
  the origin than x and is not x; or an error in the identification of
  Bui and colleagues' Eq. 11 with that family. Not defeated by new
  embeddings outside their cones, which a soft penalty allows and the
  claim does not cover; nor by a cone family with half-apertures above
  π/2, where the claim says it fails; nor by a bounded total growth,
  since the claim says the norm rises at each update, not that it
  diverges.
tags:
- representation-learning
- mathematics
date: '2026-11-22'
line:
- learned-structure
grounds:
- THEORY-189
- THEORY-2190
bears_on:
- QUESTION-512
summary: >-
  A gap in Bui and colleagues' backward-compatible training
  ([THEORY-2190](../theory.d/THEORY-2190.md), [NOTE-2281](../notes.d/NOTE-2281.md)), filled: their Eq. 11 is [THEORY-189](../theory.d/THEORY-189.md)'s
  widest transitive cone family in Lorentz form, sinh(√K·d) sin ψ = 2ε,
  and a cone with half-aperture at most π/2 holds only points farther
  from the origin than its apex. So a satisfied constraint raises each
  moved item's norm and lowers its norm-based uncertainty at every update,
  correct or not, which is what their raised clipping radius and falling
  gallery uncertainty show and what they list as a limitation without
  deriving it. Checked numerically in the Lorentz model. The wording is
  the assistant's (Claude, in this session); adopting it is the owner's
  call.
---
<!-- inactive-ok-file: THEORY-2190 CLAIM-839 CLAIM-816 ARG-193 — Proposed or new; the reading this fills a gap in, the claims it bears on and the argument that says how -->

# CLAIM-860: In the Lorentz model every point of an entailment cone of the widest transitive family lies farther from the origin than the cone's apex, so a scheme that keeps each item's new embedding inside the cone of its old one must raise the item's norm at every update that moves it, which drives a norm-based uncertainty down whether or not the update is correct and accounts for the norm growth such schemes report

## The gap

Bui and colleagues ([THEORY-2190](../theory.d/THEORY-2190.md)) penalise each new embedding h_n for
leaving the cone of the same item's old embedding h_o, and read
uncertainty from the radius. They raise the new model's clipping
threshold, ζ_n = ζ_o + 0.2, "to account for the evolution in the
embedding space", observe that "As the model improves, the uncertainty
in the gallery embeddings decreases", and list as a limitation that "This
may lead to instability as norms grow". They present these as empirical.
They follow from the cone.

## The claim

**Eq. 11 is [THEORY-189](../theory.d/THEORY-189.md)'s family.** In the Lorentz model of curvature −K,
a point at distance d from the origin O has √K‖h_space‖ = sinh(√K·d).
Bui's half-aperture aper(h_o) = sin⁻¹(2ε/(√K‖h_o,space‖)) therefore reads
sinh(√K·d) sin ψ = 2ε, which at K = 1 is [THEORY-189](../theory.d/THEORY-189.md)'s widest transitive
family sinh(d(O, x)) sin ψ(x) = 2K, with Bui's ε for Ganea's K.

**Radial monotonicity.** Membership is the test
ext(x, y) = π − ∠(O, x, y) ≤ ψ(x). If ψ(x) ≤ π/2, then ∠(O, x, y) ≥ π/2,
and in a hyperbolic triangle the side opposite an angle of at least π/2
is the longest: cosh(√K·d(O, y)) = cosh(√K·d(O, x)) cosh(√K·d(x, y))
− sinh(√K·d(O, x)) sinh(√K·d(x, y)) cos∠(O, x, y)
≥ cosh(√K·d(O, x)) cosh(√K·d(x, y)) > cosh(√K·d(O, x)) for y ≠ x. This is
[THEORY-189](../theory.d/THEORY-189.md)'s derivation, carried to curvature −K.

**Consequences for the scheme.**

- Each update that moves an item and satisfies its constraint raises the
  item's distance from the origin, and so its norm ‖z‖ and its time
  coordinate.
- Bui's uncertainty, 1 − (1/√K) tanh(√K‖z‖) (Eq. 10), strictly decreases
  in ‖z‖, so it falls at every such update. Nothing in the cone term
  depends on whether the new embedding is closer to the item's true
  class; correctness enters only through the base loss.
- By transitivity ([THEORY-189](../theory.d/THEORY-189.md)), the generations of one item form a chain
  of nested cones, so the constraint carries to non-adjacent generations,
  and the norm rises monotonically along the chain.
- A clipping radius held fixed eventually binds: Table 4's ζ_n = 1.0
  harms cross-model compatibility, as the claim predicts.

## Checked

With `python3 -I` (a script kept in the session's scratchpad, not in the
repository): 960,000 sampled pairs (apex x, point y) in the Lorentz model,
for K ∈ {0.5, 1, 2}, dimensions n ∈ {2, 3, 8, 128} and ε = 0.1. Apexes at
distances from the edge of definition, sinh(√K·d) = 2ε (half-aperture up
to 89.99999°), out to √K·d = 12; points by the exponential map at x along
random unit tangents, at exponentially distributed lengths. The angle
∠(O, x, y) was computed from the tangent vectors at x by Minkowski inner
products, not from the law of cosines, and √K‖x_space‖ = sinh(√K·d) was
confirmed for every apex. Of 132,178 points inside their cones, none lay
nearer the origin than the apex; the least ratio d(O, y)/d(O, x) was
1.0000002. An uncapped run found 11 apparent exceptions, all at
√K·d > 19, where float64 returns an exterior angle of exactly 0 for
points plainly off the axis; they are rounding, and the cap removes them.

The condition is needed. Replacing ψ by a fixed half-aperture (K = 1,
n = 3): at 89.9° and 90°, 0 of 14,849 and 0 of 15,180 in-cone points lay
nearer the origin; at 95°, 66 of 15,782; at 100°, 233 of 16,386; at 120°,
1,662 of 19,467. Bui's arcsin never exceeds π/2 where it is defined, so
their cones meet the condition.

## Under which conditions it holds

- **Only for embeddings that satisfy their constraint.** Bui's hinge is
  soft (weighted 0.3), and they never report how many new embeddings lie
  inside their cones. A new embedding outside its cone can lie nearer the
  origin. The claim explains the observed growth to the extent the
  constraint is met.
- **Half-aperture at most π/2**, which Eq. 11 gives wherever
  √K‖h_o,space‖ ≥ 2ε. Nearer the origin the arcsin is undefined, and
  [THEORY-189](../theory.d/THEORY-189.md) holds that no transitive family is defined there.
- **Monotone, not unbounded.** Each step raises the norm, but the steps
  can be small; unbounded growth needs updates that keep moving items by
  amounts that do not shrink fast enough. Raising ζ at each update permits
  that, and the paper's "norms grow (e.g., ≥ 10.)" reports it.

## What it does not say

That the scheme fails, or that norm growth is the only cause of the
falling uncertainty: the new model may also be more confident because it
is better. The claim is that the cone term lowers the norm-based
uncertainty by itself, so that signal cannot certify an update's
correctness ([ARG-193](../arguments.d/ARG-193.md), on [CLAIM-839](CLAIM-839.md)'s rule that a narrower region
counts as progress only while it stays correct). It bears on [THEORY-421](../theory.d/THEORY-421.md),
which holds that radius is only a partial reading of level even when
trained for hierarchy, and on [CLAIM-816](CLAIM-816.md), whose narrow radial range each
cone-constrained update spends.
