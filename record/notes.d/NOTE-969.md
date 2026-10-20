---
number: 969
status: Read
formerly:
- NOTE-tmp5es2s
paper: LIT-1239
title: 'Eyink and Aluie — Localness of energy cascade I'
version: 1
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Read in full from arXiv:0909.2386v1 (13 September 2009), 26 pages, text
    extracted with pdftotext: the abstract, §I, §II.A–B, §III.A–C, §IV,
    Appendix 1 (filter kernels with compact spectral support) and
    Appendix 2 (band-pass decomposition of quadratic integrals). The
    published version (Phys. Fluids 21, 115107) was not compared. Several
    displayed equations lost their overbars and tildes in extraction; they
    were reconstructed from the prose and the definitions, and the key
    ones re-derived. Figures 1–2 (log-log flux decay) were read from their
    captions and the fitted slopes stated there; Figures 3–4 are plots of
    the Appendix 1 kernel. The proofs the paper refers to are in Eyink
    (2005), LIT-1252, which was not read.
date: '2026-10-20'
summary: >-
  Builds an exact band-pass decomposition of kinetic energy from smooth
  filters, a multiscale Germano identity, in which each band's energy
  changes by the flux into it minus the flux out. It then restates, with
  heuristic sketches, Eyink's (2005) bounds: under a scaling hypothesis on
  velocity increments with exponents strictly between 0 and 1, the mean
  energy flux across ℓ takes at most O((ℓ/Δ)^(2/3)) from scales above Δ
  and O((δ/ℓ)^(2/3)) from scales below δ. It argues, without proof, and
  checks on one 512³ simulation, that sign cancellations give Kraichnan's
  faster 4/3 decay. Locality here is in scale, for one field. Nothing in
  it bears on units.
---
<!-- inactive-ok-file: LIT-1252 LIT-1243 — Deferred; works registered unread, cited as open, nothing here rests on them -->
<!-- inactive-ok-file: CLAIM-157 CLAIM-331 THEORY-257 — Proposed; open claims and readings this reading bears on, nothing here rests on their being settled -->
# NOTE-969: Eyink and Aluie — Localness of energy cascade I

## Contribution

Two things. First, an exact decomposition of the kinetic energy (or any
quadratic integral) into band-pass contributions at a geometric sequence
of scales ℓ_n = ρ^(−n)L, using smooth filters. It generalizes the Germano
identity, has no off-diagonal terms, and gives a band budget in which the
fluxes telescope. Second, the observation that the fluxes in this budget
are exactly the low-pass fluxes Π_ℓ that Eyink (2005) proved scale-local,
so his bounds carry over to band-to-band transfer. The bounds themselves
are restated here with heuristic sketches, not proved. A third part
argues, with simulation support, why the rigorous exponent 2/3 is smaller
than Kraichnan's 4/3.

## Key insight

The Galilean-invariant energy flux across a scale ℓ, Π_ℓ = −∇u_ℓ : τ_ℓ,
depends on the velocity only through increments δu(r) over separations up
to about ℓ. If increments are scale-local, as they are when they scale
like r^σ with 0 < σ < 1, then so is the flux. The large scales enter only
through their gradients, which are smaller than the gradients at ℓ by
(ℓ/Δ)^(1−σ). The small scales enter only through their amplitudes, which
are smaller by (δ/ℓ)^σ. Locality is a consequence of roughness of the
right degree. A smooth field (σ ≥ 1) would lose infrared locality, and a
field that does not decay with scale (σ ≤ 0) would lose ultraviolet
locality.

## Assumptions

- **Filters.** G is real, smooth, rapidly decaying, with ∫G = 1, ∫rG = 0
  and ∫|r|²G = O(1). Its dilation is G_ℓ(r) = ℓ^(−d)G(r/ℓ). G ≥ 0 is
  needed to read u_ℓ as a local average and for the band energy densities
  to be non-negative pointwise. The simple form (11) of the band
  decomposition needs an **S-type** kernel, Ĝ(k) = 1 for |k| < 1 and 0
  for |k| > ρ, which Appendix 1 shows can be C^∞ in k (so G decays faster
  than any power) but **cannot be non-negative**.
- **Logarithmic bands.** Scales ℓ_n = ρ^(−n)L with ρ > 1. The authors
  stress that the results are for graded filters on logarithmic bands;
  sharp spectral filters and linear bands are left to Part II.
- **Incompressible Navier–Stokes**, with ν → 0 and finite total energy, so
  viscous terms drop out of every band except the last.
