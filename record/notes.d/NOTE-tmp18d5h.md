---
status: Read
paper: 'LIT-tmpv4d6t'
title: "Buckmaster, De Lellis, Székelyhidi and Vicol — Onsager's conjecture for admissible weak solutions"
version: 2
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Read in full from arXiv:1701.08678v1 (36 pages, 30 January 2017, the
    only arXiv version), text extracted with pdftotext. Every section was
    read: the introduction with Theorems 1.1 and 1.3; Section 2, the
    inductive Proposition 2.1, the proof of Theorem 1.1 from it including
    the time-regularity argument, and the outline of the three stages;
    Sections 3–4, the stability estimates for exact solutions and the
    gluing; Section 5, Mikado flows, the squiggling cut-offs, the
    perturbation and its estimates; Section 6, the new stress and the
    energy iterate; Section 7, the h-principle; and Appendices A–D. The
    reduction of Theorem 1.1 to Proposition 2.1, the parameter inequality
    (2.38)–(2.39) and the energy bookkeeping were checked by hand (the
    factorization of (2.39) also numerically); the estimates of Sections
    3–6 were followed line by line but not each re-derived. Theorem 7.1,
    on which Theorem 1.3 rests, is quoted from Daneri and Székelyhidi
    without proof and was not checked. Figure 1 (the squiggling supports)
    was not seen. Many displayed formulas were garbled by extraction and
    were read from their surrounding text. The CPAM text was not compared.
- version: 2
  date: '2026-10-20'
  note: >-
    Giri, Kwon and Novack is now skimmed (NOTE-tmpms8u2); Connections and
    the first open question cite it. The reading is unchanged.
date: '2026-10-20'
summary: >-
  The admissible version of the negative half of Onsager's conjecture. For
  every β < 1/3 and every smooth strictly positive e(t) on [0, T] there is a
  C^β weak solution of 3D Euler on the torus with ∫|v|² = e(t) exactly, so
  with e decreasing the energy only falls and the coarse-grained flux runs
  into vanishing scales on every time interval ([THEORY-tmpnvuqr](../theory.d/THEORY-tmpnvuqr.md)). That is
  the one-way transfer Isett's solutions lacked, but one-way only for the
  box as a whole (no local energy inequality), and chosen by the prescribed
  profile, since an increasing e works just as well.
---
<!-- inactive-ok-file: NOTE-tmpms8u2 THEORY-tmp6pe5a — Skimmed or Proposed; the local version, cited as the later reading -->
<!-- inactive-ok-file: THEORY-tmpnvuqr THEORY-763 — Proposed; the account this reading files, and Isett's, cited as outcomes -->
<!-- inactive-ok-file: NOTE-974 — Skimmed; the Isett reading that named this work -->
<!-- inactive-ok-file: CLAIM-157 THEORY-257 CLAIM-331 CLAIM-327 — Proposed; entries named as not bearing, open -->
# NOTE-tmp18d5h: Buckmaster, De Lellis, Székelyhidi and Vicol — Onsager's conjecture for admissible weak solutions

## Contribution

Isett ([LIT-1255](../literature.d/LIT-1255.md), [NOTE-974](NOTE-974.md)) reached the Onsager exponent 1/3, but his
solutions are only shown to be non-conservative, and, the authors say,
their energy "fails to be monotonic on any interval of time". This paper
modifies Isett's scheme so that the energy can be prescribed exactly: any
smooth, strictly positive e(t) is the kinetic energy of some C^β weak
solution, for every β < 1/3. A strictly decreasing e gives solutions whose
energy strictly decreases, which the title calls admissible and the text
calls dissipative. An h-principle adds that these solutions are weak-*
dense among smooth strict subsolutions. The proof is also, the authors note,
"considerably shorter" than Isett's.

## Key insight

The energy of a convex-integration solution is decided step by step by how
much energy each perturbation adds. In Isett's scheme the perturbations sit
only where the glued Reynolds stress lives, on separated time intervals, so
there is nothing to add in the gaps. Here the perturbations are placed in
disjoint space-time regions with wavy ("squiggling") boundaries whose
projections on the time axis cover every time, so energy
ρ_q(t) = ⅓(e(t) − δ_{q+2}/2 − ∫|v̄_q|²) can be pumped in everywhere, and the
energy gap is closed to a prescribed target at each step. For that
bookkeeping to work the glued stress must stay trace-free, which is why the
gluing stress is rebuilt with De Lellis and Székelyhidi's inverse
divergence and a new commutator estimate.

