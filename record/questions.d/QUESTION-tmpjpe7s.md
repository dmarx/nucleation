---
status: Open
title: 'Does the coarse-graining that maximizes mutual information with the system beyond a buffer find the renormalization-group variables of a system where they were not known beforehand, and does it give short-ranged effective Hamiltonians in two or more dimensions?'
version: 1
tags:
- natural-sciences
- information-theory
- representation-learning
date: '2026-10-20'
line: 'formal-apparatus'
summary: >-
  The promotion condition formerly on [THEORY-194](../theory.d/THEORY-194.md), moved here when
  [THEORY-194](../theory.d/THEORY-194.md) was narrowed to what Koch-Janusz and Ringel measured on the
  2D Ising and dimer models and promoted on 2026-10-20 ([ADR-047](../decisions.d/ADR-047.md) v3).
  Every 2D case in that study had a known answer, and the link to a
  short-ranged effective Hamiltonian is proved only for 1D and quasi-1D
  chains.
---

# QUESTION-tmpjpe7s: Does the coarse-graining that maximizes mutual information with the system beyond a buffer find the renormalization-group variables of a system where they were not known beforehand, and does it give short-ranged effective Hamiltonians in two or more dimensions?

## Why it is a question

On Monte Carlo samples of the 2D Ising model and the noisy 2D dimer model,
the block coarse-graining trained to maximize mutual information with the
environment beyond a buffer recovered the variables renormalization
already knew: Kadanoff block spins and the dimers' low-momentum electric
fields. Iterated on the Ising model, it gave the flow and ν ≈ 1.0 ± 0.15
([THEORY-194](../theory.d/THEORY-194.md), from [LIT-873](../literature.d/LIT-873.md) read in [NOTE-674](../notes.d/NOTE-674.md)). The sequels extend the
evidence to the interacting dimer model across a BKT transition ([LIT-878](../literature.d/LIT-878.md)),
again with operators known from field theory. They also prove that a
coarse-graining keeping all of a block's information about its
environment adds no range to the Hamiltonian, while the optimised
coarse-grainings fall short of that condition ([LIT-881](../literature.d/LIT-881.md), [THEORY-198](../theory.d/THEORY-198.md)).
Near the first information-bottleneck transition the optimal encoder of a
slab follows the leading transfer-matrix mode ([LIT-885](../literature.d/LIT-885.md), [THEORY-205](../theory.d/THEORY-205.md)),
which is a different geometry from a block in a buffer shell.

So whether the objective and renormalization agree where renormalization's
variables are unknown is open, and so is whether the maximizer yields
short-ranged couplings in two or more dimensions. Until 2026-10-20 this
was [THEORY-194](../theory.d/THEORY-194.md)'s promote_when.

## What would answer it

Yes, empirically: a system in two or more dimensions whose relevant
variables were not known beforehand, where the maximizer is computed and
iterated and gives critical exponents that agree with an independent
method (high-precision Monte Carlo, series or conformal bootstrap) within
stated errors, while a coarse-graining fitted to the data distribution on
the same samples does not. Yes, formally: a proof, for a class of local
Hamiltonians in two or more dimensions, that the maximizer yields an
effective Hamiltonian whose couplings decay with distance.

No: a system where the maximizer's iterated flow gives exponents that
disagree with an independent method, or a local Hamiltonian in two or
more dimensions where the maximizer produces long-ranged couplings.

What would not answer it: more rediscoveries of block spins or of other
variables already known, since the account was shown on exactly those.
