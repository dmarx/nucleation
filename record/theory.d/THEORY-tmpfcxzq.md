---
status: Active
title: 'If a velocity field''s third-order increments obey ‖δu(r)‖₃ ≤ C u_rms (r/L)^σ at every separation r, with 0 < σ < 1, then for a smooth, rapidly decaying filter the space-averaged energy flux across scale ℓ takes at most a fraction of order (ℓ/Δ)^(1−σ) from strain at scales above Δ and of order (δ/ℓ)^(2σ) from stress at scales below δ, measured against u_rms³/L·(ℓ/L)^(3σ−1); so transfer between scales is local in scale, with a power-law decay and no gap'
version: 2
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Filed Active from NOTE-tmp5es2s. The bounds are the paper's (23)–(24)
    with their supporting estimates (14)–(16) and (20)–(22), which the
    paper states and refers to Eyink (2005) for proof. Every step is
    re-derived below from the scaling hypothesis taken as an upper bound,
    which meets the condition for Active under ADR-047 v2. The result is
    held as a conditional: whether Navier–Stokes solutions satisfy the
    hypothesis is not part of it. The general-σ prefactor, and the reading
    of the decay as banded rather than gapped, are the record's.
- version: 2
  date: '2026-10-20'
  note: >-
    Connections gain Constantin, E and Titi (THEORY-tmp99aof): the same estimate vanishes for σ > 1/3, so the non-zero mean flux this account assumes requires σ₃ ≤ 1/3. The account is unchanged.
tags:
- natural-sciences
- mathematics
date: '2026-10-20'
source:
- LIT-tmp2snx1
summary: >-
  Eyink and Aluie (2009), [LIT-tmp2snx1](../literature.d/LIT-tmp2snx1.md), read in [NOTE-tmp5es2s](../notes.d/NOTE-tmp5es2s.md), stating
  bounds proved in Eyink (2005), [LIT-tmpko78q](../literature.d/LIT-tmpko78q.md). A conditional inequality:
  if velocity increments scale no faster than r^σ in the L³ mean, the
  contributions of far larger and far smaller scales to the mean flux
  across ℓ are bounded by powers of the scale ratio. It needs 0 < σ < 1:
  σ < 1 for the large scales, σ > 0 for the small. That the inertial range
  satisfies the hypothesis, that the mean flux there is non-zero, and the
  sharper 4/3 exponent are assumptions or heuristics, not part of it. It
  is about one field decomposed by scale, and says nothing about units.
---
<!-- inactive-ok-file: LIT-tmpko78q — Deferred; the paper holding the original proofs, registered unread, cited as the source the reading refers to -->
<!-- inactive-ok-file: CLAIM-157 — Proposed; the block criterion this account is contrasted with, open -->
# THEORY-tmpfcxzq: If a velocity field's third-order increments obey ‖δu(r)‖₃ ≤ C u_rms (r/L)^σ at every separation r, with 0 < σ < 1, then for a smooth, rapidly decaying filter the space-averaged energy flux across scale ℓ takes at most a fraction of order (ℓ/Δ)^(1−σ) from strain at scales above Δ and of order (δ/ℓ)^(2σ) from stress at scales below δ, measured against u_rms³/L·(ℓ/L)^(3σ−1); so transfer between scales is local in scale, with a power-law decay and no gap

## Source

Eyink and Aluie (2009), *Physics of Fluids* 21:115107, [LIT-tmp2snx1](../literature.d/LIT-tmp2snx1.md), read
in full in [NOTE-tmp5es2s](../notes.d/NOTE-tmp5es2s.md) from arXiv:0909.2386v1. The bounds are its (23)
and (24). The paper sketches them heuristically and refers to Eyink (2005),
[LIT-tmpko78q](../literature.d/LIT-tmpko78q.md) (registered unread), for the proofs. The derivation below is
the record's, written from the hypothesis the paper states as its (20).

## What was actually shown

**Setting.** u is a velocity field on a periodic or unbounded domain in d
dimensions, ⟨·⟩ is the space average, and ‖f‖_p = ⟨|f|^p⟩^(1/p). G is a
filter kernel: smooth, with ∫G = 1, and decaying fast enough that ∫|G(s)|
|s|^(2σ) ds and ∫|∇G(s)| |s|^σ ds are finite. Write G_ℓ(r) = ℓ^(−d)G(r/ℓ),
u_ℓ = G_ℓ ∗ u, u′_δ = u − u_δ, τ_ℓ(v, w) = (vw)_ℓ − v_ℓ w_ℓ, and

  Π_ℓ(u, v, w) = −∇u_ℓ : τ_ℓ(v, w),

