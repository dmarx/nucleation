---
number: 301
status: Active
formerly:
- THEORY-tmp52yl2
title: 'The Procrustes distance between regularization-normalized representations and their average linear-decoding distance bound each other only through the participation ratio of the kernel difference: a small Procrustes distance forces a small decoding distance, but not conversely'
version: 2
history:
- version: 2
  date: '2026-10-19'
  note: >-
    Promoted from Proposed to Active at the owner's direction, carrying out
    the promotion audit's decision (record/promotion-audit/decisions/THEORY-301.yaml,
    batch 013). The promote_when asked for a second close reading of
    App. A.1: Lemma 1, the partial-trace monotonicity and the
    Powers–Størmer step. It is met instead by a direct derivation of
    eqs. 25–26 for real matrices, written out below and in the decision
    file, which also re-derives Cor. 1 so that nothing here rests on
    THEORY-008. The owner's rule of 2026-10-19 (ADR-047): a checked
    step-by-step re-derivation recorded in the decision file meets a
    promote_when that asks for a proof the record does not hold, and the
    THEORY is promoted. The promote_when is removed. The claim is
    unchanged.
tags:
- representation-learning
- mathematics
date: '2026-10-14'
source:
- LIT-257
- LIT-250
summary: >-
  Harvey, Lipshutz & Williams (2024), [LIT-257](../literature.d/LIT-257.md), Proposition 3 and App. A.1,
  read in [NOTE-834](../notes.d/NOTE-834.md). With K_X = XG(X)⁻¹Xᵀ/M, α = Tr K_X, β = Tr K_Y and
  R_Δ the participation ratio of K_X − K_Y,
  P⁴/R_Δ ≤ E‖Xw* − Yv*‖² ≤ (2(α + β)P² − P⁴)/R_Δ for targets with
  E[zzᵀ] = I. The Procrustes–Bures equivalence is imported from [LIT-250](../literature.d/LIT-250.md).
  Kernels with orthogonal supports show the converse fails: Procrustes
  distance maximal, decoding distance as small as 2/r. Finite samples,
  linear readouts only.
---
<!-- inactive-ok-file: THEORY-008 — Proposed; the equivalence this rests on, the readout identities it extends, and the parallel CKA–Bures envelope, named in Connections -->

# THEORY-301: The Procrustes distance between regularization-normalized representations and their average linear-decoding distance bound each other only through the participation ratio of the kernel difference: a small Procrustes distance forces a small decoding distance, but not conversely

## Source

Harvey, Lipshutz & Williams (2024), [LIT-257](../literature.d/LIT-257.md), §4 (eqs. 22–26),
Proposition 3, App. A.1 (eqs. 27–53) and Fig. 2, read in [NOTE-834](../notes.d/NOTE-834.md).
The Procrustes–Bures equivalence, P(X̃,Ỹ) = d_B(X̃X̃ᵀ, ỸỸᵀ), is Harvey,
Larsen & Williams, [LIT-250](../literature.d/LIT-250.md), Thm 1 ([THEORY-004](THEORY-004.md)).

## What was actually shown

Take the optimal readouts of eq. 1, w* = G(X)⁻¹Xᵀz/M, with
G(X) = aC_X + bI, and targets with E[zzᵀ] = I. Then the average decoding
distance is E‖Xw* − Yv*‖² = ‖K_X − K_Y‖²_F (Cor. 1). Normalize
X̃ = XG(X)^{−1/2}/√M, so that X̃X̃ᵀ = K_X, and let P be the Procrustes
distance, zero-padded to equal widths. With α = Tr K_X, β = Tr K_Y and
R_Δ = ‖K_X − K_Y‖²_*/‖K_X − K_Y‖²_F:

(α + β) − √((α + β)² − R_Δ E‖Xw* − Yv*‖²) ≤ P(X̃,Ỹ)² ≤ √(R_Δ E‖Xw* − Yv*‖²)  (eq. 25),

equivalently P⁴/R_Δ ≤ E‖Xw* − Yv*‖² ≤ (2(α + β)P² − P⁴)/R_Δ (eq. 26).

- **The lower bound on P²** comes from a Fuchs–van de Graaf-type
  argument. ‖αuuᵀ − βvvᵀ‖_* = √((α + β)² − 4αβ⟨u,v⟩²) (Lemma 1). Choosing
  representatives in the orthogonal orbits so that ⟨vec X̃, vec Ỹ⟩ is the
  fidelity, partial-trace monotonicity gives
  ‖K_X − K_Y‖_* ≤ √((α + β)² − 4F²).
- **The upper bound on P²** is d_B² ≤ ‖K_X^{1/2} − K_Y^{1/2}‖²_F ≤
  ‖K_X − K_Y‖_* (Powers–Størmer).
- **Lemma 2.** With equal traces, R_Δ ≥ 2. A shorter proof: a trace-zero
  difference has nuclear norm 2S, S its positive eigenvalue sum, and
  squared Frobenius norm at most 2S² ([NOTE-834](../notes.d/NOTE-834.md)).

**Small P forces small decoding distance.** Since R_Δ ≥ 1,
E‖Xw* − Yv*‖² ≤ 2(α + β)P².