## Assumptions

- **Domain.** The periodic box T³ = R³/Z³ and a finite time interval
  [0, T]. No initial-value problem is posed: v(0) is an output.
- **Notion of solution.** Distributional solutions of
  ∂_t v + v·∇v + ∇p = 0, div v = 0, with v Hölder-continuous.
- **Regularity class.** C^β(T³ × [0, T]), Hölder jointly in space and
  time; the inductive estimates use spatial Hölder norms only (Appendix A),
  and time regularity is recovered at the end.
- **The energy profile.** e : [0, T] → R smooth and strictly positive.
  Positivity is needed: the inductive gap (2.10) requires
  e(t) − ∫|v_q|² ≥ δ_{q+1}λ_q^(−α) > 0 at every step, so the solution can
  never be at rest. By scaling, sup|e′| ≤ 1 (2.1) and (2.13) are assumed
  without loss of generality.
- **"Admissible".** The word occurs only in the title. What is obtained is
  a prescribed, hence possibly strictly decreasing, total energy. The local
  energy inequality is not claimed.

## Key results

- **Theorem 1.1.** For any strictly positive smooth e and any 0 < β < 1/3
  there is a weak solution v ∈ C^β(T³ × [0, T]) with
  ∫_{T³}|v(x, t)|² dx = e(t) for all t.
- **Theorem 1.3 (h-principle).** If (v̄, p̄, R̄) is a smooth strict
  subsolution, ∂_t v̄ + div(v̄⊗v̄) + ∇p̄ = −div R̄ with R̄ positive
  definite, then for β < 1/3 there are C^β weak solutions v_k with
  v_k ⇀* v̄, v_k⊗v_k ⇀* v̄⊗v̄ + R̄ in L^∞ uniformly in time, and
  ∫|v_k|² = ∫(|v̄|² + tr R̄) for all t.
- **Proposition 2.1 (the iteration).** With λ_q = 2π⌈a^(b^q)⌉,
  δ_q = λ_q^(−2β), and 1 < b < (1 − β)/(2β) (2.11), the inductive bounds
  ‖R̊_q‖₀ ≤ δ_{q+1}λ_q^(−3α), ‖v_q‖₁ ≤ Mδ_q^(1/2)λ_q,
  ‖v_q‖₀ ≤ 1 − δ_q^(1/2), δ_{q+1}λ_q^(−α) ≤ e(t) − ∫|v_q|² ≤ δ_{q+1}
  propagate from q to q + 1, with
  ‖v_{q+1} − v_q‖₀ + λ_{q+1}^(−1)‖v_{q+1} − v_q‖₁ ≤ Mδ_{q+1}^(1/2), M
  geometric (Definition 5.6). *Holds when:* α below a threshold depending
  on β and b, and a large.
- **The parameter inequality (2.38)–(2.39).** It reduces to
  −β − βb + 1 − b + 2b²β < 0, which factors as
  (b − 1)(β(2b + 1) − 1) < 0 (checked here), i.e. (2.11). A b > 1 exists
  iff β < 1/3.
- **Scales.** Mollification at
  ℓ = δ_{q+1}^(1/2)/(δ_q^(1/2)λ_q^(1+3α/2)) (2.19); gluing time
  τ_q = ℓ^(2α)/(δ_q^(1/2)λ_q) (2.26), with the CFL-like condition
  τ_q‖v_ℓ‖_{1+α} ≲ ℓ^α ≪ 1 (2.27).
- **Gluing (Section 4, Propositions 4.2–4.4).** v̄_q = Σχ_i v_i with v_i the
  exact Euler solutions from v_ℓ(t_i); on I_i the stress is
  ∂_tχ_i R(v_i − v_{i+1}) − χ_i(1 − χ_i)(v_i − v_{i+1})⊗̊(v_i − v_{i+1}),
  trace-free, bounded by δ_{q+1}ℓ^(−N+α) in C^{N+α}, with energy within
  δ_{q+1}ℓ^α of v_ℓ's.
