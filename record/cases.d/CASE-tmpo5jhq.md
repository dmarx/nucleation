---
status: Proposed
title: 'The five conditions on an effective description, computed exactly for linear coarse-grainings of linear Gaussian VAR(1) and VAR(2) models under one declared regime: a construction for every presence-absence configuration that three proved entailments allow, sixteen of thirty-two in VAR(1) and twenty-two in VAR(2) at zero tolerance, and none of the forbidden ones among 6,000 random sparse models'
version: 1
standing: documented
kind: executed-study
tags:
- mathematics
- complex-systems
- information-theory
date: '2026-11-22'
bears_on:
- QUESTION-252
line:
- formal-apparatus
summary: >-
  Run on 2026-11-22 for [LEAD-173](../leads.d/LEAD-173.md) (scratch/studies/lead-173/, on the branch
  claude/lead-173-five-conditions). With target, projection, metric,
  horizon and budget declared, every configuration of predictive
  sufficiency (P), dynamical independence (D), memory closure (M),
  approximation fidelity (A) and tractability (C) that the entailments
  D ⇒ M (VAR(1) only), P ∧ D ∧ M ⇒ A and, at zero tolerance, A ⇒ P allow
  has an explicit witness, checked from exact stationary covariances, and
  a random search found no model in a forbidden cell. The result is
  [CLAIM-tmp186gy](../claims.d/CLAIM-tmp186gy.md); the target-is-Y alternative is [CLAIM-tmp9xo66](../claims.d/CLAIM-tmp9xo66.md). The
  wording is the assistant's (Claude, in this session); adopting it is the
  owner's call.
---
<!-- inactive-ok-file: CLAIM-tmp186gy CLAIM-tmp9xo66 — new; the claims filed from this study -->

# CASE-tmpo5jhq: The five conditions on an effective description, computed exactly for linear coarse-grainings of linear Gaussian VAR(1) and VAR(2) models under one declared regime: a construction for every presence-absence configuration that three proved entailments allow, sixteen of thirty-two in VAR(1) and twenty-two in VAR(2) at zero tolerance, and none of the forbidden ones among 6,000 random sparse models

## The case

**The class.** Stable, stationary linear Gaussian VAR(p),
X_t = Σ_k A_k X_{t−k} + ε_t, ε_t ~ N(0, Σ), Σ ≻ 0, for p = 1 and p = 2,
worked in the companion state, which carries the full past. A description
is a linear coarse-graining Y_t = LX_t of dimension m. VAR(2) matters
because its companion form is a VAR(1) whose noise is singular.

**The declared regime** ([TERM-065](../terms.d/TERM-065.md)), each choice the lead left open:

- **Target.** Z_{t+1} = GX_{t+1}, a declared linear functional outside Y.
  Not Y's own future: with that target P is D and M together by
  definition ([CLAIM-tmp9xo66](../claims.d/CLAIM-tmp9xo66.md)), the collapse A3 warned of ("P and D must
  have different conditioning sets").
- **P.** Y_t, the current coarse value, is sufficient for Z_{t+1} against
  the full past: E[Z_{t+1} | X⁻] = E[Z_{t+1} | Y_t]. Defect: the relative
  excess mean squared error of the best predictor from Y_t.
- **D.** Y's own past is sufficient for Y_{t+1} against the full past
  ([THEORY-733](../theory.d/THEORY-733.md)). Defect: the transfer entropy from X to Y, from the
  Kalman predictor of the companion state given Y's past, checked against
  a 60-lag regression.
- **Projection, for M.** Mori's, onto span(Y_t) in L² of the stationary
  law. M holds iff every Mori–Zwanzig memory kernel
  P K (QK)^{j−1} Q K P vanishes, equivalently iff R(k) = Ω^k R(0) for
  all k with Ω = R(1)R(0)⁻¹ ([CLAIM-397](../claims.d/CLAIM-397.md)'s criterion, for vector Y). The
  two tests agreed on 40 random models.
- **Metric, horizon and tolerance, for A.** The memoryless reduced model
  Ẑ_{t+k} = HΩ^{k−1}Y_t, H = Cov(Z_{t+1}, Y_t)R(0)⁻¹, has relative excess
  mean squared error over E[Z_{t+k} | X⁻] at most ε for every
  k = 1, …, h. Horizon h = 2, the shortest at which A is not P.
  Tolerance ε = 0, with ε = 0.01 as the alternative. Measured against the
  optimal predictor, not against the realized future, so that A is
  fidelity of the description and not the system's noise.
- **Budget, for C.** The reduced model's state, Y, has m ≤ b = 2. In this
  class every quantity is polynomial-time, so the dimension a user must
  carry is the budget that separates descriptions of one system. A sample
  budget would make C a parameter of A, as [CLAIM-401](../claims.d/CLAIM-401.md) reads it.

**The constructions.** Independent blocks stacked block-diagonally, so they
are uncorrelated at every lag: an autonomous AR(1); [CLAIM-389](../claims.d/CLAIM-389.md)'s pair
A = [[0.5, 0.4], [0, 0.3]], Σ = I − AAᵀ (D fails, M holds, 0.1200 nats);
a loop A = [[0.5, 0.4], [0.4, 0.3]] (D and M fail); an autonomous AR(2)
Y_t = 0.5Y_{t−1} + 0.3Y_{t−2} + ε (D holds, M fails, kernels 0.147 and
0.0315 as [QUESTION-252](../questions.d/QUESTION-252.md) records); a coordinate that Y drives and that does
not drive Y; and a copy row Z_{t+1} = (part of Y_t) + noise, which makes P
hold. A target that reads only an AR(1) part of a two-dimensional Y lets P
and A hold exactly while D or M fails in the other part. Appending
independent AR(1) coordinates to Y leaves P, D, M and A unchanged and
switches C off. For ε > 0, a leak of 0.05 from an unobserved AR(1) into
the target puts P's defect at 0.0013, below ε.

**Results** (scratch/studies/lead-173/results.md):

| regime | configurations allowed | witnessed | leave-one-out: P D M A C |
|---|---|---|---|
| VAR(1), ε = 0 | 16 of 32 | all | no yes no no yes |
| VAR(1), ε = 0.01 | 22 | all | yes yes no no yes |
| VAR(2), ε = 0 | 22 | all | no yes yes no yes |
| VAR(2), ε = 0.01 | 30 | all | yes yes yes no yes |

The defects in the witnesses that fail a condition are all at least 0.03
(A) and 0.09 (P), except the deliberate leaks, so no cell turns on
numerical noise. Of 3,000 random sparse VAR(1) and 3,000 VAR(2) models,
none fell in a forbidden cell and none had a defect between 10⁻⁹ and 10⁻⁶;
they reached 16 and 22 of the allowed cells. 94 pytest checks pass.

## What it can show

That under this regime the three entailments are the only ones: every
other configuration is realized, so the table is complete for the class.
It is documented in that every number is computed from exact covariances
and can be rerun in a minute (the study's README).

It cannot show what the table is under other declarations. A target equal
to Y, a horizon set that leaves out k = 1, a metric against the realized
future, or a sample budget each change it, and the claims say how. It says
nothing about nonlinear models, state-space models with observation noise,
or nonlinear coarse-grainings.
