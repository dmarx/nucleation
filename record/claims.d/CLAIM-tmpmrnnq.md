---
status: Proposed
title: 'In the two-path construction where a resource budget below √2 disconnects two zero-loss realizations, the two lie on one orbit of the symmetry that swaps the network''s two paths, and for every budget from 1 to below √2 the budgeted zero-loss set is two path-connected pieces that the swap exchanges, so once that symmetry is quotiented the budgeted set is connected: the construction shows connectedness relative to the admitted paths in parameter space, not between solutions counted up to the architecture''s symmetries'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation: a budget B with 1 ≤ B < √2 at which the swap
  (u₁, v₁, u₂, v₂) ↦ (u₂, v₂, u₁, v₁) fails to preserve f or the resource
  R, or at which the set {f = 1, R ≤ B} has a piece that the swap does not
  map onto the other, or a piece that is not path-connected. Not defeated
  by a resource that the swap does not preserve, which the claim does not
  cover; nor by budgets of √2 or more, where the set is connected without
  any quotient; nor by anything about trained networks, of which it says
  nothing.
tags:
- loss-landscapes
- mathematics
date: '2026-11-10'
line:
- learned-structure
rests_on:
- CLAIM-524
bears_on:
- QUESTION-069
summary: >-
  An inference across two parts of the learned-structure line that no
  entry states, found in the synthesis review of the line on 2026-11-10.
  [CLAIM-524](CLAIM-524.md) answers part of [QUESTION-069](../questions.d/QUESTION-069.md): for a fixed function and fixed
  endpoints, connectedness changes with the path family admitted, and a
  budget below √2 disconnects (1, 1, 0, 0) from (0, 0, 1, 1). Those two
  endpoints are images of each other under swapping the two paths, a
  function-preserving symmetry of the kind [CLAIM-263](CLAIM-263.md) quotients, and so
  are the two budgeted pieces. Up to that symmetry the budgeted set is
  connected. So the construction bears on [QUESTION-069](../questions.d/QUESTION-069.md)'s path-family
  alternative only before quotienting, and leaves the reading that
  connectedness belongs to the solutions untouched for solutions counted
  up to symmetry. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---
<!-- inactive-ok-file: ADR-075 CLAIM-263 — Proposed; components, citations and the decisions this account follows, with their standing -->

# CLAIM-tmpmrnnq: In the two-path construction where a resource budget below √2 disconnects two zero-loss realizations, the two lie on one orbit of the symmetry that swaps the network's two paths, and for every budget from 1 to below √2 the budgeted zero-loss set is two path-connected pieces that the swap exchanges, so once that symmetry is quotiented the budgeted set is connected: the construction shows connectedness relative to the admitted paths in parameter space, not between solutions counted up to the architecture's symmetries

## The claim

[CLAIM-524](CLAIM-524.md)'s network computes f = u₁v₁ + u₂v₂ with nonnegative weights,
and its resource is R = ½ Σ (uᵢ + vᵢ). Let σ swap the two paths:
σ(u₁, v₁, u₂, v₂) = (u₂, v₂, u₁, v₁).

1. σ preserves f and R, so it is a function-preserving symmetry that
   also preserves the budget. It is a permutation of hidden units, one of
   the symmetries [CLAIM-263](CLAIM-263.md)'s first step quotients.
2. σ maps [CLAIM-524](CLAIM-524.md)'s endpoints a = (1, 1, 0, 0) and b = (0, 0, 1, 1) to
   each other.
3. For 1 ≤ B < √2, the set S_B = {f = 1, R ≤ B} is the union of two
   path-connected pieces, S₋ containing a and S₊ containing b, and
   σ(S₋) = S₊.
4. So S_B / σ is connected. Up to the swap, a and b are one solution, and
   the budget leaves it one connected set.

## The derivation

Write p = u₂v₂, so u₁v₁ = 1 − p on f = 1. [CLAIM-524](CLAIM-524.md)'s AM–GM step gives
R ≥ √(1 − p) + √p, with equality when u₁ = v₁ and u₂ = v₂.

- **Two pieces.** h(p) = √(1 − p) + √p rises from 1 at p = 0 to √2 at
  p = ½ and falls back to 1 at p = 1. For B < √2, R ≤ B forces
  h(p) ≤ B, so p lies in [0, p_B] or [1 − p_B, 1] for some p_B < ½.
  Call the two parts S₋ and S₊.
- **The swap exchanges them.** σ sends p to 1 − p and preserves R.
- **Each piece is path-connected.** Take a point of S₋. Move (u₁, v₁)
  along u₁v₁ = 1 − p, and (u₂, v₂) along u₂v₂ = p, to the balanced point
  (if p = 0, shrink the nonzero one of u₂, v₂ to 0). u + v falls
  monotonically along a hyperbola toward its balanced point, so R does
  not rise and the path stays in S_B. Then move along balanced points,
  where R = h(p), with p falling to 0: h falls on [0, ½], so the path
  stays in S_B, and it ends at a. Every point of S₋ is joined to a inside
  S₋.
- **B = 1** leaves only a and b, still exchanged by σ. For B < 1 the set is
  empty.

**Checked** by sampling in this session (not filed as a script): at B = 1.3,
of 200,000 points drawn on f = 1, the 22,994 with R < B had p below 0.136
or above 0.862, and the swap kept every one on f = 1 with R < B. The
monotone steps were checked on a grid.

## Relation to the record

- **[CLAIM-524](CLAIM-524.md)** is the premise: the construction and its √2 bound. Its
  reading of [QUESTION-069](../questions.d/QUESTION-069.md), that "for a fixed function and fixed endpoints,
  the answer changes with the path family admitted", stands as stated.
  This claim adds that its endpoints are not distinct solutions up to the
  architecture's symmetry, and that the disconnection is between symmetric
  copies.
- **[CLAIM-263](CLAIM-263.md)** supplies the quotient; this claim needs only the
  definition of its first step, not its Proposed reading of a residual
  barrier, and it does not rest on it.
- **[QUESTION-069](../questions.d/QUESTION-069.md)** asks whether connectedness belongs to the solutions or
  to the path family searched. Before this claim, [CLAIM-524](CLAIM-524.md) was the
  record's one construction for the path-family alternative. After it,
  that construction separates the two only for solutions not identified up
  to symmetry.

## Admission

A claim whose premise is a claim, tested by [ADR-075](../decisions.d/ADR-075.md)'s step 5.

- **Route: derivation.** The inference above is valid from [CLAIM-524](CLAIM-524.md)'s
  construction and the definition of the swap. It is not held: no entry
  names the swap, the orbit or the budgeted pieces' exchange (the
  learned-structure line's synthesis review of 2026-11-10 searched the
  record). It is not trivial in the sense of [ADR-075](../decisions.d/ADR-075.md): that a and b are
  swapped is one line, but that every budgeted piece is path-connected
  and exchanged needs the retraction above, and it changes what
  [CLAIM-524](CLAIM-524.md) is evidence of.
- **Free parameters.** None. The symmetry, the resource and the budgets
  are [CLAIM-524](CLAIM-524.md)'s or fixed above.
- **A realistic separating case** does not arise for a derivation. The
  nearest case against the claim's reach is a resource the swap does not
  preserve, such as different costs on the two paths; the claim excludes
  it in its defeater.

## What it does not say

- That trained networks are connected after alignment, under budgets or
  not. That is [QUESTION-317](../questions.d/QUESTION-317.md)'s.
- That path-family relativity never survives a quotient. A construction
  whose budget-separated realizations lie on different orbits would show
  it; the record holds none.
- That [CLAIM-263](CLAIM-263.md)'s step 2 is right.
