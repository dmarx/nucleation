---
status: Proposed
promote_when: >-
  A proof that the coarse-graining maximizing mutual information with the
  environment beyond a buffer, under a fixed number and type of coarse
  variables and so short of full capture, yields effective couplings whose
  range or strength beyond nearest neighbours is bounded by the
  information lost, for a class of local Hamiltonians in two or more
  dimensions; or a check, on a 2D lattice model with its blocks, that the
  per-block capture assumption of the D-dimensional proof holds or fails.
  More 1D cases cannot settle it, nor can examples in which the
  renormalized Hamiltonian is short-ranged for reasons of the model
  (decimation of the Ising chain is exact whatever information it keeps).
title: 'For a finite-range lattice Hamiltonian, a block coarse-graining that keeps all the mutual information the block shares with the system beyond a buffer makes the coarse measure factorize across the block, so the renormalized Hamiltonian gains no range and, in 1D, product disorder gains no correlations across the block; the coarse-grainings actually optimized fall short of that condition, and for them the link is shown only numerically, in 1D'
version: 1
tags:
- natural-sciences
- information-theory
date: '2026-10-09'
source:
- LIT-tmptez84
summary: >-
  Lenggenhager, Gökmen, Ringel, Huber and Koch-Janusz (2018),
  [LIT-tmptez84](../literature.d/LIT-tmptez84.md): proved in 1D, and in D dimensions under an extra per-block
  assumption and barring fine-tuned cancellations. The full-capture
  condition is not met in the paper's own worked case (decimation of
  two-spin Ising blocks keeps about half the information), and the decay
  of longer-range, many-spin and disorder-correlation terms as more
  information is kept is shown perturbatively for two-spin blocks of 1D
  chains only, and is monotonic only locally.
---
<!-- inactive-ok-file: THEORY-194 THEORY-073 QUESTION-025 — Proposed or open; cited as the account this one underpins, a neighbour, and the question it does not answer -->

# THEORY-tmpc8tc8: For a finite-range lattice Hamiltonian, a block coarse-graining that keeps all the mutual information the block shares with the system beyond a buffer makes the coarse measure factorize across the block, so the renormalized Hamiltonian gains no range and, in 1D, product disorder gains no correlations across the block; the coarse-grainings actually optimized fall short of that condition, and for them the link is shown only numerically, in 1D

## Source

Lenggenhager, Gökmen, Ringel, Huber and Koch-Janusz (2018; Phys. Rev. X
2020), [LIT-tmptez84](../literature.d/LIT-tmptez84.md): Sec. III and Appendix B (Lemma, Propositions 1 and
2, Eqs. B1–B22), Secs. IV and VI with Appendix D (Figs. 4, 5, 9–12); as
read in [NOTE-tmp2hvr8](../notes.d/NOTE-tmp2hvr8.md).

## What was actually shown

**The proof.** Blocks are taken large enough that only neighbouring
blocks interact. Fix a block (in D dimensions, a hyperplane of blocks),
call its neighbours the buffer and the rest the left and right
environments. If the coarse variable keeps all the block's information
about the environment, the block carries no further information about the
environment given the coarse variable; locality makes the two
environments independent given the block; together they make the two
environments independent given the coarse variable. The coarse measure
then factorizes across that variable once the coarse buffer is summed
out, so no effective term couples the two sides. Since the block was
arbitrary, the range does not grow. In 1D with a product distribution of
nearest-neighbour disorder, the same rule stays optimal under any change
of disorder confined to one side, so the renormalized disorder
distribution carries no correlations across the block.

This could have failed: full capture might have left the environments
correlated through the buffer, and in D dimensions it might require
coarse variables shared across blocks. The first is excluded by the
proof; the second is excluded by assumption.

**The numerics.** For every two-spin rule (λ₁, λ₂) on the 1D Ising chain
and on the dilute random Ising chain, the information kept is computed
exactly and the renormalized couplings perturbatively. Next-nearest
neighbour and four-spin couplings, and correlations between neighbouring
renormalized couplings, vanish where the information is greatest, at
decimation. Majority rule, which keeps least, generates them.

## What this does not say

- **Not that the maximizer gets full capture.** With the number and type
  of coarse variables fixed, it usually cannot. In the paper's worked
  case decimation keeps about half of I(V : E) (0.505 at K = 0.1 with a
  one-site buffer, by the reader's calculation), yet its Hamiltonian is
  exactly nearest-neighbour; that exactness is a property of the 1D
  chain, not a consequence of the theorem.
- **Not that complexity falls monotonically with information.** The
  authors find it monotonic only locally, with accidental zeros away from
  the maximum; what is kept is that the global maximum is a global
  minimum of the measured couplings.
- **Not a proof for two or more dimensions without conditions.** The
  D-dimensional step assumes that capture for a hyperplane amounts to
  capture by each block separately, called reasonable, not shown, and
  excludes fine-tuned cancellations of existing couplings. The disorder
  result is proved in 1D only.
- **Not that the block, buffer and environment are found.** They are a
  spatial partition fixed before anything is computed, and locality is
  stated with respect to it.
- **Not an instruction for machine learning.** No network is trained;
  the RBM is only a family of rules.

## Connections

It underpins [THEORY-194](THEORY-194.md), which records that the information-maximizing
coarse-graining matched the known RG variables of the Ising and dimer
models: this is the argument for why such a coarse-graining should keep
the effective Hamiltonian short-ranged. It does not meet [THEORY-194](THEORY-194.md)'s
`promote_when`, which asks for a statement about the maximizer, not the
perfect case. The Lemma is a screening statement of the kind [THEORY-073](THEORY-073.md)
examines for Markov blankets, with the screening region likewise placed
in advance; that parallel is the reader's. It does not bear on
[QUESTION-025](../questions.d/QUESTION-025.md).