- **New stress (Proposition 6.1).** ‖R̊_{q+1}‖₀ ≲
  δ_{q+1}^(1/2)δ_q^(1/2)λ_q/λ_{q+1}^(1−4α), from the Nash, transport and
  oscillation errors (5.21).
- **Energy (Proposition 6.2).** |e(t) − ∫|v_{q+1}|² − δ_{q+2}/2| ≲
  δ_q^(1/2)δ_{q+1}^(1/2)λ_q^(1+2α)/λ_{q+1}.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | For every β < 1/3 and smooth e > 0 on [0, T] there is a C^β weak Euler solution on T³ with ∫\|v\|² = e(t) | strong | Theorem 1.1, via Proposition 2.1 and Sections 3–6 (estimates followed, not each re-derived here) |
| C2 | Hence there are C^β solutions, β < 1/3, with strictly decreasing energy | strong | C1 with e′ < 0 |
| C3 | Smooth strict subsolutions are weak-* limits of such solutions (h-principle) | moderate | Theorem 1.3, resting on Theorem 7.1 quoted from Daneri and Székelyhidi without proof |
| C4 | The dissipative solutions are "in a sense typical" among subsolutions | weak | abstract's gloss of C3; density is shown, not genericity, and the h-principle solutions have energy ∫(\|v̄\|² + tr R̄), which need not decrease |
| C5 | Isett's solutions' energy fails to be monotonic on any time interval | weak | asserted in the introduction without proof or reference; Isett's own Theorem 1 claims only non-conservation ([NOTE-974](NOTE-974.md)) |
| C6 | Dissipative solutions satisfy weak–strong uniqueness | moderate | cited (Lions; Brenier, De Lellis and Székelyhidi), not proved here |
| C7 | The proof is self-contained apart from classical appendix facts and shorter than Isett's | moderate | true of Theorem 1.1 as read; Proposition D.1 for N = 0 is Constantin's lemma adapted to the torus by a sketch |

## Method

1. Normalize e by the Euler scaling v ↦ Γv(x, Γt) so that (2.13) holds;
   start from (v₀, R₀, p₀) = (0, 0, 0).
2. At step q:
   - **mollify** v_q at scale ℓ (Proposition 2.2, using the
     Constantin–E–Titi commutator estimate, Proposition A.2);
   - **glue**: solve Euler exactly from v_ℓ(t_i), t_i = iτ_q; join with a
     partition of unity in time; the stress lives on I_i, is trace-free,
     and is estimated through vector potentials z_i = (−Δ)^(−1)curl v_i
     (Proposition 3.4), gaining a factor ℓ;
   - **perturb**: choose cut-offs η_i on disjoint squiggling space-time
     slabs covering every time, distribute the energy deficit ρ_q(t) as
     ρ_{q,i} ∝ η_i²ρ_q, form R̃_{q,i} = ∇Φ_i(ρ_{q,i}Id − η_i²R̊_q)∇Φ_iᵀ/ρ_{q,i}
     near the identity, and add
     w_o = Σ_i ρ_{q,i}^(1/2)(∇Φ_i)^(−1)W(R̃_{q,i}, λ_{q+1}Φ_i) with W the
     Mikado flows and Φ_i the back-to-labels map, plus a corrector w_c
     making w_{q+1} a curl.
3. The new stress is the inverse divergence of the Nash, transport and
   oscillation errors; the cross terms between different i vanish because
   the supports are disjoint.
4. v_q converges uniformly; R̊_q → 0, so v solves Euler; (2.10) with
   δ_q → 0 gives ∫|v|² = e; Section 2.2 gives joint Hölder regularity.

## Concepts

- **Euler–Reynolds system**: ∂_t v + div(v⊗v) + ∇p = div R̊, R̊ symmetric
  and trace-free, p of mean zero.
- **Smooth strict subsolution**: (v̄, p̄, R̄) solving the same with −div R̄
  and R̄ positive definite. Its "energy" is ∫(|v̄|² + tr R̄).
