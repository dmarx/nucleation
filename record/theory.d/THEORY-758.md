---
number: 758
status: Active
formerly:
- THEORY-tmpm2oxc
title: 'For a self-adjoint diffusion operator T with spectrum in [0, 1], the diffusion-wavelet levels are spectral subspaces spanned by the eigenvectors with λ^s ≥ ε for an increasing sequence of powers s, so they form an exactly nested chain of T-invariant subspaces whose differences are bands of the spectrum, about one octave each, not spatial blocks; Coifman and Maggioni''s compressed algorithm, which squares the operator on each orthonormal basis, thresholds T^{2^{j−1}} at level j and not T^{2^j−1} as the paper states; and since each level is T-invariant, each is an exactly closed linear coarse-graining whose localized basis is a choice the level does not fix'
version: 1
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Filed Active from NOTE-984. The spectral multiresolution
    (4.8)–(4.11) and the compressed algorithm (§4.6, Fig. 3) are the
    paper's. The induction giving the compressed algorithm's threshold, the
    closure statement and the basis-dependence of localization are the
    record's. Every step is re-derived below, which meets the condition for
    Active under ADR-047 v2. A numerical check on the paper's own circle
    example is reported with it.
tags:
- mathematics
- complex-systems
date: '2026-10-20'
source:
- LIT-1256
summary: >-
  Coifman and Maggioni (2006), [LIT-1256](../literature.d/LIT-1256.md), read in full in
  [NOTE-984](../notes.d/NOTE-984.md). The levels of a diffusion multiresolution are spectral
  bands. Nesting is exact and needs no decay of the spectrum, and decay
  buys only compression. The compressed algorithm as written keeps
  ⟨ξ : λ^{2^{j−1}} > ε⟩ at level j, and the paper's own Fig. 9 follows
  this, not its stated count. Each level closes exactly under T, but a
  single scaling function does not. It says nothing about non-self-adjoint
  operators, about error bounds for the compressed scheme with finite
  precision, or about when a localized basis exists.
bears_on:
- QUESTION-218
- QUESTION-217
---
<!-- inactive-ok-file: CLAIM-157 — Proposed; the block criterion this account is contrasted with, open -->

# THEORY-758: For a self-adjoint diffusion operator T with spectrum in [0, 1], the diffusion-wavelet levels are spectral subspaces spanned by the eigenvectors with λ^s ≥ ε for an increasing sequence of powers s, so they form an exactly nested chain of T-invariant subspaces whose differences are bands of the spectrum, about one octave each, not spatial blocks; Coifman and Maggioni's compressed algorithm, which squares the operator on each orthonormal basis, thresholds T^{2^{j−1}} at level j and not T^{2^j−1} as the paper states; and since each level is T-invariant, each is an exactly closed linear coarse-graining whose localized basis is a choice the level does not fix

## Source

Coifman and Maggioni (2006), "Diffusion wavelets", *Applied and
Computational Harmonic Analysis* 21(1): 53–94, [LIT-1256](../literature.d/LIT-1256.md), read in full
in [NOTE-984](../notes.d/NOTE-984.md) from the published version. The spectral spaces are
(4.8)–(4.11) of §4.3. The compressed construction is §2.2, §4.6 (4.16)
and Fig. 3. The stated dimension is §5.4, with Fig. 1. The derivations
below are the record's.

## What was actually shown

