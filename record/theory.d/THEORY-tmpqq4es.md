---
status: Proposed
promote_when: >-
  A close reading of Harvey, Lipshutz & Williams confirming Prop. 2 and Cor.
  1, including the population version in App. A.3. The identities are proved
  in the source; this record has so far only skimmed it.
title: 'What a regularized linear readout can decode from a representation is a function of its normalized kernel, and CKA, CCA and GULP are averages of readout agreement'
version: 1
tags:
- representation-learning
- mathematics
date: '2026-09-26'
source:
- LIT-tmptlaw2
- LIT-tmpmford
summary: >-
  Harvey, Lipshutz & Williams (2024), [LIT-tmptlaw2](../literature.d/LIT-tmptlaw2.md), eqs. 2, 7–8, Prop. 2, Cor.
  1 and Table 1 — proved identities. This is the finite-dimensional content of
  "a probe is a functional": the probe's output is fixed by the kernel,
  whatever basis the representation is written in.
extends:
- THEORY-tmpcawyi
---
<!-- inactive-ok-file: LIT-tmptlaw2 — Deferred: filed and skimmed on 2026-09-26 while pursuing the owner's Riesz/Radon–Nikodym/GNS question; the theories citing it are Proposed until it is read closely -->
<!-- inactive-ok-file: LIT-tmpmford — Deferred: filed and skimmed on 2026-09-26 while pursuing the owner's Riesz/Radon–Nikodym/GNS question; the theories citing it are Proposed until it is read closely -->

# THEORY-tmpqq4es: What a regularized linear readout can decode from a representation is a function of its normalized kernel, and CKA, CCA and GULP are averages of readout agreement

## Source

Harvey, Lipshutz & Williams (2024), [LIT-tmptlaw2](../literature.d/LIT-tmptlaw2.md), eqs. 2, 7–8, 22–23, Prop. 2, Cor. 1, Table 1. Supporting: Kornblith et al. (2019), [LIT-tmpmford](../literature.d/LIT-tmpmford.md). The same point from the concept-direction side is [ANTH-LIT-606](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-606.md) (Park, Choe & Veitch), whose Thm 3.2 uses a Riesz isomorphism and whose §3 shows the inner product is not identified by training.

## What was actually shown

For readouts w maximizing zᵀXw/M − ½wᵀG(X)w, the decoded signal is K_X z with K_X = X G(X)⁻¹ Xᵀ/M ([LIT-tmptlaw2](../literature.d/LIT-tmptlaw2.md) eqs. 2, 7–8), so it depends on X only through K_X, which is invariant under orthogonal transformations of X (eqs. 22–23). The task-averaged agreement of two representations' readouts is Tr(K_X K_z K_Y) (Prop. 2); with K_z = I it equals linear CKA, GULP, mean squared CCA or ENSD for particular choices of G (Cor. 1, Table 1).

## What this does not say

- Anything about nonlinear readouts or classifiers (named as future work in the source's §5).
- Which task distribution K_z is the right one to average over.
- The source's Proposition 3 (bounds via Procrustes distance) is a separate, weaker result, and its proof was not read.
