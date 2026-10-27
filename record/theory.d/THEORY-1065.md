---
number: 1065
status: Active
formerly:
- THEORY-tmpbgffi
title: 'In a coupled cell network, a pattern of synchrony is invariant under every dynamics the network''s architecture admits if and only if its partition of the cells is balanced, each cell of a class receiving, through each kind of arrow, the same number of inputs from each class; symmetry is one way to get balance and not the only one, so robust synchrony occurs in networks with no symmetry and among cells with no coupling between them, and the invariance says nothing about whether the pattern attracts'
version: 1
tags:
- network-science
- mathematics
date: '2026-10-27'
source:
- LIT-1674
summary: >-
  Stewart, Golubitsky and Pivato (2003), [LIT-1674](../literature.d/LIT-1674.md), read in
  [NOTE-1217](../notes.d/NOTE-1217.md) from the accepted version: Theorem 6.5 with proof, Lemma
  6.3, worked examples without symmetry (Figures 3, 9, 15, 19). Active as
  mathematics. It generalizes [THEORY-276](THEORY-276.md)'s orbit clusters. "Robust" means
  invariant for the whole admissible class, not stable, and not invariant
  for one model family; the paper studies "existence, not stability".
---
<!-- inactive-ok-file: QUESTION-063 — Open; the drive-or-coupling question this account bears on, cited as open -->

# THEORY-1065: In a coupled cell network, a pattern of synchrony is invariant under every dynamics the network's architecture admits if and only if its partition of the cells is balanced, each cell of a class receiving, through each kind of arrow, the same number of inputs from each class; symmetry is one way to get balance and not the only one, so robust synchrony occurs in networks with no symmetry and among cells with no coupling between them, and the invariance says nothing about whether the pattern attracts

## Source

Stewart, Golubitsky and Pivato (2003), [LIT-1674](../literature.d/LIT-1674.md), §§1–6 (pp. 609–632
of SIAM J. Appl. Dyn. Syst. 2(4), read from the accepted version); read in
[NOTE-1217](../notes.d/NOTE-1217.md).

## What was actually shown

**The setting.** A coupled cell network is a finite directed graph with
typed cells and typed arrows (Definition 2.1, p. 616). An admissible vector
field gives each cell an equation depending only on its input set, the same
function for cells whose input sets are isomorphic by a type-preserving map,
symmetric under permutations of equivalent inputs (Definition 4.1, p. 622).
Coupling need not be additive: a cell's evolution "can in principle be any
(smooth) function" of its inputs (p. 610).

**The theorem.** For an equivalence relation ⋈ on the cells, the
polydiagonal {x : x_c = x_d whenever c ⋈ d} is invariant under every
admissible vector field "if and only if ⋈ is balanced" (Theorem 6.5,
p. 630). Balanced: equivalent cells c, d have an input isomorphism γ with
i ⋈ γ(i) for every input i (Definition 6.4, p. 629). The proof's counting
condition, |U ∩ K_s| = |U ∩ L_s| for every class U and arrow type s (eq. 6.2),
is the "same number of inputs from each class" form. Lemma 6.3 (p. 629):
only cells with isomorphic input sets can be robustly synchronous at all.

**What could have come out otherwise.** Necessity is not obvious, and the
paper proves it by constructing, for any unbalanced relation, an admissible
field that leaves the polydiagonal (eq. 6.4, pp. 631–632). Its worked case:
moving one cell to another class in Example 5.1 changes "multiplicity",
three inputs of one colour against two, and the subspace is no longer
invariant (p. 629).

**Without symmetry.** In the three-cell network of Figure 3 (eq. 1.5,
p. 612), "This network has no symmetry, but the network structure forces the
"polydiagonal" subspace Y = {x : x₁ = x₂} to be flow-invariant." Example 4.4
(p. 623), the five-cell network of Example 7.1 (p. 633) and the three-cell
master–slave network of Figure 19 (p. 635) are others. A network symmetry,
restricted to an input set, is an input isomorphism that keeps each cell in
its orbit, so orbit partitions are balanced and the symmetry-group case
([THEORY-276](THEORY-276.md)) is contained in this one; the paper builds on the
fixed-point-subspace argument (p. 611) but does not state this inclusion as
a theorem.

**Without coupling among the synchronized cells.** In Example 5.1 cells 4,
5, 7 and 9 have no arrows between them; each receives one input of the
round type and one from the class {2, 3, 6, 8}, and they are robustly
synchronous (Figures 11–12, p. 626). In Figure 19, cell 3 is only driven by
cell 1 while cell 2 is driven by and drives cell 1; 2 and 3 are robustly
synchronous.

## What this does not say

- **That a balanced pattern is stable or will be seen.** "in this paper we
  are studying existence, not stability, and we do not wish to rule out
  unstable synchrony because it still corresponds to an invariant subspace
  for the dynamics" (p. 626). The authors' example, identical cells with no
  inputs, is invariant and, they say, "dynamically unstable" (p. 626); that
  holds for some internal dynamics, not all. Which patterns attract is a
  model-dependent question the paper leaves alone.
- **What is invariant for one model.** "Robust" quantifies over the whole
  admissible class, and the necessity proof uses linear admissible fields
  (eq. 6.4). A narrower family, such as identical diffusive coupling with
  one fixed coupling function, can have invariant subspaces that are not
  balanced in this sense.
- **That synchronized cells interact.** Balance is equal input; cells can be
  robustly synchronous with no arrow between them, so a synchronized class
  is not shown to be coupled, entrained or a unit of any kind.
- **That a synchrony pattern distinguishes coupling from common drive.** A
  drive is another cell, and balance counts inputs regardless of source
  (Figure 19). The paper does not discuss inference from observed
  synchrony; [QUESTION-063](../questions.d/QUESTION-063.md)'s case is outside it.
- **Anything about weighted or multiple arrows.** The 2003 definition takes
  arrows as a subset of C × C (Definition 2.1), one per ordered pair.
- **Anything about nonidentical cells within a class.** ⋈ refines cell type
  (p. 628); synchrony of cells of different types is not defined here.
