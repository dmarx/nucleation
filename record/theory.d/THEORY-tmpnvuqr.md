---
status: Proposed
promote_when: >-
  A reading recorded as Read that checks, step by step, the estimates this
  entry takes on trust: the stability and potential estimates of Section 3,
  the glued-stress bounds of Section 4 (Propositions 4.2–4.4), the perturbation
  bounds of Section 5 and the stress and energy iterates of Section 6
  (Propositions 6.1 and 6.2), either in this paper or in an independent
  complete proof of the same statement with a prescribed or strictly
  decreasing energy. Acceptance by the journal, citation counts or later work
  that assumes the theorem do not count. The consequence for the flux is
  re-derived below and needs nothing further once the theorem is granted. A
  claim that the transfer is one-way in space as well, at every point, is not
  covered by this entry and would need the local energy inequality, a
  different theorem.
title: 'For every β < 1/3 and every smooth, strictly positive and strictly decreasing energy profile e(t) on [0, T], there is a weak solution of the 3D incompressible Euler equations on the periodic box, Hölder-continuous of exponent β in space and time, with ∫|v(t)|² = e(t) at every time; for such a solution the energy flux across a mollification scale ε, integrated over any time interval, tends as ε → 0 to ½ times the drop in e, which is strictly negative, so energy leaves the resolved field for vanishing scales on every interval; this is one-way for the energy of the whole box, not at every point, and it is chosen by the prescribed profile, not forced by the equations'
version: 1
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Filed Proposed from NOTE-tmp18d5h, a full reading of the arXiv text.
    The existence theorem is the paper's Theorem 1.1. Its reduction to the
    inductive Proposition 2.1, the parameter inequality (2.38)–(2.39), the
    energy bookkeeping and the time-regularity argument were checked; the
    estimates of Sections 3–6 were followed and not each re-derived, so the
    entry is not Active under ADR-047 v2. The consequence for the flux, its
    sign on every interval, and the limits on what "admissible" means here
    are the record's, derived from the energy balance re-derived in
    THEORY-749.
tags:
- mathematics
- natural-sciences
date: '2026-10-20'
source:
- LIT-tmpv4d6t
- LIT-1248
- LIT-1255
answers:
- QUESTION-219
summary: >-
  Buckmaster, De Lellis, Székelyhidi and Vicol (2017; CPAM 2019),
  [LIT-tmpv4d6t](../literature.d/LIT-tmpv4d6t.md), read in [NOTE-tmp18d5h](../notes.d/NOTE-tmp18d5h.md): the admissible version of Isett's
  negative half of Onsager's conjecture ([THEORY-763](THEORY-763.md)). Any smooth positive
  energy profile can be imposed on a C^β solution, β < 1/3, so a strictly
  decreasing one gives solutions whose total energy only falls. Through
  [THEORY-749](THEORY-749.md)'s energy balance, the coarse-grained flux then runs into the
  vanishing scales on every time interval. That is the one-way transfer
  [THEORY-763](THEORY-763.md) could not give. It is one-way for the box as a whole, not at
  every point (no local energy inequality is proved); the same theorem gives
  increasing energy as readily, so the direction is a choice of the
  construction; and nothing ties these solutions to Navier–Stokes, to a
  constant-flux inertial range or to uniqueness.
---
<!-- inactive-ok-file: THEORY-763 — Proposed; Isett's non-admissible half, cited for contrast -->
# THEORY-tmpnvuqr: For every β < 1/3 and every smooth, strictly positive and strictly decreasing energy profile e(t) on [0, T], there is a weak solution of the 3D incompressible Euler equations on the periodic box, Hölder-continuous of exponent β in space and time, with ∫|v(t)|² = e(t) at every time; for such a solution the energy flux across a mollification scale ε, integrated over any time interval, tends as ε → 0 to ½ times the drop in e, which is strictly negative, so energy leaves the resolved field for vanishing scales on every interval; this is one-way for the energy of the whole box, not at every point, and it is chosen by the prescribed profile, not forced by the equations

## Source

Buckmaster, De Lellis, Székelyhidi and Vicol (2019), *Communications on Pure
and Applied Mathematics* 72(2):229–274, [LIT-tmpv4d6t](../literature.d/LIT-tmpv4d6t.md), read in full in
[NOTE-tmp18d5h](../notes.d/NOTE-tmp18d5h.md) from arXiv:1701.08678v1. The existence statement is its
Theorem 1.1. The energy balance used for the flux is Constantin, E and
Titi's ([LIT-1248](../literature.d/LIT-1248.md)), as re-derived for any weak solution in [THEORY-749](THEORY-749.md),
Steps 4–5. The construction is a modification of Isett's ([LIT-1255](../literature.d/LIT-1255.md),
[THEORY-763](THEORY-763.md)).

## What was actually shown

