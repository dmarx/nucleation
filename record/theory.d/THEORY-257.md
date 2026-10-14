---
number: 257
status: Proposed
formerly:
- THEORY-tmpc7h4d
promote_when: >-
  An application to measured data from a system whose emergent variables
  are independently known, such as a mechanical system with conserved
  quantities or a neural recording with an established macrostate.
  Minimizing dynamical dependence must recover those variables at the
  expected scale, the remaining optima must be reported, and the
  generic-absence result for VAR order above 1 must hold in the fitted
  models. It is refuted by a system in which the variables of least
  dynamical dependence are not the ones its dynamics single out (for
  example, not built from its invariants), or by a proof that a generic
  stable VAR(p), p > 1, has exactly independent linear coarse-grainings on
  a set of positive measure. What cannot settle it: further toy models
  built from a planted causal graph, which the authors call privileged
  by construction.
title: "Dynamical independence, zero information flow from the microscopic history into a coarse-graining given its own history, fixes emergent macroscopic variables by the dynamics rather than by a chosen query, but generically none is exact and the optima are many"
version: 1
tags:
- complex-systems
- information-theory
- mathematics
date: '2026-10-14'
source:
- LIT-979
answers:
- QUESTION-065
summary: >-
  Barnett and Seth (2023), [LIT-979](../literature.d/LIT-979.md), read in [NOTE-791](../notes.d/NOTE-791.md): definition
  (2.6), transitivity (App. A), the causal-graph form (2.12), the
  state-space closed form (3.18) and the genericity count (3.25)–(3.26).
  The target is the coarse variable's own future, so no outside query is
  chosen. But the system/environment boundary, the scale and the class of
  maps are inputs, and the worked theory's candidates are linear
  subspaces, not partitions. The cost is multimodal, with every local
  optimum kept. The criterion is closure, not locality or informativeness
  about a far environment.
---
<!-- inactive-ok-file: THEORY-198 THEORY-205 CLAIM-157 CLAIM-167 — Proposed; the locality accounts on QUESTION-065 and the boundary claims this account bears on, open -->

# THEORY-257: Dynamical independence, zero information flow from the microscopic history into a coarse-graining given its own history, fixes emergent macroscopic variables by the dynamics rather than by a chosen query, but generically none is exact and the optima are many

## Source

Barnett and Seth (2023), *Physical Review E* 108, 014304, [LIT-979](../literature.d/LIT-979.md), read in
full in [NOTE-791](../notes.d/NOTE-791.md) (arXiv:2106.06511v2).

## What was actually shown

- **Definition (2.3)–(2.6).**
  - A coarse-graining Y = f(X) is dynamically independent of the
    microscopic system X, in the context of an environment E, iff
    T(X → Y | E) = I(Y_t : X_t⁻ | Y_t⁻, E_t⁻) ≡ 0.
  - That is, the micro history adds nothing to predicting Y beyond Y's
    own history.
  - The same transfer entropy, the dynamical dependence, measures the
    departure from independence.
- **Properties (proved).**
  - Invariance under reparametrization of source, target and conditioner
    (2.7).
  - Transitivity across nested coarse-grainings (2.10, App. A), giving a
    partial order across scales.
  - In suitable coordinates, independence holds iff the variable is a
    sub-graph of the conditional causal graph with no incoming transfer
    (2.12).
- **Linear systems (derived).**
  - For an innovations-form state-space model with Σ = I and orthonormal
    L, F(X → Y) = log|LVLᵀ| with V = CPCᵀ + I, P from a reduced DARE
    (3.17)–(3.18). There is also a spectral integral form (3.21).
  - Exact independence ⇔ LCA^kKMᵀ ≡ 0 for k < r (3.25). For a VAR(p) it
    is LA_kMᵀ ≡ 0 (3.26).
  - By counting equations against the m(n − m) Grassmannian parameters,
    exact solutions are generic at every scale for VAR(1) and absent for
    VAR(p > 1), except on a set of measure zero.
- **Search (simulation).**
  - Minimizing F over the Grassmannian is "in general multi-modal", and a
    (1+1) evolution strategy with restarts was used.
  - In a 9-variable VAR(7) built from three modules, the planted
    independent subspaces were found at scales 2 and 6, nested. Other
    runs ended in distinct local optima, some nearly orthogonal to the
    global one.
- **What could have failed.**
  - The transitivity proof and the closed form could have needed further
    conditions.
  - The search could have missed the planted subspaces or found spurious
    zeros. It found them at the expected scales only.

## What this does not say

- **It does not make the coarse-graining analyst-free.**
  - The system/environment boundary is "assume[d] … given".
  - The scale m is chosen, and the search is run at each m.
  - The admissible maps are chosen. In the worked theory they are linear
    subspaces mixing all units, not partitions of the units into groups.
  - What the dynamics fix is the target: the variable's own future rather
    than an outside query. The authors contrast this with abstractions
    "driven by the agenda of the observer".
- **It does not say the optimum is unique.** The authors keep every local
  optimum as part of an "emergence portrait". The planted example has
  one exact optimum per scale because it was built that way, "in effect,
  … a 'privileged' coordinate system".
- **It does not say emergent variables are common.** For generic linear
  models of order above 1 there is no exact one. The portrait then
  consists of near-independent optima, and "near" is set by a threshold
  or a significance test.
- **It does not say an independent variable predicts itself well.** A
  white-noise coordinate can be exactly independent (§5.2).
- **It says nothing about locality.** The criterion is closure against
  the rest of the system, not informativeness about a far environment
  across a buffer.

## Connections

- **[QUESTION-065](../questions.d/QUESTION-065.md): answers in part.**
  - *First part.* Yes, a target can be supplied by the system: here it is
    the coarse variable's own future. But it is not the locality-based
    target the question names. Boundary, scale and the class of maps
    remain the analyst's.
  - *Second part.* Under this criterion the winner at a scale is not
    unique in general: the cost is multimodal, and exact optima are
    generically absent.
- **[THEORY-198](THEORY-198.md) and [THEORY-205](THEORY-205.md).** Those select coarse variables by
  information about a far environment. This selects them by closure. On a
  local lattice the two could be compared directly, which is the
  divergence-or-match result [QUESTION-065](../questions.d/QUESTION-065.md) asks for. No paper held has
  made that comparison.
- **[CLAIM-157](../claims.d/CLAIM-157.md).** Near-decomposability asks for weak coupling across a
  block's edge both ways. Dynamical independence asks only for none
  coming in. A module that drives the rest and is not driven back is
  exactly independent. A driven module never is.
- **[CLAIM-167](../claims.d/CLAIM-167.md).** On this criterion a driver is a macro-variable of its
  own, and driver-plus-driven may form a larger nested one. That reading
  of one-way drive differs from treating the pair as a single system at
  one scale.
- **[CLAIM-152](../claims.d/CLAIM-152.md).** It is consistent with [CLAIM-152](../claims.d/CLAIM-152.md): this is still
  sufficiency for a target, fixed here as self-prediction. It does not
  refute it.
