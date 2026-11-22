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
<!-- inactive-ok-file: THEORY-tmpdfeto NOTE-tmpcjw5n — Proposed or Skimmed; the reading of the long paper, 2026-11-22 -->

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

## Note of 2026-11-22: Toner and Tu (1998), read

The long paper (LIT-2970, read in NOTE-tmpcjw5n; the reading is
THEORY-tmpdfeto) **keeps the conclusion and changes the argument.** Its
d = 2 exponents are again z = 6/5, ζ = 3/5, χ = −1/5, "exact and universal
for all flocks with the simple symmetries we discussed" (eq. 1.20, p. 10),
and the 1995 results are "sound" in d = 2 (p. 11). But the two unproved
steps this reading names, the cubic vertex staying irrelevant and z < 2
"on physical grounds", are the 1995 letter's; the word "cubic" does not
occur in the 1998 text. The 1998 argument (§V.C, pp. 46–50) rests instead
on:

- **every relevant vertex ∝ q⊥** in d = 2 (the longitudinal–transverse
  cross terms dropped as irrelevant because their frequency peaks do not
  overlap, the longitudinal–longitudinal term a total derivative), so ∆,
  D∥ and Dρ are not renormalized (eqs. 5.74–5.75);
- **pseudo-Galilean invariance**: at λ₁ = λρ the equations have "an exact
  symmetry which we call pseudo-Galilean invariance" (eqs. 5.76–5.77), so
  λ₁ is not renormalized there;
- **mass conservation**, exact, which with the above gives χ = 1 − z at a
  "type II" fixed point (eq. 5.79);
- **a flow to that fixed point** for all flocks, which the authors do not
  prove: "We consider it highly probable that this is, in fact, the case"
  (p. 48); then "So all models in d = 2 must have the canonical exponents"
  (p. 50).

The reader's own observation, not the paper's: eq. (5.8) gives
γₙ = n + (1 − n)d/2, which is 1 for every n in d = 2, so every pressure
term σₙ(δρ)ⁿ is relevant there by power counting (checked: n + (1 − n) =
1). They are ⊥ gradients, so the non-renormalization of ∆ and D∥
survives, but the type I/II analysis treats σ₂ alone.

So the `promote_when` stands and is not met: the 1998 argument avoids the
cubic vertex but has its own unproved step, a flow called "highly
probable", and it is an argument, not the controlled calculation or
finite-size scaling the condition asks for. THEORY-tmpdfeto holds the
long paper's account; the exactness stays this entry's question. No
status change.
