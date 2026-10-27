---
number: 1095
status: Proposed
formerly:
- THEORY-tmpzaxy0
promote_when: >-
  A result that fixes the sign of χ in d = 2 for this model without either
  of the paper's unproved steps (that the cubic vertex |v⊥|²∂∥v⊥ stays
  irrelevant down to d = 2, or that z < 2 "on physical grounds"): a
  controlled renormalization-group or non-perturbative argument, or
  finite-size scaling of the transverse velocity fluctuations ⟨|v⊥|²⟩ in
  simulations of the Vicsek class, over a range of L⊥ and L∥, showing them
  bounded as the flock grows. A nonzero mean velocity at one system size
  does not settle it, and neither do measured exponents near z = 6/5,
  ζ = 3/5, χ = −1/5, since the order does not depend on those values being
  exact.
title: 'In Toner and Tu''s hydrodynamic model of a flock, true long-range orientational order survives in two dimensions, where the Mermin–Wagner theorem forbids it at equilibrium and the model''s own linearized theory loses it, because the convective coupling of the velocity field to its own transport, relevant below four dimensions, keeps the transverse velocity fluctuations bounded; the authors'' heuristic is that motion keeps changing each member''s neighbours, so originally distant members come to interact'
version: 1
tags:
- complex-systems
- natural-sciences
date: '2026-10-27'
source:
- LIT-1670
summary: >-
  Toner and Tu (1995), [LIT-1670](../literature.d/LIT-1670.md), read in [NOTE-1228](../notes.d/NOTE-1228.md) from the arXiv
  preprint. The linear theory's loss of order in d ≤ 2 and the relevance of
  the convective nonlinearity below d = 4 are calculations. The survival of
  order in d = 2 follows from χ = −1/5 < 0, which is exact only if a cubic
  vertex stays irrelevant ("we strongly suspect"), or from χ = (z − d)/3
  with z < 2, which is expected "on physical grounds". The change-of-
  neighbours mechanism is a heuristic. Proposed for those two steps.
---
<!-- inactive-ok-file: CLAIM-280 — Proposed; the turnover claim this mechanism bears on, cited as open -->

# THEORY-1095: In Toner and Tu's hydrodynamic model of a flock, true long-range orientational order survives in two dimensions, where the Mermin–Wagner theorem forbids it at equilibrium and the model's own linearized theory loses it, because the convective coupling of the velocity field to its own transport, relevant below four dimensions, keeps the transverse velocity fluctuations bounded; the authors' heuristic is that motion keeps changing each member's neighbours, so originally distant members come to interact

## Source

Toner and Tu (1995), [LIT-1670](../literature.d/LIT-1670.md), pp. 2–9 of the arXiv preprint
adap-org/9506001; read in [NOTE-1228](../notes.d/NOTE-1228.md).

## What was actually shown

**The puzzle.** Vicsek et al.'s rule reduces, at zero speed, to Monte Carlo
dynamics of the 2D XY model, which has no long-range order at T > 0; yet
their simulations find an ordered phase. "In light of the Mermin-Wagner
theorem for equilibrium systems, its existence must depend on fundamentally
dynamical, non-equilibrium aspects of the model" (p. 2).

**What could have come out otherwise, and did not.** The linearized theory
of eqs. (1, 2) gives χ = 1 − d/2, so "v⊥ fluctuations grow without bound
(like L^χ) as L → ∞ for d ≤ 2" (p. 4): without the nonlinearity, the flock
is the equilibrium case. Power counting then shows the convective vertex
λ(v⊥ · ∇)v⊥ and the σ₂ pressure term relevant below d = 4 (p. 5).

**The exponents.** A "Galilean invariance" protects λ, and in d = 2 the
noise strength Δ and D∥ are also unrenormalized, which gives z = 6/5,
ζ = 3/5, χ = −1/5 (eqs. 9, 10; p. 7). Then ⟨|v⊥|²⟩ = constant −
L⊥^{−2/5} g(L∥/L⊥^{3/5}) (eq. 16, p. 8), which "goes to a finite constant
as L → ∞": "long ranged order is stable in this model in d = 2".

**The two unproved steps.** The exactness needs the cubic vertex
|v⊥|²∂∥v⊥, with linear eigenvalue 3 − d, to stay irrelevant to d = 2; the
authors argue it from the φ⁶ term in φ⁴ theory and "strongly suspect" it
(p. 8). If it fails, rotational invariance still gives χ = (z − d)/3, and
χ < 0 in d = 2 if z < 2, which they "expect on physical grounds", since
"the motion of the "birds" enhances the mixing" (p. 9).

**The mechanism, as a heuristic.** In Lagrangian coordinates the convective
term drops out, "However, at different times, the "neighbors" of one
particular "bird" will be different depending on the velocity field itself.
Therefore, two originally distant "birds" can interact with each other at
some later time. It is exactly this time dependent variable ranged
interaction which stabilizes the ordered phase" (p. 3).

## What this does not say

- **That the exponents are exact.** That is conditional here, and is
  standardly reported to have been revised by Toner's later reanalysis (not
  held, not read).
- **That any finite flock is ordered.** Eq. (16) is about L → ∞; how large
  a flock must be for the statement to bite is not given.
- **That the order is the members' doing in any sense beyond the field
  equations.** The birds appear only through a conserved density and the
  coarse-grained velocity; the change-of-neighbours story is a gloss on the
  convective term, not a calculation about members ([CLAIM-280](../claims.d/CLAIM-280.md)).
- **That every flocking rule is in this class.** The universality claim is
  asserted, not derived from a microscopic rule.
- **Anything about the transition into order**, which is left open
  (pp. 9–10).
