---
number: 763
status: Proposed
formerly:
- THEORY-tmpy2pkj
promote_when: >-
  A reading recorded as Read that checks, step by step, the estimates this
  entry takes on trust: the Main Lemma's bounds (2.7)–(2.10), through the
  gluing estimates of Sections 9–10 and the convex-integration estimates of
  Section 17, either in this paper or in an independent complete proof of
  the same statement. Buckmaster, De Lellis, Székelyhidi and Vicol
  (THEORY-776) prove Hölder non-conservation below 1/3 but need a
  strictly positive energy, so they do not give compact time support and
  cannot stand in for it. The journal's acceptance, citation
  counts or later work that assumes the theorem do not count. The
  consequence for the flux is re-derived below and needs nothing further
  once the theorem is granted.
title: 'For every α < 1/3 there is a nonzero weak solution of the 3D incompressible Euler equations on the periodic box, with velocity Hölder-continuous of exponent α in space and time, that vanishes outside a finite time interval; its energy is not conserved, so the energy flux across a mollification scale ε does not vanish as ε → 0, and it runs in both directions, out of the vanishing scales while the energy rises and into them while it falls'
version: 2
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Filed Proposed from NOTE-974, a skim of Isett's paper. The
    existence theorem is the paper's Theorem 1; its proof was read in
    outline, with the step from the Main Lemma to the theorem (Section 18)
    read in full and its limiting exponent checked by hand, and the long
    estimates were not checked. So the entry is not Active under ADR-047
    v2. The consequence for the coarse-grained flux, and its two signs, are
    the record's, derived below from the energy balance re-derived in
    THEORY-749.
- version: 2
  date: '2026-10-20'
  note: >-
    The admissible version is now read (THEORY-776, Proposed). "What
    this does not say" cites it, and promote_when no longer names it as an
    independent proof, since it needs a strictly positive energy and so
    cannot give compact support in time. The account is unchanged.
tags:
- mathematics
- natural-sciences
date: '2026-10-20'
source:
- LIT-1255
- LIT-1248
summary: >-
  Isett (2018), [LIT-1255](../literature.d/LIT-1255.md), skimmed in [NOTE-974](../notes.d/NOTE-974.md): the negative half of
  Onsager's conjecture. With [THEORY-749](THEORY-749.md) (Constantin, E and Titi, the
  positive half) it makes 1/3 the threshold. For the record, its point is
  that below 1/3 the energy flux into vanishing scales can survive the
  limit, which is the half of A3's point that THEORY-749 could not
  give. It does not say that this flux is a dissipative cascade. Isett's
  solutions start from rest, gain energy and lose it again, so the
  surviving flux takes both signs. Nor does it say that such solutions are
  limits of Navier–Stokes or describe turbulence.
bears_on:
- QUESTION-219
---
<!-- inactive-ok-file: THEORY-776 — Proposed; the admissible version, cited for contrast, nothing here rests on it -->
<!-- inactive-ok-file: NOTE-974 — Skimmed; the partial reading this account rests on -->
# THEORY-763: For every α < 1/3 there is a nonzero weak solution of the 3D incompressible Euler equations on the periodic box, with velocity Hölder-continuous of exponent α in space and time, that vanishes outside a finite time interval; its energy is not conserved, so the energy flux across a mollification scale ε does not vanish as ε → 0, and it runs in both directions, out of the vanishing scales while the energy rises and into them while it falls

## Source

Isett (2018), *Annals of Mathematics* 188(3):871–963, [LIT-1255](../literature.d/LIT-1255.md),
skimmed in [NOTE-974](../notes.d/NOTE-974.md) from arXiv:1608.08301v2. The existence statement is
its Theorem 1. The energy balance used for the flux is Constantin, E and
Titi's (11) ([LIT-1248](../literature.d/LIT-1248.md)), as re-derived for any weak solution in
[THEORY-749](THEORY-749.md), Steps 4–5.

## What was actually shown

