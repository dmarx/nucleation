---
status: Proposed
promote_when: >-
  A reading recorded as Read that checks, step by step, the estimates this
  entry takes on trust: the component bounds and transport estimates of
  Section 4.6 (Propositions 4.3–4.8), the stress estimates of Sections 4.7–4.8,
  the unresolved flux density and current estimates of Sections 4.9–4.13
  (Propositions 4.9–4.15, including the cancellations (214)–(215) and the
  commutator estimate of Section 4.13), and their assembly in Section 4.14;
  or an independent complete proof of a Hölder-continuous weak Euler
  solution satisfying the local energy inequality whose dissipation measure
  is a known nonnegative function. Acceptance by the journal, citation counts
  or later work that assumes the theorem (De Lellis and Kwon's improvement to
  1/7 among them) do not count. The parameter algebra that fixes 1/15, the
  form of the dissipation measure (a function of time alone), and the
  consequence for the local flux are re-derived below and need nothing
  further once the Main Lemma is granted. A claim about the sign of the flux
  at a fixed positive scale, about exponents up to 1/3 in a Hölder class, or
  about where dissipation would sit in a vanishing-viscosity limit is not
  covered by this entry and would need a different theorem.
title: 'For every α < 1/15 there are weak solutions of the 3D incompressible Euler equations on the periodic box, Hölder-continuous of exponent α in space and time, that satisfy the local energy inequality; in the construction their dissipation measure is a nonnegative function of time alone, equal at each time to the rate at which the total energy falls, zero while the local energy equality holds and positive on all of space during a short final interval in which the solution''s energy is drained to zero; uncountably many such solutions share one initial datum and one dissipation measure; for them the local coarse-grained energy flux into vanishing scales converges to that measure, so the transfer is one-way at every place and time in the limit and spread uniformly over the box, with its timing chosen by the construction, not forced by the equations'
version: 1
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Filed Proposed from NOTE-tmpb08k2, a skim of the arXiv v4 text. The
    existence and nonuniqueness statements are the paper's Theorems 1, 4
    and 7. That the dissipation measure is a function of time alone, equal
    to minus the derivative of the total energy, is the record's reading of
    the construction: (44) and (117) of the Main Lemma's proof and the
    choice µ̃ = µ − (3/4)∂_t e_Z in Lemma 6.1 were followed, and the
    integral identity was re-derived. The exponent 1/15 was re-derived
    from the parameter recursion (291)–(292) with a short numpy check. The
    estimates of Sections 4.6–4.13 were not checked, so the entry is not
    Active under ADR-047 v2. The consequence for the local flux is the
    record's.
tags:
- mathematics
- natural-sciences
date: '2026-10-20'
source:
- LIT-tmp6vocc
- LIT-1248
- LIT-tmpfah3l
answers:
- QUESTION-219
summary: >-
  Isett (2017; ARMA 2022), [LIT-tmp6vocc](../literature.d/LIT-tmp6vocc.md), skimmed in [NOTE-tmpb08k2](../notes.d/NOTE-tmpb08k2.md): the first
  continuous, indeed C^α with α < 1/15, weak Euler solutions satisfying the
  local energy inequality with nonzero dissipation, and a Cantor family of
  them sharing one initial datum and one dissipation measure. In the
  construction the dissipation measure is a function of time alone, so in
  the limit of vanishing scale the energy flux runs one way at every place,
  as in [THEORY-tmp6pe5a](THEORY-tmp6pe5a.md), but in a Hölder class and spread uniformly over the
  torus rather than set in pipes. It is switched on only while the
  constructor drains the solution's energy to zero at the end of its life.
  Where, when and how fast the energy goes are inputs; the exponent is far
  from 1/3; nothing ties these solutions to Navier–Stokes.
---
<!-- inactive-ok-file: NOTE-tmpb08k2 — Skimmed; this entry's reading -->
<!-- inactive-ok-file: THEORY-tmp6pe5a THEORY-tmpnvuqr THEORY-763 — Proposed; the L³-local, whole-box and two-signed accounts, cited for contrast -->
# THEORY-tmpxpm2w: For every α < 1/15 there are weak solutions of the 3D incompressible Euler equations on the periodic box, Hölder-continuous of exponent α in space and time, that satisfy the local energy inequality; in the construction their dissipation measure is a nonnegative function of time alone, equal at each time to the rate at which the total energy falls, zero while the local energy equality holds and positive on all of space during a short final interval in which the solution's energy is drained to zero; uncountably many such solutions share one initial datum and one dissipation measure; for them the local coarse-grained energy flux into vanishing scales converges to that measure, so the transfer is one-way at every place and time in the limit and spread uniformly over the box, with its timing chosen by the construction, not forced by the equations

