---
status: Read
paper: LIT-tmpeyk8p
title: "Constantin, E and Titi — Onsager's conjecture on energy conservation"
version: 1
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Read in full from the authors' manuscript on Weinan E's Princeton page
    (the LIT's `url:`), 4 pages: a title page and three pages of text. The
    PDF was generated in 2000 from a file named "revised3.dvi" and carries
    the authors' 1994 affiliations. It is the manuscript, not the typeset
    CMP 165:207–209 article, which was not reached, so no differences from
    the published text could be checked. Text was extracted with pdftotext
    and every displayed equation was read from the rendered pages, since
    extraction garbled the integrals and the final estimate. Every line was
    read: the statement, the discussion of Kolmogorov and Eyink, and the
    proof. The proof was re-derived step by step in THEORY-tmp99aof.
    Identity (10) and the scalings (7), (8) and (12) were checked
    numerically on a synthetic field. Onsager (1949) and Eyink's 1992
    preprints, the paper's two references, were not read.
date: '2026-10-20'
summary: >-
  A one-page proof that a weak solution of the 3D incompressible Euler
  equations on the periodic box conserves energy if it lies in
  L³(0,T; B^α_{3,∞}) ∩ C([0,T]; L²) with α > 1/3. The flux of energy
  into scales below a mollification scale ε is written exactly as a
  commutator, (u⊗u)^ε − u^ε⊗u^ε = r_ε − (u−u^ε)⊗(u−u^ε), of size ε^(2α),
  against a gradient of size ε^(α−1), so the flux is O(ε^(3α−1)) and
  vanishes. This is the positive half of Onsager's conjecture only. It
  does not show that rougher solutions dissipate. Two printed formulas in
  the manuscript are wrong as typeset, without effect on the result.
---
<!-- inactive-ok-file: CLAIM-157 CLAIM-327 CLAIM-331 THEORY-257 — Proposed; open claims and readings this reading is set beside and does not address, nothing here rests on their being settled -->
# NOTE-tmpqux8d: Constantin, E and Titi — Onsager's conjecture on energy conservation

## Contribution

It proves the sharp positive half of Onsager's 1949 conjecture, in the
Besov scale. A weak solution of incompressible Euler whose velocity
increments obey ‖u(·+y) − u‖_{L³} ≤ C|y|^α with α > 1/3, uniformly enough
in time, conserves kinetic energy exactly. Before it, by the paper's own
account, Eyink had proved conservation for Hölder exponent α > 1/2, and
for α > 1/3 only under the stronger norm Σ_k |k|^α |û_k|. The proof is
short enough to be checked in full, and it became the template for later
work.

## Key insight

Energy can leave a weak solution only through the flux into vanishingly
small scales, and that flux is a commutator. Mollify at scale ε. The
energy of u^ε changes by ∫(u⊗u)^ε : ∇u^ε. The part u^ε⊗u^ε contributes
nothing (it is transport by a divergence-free field), so only the subgrid
stress (u⊗u)^ε − u^ε⊗u^ε matters, and it is quadratic in increments over
distances below ε. Increments of size ε^α, twice, against a gradient of
size ε^(α−1), give a flux of size ε^(3α−1). Above α = 1/3 the flux into
the unresolved scales dies as the resolution is refined, so nothing can be
lost there. At α = 1/3 the bound stops decaying, which is exactly the
Kolmogorov scaling (4). Regularity decides whether the coarse-grained
flux can survive the limit.

## Assumptions

- **Domain.** The periodic box D = [0, 1]³, "to avoid questions regarding
  boundaries". Three dimensions are stated; nothing in the proof uses d = 3
  except the notation.
- **Weak solution.** u satisfies the distributional form (1) of
  ∂_t u + ∇·(u⊗u) + ∇p = 0 against every smooth, compactly supported
  test field ψ, with initial data u(·, 0). Divergence-free u is implicit.
  The pressure's regularity is not stated. On the torus it is fixed, up to
  a function of time that has no gradient, by −Δp = ∂_i∂_j(u_iu_j), so
  p ∈ L^{3/2} follows from u ∈ L³; the proof needs only that ∇p^ε is a
  gradient.
- **Regularity.** u ∈ L³([0, T]; B^α_{3,∞}(D)) ∩ C([0, T]; L²(D)) with
  α > 1/3. For 0 < α < 1, B^α_{3,∞} is the space with
  ‖u‖_{L³} + sup_y |y|^(−α)‖u(·+y) − u‖_{L³} finite; that is what (6)
  uses. The time integrability is L³, so the bound is integrated in time,
  not uniform.
- **Mollifier.** φ ∈ C₀^∞(R³), "a standard mollifier supported in
  B(0, 1)": ∫φ = 1, and, for (12) as written, φ ≥ 0.

## Key results

- **Theorem.** Under the assumptions above, with α > 1/3,
  ∫_D |u(x, t)|² dx = ∫_D |u(x, 0)|² dx for t ∈ [0, T). The manuscript
  writes the integrals in (2) over R³; on the periodic box they are over D.
- **Besov facts (6)–(8).** ‖u(·+y) − u‖_{L³} ≤ C|y|^α‖u‖_{B^α_{3,∞}};
  ‖u − u^ε‖_{L³} ≤ Cε^α‖u‖; ‖∇u^ε‖_{L³} ≤ Cε^(α−1)‖u‖. Re-derived in
  [THEORY-tmp99aof](../theory.d/THEORY-tmp99aof.md): (6) is the definition, and (7) and (8) follow from it by
  Minkowski's inequality, using ∫φ_ε = 1 and ∫∇φ_ε = 0.
- **Main identity (10)**, pointwise: with
  r_ε(u, u)(x) = ∫φ_ε(y) δ_yu(x) ⊗ δ_yu(x) dy and δ_yu(x) = u(x−y) − u(x),
  (u⊗u)^ε = u^ε⊗u^ε + r_ε(u, u) − (u − u^ε)⊗(u − u^ε). Re-derived by
  expanding r_ε; checked numerically to 10⁻¹⁴.
- **Energy balance (11)** of the mollified field:
  ∫|u^ε(t)|² − ∫|u^ε(0)|² = 2∫₀ᵗ dτ ∫ Tr((u⊗u)^ε ∇u^ε).
- **Commutator bound (12).** ‖r_ε(u, u)‖_{L^{3/2}} ≤ Cε^(2α)‖u‖²_{B^α_{3,∞}}.
- **Flux bound** (unnumbered, last display):
  |∫|u^ε(t)|² − ∫|u^ε(0)|²| ≤ Cε^(3α−1)∫₀ᵗ ‖u(τ)‖³_{B^α_{3,∞}} dτ → 0.
  *Holds when:* α > 1/3. At α = 1/3 the bound is constant in ε and
  decides nothing.
- **Physical reading** (stated, not proved): "if
  ⟨|u(x + r) − u(x)|³⟩^(1/3) ≤ Cr^α for α > 1/3 then ε̄ = 0."

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Weak Euler solutions in L³(0,T; B^α_{3,∞}) ∩ C(0,T; L²) with α > 1/3 conserve energy | strong | the proof; re-derived step by step in [THEORY-tmp99aof](../theory.d/THEORY-tmp99aof.md) |
| C2 | This implies the Hölder version of the positive half | strong | C^α ⊂ B^α_{3,∞} on the bounded box; needs L³ integrability of the Hölder norm in time |
| C3 | This is the "sharp result" | moderate as written | sharp in the exponent, as the later negative half shows; not proved sharp here, and the endpoint α = 1/3 is not covered (see Limitations) |
| C4 | Onsager conjectured that (2) "ceases to be true for α ≤ 1/3" | weak as phrased | Onsager's claim, and the later theorems, are that dissipative solutions exist, not that every rough solution dissipates (see Limitations) |
| C5 | If ⟨|δu(r)|³⟩^(1/3) ≤ Cr^α with α > 1/3, then ε̄ = 0 | weak as proved here | an interpretation. ε̄ is the viscous dissipation of Navier–Stokes; the theorem is about Euler weak solutions, and the passage between them is not given |
| C6 | Eyink proved the α > 1/2 Hölder case and α > 1/3 under norm (5) | not checked | the paper's report of [2], which the record does not hold |

## Method

1. Mollify at scale ε. The mollified field u^ε is smooth in space and
   satisfies ∂_t u^ε + ∇·(u⊗u)^ε + ∇p^ε = 0. Multiply by u^ε and integrate:
   the pressure term vanishes since ∇·u^ε = 0, and integration by parts
   gives (11).
2. Split the mollified flux by identity (10). The term u^ε⊗u^ε contributes
   ∫u^ε_i u^ε_j ∂_i u^ε_j = ∫u^ε·∇(½|u^ε|²) = 0.
3. Bound what remains by Hölder's inequality, L^{3/2} against L³, using
   (12) for r_ε, (7) twice for (u − u^ε)⊗(u − u^ε), and (8) for ∇u^ε.
4. Let ε → 0. The right side vanishes for α > 1/3, and ∫|u^ε(t)|² →
   ∫|u(t)|² at each t because u(t) ∈ L².

The paper does step 1 "as if the solution is differentiable in time" and
says the time mollification is "straightforward". It is: testing (1) with
ψ = θ(t)φ_ε(x − ·)e_j shows ∂_t u^ε ∈ L^{3/2}(0, T; C^∞), so
t ↦ ∫|u^ε|² is absolutely continuous and its derivative is 2∫u^ε·∂_t u^ε.

## Concepts

- **Weak solution**: a field satisfying the Euler equations only after
  integration against smooth test fields, (1). Such a field need not have
  derivatives, so energy conservation, automatic for smooth solutions, is
  not.
- **B^α_{3,∞}**: fields whose L³-averaged increments scale at most as
  |y|^α. An L³ analogue of Hölder continuity, weaker than C^α, and the
  space-averaged form of the scaling Kolmogorov's theory assigns to
  turbulent velocity at α = 1/3.
- **r_ε(u, u)**: the mollifier-weighted second moment of increments over
  distances below ε. With (u − u^ε)⊗(u − u^ε) it makes up the subgrid
  stress, (u⊗u)^ε − u^ε⊗u^ε = r_ε − (u − u^ε)⊗(u − u^ε).
- **Path-wise** (the paper's word): a statement about each solution, as
  against Kolmogorov's statements about ensemble averages.

## Connections

It proves what Onsager (1949) asserted, in a sharper space than his
Hölder one, and improves on Eyink's preprints of 1992 (published 1994),
which the paper credits with α > 1/2 and with α > 1/3 under norm (5).
Neither reference is held by the record. The mollified flux in step 2 is
exactly the subgrid energy flux of the filtering approach to turbulence:
∫(u⊗u)^ε : ∇u^ε = ∫τ_ε : ∇u^ε with τ_ε = (u⊗u)^ε − u^ε⊗u^ε, the
Π_ℓ of Eyink and Aluie ([LIT-tmp2snx1](../literature.d/LIT-tmp2snx1.md), [NOTE-tmp5es2s](NOTE-tmp5es2s.md)) up to sign and the
choice of kernel. The estimate is the one [THEORY-tmpfcxzq](../theory.d/THEORY-tmpfcxzq.md) re-derives, read
in the other direction (see Bearing). Later work the record does not
hold, named here so that what this paper did not do is placed: the local
energy balance with a dissipation measure (Duchon and Robert 2000); the
endpoint, conservation in a space just below B^{1/3}_{3,∞} (Cheskidov,
Constantin, Friedlander and Shvydkoy 2008); and the negative half,
dissipative weak solutions in C^α for every α < 1/3 (Isett 2018, after
De Lellis and Székelyhidi's convex integration; Buckmaster, De Lellis,
Székelyhidi and Vicol 2019 for admissible ones).

## Bearing on the record

- **[THEORY-tmp99aof](../theory.d/THEORY-tmp99aof.md)** is filed from this reading, Active: the
  theorem and its proof, re-derived step by step, with the bound
  O(ε^(3α−1)) on the flux into the unresolved scales.
- **A3's point, which [QUESTION-tmpmz64i](../questions.d/QUESTION-tmpmz64i.md) carries in spirit.** A3 cited the
  "Constantin–E–Titi work" for "Onsager's 1/3, where the regularity of a
  field decides whether the unresolved scales vanish in the limit", and
  the LIT took it as the ground for "a coarse-grained flux can survive as
  the scale goes to zero". The paper proves half of that. **Above 1/3,
  the flux of energy into the unresolved scales must vanish as the
  resolution is refined.** It does not prove that below 1/3 it survives.
  Roughness below 1/3 permits a surviving flux; it does not produce one.
  A shear flow u = (f(x₂), 0, 0), with f as rough as one likes, is a
  stationary weak solution whose flux is zero at every ε: the only
  non-zero component of (u⊗u)^ε is (f²)^ε in position (1, 1), and it
  meets ∂₁u^ε₁ = 0, so Σ_{ij}(u_iu_j)^ε ∂_iu^ε_j = 0 pointwise. That
  "a coarse-grained flux can survive" is true is the negative half, from
  Isett (2018) on, which the record has not read. The LIT's "Why this is
  here" and [QUESTION-tmpmz64i](../questions.d/QUESTION-tmpmz64i.md) should not cite this paper for survival.
- **[THEORY-tmpfcxzq](../theory.d/THEORY-tmpfcxzq.md).** Its hypothesis, ‖δu(r)‖₃ ≤ C₀u_rms(r/L)^σ,
  is the B^σ_{3,∞} condition, and its prefactor (u_rms³/L)(ℓ/L)^(3σ−1) is
  this paper's ε^(3α−1). Read at a fixed field as ℓ → 0, that prefactor
  is the Constantin–E–Titi bound on the whole flux: it vanishes for
  σ > 1/3 and is constant at σ = 1/3. So a non-zero mean flux through an
  inertial range, which Eyink and Aluie assume, is consistent only with
  σ₃ ≤ 1/3 in the limit, and Kolmogorov's 1/3 is the largest exponent at
  which it can be. [THEORY-tmpfcxzq](../theory.d/THEORY-tmpfcxzq.md)'s Connections could say so. The two
  results use the same three estimates; Eyink and Aluie split the flux by
  which scales it comes from, and this paper bounds it whole.
- **[QUESTION-tmpmz64i](../questions.d/QUESTION-tmpmz64i.md) itself.** Nothing here bears on whether a pattern
  of transfer picks out a unit. The paper concerns one field and the
  energy crossing an analyst-chosen scale ε. Its relevance is narrower:
  it shows that a flux across scales, as a quantity, is fixed by a
  balance law and a regularity class, and that in a regular enough class
  there is no flux to the smallest scales to be organized at all. A5's
  requirement, "a balance law for a specified transferred quantity", is
  met here in its purest form.
- **[THEORY-661](../theory.d/THEORY-661.md), [CLAIM-157](../claims.d/CLAIM-157.md), [THEORY-733](../theory.d/THEORY-733.md), [THEORY-257](../theory.d/THEORY-257.md),
  [CLAIM-331](../claims.d/CLAIM-331.md), [CLAIM-327](../claims.d/CLAIM-327.md), [CLAIM-tmpkoi6k](../claims.d/CLAIM-tmpkoi6k.md), [THEORY-tmpj32n2](../theory.d/THEORY-tmpj32n2.md).**
  Not addressed. There is no decomposition into blocks, no aggregation,
  no time scales and no closure here. The mollified equation for u^ε is
  not closed: it depends on (u⊗u)^ε, which u^ε does not determine. That
  is a small instance of [QUESTION-tmpxapb2](../questions.d/QUESTION-tmpxapb2.md)'s and [QUESTION-tmplru2n](../questions.d/QUESTION-tmplru2n.md)'s
  closure problem, and the paper's point is that the unclosed term's
  effect on energy vanishes in the limit for regular fields, not that it
  can be closed.
- **[QUESTION-tmp8qovh](../questions.d/QUESTION-tmp8qovh.md), [QUESTION-tmpproc1](../questions.d/QUESTION-tmpproc1.md), [QUESTION-tmpt64jh](../questions.d/QUESTION-tmpt64jh.md).** Nothing.
  Mollifiers at different ε are nested only in the trivial sense that
  u^ε → u; the paper uses one scale at a time.

No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- **Two printed formulas are wrong in this manuscript.** In (2) the
  integrals are over R³; the solution lives on the periodic box D. In the
  final estimate the middle line reads
  ‖r_ε‖^{2/3}_{L^{3/2}}‖∇u^ε‖^{1/3}_{L³} + ‖u − u^ε‖^{2/3}_{L³}‖∇u^ε‖^{1/3}_{L³}.
  That is not what Hölder's inequality gives, and it is not homogeneous:
  the left side is cubic in u and these terms are of degree 5/3. Inserting
  (7), (8) and (12) into it would give ε^((5α−1)/3), not the ε^(3α−1) of the
  next line. The correct middle line is
  ‖r_ε‖_{L^{3/2}}‖∇u^ε‖_{L³} + ‖u − u^ε‖²_{L³}‖∇u^ε‖_{L³}, which gives
  ε^(3α−1) and the theorem. Whether the typeset article corrects either
  could not be checked.
- **The proof is terse, not gapped.** Three steps are left to the reader:
  the time mollification, the pressure's regularity, and the convergence
  ∫|u^ε(t)|² → ∫|u(t)|². Each is routine and is written out in
  [THEORY-tmp99aof](../theory.d/THEORY-tmp99aof.md).
- **"Ceases to be true for α ≤ 1/3" misstates the converse.** What is
  conjectured, and now proved by others, is that energy-dissipating weak
  solutions exist below 1/3. Conservation does not fail for every rough
  solution: the rough shear flows above conserve energy. The paper's
  "sharp" is sharp in this sense only.
- **The endpoint.** At α = 1/3 the bound is constant in ε and the
  theorem says nothing. Conservation in a space slightly smaller than
  B^{1/3}_{3,∞} came later (Cheskidov et al. 2008, not held).
- **The physical reading overreaches the proof.** "If ⟨|δu|³⟩^(1/3) ≤ Cr^α
  for α > 1/3 then ε̄ = 0" moves from a statement about Euler weak
  solutions to one about the viscous dissipation of Navier–Stokes in the
  limit, and from a path-wise bound to an ensemble average ⟨·⟩. The
  theorem needs the bound for the solution itself, integrated in time.
  The passage to Navier–Stokes needs a convergence argument the paper
  does not give, and the record has not checked one.
- **Global, not local.** The theorem conserves the total energy. A local
  energy balance, with a defect measure saying where dissipation happens,
  is Duchon and Robert's (2000), not here.
- **Nothing about existence or the negative half.** It does not show that
  solutions with this regularity exist for given data, and it does not
  construct dissipative solutions.

## Open questions

- Does any weak solution arising as an inviscid limit of Navier–Stokes
  belong to a class with α ≤ 1/3 while dissipating? The negative half
  gives dissipative weak solutions, constructed by convex integration,
  not as vanishing-viscosity limits. Whether turbulence's limit is one of
  them is a question about Navier–Stokes, which only a theorem about the
  equations would settle.
- For the record: does a surviving flux into the unresolved scales
  correspond to anything the record would call organization, or is it, in
  A5's term, mere transport? This paper only says when there is none.
