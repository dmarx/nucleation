---
number: 3
status: Proposed
formerly:
- THEORY-tmp8uwye
promote_when: >-
  A close reading of Li et al. App. B.2 and of Muandet et al. Lemma 3.1
  confirming the identity and the lemma with their integrability conditions.
  Both are proved in the sources; this record has so far only skimmed them.
title: 'Maximizing HSIC between representations and image identity maximizes the average squared MMD between the images'' view distributions, whose kernel mean embeddings exist by the Riesz representation theorem'
version: 1
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
  family where Riesz is invoked explicitly. InfoNCE ≈ HSIC holds only as a
  small-variance approximation.
---
<!-- inactive-ok-file: LIT-248 — Deferred: filed and skimmed on 2026-09-26 while pursuing the owner's Riesz/Radon–Nikodym/GNS question; the theories citing it are Proposed until it is read closely -->
<!-- inactive-ok-file: LIT-260 — Deferred: filed and skimmed on 2026-09-26 while pursuing the owner's Riesz/Radon–Nikodym/GNS question; the theories citing it are Proposed until it is read closely -->

# THEORY-003: Maximizing HSIC between representations and image identity maximizes the average squared MMD between the images' view distributions, whose kernel mean embeddings exist by the Riesz representation theorem

## Source

Li, Pogodin, Sutherland & Gretton (2021), [LIT-248](../literature.d/LIT-248.md), eq. 5, eqs. 6–8, App. B.2. Muandet, Fukumizu, Sriperumbudur & Schölkopf (2017), [LIT-260](../literature.d/LIT-260.md), Thm 2.4, Prop. 2.1, Lemma 3.1, Def. 3.2, §3.5.

## What was actually shown

Muandet et al. define an RKHS by bounded evaluation, state Riesz (Thm 2.4) and derive the reproducing property from it (Prop. 2.1). Their Lemma 3.1: if E_P √k(X,X) < ∞, then f ↦ E_P f is bounded, so by Riesz there is a unique μ_P with E_P f = ⟨f, μ_P⟩, and μ_P = ∫ k(·,x) dP(x). MMD is then a norm, ‖μ_P − μ_Q‖ (§3.5), and P ↦ μ_P is injective exactly when k is characteristic (Def. 3.2).

Li et al. show that with one-hot image-identity labels, (1/2N²)Σ_ij MMD²(i,j) = NΔ_l HSIC(Z,Y) (App. B.2, eq. 5). So maximizing HSIC maximizes the average squared distance between the mean embeddings of each image's view distribution: views of one image concentrate, different images spread.

## What this does not say

- That InfoNCE is HSIC. Li et al.'s §3.1 link (eqs. 6–8) is a Taylor approximation in a small-variance regime.
- That the embedding is injective on a learned feature space. That needs a characteristic kernel there, and every result in the review assumes a fixed kernel.
- Anything about losses that are not kernel dependence measures.
