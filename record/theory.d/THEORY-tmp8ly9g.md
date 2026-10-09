---
status: Proposed
promote_when: >-
  A published proof or statement of the continuity (or Lipschitz bound) of
  the contextual fraction in the empirical model, read and checked. Or an
  independent check of the derivation below against the linear programme
  of LIT-265, including that strong duality holds and that the dual
  minimum is attained at a vertex for every empirical model. Numerical
  agreement on more examples does not count.
title: 'Within a fixed measurement scenario, the contextual fraction is a convex, piecewise-linear and Lipschitz-continuous function of the empirical model''s probability table'
version: 1
tags:
- contextuality
- mathematics
date: '2026-10-09'
source:
- LIT-265
summary: >-
  From Abramsky, Barbosa & Mansfield (2017), LIT-265: the non-contextual
  fraction is the value of a linear programme whose constraint vector is
  the empirical model (Eq. 3), and convexity of CF under mixing is their
  Theorem 2. Piecewise linearity and the Lipschitz bound are the reader's
  derivation from strong duality, not stated in the paper. The Lipschitz
  constant depends on the scenario and is not bounded here. Nothing here
  applies to signalling data, where CF is undefined.
---

# THEORY-tmp8ly9g: Within a fixed measurement scenario, the contextual fraction is a convex, piecewise-linear and Lipschitz-continuous function of the empirical model's probability table

## Source

Abramsky, Barbosa & Mansfield (2017), LIT-265, Eqs. (3)–(4), Theorem 1 and
its supplemental proof, and Theorem 2 (mixing) with its supplemental proof,
as read in NOTE-236. The continuity statement is the reader's derivation,
set out below.

## What was actually shown

In a scenario ⟨X, M, O⟩ with incidence matrix M, an empirical model e is a
vector v_e of context-wise probabilities whose marginals agree on overlaps.
The paper defines NCF(e) = max {1·b : Mb ≤ v_e, b ≥ 0} and CF = 1 − NCF.
It proves that strong duality holds, with dual min {y·v_e : Mᵀy ≥ 1,
y ≥ 0}. Theorem 2 proves NCF(λe + (1 − λ)e′) ≥ λNCF(e) + (1 − λ)NCF(e′),
so CF is convex along mixtures.

The derivation (the reader's): the dual feasible set P = {y ≥ 0, Mᵀy ≥ 1}
is a nonempty polyhedron inside the nonnegative orthant, so it has
finitely many vertices y₁, …, y_K and its recession directions are
nonnegative. Since v_e ≥ 0, the objective y·v_e cannot decrease along a
recession direction, so the minimum is attained at a vertex:
NCF(e) = min_k y_k·v_e. A minimum of finitely many linear functions is
concave and piecewise linear, and
|CF(e) − CF(e′)| ≤ (max_k ‖y_k‖₁) · ‖v_e − v_e′‖_∞. The constant depends
only on the scenario.

A numerical check on the CHSH (2,2,2) scenario: along the line from
uniform noise to the PR box, CF is 0 up to weight ½ and 2t − 1 after. It
is continuous with a kink, as the derivation predicts. The Bell–CHSH table
of the paper's Table I gives CF = 1/4, its normalised CHSH violation
(Theorem 1). The largest ‖y*‖₁ seen over 300 random mixtures was 8. That
is a sample, not the constant.

## What this does not say

- **Not that small changes in the underlying states or chains give small
  changes in CF.** The bound is in the empirical table. A drift result
  must first bound the change in every context's distribution, and then
  pays the scenario's constant, which can be large.
- **Not anything across scenarios.** The bound holds for a fixed
  scenario. CF is comparable across scenarios as a number in [0, 1]
  (the paper's point), but a map between scenarios is a separate
  operation. Translations of measurements and coarse-grainings cannot
  raise it (Theorem 2), while other maps may.
- **Not for signalling data.** CF requires compatible marginals. An
  empirical table with context-dependent marginals has no CF, and
  Contextuality-by-Default's measure (LIT-777) is a different quantity.
- **Not that the strongly contextual / noncontextual decomposition varies
  continuously.** The decomposition need not be unique (the paper's
  Table II), even though its weight is continuous.
