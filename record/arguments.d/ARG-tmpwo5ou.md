---
status: Proposed
title: 'From the spherical-cap null to the cost of restricting hyperbolic entailment cones'
version: 1
form: analogy
rests_on:
- CLAIM-tmpqqngq
grounds:
- THEORY-189
concludes:
- CLAIM-tmpr4k9z
tags:
- representation-learning
- mathematics
date: '2026-11-21'
line:
- learned-structure
summary: >-
  A33 §3–§4 computes how costly cone restriction is in high dimension for
  spherical caps about the origin, and A33 §10 then states that
  "concentration of measure determines the geometric cost of restricting"
  entailment regions ([CLAIM-tmpr4k9z](../claims.d/CLAIM-tmpr4k9z.md)). The filing finds the analogy carries to the
  angular part of a hyperbolic cone, in the tangent space at its apex, and
  not to the radial structure that makes Ganea's cones what they are; so it
  supports the conclusion only in that narrower form. Proposed: the verdict
  is the filer's (Claude, in this session); adopting it is the owner's
  call.
---
<!-- inactive-ok-file: CLAIM-tmpqqngq CLAIM-tmpr4k9z CLAIM-tmpdwm3z — new and Proposed, filed from the exchange "Rich Get Richer Power Laws" on 2026-11-21 -->

# ARG-tmpwo5ou: From the spherical-cap null to the cost of restricting hyperbolic entailment cones

## The inference

Premise ([CLAIM-tmpqqngq](../claims.d/CLAIM-tmpqqngq.md)): on S^(D−1) the share of directions within half-angle ψ of
an axis falls exponentially in D at fixed ψ, a fixed share needs
ψ_D = π/2 − a/√D, and a tilt must be of order √D or D to fill such caps.

Conclusion ([CLAIM-tmpr4k9z](../claims.d/CLAIM-tmpr4k9z.md), from A33 §10): "Concentration of measure determines the
geometric cost of restricting those regions", the entailment regions of a
hyperbolic cone system.

## Critical questions

**In what respect are they alike, and is it the respect the conclusion
needs?** Both are sets of directions within an angle of an axis. A
hyperbolic entailment cone at apex x is defined by the angle, measured at x,
between the cone's axis (the outward ray) and the geodesic to a point
([THEORY-189](../theory.d/THEORY-189.md)). In the tangent space at x, which is D-dimensional, the set of
admissible initial directions is a spherical cap of half-angle ψ(‖x‖). Its
share of directions is q_D(ψ(‖x‖)), so the premise does apply to it: at fixed
aperture, the share of directions a cone admits from its apex falls
exponentially with D.

**What relevant difference is there?** Three.

- The apex is not the origin. A33's caps are measured from the origin, and
  [THEORY-189](../theory.d/THEORY-189.md) holds that no cone of the family can be defined near the
  origin; A33 says its table is "not the volumes of hyperbolic entailment
  cones". So the premise is about the apex's tangent directions, not about
  the population of embeddings measured from the centre, which is what the
  annulus and the von Mises–Fisher calculation describe.
- The aperture depends on depth. ψ(r) = arcsin(K(1 − r²)/r) shrinks
  outward, so the cost of restriction is set by radius as well as angle, and
  radius is the coordinate concentration narrows ([CLAIM-tmpdwm3z](../claims.d/CLAIM-tmpdwm3z.md)).
- The measure. "Cost" needs a reference measure; under the uniform measure
  on the ball's directions it is the cap share, but A33 itself notes there
  is no uniform measure on the unbounded hyperbolic space and proposes
  I_i(t) = −log P₀(C_i(t)) with a chosen P₀.

**What transfers, and what does not?** Transfers: that an angular constraint
of fixed aperture is exponentially selective in D, and that apertures should
be calibrated by mass under a stated reference, not by angle. Does not
transfer: the specific thresholds κ ∼ √D or κ ∼ D, which are for a tilt of
the whole population about the origin; and anything about the radial
ordering that encodes entailment.

## Verdict

The premise supports the conclusion for the angular component of cone
membership at the apex, under a stated reference measure; it does not
support it as a statement about hyperbolic entailment regions as such.
Proposed.
