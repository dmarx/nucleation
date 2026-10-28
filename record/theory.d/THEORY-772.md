---
number: 772
status: Proposed
formerly:
- THEORY-tmp6pe5a
promote_when: >-
  A reading recorded as Read that checks, step by step, the estimates this
  entry takes on trust: the inductive Proposition 2.11 of Giri, Kwon and
  Novack, that is, the estimates of their Sections 3–6 together with the
  results of the companion paper (Annals of PDE 10:19, 2024, with its errata)
  that Section 3 quotes without proof; or an independent complete proof of a
  weak Euler solution below 1/3 whose Duchon–Robert measure is a known
  nonnegative function. Acceptance by the journal, citation counts or later
  work that assumes the theorem do not count. The consequence for the
  coarse-grained flux, and the verification of the iteration's first step, are
  re-derived below and need nothing further once Proposition 2.11 is granted.
  A claim about the sign of the flux at a fixed positive scale, or about where
  the dissipation would sit in a vanishing-viscosity limit, is not covered by
  this entry and would need a different theorem.
title: 'For every β < 1/3 there is a weak solution of the 3D incompressible Euler equations on the periodic box, in C⁰_t(B^β_{3,∞} ∩ L^{1/(1−3β)}), whose Duchon–Robert dissipation is the smooth nonnegative density E(t, x) = −e(t)e′(t)ρ₀(x₁, x₂)² fixed at the construction''s first step; for such a solution the local coarse-grained energy flux into scales below ℓ converges, as ℓ → 0 and as a distribution in space and time, to E, so the transfer into vanishing scales is one-way at every place and time in the limit, nonzero inside a periodic array of pipes and zero outside them; where and how fast energy is dissipated is chosen by the construction, not forced by the equations, and nothing is shown about the sign at any positive scale'
version: 2
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Filed Proposed from NOTE-1022, a skim of the arXiv v3 text. The
    existence statement is the paper's Theorem 1.1; that the Duchon–Robert
    measure equals E is read from its proof (Proposition 2.11 and Step 2).
    The base case (Step 1) and the heuristic exponent counts of §1.2 were
    re-derived, the first symbolically; the identity of §5.1 and Lemma 6.10
    carrying E unchanged was followed. The estimates of Sections 3–6 and the
    companion paper were not checked, so the entry is not Active under
    ADR-047 v2. The consequence for the local flux, and the limits on what
    one-signed means here, are the record's.
- version: 2
  date: '2026-10-20'
  note: >-
    "Not Hölder, not bounded" adds Isett's α < 1/15 (THEORY-821) and contrasts where each construction puts its dissipation. The account is unchanged.
tags:
- mathematics
- natural-sciences
date: '2026-10-20'
source:
- LIT-1289
- LIT-1248
- LIT-1300
summary: >-
  Giri, Kwon and Novack (2023; Annals 2026), [LIT-1289](../literature.d/LIT-1289.md), skimmed in
  [NOTE-1022](../notes.d/NOTE-1022.md): the L³-based strong Onsager theorem. Below 1/3, in
  Constantin, E and Titi's own scale of spaces ([THEORY-749](THEORY-749.md)), there are
  weak Euler solutions satisfying the local energy inequality. In the proof
  the Duchon–Robert measure is a prescribed smooth function, positive in a
  periodic array of pipes and zero elsewhere. So the coarse-grained flux into
  vanishing scales is one-signed locally in space and time, in the limit, and
  not only for the whole box as in [THEORY-776](THEORY-776.md). Its location and rate are
  inputs of the construction; it is a smooth density on a few pipes, not
  concentrated on a thin set; nothing is said about the sign at a positive
  scale or about vanishing viscosity.
bears_on:
- QUESTION-219
---
<!-- inactive-ok-file: THEORY-821 — Proposed; Isett's Hölder flows with the local inequality, cited for contrast -->
<!-- inactive-ok-file: THEORY-776 THEORY-763 — Proposed; the whole-box dissipative and the two-signed accounts, cited for contrast -->
<!-- inactive-ok-file: NOTE-1022 — Skimmed; this entry's reading -->
# THEORY-772: For every β < 1/3 there is a weak solution of the 3D incompressible Euler equations on the periodic box, in C⁰_t(B^β_{3,∞} ∩ L^{1/(1−3β)}), whose Duchon–Robert dissipation is the smooth nonnegative density E(t, x) = −e(t)e′(t)ρ₀(x₁, x₂)² fixed at the construction's first step; for such a solution the local coarse-grained energy flux into scales below ℓ converges, as ℓ → 0 and as a distribution in space and time, to E, so the transfer into vanishing scales is one-way at every place and time in the limit, nonzero inside a periodic array of pipes and zero outside them; where and how fast energy is dissipated is chosen by the construction, not forced by the equations, and nothing is shown about the sign at any positive scale