## Source

Isett, "Nonuniqueness and existence of continuous, globally dissipative
Euler flows", *Archive for Rational Mechanics and Analysis* 244:1223–1309
(2022), [LIT-tmp6vocc](../literature.d/LIT-tmp6vocc.md), skimmed in [NOTE-tmpb08k2](../notes.d/NOTE-tmpb08k2.md) from arXiv:1710.11186v4. The
existence statements are its Theorems 1 and 4, both consequences of the
Approximation Theorem 7. The form of the dissipation measure is read from
the proof of the Main Lemma 3.1 (lines (43)–(44) and (117)) and from Lemma
6.1. The coarse-grained energy balance is Constantin, E and Titi's
([LIT-1248](../literature.d/LIT-1248.md)), re-derived in [THEORY-749](THEORY-749.md), taken in its local form as in
[THEORY-tmp6pe5a](THEORY-tmp6pe5a.md) ([LIT-tmpfah3l](../literature.d/LIT-tmpfah3l.md)).

## What was actually shown

**The terms.** The paper calls a weak solution *globally dissipative* if
v ∈ L³_{t,x} and it satisfies the local energy inequality

  ∂_t(|v|²/2) + ∇_j((|v|²/2 + p)v^j) ≤ 0   (2)

in the sense of distributions; the left side is then minus a nonnegative
Radon measure µ, the *dissipation measure*. "Globally" does not mean "for
the whole box": it means the local inequality holds everywhere, and the
inequality need not be strict. The record's other entries use "global" for
the whole-box energy ([THEORY-tmpnvuqr](THEORY-tmpnvuqr.md)); the two usages are opposite.

**The theorems.**

- *Theorem 1.* "On (0, ∞) × T^d, for d ≥ 3, there exist Hölder-continuous
  weak solutions (v, p) that satisfy the local energy inequality (2) with
  strict inequality holding everywhere on an open interval of time."
- *Theorem 4.* "For any α ∈ [0, 1/15), there exists an infinite family of
  weak solutions (v_β, p_β) to (1) of class v_β ∈ C^α_{t,x}([0, ∞) × T³)
  that satisfy the local energy inequality (2) and share the same initial
  data while having uniformly bounded, compact support. Such a family may
  be chosen to have a common dissipation measure µ … independent of β while
  being homeomorphic to a Cantor set as a subspace of C^α_{t,x}, and also
  having positive Hausdorff dimension as a subspace of C_tL²_x."
- *Theorem 5.* The same with the local energy *equality* on R × T³:
  nonunique energy-conserving C^α solutions from one datum.
- *Theorem 6 (8).* For α < 1/15 the initial data admitting uncountably many
  C^α solutions with the local energy equality on a common interval are C⁰
  dense among continuous divergence-free fields.

The exponent 1/15 does not depend on the dimension d ≥ 3.

**How it is proved (read in outline; estimates not checked).** A
*dissipative Euler–Reynolds flow* (Definition 2.1) adds to the
Euler–Reynolds system a relaxed local energy inequality with an unresolved
flux density κ and current ϕ:

  ∂_t(|v|²/2) + ∇_j((|v|²/2 + p)v^j) = D_tκ + ∇_j(v_ℓR^{jℓ}) + ∇_jϕ^j − µ,  µ ≥ 0.

The Main Lemma corrects (v, p) by plane waves V_I = P_I[e^{iλξ_I}v_I]
whose phases are transported by the coarse flow, each oscillating
essentially along one coordinate axis and taking values in the
perpendicular plane, cycling the axis from stage to stage. Some waves cancel
the low-frequency stress; others cancel the low-frequency current ϕ through
"high-high-low" triads (two passive waves and one active wave with
n₁ + n₂ + n₃ = 0), which the paper likens to Kraichnan's Lagrangian direct
interaction approximation. Beltrami and Mikado waves are set aside: the
paper says Mikado implementations "introduce both creation and dissipation
of energy in the disjoint regions where the waves are supported and cut
off". Nonuniqueness comes from flipping the sign of one large wave at each
stage k ∈ β; this changes nothing in the estimates or in µ, and shifts the
solution by at least a fixed fraction of the stage's amplitude in C_tL²_x.

**Checked here.**

