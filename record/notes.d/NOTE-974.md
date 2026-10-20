---
number: 974
status: Skimmed
formerly:
- NOTE-tmpi1i5f
paper: 'LIT-1255'
title: "Isett — A proof of Onsager's conjecture"
version: 2
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Skimmed from arXiv:1608.08301v2 (74 pages, the author's revision of 22
    July 2024; v1 is of 30 August 2016), text extracted with pdftotext.
    Read: the abstract; Part I, the introduction, with Conjectures 1 and 2
    and Theorem 1; Section 1, the organization; Section 2, notation, the
    Euler–Reynolds system, frequency–energy levels and the Main Lemma 2.1;
    Section 3, the three sublemmas and the proof of the Main Lemma from
    them; Section 4, the regularization, in full; Sections 5–8, the gluing
    construction, the anti-divergence and existence, including the proof of
    Proposition 8.1 and the statement of the Gluing Proposition 8.2; the
    start of Section 9; Sections 11–16, Mikado flows, the coarse flow and
    back-to-labels map, the ansatz, the error terms, the algebraic equation
    and the choice of mollification scales; and Section 18, the proof of
    Theorem 1 from the Main Lemma, in full. Not read: the rest of Section 9
    and Section 10, the gluing estimates (about 20 pages); Section 17, the
    convex-integration estimates (about 16 pages); and the appendix. So the
    proof's architecture and its exponent bookkeeping were read and the
    estimates that carry it were not. Section 18's limiting exponent was
    redone by hand. The Annals text was not compared. Some displayed
    formulas were garbled by extraction and were read from the surrounding
    text.
- version: 2
  date: '2026-10-20'
  note: >-
    The admissible version of Buckmaster, De Lellis, Székelyhidi and Vicol
    is now read (NOTE-1013, THEORY-776); the places that called it
    not held now cite it. The reading is unchanged.
date: '2026-10-20'
summary: >-
  The negative half of Onsager's conjecture. For every α < 1/3 there is a
  nonzero weak solution of the 3D incompressible Euler equations on the
  periodic box, in C^α in space and time, that vanishes outside a finite
  time interval and so does not conserve energy. It is built by iterating a
  Main Lemma that first glues exact local Euler solutions so that the error
  lives on separated short time intervals, then cancels each piece with a
  single transported Mikado-flow wave. For the record, it shows that a
  coarse-grained energy flux can survive the limit of vanishing scale for
  rough fields; it does not show a one-way dissipative cascade, since these
  solutions gain energy and then lose it.
---
<!-- inactive-ok-file: THEORY-763 — Proposed; the account this reading files, cited as its outcome -->
<!-- inactive-ok-file: THEORY-776 — Proposed; the admissible version, cited as the later reading -->
<!-- inactive-ok-file: CLAIM-157 THEORY-257 CLAIM-331 CLAIM-327 — Proposed; entries named as not bearing, open -->
# NOTE-974: Isett — A proof of Onsager's conjecture

## Contribution

It proves Conjecture 2, the negative direction of Onsager's conjecture:
for every α < 1/3 there are weak solutions of incompressible Euler on T³
in the Hölder class C^α that fail to conserve energy. The best previous
results were 1/5 for C_tC^α_x (Isett 2013) and 1/3 in the weaker class
L¹_tC^α_x (Buckmaster, De Lellis and Székelyhidi). With the positive half,
conservation above 1/3 (Eyink; Constantin, E and Titi, [LIT-1248](../literature.d/LIT-1248.md)), it
makes 1/3 the threshold for the class L^∞_tC^α_x. The new device is a
"gluing approximation". Before each convex-integration step, the
approximate solution is replaced by exact Euler solutions on short time
windows, glued together, so that the remaining error lives on separated
time intervals and the high-frequency corrections that cancel it never
interact.

## Key insight

The obstruction below 1/5 had been interference between the
high-frequency waves added at each stage: they had to be cut off sharply
in time, and the cutoffs cost regularity. If the error that the waves must
cancel can first be confined to well-separated short time intervals, one
wave per interval suffices and no two waves ever meet. The gluing step
does this by solving Euler exactly between the intervals. Its difficulty
is to make the glued error no larger than the original. That needs a
"good anti-divergence" of the velocity difference, which is built by
transporting along the flow and by using the structure of the linearized
Euler equation. Mikado flows, straight pipe flows in disjoint cylinders,
supply waves that are exact stationary solutions and stay coherent over
the needed time scale.

