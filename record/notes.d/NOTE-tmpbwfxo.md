---
status: Read
paper: LIT-tmp7ay36
title: 'Statistical Physics of Adaptation'
version: 1
history:
- version: 1
  date: '2026-10-02'
  note: >-
    Read in full (arXiv:1412.1875 v1, 5 Dec 2014, the only arXiv version,
    24 pp., text extracted with PyMuPDF): the abstract, Introduction,
    "Entropy production and stochastic evolution" (Eqs. 1–8),
    "Self-organization and dissipation-driven adaptation", "Dissipation and
    drift in time-varying energy landscapes" (Eqs. 9–13, Figs. 3–4), the
    Discussion and the 12 references. I checked the passage from Eq. (3) to
    Eq. (8) and recomputed Eqs. (10)–(13). The Phys. Rev. X version of 2016
    was not seen (HTTP 403 from the publisher), so this is a reading of the
    preprint. The Crooks relation (Eq. 2) and England's macrostate
    relation (Eq. 3, from LIT-tmp2fe4j) were taken as given.
date: '2026-10-02'
summary: >-
  A macrostate fluctuation relation for driven systems, rearranged as an
  internal-entropy term, a reversal term and Ψ − Φ = −ln⟨e^{−βΔQ}⟩. It is
  read as a tendency of driven matter towards states formed by reliable
  work absorption and dissipation, "adaptation" without replication. The
  relation is exact. The tendency needs the other two terms held fixed,
  which the paper arranges only in contrived one-particle landscapes; the
  many-body claim and the "adaptive resonance" simulation are argued and
  reported, not shown.
---

<!-- inactive-ok-file: THEORY-026 THEORY-030 — Proposed; named as the accounts this reading is contrasted with, not as support -->

# NOTE-tmpbwfxo: Statistical Physics of Adaptation

## Contribution

The paper proposes a physical, replication-free notion of adaptation: a
structure is well adapted to a drive if its formation involved
exceptionally reliable absorption and dissipation of the drive's work. It
gives an exact expression in which that quantity appears, and two toy
models in which it visibly biases where probability flows. Before it,
England's 2013 relation had been used only to bound the heat of
replication.

## Key insight

In a driven system, how likely an outcome is depends not only on its
entropy and on how hard it is to reach, but also on how much work the paths
to it absorbed and how reliably they shed it as heat. Configurations that
happen to resonate with the drive absorb more work. So, all else equal, the
system drifts towards them, and what it ends up in looks "tuned" to its
environment.

## Assumptions

- **Setting.** Classical Hamiltonian H_sys(x, λ(t)) + H_bath(y) +
  h_int(x, y) with weak coupling. The field λ(t) acts on the system only
  and is fixed in advance, with no feedback from the system to the drive.
  The bath is at fixed inverse temperature β.
- **Crooks's relation** for microtrajectories (Eq. 2) and its macrostate
  form from England 2013 (Eq. 3).
- **For Eq. (5).** Driving long enough that x(0) and x(τ) are uncorrelated
  except through the macrostate constraints, and densities near-uniform on
  each macrostate, so that 1/p ∼ Ω.
- **For Eq. (6).** Averages taken over a "select sub-ensemble" of likely
  forward paths, with reversal probabilities restricted to their reverse
  movies. This is stated, not derived, and the text calls the next step
  (Eq. 7) "heuristic".
- **For the adaptation claim.** Outcomes compared at equal internal entropy
  and equal reversal probability. The paper imagines parcelling phase space
  into macrostates of equal size that are equally kinetically accessible.
  It does not show such a parcelling exists for a many-body system.
- **Toy models.** Arrhenius hopping, r_{i→j} = r⁰_ij exp[−β(B_ij − E_i)]
  (Eq. 9), with βΔE ≫ 1 and r ≪ 1/τ ≪ ω.

## Key results