**The converse fails without control of R_Δ.** Take trace-one kernels
K_X = Π₁/r and K_Y = Π₂/r, with Π₁, Π₂ orthogonal rank-r projections.
The fidelity is 0, so P² = 2, the maximum under α = β = 1, while
E‖Xw* − Yv*‖² = 2/r. That is the reader's example ([NOTE-834](../notes.d/NOTE-834.md)), and
it is the case R_Δ = 2r. The paper shows the same region with random
positive semidefinite pairs (Fig. 2D) and states the asymmetry in words
(§4).

What could have failed: the two distances could have been equivalent
with dimension-free constants. The participation ratio in eq. 25 is
where they are not.

## What this does not say

- **Not which distance is right.** The paper calls Procrustes "a more
  strict notion of geometric dissimilarity" and does not argue that
  either tracks function better.
- **Not anything beyond K_z = I.** Both bounds use Cor. 1's identity, so
  they hold for targets uncorrelated across conditions, with unit
  variance.
- **Not anything about nonlinear readouts, classifiers or the
  population limit.** Linear regression readouts at finite M only.
- **Not tight in general.** Saturation is stated for rank-one kernels
  (lower bound) and for commuting kernels with spectra in {0,1} (upper
  bound). Elsewhere the slack is not characterized.
- **Not about trained networks.** Fig. 2 uses random ensembles of
  50 × 50 PSD matrices.

## Connections

- **[THEORY-004](THEORY-004.md)** supplies the premise: rotation-aligned distance equals
  Bures distance between kernels. Here the Bures distance is
  re-expressed through decoding.
- **[THEORY-008](THEORY-008.md)** holds the identity E‖Xw* − Yv*‖² = ‖K_X − K_Y‖²_F, which
  this account bounds against Procrustes.
- **[THEORY-233](THEORY-233.md)** is the parallel envelope between CKA and normalized
  Bures similarity ([LIT-250](../literature.d/LIT-250.md)), with the kernels' ranks as the constant.
  Here the constant is the participation ratio of the difference. Both
  bounds come from the Fuchs–van de Graaf route, and both say the
  Euclidean and Bures geometries of kernels agree only up to a
  dimension-like factor.

## Note of 2026-10-19: eqs. 25–26, derived directly

With the notation above, write Δ = K_X − K_Y and D = E‖Xw* − Yv*‖². All
matrices are real.

- **Cor. 1.** Xw* = XG(X)⁻¹Xᵀz/M = K_X z, so D = E‖Δz‖² =
  Tr(Δ E[zzᵀ] Δ) = ‖Δ‖²_F when E[zzᵀ] = I.
- **Procrustes is Bures** ([THEORY-004](THEORY-004.md)). P² = α + β − 2F, with F the
  fidelity ‖K_X^{1/2}K_Y^{1/2}‖_*, which is also the maximum over
  orthogonal Q of ⟨X̃, ỸQ⟩.
- **Upper bound on P².** F ≥ Tr(K_X^{1/2}K_Y^{1/2}), so
  P² ≤ ‖K_X^{1/2} − K_Y^{1/2}‖²_F. For Powers–Størmer, let S = K_X^{1/2},
  T = K_Y^{1/2}, E = S − T with eigenpairs (dᵢ, eᵢ), and J = sign(E).
  Then K_X − K_Y = ½(E(S + T) + (S + T)E), and J commutes with E, so
  Tr(JΔ) = Σᵢ |dᵢ|⟨eᵢ, (S + T)eᵢ⟩ ≥ Σᵢ |dᵢ||⟨eᵢ, (S − T)eᵢ⟩| = ‖E‖²_F,
  because S and T are positive semidefinite. Since ‖J‖_op ≤ 1,
  P² ≤ ‖E‖²_F ≤ ‖Δ‖_* = √(R_Δ D).
- **Lower bound on P².** Replace Ỹ by ỸQ for the optimal Q, which leaves
  K_Y unchanged. Let u = vec X̃/√α and v = vec Ỹ/√β in ℝ^M ⊗ ℝ^N, so
  ⟨u, v⟩ = c = F/√(αβ). The partial trace over ℝ^N sends αuuᵀ to K_X and
  βvvᵀ to K_Y. It is a trace-norm contraction:
  ‖Tr_N H‖_* = sup over ‖W‖_op ≤ 1 of Tr((W ⊗ I)H) ≤ ‖H‖_*. On span{u, v},
  with v = cu + sw, the matrix αuuᵀ − βvvᵀ has trace α − β and
  determinant −αβs² ≤ 0. Its nuclear norm is therefore |λ₁ − λ₂| =
  √((α − β)² + 4αβs²) = √((α + β)² − 4F²), which is Lemma 1. So
  R_Δ D = ‖Δ‖²_* ≤ (α + β)² − (α + β − P²)². Since α + β − P² = 2F ≥ 0,
  this is the left side of eq. 25.
- **Eq. 26** rearranges eq. 25. Since ‖·‖_* ≥ ‖·‖_F, R_Δ ≥ 1 and
  D ≤ 2(α + β)P².

Uhlmann's theorem enters only through the maximisation in [THEORY-004](THEORY-004.md).
The other steps are elementary and hold for real matrices as stated.
