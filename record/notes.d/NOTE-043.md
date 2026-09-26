---
number: 43
status: Read
formerly:
- NOTE-tmpbih3l
paper: LIT-082
title: 'Observational entropy meets maximum entropy'
version: 2
history:
- version: 2
  date: '2026-09-25'
  note: >-
    Read in full (full text of arXiv 2503.15612v1 (19 Mar 2025, dated 21 Mar
    2025; the only version on arXiv as of 2026-09-26), 35 pp. Covered §§I–X,
    Figs. 1–7 (captions and prose; the plotted curves came through only as
    axis labels), Tables I–II, App. A (hard-sphere gas), App. B
    (random-matrix model), App. C (relative-entropy review, Props. 1–10),
    App. D (Proofs 1–12) and references [1]–[126]. Nothing skipped. PDF from
    arxiv.org/pdf/2503.15612, extracted with PyMuPDF to raw4/2503.15612.txt.
    I checked Proofs 1, 2, 7, 10 and 11 line by line. I did not run the
    simulation code ([99], github.com/jcschindler01/kinetic). The arXiv
    abstract page shows v1 only with no journal reference, and a Crossref
    title search found no published version, so it is unpublished as far as
    I can verify.). Upgraded from `Skimmed` to `Read`: the claims table,
    assumptions and results are new, and the skim is corrected where the
    full text disagreed.
date: '2026-09-25'
summary: >-
  The paper defines S^τ_M(ρ) = S(τ) − D_M(ρ‖τ) = −Σ_x p_x log(p_x/V_x),
  with V_x = Tr(τM_x)e^{S(τ)} (Eqs. 10–12). It is bounded as S(τ) ≥
  S^τ_M(ρ) ≥ S(ρ) when ρ obeys the constraint S(ρ;τ) ≤ S(τ) (Eqs. 17–18).
  It reduces to 24 listed entropies, and it removes traditional
  observational entropy's infinite-dimensional pathologies whenever S(τ) <
  ∞ (§VIII.7). Its "second laws" are bounds D_M(ρ̄‖τ) ≤ ε on the
  time-averaged state, split as equilibration plus prior-fit (Eq. 27). The
  paper proves the first term small in two regimes (Eqs. 28–29) and the
  second only under the ETH (Eq. 31). It states that in its own numerical
  examples the smallness "was [not] proved here analytically" (p. 12).
---

<!-- inactive-ok-file: LIT-049 — Proposed; Bourrat's coarse-graining account, named in Connections -->

# NOTE-043: Observational entropy meets maximum entropy

## Contribution

The paper gives one definition, S^τ_M(ρ), that takes three arguments: a state ρ, a measurement (POVM) M, and a prior τ that is the MaxEnt state for a linear constraint. The textbook entropies of statistical mechanics become choices of (M, τ): Jaynes, von Neumann, traditional observational entropy (OE), Boltzmann, Shannon over outcomes, diagonal, canonical, microcanonical, surface/volume, Wehrl, free energy, stochastic-thermodynamic, and the H-theorem entropies. The prior makes OE finite and continuous in infinite dimensions whenever S(τ) < ∞, where traditional OE is infinite for almost all states (§VIII.7). It also supplies a template for second laws: a bound on D_M(ρ̄‖τ), decomposed into an equilibration term and a prior-fit term. It proves both terms small under stated sufficient conditions.

## Key insight

Any state τ defines a linear constraint in "informational form", S(ρ;τ) ≤ S(τ), with cross entropy S(ρ;τ) = −Tr ρ log τ (Eq. 8). τ is automatically the MaxEnt state on that constraint set. Given such a prior, the natural entropy is "prior missing information minus what measurement M reveals relative to the prior": S(τ) − D_M(ρ‖τ). This equals a Shannon-over-macrostates term plus a mean Boltzmann term with *prior-weighted* volumes V_x = q_x·e^{S(τ)} (Eq. 13). The weighting by τ rather than by Tr M_x is what makes entropy increase generic. Example: gas in a gravitational field settles at the bottom, which is high entropy under canonical V_x but low under uniform W_x (§VI).

