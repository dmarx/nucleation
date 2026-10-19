---
number: 136
status: Open
formerly:
- QUESTION-tmp4uhs6
title: 'As the number of stimuli grows, do the task-averaged readout identities with white-noise tasks have a non-degenerate population form, with (1/M²)Tr(K̂_X K̂_Y) converging to the Hilbert–Schmidt inner product of the kernel operators, and at what rate when the regularizer is estimated?'
version: 1
tags:
- representation-learning
- mathematics
date: '2026-10-19'
line: formal-apparatus
summary: >-
  The population clause of [THEORY-008](../theory.d/THEORY-008.md)'s former promote_when. On
  2026-10-19 [THEORY-008](../theory.d/THEORY-008.md) was confined to a finite stimulus set, where
  Harvey, Lipshutz & Williams prove its identities, and promoted. Their
  App. A.3 sketch does not reach the K_z = I case, where its limit is zero
  ([NOTE-834](../notes.d/NOTE-834.md)). GULP's population analysis may answer it, and the record
  does not hold it.
---

# QUESTION-136: As the number of stimuli grows, do the task-averaged readout identities with white-noise tasks have a non-degenerate population form, with (1/M²)Tr(K̂_X K̂_Y) converging to the Hilbert–Schmidt inner product of the kernel operators, and at what rate when the regularizer is estimated?

## Why it is a question

[THEORY-008](../theory.d/THEORY-008.md) states Harvey, Lipshutz & Williams's identities ([LIT-257](../literature.d/LIT-257.md),
Prop. 2 and Cor. 1) for M stimuli. The task-averaged readout agreement is
Tr(K_X K_z K_Y). With K_z = I it gives linear CKA, GULP, mean squared CCA
or ENSD. [NOTE-834](../notes.d/NOTE-834.md) read the proofs and re-derived them. Until 2026-10-19,
[THEORY-008](../theory.d/THEORY-008.md)'s promote_when also asked for the population version. At the
owner's direction, from the owner's promotion audit of that date, the
finite identities were promoted alone, and that clause moved here
unchanged.

It is open because the source does not settle it. App. A.3 is an outline
by its own account. It needs b > 0, so the CCA member is not covered, and
it mis-states a constant (eq. 77). It also treats a trace-class task
covariance, and at K_z = I, the white-noise limit, the quantity it tracks,
(1/M³)Tr(K̂ I Ĥ) = (1/M)Tr(K_X K_Y), goes to 0. The non-degenerate form
needs the normalization (1/M²)Tr(K̂Ĥ) → Tr[KH], which A.3 does not state.

## What would answer it

A source that proves the identities at K_z = I in the population limit,
such as GULP's population analysis (Boix-Adsera et al., not held). Or a
proof the record checks of the convergence of (1/M²)Tr(K̂Ĥ), with G
estimated from the sample, for each member of the family, CCA included.