- **Gluing** (Isett's): replacing an approximate solution by exact local
  solutions joined in time, so the error is confined to separated
  intervals.
- **Mikado flows** (Daneri and Székelyhidi): stationary Euler solutions
  W(R, ξ) with mean zero and ∫W⊗W dξ = R, for R in a compact set of
  positive-definite matrices (Lemma 5.1).
- **Squiggling stripes**: space-time regions bounded by
  t = t_i + (τ_q/6)(sin 2πx₁ ± ½), so that each time slice meets some
  region while the regions stay disjoint.
- **Dissipative / admissible** (as used here): total kinetic energy
  strictly decreasing in time.

## Connections

It is a direct modification of Isett ([LIT-1255](../literature.d/LIT-1255.md)), with Mikado flows from
Daneri and Székelyhidi (2016) and the convex-integration framework of De
Lellis and Székelyhidi (2009–2014) after Nash and Kuiper; earlier exponents
were 1/10, 1/5 (Isett; Buckmaster, De Lellis, Isett and Székelyhidi) and
1/3 in L¹_tC^β_x (Buckmaster, De Lellis and Székelyhidi). The positive half
is Constantin, E and Titi ([LIT-1248](../literature.d/LIT-1248.md)), after Eyink, with Cheskidov et al.
for the endpoint space. The non-L^∞ precursors are Scheffer and Shnirelman.
Later work: Isett, "Nonuniqueness and existence of
continuous, globally dissipative Euler flows" (arXiv:1710.11186); Daneri,
Runa and Székelyhidi, "Non-uniqueness for the Euler equations up to
Onsager's critical exponent" (arXiv:2004.00391), for admissible
non-uniqueness from given data; and Giri, Kwon and Novack, "The L³-based
strong Onsager theorem" (arXiv:2305.18509), which obtains the local
energy inequality in an L³-based class, since skimmed ([LIT-tmpfah3l](../literature.d/LIT-tmpfah3l.md),
[NOTE-tmpms8u2](NOTE-tmpms8u2.md)). The first two are not read.

## Bearing on the record

- **[THEORY-tmpnvuqr](../theory.d/THEORY-tmpnvuqr.md)** is filed from this reading, Proposed. It states
  Theorem 1.1 with e strictly decreasing and the record's consequence: by
  [THEORY-749](../theory.d/THEORY-749.md)'s energy balance, for every s < t the integrated flux
  ∫_s^t Π_ε across a mollification scale tends to ½(e(t) − e(s)) < 0. So
  the resolved field loses energy to vanishing scales over every interval.
- **[QUESTION-219](../questions.d/QUESTION-219.md) and A3's dissipative cascade.** This is the reading
  [NOTE-974](NOTE-974.md) said the question needed. The answer to "does a rough Euler
  solution carry a one-way, dissipative flux into vanishing scales?" is yes,
  with three qualifications the question should carry:
  - *Global, not local.* "Admissible" here is the total-energy inequality.
    Nothing is proved about the sign of the local defect, so backscatter in
    parts of the box is not excluded.
  - *Chosen, not forced.* The same theorem gives increasing energy. At
    β < 1/3 the Euler equations alone do not set the direction of
    transfer; the energy profile is a free input. That fits A3's separation
    of "direction of transfer" from "that scales exist" and "locality".
  - *Not turbulence.* No link to vanishing viscosity, to a constant-flux
    range, or to uniqueness.
  The question's text, "The admissible version (Buckmaster, De Lellis,
  Székelyhidi and Vicol 2019) is not held", can now cite [LIT-tmpv4d6t](../literature.d/LIT-tmpv4d6t.md) and
  [THEORY-tmpnvuqr](../theory.d/THEORY-tmpnvuqr.md). On the question proper, whether flux picks out a unit:
  if anything negative. The dissipation rate is −½e′, an arbitrary input,
  and the transfer is carried by non-interacting waves on disjoint
  space-time slabs; nothing persists that A5's conditions (2)–(4) could
  recognise as self-maintained organization.
- **[THEORY-763](../theory.d/THEORY-763.md).** Its "What this does not say" names this paper as the
  later theorem the record did not hold; it can now cite [THEORY-tmpnvuqr](../theory.d/THEORY-tmpnvuqr.md).
  Its promote_when names this paper as a possible independent proof, but
  only of the Hölder non-conservation statement, not of Isett's compact time
  support, which this construction cannot give (e > 0).