**The theorem (Theorem 1.1).** "Assume e : [0, T] → R is a strictly positive
smooth function. Then for any 0 < β < 1/3 there exists a weak solution
v ∈ C^β(T³ × [0, T]) to (1.1) such that ∫_{T³} |v(x, t)|² dx = e(t)." Here
(1.1) is ∂_t v + v·∇v + ∇p = 0, div v = 0 on the torus T³ = R³/Z³, and
C^β(T³ × [0, T]) is Hölder continuity in space and time jointly. Nothing
restricts the sign of e′. Taking e′ < 0 gives a solution whose kinetic
energy strictly decreases, which is what the paper calls dissipative and
the title calls admissible.

**How it is proved (read; estimates followed, not each re-derived).**

- *Inductive Proposition 2.1.* A sequence of Euler–Reynolds flows
  (v_q, p_q, R̊_q), ∂_t v_q + div(v_q⊗v_q) + ∇p_q = div R̊_q with R̊_q
  trace-free, at frequency λ_q = 2π⌈a^(b^q)⌉ and amplitude δ_q = λ_q^(−2β),
  satisfying ‖R̊_q‖₀ ≤ δ_{q+1}λ_q^(−3α), ‖v_q‖₁ ≤ Mδ_q^(1/2)λ_q,
  ‖v_q‖₀ ≤ 1 − δ_q^(1/2), and the energy gap
  δ_{q+1}λ_q^(−α) ≤ e(t) − ∫|v_q|² ≤ δ_{q+1} (2.7)–(2.10). The step to q + 1
  holds whenever 1 < b < (1 − β)/(2β) (2.11), with
  ‖v_{q+1} − v_q‖₀ + λ_{q+1}^(−1)‖v_{q+1} − v_q‖₁ ≤ Mδ_{q+1}^(1/2) (2.12),
  M a geometric constant. The iteration starts from (0, 0, 0).
- *Each step* is Isett's three stages: mollify at scale ℓ; glue exact Euler
  solutions started at times t_i = iτ_q with a partition of unity in time,
  so that the new stress lives on disjoint intervals I_i of length about τ_q;
  then add Mikado-flow perturbations transported by the glued flow. Two
  changes from Isett. The glued stress is built with the standard inverse
  divergence R of De Lellis and Székelyhidi, so it stays trace-free, which
  is "crucial to control the energy"; this needs a commutator estimate for
  the advective derivative of negative-order operators (Proposition D.1).
  And the perturbations are placed in disjoint "squiggling" space-time
  regions whose time projections cover all of [0, T] (Lemma 5.3), so energy
  ρ_q(t) = ⅓(e(t) − δ_{q+2}/2 − ∫|v̄_q|²) can be added even where the
  stress vanishes. That second change is what lets the energy follow any
  prescribed e.
- *Energy.* Proposition 6.2 gives |e(t) − ∫|v_{q+1}|² − δ_{q+2}/2| ≲
  δ_q^(1/2)δ_{q+1}^(1/2)λ_q^(1+2α)/λ_{q+1}. Since δ_q → 0, (2.10) forces
  ∫|v|² = e(t) in the limit, at every t.
- *Regularity.* (2.12) gives C⁰_tC^{β′}_x for every β′ < β by
  interpolation, and Section 2.2 recovers time regularity by a short
  mollification argument, so v ∈ C^{β″} jointly for every β″ < β < 1/3.

**Checked here.** The parameter condition (2.39),
−β − βb + 1 − b + 2b²β < 0, factors as (b − 1)(β(2b + 1) − 1) < 0, i.e.
b < (1 − β)/(2β), which is (2.11). A b > 1 exists if and only if β < 1/3.
This is the same bookkeeping as Isett's α = 1/(2b + 1) in [THEORY-763](THEORY-763.md), read
the other way. The factorization was confirmed numerically on random (b, β).
The derivation of (2.39) from (2.38), by taking logarithms base λ_q, was
redone by hand, as was the claim that (2.10) with δ_{q+1} → 0 gives the
exact profile.

