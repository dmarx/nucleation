---
number: 237
status: Proposed
formerly:
- THEORY-tmpx4k5f
promote_when: >-
  A read derivation of the optimal InfoNCE critic, from Ma & Collins or
  another original source, with its conditions on the negatives, since
  Poole et al. state that critic on Ma & Collins's authority. With it the
  claim would rest on derivations the record has checked for every member
  of the family. It is refuted by a critic that attains one of these bounds
  with equality at a nonzero mutual information and is not, up to the
  stated free term, the log density ratio. What cannot settle it: estimator
  benchmarks on Gaussian toys, which test bias and variance, not tightness.
title: "The critic-based variational lower bounds on mutual information, Donsker–Varadhan, NWJ, MINE's and InfoNCE, are relaxations of one unnormalized Barber–Agakov bound, and each is tight only at a critic equal to the log density ratio up to a term its normalization leaves free"
version: 2
history:
- version: 2
  date: '2026-10-14'
  note: >-
    After the close reading of LIT-256 (NOTE-tmp8mfe9). The Source now
    says that DV tightness "only" at the log derivative is the converse of
    the paper's "whenever", and holds only under mutual absolute
    continuity. The Deferred comment on LIT-256 removed.
tags:
- information-theory
- representation-learning
date: '2026-10-14'
source:
- LIT-246
- LIT-256
summary: >-
  Poole, Ozair, van den Oord, Alemi & Tucker (2019), [LIT-246](../literature.d/LIT-246.md), read in
  [NOTE-739](../notes.d/NOTE-739.md). Writing q(x|y) = p(x)e^f/Z(y) in Barber and Agakov's bound
  gives I_UBA, tight at f = log p(y|x) + c(y). Jensen gives
  Donsker–Varadhan, a tangent bound on the log gives TUBA and NWJ (unique
  optimal critic 1 + log p(x|y)/p(x)), and NWJ applied to a K-sample
  problem with the batch mean as normalizer gives InfoNCE. MINE's
  bias-corrected gradient is the exact gradient of TUBA. A Monte-Carlo DV
  estimate is neither an upper nor a lower bound. The InfoNCE optimum is
  cited, not derived, and the bias–variance comparisons are on toys.
---
<!-- inactive-ok-file: THEORY-001 — Proposed; cited for context -->

# THEORY-237: The critic-based variational lower bounds on mutual information, Donsker–Varadhan, NWJ, MINE's and InfoNCE, are relaxations of one unnormalized Barber–Agakov bound, and each is tight only at a critic equal to the log density ratio up to a term its normalization leaves free

## Source

Poole et al. (2019), [LIT-246](../literature.d/LIT-246.md), read in [NOTE-739](../notes.d/NOTE-739.md): §2.1–2.4, Eqs. 1–11,
Table 1. Supporting: Belghazi et al. (2018), [LIT-256](../literature.d/LIT-256.md), Eqs. 1, 3–4 and
App. 8.2.1, for the Donsker–Varadhan bound's tightness at the log
Radon–Nikodym derivative plus a constant. Belghazi et al. say
"whenever"; that it is tight only there is the converse, which follows
from their Eq. 25 but is not stated, and the supremum is attained only
when the joint and the product of marginals are mutually absolutely
continuous, otherwise it is approached in the limit ([NOTE-tmp8mfe9](../notes.d/NOTE-tmp8mfe9.md)).

## What was actually shown

One derivation, with each step a stated inequality:

1. **Barber–Agakov (Eq. 2).** I(X;Y) ≥ E[log q(x|y)] + h(X), tight at
   q(x|y) = p(x|y).
2. **Unnormalized BA (Eqs. 3–4).** With q(x|y) = p(x)e^(f(x,y))/Z(y),
   I ≥ E_(p(x,y))[f] − E_(p(y))[log Z(y)] =: I_UBA, "tight when
   f(x,y) = log p(y|x) + c(y), where c(y) is solely a function of y".
3. **Donsker–Varadhan (Eq. 5).** Jensen on E[log Z] gives I_DV ≤ I_UBA.
   A Monte-Carlo estimate of I_DV, as in MINE, gives "estimates that are
   neither an upper or lower bound on MI".
4. **TUBA and NWJ (Eqs. 6–7).** Bounding log Z(y) by a tangent at a(y) > 0
   gives I_TUBA, with unbiased estimates and gradients. a(y) = e gives
   I_NWJ, with "a unique optimal critic f*(x,y) = 1 + log p(x|y)/p(x)". With
   a(y) a moving average of e^f, the gradient of I_TUBA is MINE's
   bias-corrected gradient, so that heuristic is the exact gradient of a
   valid bound.
5. **InfoNCE (Eqs. 8–10).** NWJ applied to I(X_1, X_(2:K); Y), with the
   batch mean of e^f as the normalizer, gives I(X;Y) ≥ I_NCE once the K
   choices of which sample is paired are averaged ([THEORY-006](THEORY-006.md)). I_NCE ≤ log K.
6. **Interpolation (Eq. 11).** Mixing the batch mean with a learned q(y) by
   α ∈ [0,1] gives I_α, with NWJ at α = 0 and InfoNCE at α = 1, and
   I_α ≤ log(K/α).

So the optimal critic of every member is a function of the log density
ratio log p(y|x)/p(y), "for both I_NWJ and I_NCE" (§2.6). What is left free
is fixed by the normalization: nothing for NWJ beyond the +1, a function of
y for I_UBA and InfoNCE.

## What this does not say

- **Not a proof of the InfoNCE optimum.** That the optimal InfoNCE critic
  is log p(y|x) + c(y), and does not depend on K, is stated with a citation
  to Ma & Collins, not derived. The optimal critic of I_α is a conjecture.
- **Not which bound to use.** The bias–variance results, including that
  no bound studied is both low-bias and low-variance at large MI and small
  batch, come from 20-dimensional Gaussian and cubic toys and dSprites.
  Advice on estimator choice is machine-learning practice and belongs in
  the anthology.
- **Not that a tighter bound gives better representations.** Tschannen
  et al. ([LIT-247](../literature.d/LIT-247.md)) show the opposite for NWJ, and their invertible-encoder
  experiments show that MI does not fix representation quality.
- **Not about dependent batches.** With identically distributed but
  dependent pairs, I_NCE is neither a lower nor an upper bound ([THEORY-006](THEORY-006.md)).

## Connections

- **[THEORY-006](THEORY-006.md)** holds the InfoNCE member of this family: the bound for
  every critic and the log K ceiling. This account places that result in
  the family it comes from.
- **[THEORY-001](THEORY-001.md).** That every critic-based bound peaks at the log density
  ratio is the general-density form of [THEORY-001](THEORY-001.md)'s finite-space shared
  optimum, K⁺. Poole et al. support it in form. They do not treat the
  spectral or logistic losses.