## Assumptions

- **States obey the constraint**: ρ ∈ χ_τ = {ρ : S(ρ;τ) ≤ S(τ)}. This is needed for the lower bound S^τ_M(ρ) ≥ S(ρ) (Eq. 18) and for I_max = S(τ) (Eq. 9). The upper bound (17) holds without it. §X says the definition may be applied to arbitrary (ρ, τ) with loss of (18).
- **"Well-behaved" constraints**: some state of the Gibbs form e^{−λX}/Z meets the constraint (§III.1).
- **Quantum S(ρ) ≥ 0** for Eq. 9. Classically this fails unless the phase-space measure l₀p₀ reflects a quantum resolution limit (p. 4).
- **Isolated systems** = unitary evolution under an undriven, time-independent H (§VII.2). Driven Hamiltonians and thermodynamic cycles are excluded (§X).
- **Eq. 28**: nondegenerate energies and energy gaps (via Short 2011, Cor. 1). ε = m/(4√d₂(ρ̄)), with m the number of outcomes and d₂ = (Tr ρ̄²)^{−1}.
- **Eq. 31**: diagonal ETH within a subextensive energy window containing the supports of τ and ρ̄.
- **Eqs. 32–33**: Eq. 26 holds; weak coupling (H_int ≈ 0); energy approximately constant in each shell; a definite macrostate; entropy treated as a smooth function of E_A.
- **Eq. 35**: macrostate probabilities follow a master equation whose rates satisfy local detailed balance R_xx′/R_x′x = q_x/q_x′.
- **Eq. 39**: finitely many nonzero V_x, and both states obey the constraint.

## Key results

- **Definition (Eqs. 10–13)** — S^τ_M(ρ) = S(τ) − D_M(ρ‖τ) = −Σ p_x log(p_x/V_x) = H(p) + Σ p_x log V_x.
- **I_max (Eq. 9, Proof 1)** — S(τ) = max over M and over ρ ∈ χ_τ of D_M(ρ‖τ). The maximum is attained by the pure state Σ√τ_k|k⟩ measured in τ's eigenbasis.
- **Bounds (Eqs. 17–18, Proof 2)** — S(τ) ≥ S^τ_M(ρ) ≥ S(ρ). The upper bound is tight iff M cannot distinguish ρ from τ.
- **Special cases (§V items 1–24, Table II)** — as listed under Contribution. Item 21 recasts von Neumann's H-theorem as D_M(ψ‖Uψ) < ε.
- **Open systems (Eqs. 22–23, Proof 3)** — S^{τ_SE}_{M_S⊗1}(ρ_SE) ≥ S(τ_SE) − D(ρ_S‖τ_S). So microstate equilibration of the subsystem implies OE maximisation for all system measurements.
- **Time-averaged prior (Eq. 24, Proof 4)** — S(ρ(t);ρ̄) = S(ρ̄) for all t, and S(ρ̄) ≤ S(τ) for any stationary valid τ.
- **Fluctuation bound (Proof 5, Eqs. D1–D2)** — Pr_t[S(τ) − S^τ_M(ρ(t)) ≥ δ] ≤ 2Δ/δ for averaging windows T ≥ T_eq. T_eq exists but is unquantified.
- **Decomposition (Eq. 27, Proof 7)** — D_M(ρ‖τ), time-averaged, equals D_M(ρ(t)‖ρ̄) time-averaged plus D_M(ρ̄‖τ).
- **Equilibration bounds** — Eq. 28: D_M(ρ‖ρ̄) time-averaged ≤ ε log m + g(ε), with g(ε) = −ε log ε + (1+ε)log(1+ε). Eq. 29: ≤ S(ρ̄). Eq. 30: D_M(ρ̄‖τ) ≤ log sup_x p̄_x/q_x. Eq. 31: ≤ ε_eth under the ETH.
- **Thermodynamics (Eqs. 32–35)** — if Eq. 26 holds with M = M_EA ⊗ M_EB and τ ∝ e^{−βH}, then T_A = T_B (Boltzmann temperatures) and ΔS = ∫dE_A/T_A + ∫dE_B/T_B > 0 with high probability. With the one-sided M_EA ⊗ 1_B, the equilibrium condition is T_A = β^{−1}, the global Gibbs temperature. In general d/dt S^τ_M = Σ ṗ_x (log q_x − log p_x) (Eq. 34). Under local detailed balance this equals Σ R_xx′p_x′ log(R_xx′p_x′/R_x′xp_x) ≥ 0 (Eq. 35).
- **Mathematical properties (§VIII, Proof 12)** — the OE is:
  - jointly concave in (ρ, τ) and concave in M;
  - monotone under post-processing (coarser M gives higher entropy) and under sequential measurement;
  - bounded below by S(τ) − D(ρ‖τ) (Eq. 36);
  - decomposed over convex mixtures as S^τ_M(Σλ_kρ_k) = Σλ_k S^τ_M(ρ_k) + I(M:E) (Eq. 37);
  - continuous: |ΔS| ≤ h(s) + s(log A + B) (Eq. 39);
  - bounded by recovery: S^τ_M(ρ) − S(ρ) ≥ sup_M D_M(ρ‖ρ̃_cg) (Eq. 43);
  - a resource monotone of τ-preserving maps when minimised over all M (xvi).
