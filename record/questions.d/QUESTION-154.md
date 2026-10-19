---
number: 154
status: Open
formerly:
- QUESTION-tmpavq90
title: "Does a block coarse-graining that maximizes the information its coarse variables keep about the far environment, but falls short of full capture with their number and type fixed, keep the renormalized Hamiltonian's longer-range couplings bounded by the information lost, in two or more dimensions?"
version: 1
tags:
- natural-sciences
- information-theory
date: '2026-10-19'
line: 'distributed-agency'
refines:
- QUESTION-065
summary: >-
  The promotion condition formerly on [THEORY-198](../theory.d/THEORY-198.md), moved here unchanged when
  [THEORY-198](../theory.d/THEORY-198.md) was narrowed and promoted on 2026-10-19. The perfect case is
  proved: full capture makes the coarse measure factorize across the block.
  The maximizers actually found fall short of full capture, and for them
  the link to a short-ranged Hamiltonian is shown only on 1D chains.
---

# QUESTION-154: Does a block coarse-graining that maximizes the information its coarse variables keep about the far environment, but falls short of full capture with their number and type fixed, keep the renormalized Hamiltonian's longer-range couplings bounded by the information lost, in two or more dimensions?

## Why it is a question

[THEORY-198](../theory.d/THEORY-198.md), narrowed on 2026-10-19, holds that a block coarse-graining
keeping all of the block's information about the environment beyond a
buffer makes the coarse measure factorize across the block. This is proved
in 1D, and in D dimensions when capture by a hyperplane of blocks amounts
to capture by each block and no existing couplings cancel. So the
renormalized Hamiltonian gains no range. Until that date, [THEORY-198](../theory.d/THEORY-198.md)'s
promote_when asked about the case short of full capture. At the owner's
direction, from the promotion audit's batch 019 ([ADR-047](../decisions.d/ADR-047.md)), the THEORY was
narrowed and promoted on the proved case, and the condition moved here
unchanged.

It is open because full capture is not what optimization reaches. With the
number and type of coarse variables fixed in advance, the maximizer usually
falls short: decimation of two-spin Ising blocks keeps about half of
I(V : E) (0.505 at K = 0.1 with a one-site buffer, [NOTE-682](../notes.d/NOTE-682.md)). Whether the
information lost bounds the couplings generated is shown only by
perturbative calculation on 1D chains ([LIT-881](../literature.d/LIT-881.md)), and only locally
monotonically. It refines [QUESTION-065](QUESTION-065.md)'s question of whether locality can
supply the target a sufficiency-based boundary is relative to.

## What would answer it

The condition formerly on [THEORY-198](../theory.d/THEORY-198.md), unchanged. It asks for a proof that
the coarse-graining maximizing mutual information with the environment
beyond a buffer, under a fixed number and type of coarse variables and so
short of full capture, yields effective couplings whose range or strength
beyond nearest neighbours is bounded by the information lost, for a class
of local Hamiltonians in two or more dimensions. Or it asks for a check, on
a 2D lattice model with its blocks, that the per-block capture assumption
of the D-dimensional proof holds or fails. More 1D cases cannot settle it.
Nor can examples in which the renormalized Hamiltonian is short-ranged for
reasons of the model: decimation of the Ising chain is exact whatever
information it keeps.