the subgrid energy flux across ℓ, a source in the small-scale and a sink
in the large-scale energy budget. **Hypothesis (H):** ‖δu(r)‖₃ ≤
C₀ u_rms (|r|/L)^σ for every r, where δu(r)(x) = u(x + r) − u(x).

**Step 1. Everything is an increment.** Since ∫G = 1 and ∫∇G = 0:

- ∇u_Δ(x) = −∫(∇G_Δ)(r) δu(r)(x) dr, and (∇G_Δ)(r) = Δ^(−d−1)(∇G)(r/Δ);
- u′_δ(x) = −∫G_δ(r) δu(r)(x) dr;
- τ_ℓ(v, w) = ∫G_ℓ(r) δv(r)δw(r) dr − (∫G_ℓ δv dr)(∫G_ℓ δw dr). Expanding
  both terms, the products f·g_ℓ and f_ℓ·g cancel and what is left is
  (vw)_ℓ − v_ℓw_ℓ. The paper uses this form, after Vreman et al., for the
  positivity of the subgrid energy.

**Step 2. Norm bounds from (H).** By Minkowski's inequality, then (H),
then the change of variable r = Δs:

- ‖∇u_Δ‖₃ ≤ ∫|∇G_Δ(r)| ‖δu(r)‖₃ dr ≤ C₁ u_rms Δ^(σ−1) L^(−σ). Filtering
  again at ℓ multiplies the norm by at most ‖G‖₁ (Young), so the same bound
  holds for ∇(u_Δ)_ℓ. This is the paper's (21) in gradient form.
- ‖u′_δ‖₃ ≤ ∫|G_δ(r)| ‖δu(r)‖₃ dr ≤ C₂ u_rms (δ/L)^σ. This is (22).
- ‖τ_ℓ(u, u)‖_{3/2} ≤ ∫|G_ℓ(r)| ‖δu(r)‖₃² dr + (∫|G_ℓ(r)| ‖δu(r)‖₃ dr)²
  ≤ C₃ u_rms² (ℓ/L)^(2σ), using ‖|f|²‖_{3/2} = ‖f‖₃². This is (15).
- |τ_ℓ(f, f)| ≤ (|G| ∗ |f|²) + |f_ℓ|², so ‖τ_ℓ(u′_δ, u′_δ)‖_{3/2} ≤
  (‖G‖₁ + ‖G‖₁²)‖u′_δ‖₃² ≤ C₄ u_rms² (δ/L)^(2σ).

**Step 3. Hölder.** |⟨a : b⟩| ≤ ‖a‖₃ ‖b‖_{3/2}. So

- **large-scale strain:** |⟨Π_ℓ(u_Δ, u, u)⟩| ≤ C (u_rms³/L) (ℓ/L)^(3σ−1)
  (ℓ/Δ)^(1−σ);
- **small-scale stress:** |⟨Π_ℓ(u, u′_δ, u′_δ)⟩| ≤ C (u_rms³/L)
  (ℓ/L)^(3σ−1) (δ/ℓ)^(2σ).

The exponents check: Δ^(σ−1)ℓ^(2σ) = ℓ^(3σ−1)(ℓ/Δ)^(1−σ), and
ℓ^(σ−1)δ^(2σ) = ℓ^(3σ−1)(δ/ℓ)^(2σ). At σ = 1/3 the prefactor is u_rms³/L,
of order the mean dissipation ε, and both exponents are exactly 2/3. These
are the paper's (23) and (24). The paper writes them with ε, which is
right only at σ₃ = 1/3; the general form is the record's.

**Where 0 < σ < 1 enters.** The large-scale factor (ℓ/Δ)^(1−σ) vanishes as
Δ/ℓ → ∞ only if σ < 1. The small-scale factor (δ/ℓ)^(2σ) vanishes as
δ/ℓ → 0 only if σ > 0. A field rough enough for σ ≤ 0 is not
ultraviolet-local, and one smooth enough for σ ≥ 1 is not
infrared-local, by this argument.

**Checked numerically** ([NOTE-tmp5es2s](../notes.d/NOTE-tmp5es2s.md)): on a synthetic one-dimensional
Gaussian field with σ₂ = 1/3, the L² share of the large-scale filtered
field in an increment fell as (r/Δ)^0.62, and that of the high-passed
field as (δ/r)^0.36. The predictions were 2/3 and 1/3. That is a check on
the increment estimates behind (21)–(22) for one field, not on
Navier–Stokes.

