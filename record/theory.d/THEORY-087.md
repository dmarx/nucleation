---
number: 87
status: Proposed
formerly:
- THEORY-tmpzelk0
promote_when: >-
  A held proof of the singular half. The regular half is derived in the
  sources. The singular half rests on Watanabe's free-energy asymptotics
  (Theorem 2 of LIT-616), which that paper states and cites but does
  not prove, and on its §7.1 remark that λ < d/2 when the prior is positive
  on the optimal set, which is also stated with a citation. A reading of
  the proofs, in Watanabe's book (LIT-354) or in the earlier papers it
  cites (Watanabe 2001a, 2010b), would promote this. So would a direct
  check that does not go through WBIC: in a singular model whose RLCT is
  known, such as the reduced-rank regression of LIT-616 §6, a free
  energy computed by integration over all temperatures, or exactly for a
  small model, should grow with log n at slope λ and not at slope d/2.
  The account is refuted by such a model whose free energy grows at any
  slope other than λ. WBIC's own estimates of λ cannot settle it, since
  they are derived from the same theory. Further agreement between BIC
  and the evidence in regular models cannot settle it either.
title: 'The Bayesian complexity penalty grows as (d/2) log n in a regular model, where the curvature at the optimum sets the Occam factor, and as λ log n in a singular one, where λ is the real log canonical threshold and falls below d/2 when the prior is positive on the optimal set'
version: 1
tags:
- model-comparison
- information-geometry
- learning-theory
- probabilistic-modeling
- mathematics
- anthology-candidate
date: '2026-10-03'
source:
- LIT-623
- LIT-616
summary: >-
  MacKay (1992), [LIT-623](../literature.d/LIT-623.md), writes the evidence as best-fit likelihood
  times an Occam factor, the ratio of posterior to prior accessible volume,
  which under a Gaussian approximation is P(w_MP)(2π)^{k/2} det^{-1/2}A.
  When the likelihood dominates, det A grows as n^d, so the penalty is
  (d/2) log n. Watanabe's WBIC paper, [LIT-616](../literature.d/LIT-616.md), recovers that case
  (Lemma 3, Theorem 5) and states what replaces it when the Fisher
  information is degenerate at the optimum: λ log n − (m − 1) log log n,
  with λ the RLCT (Theorem 2). The regular half is derived. The singular
  half is a theorem the record holds only as cited, so this is Proposed.
  The volume reading of λ is in Watanabe's book, which is unread.
extended_by:
- THEORY-080
presupposed_by:
- THEORY-079
---
<!-- inactive-ok-file: LIT-354 — Deferred: Watanabe's book is unread; named as where the singular theorems are proved, nothing here rests on reading it -->
<!-- inactive-ok-file: THEORY-079 THEORY-080 — Proposed; an account that presupposes this one and one that extends it, named in Connections -->

# THEORY-087: The Bayesian complexity penalty grows as (d/2) log n in a regular model, where the curvature at the optimum sets the Occam factor, and as λ log n in a singular one, where λ is the real log canonical threshold and falls below d/2 when the prior is positive on the optimal set

## Source

- MacKay (1992), [LIT-623](../literature.d/LIT-623.md), read in [NOTE-471](../notes.d/NOTE-471.md): §2 (the evidence
  and the Occam factor, Eqs. 4–6), §5 (γ, Eqs. 22–24) and the Legendre
  demonstration (the "Occam hill").
- Watanabe (2012; JMLR 2013), [LIT-616](../literature.d/LIT-616.md), read in [NOTE-473](../notes.d/NOTE-473.md): Eq. 14
  (regular and singular), Eqs. 18–19 (the RLCT), Lemma 3, Theorems 2, 4
  and 5, Table 3 and the remark in §7.1.

## The claim, in two halves

**Regular models: the curvature at the optimum sets the penalty.** MacKay
shows that the evidence is the best-fit likelihood times an Occam factor.
That factor is "the ratio of the posterior accessible volume of H's
parameter space to the prior accessible volume", the factor by which the
hypothesis space collapses when the data arrive. With a k-dimensional
Gaussian posterior it is P(w_MP|H)(2π)^{k/2} det^{-1/2}A, where A is the
Hessian of the negative log posterior ([LIT-623](../literature.d/LIT-623.md), Eq. 6). For n
independent observations whose likelihood dominates the prior, A is about
n times the Fisher information at the optimum, so det A ∝ n^d and the log
Occam factor is −(d/2) log n plus a term that does not grow with n. MacKay
observes this scaling directly in his polynomial models: the right side of
the Occam hill falls as "k log N" ([LIT-623](../literature.d/LIT-623.md), §6). This is BIC's
penalty, and it is set by curvature. The determinant of the Fisher measures
how fast the posterior shrinks in each direction.

