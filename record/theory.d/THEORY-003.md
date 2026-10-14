---
number: 3
status: Active
formerly:
- THEORY-tmp8uwye
title: 'Maximizing HSIC between representations and image identity maximizes the average squared MMD between the images'' view distributions, whose kernel mean embeddings exist by the Riesz representation theorem'
version: 3
history:
- version: 2
  date: '2026-10-14'
  note: >-
    After close readings of LIT-248 (NOTE-830) and LIT-260 (NOTE-838). The MMD–HSIC constant corrected to N/Δ_l, and the citation
    to the unnumbered B.2 identity rather than eq. 5. The InfoNCE–HSIC
    link is no longer called only a small-variance approximation: eq. 28
    is exact and Theorem B.1 a bound; the disclaimer that InfoNCE is HSIC
    is kept. MMD is a metric only for characteristic kernels. promote_when
    records that both halves now look met; the status is unchanged, for
    the owner. THEORY-312 cited in Connections. The Deferred comments
    on LIT-248 and LIT-260 removed.
- version: 3
  date: '2026-10-14'
  note: >-
    Promoted from Proposed to Active at the owner's direction. Both clauses
    of promote_when are met by Read NOTEs. The Li et al. clause: NOTE-830
    (LIT-248, read in full) confirms the App. B.2 identity,
    (1/2N²)Σ_ij MMD²(i,j) = (N/Δ_l)·HSIC(Z,Y), as an exact derivation under
    Theorem A.1's setting; the paper states no integrability condition, and
    for the bounded kernels it uses the condition holds through Lemma 3.1,
    since E√k(X,X) ≤ √k_max. The Muandet et al. clause: NOTE-838
    (LIT-260, chs. 2–3 read closely) confirms Lemma 3.1, proved in the
    review, with its condition E_P√k(X,X) < ∞. The promote_when is removed.
    The claim is unchanged.
tags:
- representation-learning
- mathematics
date: '2026-09-26'
source:
- LIT-248
- LIT-260
summary: >-
  Li, Pogodin, Sutherland & Gretton (2021), [LIT-248](../literature.d/LIT-248.md), eq. 5 and App. B.2;
  Muandet et al. (2017), [LIT-260](../literature.d/LIT-260.md), Lemma 3.1 — the one place in this
  family where Riesz is invoked explicitly. InfoNCE is not HSIC: Li et
  al.'s eq. 28 decomposes it exactly as −HSIC plus a log-mean-exp term,
  and Theorem B.1 bounds it with no variance assumption.
answers:
- QUESTION-052
---
<!-- inactive-ok-file: THEORY-312 — Proposed; the account of eq. 28 and Theorem B.1 filed from LIT-248, named in Connections -->

# THEORY-003: Maximizing HSIC between representations and image identity maximizes the average squared MMD between the images' view distributions, whose kernel mean embeddings exist by the Riesz representation theorem

## Source

Li, Pogodin, Sutherland & Gretton (2021), [LIT-248](../literature.d/LIT-248.md), eq. 5, eqs. 6–8, App. B.2. Muandet, Fukumizu, Sriperumbudur & Schölkopf (2017), [LIT-260](../literature.d/LIT-260.md), Thm 2.4, Prop. 2.1, Lemma 3.1, Def. 3.2, §3.5.

## What was actually shown

Muandet et al. define an RKHS by bounded evaluation, state Riesz (Thm 2.4) and derive the reproducing property from it (Prop. 2.1). Their Lemma 3.1: if E_P √k(X,X) < ∞, then f ↦ E_P f is bounded, so by Riesz there is a unique μ_P with E_P f = ⟨f, μ_P⟩, and μ_P = ∫ k(·,x) dP(x). MMD is then the RKHS norm ‖μ_P − μ_Q‖ (§3.5, eq. 3.29), a metric on distributions only for a characteristic kernel, and P ↦ μ_P is injective exactly when k is characteristic (Def. 3.2).

Li et al. show that with one-hot image-identity labels, (1/2N²)Σ_ij MMD²(i,j) = (N/Δ_l) HSIC(Z,Y) (App. B.2; the identity is unnumbered there, and eq. 5 is Theorem A.1's proportional form). So maximizing HSIC maximizes the average squared distance between the mean embeddings of each image's view distribution: views of one image concentrate, different images spread.

## What this does not say

- That InfoNCE is HSIC. Li et al.'s §3.1 link (eqs. 6–8) is a Taylor approximation in a small-variance regime, but the link is not only that: eq. 28 is an exact decomposition of the large-batch loss as −HSIC(Z,Y) plus a log-mean-exp of the centred critic, and Theorem B.1 is a bound for every bounded kernel with no variance assumption.
- That the embedding is injective on a learned feature space. That needs a characteristic kernel there, and every result in the review assumes a fixed kernel.
- Anything about losses that are not kernel dependence measures.

## Connections

- [THEORY-312](THEORY-312.md), filed from the close reading of [LIT-248](../literature.d/LIT-248.md), holds eq. 28 and Theorem B.1 at the strength they are established: the large-batch InfoNCE loss is −HSIC(Z,Y) plus a nonnegative term, so it bounds a kernel dependence loss from above.
