---
number: 473
status: Read
formerly:
- NOTE-tmp3drtl
paper: 'LIT-616'
title: 'A Widely Applicable Bayesian Information Criterion'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read in full from arXiv 1208.6338v1 (30 pages): §§1–8, all proofs in
    §5, the example resolution of K(a, b, c) = (ab + c)² + a²b⁴, Tables
    1–4, and the references. The text layer kept the mathematics legible
    enough to follow the proofs. The JMLR version (2013) was not compared.
    Theorems 1 and 2 are stated here with proofs deferred to Watanabe
    (2009, 2010b); this reading takes them as stated and has not checked
    them.
date: '2026-10-03'
summary: >-
  The Bayes free energy of a singular model is nL_n(w0) + λ log n − (m − 1)
  log log n + O_p(1), with λ the RLCT. The posterior mean of nL_n(w) at
  inverse temperature 1/log n (WBIC) reproduces the first two terms
  without knowing λ, equals BIC for regular models, and two temperatures
  estimate λ. In reduced-rank regression WBIC chose the true rank 100/100
  times, and estimated RLCTs within about 0.5 of theory.
---

<!-- inactive-ok-file: LIT-354 — Deferred: the book is unread; named as the source of Theorems 1 and 2, which this paper restates -->

# NOTE-473: A Widely Applicable Bayesian Information Criterion

## Contribution

Before this paper, singular learning theory said the Bayes free energy of a
singular model grows as λ log n. But λ depends on the unknown true
distribution, so the result could not be used for model selection. WBIC is
a quantity computable from one posterior sample at a tempered inverse
temperature. It has the same asymptotic expansion as the free energy to
the λ log n term, for singular and unrealizable models alike, and reduces
to BIC for regular ones. Comparing two temperatures also gives a consistent
estimator of λ.

## Key insight

The free energy is the integral over inverse temperature from 0 to 1 of
the posterior mean log loss at that temperature (proof of Theorem 3). The
mean value theorem says one temperature β* reproduces it exactly. The
asymptotics say β* log n → 1. So instead of integrating over all
temperatures, evaluate at β = 1/log n. At that temperature the singular
geometry, through λ, enters the posterior mean of nK_n(w) as λ/β = λ log n.

## Assumptions

- **Fundamental Conditions (1)–(4), §3.** W is compact with an analytic
  boundary. The prior is φ1φ2, with φ1 ≥ 0 analytic and φ2 > 0 smooth.
  w ↦ f(x, w) = log p0(x)/p(x|w) extends to an L^s(q)-valued analytic
  function with s ≥ 6. Near the optimum, E[f] ≥ c E[f²] (Eq. 15), which
  holds if the truth is realizable by or regular for the model, but not in
  general for unrealizable singular cases.
- **A unique optimal distribution** p0 (all optimal parameters give the same
  density), although the set W0 of optimal parameters may be an analytic
  set with singularities.
- **Definitions (Eq. 14).** The truth is *regular* for the model if W0 is a
  single point and the Hessian J(w0) of L(w) is positive definite; J(w0) is
  the Fisher information when the truth is realizable. Otherwise it is
  *singular*.

## Key results

