---
status: Active
title: 'A weak solution of the incompressible Euler equations on the periodic box that lies in L³(0,T; B^α_{3,∞}) ∩ C([0,T]; L²) with α > 1/3 conserves kinetic energy, because the energy flux into scales below a mollification scale ε is bounded by Cε^(3α−1)∫‖u‖³ and so vanishes as ε → 0; this does not show that rougher solutions dissipate'
version: 1
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Filed Active from NOTE-tmpqux8d, a full reading of the authors'
    manuscript. The theorem and its proof are the paper's. Every step is
    re-derived below, including the three the paper leaves to the reader
    (the time mollification, the pressure, and the limit of the mollified
    energy), and the misprinted middle line of its final estimate is
    corrected. That meets the condition for Active under ADR-047 v2. The
    identity (10) and the scalings (7), (8) and (12) were also checked
    numerically on a synthetic field. The comparison with THEORY-tmpfcxzq
    and the shear-flow example are the record's.
tags:
- mathematics
- natural-sciences
date: '2026-10-20'
source:
- LIT-tmpeyk8p
summary: >-
  Constantin, E and Titi (1994), [LIT-tmpeyk8p](../literature.d/LIT-tmpeyk8p.md), read in [NOTE-tmpqux8d](../notes.d/NOTE-tmpqux8d.md). The
  positive half of Onsager's conjecture, in the Besov form: if velocity
  increments obey ‖u(·+y) − u‖_{L³} ≤ C|y|^α with α > 1/3, integrated in
  time, the coarse-grained energy flux across scale ε is O(ε^(3α−1)) and
  no energy can be lost to vanishing scales. It is a statement about
  regular fields only. It does not show that a flux survives the limit for
  rougher ones: that dissipative solutions exist below 1/3 is a later
  theorem (Isett 2018 and others), which the record has not read, and some
  rough solutions conserve energy anyway.
---
<!-- inactive-ok-file: LIT-tmpko78q — Unavailable; Eyink 2005, cited for where finer versions of the same estimate are proved, nothing here rests on it -->
<!-- inactive-ok-file: CLAIM-157 — Proposed; the block criterion named for context, nothing here rests on it -->
# THEORY-tmp99aof: A weak solution of the incompressible Euler equations on the periodic box that lies in L³(0,T; B^α_{3,∞}) ∩ C([0,T]; L²) with α > 1/3 conserves kinetic energy, because the energy flux into scales below a mollification scale ε is bounded by Cε^(3α−1)∫‖u‖³ and so vanishes as ε → 0; this does not show that rougher solutions dissipate

## Source

Constantin, E and Titi (1994), *Communications in Mathematical Physics*
165:207–209, [LIT-tmpeyk8p](../literature.d/LIT-tmpeyk8p.md), read in full in [NOTE-tmpqux8d](../notes.d/NOTE-tmpqux8d.md) from the
authors' manuscript. The theorem and the proof are the paper's; the
derivation below follows it and fills in what it leaves out.

## What was actually shown

**Setting.** D = [0, 1]³ with periodic boundary conditions; ‖·‖_p is the
L^p(D) norm. u is divergence-free and satisfies the weak Euler equations
(1): for every smooth ψ with compact support in time,

  −∫∫u_j ∂_tψ_j − ∫u_j(x, 0)ψ_j(x, 0) − ∫∫∂_iψ_j u_iu_j − ∫∫∂_iψ_i p = 0.

**Hypothesis.** u ∈ C([0, T]; L²) and u ∈ L³(0, T; B^α_{3,∞}) with
1/3 < α < 1, where ‖u‖_{B^α_{3,∞}} = ‖u‖₃ + sup_y |y|^(−α)‖u(·+y) − u‖₃.
(For α ≥ 1 the field lies in B^β_{3,∞} for every β < 1, so take β in
(1/3, 1).) φ ≥ 0 is smooth, supported in the unit ball, ∫φ = 1;
φ_ε(x) = ε^(−3)φ(x/ε) and v^ε = φ_ε ∗ v.

**Step 1. The Besov facts.** Write δ_yu(x) = u(x − y) − u(x).

- (6) ‖δ_yu‖₃ ≤ |y|^α‖u‖_{B^α_{3,∞}}: the definition.
- (7) u^ε(x) − u(x) = ∫φ_ε(y)δ_yu(x) dy, since ∫φ_ε = 1. By Minkowski's
  inequality, ‖u^ε − u‖₃ ≤ ∫φ_ε(y)‖δ_yu‖₃ dy ≤ ε^α‖u‖, because
  |y| ≤ ε on the support.
- (8) ∇u^ε(x) = ∫∇φ_ε(y)u(x − y) dy = ∫∇φ_ε(y)δ_yu(x) dy, since
  ∫∇φ_ε = 0. So ‖∇u^ε‖₃ ≤ ∫|∇φ_ε(y)| |y|^α dy ‖u‖ ≤ ε^(α−1)‖∇φ‖₁‖u‖,
  using ∇φ_ε(y) = ε^(−4)(∇φ)(y/ε).

