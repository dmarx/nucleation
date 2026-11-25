---
number: 1079
status: Proposed
formerly:
- CLAIM-tmpdhfpb
title: In the linear tangent–transverse model with a coupling C x∥ in the transverse
  equation, the deviation from the defining relations is at most ‖C‖X/κ + ‖B⊥‖‖u‖₂/√(2κ),
  for κ the least restoring rate and X the largest tangential excursion, so strong
  stabilization leaves tangential adaptation possible only where the demanded move
  is actuated and affordable and the restoring rate grows with the excursion it
  must carry
version: 1
role: thesis
warrant: demonstrated
defeated_if: An error in the derivation; or a system of this form, with the symmetric
  part of K⊥ at least κ and the transverse deviation starting at zero, whose deviation
  exceeds the bound.
tags:
- control-theory
- mathematics
- society-and-governance
date: '2026-11-23'
line:
- realizability
- formal-apparatus
rests_on:
- CLAIM-589
- CLAIM-345
summary: 'A gap fill: a gap of the manuscript governance-of-possibility, §5.3 (GB1),
  the two conditions the tangent/transverse argument for "strong organizational
  stabilization can enable extensive adaptation" needs and does not state: decoupling,
  or a restoring rate that grows with the excursion, and actuation in [CLAIM-589](CLAIM-589.md)''s
  sense. Checked by simulation with python3 -I. The wording is the assistant''s
  (Claude, in this session); adopting it is the owner''s call.'
---

# CLAIM-1079: In the linear tangent–transverse model with a coupling C x∥ in the transverse equation, the deviation from the defining relations is at most ‖C‖X/κ + ‖B⊥‖‖u‖₂/√(2κ), for κ the least restoring rate and X the largest tangential excursion, so strong stabilization leaves tangential adaptation possible only where the demanded move is actuated and affordable and the restoring rate grows with the excursion it must carry

## The derivation

The manuscript's model, with a coupling added:

  ẋ⊥ = −K⊥x⊥ + C x∥ + B⊥u,  ẋ∥ = A∥x∥ + B∥u,  x⊥(0) = 0,

x⊥ the deviation from the defining relations M_θ, x∥ the motion along them.
Let κ > 0 be the least eigenvalue of the symmetric part (K⊥ + K⊥ᵀ)/2, so
‖e^{−K⊥t}‖ ≤ e^{−κt}. By variation of constants,

  x⊥(t) = ∫₀ᵗ e^{−K⊥(t−s)} (C x∥(s) + B⊥u(s)) ds,

so, with X = sup_{s≤t} ‖x∥(s)‖, U = sup ‖u‖ and ‖u‖₂ the input's energy
norm on [0, t] (Cauchy–Schwarz for the last form),

  ‖x⊥(t)‖ ≤ ‖C‖X/κ + ‖B⊥‖ · min(U/κ, ‖u‖₂/√(2κ)).

**The first term is tight.** For scalars with x∥ held at X and u = 0,
x⊥ → CX/K. So keeping the deviation below ε while carrying an excursion X
needs κ ≥ ‖C‖X/ε in the worst case: the restoring rate has to grow in
proportion to the excursion. With C = 0 and B⊥ = 0, the draft's
block-diagonal case, any κ > 0 keeps the relations exactly.

**The actuation condition.** K⊥ does not enter the tangential equation, so
stabilization neither helps nor hinders the tangential move itself. A
demanded displacement Δ along M_θ by H is possible only if
Δ − e^{A∥H}x∥(0) lies in the range of the Gramian
W_H = ∫₀^H e^{A∥s}B∥B∥ᵀe^{A∥ᵀs} ds (the actuated directions, [CLAIM-589](CLAIM-589.md)'s
second object), and affordable only if its least effort
E* = (Δ − e^{A∥H}x∥(0))ᵀ W_H^† (Δ − e^{A∥H}x∥(0)) ([CLAIM-345](CLAIM-345.md)'s form) is
within budget (its third). The input that achieves it adds at most
‖B⊥‖√(E*/(2κ)) of deviation. So strong transverse stabilization leaves
tangential adaptation possible when:

1. the move is actuated (Δ − e^{A∥H}x∥(0) in the range of W_H);
2. it is affordable (E* within budget);
3. ‖C‖X/κ + ‖B⊥‖√(E*/(2κ)) ≤ ε, X the excursion along the move.

Conditions 1 and 2 do not depend on K⊥. Large κ meets condition 3, at a
rate in proportion to X when C ≠ 0. Condition 3 is sufficient, not
necessary, in more than one dimension; the proportional growth is shown
necessary only in the scalar case.

## The check

With python3 -I: 300 random systems (dimensions 1 to 3, K⊥ positive
definite plus a random skew part, Euler steps of 10⁻³ over t = 5,
sinusoidal inputs). The largest ratio of ‖x⊥(t)‖ to the bound over all
times and systems was 0.953 for the sup form and 0.939 for the energy
form, never above 1. The scalar case with C = 2, X = 3, K = 4 settles at
1.5 = CX/K.

## What it does not say

- Nothing where the restoring rate varies along M_θ, a nonlinear K⊥(x∥);
  there κ is the least rate along the path, and the bound needs it.
- Nothing where the tangential equation has a term in x⊥.
- Nothing where the demand needs θ itself changed, where stabilization of
  M_θ is the obstacle (the manuscript's third condition).
- Not that any organization has this linear structure.

## Gap filled

A gap of the manuscript governance-of-possibility, §5.3 (GB1), whose last
paragraph describes this fill: "a bound on the transverse deviation under
tangential motion in terms of ‖C‖, ‖B⊥‖, the input and K⊥, together with
the actuation condition stated with [CLAIM-589](CLAIM-589.md)'s three objects".
