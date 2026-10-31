---
number: 1253
status: Active
formerly:
- THEORY-tmp5nt8h
title: 'Treating the Bayesian evidence as a partition function with sample size as inverse temperature, the analogue of heat capacity, the rate at which leave-one-out predictive loss falls with sample size, equals half the parameter count in a regular model, as equipartition, and the real log canonical threshold in a singular one, falling below these where prior or discreteness fixes parameters; with multiplicity above one the approach to the singular value is only logarithmic, and the correspondence has no counterpart of physical current or dissipation'
version: 1
tags:
- learning-theory
- model-comparison
- thermodynamics
- probabilistic-modeling
date: '2026-10-31'
source:
- LIT-1882
summary: >-
  LaMont & Wiggins (2019), [LIT-1882](../literature.d/LIT-1882.md), read in [NOTE-1481](../notes.d/NOTE-1481.md): the
  learning capacity C = −N²∂_N U and its equipartition values (Table II,
  eqs. 16–18, 24, 28, 30). Active: the regular entries were checked by
  differentiation, and the singular case exactly in K = a²b² ([CASE-152](../cases.d/CASE-152.md)'s
  model), where C approaches λ = ½ as ½ − 1/log n, not with the O(1/N)
  error the paper states. The statistical "temperature" is a sample size,
  so nothing in the dictionary is a physical heat flow.
---

# THEORY-1253: Treating the Bayesian evidence as a partition function with sample size as inverse temperature, the analogue of heat capacity, the rate at which leave-one-out predictive loss falls with sample size, equals half the parameter count in a regular model, as equipartition, and the real log canonical threshold in a singular one, falling below these where prior or discreteness fixes parameters; with multiplicity above one the approach to the singular value is only logarithmic, and the correspondence has no counterpart of physical current or dissipation

## Source

LaMont & Wiggins (2019), [LIT-1882](../literature.d/LIT-1882.md), §§II–III.C, Tables I–II, eqs.
(4)–(30) and appendices A3–A4, read in [NOTE-1481](../notes.d/NOTE-1481.md) from arXiv
1706.01428v5. The singular asymptotics are Watanabe's, cited there, as in
[THEORY-087](THEORY-087.md).

## What was actually shown

**The dictionary.** Z(xᴺ) = ∫ dθ ϖ(θ) e^{−NĤ(θ)} (eq. 4): parameters as
states, empirical cross-entropy as energy, prior as density of states, N
as inverse temperature. Then F = −N⁻¹ log Z, U = ∂_N(NF), C = −N²∂_N U,
S = N(U − F) (Table I). U is the leave-one-out cross-validation loss,
using a finite difference in N (eqs. 11–12, A8–A9).

**Equipartition.** In a regular K-parameter model,
F = H₀ + (K/2N) log(N/N₀), U = H₀ + K/2N and C = K/2 (Table II, eq. 17),
term for term the free particle's E₀ + (K/2β) log(β/β₀). Checked by
differentiation.

**Singular models.** With F = H₀ + (γ/2N) log N, C = γ/2 (eq. 18). The
paper's γ is 2λ in Watanabe's convention (F_n = nS + λ log n), so C → λ.

**Freeze-out.** C falls below K/2 when the prior dominates at small N,
C = K/(2(1 + N₀/N)²) (eq. 24); when a parameter is discrete and resolved
at large N (eq. 30); and near a singular point of a two-component
exponential mixture (C = 0.61 against 1.5 at N = 100, eq. 28). It can also
exceed K/2: the uniform endpoint model has C = 1 for one parameter
(appendix C2).

**The logarithmic approach (my check).** Watanabe's free energy has a
further −(m − 1) log log n term, which Table II drops. With it,
C = λ − (m − 1)/log n + …. For the deterministic part of the free energy
of K = a²b² with a uniform prior on [0, 1]² (λ = ½, m = 2; [CASE-152](../cases.d/CASE-152.md)'s
model), exactly: C = 0.325, 0.375, 0.403, 0.433, 0.449, 0.465 at
n = 10², 10³, 10⁴, 10⁶, 10⁸, 10¹², against ½ − 1/log n = 0.283, 0.355,
0.391, 0.428, 0.446, 0.464.

**What could have failed.** The learning capacity of a singular model
could have kept the regular value K/2. It does not, and departs from it in
the direction of the RLCT.

## What this does not say

- **That inference is thermodynamics.** The temperature is a sample size,
  the energy an empirical loss. There is no dynamics, so there are no
  currents, no entropy production and no housekeeping heat. The A14
  analogy between SLT's e^{−nK} and a physical e^{−ΩV} is exact as a
  statement about concentration of a Gibbs-form measure. It is silent on
  the dissipative structure that maintained physical states carry
  ([THEORY-1264](THEORY-1264.md), [THEORY-1265](THEORY-1265.md)).
- **That the learning capacity is the singular penalty itself.** It is its
  second derivative in N. For m > 1 it reaches λ only logarithmically, so
  at practical n a measured C is not λ (0.40 against 0.5 at n = 10⁴ in the
  example).
- **That sloppiness in large networks is freeze-out.** The authors
  "speculate" this (§I.A); their evidence is three toy models.
- **Anything about the GPI prior.** Its AIC limit and its treatment of the
  Lindley–Bartlett paradox are in [NOTE-1481](../notes.d/NOTE-1481.md) and are not part of this
  claim.
- **The fluctuation part.** My check computes only the deterministic part
  of the free energy; data fluctuations add terms the check does not
  cover.