- **Eq. (8).** ln[π^fwd(I→II)/π^fwd(I→III)] = Δln Ω_{II,III} + ln[π^rev
  ratio] + ΔΨ − ΔΦ, with Ψ = β⟨ΔQ⟩ and Φ = ln⟨e^{−βΔQ}⟩ + Ψ. By
  definition Ψ − Φ = −ln⟨e^{−βΔQ}⟩. The cumulant expansion (Eq. 7) only
  interprets this, as mean minus β²σ²/2 and higher terms.
- **Three-state model (Fig. 3).** With E₁(t) = −ΔE cos ωt/2 and B₁₂(t) =
  ΔE − ΔE cos ωt/2, the return rates from x₁ and x₃ are equal, and the
  cycle-averaged rates are r̄(2→1) = re^{−βΔE} I₀(βΔE/2) > r(2→3) =
  re^{−βΔE}. I recomputed this: the average of exp(βΔE cos ωt/2) over a
  period is I₀(βΔE/2). Hops left release βΔE/2 and hops right release
  nothing, so Ψ(2→1) = βΔE/2 and Ψ(2→3) = 0, and r_max(2→1)/r(2→3) =
  e^{βΔE/2} = e^{ΔΨ} (Eqs. 11–12).
- **Two-path model (Fig. 4).** Two barriers driven out of phase give mean
  dissipation Ψ = 0 and Φ = ln cosh(βΔE/2) ≃ βΔE/2. The forward rate is
  ln r_tot ≃ ln[2re^{−βΔE} I₀(βΔE/2)] ≃ −βΔE/2, so ln r ≃ −Φ (Eq. 13).
  Both checked.
- **Futile cycles.** For paths starting and ending in the same state, Ψ =
  Φ ≥ 0. Heat produced in cycles cancels out of Eq. (8) and drives no
  drift.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The log-odds of two driven outcomes decompose into internal entropy, reversal probability and Ψ − Φ | strong for the exact form, Eqs. (3)–(4); moderate for Eqs. (5)–(6) | Eq. (5) adds no-correlation and near-uniformity assumptions; Eq. (6)'s restriction to likely paths is stated, not derived |
| C2 | All else equal, driven systems favour outcomes formed by reliable work absorption and dissipation | moderate in toy models; weak in general | shown for two contrived hopping landscapes (Eqs. 12–13); "all else equal" is not shown achievable for many-body systems |
| C3 | Many-body driven systems will drift into phase-space regions particularly suited to work absorption | weak | a plausibility argument: some of ∼10²⁵ directions "should" mimic the drift pattern |
| C4 | Such adaptation requires no self-replication | follows from C2–C3 as stated | the argument never uses replication; its strength is that of C2–C3 |
| C5 | If the system is made of self-replicators, the Darwinian and thermodynamic accounts of adaptation "become one and the same" | assertion | supported only by citing England's replication heat bound |
| C6 | A driven toy chemical mixture shows "adaptive" resonance tracking the drive frequency | not shown | a summary of a study "published in a separate article, rather than shown here" |
| C7 | Maximum-entropy-production principles miss the fluctuation term | informal argument | Ψ alone does not fix Eq. (8); no MEP model is analysed |

## Concepts

- **Macrostate.** A set of microstates sharing an observed property (I, II,
  III); the paper insists the grouping is the observer's.
- **Reversal probability π^rev.** The probability of the time-reversed
  movie with reversed momenta and drive.
- **Ψ (dissipation).** Mean heat released into the bath on the way to an
  outcome, β⟨ΔQ⟩.
- **Φ (fluctuation term).** Ψ + ln⟨e^{−βΔQ}⟩ ≥ 0. Large when the heat
  released varies widely between paths.
- **Dissipative (dissipation-driven) adaptation.** The drift of a driven
  system towards states whose formation involved reliably high Ψ − Φ,
  showing a "finely-tuned" response to the drive.

## Connections

- **England 2013, [LIT-tmp2fe4j](../literature.d/LIT-tmp2fe4j.md) ([NOTE-tmpeo3wn](NOTE-tmpeo3wn.md)).** Source of Eq. (3) and
  of the replication heat bound used in the Discussion.
