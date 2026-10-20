---
number: 733
status: Active
formerly:
- THEORY-tmp7brn5
title: 'For a stable linear Gaussian VAR(p), a linear coarse-graining is exactly dynamically independent iff its row space is invariant under the transpose of every lag matrix, so for p ≥ 2 almost no parameter set has one at any scale, while for p = 1 they are the transpose''s invariant subspaces, which exist on open sets but not generically at every scale'
version: 1
history:
- version: 1
  date: '2026-10-19'
  note: >-
    Split from THEORY-257 and filed Active at the owner's direction,
    carrying out the promotion audit's decision
    (record/promotion-audit/decisions/THEORY-257.yaml, batch 012, ADR-047).
    LIT-979's criterion (3.26) is re-derived below in both directions. Its
    genericity statement was a count of equations against unknowns
    (NOTE-791 C4, "strong as a counting argument"). It is replaced here by
    a proof that the exceptional set is Lebesgue-null for p ≥ 2. The
    count's p = 1 half ("solutions at every scale, generically") fails
    over the reals, and the counterexample is given. Under ADR-047 v2 (the
    owner's rule of 2026-10-19), a step-by-step re-derivation meets the
    condition. THEORY-257 keeps the interpretive reading and the
    multimodality, and extends this one.
tags:
- complex-systems
- information-theory
- mathematics
date: '2026-10-19'
source:
- LIT-979
summary: >-
  Barnett and Seth (2023), [LIT-979](../literature.d/LIT-979.md), read in [NOTE-791](../notes.d/NOTE-791.md): the VAR form (3.26)
  of exact dynamical independence, with the genericity count of §3.3 made
  a proof for VAR order p ≥ 2 and corrected for p = 1. Linear
  coarse-grainings Y = LX of a stable VAR with non-degenerate Gaussian
  innovations only. It says nothing about near-independence, about the
  multimodality of the dynamical-dependence cost, or about nonlinear maps.
extended_by:
- THEORY-257
supports:
- CLAIM-388
- CLAIM-389
- CLAIM-390
- CLAIM-394
- CLAIM-398
---
<!-- inactive-ok-file: THEORY-257 — Proposed; the account this was split from and that extends it, cited as open -->

# THEORY-733: For a stable linear Gaussian VAR(p), a linear coarse-graining is exactly dynamically independent iff its row space is invariant under the transpose of every lag matrix, so for p ≥ 2 almost no parameter set has one at any scale, while for p = 1 they are the transpose's invariant subspaces, which exist on open sets but not generically at every scale

## Source

Barnett and Seth (2023), *Physical Review E* 108, 014304, [LIT-979](../literature.d/LIT-979.md), read in
full in [NOTE-791](../notes.d/NOTE-791.md) (arXiv:2106.06511v2): the definition of dynamical
independence (2.3)–(2.6), the VAR criterion (3.26) and the genericity
remark of §3.3. The criterion is the paper's. The derivation, the measure
argument and the p = 1 counterexample below are the record's.

## What was actually shown

Model: X_t = Σ_{k=1}^p A_k X_{t−k} + ε_t in ℝⁿ, stable, with ε_t i.i.d.
N(0, Σ), Σ ≻ 0. A coarse-graining Y = LX, with L an m × n matrix of full
row rank, 0 < m < n, is dynamically independent when the transfer entropy
T(X → Y) = I(Y_t : X⁻ | Y⁻) vanishes. Let W be L's row space.

**Sufficiency.** If L A_k = B_k L for every k, equivalently W·A_k ⊆ W,
then Y_t − Σ_k B_k Y_{t−k} = Lε_t, which is independent of the whole past
of X. So T(X → Y) = 0.

**Necessity.** With Gaussian laws, T(X → Y) = 0 means
E[Y_t | X⁻] = E[Y_t | Y⁻]. Write X_s = Σ_{j≥0} Ψ_j ε_{s−j}, with Ψ_0 = I
and Ψ_j = Σ_{k=1}^{min(j,p)} A_k Ψ_{j−k}. Then
E[Y_t | X⁻] = Σ_{j≥1} LΨ_j ε_{t−j}. In an element Z of the closed span of
{Y_s : s < t}, the coefficient of ε_{t−j} is Cov(Z, ε_{t−j})Σ⁻¹. For a
finite combination Σ_s C_s Y_{t−s} this coefficient is
Σ_{s=1}^{j} C_s LΨ_{j−s}. For each j ≤ p these tuples form a
finite-dimensional, hence closed, set, so limits keep the form. So
LΨ_j = Σ_{s=1}^{j} C_s LΨ_{j−s} for j = 1, …, p. At j = 1 this is
L A_1 = C_1 L. If L A_i = B_i L for all i < j, then LΨ_i = D_i L for i < j,
and the j-th equation becomes L A_j + (something)·L = (something)·L. So
L A_j = E_j L. By induction, the condition holds for every lag. This is
(3.26), L A_k Mᵀ = 0 for k = 1, …, p, with the rows of M spanning ker L.

**p ≥ 2: almost never.** For a fixed W in the Grassmannian Gr(m, n), the
map A ↦ L A Mᵀ is onto ℝ^{m×(n−m)}. So each lag's condition is m(n − m)
independent linear equations, and all p together are p·m(n − m). The set
of pairs ((A_k), W) meeting them is a vector bundle over Gr(m, n) of total
dimension pn² − (p − 1)m(n − m). That is less than pn² when p ≥ 2. Its
projection to the parameter space ℝ^{pn²} is smooth, so its image is
Lebesgue-null. A finite union over m keeps it null, and stability is an
open condition. So almost every stable VAR(p) with p ≥ 2 has no exactly
dynamically independent linear coarse-graining at any scale.

**p = 1: open sets, not every scale.** Exact independence at scale m holds
iff W is an m-dimensional subspace invariant under Aᵀ. Such subspaces exist
for all m on an open set, for example when every eigenvalue is real and
distinct. But A = ½·[[0, −1], [1, 0]] is stable with eigenvalues ±i/2.
Every matrix near it has non-real eigenvalues, and so no real
one-dimensional invariant subspace. So on an open set of stable VAR(1)
models in ℝ², no scale-1 coarse-graining is exactly independent. In
general, a scale m fails whenever Aᵀ has no real invariant subspace of
dimension m.

What could have failed: a generic VAR(p) could have had exact solutions
from nonlinear coincidences between lags. It cannot, because the
conditions are linear in the parameters for each fixed subspace.

## What this does not say

- **Not that near-independent variables are rare.** It concerns exact
  zeros. The paper's "emergence portrait" is built from near-independent
  optima, which this result leaves open.
- **Not about nonlinear coarse-grainings or non-Gaussian noise.** The
  criterion uses linear maps and Gaussian conditional laws.
- **Not about state-space models with r > 1.** The paper's (3.25) and its
  stated ranges of m were not re-derived.
- **Not that the dynamics fix the variables.** That reading belongs to
  [THEORY-257](THEORY-257.md) and stays Proposed.