- **Numerics (§IX, Apps. A–B)**:
  - Quantum: a random-matrix model with d_A = d_B = 140, β_A = 0.25, β_B = 7.0, Δ_E = 0.5.
  - Classical: a 2-D hard-sphere gas with N = 500, four initial conditions, ΔP = 0.02.
  - Results: S^τ_M with canonical τ rises to S(τ) for every M shown in the chaotic cases. Traditional OE with the one-sided energy measurement decreases.
  - Integrable (free) gas: increase depends on M and the initial condition, and is slower with larger fluctuations. The authors present this as "somewhat different" from Chakraborti et al. and Garrido et al. [100, 101].

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | S(τ) ≥ S^τ_M(ρ) ≥ S(ρ) for ρ in the constraint set | strong | Proof 2 (RE non-negativity and monotonicity) |
| C2 | S(τ) is the maximum information extractable by any M from constrained states (quantum) | strong | Proof 1, with an explicit saturating state |
| C3 | The definition contains "most" physically relevant entropies as special cases | moderate | §V items 1–24, Table II; mostly direct substitution. Items 18–21 (H-theorems) are equivalences argued in outline, using App. A approximations (Sanov, N → ∞) |
| C4 | It resolves traditional OE's infinite-dimensional pathologies whenever S(τ) < ∞ | strong | Eq. 17 plus the continuity bound Eq. 39 (finite-outcome case only; the general case "still under investigation", Proof 12 vii) |
| C5 | Time-averaged OE near maximum implies rare, short-lived low-entropy fluctuations | strong | Proof 5–6, a Markov-inequality argument; T_eq exists but is unquantified |
| C6 | The equilibration term is small when m ≪ √d₂(ρ̄) | strong | Eq. 28, Proof 8 (from Short 2011 plus the continuity bound of [21]) |
| C7 | The prior-fit term is small under the ETH | moderate | Eq. 31; from the ETH as an assumption plus convexity |
| C8 | "Strong and general entropy increase theorems" follow (abstract, §X) | weak | only sufficient conditions (C6–C7) are proved. Δ is small in the examples only empirically: "in none of those cases was the smallness proved here analytically" (p. 12) |
| C9 | Eq. 26 implies heat flows from hot to cold (T_A = T_B; Clausius form) | moderate | Proof 9; heuristic steps (smoothness, weak coupling, constant energy in shells) |
| C10 | Under local detailed balance, OE is non-decreasing | strong | Proof 11; standard Schnakenberg-type algebra |
| C11 | The prior-weighted volumes are *necessary* for entropy increase to be generic | moderate | §VI argument plus Figs. 4–5 (one-sided energy measurement); no theorem |
| C12 | In integrable systems entropy increase is measurement- and state-dependent | weak | Fig. 6 free-gas curves, four hand-chosen initial conditions, "reasonably stable under perturbing" (asserted) |
| C13 | Von Neumann's H-theorem entropy difference is D_M(ψ‖Uψ) | moderate | §V item 21; a translation of von Neumann's notation, not re-derived in App. D |

