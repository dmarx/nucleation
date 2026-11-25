---
number: 770
status: Proposed
formerly:
- CLAIM-tmp9lm3d
title: 'Budget tree changes only at barrier crossings'
statement: >-
  The tree of classes reachable within a budget, the limit of a chain's time
  geometry as time scales separate, keeps its shape while barriers move and
  changes only where two barriers cross: a distinction between levels comes
  into being or passes away at such a crossing, and near it the two levels
  cannot be told apart in the time geometry
version: 2
history:
- version: 2
  date: '2026-11-21'
  note: >-
    A dated note: Bovier and colleagues' genericity condition excludes the
    near-crossings this claim describes. No change of status or title.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation: in the minimax barrier being the largest
  barrier on the path between two states in a minimum spanning tree of
  the barriers, or in the set of classes at every budget being fixed by
  the order of the barrier values. Or a continuous change of one barrier
  that changes the tree without its value crossing another barrier's.
tags:
- mathematics
- complex-systems
date: '2026-11-20'
line:
- formal-apparatus
- distributed-agency
rests_on:
- CLAIM-581
- CLAIM-780
bears_on:
- QUESTION-281
summary: >-
  What makes and unmakes a level of the tree [CLAIM-780](CLAIM-780.md) derives. The
  budgeted classes are those of single-linkage clustering on the barriers,
  so the tree depends only on the order of the barrier values: it is
  constant while barriers move without crossing, and changes only where
  two cross. With [CLAIM-780](CLAIM-780.md)'s slack, levels whose barriers are close
  cannot be told apart in the time geometry. A partial answer, in this
  model, to how distinctions come into being and pass away
  ([QUESTION-281](../questions.d/QUESTION-281.md)). The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-2137 — Proposed, Unfetched or new; filed in the readings of 2026-11-21 -->
<!-- inactive-ok-file: CLAIM-780 — Proposed; filed in this contribution of 2026-11-20 -->
<!-- inactive-ok-file: THEORY-1558 — Proposed; the levels lost when rates converge -->

# CLAIM-770: Budget tree changes only at barrier crossings

## The claim

[CLAIM-581](CLAIM-581.md)'s classes at budget b are the components of the graph keeping
only edges with barrier at most b. As b rises, these are the merges of
single-linkage clustering on the barrier values, so the minimax barrier
u(i, j) is the largest barrier on the path from i to j in a minimum spanning
tree of the barriers, and the whole tree of classes depends only on the
**order** of the barrier values. While barriers move without any two
crossing, the order is fixed and so is the tree. A class is created or
dissolved only where two barriers cross.

**Near a crossing the levels blur.** Two levels whose barriers differ by Δu
are separated in the log commute-time geometry by about log(1/ε)·Δu, and
[CLAIM-780](CLAIM-780.md)'s slack is 2·log max(E, n − 1). As two barriers approach a
crossing, Δu → 0 and the two levels stop being distinguishable in the time
geometry before the tree itself changes. This is [THEORY-1558](../theory.d/THEORY-1558.md)'s "when the
cycling rates converge … the distinction between the levels [is] lost",
stated for this model.

## Check

On the 4×4 torus with random barriers, each of 12 edges' barriers was swept
through 400 values in (0, 1), and the set of classes over all budgets was
computed at each. The tree changed 68 times over 4,800 settings, and every
change straddled the value of another edge's barrier (script in the curation
entry of 2026-11-20, 232905).

## What it bears on

[QUESTION-281](../questions.d/QUESTION-281.md) asks by which transitions distinctions come into being and pass
away: instability, nucleation across a barrier, bifurcation, tipping. In this
model a distinction between levels is made or unmade only when two barriers
exchange order, a crossing of time scales. That is one answer for systems a
barrier landscape describes, not an answer to the question in general; it
says nothing about creation by instability or by bifurcation of the
attractors themselves.

## Note of 2026-11-21: genericity and the degenerate case

Bovier and colleagues ([THEORY-2137](../theory.d/THEORY-2137.md)) assume genericity, that relevant times differ by factors going to infinity, which excludes exactly the near-crossings where this claim says levels blur. Their remark on the degenerate case, where times "differ only by constant factors" and the spectrum "will have to be computed specially through a finite dimensional, non-trivial diagonalisation problem", is their form of the same point. A parallel, not further evidence about the tree's changes.
