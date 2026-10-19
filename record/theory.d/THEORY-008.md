---
number: 8
status: Active
formerly:
- THEORY-tmpqq4es
title: 'On a finite set of stimuli, what a regularized linear readout can decode from a representation is a function of its normalized kernel, and CKA, CCA and GULP are averages of readout agreement'
version: 5
history:
- version: 2
  date: '2026-10-14'
  note: >-
    After the close reading NOTE-743 (LIT-254). Kornblith et al. are
    now cited only for what they show: that R²_CCA, linear regression and
    linear CKA are one family, differing in how eigen-directions are
    weighted, with canonical ridge interpolating among them (Eqs. 11–14,
    App. D.1). They say nothing about readouts, decoding, averaging over
    tasks or GULP. The Deferred comment for LIT-254 removed; LIT-257 is
    still Deferred and the promote_when, which concerns it, is unchanged.
- version: 3
  date: '2026-10-14'
  note: >-
    A Connections section added: THEORY-236 (LIT-254, Thm 1), filed
    today, says why the CCA member of the family, which is invariant to
    every invertible linear map, is degenerate at full rank.
- version: 4
  date: '2026-10-14'
  note: >-
    After the close reading of LIT-257 (NOTE-834). promote_when
    records the Prop. 2 / Cor. 1 clause as met and the App. A.3 clause as
    unmeetable from this paper; it now asks for finite-M confirmation plus
    a population source such as GULP's analysis. Not promoted. "Equals"
    CKA, GULP, CCA, ENSD corrected (only ENSD is the average similarity
    itself); orthogonal invariance given its condition G = aC_X + bI;
    "whatever basis" made orthonormal, any linear change only for CCA;
    §5's future work is linear classifiers. Prop. 3 is read, holds, gives
    inequalities, and is cited as THEORY-301. The Deferred comment on
    LIT-257 removed.
- version: 5
  date: '2026-10-19'
  note: >-
    Confined to a finite stimulus set and promoted from Proposed to Active
    at the owner's direction, from the second pass of the owner's
    promotion audit of 2026-10-19. NOTE-834 found the promote_when's first
    clause met (Prop. 2 and Cor. 1 proved in full and re-derived) and its
    population clause unmeetable from this paper, and named the two ways
    forward: another source, or "a rewording that confines the claim to
    finite M". This takes the second. The body already stated everything
    at finite M; the title now says so. The population clause moves,
    unchanged, to QUESTION-tmp4uhs6, and the promote_when is removed.
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
  whatever orthonormal basis the representation is written in, for
  G = aC_X + bI; under any linear change of basis only for the CCA member,
  G = C_X.
extends:
- THEORY-004
supports:
- CLAIM-193
- CLAIM-269
---
<!-- inactive-ok-file: THEORY-301 — Proposed; the account of Prop. 3 filed from LIT-257, named and not leaned on -->
<!-- inactive-ok-file: THEORY-236 — Proposed; named in Connections for why GL-invariant comparison is degenerate, not leaned on -->

# THEORY-008: On a finite set of stimuli, what a regularized linear readout can decode from a representation is a function of its normalized kernel, and CKA, CCA and GULP are averages of readout agreement

## Source

Harvey, Lipshutz & Williams (2024), [LIT-257](../literature.d/LIT-257.md), eqs. 2, 7–8, 22–23, Prop. 2, Cor. 1, Table 1. Supporting, for the family structure only: Kornblith et al. (2019), [LIT-254](../literature.d/LIT-254.md), Eqs. 11–14 and App. D.1, as read in [NOTE-743](../notes.d/NOTE-743.md). The same point from the concept-direction side is [ANTH-LIT-606](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-606.md) (Park, Choe & Veitch), whose Thm 3.2 uses a Riesz isomorphism and whose §3 shows the inner product is not identified by training.

## What was actually shown

For readouts w maximizing zᵀXw/M − ½wᵀG(X)w, the decoded signal is K_X z with K_X = X G(X)⁻¹ Xᵀ/M ([LIT-257](../literature.d/LIT-257.md) eqs. 2, 7–8), so it depends on X only through K_X, which is invariant under orthogonal transformations of X (eqs. 22–23) whenever G(X) is parameterized as in eq. 4, G = aC_X + bI. The task-averaged agreement of two representations' readouts is Tr(K_X K_z K_Y) (Prop. 2); with K_z = I it gives linear CKA, GULP, mean squared CCA or ENSD for particular choices of G (Cor. 1, Table 1). Only ENSD is the average similarity itself: CKA and mean squared CCA are it normalized by the self-similarities, and GULP is the average decoding distance. The family structure has a precursor in Kornblith et al., who show that R²_CCA, linear regression and linear CKA differ only in how they weight the same eigen-direction overlaps, and that canonical ridge interpolates among them ([LIT-254](../literature.d/LIT-254.md) Eqs. 11–14, App. D.1). They say nothing about readouts, decoding, averaging over tasks or GULP; the readout reading is [LIT-257](../literature.d/LIT-257.md)'s alone.

## What this does not say

- **Anything in the population limit.** Every identity here is for M stimuli. Whether the K_z = I identities have a non-degenerate limit as M grows, which the source's App. A.3 does not reach, is [QUESTION-tmp4uhs6](../questions.d/QUESTION-tmp4uhs6.md).
- Anything about nonlinear readouts, which are outside the source, or classifiers (§5 names linear classifiers, SVMs and multi-class logistic regression, as future work).
- Which task distribution K_z is the right one to average over.
- The source's Proposition 3 (bounds via Procrustes distance) is a result of a different kind: two-sided inequalities rather than identities. It is now read and holds, given the imported Procrustes–Bures equivalence; [THEORY-301](THEORY-301.md) holds it.

## Connections

- **[THEORY-236](THEORY-236.md).** Mean squared CCA, one of the averages above, is
  invariant to every invertible linear map: it is an orthogonally invariant
  index applied to orthonormalized columns ([LIT-254](../literature.d/LIT-254.md), Prop. 1). Kornblith et
  al.'s Theorem 1 then makes it constant on all representations whose rank
  equals the number of examples. Linear CKA, invariant only to orthogonal
  maps and isotropic scaling, escapes that degeneracy.
