---
number: 1056
status: Proposed
formerly:
- THEORY-tmp24sxe
promote_when: >-
  A theorem, for this outlier model (each offset exact with probability p,
  otherwise uniform and independent), that a polynomial-time estimator
  recovers the angles under the same success criterion the information
  bound uses (exact recovery of all angles, or a per-angle error
  probability), for p above c(L)·√(n/m) with c(L) depending only on L; or
  a proof that the eigenvector estimator's correlation with the truth is
  bounded away from zero exactly above p = Θ(1/√n) on the complete graph.
  More simulations at fixed n do not settle it, and neither does the ratio
  (5.34) as the paper states it, since it compares thresholds for an
  above-random correlation and for correct decoding.
title: 'In angular synchronization with outlier offsets, a polynomial-time spectral relaxation, the top eigenvector of the Hermitian matrix of measured phase offsets, recovers the angles once the share of good offsets exceeds about 1/√n on the complete graph, within a factor √((L − 1)/(2 log₂ L)) of the information bound that limits every algorithm, while exact maximum likelihood is a non-convex search costing O(mLⁿ) exhaustively; in this model the price of recovering the global configuration cheaply instead of optimally is a constant factor in evidence, which vanishes for L ≤ 6'
version: 1
tags:
- mathematics
- information-theory
- network-science
date: '2026-10-27'
source:
- LIT-1655
summary: >-
  Singer (2011), [LIT-1655](../literature.d/LIT-1655.md), §§2, 4 and 5, read in [NOTE-1224](../notes.d/NOTE-1224.md) from
  arXiv v2. The threshold p > 1/√n comes from a cited rank-one deformation
  theorem adopted to a non-Gaussian mixture and a heuristic comparison with
  random correlation, confirmed by simulation at n = 100 and 400; the
  near-optimality ratio compares it with an information bound for a
  different success criterion. Proposed for both steps. It does not say
  that recovery is cheap on every graph, under every noise model, or for
  fine angular resolution.
---
<!-- inactive-ok-file: CLAIM-475 — Proposed; the claim this bears on, cited as open -->

# THEORY-1056: In angular synchronization with outlier offsets, a polynomial-time spectral relaxation, the top eigenvector of the Hermitian matrix of measured phase offsets, recovers the angles once the share of good offsets exceeds about 1/√n on the complete graph, within a factor √((L − 1)/(2 log₂ L)) of the information bound that limits every algorithm, while exact maximum likelihood is a non-convex search costing O(mLⁿ) exhaustively; in this model the price of recovering the global configuration cheaply instead of optimally is a constant factor in evidence, which vanishes for L ≤ 6

## Source

Singer (2011), [LIT-1655](../literature.d/LIT-1655.md), §§1–2 (pp. 1–5), §4.1 (pp. 6–10), §5
(pp. 14–20) and §6 (pp. 21–22) of arXiv 0905.3174v2; read in
[NOTE-1224](../notes.d/NOTE-1224.md).

## What was actually shown

**The cheap method.** Hᵢⱼ = e^{iδᵢⱼ} on measured edges (1.6); its top
eigenvector maximizes z*Hz under the single constraint ‖z‖² = n, a
relaxation of the n unit-modulus constraints (2.4–2.5). Power iteration costs
O(n²) per step for dense H and O(m) for sparse H, with a number of steps that
"decreases with the spectral gap" (p. 5), not bounded in the text.

**The expensive one.** Maximum likelihood minimizes the number of violated
offsets (1.4), "a non-convex optimization problem in a huge parameter space"
(p. 3); "The exponential complexity of O(mLⁿ) of the exhaustive search for
the maximum likelihood makes it impractical even for moderate-scale
problems" (p. 20).

**The threshold of the cheap method.** On the complete graph, H = npzz* + R
with R zero-mean of entry variance 1 − p² (4.4–4.6). Adopting Féral and
Péché's rank-one deformation theorem, the top eigenvalue leaves the noise
bulk when np > √(n(1 − p²)) (4.8), and requiring the eigenvector's
correlation with the truth to beat 1/n gives p > 1/√n (4.13–4.16, p. 8).
Above it, E cos²α ~ 1/(1 + 1/(np²)) (4.24). Simulations at n = 100 and 400
agree (Table 4.1, p. 11): at n = 400 with 85% outliers, ρ₁ = 0.97 (p. 10).
Least squares fails where the eigenvector succeeds (Table 4.3, p. 15).

**The comparison.** With the per-angle information bound
p_c^ind = √((n/m)·log₂ L/(L − 1)) ([THEORY-1067](THEORY-1067.md)), on the complete
graph p_c^eig/p_c^ind = √((L − 1)/(2 log₂ L)) + o(1),
independent of n and m (5.34, p. 20). It is below 1 for L ≤ 6 and about 2.73
at L = 100. Citing the NP-hardness of approximating Max-2-Lin mod L within a
constant independent of L, the paper expects "an L-dependent gap similar to
(5.34) for any polynomial time algorithm" (p. 21).

**What could have come out otherwise.** The spectral threshold could have
scaled worse than the information bound in n or m, so that cheap recovery
needed asymptotically more evidence. On the paper's analysis it does not:
the gap is a function of L alone.

## What this does not say

- **That the threshold is proved.** §7 says random matrix theory was used
  "to prove" the method accurate (p. 22), but the theorem is adopted to a
  non-Gaussian mixture without its conditions being checked in the text, the
  threshold rests on the heuristic comparison (4.13), and the correlation on
  a first-order expansion.
- **That the comparison is like for like.** p_c^eig is a threshold for
  above-random correlation, p_c^ind for correct decoding; the paper concedes
  the difference for L = 2 (pp. 18–19) and reads (5.34) as near-optimality
  anyway.
- **That it holds on other graphs.** On the general graph the condition
  (4.36) is stated by analogy, and its S² instance (4.41) is "far from being
  tight" (p. 13); the observed jumps follow √(n/(2m)) (p. 14).
- **That it holds under other noise.** Only exact-or-uniform offsets are
  analysed. NP-hardness, which §6 uses to expect a gap for every polynomial
  algorithm, is a worst-case statement; the model is average-case.
- **That recovering a global configuration from pairwise evidence is cheap
  in general.** It is so in this model, at coarse resolution. For
  [CLAIM-475](../claims.d/CLAIM-475.md), which cites the paper for the cost of such recovery, the
  paper's finding is that here the binding resource is evidence
  ([THEORY-1067](THEORY-1067.md)), and computation adds only an L-dependent factor.
- **Anything about the runtime in practice** beyond the abstract's one
  unreported-protocol timing (n = 400, 90% outliers, "less than a second on
  a commercial laptop").
