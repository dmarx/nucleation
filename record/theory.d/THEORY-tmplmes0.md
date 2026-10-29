---
status: Active
title: 'In a Lotka–Volterra community with a symmetric interaction matrix, the growth-weighted biomass rᵀx strictly increases along every edge of the invasion graph, so the invasion graph has no cycles'
version: 1
history:
- version: 1
  date: '2026-10-29'
  note: >-
    Filed Active from NOTE-tmpwunhc, re-derived. Serván and Allesina
    assert that MacArthur's Lyapunov function makes their assembly graph
    acyclic in symmetric competitive Lotka–Volterra without writing out
    the step; the identity below supplies it, and extends it to Hofbauer
    and Schreiber's invasion graph (LIT-1233), which they do not treat.
    Derived by hand and checked by a record script on 2026-10-29: 300
    random systems of three to six species, with Gram, signed indefinite
    and positive-entry symmetric matrices; 3,274 feasible equilibria and
    14,266 invasion-graph edges, with rᵀx increasing along every edge
    and the identity holding to 10⁻⁹.
tags:
- ecology
- mathematics
date: '2026-10-29'
source:
- LIT-tmp8en4t
- LIT-1233
summary: >-
  Re-derived from Serván and Allesina (2021), LIT-tmp8en4t, read in
  NOTE-tmpwunhc, and applied to Hofbauer and Schreiber's invasion graph
  (LIT-1233). At an equilibrium V = 2rᵀx − xᵀAx equals rᵀx, and for two
  equilibria the difference is a sum of invasion growth rates weighted by
  abundances, which an edge of the invasion graph makes positive. It
  needs symmetry and one equilibrium per vertex, not positive
  definiteness. It does not say assembly is order-independent: an
  indefinite symmetric matrix has several sinks.
---
<!-- inactive-ok-file: QUESTION-132 — Open; the question whose invasion-graph condition this meets in the potential case, cited as open -->

# THEORY-tmplmes0: In a Lotka–Volterra community with a symmetric interaction matrix, the growth-weighted biomass rᵀx strictly increases along every edge of the invasion graph, so the invasion graph has no cycles

## Source

Serván and Allesina (2021), LIT-tmp8en4t, read in NOTE-tmpwunhc, for the
assembly-graph result and MacArthur's Lyapunov function; Hofbauer and
Schreiber (2022), LIT-1233, read in NOTE-1379, for the invasion graph.

## What was actually shown

Take ẋ_i = x_i(r_i − (Ax)_i) with A symmetric. (Per-capita weights v_i > 0,
as in Serván and Allesina's ẋ_i = v_i x_i(γ_i − (Bx)_i), change no sign and
leave the argument as it is, with γ for r.) For a set of species S with
an equilibrium x_S supported on S, write f_k(S) = r_k − (Ax_S)_k, the
growth of species k when rare at x_S; f_k(S) = 0 for k ∈ S.

1. At an equilibrium, x_Sᵀ(r − Ax_S) = 0, so MacArthur's
   V(x) = 2rᵀx − xᵀAx takes the value V(x_S) = rᵀx_S.
2. For two equilibria, because A is symmetric the cross terms cancel:
   f(S)ᵀx_T − f(T)ᵀx_S = rᵀx_T − x_SᵀAx_T − rᵀx_S + x_TᵀAx_S = rᵀ(x_T − x_S).
3. Dropping the zero terms,
   V(x_T) − V(x_S) = Σ_{j ∈ T∖S} f_j(S) x_{T,j} − Σ_{i ∈ S∖T} f_i(T) x_{S,i}.
4. Hofbauer and Schreiber's edge S → T requires S ≠ T, f_j(S) > 0 for
   every j ∈ T∖S, and f_i(T) < 0 for every i ∈ S∖T. Both sums then make
   the difference strictly positive, so rᵀx rises along every edge and
   no directed cycle exists.
5. Serván and Allesina's edge, a single invader j that grows at x_S and
   a community that settles at x_T, is covered the same way: V rises
   when j is added at small density, since ∂V/∂x_j = 2f_j(S) > 0, and V
   does not fall along the flow, so V(x_T) > V(x_S).

The check that could have failed: a script enumerated every feasible
equilibrium of 300 random symmetric systems and every invasion-graph
edge between them, and compared rᵀx across each edge and against the
identity of step 3. No edge violated it.

When A = UᵀU and r = Uᵀb − c (CLAIM-369), V(x*) = ‖b‖² − 2L(x*), so the
claim's objective L falls along every invasion-graph edge.

## What this does not say

- **Not that assembly is order-independent.** Acyclicity removes cycles,
  not alternative end-points. A symmetric matrix that is not positive
  definite has several uninvadable communities, and which one assembly
  reaches depends on order of arrival (Serván and Allesina's Figure 3.3).
  Uniqueness needs A positive definite, as a Gram matrix of independent
  vectors is.
- **Not that the invasion graph is defined.** The argument needs one
  equilibrium per vertex. With singular principal submatrices, as for a
  Gram matrix with more species than features, a vertex can carry a
  continuum of equilibria, and the statement is about whichever are
  chosen.
- **Not competition.** Neither positive entries nor positive
  definiteness is used, so it holds for symmetric facilitation too; the
  ecological reading as competition is a further condition.
- **Not beyond symmetry.** With A asymmetric the cross terms do not
  cancel, and cyclic invasion graphs exist (rock–paper–scissors).
