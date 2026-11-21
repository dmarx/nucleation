---
number: 2149
status: Proposed
formerly:
- THEORY-tmp0zr7o
promote_when: >-
  A second reading of the theorems (Theorems 1.1–1.3, with (1.10) and
  (1.14)), or an independent restatement read by the record, confirms that
  for real or complex samples with i.i.d. standardized entries of finite
  fourth moment and finitely many fixed spikes, at any c > 0, each spike
  above 1 + √c gives a sample eigenvalue converging almost surely to
  α + cα/(α − 1), and that otherwise the top eigenvalue tends to the edge
  (1 + √c)².
title: "Baik and Silverstein prove that for real or complex samples with independent standardized entries of finite fourth moment and a population covariance that is the identity but for finitely many spikes, at any ratio of variables to samples c, each spike above 1 + √c gives its own sample eigenvalue converging almost surely to α + cα/(α − 1), and spikes at or below it leave the top eigenvalue at the bulk edge"
version: 1
tags:
- mathematics
- mathematical-statistics
date: '2026-11-21'
source:
- LIT-2988
summary: >-
  Baik and Silverstein (2006), [LIT-2988](../literature.d/LIT-2988.md), read in [NOTE-2245](../notes.d/NOTE-2245.md) (§1
  only). The real, non-Gaussian, any-ratio, every-spike version of the
  BBP threshold and outlier, for limits. The record's spiked-matrix claims
  rest on it where BBP's complex Gaussian top-eigenvalue result does not
  reach ([ARG-151](../arguments.d/ARG-151.md)). Proposed until the theorems are confirmed.
bears_on:
- QUESTION-510
---
<!-- inactive-ok-file: NOTE-2245 — Skimmed; the reading this account is filed from -->
<!-- inactive-ok-file: ARG-151 THEORY-2148 — Proposed; the argument and the neighbouring reading of 2026-11-21 -->

# THEORY-2149: Baik and Silverstein prove that for real or complex samples with independent standardized entries of finite fourth moment and a population covariance that is the identity but for finitely many spikes, at any ratio of variables to samples c, each spike above 1 + √c gives its own sample eigenvalue converging almost surely to α + cα/(α − 1), and spikes at or below it leave the top eigenvalue at the bulk edge

## Source

Baik and Silverstein, arXiv math/0408165 (2004); J. Multivariate Anal. 97
(2006). [LIT-2988](../literature.d/LIT-2988.md), read in [NOTE-2245](../notes.d/NOTE-2245.md) (§1).

## The account

Samples T^(1/2)Z, Z with i.i.d. entries of mean 0, variance 1 and finite
fourth moment, real or complex; p variables, n samples, p/n → c > 0; T the
identity but for finitely many fixed eigenvalues. Each population spike
α_j > 1 + √c produces sample eigenvalues converging almost surely to
α_j + cα_j/(α_j − 1), one per unit of its multiplicity (1.10). With one
spike, the top eigenvalue tends to (1 + √c)² if the spike is at most
1 + √c (1.14). In the record's notation, c = γ = D/N and α = 1 + β, this is
β > √γ and (1 + β)(1 + γ/β), at every γ and for each spike.

## What this does not say

- Not the fluctuations, which it leaves open; those are BBP's, for complex
  Gaussian samples ([THEORY-2148](THEORY-2148.md)).
- Not anything about eigenvectors.
- Not a number of spikes growing with p.
- Not models whose entries are not identically distributed, such as a
  mixture with a distinguished direction.
