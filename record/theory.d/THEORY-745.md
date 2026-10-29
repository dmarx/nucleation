---
number: 745
status: Active
formerly:
- THEORY-tmp3xg7a
title: 'For the reversible walk p = k/d built from a symmetric non-negative kernel on a finite connected set, the t-step diffusion distance is exactly the Euclidean distance between the coordinates λ_l^t ψ_l, and keeping only the coordinates with |λ_l|^t > δ|λ₁|^t errs in D_t² by at most δ²|λ₁|^{2t}(1/π(x) + 1/π(y)), an absolute bound and not the relative accuracy δ that Coifman and Lafon state; the truncated maps are nested as t grows, so with δ fixed the steps t order a refinement chain by eigenvalue modulus, while untruncated they are all invertible images of one another'
version: 1
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Filed Active from NOTE-985. The spectral identity is the paper's
    Appendix A, whose ψ_l = φ_l/π is a misprint for φ_l/√π. The
    truncation bound, the 2t-path form, the nesting and the
    counterexample to "relative accuracy δ" are the record's. Every step
    is re-derived below, which meets the condition for Active under
    ADR-047 v2. A numerical check is reported with it.
tags:
- mathematics
- representation-learning
date: '2026-10-20'
source:
- LIT-1246
summary: >-
  Coifman and Lafon (2006), [LIT-1246](../literature.d/LIT-1246.md), read in full in [NOTE-985](../notes.d/NOTE-985.md).
  The identity D_t² = Σ λ_l^{2t}(ψ_l(x) − ψ_l(y))² is exact. The paper's
  Proposition 1 says the truncated map keeps it "up to relative accuracy
  δ". The true bound is absolute and can be large relative to D_t for
  nearby points. In the refinement sense, the diffusion-map family
  coarsens with t only through the threshold. Finite sets, counting
  measure and reversible walks only. It says nothing about the manifold
  limit or about non-reversible chains.
bears_on:
- QUESTION-217
---
<!-- inactive-ok-file: CLAIM-157 THEORY-186 — Proposed; accounts this is contrasted with, nothing here rests on their being settled -->

# THEORY-745: For the reversible walk p = k/d built from a symmetric non-negative kernel on a finite connected set, the t-step diffusion distance is exactly the Euclidean distance between the coordinates λ_l^t ψ_l, and keeping only the coordinates with |λ_l|^t > δ|λ₁|^t errs in D_t² by at most δ²|λ₁|^{2t}(1/π(x) + 1/π(y)), an absolute bound and not the relative accuracy δ that Coifman and Lafon state; the truncated maps are nested as t grows, so with δ fixed the steps t order a refinement chain by eigenvalue modulus, while untruncated they are all invertible images of one another

## Source

Coifman and Lafon (2006), "Diffusion maps", *Applied and Computational
Harmonic Analysis* 21(1): 5–30, [LIT-1246](../literature.d/LIT-1246.md), read in full in
[NOTE-985](../notes.d/NOTE-985.md) from the published version. The construction is §2. The
identity is Appendix A. The truncation and Proposition 1 are §2.4. The
derivations below are the record's.

## What was actually shown

**Setting.** X is finite with counting measure. k(x, y) = k(y, x) ≥ 0, with
k(x, x) > 0, and the graph of k is connected. Let d(x) = Σ_y k(x, y),
P = D⁻¹K (so p(x, y) = k(x, y)/d(x)), Z = Σ_x d(x) and π = d/Z. Then
π(x)p(x, y) = k(x, y)/Z = π(y)p(y, x), so the walk is reversible.

**Spectral form.** A = D^{−1/2}KD^{−1/2} is symmetric, so
A = Σ_l λ_l φ_l φ_lᵀ with the φ_l an orthonormal basis of ℝ^X. Since
P = D^{−1/2}AD^{1/2},
p(x, y) = Σ_l λ_l φ_l(x)φ_l(y)√(d(y)/d(x)) = Σ_l λ_l ψ_l(x)φ̃_l(y), with
ψ_l = φ_l/√π and φ̃_l = φ_l√π. (The paper prints φ_l/π and φ_l π.) A√d = √d,
so φ₀ = √π, λ₀ = 1 and ψ₀ ≡ 1. Connectivity and k(x, x) > 0 make the walk
irreducible and aperiodic, so |λ_l| < 1 for l ≥ 1. Order l ≥ 1 by |λ_l|,
largest first. Biorthogonality gives P^t's kernel as
p_t(x, y) = Σ_l λ_l^t ψ_l(x)φ̃_l(y).

**The identity.** The φ̃_l are orthonormal for the inner product weighted
by 1/π: Σ_u φ̃_l(u)φ̃_m(u)/π(u) = Σ_u φ_l(u)φ_m(u) = δ_lm. So u ↦ p_t(x, u)
has coefficients λ_l^t ψ_l(x) in that basis, and by Parseval
D_t(x, y)² = Σ_u (p_t(x, u) − p_t(y, u))²/π(u) = Σ_{l≥1} λ_l^{2t}(ψ_l(x) − ψ_l(y))².
The l = 0 term vanishes because ψ₀ is constant.

**The 2t-path form.** By reversibility, p_t(y, u)/π(u) = p_t(u, y)/π(y). So
Σ_u p_t(x, u)p_t(y, u)/π(u) = p_{2t}(x, y)/π(y), and
D_t(x, y)² = p_{2t}(x, x)/π(x) + p_{2t}(y, y)/π(y) − 2p_{2t}(x, y)/π(y).
D_t counts paths of length 2t between x and y, against the return paths
at each.

