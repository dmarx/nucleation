---
number: 194
status: Proposed
formerly:
- THEORY-tmpsylqv
promote_when: >-
  A system whose relevant variables were not known beforehand, in two or
  more dimensions, where the coarse-graining that maximizes mutual
  information with the environment beyond a buffer is computed, iterated,
  and gives critical exponents that agree with an independent method
  (high-precision Monte Carlo, series or conformal bootstrap) within
  stated errors, while a coarse-graining fitted to the data distribution
  on the same samples does not. Or a proof, for a class of local
  Hamiltonians in two or more dimensions, that the maximizer yields an
  effective Hamiltonian whose couplings decay with distance. More
  rediscoveries of block spins or of other variables already known cannot
  settle it, because the account was shown on exactly those.
title: 'For the 1D and 2D Ising and 2D dimer models, the block coarse-graining that maximizes mutual information with the system beyond a buffer around the block is the renormalization-group relevant one, while a coarse-graining fitted to reproduce the data distribution is not: which variables a compression keeps is set by what it must stay informative about'
version: 1
tags:
- natural-sciences
- information-theory
- representation-learning
date: '2026-10-09'
source:
- LIT-873
summary: >-
  Koch-Janusz and Ringel (2017), [LIT-873](../literature.d/LIT-873.md): shown numerically on two
  2D lattice models whose relevant variables were known (Ising block
  spins, dimer electric fields), with an iterated Ising flow giving T_c to
  about 1% and ν ≈ 1.0 ± 0.15, and analytically only for 1D and quasi-1D
  chains. The general equivalence of the objective with a short-ranged
  effective Hamiltonian is argued, not proved, and no system with unknown
  relevant variables was tried.
---
<!-- inactive-ok-file: THEORY-036 THEORY-017 QUESTION-025 — Proposed or open; cited as accounts this one bears on and the question it does not answer -->

# THEORY-194: For the 1D and 2D Ising and 2D dimer models, the block coarse-graining that maximizes mutual information with the system beyond a buffer around the block is the renormalization-group relevant one, while a coarse-graining fitted to reproduce the data distribution is not: which variables a compression keeps is set by what it must stay informative about

## Source

Koch-Janusz and Ringel (2017; Nature Physics 2018), [LIT-873](../literature.d/LIT-873.md): main
text Figs. 2, 4 and 5; supplement Eqs. 5–15 (the estimator), Eqs. 20–40
(1D Ising), Eqs. 41–44 (saturation), Figs. 8–11; as read in [NOTE-674](../notes.d/NOTE-674.md).

## What was actually shown

**The objective.** For a block V, a buffer B and the environment E beyond
it, choose the coarse variables H, drawn from an RBM-form P_Λ(H|V), to
maximize I_Λ(H : E). Only Monte Carlo samples are used.

**Numerically, in 2D.** For the Ising model the maximizer on a 2 × 2 block
is Kadanoff's block spin, and on larger blocks it weights the boundary. For
the fully packed dimer model it reads the low-momentum electric fields of
the height-field description, and it gives zero weight to decoupled,
regularly patterned noise spins. Iterated four times on 128 × 128 Ising
samples, it produces the flow away from T_c on both sides, locates T_c to
about 1%, and gives ν ≈ 1.0 ± 0.15. An RBM trained by contrastive
divergence to fit the noisy dimer data instead spends its hidden units on
the noise, then on columnar patterns that carry no field. Each could have
come out otherwise: the maximizer could have coupled to the noise, the
flow could have failed to separate, or the fitted RBM could have found the
fields too.

**Analytically, in 1D.** Among decimation, boundary-majority and uniform
majority filters for the 1D Ising chain, decimation, the known optimal RG,
carries twice the boundary filter's information and the uniform filter's
vanishes with block size. For 1D and quasi-1D systems with short-range
interactions, if adding hiddens no longer increases the information, the
effective Hamiltonian has no coupling across the block.

## What this does not say

- **Not that the objective finds relevant variables in general.** Every 2D
  case had a known answer. The account is that, on these models, the
  objective and RG agree; whether they agree where RG's variables are
  unknown is what `promote_when` asks.
- **Not a proof of equivalence with RG in two or more dimensions.** The
  equivalence with a compact, short-ranged effective Hamiltonian is proved
  only for 1D and quasi-1D chains, and the 1D comparison is among three
  filters, not over all.
- **Not that distribution-fitting networks never coarse-grain correctly.**
  One dataset shows that they need not; when the two objectives coincide is
  open.
- **Not that the variables are intrinsic to the data.** The block, buffer
  and environment are a spatial partition supplied before anything is
  learned, and the buffer's width is a choice. Mutual information is
  invariant under bijections of the variables, but the partition is not;
  so, consistently with [THEORY-017](THEORY-017.md), the parts the method compresses are
  given to it.
- **Not a hierarchy of attributes.** The levels are nested spatial blocks.
  Nothing here concerns attributes implying one another, linear attribute
  directions in embeddings or concept lattices, so it leaves [QUESTION-025](../questions.d/QUESTION-025.md)
  as it was.
- **Not an instruction for machine learning.** It says which objective
  coincides with RG on these models, not how to train anything.

## Connections

It gives an operational criterion for the scale-relative, lossy
description that [THEORY-036](THEORY-036.md) and Ladyman's real patterns ([LIT-219](../literature.d/LIT-219.md)) take RG
as their example of: the compression that counts is the one that keeps
information about the far field. The objective is a variant of the
information bottleneck ([LIT-338](../literature.d/LIT-338.md)) with the environment as the relevance
variable.