## Method

The paper is a definition plus proofs, not an algorithm. The numerics evaluate Eq. 11 directly in the quantum model (exact diagonalisation). In the classical gas, volumes come from closed forms: Eq. A4 (a Sanov-theorem approximation, exact as N → ∞) for empirical-frequency measurements M_P(•), and Eqs. A10 and A12 for the energy measurements. The Sanov step estimates the dominant distribution P* by mixing the observed empirical distribution with Q "by the largest amount allowed by the bin width", so that energy and normalisation constraints are respected (App. A.a). This is a heuristic choice, and the paper does not bound its error.

## Concepts

- **Observational entropy (generalised) S^τ_M(ρ)** — Eq. 10; a function of the state, the measurement and the prior.
- **Traditional OE S_M(ρ)** — −Σ p_x log(p_x/W_x), with W_x = Tr M_x (Eq. 14). This is the case τ ∝ 1.
- **Informational form of a constraint** — S(ρ;τ) ≤ S(τ) (inequality) or = (equality) (Eq. 8). The sets are χ_τ and ∂χ_τ.
- **Effective macrostate volume** — V_x = Tr(M_xτ)e^{S(τ)} = q_x·d_eff, with d_eff = e^{S(τ)} (Eq. 12).
- **Measured relative entropy** — D_M(ρ‖σ) = D(p^ρ‖p^σ) (Eq. 2). Its supremum over M is ≤ D(ρ‖σ), with equality iff the states commute (App. C Prop. 3).
- **Equilibration (strong sense)** — D_M(ρ(t)‖τ) becomes and stays small, i.e. the entropy *maximises*. Merely reaching a steady value is not enough (§VII.1).
- **Coarse-grained state ρ_cg** — the Petz recovery of ρ from M's outcomes given prior τ (Eq. 40). Rotated and averaged variants are ρ^s_cg and ρ̃_cg (Eq. 41).

## Connections

- **Builds on:** Šafránek, Deutsch & Aguirre's observational entropy [1–4]; Jaynes (1957) MaxEnt [41–42]; von Neumann's 1929 H-theorem [30]; equilibration theory (Linden–Popescu–Short–Winter [77], Short [86], Reimann [85]); continuity bounds [21, 98]; Sutter–Berta–Tomamichel strong monotonicity [94].
- **Closest prior generalisation:** Bai et al. [24], S(ρ;τ) − D_M(ρ‖τ). This coincides with the present definition under equality constraints (§V item 12).
- **Positioned against:** Meier et al. [52], who question including volume terms; Scarpa et al. [103], who maximise after evaluating probabilities; Varizi & Correia [104], whose entropy production is the D(ρ‖τ) term.
- **In this record:**
  - [LIT-010](../literature.d/LIT-010.md) (Vinjanampathy & Anders, "Quantum Thermodynamics", Active) is the natural background for the Clausius and entropy-production special cases (§V items 17, 22–24). This paper does not cite it.
  - [LIT-027](../literature.d/LIT-027.md) (Varley & Hoel) and [LIT-049](../literature.d/LIT-049.md) (Bourrat) also treat coarse-graining as the source of macro-level quantities. They use different formal objects (a PID synergy bias; a projected-versus-truthful prediction gap), and none of the three cites another. The overlap is conceptual, not formal. This paper's own position is that the entropy is objective once (M, τ) are fixed, and that choosing them is a modelling decision (§X). Anyone comparing it with those two should start from that position.

## Bearing on the record

