---
status: Active
title: 'Whether functionally equivalent realizations are connected depends on which paths are admissible: for f = u₁v₁ + u₂v₂ with nonnegative weights, (1, 1, 0, 0) and (0, 0, 1, 1) are joined by a curve along which f stays 1 though the straight line between them falls to ½, and under any resource budget below √2 times the endpoints'' cost no path with f = 1 joins them'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the construction. It is not defeated by trained networks
  being connected under the resources they actually have: the claim is
  that connectedness is relative to an admissible path family, not that
  any architecture lacks it.
tags:
- loss-landscapes
- mathematics
date: '2026-10-31'
line:
- learned-structure
- formal-apparatus
bears_on:
- QUESTION-069
grounds:
- THEORY-114
- THEORY-741
summary: >-
  From the owner's remark at U17 of the exchange "Analyze nucleation
  concepts" (2026-10-31), that the reconstruction fibres "reminds me of
  loss landscape connected mode stuff (which might just be a consequence of
  high dimensional geometry? ... probably already discussed on the
  nucleation record)". It is: see below. A17 §9 gave the curve and A18 §7
  the budget for a tied-weight family; the general bound here is the
  reader's, rechecked. "Viable mode connectivity" is A18's name and is not
  filed as a term.
---
<!-- inactive-ok-file: QUESTION-069 THEORY-1172 THEORY-210 — Open or Proposed; the question this answers in part, the wide form of connectivity and the symmetry account, cited as context and not leaned on -->

# CLAIM-tmpxz1fa: Whether functionally equivalent realizations are connected depends on which paths are admissible: for f = u₁v₁ + u₂v₂ with nonnegative weights, (1, 1, 0, 0) and (0, 0, 1, 1) are joined by a curve along which f stays 1 though the straight line between them falls to ½, and under any resource budget below √2 times the endpoints' cost no path with f = 1 joins them

## The construction

Take a two-path network computing f = u₁v₁ + u₂v₂ with uᵢ, vᵢ ≥ 0, and the
two realizations a = (1, 1, 0, 0) and b = (0, 0, 1, 1), both with f = 1.

- **The straight line has a barrier.** At (1 − t)a + tb, f = (1 − t)² + t²,
  which is ½ at t = ½.
- **A curve has none.** (cos s, cos s, sin s, sin s) for s ∈ [0, π/2] keeps
  f = cos²s + sin²s = 1.
- **A budget removes every zero-loss path.** Let a realization's resource
  be R = ½ Σ (uᵢ + vᵢ), which is 1 at both endpoints. On f = 1 write
  p = u₂v₂, so u₁v₁ = 1 − p. By the AM–GM inequality,
  R ≥ √(u₁v₁) + √(u₂v₂) = √(1 − p) + √p. Any path from a to b moves p from
  0 to 1 and so passes p = ½, where R ≥ √2. Under any budget below √2, the
  set of budget-feasible realizations with f = 1 is disconnected between a
  and b.

So the zero-loss set is connected while the zero-loss set under a resource
bound is not. A17: "A low-path loss is not necessarily a viable transition
path."

## Against the record's readings

The owner's guess was right: the record holds the mode-connectivity
literature, and it bears on "just high-dimensional geometry?" both ways.
Continuous symmetries stretch minima into connected manifolds (THEORY-210),
and enough width gives piecewise-linear paths of minima (THEORY-741), which
is the geometric explanation. But at practical widths linear connectivity
emerges in training (THEORY-114), and connectivity at initialization needs
widths far past practice (THEORY-1172), which cuts against geometry alone.
QUESTION-069 asks whether connectedness belongs to the solutions or to the
path family searched. This construction answers one part: for a fixed
function and fixed endpoints, the answer changes with the path family
admitted, and a resource bound is one way to restrict it.

## What it does not say

- That trained networks are disconnected under realistic budgets.
- That parameter norm is the right resource. It is the simplest one to
  state; the point holds for any resource that grows when both paths are
  partly active.