- **Theorem 1 (standard representation; from the book's Theorem 6.1).**
  There is a real analytic manifold M and a proper analytic map g with
  K(g(u)) = u^{2k}, f(x, g(u)) = u^k a(x, u), and φ(w)dw = b(u)|u^h| du in
  each local chart.
- **Definition (Eqs. 18–20).** λ = min_α min_j (h_j + 1)/(2k_j). m is the
  maximum number of j attaining it. The parity Q(K, φ) is odd if, in every
  essential chart, some attaining coordinate has odd k_j along the prior's
  support.
- **Worked example (p. 9).** K(a, b, c) = (ab + c)² + a²b⁴ (a neural network
  from the book's Example 1.6), resolved in four charts: λ = 3/4, m = 1,
  parity even.
- **Lemma 3.** Regular truth, w0 interior, φ(w0) > 0 ⇒ λ = d/2, m = 1, odd
  parity.
- **Theorem 2 (from earlier work).** F = nL_n(w0) + λ log n − (m − 1)
  log log n + R_n, with R_n converging in law.
- **Theorem 3.** E_w^β[nL_n(w)] decreases in β, and there is a unique
  β* ∈ (0, 1) with F = E_w^{β*}[nL_n(w)].
- **Theorem 4 (main).** For β = β0/log n, E_w^β[nL_n(w)] = nL_n(w0) +
  λ log n/β0 + U_n √(λ log n/(2β0)) + O_p(1), where U_n has mean zero and
  tends to a Gaussian. If the truth is realizable, E[U_n²] < 1.
- **Corollaries.** (1) Odd parity ⇒ U_n = 0. (2) β* log n = 1 +
  U_n/√(2λ log n) + o_p(1/√log n). (3) [E^{β1} − E^{β2}]/(1/β1 − 1/β2) → λ
  in probability.
- **Theorem 5.** Regular truth ⇒ WBIC = nL_n(ŵ) + (d/2) log n + o_p(1), even
  if the truth is unrealizable.
- **Experiment (§6).** Reduced-rank regression, M = N = 6, true rank
  H0 = 3, n = 500, 100 data sets, Metropolis sampling at β = 1/log n.
  WBIC chose H = 3 in all 100 (Table 2). RLCT estimates from β1 = 1/log n
  and β2 = 1.5/log n against theory, for H = 1–6: 5.50 vs 5.5, 9.93 vs
  10, 13.44 vs 13.5, 14.69 vs 15, 15.74 vs 16, 16.53 vs 17 (Table 3).
  The gaps are largest where m = 2, attributed to the log log n term.
- **§7.1.** E[WAIC] = E[G] + O(1/n²) (proved elsewhere) and E[WBIC] = E[F] +
  O(log log n) (this paper). WAIC and WBIC reduce to AIC and BIC for
  regular, realizable models.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The Bayes free energy of a singular model grows as λ log n − (m − 1) log log n, with λ the RLCT, not d/2 | strong, as a cited theorem; proved in the book and earlier papers, not here | Theorem 2 |
| C2 | WBIC has the same asymptotic expansion as the free energy to the λ log n term, under the Fundamental Conditions | strong (proof) | Theorem 4, §5.7 |
| C3 | WBIC equals BIC up to o_p(1) for regular models, realizable or not | strong (proof) | Theorem 5, §5.11 |
| C4 | The RLCT can be estimated consistently from posterior means at two temperatures | strong (proof); demonstrated on one model family | Corollary 3, Table 3 |
| C5 | WBIC selects the true model in practice | weak to moderate: one experiment, 100 data sets, one model family whose RLCTs are known | Table 2 |
| C6 | With a prior positive on the singularities, λ < d/2, so singular Bayes models generalise better than parameter count suggests and select models less consistently | moderate: stated, with citations; not shown here | §7.1 remark |
| C7 | The parity of a model is a birational invariant in general | conjecture (proved only for realizable truths, Lemma 2) | §3 |

## Concepts

- **regular / singular**: the truth is regular for the model if the optimum
  is a single point with positive-definite J(w0), the Fisher information
  when realizable. Singular otherwise.
- **realizable**: q(x) = p0(x), the truth is in the model.
- **Bayes free energy** F: minus the log marginal likelihood, Eq. 2.
- **real log canonical threshold (RLCT)** λ, with **multiplicity** m:
  birational invariants of (K, φ), Eqs. 18–19.
- **inverse temperature** β: the power on the likelihood in the tempered
  posterior, Eq. 5.
- **parity** Q(K, φ): odd or even, Eq. 20. It decides whether the
  fluctuation term U_n vanishes.

## Connections

- **Watanabe (2009), [LIT-354](../literature.d/LIT-354.md).** The source of Theorem 1 (Theorem 6.1 there),
  Theorem 2 (with Watanabe 2001a, 2010b), the empirical-process results of
  Theorems 5.9–6.3 used in the proofs, and Main Theorem 6.4.
- **Schwarz (1978)** for BIC; **Drton (2010)** for a two-step method using
  theoretical RLCTs; **Aoyagi & Watanabe (2005)** for the reduced-rank RLCTs
  of Table 3.
- **MacKay ([LIT-623](../literature.d/LIT-623.md)).** The Gaussian Occam factor gives (d/2) log n.
  Theorem 5 is the regular case, Theorem 4 the singular one.

## Bearing on the record

- It is the record's lawful reading of singular learning theory's core
  results, so [LIT-354](../literature.d/LIT-354.md)'s status note names it as the substitute.
- **THEORY candidate.** "In a singular model the Bayesian complexity penalty
  is λ log n, with λ the RLCT, and λ ≤ d/2 when the prior is positive at
  the singularities." Sources: this paper and MacKay ([LIT-623](../literature.d/LIT-623.md)). It
  would join model comparison to Fisher geometry, since singularity is
  degeneracy of the Fisher information.
- **Anthology.** The deep-learning uses of the RLCT ([ANTH-LIT-541](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-541.md),
  [ANTH-LIT-542](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-542.md)) are held there. This paper is flagged anthology-candidate.

## Limitations

- **Conditions.** Eq. 15 can fail when the truth is both unrealizable and
  singular, and the paper studies only the case where it holds.
- **Asymptotic.** The O_p(√log n) fluctuation term and the log log n term
  are not small at moderate n: Table 3's RLCT estimates fall short of
  theory by up to 0.47.
- **One experiment** in one model family with odd parity (U_n = 0). Even-
  parity models, where the fluctuation term is live, are not tested.
- **WBIC vs WAIC** in singular model selection is named as future work.

## Open questions

- Is the parity a birational invariant in general? This is conjectured,
  and reduced to finding, for any analytic K, a model with K as its KL
  divergence.
- Which free-energy estimator (all-temperatures, importance sampling,
  two-step, WBIC) is best under which conditions? Table 4 compares them
  qualitatively and leaves it open.

## Corrections

- none (there was no seed)