## Assumptions

- **Domain.** The periodic box T³ = (R/Z)³, for all times t ∈ R. The
  paper says the proof extends to d ≥ 3, and does not cover d = 2 or the
  whole space with finite energy.
- **Notion of solution.** Continuous v and p satisfying the Euler
  equations in the sense of distributions, equivalently the integral
  balances of momentum and mass (2)–(3) over every smooth subregion.
- **Regularity class.** C^α_{t,x}: |f(t + Δt, x + Δx) − f(t, x)| ≤
  C(|Δt| + |Δx|)^α uniformly. That is stronger than the L^∞_tC^α_x of the
  conjecture and much stronger than Constantin, E and Titi's
  L³_tB^α_{3,∞}.
- **What is not assumed or obtained.** No initial-value problem is posed:
  the solution is constructed, starting from the zero solution, and
  vanishes before some time. No energy inequality (admissibility) is
  claimed.

## Key results

- **Theorem 1.** For any α < 1/3 there is a nonzero weak solution
  v ∈ C^α_{t,x}(R × T³), p ∈ C^{2α}_{t,x}, with v ≡ 0 outside a finite
  time interval. It does not conserve energy.
- **Theorem 3 (Section 18).** For any 0 < δ < 1/4 there is such a
  solution for every α satisfying (18.1). The left side of (18.1) tends to
  −1/2 + 3α/2 as δ → 0, which gives Theorem 1. Redone here by hand from
  the parameter-evolution matrix (eigenvalues 1 + δ, δ/2, 1).
- **Main Lemma 2.1.** An Euler–Reynolds flow (v, p, R) with
  frequency–energy levels (Ξ, e_v, e_R) can be corrected to one with
  levels (CNΞ, log Ξ̂ e_R, (log Ξ̂)^{5/2} e_v^{1/2}e_R^{1/2}/N), with
  Ξ̂ = Ξ(e_v/e_R)^{1/2} and N ≥ max{Ξ^η, (e_v/e_R)^{1/2}}. The correction
  is bounded by C(log Ξ̂)^{1/2}e_R^{1/2} in C⁰ and by
  CNΞ(log Ξ̂)^{1/2}e_R^{1/2} in C¹. The time support grows by at most
  Ξ⁻¹e_v^{−1/2}.
- **The three sublemmas.** Regularization (Lemma 3.1, by mollification and
  the quadratic commutator estimate (4.1)). Gluing (Lemma 3.2: the new
  stress is Σ_I R_I with the R_I supported in disjoint intervals of length
  θ ≈ δ(log Ξ̂)⁻²Ξ⁻¹e_v^{−1/2}, with the same size bounds up to logarithms
  and a bound on their advective derivatives). Convex integration (Lemma
  3.3: one Mikado wave per R_I).
- **Proposition 8.1** (proof read). The tensor r_I = ρ_I + z_I built by the
  transport equations (7.8)–(7.10) is a symmetric anti-divergence of the
  velocity difference y_I. The proof uses that y_I and v are divergence
  free and uniqueness for transport.
- **Mikado flows (Section 11).** For F = {e_i ± e_j}, |F| = 6, the fields
  ψ_f(X)f with ψ_f supported in disjoint thin cylinders around periodic
  lines in direction f are divergence free and have disjoint supports, so
  any combination Σγ_fψ_ff is a stationary Euler solution with zero
  pressure. The six tensors f⊗f form a basis of symmetric matrices with
  Σ ¼ f⊗f = Id (15.6)–(15.7), which lets the algebraic equation (15.5)
  absorb any small stress.
- **Nontriviality (Section 18.5).** The base stage has ‖v₍₀₎‖ ≥ 0.9; the
  corrections sum to at most 0.01.

## Claims

Not filled: this reading is Skimmed, and only a Read note may fill in a
claims table. What the skim supports is in [THEORY-763](../theory.d/THEORY-763.md), filed Proposed.

## Method

1. Start from the zero flow and apply the Main Lemma of Isett's 2013 paper
   once, with a prescribed energy profile e(t), e(0) = 1, to get a nonzero
   Euler–Reynolds flow with compact time support.
2. Iterate the Main Lemma with frequencies Ξ_(k) and energy levels growing
   and shrinking double-exponentially, governed by the matrix of (18.20).
