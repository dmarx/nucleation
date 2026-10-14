---
number: 1
status: Proposed
formerly:
- THEORY-tmp34v8v
promote_when: >-
  Done (NOTE-tmpu7m7r): a close reading of Johnson, El Hanchi & Maddison
  confirms the spectral and logistic derivations (App. B.2–B.3) with their
  finite-space and unconstrained-function conditions. Remaining: a read
  derivation of the InfoNCE/NT-Xent minimizer. Johnson et al. take its form
  from van den Oord et al. and minimize over symmetric functions only, and
  Poole et al. cite it from Ma & Collins; a close reading of either original
  proof, with its conditions on the negatives, would settle it.
title: 'On a finite augmentation space, InfoNCE, logistic and spectral contrastive losses share one population optimum: the positive-pair density ratio'
version: 2
history:
- version: 2
  date: '2026-10-14'
  note: >-
    After close readings of LIT-258 (NOTE-tmpu7m7r), LIT-249
    (NOTE-tmpbkfrz) and LIT-246 (NOTE-tmpapyks). The InfoNCE/NT-Xent
    minimizer is now said to be taken from van den Oord et al. rather than
    derived, over symmetric functions only, with negatives drawn i.i.d. from
    the marginal, and not unique. HaoChen et al.'s Lemma 3.2 is credited
    only with the factorization, and the step to K⁺ with Johnson et al. App.
    B.3. Poole et al. §2.3 is said to support the density-ratio optimum in
    form, citing it rather than proving it. promote_when rewritten: the
    spectral and logistic derivations are confirmed, the InfoNCE one is not.
    The Deferred comments on LIT-246, LIT-249 and LIT-258 removed.
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
  and a minimizer of NT-Xent/InfoNCE over symmetric functions, with negatives
  i.i.d. from the marginal, is K⁺ up to a factor constant on communicating
  classes; that form is taken from van den Oord et al., not derived. It is a
  statement about the unconstrained optimum, not about what a network
  reaches.
extended_by:
- THEORY-007
answers:
- QUESTION-052
---
<!-- inactive-ok-file: LIT-251 — Deferred: filed and skimmed on 2026-09-26 while pursuing the owner's Riesz/Radon–Nikodym/GNS question; the theories citing it are Proposed until it is read closely -->

# THEORY-001: On a finite augmentation space, InfoNCE, logistic and spectral contrastive losses share one population optimum: the positive-pair density ratio

## Source

Johnson, El Hanchi & Maddison (2023), [LIT-258](../literature.d/LIT-258.md), Table 1 and App. B.1–B.3. Supporting: HaoChen et al. (2021), [LIT-249](../literature.d/LIT-249.md), Lemma 3.2 (the factorization only; the step to K⁺ is Johnson et al. App. B.3); Poole et al. (2019), [LIT-246](../literature.d/LIT-246.md), §2.3 (the InfoNCE optimum in form, cited there, not proved); Tosh, Krishnamurthy & Hsu (2021), [LIT-251](../literature.d/LIT-251.md), §2.3; Tan et al., [LIT-227](../literature.d/LIT-227.md). Levy & Goldberg's shifted-PMI factorization of word2vec ([ANTH-LIT-612](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-612.md), Eq. 7) is the log-domain case with k negatives, and CPC ([ANTH-LIT-589](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-589.md), Eq. 5) states the critic's proportionality to the ratio.

## What was actually shown

On a finite augmentation space, the logistic loss with one negative per positive and the spectral contrastive loss are minimized over all functions of the two views by exactly the ratio K⁺ = p⁺/(p⊗p), and these minimizers are derived ([LIT-258](../literature.d/LIT-258.md), App. B.2–B.3). HaoChen et al. show that the spectral loss is a matrix-factorization loss ([LIT-249](../literature.d/LIT-249.md), Lemma 3.2) but never name K⁺; their own minimizer is the rank-k one. InfoNCE/NT-Xent is handled differently. Johnson et al. take the form of its minimizer, f*(c,a) = (p(a|c)/p(a))·b(c), from van den Oord et al., with the negatives drawn i.i.d. from the marginal rather than from other positive pairs as in practice. They then restrict to symmetric functions, which forces b to be constant on each communicating class of the positive-pair chain, so the minimizer is K⁺ times such a factor ([LIT-258](../literature.d/LIT-258.md), Table 1, App. B.1). They note that this optimum "is not unique" for the cross-entropy loss. Poole et al. state the optimal InfoNCE critic as log p(y|x) + c(y), the log ratio plus a function of y, for general densities, on Ma & Collins's authority rather than by derivation ([LIT-246](../literature.d/LIT-246.md), §2.3). In the log domain, skip-gram with k negatives is minimized by PMI − log k ([ANTH-LIT-612](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-612.md)). K⁺ is the Radon–Nikodym derivative of the positive-pair distribution with respect to the product of its marginals, so each of these objectives estimates the same change of measure; [LIT-251](../literature.d/LIT-251.md) §2.4 names it as such ("the change-of-measure from P_Z to P_(Z|X=x)").

The derivation could have come out otherwise: a loss whose optimum depended on the negative-sampling scheme or the batch size in a way that did not cancel would have a different target. It does not, for these three, in the unconstrained population limit.

## What this does not say

- That a finite-capacity encoder reaches K⁺. Every result here is over unconstrained functions, and for InfoNCE over symmetric functions only.
- Anything about InfoNCE with in-batch negatives drawn from other positive pairs. Johnson et al.'s NT-Xent minimizer assumes negatives i.i.d. from the marginal.
- That low-rank truncations under the different losses coincide. InfoNCE and skip-gram fit the log of the ratio, while the spectral loss fits the ratio itself; exp and log do not commute with rank-d truncation, so the d-dimensional representations can differ.
- Anything about continuous augmentation spaces without an integrability condition (see the operator claim that extends this one).
- That the features are good. That is a separate question (the eigenbasis claim, and Tschannen et al. on why the MI story is not the explanation).