**Setting.** X finite (n points, counting measure), T a symmetric n × n
matrix with eigenvalues λ ∈ [0, 1] and orthonormal eigenvectors ξ_λ. (The
paper's semigroups have this spectrum by Remark 14.) Fix ε ∈ (0, 1), and
assume no eigenvalue has a power in the sequence below exactly equal to ε.

**1. The spectral chain.** For an increasing sequence s₀ < s₁ < … let
V_j = ⟨ξ_λ : λ^{s_j} ≥ ε⟩. For λ ∈ [0, 1], λ^{s_{j+1}} ≤ λ^{s_j}, so
λ^{s_{j+1}} ≥ ε implies λ^{s_j} ≥ ε. Hence V_{j+1} ⊆ V_j. Each V_j is
spanned by eigenvectors, so TV_j ⊆ V_j, and the orthogonal projector P_j
onto V_j commutes with T. W_j := V_j ⊖ V_{j+1} is spanned by the ξ_λ with
ε^{1/s_j} ≤ λ < ε^{1/s_{j+1}}. In generator units ν = −ln λ, this is
ln(1/ε)/s_{j+1} < ν ≤ ln(1/ε)/s_j. For dyadic s (s_{j+1}/s_j → 2) it is
one octave. ℝⁿ = ⊕_j W_j ⊕ ⟨ξ_λ : λ = 1⟩ ⊕ (the part below the first
threshold). No decay of the spectrum is used. Decay enters only in how
fast dim V_j falls: under γ-strong decay, dim V_j ≤ C(log₂(1/ε)/s_j)^γ,
which is (4.12) with s_j = t_j ≥ 2^j.

**2. What the compressed algorithm keeps.** The algorithm sets Φ₀ = I and
T₀ = T. At level j it truncates T_j = Φ_jᵀT^{2^j}Φ_j at ε, keeps the
orthonormal columns Q, sets Φ_{j+1} = Φ_jQ and M_j = QᵀT_j, and sets
T_{j+1} = M_jM_jᵀ (4.16). Take the truncation to be the exact one: the
singular vectors with singular value > ε. (The paper's rank-revealing QR
approximates it within p(k, n).)

*Claim.* For j ≥ 1, ⟨Φ_j⟩ = U_j := ⟨ξ_λ : λ^{2^{j−1}} > ε⟩, and
T_j = Φ_jᵀT^{2^j}Φ_j.

*Base.* T₀ = T is symmetric positive semi-definite, so its singular
vectors are its eigenvectors and its singular values are its eigenvalues.
Keeping those > ε gives ⟨Φ₁⟩ = ⟨ξ_λ : λ > ε⟩ = U₁. M₀M₀ᵀ = QᵀT²Q =
Φ₁ᵀT²Φ₁.

*Step.* Suppose ⟨Φ_j⟩ = U_j, an invariant subspace, and
T_j = Φ_jᵀT^{2^j}Φ_j. Then T_j is symmetric positive semi-definite with
eigenvalues λ^{2^j} for λ in U_j's set, and eigenvectors Φ_jᵀξ_λ. Keeping
those with λ^{2^j} > ε gives
⟨Φ_{j+1}⟩ = ⟨ξ_λ : λ^{2^{j−1}} > ε and λ^{2^j} > ε⟩ = ⟨ξ_λ : λ^{2^j} > ε⟩ = U_{j+1},
because λ^{2^j} ≤ λ^{2^{j−1}}. Since U_j is T-invariant,
Φ_jΦ_jᵀ T^{2^j}Φ_j = T^{2^j}Φ_j, so
M_jM_jᵀ = QᵀΦ_jᵀT^{2^j}Φ_jΦ_jᵀT^{2^j}Φ_jQ = Φ_{j+1}ᵀT^{2^{j+1}}Φ_{j+1}. This
completes the induction.

So level j keeps the band set by T^{2^{j−1}}. The reason is that Φ_j is
orthonormal, so the shrinkage λ^{2^j−1} already applied by the earlier
factors is not carried forward. The paper's §5.4 says
k = dim Ṽ_{j+1} = #{λ^{2^{j+1}−1} ≥ ε}, and Fig. 1 labels V₁, …, V₄ on the
spectra of T, T³, T⁷ and T¹⁵. That count belongs to the uncompressed route
of Theorem 27, the ε-span of T^{2^j−1}Φ₀, whose ε-rank is #{λ^{2^j−1} > ε}.
Both are nested chains of octave bands. The compressed one lags by about
one level.

*Nesting holds for any truncation and any T.* Φ_{j+1} = Φ_jQ, so
⟨Φ_{j+1}⟩ ⊆ ⟨Φ_j⟩ exactly, with no use of symmetry or of the spectrum.

**3. Closure.** Since TV_j ⊆ V_j, TΦ_j = Φ_j(Φ_jᵀTΦ_j). For the linear
dynamics x_{t+1} = Tx_t + e_t, the coarse variable y = Φ_jᵀx satisfies
y_{t+1} = (Φ_jᵀTΦ_j)y_t + Φ_jᵀe_t, with no dependence on the rest of x. In
[THEORY-733](THEORY-733.md)'s terms (VAR(1), A = T), the row space of L = Φ_jᵀ is
invariant under Aᵀ = T, so the coarse-graining is exactly dynamically
independent. A symmetric T has such invariant subspaces at every
dimension. [THEORY-733](THEORY-733.md) notes that a general VAR(1) need not. The
diffusion-wavelet levels are a nested chain of them.

**4. The basis is not fixed by the level.** Every orthonormal basis of
V_j spans the same closed space. In particular the eigenvectors are a
basis, and they are global modes. A single scaling function φ is not
closed: Tφ lies in V_j but is not in general a multiple of φ. So whatever
units the localized scaling functions provide come from the
orthogonalization rule (dyadic cubes, pivoting), not from T.

**Numerical check.** The paper's circle example: T = (T′)² with T′ the
periodic three-point average (½ on the diagonal, ¼ off it), ε = 10⁻⁴.
- With exact (SVD) truncation at n = 256, the compressed dimensions were
  239, 203, 159, 117, 85, 61, 43, 31, 21, 15, 11 for j = 1, …, 11. These
  equal #{λ^{2^{j−1}} > ε} at every level. The paper's count
  #{λ^{2^j−1} ≥ ε} gives 239, 177, 125, 89, 63, ….
- With pivoted QR (|R_kk| > ε) at n = 512, the dimensions were 486, 408,
  317, 236, 170, … against 479, 407, 317, 235, 171. The paper's Fig. 9,
  read from a render, passes about 410, 310 and 235 at j = 2, 3, 4. The
  paper's count would be 355, 251 and 177.
- Nestedness held to 2 × 10⁻¹⁴ at every level.
- With exact truncation the computed space equals the spectral one. With
  pivoted QR it was invariant under T^{2^j} to 2–7 × 10⁻⁵, but under T only
  to 1.2 × 10⁻², because the circle's spectrum has no gap at the
  threshold.

What could have failed: the compressed count could have matched the paper
(it would, if the algorithm carried singular values forward), and the
nesting could have needed the spectrum (it does not).

## What this does not say

- **Not an error bound for the compressed scheme in finite precision.**
  With rank-revealing QR, the computed spaces differ from the spectral
  ones near each threshold. How far they differ depends on the gap there
  ([CLAIM-164](../claims.d/CLAIM-164.md)), and the paper proves no bound. Part 3's exact closure is
  for the exact spectral spaces. The computed ones close only
  approximately, and at the level's own time step better than at one step
  of T.
- **Not that the levels have units.** Part 4 says the level fixes a space,
  not a basis. When a gap isolates metastable sets, a basis of
  near-indicators lies in the band ([CLAIM-157](../claims.d/CLAIM-157.md)'s block, the paper's
  three-cloud example). Without one (the circle), coarse scaling functions
  tend to sines and cosines. Whether a given pivoting rule finds the
  localized basis is a separate, unproved matter.
- **Not about non-self-adjoint operators.** Nesting by construction
  survives. The band reading, the orthogonal W_j, the squaring step and
  the induction in part 2 all use T = Tᵀ.
- **Not a relevance order.** No target enters. The chain is the
  operator's own, and the dyadic spacing of the cuts is a choice ("the
  choice of the factor 2 is arbitrary").
- **Not that the paper's hierarchy is wrong in form.** Both the stated
  and the computed chains are nested octave bands. The correction is
  which power sets each cut, so the compression is about one level less
  than the paper says.

## Connections

- **[QUESTION-217](../questions.d/QUESTION-217.md): answers in part.** It is the multilevel form of
  the commuting case in [THEORY-745](THEORY-745.md). The refinement order is exact and
  is the order of λ. Acquisition by the operator's own evolution follows
  the same order, because every level commutes with T. Spectral decay is
  needed for compression, not for the chain.
- **[QUESTION-218](../questions.d/QUESTION-218.md): answers in part.** Each level is a closed
  collective-mode space ([CLAIM-388](../claims.d/CLAIM-388.md)'s kind), and its localized basis
  elements are units only where a gap places block indicators in the band.
  Closure belongs to the space, and blockhood to a basis.
- **[THEORY-733](THEORY-733.md).** Part 3 is its p = 1 criterion applied to a symmetric
  operator, which has invariant subspaces at every scale.
- **[THEORY-745](THEORY-745.md).** V_j is the diffusion-map truncation at t = s_j with
  an absolute threshold, and the nesting is the same fact.
- **[CLAIM-164](../claims.d/CLAIM-164.md).** It is the reason the computed levels are stable only
  where the threshold falls in a gap.
