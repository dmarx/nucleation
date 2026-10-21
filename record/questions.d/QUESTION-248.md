---
number: 248
status: Answered
formerly:
- QUESTION-tmphwjsk
title: 'In a stable linear Gaussian VAR(1), does a scalar linear coarse variable whose reduced dynamics carry memory admit an exact finite-dimensional Markovian augmentation?'
version: 1
tags:
- complex-systems
- mathematics
date: '2026-10-21'
line: distributed-agency
refines:
- QUESTION-222
summary: >-
  [QUESTION-222](QUESTION-222.md) for the linear Gaussian class, split off under [ADR-049](../decisions.d/ADR-049.md) and
  answered by [CLAIM-398](../claims.d/CLAIM-398.md). Yes: a scalar coarse variable Y = LX of a VAR(1)
  on ℝⁿ is an ARMA process of orders at most (n, n − 1). Its
  Mori–Zwanzig memory is non-zero at every lag in general, but finitely
  many coordinates, built from Y's own past and innovations, carry it
  exactly. Other classes, error in terms of the eliminated spectrum, and
  the ruling on levels stay with [QUESTION-222](QUESTION-222.md).
answered_by:
- CLAIM-398
---

# QUESTION-248: In a stable linear Gaussian VAR(1), does a scalar linear coarse variable whose reduced dynamics carry memory admit an exact finite-dimensional Markovian augmentation?

## Answer

Yes. [CLAIM-398](../claims.d/CLAIM-398.md) (Active, demonstrated): in a stable linear Gaussian VAR(1)
on ℝⁿ, a scalar linear coarse variable Y = LX is, in its own law, an
ARMA process of orders at most (n, n − 1). Its Mori–Zwanzig memory is
non-zero at every lag in general. Still, finitely many coordinates, all
functions of Y's own past and innovations, carry it exactly, so the
prediction error of the augmentation is that of the optimal predictor,
with nothing added. The augmentation is the one [THEORY-257](../theory.d/THEORY-257.md)'s criterion
conditions on.

[CLAIM-397](../claims.d/CLAIM-397.md) adds that, for any scalar stationary process, the memory
kernels are fixed by the autocovariance alone. So an own-history
representation exists in second order for every stationary variable, and
having one marks no level.

## What it leaves to [QUESTION-222](QUESTION-222.md)

- **Other classes.** Nonlinear dynamics, noisy or slow eliminated
  variables, and vector coarse variables. [THEORY-762](../theory.d/THEORY-762.md) and [THEORY-773](../theory.d/THEORY-773.md) cover
  two further cases.
- **Error in terms of the eliminated spectrum.** In [CLAIM-398](../claims.d/CLAIM-398.md)'s one
  example, the cost of truncating to AR(p) fell at a rate set by the
  moving-average zero, not by the spectrum of the eliminated dynamics.
- **The ruling** on whether the record's level criteria apply to the
  augmented state or to the instantaneous one.