## Source

Giri, Kwon and Novack, "The L³-based strong Onsager theorem", *Annals of
Mathematics* 204(1):265–421 (2026), [LIT-1289](../literature.d/LIT-1289.md), skimmed in
[NOTE-1022](../notes.d/NOTE-1022.md) from arXiv:2305.18509v3. The existence statement is its
Theorem 1.1, and the identity D[u] = E is in the proof of that theorem. The
coarse-grained energy balance is Constantin, E and Titi's ([LIT-1248](../literature.d/LIT-1248.md)),
re-derived in [THEORY-749](THEORY-749.md), taken here in its local form. The whole-box
predecessor is Buckmaster, De Lellis, Székelyhidi and Vicol ([LIT-1300](../literature.d/LIT-1300.md),
[THEORY-776](THEORY-776.md)).

## What was actually shown

**The theorem (Theorem 1.1).** "For any fixed β ∈ (0, 1/3) there exist weak
solutions to the Euler equations (1.1) which belong to
C⁰([0, T]; (B^β_{3,∞} ∩ L^{1/(1−3β)})(T³)), satisfy the local energy
inequality (1.6), and dissipate the total kinetic energy." Here (1.6) is

  ∂_t(½|u|²) + div((½|u|² + p)u) = −D[u] ≤ 0

in the sense of distributions, with D[u] the Duchon–Robert measure (1.5),
and B^β_{3,∞} the Besov space of (1.7): ‖u(· + z) − u‖_{L³} ≤ C|z|^β. The
paper calls this the L³-based strong Onsager conjecture, part (b); part (a),
the local energy equality above 1/3, is Duchon and Robert's.

**What the proof gives beyond the statement.** The inductive Proposition
2.11 takes a "continuous positive function E(t, x) ≥ 0" and carries it
unchanged from step to step in the relaxed local energy identity (2.8),

  ∂_t(½|u_q|²) + div((½|u_q|² + p_q)u_q) = (∂_t + û_q·∇)κ_q + div((R_q − π_q Id)û_q) + div φ_q − E,