3. Within each Main Lemma step:
   - regularize;
   - glue. Solve Euler exactly from the data v(8θI), call the differences
     y_I, and join them with a partition of unity η_I in time. The new
     stress, (6.7), comes from η_I′ times an anti-divergence of
     y_I − y_{I+1}, plus quadratic overlap terms;
   - convex-integrate. On each interval add
     V_J = e_I^{1/2}γ_J(∇Γ_I⁻¹)f ψ_f(λΓ_I) plus a divergence correction,
     with Γ_I the back-to-labels map of the mollified coarse flow and λ a
     large frequency. Choose γ_J by the algebraic equation so that
     Σ v_J⊗v_J + P + R_ε = 0, so the low-frequency part of the new stress
     cancels.
4. Pass to the limit. The corrections are summable in C⁰ (so v is
   continuous and nonzero) and in C_tC^α_x for α in range (so v ∈ C^α).
   Time regularity follows from Isett's earlier theory. The supports
   converge, so the time support is compact.

## Concepts

- **Euler–Reynolds flow**: (v, p, R) with ∂_t v + ∇·(v⊗v) + ∇p = ∇·R. R
  is what the approximate solution fails by, the analogue of a Reynolds
  stress.
- **Frequency–energy levels (Ξ, e_v, e_R)**: bounds on the derivatives of v
  and R by powers of a frequency Ξ times e_v^{1/2} and e_R (Definition 2.2).
- **Ideal Case Scenario**: Isett's 2013 target scaling for one step,
  e_R′ ≈ e_v^{1/2}e_R^{1/2}/N, which yields exponents up to 1/3.
- **Gluing approximation**: replacing an approximate solution by exact
  local Euler solutions glued in time, so that the error is localized to
  short, separated intervals.
- **Mikado flow**: a stationary Euler solution made of straight pipe flows
  in disjoint periodic cylinders (Daneri and Székelyhidi).
- **Back-to-labels map Γ_I**: the inverse flow map of the coarse velocity
  from time t(I), used to transport the waves.

## Connections

It completes the line of De Lellis and Székelyhidi (2013, 2014), who
adapted Nash's convex integration to Euler with Beltrami waves and reached
1/10. Isett's 2013 work, with its "Ideal Case Scenario", reached 1/5, and
Buckmaster, De Lellis and Székelyhidi reached 1/3 in L¹_tC^α_x. Daneri and
Székelyhidi (2016) supplied the Mikado flows. On the positive side it cites
Eyink (1994), Constantin, E and Titi (1994, [LIT-1248](../literature.d/LIT-1248.md)) and Cheskidov,
Constantin, Friedlander and Shvydkoy (2008) for the endpoint space. The
earliest non-uniqueness and non-conservation examples, in L² rather than
Hölder classes, are Scheffer (1993) and Shnirelman (1997, 2000), and the
paper suggests its gluing is related to Shnirelman's construction. Later
work: Buckmaster, De Lellis, Székelyhidi and Vicol (2019) for admissible,
strictly dissipative solutions below 1/3, since read ([LIT-1300](../literature.d/LIT-1300.md),
[NOTE-1013](NOTE-1013.md)).

## Bearing on the record

- **[THEORY-763](../theory.d/THEORY-763.md)** is filed from this reading, Proposed. It states
  Theorem 1 and the record's consequence: by Constantin, E and Titi's
  energy balance (11), re-derived for any weak solution in [THEORY-749](../theory.d/THEORY-749.md),
  the time-integrated flux across a mollification scale ε tends to the
  change in energy as ε → 0. For Isett's solutions that change is nonzero.
  It is positive while the energy rises from zero and negative while it
  falls back.
- **[QUESTION-219](../questions.d/QUESTION-219.md) and A3's point.** [NOTE-982](NOTE-982.md) found that the record
  held only the positive half: above 1/3 the flux into vanishing scales
  must die. This paper supplies the other half: below 1/3 it can survive.
  Two qualifications that the question should carry:
  - *The surviving flux is not one-way.* These solutions are not
    admissible. Energy first comes out of the vanishing scales and later
    goes back in, so they show transfer across vanishing scales, not a
    dissipative cascade. A one-way transfer, for the whole box, is
    Buckmaster, De Lellis, Székelyhidi and Vicol (2019), since read
    ([THEORY-776](../theory.d/THEORY-776.md)).
  - *It is not about turbulence.* The solutions are constructed by convex
    integration, start from rest and are non-unique, and nothing ties them
    to vanishing-viscosity limits.
  So the question's sentence "That a flux can survive for rougher fields
  is the negative half of Onsager's conjecture (Isett 2018 and others),
  which the record does not hold" can now cite [THEORY-763](../theory.d/THEORY-763.md), with "in
  both directions" added. Nothing here bears on whether a pattern of
  transfer picks out a unit. If anything, the construction cuts against
  reading flux as organization. The flux in these solutions is produced
  by a superposition of waves with disjoint supports in time and space,
  one per short interval, and nothing persists across intervals except the
  coarse field the waves are transported by.