**The truncation bound.** Let s = s(δ, t) = max{l : |λ_l|^t > δ|λ₁|^t} and
Ψ_t(x) = (λ_l^t ψ_l(x))_{1≤l≤s}. Because of the ordering, every l > s has
|λ_l|^t ≤ δ|λ₁|^t. Equal moduli fall on the same side of the strict
inequality, so the truncated distance does not depend on the basis chosen
inside an eigenspace. Completeness of the φ_l gives
Σ_l φ_l(x)φ_l(y) = 1[x = y], so Σ_l ψ_l(x)ψ_l(y) = 1[x = y]/π(x). For
x ≠ y this gives Σ_{l≥1}(ψ_l(x) − ψ_l(y))² = 1/π(x) + 1/π(y). Therefore

0 ≤ D_t(x, y)² − ‖Ψ_t(x) − Ψ_t(y)‖² = Σ_{l>s} λ_l^{2t}(ψ_l(x) − ψ_l(y))²
≤ δ²|λ₁|^{2t}(1/π(x) + 1/π(y)).

With a general weight μ on X, 1/π(x) becomes 1/(π(x)μ(x)).

**Not relative.** The paper's Proposition 1 says the truncated map gives
D_t "up to relative accuracy δ". The bound above does not shrink with
D_t(x, y). For two nearby points, whose leading coordinates nearly
coincide, the neglected tail can be most of D_t². Checked on 60 points in
three Gaussian clusters, one pair nearly duplicated, with Gaussian
weights of ε = 0.7, t = 3 and δ = 0.05, so s = 2. The spectral and direct
D_t² agreed to 10⁻¹⁴ over all pairs, and so did the 2t-path form. The absolute bound held
for all 1770 pairs, using at most 1.6% of it. The relative error
1 − ‖Ψ_t(x) − Ψ_t(y)‖/D_t(x, y) reached 0.985, for two points in the same
cluster with D_t² ≈ 5.6 × 10⁻⁶.

**Nesting in t.** For l ≥ 1, |λ_l/λ₁| ≤ 1, so the condition
|λ_l/λ₁|^t > δ, once false at t, stays false for larger t. So
s(δ, t′) ≤ s(δ, t) for t′ ≥ t, and
Ψ_{t′}(x) = diag(λ₁^{t′−t}, …, λ_{s′}^{t′−t}) · (the first s′ = s(δ, t′)
coordinates of Ψ_t(x)). Ψ_{t′} is a function of Ψ_t, so
σ(Ψ_{t′}) ⊆ σ(Ψ_t). In the example, s(δ, t) for t = 1, 2, 4, 8, 16 was
8, 3, 2, 1, 1.

**Untruncated, nothing coarsens.** Without the threshold, and with no
λ_l = 0, the full maps satisfy Ψ_{t′} = Λ^{t′−t}Ψ_t with Λ invertible. So
every Ψ_t determines every other. Increasing t reweights the metric and
discards no distinction.

What could have failed: the identity could have needed positive
semi-definiteness. It does not: negative λ_l enter as λ_l^{2t}. The
truncation could have been controlled relative to D_t, as the paper says,
and it is not.

## What this does not say

- **Not anything about the manifold limit.** The α-family and the heat
  kernel are [THEORY-744](THEORY-744.md)'s subject, not this one's.
- **Not that the retained coordinates are stable.** The bound controls the
  distance. When the threshold falls inside a cluster of nearly equal
  |λ_l|, which coordinates are kept can change under a small perturbation
  ([CLAIM-164](../claims.d/CLAIM-164.md)). A stable truncation cuts at a gap. The paper never uses a
  gap.
- **Not that t-coarsening finds clusters.** That the merging of the
  blocks of P^t in t (the paper's Fig. 1) tracks metastable clusters
  needs a gap and escape-probability argument, which the paper
  illustrates and does not prove.
- **Not about non-reversible walks.** Without reversibility there is no
  symmetric conjugate, and the identity fails.
- **Not a relevance order.** No target enters. The refinement chain is the
  operator's own.

## Connections

- **[QUESTION-217](../questions.d/QUESTION-217.md): answers in part.** It is a model case of an
  operator-induced coarse-to-fine order. With a fixed threshold, the
  refinement order is the order of |λ_l|. So is the order in which
  repeated application of the same operator suppresses modes. The two
  coincide by construction, because the levels are the operator's own
  spectral projectors. That is Conjecture A's exactly commuting case. It
  leaves open when an independently given hierarchy agrees with the
  operator's order.
- **[CLAIM-164](../claims.d/CLAIM-164.md).** It supplies what a robust version of the truncation
  needs: cut at a gap and the kept span is gap-isolated, so it rotates by
  at most ‖δP‖/gap.
- **[THEORY-186](THEORY-186.md) and [THEORY-086](THEORY-086.md).** These order acquisition by an operator's
  spectrum. This entry shows the matching refinement order for a
  diffusion. Where those entries' levels are spectral, refinement and
  acquisition coincide for the same reason.
- **[CLAIM-157](../claims.d/CLAIM-157.md).** The metastable clusters of Fig. 1 are the kind of block
  [CLAIM-157](../claims.d/CLAIM-157.md) names. This entry does not supply the link from gap to block.