**What could have come out otherwise.** A flux built from the absolute
velocity, rather than from increments, would not have been bounded this
way. The large-scale velocity itself is not small, and sweeping by it is
non-local. The bound holds because the Galilean-invariant flux depends
only on increments within about ℓ, and the hypothesis makes increments
local.

## What this does not say

- **That turbulence satisfies (H).** The paper takes the scaling of
  structure functions, with 0 < σ_p < 1 and σ₃ ≈ 1/3, from experiment and
  simulation. It is not proved for Navier–Stokes solutions. The result is
  a conditional inequality.
- **That non-local contributions are a small fraction of the flux.**
  Turning the bounds into fractions needs |⟨Π_ℓ⟩| bounded below, of order
  ε, across the range. The paper assumes this ("it must be assumed that
  the mean flux is non-zero"). It is realistic in a forced
  constant-flux inertial range, and it is not shown here.
- **The 4/3 exponent.** Kraichnan's faster decay, ε(ℓ/Δ)^(1+ζ₁), rests on
  a decorrelation estimate and a multiplicative-cascade or fusion-rule
  ansatz. The paper calls this "plausible but non-rigorous". Its 512³
  simulation gives signed-flux slopes of 1.1 (large scales) and 1.9
  (small scales), which bracket 4/3 rather than confirm it.
- **Pointwise statements.** The paper's pointwise version uses local
  Hölder exponents, and the authors say themselves that this "cannot make
  precise statements about the fractional contributions". Only the
  space-averaged bounds are re-derived here.
- **Locality in space.** "Local" means local in scale: the flux across ℓ
  is set mainly by modes within a bounded ratio of ℓ. Transport of energy
  in space by sweeping is dominated by large scales, and the paper says
  so.
- **Weak coupling.** Adjacent scales are strongly coupled: in the
  integrated band budget, d/dt E_n = Π_(n−1) − Π_n, and in a constant-flux
  range the whole throughput ε crosses every scale ℓ_n, and by locality
  mostly between neighbouring bands. Locality says the coupling falls off with scale ratio, as a power
  of it, that is geometrically in band number. It does not say any band is
  weakly coupled to its neighbours.
- **Anything about units or organization.** The result concerns transfer
  between scales of one field. The decomposition into scales is the
  analyst's choice of filter, ratio and outer scale. Nothing in it picks
  out a subsystem, a boundary in space, or something that persists while
  its constituents are replaced. Reading flux as a form of unity is the
  exchange's move (A3, A5 of 2026-10-19), not the paper's.

## Connections

- **[THEORY-661](THEORY-661.md) and [CLAIM-157](../claims.d/CLAIM-157.md).** Near-decomposability is a block-diagonal
  interaction pattern with a gap: strong within blocks, weak, of order ε,
  between them. Scale locality is a banded pattern: strongest between
  neighbouring scales, decaying as a power of the scale ratio, with no gap
  anywhere along the chain. Cut the chain of bands anywhere and the flux
  across the cut is the whole throughput. So no contiguous group of scales
  is a gap-isolated block, and [CLAIM-157](../claims.d/CLAIM-157.md)'s test would find none. The two
  are different organizing principles. This contrast is the record's; the
  paper does not mention near-decomposability.
- **[QUESTION-tmpmz64i](../questions.d/QUESTION-tmpmz64i.md).** The paper provides what A5 required before any
  flux test: a balance law for a specified quantity, with an exact
  band-by-band budget (its (11) and the telescoping flux equations). It
  does not touch the question asked, whether a pattern of transfer picks
  out a unit.
- **[LIT-tmpko78q](../literature.d/LIT-tmpko78q.md).** Eyink (2005) holds the original proofs, including the
  pointwise and all-subsets versions this account does not re-derive.
- **[THEORY-tmp99aof](THEORY-tmp99aof.md) (Constantin, E and Titi).** The same Besov hypothesis
  makes the flux across ℓ at most of order ℓ^(3σ−1), which vanishes as
  ℓ → 0 when σ > 1/3. So the non-zero mean flux that this account's
  reading as fractions assumes is consistent only with σ₃ ≤ 1/3, and
  Kolmogorov's 1/3 is the largest exponent at which a cascade can carry
  energy to arbitrarily small scales.