- **[THEORY-749](../theory.d/THEORY-749.md).** Its "What this does not say" names Isett as the
  negative half, unread. It can now cite [THEORY-763](../theory.d/THEORY-763.md) for it, with the
  admissibility caveat.
- **[THEORY-754](../theory.d/THEORY-754.md).** [NOTE-982](NOTE-982.md) found Eyink and Aluie's non-zero mean
  inertial-range flux consistent only with exponents up to 1/3. Isett
  shows weak solutions with a surviving flux exist there, but says nothing
  about a constant-flux range or about locality of transfer.
- **[QUESTION-222](../questions.d/QUESTION-222.md) and [QUESTION-218](../questions.d/QUESTION-218.md) (closure).** The Euler–Reynolds
  system is the closure problem in the form this field uses: v is a
  coarse field and R the unclosed stress. Convex integration runs the
  closure problem backwards: it chooses the fine-scale correction to make
  a prescribed stress vanish. It shows that a coarse field with a given
  Reynolds stress has many fine-scale completions, which is
  non-uniqueness in the opposite direction from closure. That is a
  contrast the record might use, and it is not filed.
- **The other key entries** ([THEORY-733](../theory.d/THEORY-733.md), [THEORY-257](../theory.d/THEORY-257.md), [THEORY-661](../theory.d/THEORY-661.md),
  [CLAIM-157](../claims.d/CLAIM-157.md), [CLAIM-331](../claims.d/CLAIM-331.md), [CLAIM-327](../claims.d/CLAIM-327.md), [CLAIM-388](../claims.d/CLAIM-388.md), [THEORY-755](../theory.d/THEORY-755.md))
  and [QUESTION-217](../questions.d/QUESTION-217.md), [QUESTION-220](../questions.d/QUESTION-220.md), [QUESTION-221](../questions.d/QUESTION-221.md): not
  addressed. The iteration's frequencies Ξ_(k) form a coarse-to-fine
  sequence of nested corrections, v = v₍₀₎ + Σ V₍k₎. But it is a
  construction device, not a claim about optimal or natural hierarchies.

No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- **Read in outline.** About 40 of the 74 pages, the estimates for the
  gluing and convex-integration steps, were not read, so no step of the
  Main Lemma was checked. The record relies on the paper for it.
- **Not admissible, not physical.** The abstract and Theorem 1 claim only
  non-conservation, and the paper is accurate about that. Readers, and A3's
  gloss, may take "anomalous dissipation" from the conjecture's motivation.
  These solutions gain energy as well as lose it.
- **The class.** The conjecture as stated is about L^∞_tC^α_x. The
  theorem gives the stronger C^α_{t,x}, which is fine for the negative
  direction. It does not reach the endpoint α = 1/3, where Eyink and
  Cheskidov et al. suggest non-conservation may still be possible.
- **Scope stated by the author.** d = 2, finite-energy solutions on R³,
  active scalars, Boussinesq and the steady equations are left open.
- **Copy.** The arXiv v2 is a 2024 revision; whether it differs from the
  2018 Annals text in substance was not checked.

## Open questions

- Are there weak solutions below 1/3 whose energy only decreases, and is
  the surviving flux then one-signed at every time? Buckmaster, De Lellis,
  Székelyhidi and Vicol (2019) answer the first part yes ([THEORY-776](../theory.d/THEORY-776.md),
  Proposed); the second, at every point in space, needs a local energy
  inequality they do not prove.
- Does any vanishing-viscosity limit of Navier–Stokes fall in this class
  with non-zero flux? Only a theorem about Navier–Stokes would settle it.
- What does the record's flux question (A5's four conditions) say of a
  flux that exists only during a construction's lifetime and is produced
  by non-interacting waves? Applying the test to these solutions would be
  a sharp negative example.
