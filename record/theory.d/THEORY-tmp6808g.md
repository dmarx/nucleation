---
status: Proposed
promote_when: >-
  A second reading of Theorem 4, or an independent restatement read by the
  record, confirms that for real Gaussian spiked covariance with
  N/n → γ ∈ (0, 1), a simple spike ℓ above 1 + √γ has sample-eigenvector
  squared overlap tending almost surely to
  (1 − γ/(ℓ − 1)²)/(1 + γ/(ℓ − 1)), and that at or below 1 + √γ the
  overlap tends to zero.
title: "Paul proves that for real Gaussian samples with a spiked covariance and fewer variables than samples, the sample eigenvector of a simple spike above 1 + √γ has a squared overlap with the population eigenvector tending to (1 − γ/(ℓ − 1)²)/(1 + γ/(ℓ − 1)), and that below the threshold the overlap tends to zero"
version: 1
tags:
- mathematics
- mathematical-statistics
date: '2026-11-21'
source:
- LIT-tmpxru3g
summary: >-
  Paul (2007), [LIT-tmpxru3g](../literature.d/LIT-tmpxru3g.md), read in [NOTE-tmp5f8al](../notes.d/NOTE-tmp5f8al.md) (statements only). The
  eigenvector half of the spiked transition, for real Gaussian data with
  γ < 1, which [CLAIM-tmp5y856](../claims.d/CLAIM-tmp5y856.md) and [CASE-tmp59xy5](../cases.d/CASE-tmp59xy5.md) state and the BBP paper
  does not prove ([ARG-tmpnwmcr](../arguments.d/ARG-tmpnwmcr.md)). Proposed until Theorem 4 is confirmed.
---
<!-- inactive-ok-file: NOTE-tmp5f8al — Skimmed; the reading this account is filed from -->
<!-- inactive-ok-file: CLAIM-tmp5y856 CASE-tmp59xy5 ARG-tmpnwmcr — Proposed; the entries this reading carries, and the argument of 2026-11-21 -->

# THEORY-tmp6808g: Paul proves that for real Gaussian samples with a spiked covariance and fewer variables than samples, the sample eigenvector of a simple spike above 1 + √γ has a squared overlap with the population eigenvector tending to (1 − γ/(ℓ − 1)²)/(1 + γ/(ℓ − 1)), and that below the threshold the overlap tends to zero

## Source

Paul, Statistica Sinica 17 (2007): 1617–1642. [LIT-tmpxru3g](../literature.d/LIT-tmpxru3g.md), read in
[NOTE-tmp5f8al](../notes.d/NOTE-tmp5f8al.md).

## The account

Real Gaussian data with Σ = diag(ℓ_1, …, ℓ_M, 1, …, 1), S = (1/n)XXᵀ,
N/n → γ ∈ (0, 1). For a simple ℓ_ν > 1 + √γ, the sample eigenvector p_ν
satisfies |⟨p_ν, e_ν⟩|² → (1 − γ/(ℓ_ν − 1)²)/(1 + γ/(ℓ_ν − 1)) almost
surely; for ℓ_ν ≤ 1 + √γ the overlap tends to zero (Theorem 4). With
β = ℓ − 1: (1 − γ/β²)/(1 + γ/β), which vanishes at β = √γ, the same point
where the eigenvalue leaves the bulk.

## What this does not say

- Not the case γ ≥ 1.
- Not non-Gaussian or complex data.
- Not a repeated spike's eigenvectors, only a simple one's.
