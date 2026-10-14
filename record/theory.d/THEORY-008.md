---
number: 8
status: Proposed
formerly:
- THEORY-tmpqq4es
promote_when: >-
  A close reading of Harvey, Lipshutz & Williams confirming Prop. 2 and Cor.
  1, including the population version in App. A.3. The identities are proved
  in the source; this record has so far only skimmed it.
title: 'What a regularized linear readout can decode from a representation is a function of its normalized kernel, and CKA, CCA and GULP are averages of readout agreement'
version: 2
history:
- version: 2
  date: '2026-10-14'
  note: >-
    After the close reading NOTE-tmph96lt (LIT-254). Kornblith et al. are
    now cited only for what they show: that R²_CCA, linear regression and
    linear CKA are one family, differing in how eigen-directions are
    weighted, with canonical ridge interpolating among them (Eqs. 11–14,
    App. D.1). They say nothing about readouts, decoding, averaging over
    tasks or GULP. The Deferred comment for LIT-254 removed; LIT-257 is
    still Deferred and the promote_when, which concerns it, is unchanged.
tags:
- representation-learning
- mathematics
date: '2026-09-26'
source:
- LIT-257
- LIT-254
summary: >-
  Harvey, Lipshutz & Williams (2024), [LIT-257](../literature.d/LIT-257.md), eqs. 2, 7–8, Prop. 2, Cor.
  1 and Table 1 — proved identities. This is the finite-dimensional content of
  "a probe is a functional": the probe's output is fixed by the kernel,
  whatever basis the representation is written in.
extends:
- THEORY-004
supports:
- CLAIM-193
- CLAIM-269
---
<!-- inactive-ok-file: LIT-257 — Deferred: filed and skimmed on 2026-09-26 while pursuing the owner's Riesz/Radon–Nikodym/GNS question; the theories citing it are Proposed until it is read closely -->

# THEORY-008: What a regularized linear readout can decode from a representation is a function of its normalized kernel, and CKA, CCA and GULP are averages of readout agreement

## Source

Harvey, Lipshutz & Williams (2024), [LIT-257](../literature.d/LIT-257.md), eqs. 2, 7–8, 22–23, Prop. 2, Cor. 1, Table 1. Supporting, for the family structure only: Kornblith et al. (2019), [LIT-254](../literature.d/LIT-254.md), Eqs. 11–14 and App. D.1, as read in [NOTE-tmph96lt](../notes.d/NOTE-tmph96lt.md). The same point from the concept-direction side is [ANTH-LIT-606](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-606.md) (Park, Choe & Veitch), whose Thm 3.2 uses a Riesz isomorphism and whose §3 shows the inner product is not identified by training.

## What was actually shown

For readouts w maximizing zᵀXw/M − ½wᵀG(X)w, the decoded signal is K_X z with K_X = X G(X)⁻¹ Xᵀ/M ([LIT-257](../literature.d/LIT-257.md) eqs. 2, 7–8), so it depends on X only through K_X, which is invariant under orthogonal transformations of X (eqs. 22–23). The task-averaged agreement of two representations' readouts is Tr(K_X K_z K_Y) (Prop. 2); with K_z = I it equals linear CKA, GULP, mean squared CCA or ENSD for particular choices of G (Cor. 1, Table 1). The family structure has a precursor in Kornblith et al., who show that R²_CCA, linear regression and linear CKA differ only in how they weight the same eigen-direction overlaps, and that canonical ridge interpolates among them ([LIT-254](../literature.d/LIT-254.md) Eqs. 11–14, App. D.1). They say nothing about readouts, decoding, averaging over tasks or GULP; the readout reading is [LIT-257](../literature.d/LIT-257.md)'s alone.

## What this does not say

- Anything about nonlinear readouts or classifiers (named as future work in the source's §5).
- Which task distribution K_z is the right one to average over.
- The source's Proposition 3 (bounds via Procrustes distance) is a separate, weaker result, and its proof was not read.