- *The exponent.* The row vector (0, 15, 11, 5, 1, 2) lies in the left null
  space of T − 1 for the recursion matrix T of (291), and its product with
  e₃ + e₆ is 13, giving (292). The reduced matrix T̊ of (294) has
  eigenvalues 1, 1/3, 0, 0 with fixed direction ζ = (1, 3/2, 1, 1), and ζ
  satisfies both admissibility inequalities (293) strictly (1 > 0, 6 > 0).
  Iterating the recursion numerically from L̊ = L_Z ζ, the frequency grows by
  about Z^{7.5} per stage while the error level e_G falls by Z, and the
  Hölder threshold of (306) tends to 1/15 as L_Ĉ/L_Z → 0 (0.0655 at
  L_Z/L_Ĉ = 50, 0.0666 at 500). So the C^α amplitude scales like
  frequency^{−1/15}.
- *The dissipation measure.* In the Main Lemma the energy increment is
  e^{1/2}(t) = 2(K₀e_ϕ)^{1/2} η_τ ∗ 1_{t ≤ sup Ĩ[G] + τ/100}(t), τ = (Ξe_v^{1/2})^{−1}
  (117): a function of t alone, constant up to just past the stage's
  interval and zero shortly after. The new measure is µ* = µ − D_t e(t)
  (after (44)), and D_t e = ∂_t e because e does not depend on x. Lemma 6.1
  starts the iteration with µ̃ = µ − (3/4)∂_t e_Z(t), tr δ[1∗] = 3/2. So from
  the zero flow (Theorems 1 and 4) every stage adds a nonnegative function
  of t alone, and the limit is µ∞(t, x) = m(t) = −(3/4)e_Z′(t) − Σ_k e_(k)′(t).
  Integrating (2) over T³ (volume 1) gives (d/dt)∫|v|²/2 = −m(t): the
  dissipation density at every point equals the rate at which the total
  energy falls. Each stage's drop is a bump of mass 4K₀e_{ϕ,(k)} and width
  about τ_k/200, so m is integrable in t but not bounded: its bumps grow
  taller as they accumulate at the end of the support.
- *Where in time.* Theorem 7(3) gives µ∞ = 0 on Ĩ(1) × T³, which is
  (−∞, 2) for Theorem 4; property 4 puts the support of every v_β in
  t ≤ 2 + (Ξ₀E₀^{1/2})^{−1}. So each solution conserves energy locally until
  t = 2, loses all of it on the whole torus within a time of order
  (Ξ₀E₀^{1/2})^{−1}, and is identically zero afterwards. The solutions of a
  family coincide for t < 1 and branch near t ≈ 1, while the local energy
  equality still holds.

**The consequence for the local flux (the record's).** v is bounded and
uniformly continuous, and p ∈ L^q_{t,x} for every q < ∞ (Section 6.2).
Mollifying in space at scale ℓ, as in [THEORY-tmp6pe5a](THEORY-tmp6pe5a.md),

  ∂_t(½|v^ℓ|²) + div((½|v^ℓ|² + p^ℓ)v^ℓ + τ_ℓv^ℓ) = τ_ℓ : ∇v^ℓ,  τ_ℓ = (v⊗v)^ℓ − v^ℓ⊗v^ℓ.

Here τ_ℓ → 0 uniformly (|τ_ℓ| ≲ ℓ^{2α}), |v^ℓ|² and |v^ℓ|²v^ℓ converge
uniformly, and p^ℓv^ℓ → pv in L¹_loc. So the left side tends in
distributions to the left side of (2), and

  −τ_ℓ : ∇v^ℓ → m(t) ≥ 0 in D′.

For every nonnegative test function ψ(t, x), the energy passed to scales
below ℓ in the region ψ weights tends to ∫ψ(t, x)m(t) dt dx. It is
positive whenever ψ's time support meets the drain interval, wherever in
space ψ sits, and zero otherwise. The pointwise bound |τ_ℓ : ∇v^ℓ| ≲ ℓ^{3α−1}
grows as ℓ → 0 for α < 1/3, so only the distributional limit is
controlled.

What could have come out otherwise: above 1/3 the measure must vanish
(Duchon and Robert; [THEORY-749](THEORY-749.md) for the total). Isett's 2018 solutions
([THEORY-763](THEORY-763.md)) and Buckmaster, De Lellis, Székelyhidi and Vicol's
([THEORY-tmpnvuqr](THEORY-tmpnvuqr.md)) satisfy no proved local sign. A scheme whose waves create
energy locally where they are cut off, which the paper says of Mikado
schemes, would not give (2).

## What this does not say

- **Not near 1/3.** α < 1/15 in C^α_{t,x}. De Lellis and Kwon improved the
  Hölder exponent to 1/7, drawing on this paper's ideas (Analysis & PDE
  15:2003–2059, 2022, not read); Giri, Kwon and Novack reach 1/3 only in
  L³-based Besov spaces ([THEORY-tmp6pe5a](THEORY-tmp6pe5a.md)). The strong Onsager conjecture in
  L^∞_tC^{1/3}_x, the paper's Conjecture 1, stays open.