**Step 2. The commutator identity (10).** Define
r_ε(x) = ∫φ_ε(y) δ_yu(x)⊗δ_yu(x) dy. Expanding the product,

  r_ε = (u⊗u)^ε − u^ε⊗u − u⊗u^ε + u⊗u,

using ∫φ_ε = 1 for the last term. Adding u^ε⊗u^ε and subtracting
(u − u^ε)⊗(u − u^ε) = u⊗u − u⊗u^ε − u^ε⊗u + u^ε⊗u^ε leaves (u⊗u)^ε.
So, pointwise,

  (u⊗u)^ε = u^ε⊗u^ε + r_ε − (u − u^ε)⊗(u − u^ε),

and the subgrid stress τ_ε = (u⊗u)^ε − u^ε⊗u^ε equals
r_ε − (u − u^ε)⊗(u − u^ε): quadratic in increments over distances
below ε.

**Step 3. The bound (12) on r_ε.** By Minkowski in L^{3/2}, and
‖a⊗a‖_{3/2} ≤ ‖a‖₃², ‖r_ε‖_{3/2} ≤ ∫φ_ε(y)‖δ_yu‖₃² dy ≤ ε^(2α)‖u‖².
Likewise ‖(u − u^ε)⊗(u − u^ε)‖_{3/2} ≤ ‖u − u^ε‖₃² ≤ ε^(2α)‖u‖², by (7).
So ‖τ_ε‖_{3/2} ≤ 2ε^(2α)‖u‖².

**Step 4. The mollified energy balance (11).** Take
ψ(z, t) = θ(t)φ_ε(x − z)e_j in (1), for fixed x and θ smooth with compact
support in (0, T). This gives, in the sense of distributions in t,

  ∂_t u^ε_j(x, t) + ∂_i(u_iu_j)^ε(x, t) + ∂_j p^ε(x, t) = 0.

The pressure: taking ψ = ∇χ with χ smooth in x gives
−Δp = ∂_i∂_j(u_iu_j) up to a function of t alone, which has no gradient,
so ∇p is determined and lies in W^{−1,3/2} in space; then ∇p^ε is smooth in
x and in L^{3/2} in t. So ∂_t u^ε ∈ L^{3/2}(0, T; L²), u^ε is absolutely
continuous in time with values in L², and

  (d/dt) ½∫|u^ε|² = ∫u^ε·∂_tu^ε = −∫u^ε_j ∂_i(u_iu_j)^ε − ∫u^ε·∇p^ε.

The pressure term is ∫p^ε ∇·u^ε = 0, since mollification commutes with
divergence. Integrating the other by parts on the torus,

  (d/dt) ½∫|u^ε|² = ∫(u_iu_j)^ε ∂_iu^ε_j,

which is the paper's ∫Tr((u⊗u)^ε ∇u^ε), the stress being symmetric.
Integrated from 0 to t, this is (11). The paper's u^ε(·, 0) is
φ_ε ∗ u(·, 0), the initial datum, because u ∈ C([0, T]; L²).

**Step 5. The resolved part carries no flux.** Since ∇·u^ε = 0,
∫u^ε_iu^ε_j ∂_iu^ε_j = ∫u^ε_i ∂_i(½|u^ε|²) = −∫(∇·u^ε)½|u^ε|² = 0. So by
Step 2 the right side of Step 4 is ∫τ_ε : ∇u^ε, the flux through the
subgrid stress.

**Step 6. Hölder.** |∫τ_ε : ∇u^ε| ≤ ‖τ_ε‖_{3/2}‖∇u^ε‖₃ ≤
2ε^(2α)‖u‖² · Cε^(α−1)‖u‖ = Cε^(3α−1)‖u(t)‖³_{B^α_{3,∞}}. Integrating
in time,

  |∫|u^ε(t)|² − ∫|u^ε(0)|²| ≤ Cε^(3α−1)∫₀ᵗ‖u(τ)‖³_{B^α_{3,∞}} dτ,

finite because u ∈ L³(0, T; B^α_{3,∞}). The manuscript's middle line,
with exponents 2/3 and 1/3, is a misprint: it is not homogeneous in u
(degree 5/3 against the cubic left side) and would give ε^((5α−1)/3). The
line written here is what Hölder gives, and it gives the paper's last
line.

**Step 7. The limit.** For each t, u(t) ∈ L², so u^ε(t) → u(t) in L² as
ε → 0, and ∫|u^ε(t)|² → ∫|u(t)|². The right side of Step 6 tends to 0
exactly when 3α − 1 > 0. Hence ∫|u(t)|² = ∫|u(0)|² for every t in
[0, T).