- **Still et al., [LIT-327](../literature.d/LIT-327.md) ([NOTE-295](NOTE-295.md)), and [THEORY-026](../theory.d/THEORY-026.md).** The same setting,
  a fixed drive and no feedback, read the other way round; see "Bearing on
  the record".
- **Prigogine & Nicolis (1971), Martyushev (2010), Crooks (1999),
  Jarzynski (1997, 2006), Hatano–Sasa (2001).** The paper's lineage on
  dissipative structures, entropy-production principles and fluctuation
  relations. These are being filed in parallel in this batch.
- **[LIT-036](../literature.d/LIT-036.md) (primitive metabolic cycles).** A chemically driven
  self-organization whose dissipation is not computed. It is a candidate
  test of C2 that neither paper runs.
- **Not held in either record.** The follow-up simulation papers the
  Discussion anticipates, and Ito et al. 2013 on silver nanorods.

## Bearing on the record

- **[THEORY-026](../theory.d/THEORY-026.md) (Proposed): a different sense of "adapted"; no
  contradiction.** [THEORY-026](../theory.d/THEORY-026.md) says that for a system driven without
  feedback, dissipated work equals nonpredictive memory, so a system that
  tracks its drive predictively wastes less. This paper says a system whose
  configuration resonates with its drive absorbs and dissipates more, and
  is likelier to be reached. The two answer different questions. Still
  asks what a given system dissipates over a protocol; this paper asks
  which macrostate a stochastic evolution reaches. The record should keep
  the senses apart. "Matched to the drive" is efficient in one and
  dissipative in the other. This is the record's reading; neither paper
  cites the other.
- **[THEORY-030](../theory.d/THEORY-030.md): no bearing.** No information-processing step is priced.
- **[LIT-192](../literature.d/LIT-192.md) and the demarcation question.** The paper denies there is a
  physical line to draw between organism and dissipative structure, on
  purpose, and replaces it with a graded property of histories (C4). It
  offers no criterion that would separate a cell from a hurricane except
  degree of reliable dissipation.
- **No ML instruction.** "Learns" appears in scare quotes and refers to
  driven matter. Nothing here belongs in the anthology.
- **No new THEORY is indicated.** C2 is too weakly supported to source one.

## Limitations

- The central "all else equal" comparison is constructed by hand in each
  toy model (the barrier is moved to keep return rates equal). The paper
  admits it is "not immediately intuitive" what equal reversal probability
  means in general.
- Eq. (12) holds for the maximum rate, not the cycle-averaged one. The
  averaged ratio is I₀(βΔE/2), which differs from e^{βΔE/2} by a factor of
  order (πβΔE)^{1/2}, so the identity is a leading-order statement in
  βΔE.
- The many-body section is argued, not computed. The only many-body
  evidence (C6) is deferred to another article.
- "Adaptation" is defined by the paper's own quantity, so calling drifted
  states "better adapted" is partly a choice of word. Nothing shows the
  states are better at anything other than absorbing the drive's work.

## Open questions

- Can "equal internal entropy and equal reversal probability" be realized
  or estimated in a many-body driven system, so that C2 becomes testable?
- Does reliable dissipation predict which structures form in the record's
  driven self-organizing systems ([LIT-036](../literature.d/LIT-036.md)), once their dissipation is
  measured?
- How does the replication-free "adaptation" here relate to the
  predictive efficiency of [THEORY-026](../theory.d/THEORY-026.md) when the system can act on its
  drive? Neither paper treats feedback.

## Corrections

- none to a seeded skim (there was no seed)
- **A slip in the three-state model.** The text says that "during moments
  in the drive cycle when transits from x₂ to x₃ are likely (such as at t
  = 0) ... E₁ will be at its minimum". The x₂→x₃ rate is constant; the
  transits that cluster at the minimum of E₁ are those from x₂ to x₁. The
  result (Ψ(2→1) = βΔE/2) is unaffected.
