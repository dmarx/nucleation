---
number: 115
status: Active
formerly:
- CASE-tmpuc54q
title: 'Two incompatible quadratic demands on one shared parameter, L₁ = (θ − 1)² and L₂ = (θ + 1)², frustrated at θ = 0 for every update budget, and the split of θ into task-routed θ_A and θ_B that makes both satisfiable'
version: 1
standing: fictional
kind: construction
tags:
- loss-landscapes
- individuation
- mathematics
date: '2026-10-18'
line: distributed-agency
supports:
- CLAIM-351
- CLAIM-365
- CLAIM-361
illustrates:
- CLAIM-360
summary: >-
  A33 §2 and §5, A35 §3.4 and A38 §4 of the exchange of 2026-10-17. Two
  demands on one scalar parameter: at θ = 0 the equal-weight gradient
  vanishes while each loss is 1, no update lowers both, and the local
  residual is Φ_r = ε for every budget r. A38 splits θ into θ_A and θ_B
  with the task context routed, and both demands are met at (1, −1). Used
  for the zero aggregate gradient, the residual, relief judged on the
  original demands, and differentiation. A38's caveat is kept: the split
  is "a division of functional jurisdiction", and it "does not
  automatically mean that two new autonomous individuals have formed".
  Fictional by construction.
---

# CASE-115: Two incompatible quadratic demands on one shared parameter, L₁ = (θ − 1)² and L₂ = (θ + 1)², frustrated at θ = 0 for every update budget, and the split of θ into task-routed θ_A and θ_B that makes both satisfiable

## The construction

**Before.** One scalar parameter θ, two demands with losses
L₁(θ) = (θ − 1)² and L₂(θ) = (θ + 1)² (A33 §2; A38 §4 writes them L_A,
L_B). At θ = 0:

- g₁ = −2, g₂ = 2. Any d ≠ 0 lowers one loss to first order and raises the
  other.
- With weights ½, ½ the aggregate gradient is 0, and the aggregate
  ½L₁ + ½L₂ = θ² + 1 is at its global minimum, while L₁ = L₂ = 1 (A33 §5).
- Globally, L₁ + L₂ = 2θ² + 2 ≥ 2, so no θ makes both losses less than 1.
  For any threshold τ < 1 the acceptance sets {L₁ ≤ τ} = [1 − √τ, 1 + √τ]
  and {L₂ ≤ τ} = [−1 − √τ, −1 + √τ] are disjoint: the compatibility
  complex of the two demands is {∅, {1}, {2}}.
- For required local improvements ε₁ = ε₂ = ε, the residual is
  Φ_r = min_{|d|≤r} max(ε − 2d, ε + 2d) = ε, attained at d = 0, for every
  r ≥ 0. The dual multiplier λ = (½, ½) gives λ₁g₁ + λ₂g₂ = 0 and the
  same value (A35 §3.4).

**After.** A38 §4: "Now allow the organization to differentiate into two
context-sensitive processes", θ_A and θ_B, with the task context available
for routing, so L₁ depends on θ_A and L₂ on θ_B. Then (θ_A, θ_B) = (1, −1)
meets both demands, and the complex is all of {∅, {1}, {2}, {1, 2}}, a
strict enlargement for the same declared demands. Locally at (0, 0), with
g₁ = (−2, 0), g₂ = (0, 2) and the Euclidean norm, the residual is
Φ_r = ε − √2·r (at λ = (½, ½), attained by d = (r, −r)/√2), so a budget
r ≥ ε/√2 meets both: what was structural becomes at worst
capacity-limited. Checked numerically.

A38: "The important change isn't just more parameters. It's the
emergence of a division of functional jurisdiction."

## What it can show

1. **A zero aggregate gradient with frustrated demands** ([CLAIM-351](../claims.d/CLAIM-351.md)).
2. **Structural frustration that no budget relieves**, and its dual
   certificate ([CLAIM-365](../claims.d/CLAIM-365.md), [CLAIM-357](../claims.d/CLAIM-357.md)).
3. **Relief as enlargement for fixed demands** ([CLAIM-347](../claims.d/CLAIM-347.md)): the
   demands before and after are the same two, with the same acceptance
   sets, so the comparison is [CLAIM-361](../claims.d/CLAIM-361.md)'s honest case, with a
   correspondence that is the identity.
4. **Differentiation as a source of relief.** In the terms of
   [CLAIM-360](../claims.d/CLAIM-360.md) the split enlarges the realizable function class, since
   the routed system computes a function of the task context that the
   shared parameter cannot. It is an illustration of that effect, not
   evidence about deep networks.

## What it cannot show

- **That anything individuated.** A38: "It does not automatically mean
  that two new autonomous individuals have formed." Whether θ_A and θ_B
  are subsystems of one more differentiated organization or new
  individuals is the individuation question, and nothing here bears on it.
- **That the split is endogenous.** The construction stipulates it.
  Nothing in it shows a learning organization reaching it, maintaining it,
  or governing it: A38's caption, "This is not, by itself, a model of
  endogenous self-maintenance."
- **That more parameters relieve frustration in general.** The split works
  because the context is routed. Without routing, a second parameter both
  demands must pass through relieves nothing. A38: "Not every form improves
  performance. Some merely partition the problem, reproduce conflict
  elsewhere, or restrict information flow."
- Anything about real networks. Fictional by construction.