- **[THEORY-749](../theory.d/THEORY-749.md).** Its summary says "that dissipative solutions exist below
  1/3 is a later theorem (Isett 2018 and others), which the record has not
  read". Isett's solutions are not dissipative; this is the dissipative one,
  now read. The sentence should cite [THEORY-tmpnvuqr](../theory.d/THEORY-tmpnvuqr.md) for the dissipative
  case and [THEORY-763](../theory.d/THEORY-763.md) for non-conservation.
- **[QUESTION-218](../questions.d/QUESTION-218.md) and [QUESTION-222](../questions.d/QUESTION-222.md) (closure).** As with Isett: the
  Euler–Reynolds system is the closure problem with the unclosed stress R̊,
  and convex integration runs it backwards. Theorem 1.3 sharpens the point:
  every smooth coarse field with a positive-definite "Reynolds stress" R̄ is
  the weak-* limit of exact solutions whose fine scales reproduce R̄ on
  average. A coarse description plus its stress does not determine the fine
  field. Not filed.
- **The other key entries** ([THEORY-733](../theory.d/THEORY-733.md), [THEORY-257](../theory.d/THEORY-257.md), [THEORY-661](../theory.d/THEORY-661.md), [CLAIM-157](../claims.d/CLAIM-157.md),
  [CLAIM-331](../claims.d/CLAIM-331.md), [CLAIM-327](../claims.d/CLAIM-327.md), [CLAIM-388](../claims.d/CLAIM-388.md), [THEORY-755](../theory.d/THEORY-755.md)) and [QUESTION-217](../questions.d/QUESTION-217.md),
  [QUESTION-220](../questions.d/QUESTION-220.md), [QUESTION-221](../questions.d/QUESTION-221.md): not addressed. The frequencies λ_q form a
  coarse-to-fine sequence of corrections, but as a construction device.

No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- **The meaning of "admissible".** The title promises admissible solutions
  and the text never defines the word. What is proved is a prescribed, and
  so possibly strictly decreasing, total energy. A reader who takes
  "admissible" in the stronger, local sense (the local energy inequality)
  would be overreading the paper.
- **The abstract's "typical".** Theorem 1.3 proves weak-* density of
  solutions near subsolutions, not genericity in any Baire or measure
  sense, and its solutions have energy ∫(|v̄|² + tr R̄), which need not
  decrease, so they are not all "dissipative solutions" as the abstract
  says.
- **The claim about Isett's solutions.** "Fails to be monotonic on any
  interval of time" is stated without argument. It may follow from
  details of Isett's construction; it is not in Isett's theorem.
- **Small slips.** Lemma 5.5 states a |k|^(−5) bound and its proof gives
  |k|^(−4); Definition 5.6 sums |k|^(−4), which converges in three
  dimensions, so nothing breaks. (2.37) and Proposition 6.2 omit the
  absolute value. Several subscripts are misprinted (ρ_{q+1,i}, w_q).
- **Scope.** Finite time interval, torus, e > 0 (never at rest), β < 1/3
  not the endpoint, no initial-value problem, no non-uniqueness for given
  data, nothing on Navier–Stokes.

## Open questions

- Are there C^β solutions, β < 1/3, satisfying the local energy inequality,
  so that transfer to vanishing scales is one-way at every point? In the
  L³-Besov class, yes (Giri, Kwon and Novack, [THEORY-tmp6pe5a](../theory.d/THEORY-tmp6pe5a.md), Proposed).
  For C^β it is still open; the best known is β < 1/7.
- Is any vanishing-viscosity limit of Navier–Stokes of this kind? Only a
  theorem about Navier–Stokes would settle it.
- Given an initial datum, how many admissible solutions start from it?
  Daneri, Runa and Székelyhidi (arXiv:2004.00391), not held.
- For [QUESTION-219](../questions.d/QUESTION-219.md): what in a flow, if not regularity, fixes the direction
  of transfer? Here the answer is "the constructor's choice of e", which
  suggests direction is a selection criterion (admissibility) imposed on
  the equations, not a consequence of them.
