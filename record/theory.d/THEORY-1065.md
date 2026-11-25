---
number: 1065
status: Active
formerly:
- THEORY-tmpbgffi
title: 'Robust synchrony iff balanced partition'
statement: >-
  In a coupled cell network, a pattern of synchrony is invariant under every
  dynamics the network's architecture admits if and only if its partition of
  the cells is balanced, each cell of a class receiving, through each kind
  of arrow, the same number of inputs from each class; symmetry is one way
  to get balance and not the only one, so robust synchrony occurs in
  networks with no symmetry and among cells with no coupling between them,
  and the invariance says nothing about whether the pattern attracts
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
<!-- inactive-ok-file: CASE-296 THEORY-2005 THEORY-2054 THEORY-2055 — Proposed; cited in this filing of 2026-11-19 -->
<!-- inactive-ok-file: THEORY-2014 — Proposed; cited in this filing of 2026-11-19 -->

# THEORY-1065: Robust synchrony iff balanced partition

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

## Note of 2026-11-19: the exchange "Topological protection explained"

A17 §1 presented graph fibrations as new to the record. They are this theorem's structure under other names. Two cells in one fibre have isomorphic "input trees" (A17 §1), which is what a balanced partition asks of each class. "Graph fibration" is the term of Boldi and Vigna's work, not on the record, and DeVille and Lerman ([LIT-2792](../literature.d/LIT-2792.md), Deferred, unread) treat the maps between network dynamical systems that fibrations induce.

Gili and colleagues ([THEORY-2014](THEORY-2014.md), read) apply the theorem in reverse: they infer the network whose coarsest balanced colouring equals an observed synchrony partition. They call an invariant partition proven to be synchronous. This account says it does not show that: invariance says nothing about whether the pattern attracts or will be seen. Velarde and colleagues ([LIT-2843](../literature.d/LIT-2843.md), Deferred, unread) report that fibrations emerge in trained neural networks.

The owner's U9 hunch, that the fibration approach relates to Li and Webb's symbolic mechanisms, is [QUESTION-492](../questions.d/QUESTION-492.md).

No status change.

## Note of 2026-11-19: readings for the exchange "Topological protection explained"

DeVille and Lerman ([THEORY-2005](THEORY-2005.md)), read: supports the sufficiency half and generalizes it. They state that the quotient maps of balanced relations are the surjective graph fibrations, and prove that surjective fibrations make the synchrony polydiagonal invariant for every groupoid-invariant vector field, on manifolds rather than Euclidean spaces (Theorem 4.3.1, Lemma 5.1.1). They prove only this direction: "We do not attempt to establish the converse" (Remark 4.3.3). The necessity half still rests on Stewart, Golubitsky and Pivato alone.

Velarde, Parra, Hashemi and Makse ([THEORY-2055](THEORY-2055.md)), read: uses the balanced-colouring form on weighted feed-forward networks, with equal summed input weight from each colour class (their Eq. 14), so that units in a fiber synchronize for every input. That weighted version lies outside the 2003 definition held here. Their claim that covers are stable attractors of SGD rests on a cited result, not on the invariance, consistent with this entry's warning that invariance says nothing about attraction.

Larremore, Clauset and Jacobs ([THEORY-2054](THEORY-2054.md)), read; the reader's observation, not the paper's: a block of a stochastic block model is a balanced partition in expectation, its members having the same expected number of edges to each block. That is a stochastic counterpart of this entry's equal count of inputs from each class, which is exact, not expected. Neither source states the link. If made, it would put the genres case ([CASE-296](../cases.d/CASE-296.md)) and the fibration hunch ([QUESTION-492](../questions.d/QUESTION-492.md)) on one formal object.

No status change.

## Note of 2026-11-19: Wang and Slotine, read
<!-- inactive-ok-file: THEORY-2044 — Proposed; cited from the readings of 2026-11-19 -->

A complement ([THEORY-2044](THEORY-2044.md); [NOTE-2096](../notes.d/NOTE-2096.md)). This account gives balanced partitions as the invariant synchrony patterns, "existence, not stability". Wang and Slotine give the stability side under their conditions: for identical units with symmetric positive-definite diffusive coupling, full synchrony attracts globally above a spectral threshold, and the same bound applies to "symmetric subgroups in a network" (Theorem 6, p. 14). Different conditions, a different question; together they say when an invariant pattern is also reached.

## Note of 2026-11-19: Chen, Kunin, Yamamura and Ganguli, read
An analogy across two dynamics ([NOTE-2127](../notes.d/NOTE-2127.md)): in weight space under training, Chen and colleagues likewise separate invariance from attraction, which needs a condition weighing curvature against noise. It supports this account's warning by parallel, not in the state dynamics of cells.

## Note of 2026-11-22: Stewart, read
<!-- inactive-ok-file: THEORY-2251 — Proposed; filed by LEAD-023 -->

Stewart ([THEORY-2251](THEORY-2251.md), which extends this account; [NOTE-2342](../notes.d/NOTE-2342.md)) proves that the balanced partitions this account describes form a complete lattice under refinement, whose meet is not intersection: two balanced colourings can have an unbalanced common refinement (Example 5·5). The lattice's top, the coarsest balanced partition, is unique and computable. It confirms this account's last clause: invariance, not attraction. No change to this account.