**What could have come out otherwise.** The exponent 3α − 1 is fixed by
counting: the flux is cubic in u, two factors are increments over
distance ε (each ε^α) and one is a gradient at scale ε (ε^(α−1)). Had the
resolved part u^ε⊗u^ε not dropped out in Step 5, it would contribute a
term with no small factor, and nothing would follow. It drops out because
transport of resolved energy by a divergence-free resolved field is a
divergence. At α = 1/3 the bound is of order one at every ε, which is
where Kolmogorov's scaling (4) puts turbulence.

**Checked numerically.** On a synthetic divergence-free periodic field in
two dimensions (512², spectrum chosen for α ≈ 1/2), with a smooth bump
mollifier at ε = 2 to 32 grid points: identity (10) held to a relative
error of 10⁻¹⁴; ∫u^ε⊗u^ε : ∇u^ε was zero to rounding; and the fitted
exponents of ‖r_ε‖_{3/2}, ‖u − u^ε‖₃ and ‖∇u^ε‖₃ in ε were 1.06, 0.59 and
−0.52, against 2α = 1, α = 0.5 and α − 1 = −0.5. The flux itself was far
below the bound, as a field with random phases should give. This checks
the algebra and the estimates, not the theorem.

## What this does not say

- **That rough solutions dissipate.** The theorem is one-directional.
  Below 1/3 it gives nothing: neither conservation nor dissipation. Some
  rough solutions conserve energy. The shear flow u = (f(x₂), 0, 0) is a
  stationary weak solution for any f in L², however rough, and its flux is
  zero at every ε, since the only non-zero entry of (u⊗u)^ε, (f²)^ε in
  position (1, 1), meets ∂₁u^ε₁ = 0. The existence of energy-dissipating
  weak solutions below 1/3, the negative half, is Isett's (2018) theorem
  for Hölder exponents below 1/3, after De Lellis and Székelyhidi, with
  Buckmaster, De Lellis, Székelyhidi and Vicol (2019) for admissible
  solutions. None of these is held or read by the record. So "a
  coarse-grained flux can survive as the scale goes to zero for rough
  fields" is true, but on that later evidence, not on this paper.
- **That turbulence dissipates energy, or does not.** The theorem is
  about Euler weak solutions. The paper's "physical interpretation", that
  ⟨|δu(r)|³⟩^(1/3) ≤ Cr^α with α > 1/3 forces ε̄ = 0, moves to viscous
  Navier–Stokes and to ensemble averages without a proof. Read the other
  way, as Onsager did: a non-zero dissipation in the limit of vanishing
  viscosity requires the limiting field to be no smoother than 1/3 in
  this sense. That reading also needs the passage from Navier–Stokes to
  Euler.
- **The endpoint α = 1/3.** The bound is constant there and decides
  nothing. Conservation slightly below B^{1/3}_{3,∞} is a later result.
- **Where energy is lost.** Only the total energy is controlled. A local
  balance with a dissipation measure is Duchon and Robert's (2000).
- **Anything about the scales that carry the flux.** The bound is on the
  whole flux across ε. Which scales above and below ε contribute it is
  [THEORY-tmpfcxzq](THEORY-tmpfcxzq.md)'s question, under a hypothesis of the same form.
- **Anything about units or organization.** One field, one balance law,
  a scale ε chosen by the analyst.

## Connections

- **[THEORY-tmpfcxzq](THEORY-tmpfcxzq.md).** Its hypothesis ‖δu(r)‖₃ ≤ C₀u_rms(r/L)^σ is the
  B^σ_{3,∞} condition, and its three norm bounds are Steps 1 and 3 here.
  Its prefactor (u_rms³/L)(ℓ/L)^(3σ−1) is this theorem's ε^(3α−1): read
  as ℓ → 0 at a fixed field, it bounds the whole flux and vanishes for
  σ > 1/3. So the non-zero mean flux that Eyink and Aluie assume for
  locality to be read as a fraction is possible only at σ₃ ≤ 1/3, and
  Kolmogorov's 1/3 is the largest exponent that allows it. Together the
  two say: regularity above 1/3 removes the flux; at 1/3 it can persist,
  and is then local in scale. Neither shows that it does persist.
- **[QUESTION-tmpmz64i](../questions.d/QUESTION-tmpmz64i.md).** A3 cited this work for "the regularity of a
  field decides whether the unresolved scales vanish in the limit". This
  THEORY holds the half of that the paper proves. It does not answer the
  question, whether a pattern of transfer picks out a unit; it bears on
  A5's precondition, that a flux is defined by a balance law for a
  specified quantity, and on which fields can carry a flux to the
  smallest scales at all.
- **[LIT-tmpko78q](../literature.d/LIT-tmpko78q.md).** Eyink (2005) refines estimates of this kind into
  locality bounds; not read.
- **[THEORY-661](THEORY-661.md) and [CLAIM-157](../claims.d/CLAIM-157.md).** Unrelated: no blocks, no gap, no
  aggregation.