- **Not dissipation the dynamics selects.** The functions e_(k)(t) are
  fixed by the frequency–energy levels and the intervals; the constructor
  chooses when the drain happens. The sign is not free, since µ ≥ 0 is what
  the scheme is built to keep, but the place, the time and the rate are
  inputs, as in [THEORY-tmp6pe5a](THEORY-tmp6pe5a.md) and [THEORY-tmpnvuqr](THEORY-tmpnvuqr.md).
- **Not a spatially structured dissipation.** In this construction the
  measure has no spatial structure at all: it is uniform on T³ at each time.
  That is the record's reading of the proof, not a statement of the paper.
  It is the opposite of the concentrated, intermittent dissipation that
  turbulence phenomenology expects, and of Giri, Kwon and Novack's pipes.
- **Not sustained dissipation.** The energy is lost only while the solution
  is being shut off: before the drain interval the local energy equality
  holds, and after it the solution is zero. There is no stationary or
  persistent cascade.
- **Not one-signed at a positive scale.** As in [THEORY-tmp6pe5a](THEORY-tmp6pe5a.md), the sign
  holds only for the limit ℓ → 0 tested against fixed functions.
- **Not non-uniqueness for given smooth data, nor turbulence.** The common
  initial datum of Theorem 4 is produced by the construction. By
  weak–strong uniqueness, which the paper cites, solutions satisfying the
  energy inequality cannot branch from data that launch a classical
  solution; Theorem 8's wild data are only C⁰-close to smooth data. The
  paper notes that L³ limits of suitable Navier–Stokes solutions satisfy
  (2); it does not show these are such limits. The Kraichnan analogy is an
  analogy.
- **Not a probabilistic result.** The "coin toss" is a deterministic binary
  choice at each stage indexed by β ∈ 2^ℕ; no law on solutions is used
  except Haar measure on 2^ℕ in the Hausdorff-dimension count.
- **Not a checked proof.** The estimates of Sections 4.6–4.13 were not
  checked.

## Connections

- **[QUESTION-219](../questions.d/QUESTION-219.md): answers in part.** It gives the one-way local transfer
  that [THEORY-tmpnvuqr](THEORY-tmpnvuqr.md) lacked in a Hölder class, as [THEORY-tmp6pe5a](THEORY-tmp6pe5a.md) does in
  an L³ one, and so makes the class no longer the obstruction. For the
  question proper it bears negatively, more sharply than the pipes did: the
  flux has no spatial pattern to pick out a unit, its timing is the
  constructor's, and it exists only while the solution is being drained.
  None of A5's four conditions can be met by a transfer with no spatial
  structure and no persistence.
- **[THEORY-tmp6pe5a](THEORY-tmp6pe5a.md).** Both prescribe the dissipation. Giri, Kwon and Novack
  set a smooth density in pipes, positive for all time, with β < 1/3 in L³
  Besov spaces; here it is uniform in space, confined to a final interval,
  with α < 1/15 in Hölder spaces. Neither contains the other.
- **[THEORY-tmpnvuqr](THEORY-tmpnvuqr.md).** Its qualification "not one-way at every point" holds
  for its solutions. This paper is the earlier Hölder construction that
  removes it at a lower exponent, and its author says that the Mikado
  cutoffs of that scheme create energy locally.
- **[THEORY-763](THEORY-763.md).** Isett's two-signed flux; here, one sign everywhere in the
  limit, at a fifth of the exponent.
- **[THEORY-749](THEORY-749.md).** The positive half; the measure here is what its local form
  forbids above 1/3.
- **[QUESTION-218](../questions.d/QUESTION-218.md) and [QUESTION-222](../questions.d/QUESTION-222.md) (closure).** Definition 2.1's remark: any
  ensemble average of globally dissipative flows is a dissipative
  Euler–Reynolds flow, with κ half the trace of the Reynolds stress and ϕ
  from the third-order cumulants. The coarse field's local energy balance
  thus carries two unclosed terms besides the stress. Convex integration
  again runs closure backwards. Not filed.
