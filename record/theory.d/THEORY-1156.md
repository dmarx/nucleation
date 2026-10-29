---
number: 1156
status: Active
formerly:
- THEORY-tmpwl8e3
title: 'The fused Gromov–Wasserstein discrepancy between two attributed graphs, a single coupling that pays (1 − α) for moving node features and α for distorting pairwise structure, tends to the Wasserstein distance between the features as α → 0 and to the Gromov–Wasserstein distance between the structures as α → 1, lies above their α-weighted mixture, and for q = 1, α strictly between 0 and 1 and distance-matrix structures is a metric that vanishes exactly when a bijection of the nodes preserves weights, features and structure together'
version: 1
tags:
- mathematics
- network-science
date: '2026-10-29'
source:
- LIT-1813
summary: >-
  Vayer, Chapel, Flamary, Tavenard and Courty (2019), [LIT-1813](../literature.d/LIT-1813.md),
  Theorems 3.1–3.2 with the supplement's proofs, read in [NOTE-1328](../notes.d/NOTE-1328.md)
  from arXiv v3. Proved; the lower bound and the concavity in α of the
  exact value were checked on enumerated permutations. Active. It says
  nothing about the uniqueness of the optimal coupling or about the
  solver, which reaches only stationary points.
---

# THEORY-1156: The fused Gromov–Wasserstein discrepancy between two attributed graphs, a single coupling that pays (1 − α) for moving node features and α for distorting pairwise structure, tends to the Wasserstein distance between the features as α → 0 and to the Gromov–Wasserstein distance between the structures as α → 1, lies above their α-weighted mixture, and for q = 1, α strictly between 0 and 1 and distance-matrix structures is a metric that vanishes exactly when a bijection of the nodes preserves weights, features and structure together

## Source

Vayer, Chapel, Flamary, Tavenard and Courty (2019), [LIT-1813](../literature.d/LIT-1813.md), §3.1, pp.
3–4, and §6.1, pp. 10–14 of arXiv 1805.09114v3; read in [NOTE-1328](../notes.d/NOTE-1328.md).

## What was actually shown

**Definition (eq. 1, p. 3).** FGW_{q,α}(µ, ν) = min_{π ∈ Π(h,g)}
Σ [(1 − α) d(a_i, b_j)^q + α |C₁(i,k) − C₂(j,l)|^q] π_{i,j} π_{k,l}.

**Bounds and interpolation (Lemma 6.1, Theorem 6.2, pp. 11–12).** Since
the objective splits as (1 − α) H_q(π) + α J_q(π), with H_q ≥ W_q^q and
J_q ≥ GW_q^q for every π, FGW ≥ (1 − α) W_q^q + α GW_q^q. Evaluating at the
W-optimal and at the GW-optimal plans gives upper bounds that close as
α → 0 and α → 1 respectively.

**Metric (Theorems 6.3–6.6, pp. 12–14).** For α ∈ ]0, 1[ and distance
matrices C₁, C₂: FGW = 0 iff n = m and some bijection σ has h_i = g_σ(i),
a_i = b_σ(i) and C₁(i, k) = C₂(σ(i), σ(k)). The hard direction passes to
the GW problem on Ĉ = ½C + ½d(a, a), shows it vanishes, and uses Mémoli's
theorem that GW vanishes only at a measure-preserving isometry. The
triangle inequality holds for q = 1 by gluing the two optimal plans. For
q > 1 it holds with a factor 2^{q−1}, from (x + y)^q ≤ 2^{q−1}(x^q + y^q).

**A consequence, checked.** The exact FGW value is a minimum over π of
functions affine in α, so it is concave in α. On two random 6-node graphs,
with the minimum over permutations, the value was concave on a 21-point
grid, met the lower bound, and had three distinct optimal plans along α.

**What could have failed.** A mixture of a feature cost and a structure
cost under one coupling could have vanished without a single bijection
doing both jobs. The Ĉ construction shows it cannot: a zero-cost plan
preserves features and structure at once.

## What this does not say

- **That the optimal coupling is unique.** Any bijection preserving
  weights, features and structure composes with an optimal plan at no cost
  ([THEORY-1129](THEORY-1129.md)).
- **That computed values are the FGW value.** The objective is non-convex
  and conditional gradient finds stationary points (p. 5).
- **Anything about α = 0 or α = 1 as metrics on structured data.** At the
  ends FGW forgets the structure or the features, and the zero theorem is
  stated for interior α only.
- **That the interior α is better for prediction.** The paper's
  experiments do not show that ([NOTE-1328](../notes.d/NOTE-1328.md)).
