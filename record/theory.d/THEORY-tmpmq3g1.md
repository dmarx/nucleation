---
status: Active
title: 'A safe set that a nominal barrier-function controller keeps invariant can be left under an arbitrarily small input disturbance, but if the barrier inequality holds with a disturbance penalty, ḣ ≥ −α(h) − ι(‖d‖), the state stays in a larger set {h + γ(‖d‖∞) ≥ 0} with γ class-K, and adding a damping term along the barrier''s input direction to any barrier controller gives this with an enlargement of ‖d‖²/(4ε) in units of h'
version: 1
tags:
- control-theory
- mathematics
- complex-systems
date: '2026-10-31'
source:
- LIT-tmpody6k
summary: >-
  Kolathaya and Ames (2019), [LIT-tmpody6k](../literature.d/LIT-tmpody6k.md), Theorems 1–2 and Examples 1–2,
  read in [NOTE-tmpjhivv](../notes.d/NOTE-tmpjhivv.md). Short proofs, checked by hand, and both
  examples checked by simulation. Active. Matched input disturbances only,
  local, and the enlargement is in barrier units and quadratic in the
  universal construction, not proportional to the disturbance.
---

# THEORY-tmpmq3g1: A safe set that a nominal barrier-function controller keeps invariant can be left under an arbitrarily small input disturbance, but if the barrier inequality holds with a disturbance penalty, ḣ ≥ −α(h) − ι(‖d‖), the state stays in a larger set {h + γ(‖d‖∞) ≥ 0} with γ class-K, and adding a damping term along the barrier's input direction to any barrier controller gives this with an enlargement of ‖d‖²/(4ε) in units of h

## Source

Kolathaya and Ames (2019), [LIT-tmpody6k](../literature.d/LIT-tmpody6k.md), §§III–V, pp. 2–4 of arXiv
1803.03035v3; read in [NOTE-tmpjhivv](../notes.d/NOTE-tmpjhivv.md).

## What was actually shown

**Fragility of the nominal guarantee.** In Example 1, ẋ = −x + x²u with
safe set x ≤ 2, the controller u = 0 is safeguarding: ḣ = x ≥ −h. With
u = 0 + d and d = 1 from x = 2, the state escapes to infinity (in
simulation, past 10³ by t ≈ 0.69). In Example 2 the standard CBF quadratic
program fails similarly at d = 10.

**Theorem 1.** For ẋ = f(x) + g(x)(k(x) + d(t)), if
L_f̄ h + L_g h µ ≥ −α(h) − ι(|µ|) for all |µ| ≤ d̄ on a domain D, then
C_d = {h + γ(‖d‖∞) ≥ 0} with γ = β⁻¹∘ι, β(r) = −α(−r), is forward
invariant. On the boundary of C_d, h = −γ and ḣ ≥ β(γ) − ι = 0.

**Theorem 2.** If sup_u[L_f h + L_g h u − εL_g h L_g hᵀ] ≥ −α(h), the
damping term absorbs the disturbance: ε|L_g h|² − |L_g h|‖d‖ ≥
−‖d‖²/(4ε). So ι(r) = r²/(4ε), and for α(h) = λh,
C_d = {h + ‖d‖²/(4ελ) ≥ 0}. Larger ε, smaller enlargement.

**Checked.** The completing-the-square inequality over a grid; Example 1
with k = −x²: the state stays at x ≤ 2 for d ≤ 4 and reaches 2.36 at
d = 6, inside x ≤ 2 + d²/4 = 11. The bound is conservative.

## What this does not say

- **That the enlargement is proportional to the disturbance.** It is a
  class-K function, quadratic in the construction.
- **Anything about disturbances outside the input channel**, or
  unbounded ones.
- **Global guarantees.** C_d must stay inside the domain where the
  barrier inequality holds, which limits d̄.
- **That the original set is kept.** ISSf is a weaker guarantee than
  robust invariance of C: it trades staying in C for leaving it by a
  bounded amount. Where a certificate shows C itself invariant against
  the disturbance (inward margin larger than the disturbance), that is
  robust invariance, the viability notion of [THEORY-134](THEORY-134.md), not ISSf.
