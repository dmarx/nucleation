---
number: 1429
status: Proposed
formerly:
- THEORY-tmpwa350
promote_when: >-
  The definition of a critical transition and the classification of the
  four bifurcations, with recovery exponents ½ for the fold and 1 for the
  others, are confirmed by checking the paper's propositions (2.5–2.8 and
  2.10) and their proofs, or against an independent restatement such as
  Kuehn's companion paper (arXiv 1101.2908) or his Multiple Time Scale
  Dynamics.
title: 'Kuehn holds that a critical transition is the point where a slowly drifting system leaves an attracting, normally hyperbolic slow manifold for a fast jump, that fold, transcritical and subcritical Hopf and pitchfork bifurcations are such points while supercritical ones are not, and that the slowing down before them scales with the distance to the bifurcation with exponent ½ for the fold and 1 for the others'
version: 1
tags:
- complex-systems
- mathematics
- probabilistic-modeling
date: '2026-11-04'
source:
- LIT-2048
summary: >-
  Kuehn (2011), [LIT-2048](../literature.d/LIT-2048.md), read in [NOTE-1598](../notes.d/NOTE-1598.md) from the arXiv v2.
  Proposed: the propositions' proofs are short normal-form computations
  that were read but not redone here. It is about one slow variable and
  one-dimensional (planar for Hopf) fast normal forms; it does not say
  when the jump comes, which drift delays and noise can advance, nor that
  observed indicators reliably reveal the exponent.
---

# THEORY-1429: Kuehn holds that a critical transition is the point where a slowly drifting system leaves an attracting, normally hyperbolic slow manifold for a fast jump, that fold, transcritical and subcritical Hopf and pitchfork bifurcations are such points while supercritical ones are not, and that the slowing down before them scales with the distance to the bifurcation with exponent ½ for the fold and 1 for the others

## Source

Kuehn, "A mathematical framework for critical transitions" (Physica D
2011), [LIT-2048](../literature.d/LIT-2048.md); read in [NOTE-1598](../notes.d/NOTE-1598.md).

## What was actually shown

- **Definition (Def. 2.4).** "We say that p is a critical transition if
  there is a candidate" γ₀ whose segment before p is an attracting normally
  hyperbolic part of the critical manifold, with p a point where normal
  hyperbolicity is lost and the candidate switches to a fast segment.
- **Classification (Props. 2.5–2.8).** "Then the fold bifurcation is also
  a critical transition."; Hopf and pitchfork are critical when
  subcritical, not when supercritical ("If it is supercritical (l1 < 0)
  then" the transition is not critical); "The transcritical bifurcation is
  a critical transition."
- **Recovery exponent (Def. 2.9, Prop. 2.10).** If the leading Lyapunov
  exponent on the attracting sheet is O(y^α), "then we suggest to call α
  the recovery exponent."; α = ½ for the fold and 1 for Hopf, pitchfork and
  transcritical, from the normal form on the centre manifold.

## What this does not say

- When the jump happens. With slow drift it is delayed past the fold by
  O(ε^{2/3}) (Theorem 3.2); with noise large against √ε it comes before
  the fold (Theorem 6.1).
- That rising variance or autocorrelation in data reveals the exponent or
  the type; the paper shows ways both mislead (§§5, 8, 9).
- Anything for several slow variables, global bifurcations or chaos, which
  §10 leaves open.
