---
number: 308
status: Active
formerly:
- THEORY-tmpapktz
title: 'The neural Donsker–Varadhan estimator of mutual information is strongly consistent as an extremum estimator over compact families of critics, and, for critics bounded by M and L-Lipschitz in their d parameters, its uniform deviation from the population bound needs a number of samples set by d, M, L and the parameter radius, not by the data dimension'
version: 2
history:
- version: 2
  date: '2026-10-19'
  note: >-
    Narrowed and promoted, carrying out the promotion audit's decision for
    THEORY-308 (batch 025, ADR-047 v2). The promote_when asked for a proof
    closing NOTE-828's two gaps. Both close, by a re-derivation written out
    in the decision file and summarised in the note of 2026-10-19 below.
    The title now names the assumptions of the sample-complexity clause.
    promote_when is removed.
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

# THEORY-308: The neural Donsker–Varadhan estimator of mutual information is strongly consistent as an extremum estimator over compact families of critics, and, for critics bounded by M and L-Lipschitz in their d parameters, its uniform deviation from the population bound needs a number of samples set by d, M, L and the parameter radius, not by the data dimension

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
- **Not proved as stated in the paper, in two places** ([NOTE-828](../notes.d/NOTE-828.md)).
  Both are repaired in the note of 2026-10-19 below.
  - Lemma 3's proof needs T* finite and Q-integrable where it is
    approximated. When P_XZ vanishes on a set of positive P_X⊗P_Z measure,
    T* = −∞ there and the written bound fails.
  - Lemma 4 is stated with one deterministic N after which the deviation
    is small with probability one. What holds is almost-sure convergence
    with a sample-dependent N, which suffices for consistency.
- **Not beyond compact domains with Lebesgue densities.** Discrete,
  mixed or unbounded variables are outside the proof.

## Note of 2026-10-19: the two gaps closed

Re-derived for the promotion audit (batch 025, [ADR-047](../decisions.d/ADR-047.md) v2). The full
steps are in the audit's decision file for THEORY-308.

- **Lemma 3 with a lower truncation.** Take T_M = max(−M, min(T*, M)).
  The negative part of T* is P-integrable whenever I is finite, since
  ∫_{p<q} p log(q/p) ≤ 1 by log x ≤ x − 1. So E_P[T_M] → I, and
  E_Q[e^{T_M}] → 1, both by dominated convergence (e^{T_M} ≤ dP/dQ + 1).
  Lusin's theorem, Tietze's extension and uniform approximation on the
  compact Ω then give a network within η of I, with one-point Θ.
- **Lemma 4 as almost-sure convergence.** {T_θ} is uniformly bounded and
  equicontinuous on compact Ω × Θ, hence totally bounded in sup-norm. The
  empirical measures converge weakly almost surely. That holds for i.i.d.
  marginal pairs and for the product of the two empirical marginals, and
  weak convergence is uniform over such a family. So
  Î_n → I_Θ almost surely, with a sample-dependent N.
- **The rate.** With |T_θ| ≤ M, L-Lipschitz in θ and ‖θ‖ ≤ K in ℝ^d,
  Hoeffding on a net of the parameter ball gives sup_θ |V_n − V| ≤ ε with
  probability 1 − δ once
  n ≥ 8 max(M², e^{4M})(d log(12KL(1 + e^{2M})/ε) + log(4/δ))/ε².
  For the product-of-marginals form, McDiarmid's inequality gives the
  same order. These are the record's constants. The paper's were not
  rechecked. The data dimension does not enter.

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
