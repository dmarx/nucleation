---
number: 1
status: Proposed
formerly:
- THEORY-tmp34v8v
promote_when: >-
  A close reading of Johnson, El Hanchi & Maddison confirming the Table 1
  derivations (App. B.1–B.3) and their finite-space and unconstrained-function
  conditions. The theorem is proved in the source; this record has so far only
  skimmed it.
title: 'On a finite augmentation space, InfoNCE, logistic and spectral contrastive losses share one population optimum: the positive-pair density ratio'
version: 1
tags:
- representation-learning
- information-theory
date: '2026-09-26'
source:
- LIT-258
- LIT-249
- LIT-246
- LIT-251
- LIT-227
summary: >-
  Johnson, El Hanchi & Maddison (2023), [LIT-258](../literature.d/LIT-258.md) — over unconstrained
  functions on a finite augmentation space, the population minimizer of the
  spectral contrastive and NT-Logistic losses is K⁺ = p⁺(a₁,a₂)/(p(a₁)p(a₂)),
  and that of NT-Xent/InfoNCE is K⁺ up to a factor constant on communicating
  classes. It is a statement about the unconstrained optimum, not about what a
  network reaches.
extended_by:
- THEORY-007
---
<!-- inactive-ok-file: LIT-251 — Deferred: filed and skimmed on 2026-09-26 while pursuing the owner's Riesz/Radon–Nikodym/GNS question; the theories citing it are Proposed until it is read closely -->
<!-- inactive-ok-file: LIT-246 — Deferred: filed and skimmed on 2026-09-26 while pursuing the owner's Riesz/Radon–Nikodym/GNS question; the theories citing it are Proposed until it is read closely -->
<!-- inactive-ok-file: LIT-258 — Deferred: filed and skimmed on 2026-09-26 while pursuing the owner's Riesz/Radon–Nikodym/GNS question; the theories citing it are Proposed until it is read closely -->
<!-- inactive-ok-file: LIT-249 — Deferred: filed and skimmed on 2026-09-26 while pursuing the owner's Riesz/Radon–Nikodym/GNS question; the theories citing it are Proposed until it is read closely -->

# THEORY-001: On a finite augmentation space, InfoNCE, logistic and spectral contrastive losses share one population optimum: the positive-pair density ratio

## Source

Johnson, El Hanchi & Maddison (2023), [LIT-258](../literature.d/LIT-258.md), Table 1 and App. B.1–B.3. Supporting: HaoChen et al. (2021), [LIT-249](../literature.d/LIT-249.md), Lemma 3.2; Poole et al. (2019), [LIT-246](../literature.d/LIT-246.md), §2.3; Tosh, Krishnamurthy & Hsu (2021), [LIT-251](../literature.d/LIT-251.md), §2.3; Tan et al., [LIT-227](../literature.d/LIT-227.md). Levy & Goldberg's shifted-PMI factorization of word2vec ([ANTH-LIT-612](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-612.md), Eq. 7) is the log-domain case with k negatives, and CPC ([ANTH-LIT-589](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-589.md), Eq. 5) states the critic's proportionality to the ratio.

## What was actually shown

For each loss, the minimizer over all functions of the two views is derived explicitly, on a finite augmentation space. The logistic loss with one negative per positive and the spectral contrastive loss are minimized by exactly the ratio K⁺ = p⁺/(p⊗p). InfoNCE/NT-Xent is minimized by K⁺ times a factor that is constant on each communicating class of the positive-pair chain ([LIT-258](../literature.d/LIT-258.md), Table 1). In the log domain, skip-gram with k negatives is minimized by PMI − log k ([ANTH-LIT-612](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-612.md)). K⁺ is the Radon–Nikodym derivative of the positive-pair distribution with respect to the product of its marginals, so each of these objectives estimates the same change of measure; [LIT-251](../literature.d/LIT-251.md) §2.4 names it as such ("the change-of-measure from P_Z to P_(Z|X=x)").

The derivation could have come out otherwise: a loss whose optimum depended on the negative-sampling scheme or the batch size in a way that did not cancel would have a different target. It does not, for these three, in the unconstrained population limit.

## What this does not say

- That a finite-capacity encoder reaches K⁺. Every result here is over unconstrained functions.
- That low-rank truncations under the different losses coincide. InfoNCE and skip-gram fit the log of the ratio, while the spectral loss fits the ratio itself; exp and log do not commute with rank-d truncation, so the d-dimensional representations can differ.
- Anything about continuous augmentation spaces without an integrability condition (see the operator claim that extends this one).
- That the features are good. That is a separate question (the eigenbasis claim, and Tschannen et al. on why the MI story is not the explanation).