- In this record it is [LIT-082](../literature.d/LIT-082.md). Its summary's "admits general second-law theorems" should be softened to "admits a template for second laws (bounds on D_M(ρ̄‖τ)), proved under sufficient conditions (Eqs. 28–31)". The number of special cases can be stated as "about two dozen (§V, Table II)".
- It supports no THEORY document here, and none depends on it.
- **For the Anthology of the SOTA:** no ML content and no instruction for ML practice. The algebra "entropy = prior entropy − measured KL to the prior" is a quantum and statistical-mechanics restatement of cross-entropy/KL identities that ML already uses. The paper makes no connection to learning.

## Limitations

- The central second-law target, Eq. 26, is proved for no concrete system. The sufficient conditions (28, 29, 31) cover the macroscopic and few-eigenstate extremes and the ETH. The mesoscopic regime of the paper's own Fig. 4 falls between them (p. 12).
- The equilibration time T_eq is shown to exist but not estimated (Proof 5). The authors say estimating it needs more system specificity.
- The continuity bound (39) needs finitely many nonzero volumes. The general infinite-outcome case is open (Proof 12 vii).
- The classical numerics use pure phase points with projective M, so only Boltzmann terms appear and S^τ_M ≤ log V_max < S(τ). Reaching S(τ) exactly in the plots is an artefact of the per-particle N → ∞ approximation (§IX.3).
- The integrable-versus-chaotic conclusion rests on four initial conditions in one 2-D gas.
- Strongly coupled systems, driven Hamiltonians, thermodynamic cycles and fluctuation theorems are deferred (§VII.6, §VIII.6, §X).

## Open questions

- Prove Eq. 26 from first principles for a concrete non-integrable system, e.g. a bound on D_M(ρ̄‖e^{−βH}/Z) for coarse local-energy M. The authors name this as the key task (§X).
- Find bounds of type (28–29) in the intermediate, mesoscopic regime where Δ is empirically small.
- Extend the Clausius relation (33) to strong coupling and to the non-single-macrostate case beyond Eq. 34.
- Continuity without the finite-outcome restriction.
- Make precise the "M-independent" notion of a high-entropy state suggested by Fig. 6 (§IX.2).

## Corrections to the seeded skim

- The dossier's summary says the definition "admits general second-law theorems". What §VII actually proves is narrower.
  - It proves bounds on the *time-averaged* deviation Δ = D_M(ρ̄‖τ) (Eq. 25).
  - The equilibration term is bounded by Eq. 28, under nondegenerate energies and gaps, with ε = m/(4√d₂(ρ̄)), or by Eq. 29.
  - The "to τ" term is bounded only by assuming the ETH (Eq. 31).
  - For the paper's own examples: "in none of those cases was the smallness proved here analytically" (p. 12).
  - The thermodynamic consequences (Eqs. 32–33) are conditional on Eq. 26 holding. Their derivation (Proof 9) is heuristic: it treats S as a smooth function and assumes weak coupling and energy constant within shells.
- The dossier lists the special cases as eight. §V lists 24 numbered items, including Boltzmann's two H-theorems, Gibbs' and von Neumann's H-theorems, and three Clausius inequalities. Table II has about 20 rows. The entanglement-entropy case uses the *traditional* OE (τ ∝ 1) minimised over local measurements, not the new τ-dependent quantity.
- The main text says fluctuation probability "decays as Pr(δ) ∝ Δ/δ" (§VII.5). Proof 5 establishes only the Markov-inequality upper bound Pr ≤ Δ_T/δ (Eq. D1), or ≤ 2Δ/δ for T ≥ T_eq (D2). "∝" overstates it.
- New, not in the dossier: the paper reinterprets von Neumann's 1929 quantum H-theorem. It shows his entropy difference S(Uψ) − S(ψ) equals the measured relative entropy D_M(ψ‖Uψ), with Uψ a coarse, microcanonical-mixture version of the time-averaged state (§V item 21). This is its most concrete new historical result.
- New, not in the dossier: the time-averaged state ρ̄ is always a valid prior, S(ρ(t);ρ̄) = S(ρ̄) (Eq. 24). It is the tightest stationary one, S(ρ̄) ≤ S(τ) for every stationary valid τ (Proof 4).
- The dossier says publication status is unverified. That is still true on 2026-09-26 (v1 only, no journal reference, no Crossref hit).
