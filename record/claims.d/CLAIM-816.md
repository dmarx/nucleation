---
number: 816
status: Proposed
formerly:
- CLAIM-tmpdwm3z
title: "Hyperbolic entailment embeddings encode depth by radius, and dimension narrows that range twice: Gaussian-like representations projected into the ball inherit a narrow norm range, and matching hyperbolic volume to a tree's growth gives a per-level radial gap that shrinks as 1/(D − 1), so depth has to be calibrated when entailment geometries are compared across widths"
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  Hyperbolic entailment embeddings of one hierarchy trained at several
  widths whose radial spacing between levels does not shrink with
  dimension and whose recovered level order does not degrade when
  Gaussian-like representations are mapped into the ball without radial
  calibration; or an argument that volume matching gives no guide to
  radial placement at all, so that the heuristic's 1/(D − 1) carries no
  information about trained embeddings.
tags:
- representation-learning
- mathematics
date: '2026-11-21'
line:
- learned-structure
bears_on:
- QUESTION-512
grounds:
- THEORY-189
- THEORY-421
- THEORY-196
summary: >-
  A33 §5–§6 and A35 §8 of the exchange "Rich Get Richer Power Laws"
  (2026-11-21), answering the owner's U21 ([QUESTION-512](../questions.d/QUESTION-512.md)). In the Poincaré ball
  radius encodes depth and cones narrow outward, but Gaussian-like radial
  concentration "could eliminate the dynamic range needed to encode
  hierarchy", and the volume-matching heuristic R_k ∼ k ln b/((D − 1)a)
  shrinks the radial gap per level as dimension grows, so "both Euclidean
  concentration and hyperbolic volume growth should be explicitly
  normalized when comparing entailment geometries across DNN widths." The
  wording is A's (the other assistant in the exchange "Rich Get Richer
  Power Laws", A33 and A35); adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-2192 THEORY-2190 CLAIM-860 — Proposed; the readings of Ghadimi Atigh et al. and Bui et al. filed 2026-11-22, and the assistant's norm-growth claim -->
<!-- inactive-ok-file: CLAIM-797 CLAIM-847 THEORY-196 THEORY-188 THEORY-618 — new and Proposed, filed from the exchange "Rich Get Richer Power Laws" on 2026-11-21; Proposed entries the record already held, cited for context -->

# CLAIM-816: Hyperbolic entailment embeddings encode depth by radius, and dimension narrows that range twice: Gaussian-like representations projected into the ball inherit a narrow norm range, and matching hyperbolic volume to a tree's growth gives a per-level radial gap that shrinks as 1/(D − 1), so depth has to be calibrated when entailment geometries are compared across widths

## The claim

**Radius is depth.** A33 §5: in the Poincaré ball "broad, general concepts
are positioned nearer the center", and the standard entailment cone has
half-aperture ψ(r) = arcsin(K(1 − r²)/r), which closes as r → 1 ([THEORY-189](../theory.d/THEORY-189.md),
which also holds that such cones cannot be defined near the origin). Depth,
specificity and aperture are all read off the radius.

**Concentration narrows it.** A33 §5: "If embeddings inherit Gaussian-like
radial concentration and are simply projected into hyperbolic space, their
norms may cluster in a narrow radial range. That could eliminate the dynamic
range needed to encode hierarchy." The annulus of [CLAIM-797](CLAIM-797.md), with relative
width 1/√(2D) for isotropic codes and √(2/D_PR) in general ([CLAIM-847](CLAIM-847.md)), is the
mechanism. The record already holds that, even when trained for it,
distance from the origin is only a partial reading of level ([THEORY-421](../theory.d/THEORY-421.md):
level order recovered for 69–75% of node pairs, root not innermost).

**Volume narrows it again.** A35 §8: at curvature −a², a geodesic ball's
volume grows as e^((D−1)aR); matching that to a tree of branching b, whose
level k has about b^k nodes, gives

R_k ∼ k ln b/((D − 1)a),

"not a general optimal-embedding theorem. It's a volume-matching heuristic.
… At fixed branching factor, the radial separation associated with each
level can shrink as the ambient hyperbolic dimension grows." And A33 §6: the
exponential volume suits trees, "however, high-dimensional Euclidean geometry
can also support very large branching factors, so hyperbolic geometry is not
automatically advantageous at large D."

## Checked

The heuristic's algebra: e^((D−1)aR_k) = b^k gives R_k = k ln b/((D − 1)a).
The concentration half is checked in [CLAIM-797](CLAIM-797.md) and [CLAIM-847](CLAIM-847.md). Nothing here is
checked against trained embeddings.

## What the record holds

[THEORY-189](../theory.d/THEORY-189.md) (the cones and their transitivity), [THEORY-421](../theory.d/THEORY-421.md) (radius a partial
reading of level), [THEORY-196](../theory.d/THEORY-196.md) (the bit cost of hyperbolic tree embeddings:
coordinates linear in the longest path), [THEORY-188](../theory.d/THEORY-188.md) and [THEORY-618](../theory.d/THEORY-618.md)
(hyperbolic geometry for hierarchies in networks and neural circuits). None
says how dimension affects radial depth.

## What it does not say

- Not that hyperbolic embeddings fail at high dimension; that depth must be
  calibrated across widths before levels are compared.

## Note of 2026-11-22: Ghadimi Atigh and colleagues, and Bui and colleagues, read

Two readings, two kinds of bearing.

- **Ghadimi Atigh et al. ([THEORY-2192](../theory.d/THEORY-2192.md), [NOTE-2282](../notes.d/NOTE-2282.md)): weakly
  supports the worry.** The paper relies on depth by radius ("general
  concepts lie closer to the origin and more specific concepts closer to
  the boundary", §3.2), and adds a Busemann term because the
  cross-entropy and entailment losses alone leave samples "biased towards
  internal classes". The radial range has to be enforced by a term of its
  own, not had for free. It sets the dimension to c − 1 without remarking
  on concentration, so it does not test the 1/(D − 1) heuristic.
- **Bui et al. ([THEORY-2190](../theory.d/THEORY-2190.md), [NOTE-2281](../notes.d/NOTE-2281.md)): a parallel.** They
  rescale ‖z‖ by √d and clip at ζ (§4.4), a practical answer to the same
  narrow-norm problem, though their radius means certainty, not depth.
  And in their scheme each cone-constrained update raises the item's norm
  ([CLAIM-860](CLAIM-860.md), the assistant's), so successive generations spend the
  radial range this claim says is narrow; the clipping radius has to be
  raised at each update. No edge.