- **The scaling hypothesis (20):** ‖δu(r)‖_p ∼ u_rms A_p (r/L)^(σ_p),
  σ_p = ζ_p/p, with 0 < σ_p < 1 and σ₃ = 1/3, "indicated" by experiments
  and simulations (Besov regularity). For the pointwise version: local
  Hölder continuity |δu(x; r)| = O(r^h) with 0 < h < 1.
- **Non-zero mean flux:** ⟨Π_ℓ⟩ of order ε across the range, needed to
  read the bounds as fractions. Called "completely realistic" in a
  constant-flux inertial range.
- **For §III.B only:** homogeneity or isotropy, so ⟨∇u⟩ = 0; ergodicity to
  trade space averages for time averages; a correlation coefficient
  between strain at Δ and stress at ℓ of order S(Δ)/S(ℓ); and a
  multiplicative-cascade or fusion-rule ansatz for multiscale structure
  functions.

## Key results

- **Subgrid budget (4), (5), (7).** Filtering Navier–Stokes gives
  ∂_t u_ℓ + (u_ℓ·∇)u_ℓ = −∇p_ℓ − ∇·τ_ℓ + νΔu_ℓ with
  τ_ℓ = (uu)_ℓ − u_ℓu_ℓ. The flux Π_ℓ = −∇u_ℓ : τ_ℓ is a sink in the
  large-scale energy budget and a source in the small-scale one. All other
  non-viscous terms are divergences, i.e. transport in space.
- **Band energy (8).** Between scales ℓ < ℓ̃,
  k_[ℓ,ℓ̃] = ½τ̃(ū, ū), whose space integral is
  (2π)^(−d) ∫ d^dk ½|û(k)|² |Ĝ(kℓ)|² [1 − |Ĝ(kℓ̃)|²]. It is non-negative
  pointwise when G ≥ 0. Its budget (9) has a flux into scales below ℓ̃ and
  a flux out of scales below ℓ.