whose error terms R_q, π_q, φ_q tend to zero (footnote 6: "The dissipation
measure E is the Duchon-Robert measure of the limiting solution"). The
first step fixes E. Step 1 of the proof takes

  u₀ = e(t)ρ₀(x₁, x₂)e₃,  e(t) = c·exp(−τ₀⁻¹(t + 1)),  p₀ = φ₀ = 0,

with ρ₀ a smooth function supported in a periodic family of straight pipes
along e₃ of thickness λ_{n̄−1}⁻¹, written as ρ₀ = div a for a vector field
a(x₁, x₂), with R₀ the trace-free matrix whose only nonzero entries are
e′(t)a₁, e′(t)a₂ in the third row and column, and π₀ a spatial constant.
Step 2 concludes, for the limit,

  ∂_t(½|u|²) + div((½|u|² + p)u) = e(t)e′(t)|ρ₀|² ≤ 0,

"In particular, the strict local energy inequality holds in the interior of
supp(ρ₀)". So D[u] = E = τ₀⁻¹e(t)²ρ₀(x₁, x₂)²: smooth, nonnegative,
independent of x₃, decaying in time at rate 2τ₀⁻¹, positive where ρ₀ ≠ 0 and
zero outside the pipes. The total energy satisfies
(d/dt)½∫|u|² = −τ₀⁻¹e(t)²∫ρ₀² < 0 at every time.

**How it is proved (read in outline; estimates not checked).** An L³-based
convex integration with intermittent pipe flows at the "Goldilocks"
intermittency r_q = λ_{q+n̄/2}/λ_{q+n̄}. Each new increment corrects only the
lowest-frequency stress and current errors (R_q^q, φ_q^q), so successive
increments overlap in frequency ("partial wavelet sums"); they are kept
apart in space by "intermittent Mikado bundles" placed to dodge earlier
pipes (Section 4), and every error is dominated pointwise by an
"intermittent pressure" π_q built in advance (Sections 2.4 and 6). The
proofs of Section 3 are in a companion paper (Giri, Kwon and Novack, Annals
of PDE 10:19, 2024, with errata on the third author's site).

**Checked here.**

- *The first step.* For u₀ = e(t)ρ₀e₃ with ρ₀ = div a, a = a(x₁, x₂), and
  R₀ as above: ∂_t u₀ + div(u₀⊗u₀) = div R₀, R₀ is trace-free, and
  ∂_t(½|u₀|²) + div(½|u₀|²u₀) = e e′ρ₀². With û₀ = 0, φ₀ = 0 and π₀ constant,
  the right side of (2.8) is −E, so E = −e e′ρ₀². Done symbolically (sympy)
  for generic a and e.
- *The heuristics of §1.2.* The Hölder Nash error gives
  (b − 1)(β(2b + 1) − 1) ≤ 0, β ≤ 1/(2b + 1); the Nash current error in a
  homogeneous scheme gives β ≤ 1/(3b + 1) → 1/4; with the extra factor
  r_{q+1}^{−2/3} of the L³ scheme the condition is
  (b − 1)(9bβ + 3β − b − 3)/3 ≤ 0, i.e. β ≤ (b + 3)/(3(3b + 1)) → 1/3 as
  b → 1. Checked symbolically. The extracted text of the last threshold is
  garbled; this is what its preceding line gives.
- *E is carried unchanged.* The algebra of (5.4)–(5.8) and of Lemma 6.10's
  (6.41), where the new errors and the time-only functions m(t) are absorbed
  into φ_{q+1} and R_{q+1} and −E passes through untouched, was followed.

**The consequence for the local flux (the record's).** u ∈ C([0, T]; L³)
and, from the paper, p ∈ C([0, T]; L^{3/2}). Mollify in space at scale ℓ.
Then u^ℓ is C¹ in time with values in smooth fields and

  ∂_t u^ℓ + div(u^ℓ⊗u^ℓ) + ∇p^ℓ = −div τ_ℓ,  τ_ℓ = (u⊗u)^ℓ − u^ℓ⊗u^ℓ.

Dotting with u^ℓ, using div u^ℓ = 0 and the symmetry of τ_ℓ:

  ∂_t(½|u^ℓ|²) + div((½|u^ℓ|² + p^ℓ)u^ℓ + τ_ℓu^ℓ) = τ_ℓ : ∇u^ℓ.

The right side is the local rate at which the resolved field u^ℓ gains
energy from scales below ℓ; its integral over T³ is [THEORY-749](THEORY-749.md)'s Π_ℓ. As
ℓ → 0, uniformly in t (the range of t ↦ u(t) is compact in L³):
|u^ℓ|² → |u|² in L^{3/2}; |u^ℓ|²u^ℓ → |u|²u and p^ℓu^ℓ → pu in L¹; and
τ_ℓ → 0 in L^{3/2}, so τ_ℓu^ℓ → 0 in L¹. Hence the left side tends in
distributions to ∂_t(½|u|²) + div((½|u|² + p)u) = −E, and so

  −τ_ℓ : ∇u^ℓ → E ≥ 0 in D′((0, T) × T³).

For every nonnegative test function ψ(t, x), the energy passed from the
resolved field to scales below ℓ in the region ψ weights tends to ∫ψE ≥ 0.
It is strictly positive whenever ψ's support meets the set where ρ₀ ≠ 0, and
zero when ψ is supported outside the pipes. The transfer is one-way at every
place and time in this sense, not only for the whole box.

What could have come out otherwise: by Duchon and Robert, D[u] = 0 for
solutions in C⁰_tB^α_{3,∞} with α > 1/3; and [THEORY-776](THEORY-776.md)'s solutions,
built in Hölder spaces with prescribed total energy, satisfy no proved local
sign at all.

## What this does not say

- **Not one-signed at any positive scale.** The convergence is of
  −τ_ℓ : ∇u^ℓ tested against fixed functions as ℓ → 0. At fixed ℓ the flux
  density may take both signs; backscatter at finite resolution is neither
  shown nor excluded. "One-way at every place" means that the limiting
  measure is nonnegative.
- **Not that the equations choose the place or the rate.** E is fixed by the
  first approximate solution and passes through the iteration unchanged.
  Proposition 2.11 accepts any continuous E ≥ 0 for which a starting triple
  exists, but the paper builds only this one, so the record cannot say which
  dissipation densities are attainable. In the same way that
  [THEORY-776](THEORY-776.md) chooses the total energy profile, this construction chooses
  the local dissipation density. The sign is not free here: E ≥ 0 is the
  local inequality the theorem was built to satisfy, and Proposition 2.11
  requires it.
- **Not the dissipation turbulence phenomenology expects.** The dissipation
  is a smooth density on a periodic array of straight pipes, set at the
  coarsest active scale, not a measure concentrated on a thin or fractal
  set. All the later, finer increments together contribute no net local
  dissipation in the limit. The paper motivates L³ and intermittency by
  structure-function exponents of turbulent velocity fields, and its
  solutions are intermittent in that sense; their dissipation is not.
- **Not that the solution is rough everywhere.** Nothing is shown about
  where u fails to lie in B^{1/3+}_{3,∞}. Where E > 0 it must be rough,
  since a local form of Duchon and Robert's estimate (not re-derived) gives
  D[u] = 0 wherever u is locally smoother than 1/3. Outside the pipes the
  record cannot say.
- **Not Hölder, not bounded.** u ∈ C⁰_t(B^β_{3,∞} ∩ L^p) for p = 1/(1 − 3β),
  which is finite for each β < 1/3. Hölder solutions with the local
  inequality are known, per the paper, only for β < 1/7 (De Lellis and
  Kwon), after Isett's α < 1/15 ([THEORY-821](THEORY-821.md), Proposed); Isett's
  strong C⁰ Onsager conjecture is left open. Both constructions prescribe
  the dissipation. Here it sits in pipes for all time; in Isett's it is
  uniform in space and confined to a final drain to zero.
- **Not Navier–Stokes.** The paper notes that L³ limits of suitable weak
  Navier–Stokes solutions satisfy the local inequality, so such flows "may"
  be inviscid limits. It does not show that these ones are.
- **Not uniqueness or an initial-value problem.** No datum is prescribed,
  and the energy is never at rest (e > 0).
- **Not a checked proof.** The estimates of Sections 3–6 and the companion
  paper's results quoted in Section 3 were not checked.

## Connections

- **[QUESTION-219](../questions.d/QUESTION-219.md): answers in part.** It removes the first qualification
  [THEORY-776](THEORY-776.md) put on the dissipative cascade. Below 1/3, a coarse-grained
  energy flux can survive the limit of vanishing scale and run one way into
  the small scales at every place and time, in the distributional sense, and
  not only for the whole box. The second qualification stands and is made
  sharper. The direction is fixed by the local inequality, and where and at
  what rate the transfer happens are fixed by the first step, so the dynamics
  selects nothing. On whether a pattern of transfer picks out a unit, the
  bearing is negative again. The set where the flux is nonzero is a
  periodic array of pipes the constructor placed. Inside it the rate is
  prescribed and decays exponentially. Nothing in it restores itself or
  depends on internal organization (A5's conditions (3) and (4)).
- **[THEORY-776](THEORY-776.md).** Its "What this does not say" names this paper for the
  local inequality. The two differ in class: Hölder C^β (BDSV) against L³
  Besov (here). They also differ in what is prescribed: the total energy
  e(t) against the local dissipation density E(t, x). Neither result
  contains the other.
- **[THEORY-749](THEORY-749.md).** The class C⁰_tB^β_{3,∞} lies in the L³_tB^α_{3,∞} of
  Constantin, E and Titi, so the 1/3 threshold is sharp in their own scale
  of spaces, for the local balance as well as the total.
- **[THEORY-763](THEORY-763.md).** Isett's flux takes both signs over time; BDSV's has one
  sign for the box; this one has one sign at every place, in the limit.
- **[THEORY-754](THEORY-754.md).** Eyink and Aluie's conditional locality concerns a
  non-zero flux through an inertial range of scales. This entry gives a
  non-zero, one-signed flux density but says nothing about how it is spread
  over scales.