**The theorem (Isett, Theorem 1).** For any α < 1/3 there is a nonzero
weak solution (v, p) of ∂_t v + ∇·(v⊗v) + ∇p = 0, ∇·v = 0 on
R × (R/Z)³, with v ∈ C^α_{t,x} and p ∈ C^{2α}_{t,x}, such that v ≡ 0
outside a finite time interval. Here C^α_{t,x} means
|f(t + Δt, x + Δx) − f(t, x)| ≤ C(|Δt| + |Δx|)^α uniformly. Since v is
continuous, nonzero somewhere and zero at early and late times,
E(t) = ½∫|v(t)|² is not constant.

**How it is proved (outline, not checked line by line).**

- An *Euler–Reynolds flow* (v, p, R) solves ∂_t v + ∇·(v⊗v) + ∇p = ∇·R
  with a symmetric stress R. Its *frequency–energy levels* (Ξ, e_v, e_R)
  bound ‖∇^k v‖ ≤ Ξ^k e_v^{1/2} and ‖∇^k R‖ ≤ Ξ^k e_R.
- **The Main Lemma (Lemma 2.1)** turns such a flow into one with levels
  (CNΞ, log Ξ̂·e_R, (log Ξ̂)^{5/2} e_v^{1/2}e_R^{1/2}/N), where
  Ξ̂ = Ξ(e_v/e_R)^{1/2}, for any N ≥ max{Ξ^η, (e_v/e_R)^{1/2}}. The
  correction has ‖V‖ ≲ (log Ξ̂)^{1/2}e_R^{1/2}, and the time support
  grows by at most Ξ⁻¹e_v^{−1/2}. Up to logarithms this is the "Ideal Case
  Scenario" of Isett's 2013 work: the new stress is e_v^{1/2}e_R^{1/2}/N.
- The Main Lemma is three sublemmas: a regularization (Lemma 3.1); a
  **gluing approximation** (Lemma 3.2), which replaces v by exact Euler
  solutions started at times 8θI and glued with a partition of unity in
  time, so that the new stress is a sum of pieces R_I supported in
  separated intervals of length about θ; and a **convex integration**
  step (Lemma 3.3), which cancels each R_I with one Mikado-flow wave,
  stationary pipe flows in six lattice directions, transported by the
  coarse flow. Waves from different I never overlap in time, and Mikado
  pipes of different directions never overlap in space, so the cross
  terms that limited earlier schemes to 1/5 vanish.
- **The iteration (Section 18, read in full).** The base case comes from
  Isett's earlier Main Lemma, which forces the energy profile close to a
  prescribed e(t) with e(0) = 1. That gives ‖v₍₀₎‖ ≥ 0.9, while all later
  corrections sum to at most 0.01, so the limit is nonzero. The parameters
  evolve by a lower-triangular matrix with eigenvalues 1 + δ, δ/2 and 1,
  so they grow double-exponentially. The C^α norms of the corrections
  decay double-exponentially when [1/2 − δα, 1/2, α]·ψ₊ < 0, ψ₊ being the
  (1 + δ)-eigenvector. That condition tends to −1/2 + 3α/2 < 0, i.e.
  α < 1/3, as δ → 0. The sum of the time-support increments converges, so
  the support stays compact.

**Checked by hand here.** The 1/3 can be read off the Main Lemma's
scaling, ignoring logarithms. Let stage k have frequency λ_k and velocity
energy e_v = δ_k = λ_k^{−2α}, let its stress be the energy of the next
correction, e_R = δ_{k+1}, and take N = λ_{k+1}/λ_k with
λ_{k+1} = λ_k^b. The new stress is then
δ_{k+2} = δ_k^{1/2}δ_{k+1}^{1/2}λ_k/λ_{k+1}. Comparing exponents of λ_k
gives −2αb² = −α − αb + 1 − b, so α(2b² − b − 1) = b − 1 and
α = 1/(2b + 1). As b ↓ 1, α ↑ 1/3. Frequencies that grow only slightly
faster than geometrically therefore reach any α < 1/3, and no b > 1
reaches 1/3. The eigenvector computation of Section 18 was redone by hand
and gives the same limit.