**The consequence for the flux (the record's).** Mollify in space at scale
ε, as in [THEORY-749](THEORY-749.md). v is continuous on [0, T] × T³, so it lies in
C([0, T]; L²) ∩ L³, and Steps 4–5 there give, for s < t,

  ½∫|v^ε(t)|² − ½∫|v^ε(s)|² = ∫_s^t Π_ε(τ) dτ,
  Π_ε = ∫τ_ε : ∇v^ε,  τ_ε = (v⊗v)^ε − v^ε⊗v^ε,

with Π_ε the rate at which energy enters the resolved field v^ε from the
scales below ε. As ε → 0 the left side tends to ½(e(t) − e(s)). With e
strictly decreasing this is strictly negative for every s < t. So for every
time interval the integrated flux converges to a negative number: the
resolved field loses energy to vanishing scales over every interval, never
gains it back over any interval, and the loss rate in the limit is −½e′,
which the construction prescribes. Compare [THEORY-763](THEORY-763.md), where the same
integral takes both signs.

What could have come out otherwise: by [THEORY-749](THEORY-749.md) a solution regular enough
(Besov 3, ∞ above 1/3) has ∫_s^t Π_ε → 0 and e constant. These solutions
escape that only because β < 1/3.

## What this does not say

- **Not one-way at every point.** "Admissible" here is the global energy
  inequality: the total energy does not increase. The word appears only in
  the title and is never defined in the text; the introduction speaks of
  "strictly monotonic decreasing energy". The local energy inequality,
  ∂_t(½|v|²) + div((½|v|² + p)v) ≤ 0 in the sense of distributions,
  equivalently a non-negative Duchon–Robert dissipation measure, is not
  claimed or proved. So nothing excludes backscatter: energy may return
  from vanishing scales in some regions while more leaves in others. Later
  work is reported to reach the local inequality below 1/3 (Isett,
  arXiv:1710.11186, for continuous globally dissipative flows; Giri, Kwon
  and Novack, "The L³-based strong Onsager theorem", arXiv:2305.18509);
  the record has not read either.
- **Not that the direction is forced.** Theorem 1.1 accepts any smooth
  positive e. An increasing profile gives solutions that steadily draw
  energy out of vanishing scales, by the same proof. At this regularity the
  Euler equations do not pick the direction of transfer; the construction
  does. A one-way cascade is admissible here, not compelled.
- **Not a pointwise-in-time flux.** The limit is of time integrals over
  intervals. Whether Π_ε(τ) itself converges for each τ, or where in space
  and in scale the energy goes, is not shown. There is no constant-flux
  inertial range and nothing on locality of transfer between scales
  ([THEORY-754](THEORY-754.md)'s conditional account is not touched).
- **Not turbulence or Navier–Stokes.** The solutions are built by convex
  integration from the zero flow. Nothing shows they are vanishing-viscosity
  limits of Navier–Stokes, and Onsager's quoted "turbulent dissipation ...
  without the final assistance by viscosity" is motivation, not a result.
- **Not uniqueness, nor non-uniqueness for given data.** Theorem 1.1
  prescribes the energy, not the initial datum, and does not show two
  admissible solutions with the same initial datum. That came later
  (Daneri, Runa and Székelyhidi, arXiv:2004.00391, not read). The paper
  cites weak–strong uniqueness for dissipative solutions (Brenier, De
  Lellis and Székelyhidi). The record's inference from it: the initial datum
  of a strictly dissipative solution here cannot launch a classical
  solution, which would conserve energy, so these solutions start from
  rough data.
- **Not the endpoint or other settings.** β = 1/3 is not reached; the
  domain is T³ on a finite interval, e must be strictly positive (the
  energy gap (2.10) needs room at every step), so the solutions are never
  at rest, unlike Isett's.
- **Not a checked proof.** The estimates of Sections 3–6 were followed,
  not re-derived. The h-principle (Theorem 1.3) further rests on Theorem
  7.1, quoted from Daneri and Székelyhidi without proof; this entry does
  not use it.

## Connections

- **[QUESTION-219](../questions.d/QUESTION-219.md): answers in part.** It supplies what [THEORY-763](THEORY-763.md) could
  not: below 1/3 a coarse-grained energy flux can survive the limit of
  vanishing scale and run one way, into the small scales, on every time
  interval. This is the dissipative transfer A3's point needed, in the
  integrated, whole-box sense. Two qualifications the question should carry:
  the one-way property is global, not local; and it is selected by the
  prescribed energy, not produced by the dynamics. On the question proper,
  whether a pattern of transfer picks out a unit, it bears negatively if at
  all: the dissipation rate −½e′ is a free input of the construction, and
  the flux is carried by non-interacting waves on disjoint space-time
  regions, so nothing in it is a persisting organization of the kind A5's
  four conditions ask for.
- **[THEORY-763](THEORY-763.md).** Isett's solutions take both signs; these take one. With
  this entry the record holds both the bidirectional and the dissipative
  negative half, and the promote_when of [THEORY-763](THEORY-763.md) names this paper as an
  independent proof.
- **[THEORY-749](THEORY-749.md).** The positive half. Together with this entry: above 1/3 no
  flux survives for any weak solution; below it, a flux of either sign, or
  of one prescribed sign throughout, can.
- **[THEORY-754](THEORY-754.md).** Eyink and Aluie's conditional account assumes a non-zero
  mean flux through an inertial range. This entry shows weak solutions with
  a non-vanishing, one-signed mean flux exist at exponents below 1/3; it
  shows nothing about a range of scales across which that flux is constant.