Watanabe reaches the same place from the other side. The truth is
*regular* for a model if the optimal parameter set is a single point and
the Hessian J(w0) of the average log loss is positive definite there.
J(w0) is the Fisher information when the truth is realizable
([LIT-616](../literature.d/LIT-616.md), Eq. 14). For a regular truth with a prior positive at w0,
the RLCT is d/2 and its multiplicity is 1 (Lemma 3, proved by one
blow-up). The proof of Theorem 5 performs MacKay's Gaussian integral, with
its (nβ)^{d/2} det J^{1/2} factor, and concludes WBIC = BIC + o_p(1). In
the regular case, then, the λ log n of singular learning theory is
MacKay's Occam factor at large n.

**Singular models: the RLCT sets the penalty.** When the optimal set is
not a point, or J(w0) is degenerate, no normal distribution approximates
the posterior. The Bayes free energy is then
F = nL_n(w0) + λ log n − (m − 1) log log n + O_p(1) ([LIT-616](../literature.d/LIT-616.md),
Theorem 2). Here λ is defined by resolving the singularities of the
Kullback–Leibler function: λ = min over charts of min_j (h_j + 1)/(2k_j)
(Eq. 18). In Watanabe's words in §7.1: "If a prior distribution is
positive at the optimal set of parameters, then RLCTs are smaller than d/2
in singular models". With Jeffreys' prior, which vanishes at
singularities, the inequality reverses and λ ≥ d/2.

**A worked case.** Reduced-rank regression with M = N = 6 and true rank 3
([LIT-616](../literature.d/LIT-616.md), §6, Table 3). Models of rank 1 and 2 cannot realize the
truth, and rank 3 realizes it without redundancy. Their λ is half their
dimension, H(M + N − H)/2: 5.5, 10 and 13.5. Models of rank 4, 5 and 6
realize it redundantly. Their RLCTs are 15, 16 and 17, below their
half-dimensions of 16, 17.5 and 18 by 1, 1.5 and 1. WBIC's two-temperature
estimates came out at 14.69, 15.74 and 16.53.

## What this does not say

- **It does not say that the singular half has been checked here.**
  Theorem 2 is quoted from Watanabe's book ([LIT-354](../literature.d/LIT-354.md)) and earlier papers,
  and the §7.1 remark is given with a citation. The record has read
  neither proof. Table 3 agrees with the theory, but its estimates come
  from WBIC, which is built on the same theory.
- **It does not give λ a volume reading.** MacKay's Occam factor is
  literally a volume ratio. The statement that λ is the exponent at which
  the prior volume of {w : K(w) < ε} shrinks with ε is in Watanabe's book
  and not in the paper read. So "the penalty is a volume ratio in
  both cases" is the natural reading, but the record holds only its
  regular half.
- **(d/2) log n is the large-n form, not the Occam factor itself.** At
  finite n MacKay's Gaussian factor charges ½ log(1 + λ_a/α) for each
  eigenvalue λ_a of the data Hessian against prior precision α. Directions
  the data do not determine cost almost nothing, and γ = Σ λ_a/(λ_a + α)
  counts the ones that do (Eq. 23). Below that scale the penalty is
  governed by the prior and not by curvature or by λ. [THEORY-080](THEORY-080.md)
  works this out for one structured prior.
- **It does not say a smaller penalty is a better model.** Watanabe's
  remark draws the trade-off himself. A λ below d/2 lets a larger model be
  used with smaller generalisation error, but it also means weaker
  consistency in finding the true model.
- **It is not about the relabelling degeneracies MacKay mentions.**
  Several equivalent maxima multiply the Gaussian evidence by their
  number ([LIT-623](../literature.d/LIT-623.md), §2). That is a constant, not a change of the
  log n slope. The singular case changes the slope.

## Connections

- **[THEORY-082](THEORY-082.md)** reads the same boundary from optimisation. Amari's
  efficiency theorem needs the Fisher at the optimum to be invertible,
  which is the regular half here.
- **[THEORY-079](THEORY-079.md)** presupposes this account, for a claim about Bayesian model reduction.
  It argues that BMR's Laplace scoring uses the regular half's penalty in
  the singular models it is applied to.
- **[THEORY-080](THEORY-080.md)** extends the regular half to a linearised network
  whose prior is set by its tangent kernel.