- **Multiscale Germano identity (Appendix 2, (A-1)).** For any f, g and
  N ≥ 0, with f^(N,n) = G_n ∗ G_(n+1) ∗ … ∗ G_N ∗ f,
  ∫fg = ∫f^(N,0)g^(N,0) + Σ_(n=1..N) ∫τ_(n−1)(f^(N,n), g^(N,n)) + ∫τ_N(f, g).
  Re-derived here: since f^(N,n−1) = G_(n−1) ∗ f^(N,n) and ∫ of a filtered
  quantity equals ∫ of the quantity, each band term is
  ∫f^(N,n)g^(N,n) − ∫f^(N,n−1)g^(N,n−1), and the sum telescopes. For an
  S-type kernel, f^(N,n) = f^n (the finer filters act as the identity on
  the coarser one's support), which gives (11):
  ½∫|u|² = ½∫|u_0|² + Σ_(n=1..N) ½∫τ_(n−1)(u_n; u_n) + ½∫τ_N(u; u).
- **Band budget.** (d/dt)∫½|u_0|² = −∫Π_0;
  (d/dt)∫½τ_(n−1)(u_n; u_n) = ∫Π_(n−1) − ∫Π_n for n = 1, …, N;
  (d/dt)∫½τ_N(u; u) = ∫Π_N − ν∫τ_N(u_(i,j), u_(i,j)). The transfer into
  band n is T_n = Π_(n−1) − Π_n, so it is local if Π_(n−1) and Π_n are.
- **Locality, defined (§III.A).** Π_ℓ is *infrared local* if replacing u in
  any subset of its three arguments by u_Δ gives a result ≪ Π_ℓ when
  Δ ≫ ℓ, and *ultraviolet local* if replacing by u′_δ = u − u_δ gives a
  result ≪ Π_ℓ when δ ≪ ℓ. Scale-local means both.
- **Increment estimates (14)–(22).** ∇u_ℓ ∼ δu(ℓ)/ℓ, τ_ℓ ∼ δu(ℓ)²,
  u′_ℓ ∼ δu(ℓ). Pointwise: δu_Δ(x; r) = O(rΔ^(h−1)), smaller than the full
  increment by (r/Δ)^(1−h); δu′_δ(x; r) = O(δ^h), smaller by (δ/r)^h. In
  L^p mean: ‖δu_Δ(r)‖_p = O(rΔ^(σ_p−1)) and ‖δu′_δ(r)‖_p = O(δ^(σ_p)), so
  scales above Δ contribute a fraction O((ℓ/Δ)^(1−σ_p)) and scales below δ
  a fraction O((δ/ℓ)^(σ_p)). *Holds when:* 0 < h < 1 (pointwise) or
  0 < σ_p < 1 (mean).
- **Flux bounds (23)–(24).** ⟨Π_ℓ(u_Δ, u, u)⟩ = O(ε(ℓ/Δ)^(1−σ₃)) and
  ⟨Π_ℓ(u, u′_δ, u′_δ)⟩ = O(ε(δ/ℓ)^(2σ₃)), by Hölder's inequality
  |⟨fgh⟩| ≤ ‖f‖₃‖g‖₃‖h‖₃. With σ₃ = 1/3 both exponents are exactly 2/3.
  *Holds when:* the scaling hypothesis holds as an upper bound; read as a
  fraction of the flux, when also ⟨Π_ℓ⟩ ≈ ε ≠ 0. Re-derived step by step
  in [THEORY-754](../theory.d/THEORY-754.md), where the prefactor for general σ₃ is
  (u_rms³/L)(ℓ/L)^(3σ₃−1), which is ε only at σ₃ = 1/3.
- **Decorrelation estimates (§III.B, heuristic).** With a correlation
  factor S(Δ)/S(ℓ) between large-scale strain and small-scale stress,
  ⟨Π_ℓ(u_Δ, u, u)⟩ ∼ (ℓ/Δ²)⟨δu²(Δ)δu(ℓ)⟩ ∼ O(ε(ℓ/Δ)^(1+ζ₁)) with ζ₃ = 1,
  and the same exponent for the ultraviolet term. Under K41, ζ₁ = 1/3,
  which is Kraichnan's 4/3. Pointwise, isotropy of u′_δ inside the ball
  of radius ℓ would remove the leading part of the small-scale stress
  (the trace part does nothing against a traceless gradient), giving
  Π_ℓ(u, u′_δ, u′_δ) = O((δ/ℓ)^(1+h)Π_ℓ).
- **Simulation (§III.C).** 512³ pseudospectral DNS, Gaussian filters
  G_ℓ(r) = (π/ℓ²)^(3/2) exp(−π²r²/ℓ²), ℓ_K = 2π/K. Infrared, K = 100:
  fitted slopes 0.7 for the mean absolute flux and 1.1 for the mean signed
  flux, against 2/3 and 4/3. Ultraviolet, K = 4: 0.9 absolute and 1.9
  signed. The gap between absolute and signed slopes is the cancellation
  the authors predict.
- **Kernel construction (Appendix 1).** A C^∞, compactly supported Ĝ with
  G and Ĝ both positive (square a compactly supported bump's transform),
  and a C^∞ S-type Ĝ = 1 − (1/H̄)∫₀^k H, H a bump on (1, ρ). Every moment
  ∫|r|^(2n)G of an S-type kernel vanishes, so it takes negative values.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Kinetic energy splits exactly into non-negative band contributions on a geometric sequence of scales, with no off-diagonal terms, and each band's energy changes by Π_(n−1) − Π_n | strong for the identity; qualified for "non-negative" | (A-1) and (11), proved by telescoping; re-derived and checked numerically here. Pointwise non-negativity fails for the S-type kernels (11) needs (see Limitations) |
| C2 | The mean energy flux across ℓ receives at most O((ℓ/Δ)^(1−σ₃)) from scales above Δ and O((δ/ℓ)^(2σ₃)) from scales below δ | strong as a conditional inequality | sketched in §III.A, proved in Eyink (2005); re-derived in [THEORY-754](../theory.d/THEORY-754.md) from the scaling hypothesis |
| C3 | Turbulent energy transfer is therefore scale-local, "assuming only the scaling properties expected in a turbulent inertial-range" | moderate | C2 plus two hypotheses not proved for Navier–Stokes: 0 < σ_p < 1 and a non-zero mean flux |
| C4 | Band-to-band transfers are local in both scale and space | moderate in scale (via C2); weak in space | space-locality rests on the pointwise Hölder sketch, which the authors say gives no fractional statement |
| C5 | Kraichnan's faster 4/3 decay is due to cancellation of signed non-local contributions under space averaging | moderate | heuristic decorrelation and fusion-rule argument ("plausible but non-rigorous"); one 512³ DNS whose signed slopes are 1.1 and 1.9 |
| C6 | Locality holds pointwise for individual realizations, and without it small-scale universality would have "scant basis" | weak as stated | the pointwise bounds are O(r^h) estimates at points of Hölder exponent h; the paper itself says they give no fractional statement |
| C7 | The SGS flux defined with the subtracted stress is the unique pointwise Galilean-invariant definition | weak | asserted, not proved |
| C8 | Because the decay is a power of the scale ratio, i.e. only exponential in band number, the cascade is "leaky" and very long inertial ranges may be needed for universality | moderate | follows from the size of the bounds; the inference to universality is the authors' |

## Method

1. Filter Navier–Stokes with a smooth kernel, and write the large- and
   small-scale energy budgets in Germano's moment notation.
2. Band-pass by differences of filters, and prove the multiscale Germano
   identity by telescoping. With an S-type kernel this gives a
   diagonal band decomposition and a band budget with telescoping fluxes.
3. Express ∇u_ℓ, τ_ℓ and u′_ℓ through increments; bound large-scale
   increments by Taylor expansion of the smooth u_Δ, and small-scale ones
   by the size of u′_δ; combine by Hölder's inequality (from Eyink 2005).
4. Estimate signed contributions with a decorrelation factor and a
   multiscale-structure-function ansatz; compare with absolute
   contributions in a DNS with Gaussian filters.

## Concepts

- **Smooth coarse-graining**: convolution with a smooth, rapidly decaying,
  normalized kernel, which resolves the field in space and scale at once.
- **S-type kernel**: Ĝ(k) = 1 for |k| < 1 and 0 for |k| > ρ, smooth in
  between. Successive dilations by ρ then nest exactly. Never
  non-negative in physical space.
- **Energy flux Π_ℓ**: −∇u_ℓ : τ_ℓ(u, u), the subgrid-scale energy flux,
  a triple product Π_ℓ(u, v, w) = −∇u_ℓ : τ_ℓ(v, w) in which each argument
  can be filtered separately.
- **Infrared / ultraviolet locality**: the flux is insensitive to
  replacing any of its arguments by the part above Δ ≫ ℓ, or by the part
  below δ ≪ ℓ, respectively.
- **Scale-local**: both. A statement about which scales set the transfer
  across ℓ, not about where in space it happens.
- **Ultralocal transfer**: the authors' name for "local transfer by
  non-local triads", transfer between wavenumbers differing by a fixed
  k₀ ≈ 1/L, which they distinguish from locality at fixed ratio.
- **Leakiness / diffuseness**: the slow, power-law decay of non-local
  contributions with scale ratio.

## Connections

It extends Eyink (2005), [LIT-1252](../literature.d/LIT-1252.md), from low-pass to band-pass
decompositions, and generalizes Germano (1992)'s identity. It answers
Cheskidov, Constantin, Friedlander and Shvydkoy (2008), whose band
decomposition keeps off-diagonal terms, and the DNS studies of Alexakis,
Mininni and Pouquet that report non-local transfer, against Domaradzki and
Carati's, which report locality. The decorrelation argument follows
Kraichnan (1966, 1971) and Tennekes and Lumley (1972). Part II (Aluie and
Eyink, sharp spectral filters and linear bands) is not filed.

## Bearing on the record

- **[THEORY-754](../theory.d/THEORY-754.md)** is filed from this reading, Active: the conditional
  mean bounds C2, re-derived step by step. It holds them as an inequality
  from a hypothesis, not as a fact about turbulence.
- **[THEORY-661](../theory.d/THEORY-661.md) and [CLAIM-157](../claims.d/CLAIM-157.md): scale locality is a different organizing
  principle from near-decomposability.** The paper does not mention
  near-decomposability; the comparison is the record's. Near-decomposability
  is a block pattern with a gap: strong inside, weak (order ε) across.
  Scale locality is a banded pattern: coupling strongest between
  neighbouring scales and decaying as a power of the scale ratio, with no
  gap. In the band budget, the whole throughput ε crosses every inertial
  scale. So no contiguous group of bands is weakly coupled to the rest,
  and [CLAIM-157](../claims.d/CLAIM-157.md)'s test would find no block among scales. What the paper
  establishes is that the coupling decays with distance in scale; what it
  does not establish is any weak coupling. This supports the premise
  [QUESTION-219](../questions.d/QUESTION-219.md) and [CLAIM-157](../claims.d/CLAIM-157.md)'s note of 2026-10-19 take from A3, in
  that form. Those entries say "unread" and can now cite this reading.
  They should also say that the proofs are Eyink (2005)'s and that
  locality is conditional on the scaling hypothesis.
- **[QUESTION-219](../questions.d/QUESTION-219.md).** The paper meets A5's precondition for any flux
  test, "a balance law for a specified transferred quantity": energy, with
  an exact band budget and Galilean-invariant fluxes. It does not touch the
  question itself. Π_ℓ is a field at each scale of one velocity field. It
  is not a unit, has no spatial boundary, and nothing in the paper concerns
  persistence under replacement of constituents, self-restoration or
  dependence on internal organization (A5's tests 1–4). The bands are
  chosen by the analyst (G, ρ, L), not found. "Flux as a form of unity" is
  A3's and A5's reading, and nothing in this paper argues for it.
- **A3's description** in the LIT ("a proof that coupling across a
  hierarchy of scales is local") overstates this paper's share. The proof
  is Eyink (2005)'s and is conditional. What this paper adds is the band
  decomposition, the transfer to band-pass fluxes, and the decorrelation
  account. Eyink (2005) should be read before anything rests on the
  pointwise statements.
- **[CLAIM-331](../claims.d/CLAIM-331.md) (higher levels slower).** Not addressed. The paper says
  nothing about time scales across bands beyond strain rates S(ℓ) ∼
  δu(ℓ)/ℓ in the heuristic section.
- **[THEORY-257](../theory.d/THEORY-257.md) and [QUESTION-218](../questions.d/QUESTION-218.md).** The bands are not dynamically
  closed: each band's energy is driven by the flux from above. The paper
  offers no closed coarse variable; large-eddy closure is a separate
  literature.
- **Information transfer across scales.** Nothing here; A3's caution
  against identifying energy and information transfer ([LIT-1243](../literature.d/LIT-1243.md))
  stands.

No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- **The rigorous bounds are not proved here.** §III.A gives order-of-
  magnitude sketches ("For rigorous details, see Eyink (2005)"). The
  abstract's "we derive rigorous upper bounds" and the introduction's "by
  deriving rigorous upper bounds" overstate what this paper does. Its
  contribution to the bounds is noticing that its band fluxes are Eyink's
  Π_ℓ.
- **Conditional, not established for Navier–Stokes.** "Assuming only the
  scaling properties expected" is two assumptions: 0 < σ_p < 1, and a
  non-zero mean flux. Neither is proved for Navier–Stokes solutions. The
  bounds are rigorous inequalities from them.
- **Positivity and S-type kernels.** §II.B says the decomposition (11)
  "contains only non-negative, diagonal terms". The integrated band terms
  are non-negative when |Ĝ| decreases with |k|, as the Appendix 1
  construction does. But (11) needs an S-type kernel, which Appendix 1
  shows cannot be non-negative, so the pointwise positivity stated for
  G ≥ 0 does not apply to it. Checked here on a one-dimensional random
  field: with the Appendix 1 S-type kernel (ρ = 2), the band energy
  density τ₀(u₁, u₁) was negative at 38% of points, while the integrated
  terms were positive and the identity held to 2 × 10⁻¹⁵. With a Gaussian
  kernel and the general form (A-1) the density stayed positive.
- **Normalization by ε.** (23) and (24) are written with ε. That is right
  only when σ₃ = 1/3 exactly; the paper says it assumed this. "Very close
  to 2/3" is exactly 2/3 under that assumption.
- **Pointwise locality.** The conclusions' "Fortunately, this is not the
  case" (that non-local triads are not sizable pointwise) rests on Hölder
  estimates which, by the paper's own §III.A, "cannot make precise
  statements about the fractional contributions". The pointwise claim C6
  is stronger than what is shown.
- **Triadic decomposition.** "It follows that transfer for non-local
  modal triads is negligibly small" is asserted without defining triadic
  contributions for smooth filters.
- **The simulation supports less than "confirmed".** One 512³ run, one
  filter (Gaussian, not S-type), one K each way. The ultraviolet
  comparison measures ∇u_ℓ,ℓ : u′u′, the form derived for S-type kernels,
  with a Gaussian. The signed slopes 1.1 and 1.9 bracket 4/3. The
  absolute-flux slopes (0.7, 0.9) do respect the 2/3 bounds.
- **Re-checks.** On a synthetic one-dimensional Gaussian field with
  σ₂ = 1/3 (65 536 points), the L² share of u_Δ in an increment at
  separation r fell as (r/Δ)^0.62 for Δ/r from 2 to 16, and that of u′_δ
  as (δ/r)^0.36 for r/δ from 2 to 32. The predictions are 2/3 and 1/3.
  This checks the increment estimates for one field, not anything about
  Navier–Stokes.

## Open questions

- Do Navier–Stokes solutions satisfy 0 < σ_p < 1 with a non-zero mean
  flux? That is the open regularity question behind Onsager's 1/3, and
  only a proof about the equations would close it.
- Can the 4/3 exponent be made rigorous, by bounding the correlation of
  strain at Δ with stress at ℓ?
- Part II's question: does locality survive sharp spectral filters and
  linear bands, where "local transfer by non-local triads" is reported?
- For the record: is there a coarse-graining of the scale chain itself, a
  closed description of a range of bands, and would it be a block? The
  paper gives the budget such a question needs and does not ask it.