**The consequence for the flux (the record's).** Mollify in space at scale
ε, as in [THEORY-749](THEORY-749.md). For any weak solution in
C([0, T]; L²) ∩ L³, which a continuous v on the torus is, Steps 4–5 there
give, for s < t,

  ½∫|v^ε(t)|² − ½∫|v^ε(s)|² = ∫_s^t Π_ε(τ) dτ,
  Π_ε = ∫τ_ε : ∇v^ε,  τ_ε = (v⊗v)^ε − v^ε⊗v^ε.

Π_ε is the rate at which energy enters the resolved field v^ε from the
scales below ε. Since v(t) ∈ L², the left side tends to E(t) − E(s) as
ε → 0, for each s and t. Take s before the support, where E(s) = 0, and t
with E(t) > 0. Then ∫_s^t Π_ε → E(t) > 0. Take instead s with E(s) > 0 and
t after the support. Then ∫_s^t Π_ε → −E(s) < 0. So the time-integrated
flux across ε survives the limit ε → 0, and its sign differs between the
two intervals. First the resolved field gains energy from vanishing scales,
then it loses energy to them. Nothing more local is claimed. Whether Π_ε(τ)
converges pointwise in time, and where in space the transfer happens, would
need Duchon and Robert's local balance, which the record does not hold.

What could have come out otherwise: by [THEORY-749](THEORY-749.md), any weak solution
regular enough (Besov 3, ∞ above 1/3) has ∫_s^t Π_ε → 0. Isett's solutions
escape this only because C^α with α < 1/3 lies below the threshold. That
is consistent, and it shows that the threshold is sharp in the exponent.

## What this does not say

- **Not that the surviving flux is a dissipative cascade.** Isett's
  solutions are not admissible: their energy rises from zero before it
  falls. Weak solutions with energy that only decreases, at every α < 1/3,
  are a later theorem (Buckmaster, De Lellis, Székelyhidi and Vicol, 2019),
  filed as [THEORY-776](THEORY-776.md) (Proposed). With it, the record can say that
  energy can cross vanishing scales one way for the whole box; this entry
  alone says only that it can cross in either direction.
- **Not that all rough solutions transfer energy.** The rough shear flows
  of [THEORY-749](THEORY-749.md) conserve energy and have Π_ε = 0 at every ε. The
  theorem is an existence result. Roughness permits a surviving flux; it
  does not force one.
- **Not anything about turbulence or Navier–Stokes.** The solutions are
  built by convex integration, starting from rest, not as limits of
  viscous flows. They also show non-uniqueness: v and 0 share the same
  initial data. Whether inviscid limits of Navier–Stokes belong to this
  class is open.
- **Not the endpoint, the plane or the whole space.** α = 1/3 is not
  covered. The paper says the proof extends to dimensions d ≥ 3 but not to
  d = 2, for lack of a substitute for Mikado flows, and does not give
  finite-energy solutions on R³.
- **Not a checked proof.** The 90-page estimates were not read. The entry
  rests on the paper's having proved what it states. The statement is the
  one the field takes as settled, but the record's check is of the
  architecture and the exponent bookkeeping only.

## Connections

- **[QUESTION-219](../questions.d/QUESTION-219.md): answers in part.** It supplies the half of A3's
  point that [THEORY-749](THEORY-749.md) could not: below Onsager's exponent a
  coarse-grained flux can survive the limit of vanishing scale. The
  question's sentence that this "is the negative half ..., which the record
  does not hold" can now cite this entry, with the qualification that the
  surviving flux here takes both signs. It does not bear on whether a
  pattern of transfer picks out a unit. A5's warning that persistent flux
  alone is not an individual is untouched. Here the flux is not even
  persistent; it exists only while the solution does.
- **[THEORY-749](THEORY-749.md).** Its "What this does not say" names this result as
  the negative half. Together the two make 1/3 sharp for the Hölder class:
  above it, for every solution, the integrated flux vanishes; below it, for
  some solutions, it does not.
- **[THEORY-754](THEORY-754.md).** Eyink and Aluie's conditional account assumes a
  non-zero mean flux through an inertial range, which [NOTE-982](../notes.d/NOTE-982.md) found
  consistent only with exponents at most 1/3. This entry shows that weak
  solutions with a non-vanishing flux exist in that range. It does not
  show that they have a constant-flux inertial range, or the scaling that
  account assumes.
