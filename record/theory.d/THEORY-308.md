---
number: 308
status: Proposed
formerly:
- THEORY-tmpapktz
promote_when: >-
  A read proof, in Belghazi et al. corrected or in an independent source,
  that closes the two gaps found in NOTE-828. First, the
  approximation lemma when the joint distribution vanishes on a set of
  positive product measure, so that the log density ratio is −∞ there.
  Second, the estimation lemma stated as almost-sure convergence rather
  than with a deterministic N. Refuted by a pair of distributions on a
  compact domain, with Lebesgue densities and finite mutual information,
  for which the empirical Donsker–Varadhan supremum over every compact
  family of continuous networks stays bounded away from the mutual
  information as n grows. What cannot settle it: estimator benchmarks on
  Gaussians, which measure what gradient training reaches, not the
  empirical supremum the theorem is about.
title: 'The neural Donsker–Varadhan estimator of mutual information is strongly consistent as an extremum estimator over a compact family of critics, and its uniform deviation from the population bound is controlled by the parameter count, not the data dimension'
version: 1
tags:
- information-theory
- mathematical-statistics
date: '2026-10-14'
source:
- LIT-256
- LIT-246
summary: >-
  Belghazi et al. (2018), [LIT-256](../literature.d/LIT-256.md), §3.3 and App. 8.2.2–8.2.3, read in
  [NOTE-828](../notes.d/NOTE-828.md). On a compact domain with Lebesgue densities, the
  supremum of the Donsker–Varadhan bound over some compact network family
  is within any η of the mutual information, and the empirical supremum
  converges to the population one almost surely. Uniform deviation ε needs
  Õ(d log d/ε²) samples for d parameters, under bounded, Lipschitz
  critics. The guarantee is for the exact empirical maximizer, not for
  gradient training. The finite-sample estimate is not a bound (Poole et
  al., [LIT-246](../literature.d/LIT-246.md)), and the proof has two gaps a reading found.
---
<!-- inactive-ok-file: THEORY-237 — Proposed; the account of the bound family this estimator belongs to, named in Connections -->

# THEORY-308: The neural Donsker–Varadhan estimator of mutual information is strongly consistent as an extremum estimator over a compact family of critics, and its uniform deviation from the population bound is controlled by the parameter count, not the data dimension

## Source

Belghazi et al. (2018), [LIT-256](../literature.d/LIT-256.md), Def. 3.1–3.2, Lemmas 1–2, Theorems 2–3,
and App. 8.2.2–8.2.3 (Eqs. 27–53), read in [NOTE-828](../notes.d/NOTE-828.md). Poole et al.
(2019), [LIT-246](../literature.d/LIT-246.md), §2.2, read in [NOTE-739](../notes.d/NOTE-739.md), for what the finite-sample
estimate is not.

## What was actually shown

MINE estimates I(X;Z) by Î_n = sup_{θ∈Θ} E_{P_n}[T_θ] −
log E_{Q_n}[e^{T_θ}], with P = P_XZ, Q = P_X⊗P_Z and P_n, Q_n their
empirical measures (Eq. 11). The setting: Ω = X × Z a compact subset of
R^d, all measures absolutely continuous with respect to Lebesgue measure,
feedforward networks with continuous activations, and Θ compact.

1. **Approximation (Lemma 3).** For every η > 0 some network family
   satisfies |I(X;Z) − I_Θ(X;Z)| ≤ η, where I_Θ is the population supremum.
   The proof bounds the gap by E_P|T* − T| + E_Q|e^{T*} − e^T|, with
   T* = log dP/dQ, and applies universal approximation in L¹(P + Q),
   truncating T* above at M.
2. **Estimation (Lemma 4).** For a fixed compact family, T_θ is uniformly
   bounded, log is Lipschitz on the range of E[e^{T_θ}], and the uniform law
   of large numbers makes the empirical supremum converge to I_Θ.
3. **Strong consistency (Theorem 2).** For every ε a family and an N exist
   with |I − Î_n| ≤ ε for n ≥ N almost surely. The family depends on ε.
4. **Sample complexity (Theorem 3).** If T_θ is L-Lipschitz in θ,
   |T_θ| ≤ M, e^{T_θ} ≤ M and ‖θ‖ ≤ K in R^d, then
   Pr(|Î_n − I_Θ| ≤ ε) ≥ 1 − δ once
   n ≥ 2M²(d log(16KL√d/ε) + 2dM + log(2/δ))/ε². The proof is Hoeffding,
   a covering of the parameter ball and a union bound.

What could have failed: the proofs could have needed the data dimension
in the rate, or a density for the joint. They need neither. The rate is
in the number of parameters, and only samples enter.

## What this does not say

- **Nothing about what training reaches.** Every statement is about the
  exact supremum over θ. The paper treats the mini-batch gradient's bias
  only with a moving-average heuristic, and proves nothing about
  convergence of gradient ascent.
- **Not that a finite-sample estimate is a lower bound.** A Monte-Carlo
  Donsker–Varadhan estimate is neither an upper nor a lower bound ([LIT-246](../literature.d/LIT-246.md),
  §2.2). Only the population I_Θ is a lower bound (Eq. 9).
- **Not a useful rate at high mutual information.** Theorem 3 controls
  the deviation from I_Θ, not from I. It assumes bounded critics, which
  excludes the unbounded log ratio that large MI needs. Its constants grow
  like e^{2M}. No theorem joins the approximation error to the sample
  size.
- **Not proved as stated, in two places** ([NOTE-828](../notes.d/NOTE-828.md)).
  - Lemma 3's proof needs T* finite and Q-integrable where it is
    approximated. When P_XZ vanishes on a set of positive P_X⊗P_Z measure,
    T* = −∞ there and the written bound fails. A lower truncation would
    probably repair it, but none is given.
  - Lemma 4 is stated with one deterministic N after which the deviation
    is small with probability one. The uniform law gives almost-sure
    convergence with a sample-dependent N. The weaker statement suffices
    for consistency.
- **Not beyond compact domains with Lebesgue densities.** Discrete,
  mixed or unbounded variables are outside the proof.

## Connections

- **[THEORY-237](THEORY-237.md)** holds the family of bounds this estimator maximizes, the
  Donsker–Varadhan bound being one relaxation of the unnormalized
  Barber–Agakov bound. This account adds the statistical side: whether
  maximizing that bound over a network class and a sample converges to
  the mutual information.
- **[THEORY-006](THEORY-006.md)** cites the same paper for the identity behind it: MI is
  the expected log Radon–Nikodym derivative, and the bound is tight at
  that derivative plus a constant. The consistency proof uses exactly
  that critic, T* = log dP/dQ, with E_P[T*] = I and E_Q[e^{T*}] = 1.
