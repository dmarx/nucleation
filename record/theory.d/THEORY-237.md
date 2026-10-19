---
number: 237
status: Active
formerly:
- THEORY-tmpx4k5f
title: "The critic-based variational lower bounds on mutual information, Donsker–Varadhan, NWJ, MINE's and InfoNCE, are relaxations of one unnormalized Barber–Agakov bound, and, when the joint and the product of the marginals are mutually absolutely continuous, each attains its supremum over critics only at a critic equal to the log density ratio up to a term its normalization leaves free, where every bound but InfoNCE equals the mutual information"
version: 3
history:
- version: 2
  date: '2026-10-14'
  note: >-
    After the close reading of LIT-256 (NOTE-828). The Source now
    says that DV tightness "only" at the log derivative is the converse of
    the paper's "whenever", and holds only under mutual absolute
    continuity. The Deferred comment on LIT-256 removed.
- version: 3
  date: '2026-10-19'
  note: >-
    Narrowed and promoted, carrying out the promotion audit's decision for
    THEORY-237 (batch 043, ADR-047 v2). The optimum of each member is
    derived in the dated note below, including InfoNCE's, which the source
    cites to Ma & Collins; that meets the promote_when. The title's
    "tight" did not fit InfoNCE, whose supremum is at most log K and
    generally below the mutual information, so it now says "attains its
    supremum", names the members that then equal the mutual information,
    and states the absolute-continuity condition.
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
  cited, not derived, in the source (the record derives it, note of
  2026-10-19), and the bias–variance comparisons are on toys.
---
<!-- inactive-ok-file: THEORY-001 — Proposed; cited for context -->

# THEORY-237: The critic-based variational lower bounds on mutual information, Donsker–Varadhan, NWJ, MINE's and InfoNCE, are relaxations of one unnormalized Barber–Agakov bound, and, when the joint and the product of the marginals are mutually absolutely continuous, each attains its supremum over critics only at a critic equal to the log density ratio up to a term its normalization leaves free, where every bound but InfoNCE equals the mutual information

## Source

Poole et al. (2019), [LIT-246](../literature.d/LIT-246.md), read in [NOTE-739](../notes.d/NOTE-739.md): §2.1–2.4, Eqs. 1–11,
Table 1. Supporting: Belghazi et al. (2018), [LIT-256](../literature.d/LIT-256.md), Eqs. 1, 3–4 and
App. 8.2.1, for the Donsker–Varadhan bound's tightness at the log
Radon–Nikodym derivative plus a constant. Belghazi et al. say
"whenever"; that it is tight only there is the converse, which follows
from their Eq. 25 but is not stated, and the supremum is attained only
when the joint and the product of marginals are mutually absolutely
continuous, otherwise it is approached in the limit ([NOTE-828](../notes.d/NOTE-828.md)).

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
is fixed by the normalization: nothing for NWJ beyond the +1, a constant
for Donsker–Varadhan, a function of y for I_UBA and InfoNCE.

## What this does not say

- **Not, in the source, a proof of the InfoNCE optimum.** That the optimal
  InfoNCE critic is log p(y|x) + c(y), and does not depend on K, is stated
  with a citation to Ma & Collins, not derived; the record derives it in
  the note of 2026-10-19. The optimal critic of I_α is a conjecture.
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

## Note of 2026-10-19: every member's optimum derived, InfoNCE's included

The promotion audit (batch 043, [ADR-047](../decisions.d/ADR-047.md) v2) derived the optimum of each
member, InfoNCE's included. The source cites that one to Ma & Collins
and does not derive it. Assume the joint P and the product of the
marginals Q are mutually absolutely continuous, and write
r = dP/dQ = p(x|y)/p(x).

1. **UBA.** I_UBA(f) = I − E_y KL(p(x|y) ‖ p(x)e^f/Z(y)). So it equals I
   exactly when f = log r + c(y), with c(y) = log Z(y) left free.
2. **DV.** I_DV = E_P f − log E_Q e^f = I_UBA − (log E_y Z(y) −
   E_y log Z(y)). Jensen is an equality only when Z(y) is constant. So,
   with step 1, I_DV = I exactly when f = log r + c with c a constant.
   MINE maximizes this bound.
3. **TUBA and NWJ.** log Z ≤ Z/a + log a − 1 gives I_TUBA ≤ I_UBA, with
   equality when a(y) = Z(y). With a ≡ e (NWJ), the objective
   E_P f − e^(−1) E_Q e^f is strictly concave pointwise. Its unique
   maximizer is f = 1 + log r, where it equals 1 + I − 1 = I.
4. **InfoNCE as NWJ.** Let x₁ ∼ p(x|y), and let the negatives x₂, …, x_K
   be i.i.d. from p(x), independent of (x₁, y). Then
   I(X_(1:K); Y) = I(X; Y). Apply NWJ with the critic
   1 + log(e^(f(x₁,y))/m), where m = (1/K) Σ_k e^(f(x_k,y)). This gives
   1 + E log(e^(f(x₁,y))/m) − E_Q[e^(f(x₁,y))/m]. Under Q every x_k is
   i.i.d. p(x) and independent of y, so by symmetry each E_Q[e^(f(x_k,y))/m]
   is equal, and they average to E_Q[m/m] = 1. That leaves I_NCE ≤ I, and
   I_NCE ≤ log K.
5. **InfoNCE's optimum.** Put the positive at a uniformly random index J.
   Then I_NCE = log K + E log softmax_J(f(x_k, y)), and the posterior is
   P(J = j | y, x_(1:K)) = r(x_j, y)/Σ_k r(x_k, y). No predictor has a
   higher expected log-likelihood than the posterior (Gibbs), and only
   predictors equal to it a.s. match it. Comparing indices j and l gives
   f(x_j, y) − f(x_l, y) = log r(x_j, y) − log r(x_l, y) for a.e.
   (y, x_j, x_l), so f − log r depends on y alone. So InfoNCE's
   maximizers are exactly f = log r + c(y), for every K ≥ 2. The
   conditions on the negatives are that they are i.i.d. from p(x) and
   independent of the positive and of y; for dependent batches see
   [THEORY-006](THEORY-006.md). At the optimum I_NCE = log K + E log posterior_J, which is
   below I whenever I > log K.

So each bound attains its supremum over critics only at log r plus the
free term: a function of y for UBA, TUBA and InfoNCE, a constant for DV,
and nothing beyond the +1 for NWJ. At that critic every member but
InfoNCE equals I. The title said "tight", which does not fit InfoNCE; it
now says "attains its supremum". Without mutual absolute continuity the
DV supremum is approached, not attained ([NOTE-828](../notes.d/NOTE-828.md)).
