---
number: 1090
status: Active
formerly:
- THEORY-tmpvecoh
title: 'Eliminating an interior vertex of a cellular sheaf on a graph can leave its boundary a space of consistent assignments that no sheaf on the boundary vertices has: the interior can impose a constraint among boundary vertices that no set of pairwise compatibility conditions expresses, so Kron reduction, which turns the Laplacian of a connected graph into a graph Laplacian on any set of boundary vertices, fails for sheaves in general and holds when every vertex stalk has dimension at most one'
version: 1
tags:
- mathematics
- network-science
date: '2026-10-27'
source:
- LIT-1659
summary: >-
  Hansen and Ghrist (2019), [LIT-1659](../literature.d/LIT-1659.md), §4.2 (pp. 18–21), read in
  [NOTE-1233](../notes.d/NOTE-1233.md): a worked three-leaf star with a two-dimensional centre,
  and a closure theorem for the scalar-stalk case. Active as mathematics;
  the argument was checked. It is about the space of sections, a static
  fact; it does not say how often the obstruction arises, what structure
  would express the reduced constraint, or anything about dynamics.
---

# THEORY-1090: Eliminating an interior vertex of a cellular sheaf on a graph can leave its boundary a space of consistent assignments that no sheaf on the boundary vertices has: the interior can impose a constraint among boundary vertices that no set of pairwise compatibility conditions expresses, so Kron reduction, which turns the Laplacian of a connected graph into a graph Laplacian on any set of boundary vertices, fails for sheaves in general and holds when every vertex stalk has dimension at most one

## Source

Hansen and Ghrist (2019), [LIT-1659](../literature.d/LIT-1659.md), §4.2 and Fig. 4.1 of arXiv
1808.01513v2 (pp. 18–21); read in [NOTE-1233](../notes.d/NOTE-1233.md).

## What was actually shown

**For graphs, reduction stays pairwise.** Given boundary vertices B and
interior S, harmonic extension (Prop. 4.1) gives the Schur complement
L_G(B, B) − L_G(B, S)L_G(S, S)⁻¹L_G(S, B), which "is the Laplacian of a
graph with vertex set B" (Theorem 4.2, cited from Dörfler and Bullo,
p. 19): a resistor network reduces to an equivalent network on its
terminals.

**For sheaves, it need not.** The authors ask whether for a sheaf F with
boundary B there is a sheaf F_B on a graph with vertex set B whose
Laplacian is the reduced one, and answer "In general, Kron reduction is
not possible for sheaves" (p. 19). The example (Fig. 4.1, p. 20): a star
with three leaves, stalk ℝ² at the centre and ℝ at the leaves and edges,
the centre's maps being the first coordinate, the second coordinate and
their sum. Every section is fixed by its value (p, q) at the centre, so
the boundary values are (p + q, q, p): a two-dimensional space with basis
x₁ = (1, 1, 0)ᵀ, x₂ = (1, 0, 1)ᵀ. A sheaf on a graph with vertex set B has
only conditions on pairs of boundary vertices. For x₁ to satisfy the
conditions on the edges to v₃, the maps from v₁ and v₂ into them must be
zero; for x₂, the maps from v₁ and v₃ on the edges to v₂; and the two
together force the remaining maps. Then every restriction map is
zero and (1, 0, 0)ᵀ is a section too, so no such sheaf has exactly the
two-dimensional space. "The problem is that the internal node allows for
constraints between boundary nodes that cannot be expressed by purely
pairwise interactions. This fact is a fundamental obstruction to Kron
reduction for general sheaves" (p. 20). The reduced constraint is
v₁ = v₂ + v₃, a relation among three values.

**Where it holds.** With vertex stalks of dimension at most 1, sheaf
Laplacians are the matrices of factor width at most two, and Theorem 4.3
(pp. 20–21) shows that class is closed under Schur complements, so
reduction stays within sheaves on graphs.

What could have come out otherwise: a pairwise sheaf on B with exactly
the section space spanned by x₁ and x₂ would refute it; the argument
above shows there is none, and it was checked for this reading.

## What this does not say

- **How common the obstruction is**, or for which sheaves beyond the
  scalar-stalk case reduction still works. The paper gives one example
  and one sufficient condition.
- **What would express the reduced constraint.** The paper does not
  propose hypergraphs, higher cells or any other target for the
  reduction.
- **Anything about dynamics.** The statement is about sections and the
  Schur complement. It does not say what a boundary observer of a
  relaxing interior sees over time; that is [CLAIM-480](../claims.d/CLAIM-480.md)'s memory case,
  which this paper does not treat.
- **That the interactions are physical.** "Pairwise interactions" here
  means compatibility conditions on edges of a graph. Reading the centre
  as a physical subsystem whose couplings the boundary inherits
  ([CLAIM-480](../claims.d/CLAIM-480.md), [CLAIM-471](../claims.d/CLAIM-471.md)) is the record's interpretation.
