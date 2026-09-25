---
number: 11
status: Read
formerly:
- NOTE-tmpdpxch
paper: LIT-010
title: 'Quantum Thermodynamics'
version: 2
history:
- version: 2
  date: '2026-09-25'
  note: >-
    Read in full (full text of arXiv:1508.06099v2 (10 May 2016), 48 PDF pp.,
    extracted with PyMuPDF into raw4/1508.06099.txt (no pdftotext on this
    host). Read line by line: §1 Introduction, §2.1–2.6, §3.1–3.7, §4.1–4.3
    (including the three CPTP theorems, the entropy inequalities,
    majorisation and smooth entropies), §5.1–5.4, §6.1–6.9, §7, and the
    acknowledgements. Figures 1–12 came through only as captions and stray
    axis labels; I read the captions and the prose describing them, not the
    plots. The reference list ([1]–[220], pp. 40–48) I checked for
    structure, and I looked up the entries the text leans on: [3]–[8], [41],
    [61], [111], [142], [146], [148], [149], [159], [168], [171], [172],
    [175], [179], [206]. I did not read every entry.). Upgraded from
    `Skimmed` to `Read`: the claims table, assumptions and results are new,
    and the skim is corrected where the full text disagreed.
date: '2026-09-25'
summary: >-
  A 2015–16 review with no new results, whose one synthesis (§5.2, §7) is
  that the field used four inequivalent notions of work: ensemble ⟨W⟩ =
  ∫tr[ρḢ]dt (Eq. 2), two-point-measurement W = E_m^(τ) − E_n^(0) (Eq. 24),
  ε-deterministic single-shot A^ε ≈ −kT ln(Z_Λ*/Z) (Eq. 49) and
  resource-theory w^max_ε = F^min_ε(ρ_S) − F(τ_S) (Eq. 50), of which only
  the last two coincide. It also judges that the field had "only made a
  small number of experimentally checkable predictions of new
  thermodynamic effects yet" (§7, p. 39).
---

# NOTE-011: Quantum Thermodynamics

## Contribution

The review adds no new results. It assembles, in one 40-page overview, the separate strands of quantum thermodynamics as of 2015–16:
- the information–thermodynamics link: Maxwell's demon, Landauer, erasure with quantum side information, work from correlations and from coherences;
- classical and quantum fluctuation relations and their experiments;
- CPTP-map tools: Stinespring, Choi–Jamiołkowski, Kraus, relative-entropy contractivity, majorisation, smooth entropies;
- thermalisation of closed systems: typicality and ETH;
- single-shot and resource-theory second laws;
- quantum thermal machines.

Its one synthesising observation is that these strands define "work" in at least four ways, and that only the two single-shot optima agree (§5.2, §7).

## Key insight

"Work" in the quantum regime is not one quantity. The ensemble average (Eq. 2), the two-point-measurement fluctuating work (Eq. 24), the ε-deterministic single-shot work (Eq. 49) and the resource-theory lift of a work bit (Eq. 50) answer different operational questions. The authors compare them to different entanglement measures, each suited to a different task (§7, p. 39). Whichever one a quantum-thermodynamic claim rests on has to be named before the claim can be assessed.

## Assumptions

- **Von Neumann entropy stands in for thermodynamic entropy out of equilibrium** (§2.1, p. 5). The authors call this assumed and "debated".
- **Clausius' inequality ⟨Q⟩ ≤ TΔS_th is "generally assumed to extend to the quantum regime"** (§2.1, Eq. 5).
- **Fluctuation relations (§3.2, §3.6):**
  - the system starts in a thermal state at inverse temperature β for the initial Hamiltonian;
  - its evolution is closed (unitary V) between two projective energy measurements;
  - the Crooks relation requires detailed balance with the bath (§3.2).
- **Master equations (§4.1):** Lindblad form, which assumes weak coupling, fast-decaying bath correlations and an initial system–bath product state.
- **Single-shot and resource theory (§5):**
  - system states diagonal in the energy eigenbasis, except §5.4;
  - thermal baths are free;
  - the global unitary commutes with H_S + H_B + H_W (perfect energy conservation);
  - the catalyst is returned exactly and uncorrelated (Eq. 52), since approximate return permits "thermal embezzling".
- **Engines (§6):**
  - two thermal baths at fixed temperatures;
  - Carnot/Curzon–Ahlborn bounds are expected to hold (§6.5);
  - the "beyond Carnot" results need non-thermal (squeezed) baths, whose preparation cost is not counted (§6.3, p. 32).

## Key results

The derivations of fluctuation relations are reproduced in full. Everything else is reported from the cited literature.

- **First law and definitions** (Eqs. 1–3): ⟨Q⟩ = ∫₀^τ tr[ρ̇ H] dt, ⟨W⟩ = ∫₀^τ tr[ρ Ḣ] dt, and ⟨Q⟩ + ⟨W⟩ = ΔU.
- **Second law** as extractable work: ⟨W_ext⟩ ≤ −ΔF with F = U − TS_th (Eqs. 6–7).
- **Landauer** (§2.3): ⟨Q_dis^min⟩ = k_B T ln 2 per bit (Eq. 10), and k_B T S(ρ) for a mixed state, "following from the second law".
- **Erasure with quantum side information** (Eq. 11, [8]): ⟨W_ext^max⟩ = −k_B T S(S|M), which is positive when the conditional entropy is negative. That requires an entangled system–memory state.
- **Work from coherences** (Eq. 12, [61]): ⟨W_ext^max⟩ = k_B T (S(η) − S(ρ)) ≥ 0 for the dephasing η = Σ_k Π_k ρ Π_k in the energy eigenbasis.
- **Classical Jarzynski and Crooks** (Eqs. 18–21): P^F(W) = P^B(−W) e^{β(W−ΔF)} and ⟨e^{−βW}⟩ = e^{−βΔF}. The closed-system proof is given in Eq. 20 via Liouville (|dx₀/dx_τ| = 1). Jensen then gives ⟨W⟩ ≥ ΔF.
- **Sagawa–Ueda feedback** (Eq. 22): ⟨e^{−β(W−ΔF)}⟩ = γ, with γ_max = 2 for two feedback branches, recovering k_B T ln 2 (Eq. 23).
- **Quantum Jarzynski and Tasaki–Crooks** (Eqs. 24–30), with two-point-measurement work W_{m,n} = E_m^(τ) − E_n^(0):
  - the proof uses Σ_n p_{m|n} = 1 (Eq. 29);
  - the review notes these are *identical in form* to the classical relations;
  - it notes the energy measurements destroy coherences, which is why the definition is contested (§3.6, [61]).
- **Entropy-production bound for CPTP maps with fixed point ρ⋆** (Eq. 44): S[Φρ] − S[ρ] ≥ −tr[Φ(ρ) ln ρ⋆ − ρ ln ρ⋆]. The additive version for concatenated maps is Eq. 45.
- **ε-deterministic single-shot work** (Eq. 49, [142]): A^ε ≈ −kT ln(Z_Λ*/Z), with Λ* the smallest energy subspace carrying probability > 1 − ε. The worked example (p. 25) uses ε = 1/10 and populations (5,4,1,2,3,0)/15, giving p = 14/15 on {0,1,3,4}E.
- **Resource-theory extractable work** (Eq. 50, [111, 149]): w^max_ε = F^min_ε(ρ_S) − F(τ_S). The work of formation (Eq. 51) is generally different.
- **Single-shot second laws** (Eq. 53, [146]): for energy-diagonal states and catalytic thermal operations, ρ_S → ρ'_S is possible iff F_α(ρ_S, τ_S) ≥ F_α(ρ'_S, τ_S) for all α ≥ 0, with F_α = kT(S_α(ρ‖τ) − ln Z). The limit α → 1 recovers ΔS ≥ βΔU = β⟨Q⟩ (Eqs. 54–56).
- **Coherence constraints** (Eq. 57, [148]): A_α(ρ_S) = S_α(ρ_S ‖ D_H(ρ_S)) must not increase. These are necessary only; sufficiency is unknown.
- **Engines:**
  - Carnot η = 1 − T_C/T_H (Eq. 61) and Curzon–Ahlborn η_CA = 1 − √(T_C/T_H) (Eq. 59);
  - Otto efficiency (Eq. 62);
  - particle-in-a-box Diesel η = 1 − ⅓(r_E² + r_E r_C + r_C²) (Eq. 65);
  - ergotropy ⟨W_ext^max⟩ = tr[H(ρ − π)] with π passive (Eq. 69);
  - steady-state Otto efficiency (Eq. 70, [168, 206]);
  - Carnot COP = T_C/(T_H − T_C) (Eq. 67).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Average heat and work are process-dependent and are not observables | moderate | §2.1, Eq. 3; cites [41] (Talkner–Lutz–Hänggi) |
| C2 | For a closed system starting thermal, ⟨e^{−βW}⟩ = e^{−βΔF}, classically and in the two-point-measurement quantum setting | strong | derivations reproduced in Eqs. 20 and 29 |
| C3 | Quantum Jarzynski/Tasaki–Crooks "show no difference to their classical counterparts" | strong (formal) | Eqs. 29–30 vs 19, 18; but the two-point scheme erases energy coherences (§3.6), so the equivalence depends on that choice |
| C4 | Erasure with quantum side information can yield work −kT S(S|M) > 0 | moderate | reported from [8]; no derivation here |
| C5 | Coherences in the energy basis are a work resource: kT(S(η) − S(ρ)) extractable | moderate | reported from [61] (Kammerlander & Anders, Anders being a coauthor of the review) |
| C6 | Single-shot ε-deterministic work (Eq. 49) and resource-theory work (Eq. 50) coincide | weak–moderate | observation that Z_Λ*/Z equals the Eq. 50 sum (p. 26); Eq. 49 is itself "≈"; the §7 statement points to Eq. 48, the wrong equation |
| C7 | For energy-diagonal states, the α-free energies give necessary and sufficient conditions under catalytic thermal operations; α → 1 recovers the standard second law | strong (as report) | reported from [146]; the α → 1 reduction is worked in Eqs. 54–56 |
| C8 | Coherent states face a second, independent family of monotones (A_α) | moderate | reported from [148]; necessary conditions only |
| C9 | Carnot efficiency can be exceeded with squeezed baths, but a "generalised" Carnot bound is not | weak | reported from [171, 172]; the bath-squeezing cost is uncounted (p. 32) |
| C10 | Photo-Carnot efficiency with atomic coherence is η = η_Carnot − π cos Φ | weak | Eq. 68 as printed; cannot be literally correct |
| C11 | Quantum thermodynamics had made few experimentally checkable predictions of new effects | weak | assertion in §7; no survey of experiments backs it beyond §3.4, §3.7 |
| C12 | The ensemble, fluctuating, single-shot and resource-theory notions of work are not unified | moderate | §7 side-by-side comparison; an informed judgement rather than a theorem |

## Concepts

- **Average heat / work** — Eq. 2: ⟨Q⟩ = ∫ tr[ρ̇H]dt, ⟨W⟩ = ∫ tr[ρḢ]dt. Work is the energy change due to the controlled change of H; heat is the rest.
- **Two-point-measurement (TPM) work** — the difference of projective energy measurements at the start and end of a closed unitary process (Eq. 24). It is a random variable with distribution Eq. 25.
- **Single-shot regime** — acting on one (possibly correlated) system rather than i.i.d. copies (§5).
- **ε-deterministic work content** — the ordered energy extractable with failure probability ≤ ε (Eq. 49).
- **Thermal operation** — a global energy-conserving unitary on system ⊗ Gibbs bath (⊗ work storage), followed by tracing out the bath (§5.2).
- **Catalytic thermal operation** — the same with a catalyst returned exactly and uncorrelated (Eq. 52).
- **Thermo-majorisation / β-ordering** — the ordering by e^{βE_k} p(E_k, g_k) that decides convertibility (§4.1).
- **Passive state / ergotropy** — a state with eigenvalues ordered inversely to energies, from which no unitary extracts work. Ergotropy tr[H(ρ − π)] is the maximum unitary work (Eq. 69).
- **Kinematic vs dynamical thermalisation** — typicality of reduced states of random pure states (the "general canonical principle", [7]) vs ETH, i.e. diagonal matrix elements of observables smooth in energy (§4.3, §7).

## Connections

The review is organised around the works it summarises:
- **Fluctuation relations:** Jarzynski [3], Crooks [4], Tasaki [5], Sagawa–Ueda [6].
- **Canonical typicality:** Popescu–Short–Winter [7].
- **Side-information erasure:** del Rio et al. [8].
- **Resource theory:** Brandão et al. [9, 146], Horodecki–Oppenheim [111], Åberg [142], Lostaglio–Jennings–Rudolph [148].
- **Engines:** Geva–Kosloff [159], Quan [175], Scully et al. [179], Abah–Lutz and Roßnagel et al. [168, 171, 172].

Two of the results it treats at most length, work from coherences [61] and single-shot → general work extraction [149], are by the second author. The smooth min/max entropies (Eqs. 41–42) use the unsquared fidelity F(x,y) = ‖√x√y‖₁ with S_max = sup ln F². That is the fidelity convention whose operational derivation is [LIT-018](../literature.d/LIT-018.md) (Fuchs' thesis). Within this record it sits alongside [LIT-011](../literature.d/LIT-011.md) and [LIT-017](../literature.d/LIT-017.md) in the owner's "quantum" cluster, with no technical overlap with either.

## Bearing on the record

No THEORY document in this record is supported or contradicted by the review. It can stand as the record's general pointer into quantum thermodynamics, with the caveats under corrections.

It carries no instruction for machine-learning practice, and nothing in it belongs in the Anthology of the SOTA. The indirect connection the dossier mentions is real but lies entirely outside the text: Jarzynski's equality is the identity behind annealed importance sampling, and Landauer bounds underlie thermodynamic views of computation. The review makes neither link. A grep of the anthology's record found no document on Jarzynski, Crooks, Landauer or annealed importance sampling that it could bear on.

## Limitations

- **A snapshot of 2015–16.** The authors call the field "rapidly evolving". Nothing after early 2016 is covered, and the open problems in §7 may have moved since. That was not checked here.
- **A review of results, not their proofs.** Only the fluctuation relations (Eqs. 16, 20, 26–29) and the α → 1 reduction (Eqs. 54–56) are derived in the text. Everything else is reported, so the review's support for any single result is the cited paper's, not its own.
- **Formula-level errors as printed:** Eq. 68; the Kraus-operator statement (p. 19); the Diesel stroke lengths (p. 33); the §7 pointer to Eq. 48 instead of Eq. 49.
  - Eq. 41 defines S_min with 2^{−λ} while Eq. 42 uses ln, a notational mismatch between log bases.
  - Anyone quoting a formula should take it from the primary source.
- **Uneven coverage.** §6 explains engine designs through selected examples (spin Carnot, harmonic Otto, particle-in-a-box Diesel, three-level and qubit–qutrit refrigerators). It is not a systematic account of bounds.
  - The claim that non-thermal baths beat Carnot rests on [171, 172] with the bath-preparation cost excluded, as the review itself notes (p. 32).
- **Undefined cross-reference:** §4.3 refers to trace distance "see section 4", but §4 does not define it.

## Open questions

These are as the review states them in §7, with what would close each.

- **Unifying work.** Wanted: an operational link between ensemble work (Eq. 2) and single-shot work, beyond taking limits of Rényi entropies. Closed by a measurement scheme showing how and when the two converge experimentally.
- **Kinematic vs dynamical thermalisation.** A result deriving typicality-type closeness to the Gibbs state from Hamiltonian eigenstate properties (ETH), or the converse. It should also cover pre-thermalisation and "rare states".
- **Statistics and engine performance.** Thermal machines with baths non-thermal in ways other than unitary transformations of thermal states, where entanglement and correlations would matter.
- **Coherent-state convertibility.** Whether the necessary conditions in Eq. 57 are also sufficient for thermal operations on states with energy coherences (§5.4).

## Corrections to the seeded skim

- **The optima that coincide are Eq. 49 and Eq. 50, not Eq. 48 and Eq. 50.** The dossier repeats §7's own cross-reference: "single-shot Eq. 48 … resource theory Eq. 50 … coincide". Eq. 48 is the *random* single-shot work yield kT ln(r_n/t_n), which depends on which level the system happens to start in. The quantity shown to coincide with the resource-theory work (Eq. 50) is the ε-deterministic work content A^ε(ρ,H) of Eq. 49. That quantity is itself stated with "≈", not "=".
  - The coincidence is shown in §5.2 (p. 26) by observing that Z_Λ*/Z equals the sum in Eq. 50. It is an identification of two published formulas ([142] Åberg; [111] Horodecki–Oppenheim; [149] Gemmer–Anders), not a derivation.
  - §7's pointer to Eq. 48 is the paper's own slip.
- **The single-shot and resource-theory notions are restricted to states diagonal in the energy basis** (Eqs. 48–50, 53: "diagonal distribution ρ", "diagonal non-equilibrium state ρ_S"). For states with coherence, §5.4 gives only *necessary* conditions (Eq. 57: A_α must decrease). It says explicitly that sufficiency is unknown. The dossier's summary does not mention this restriction.
- **The review makes a stated modelling assumption that the dossier omits.** §2.1 (p. 5) says: "For the remainder of this article we will assume that the von Neumann entropy S is the natural extension of the thermodynamic entropy S_th". It flags this as debated ([44, 45]). Everything downstream uses S in place of S_th out of equilibrium: Landauer for mixed states, work from coherences, engine efficiencies.
- **Equations that cannot be right as printed**, which a skim would not catch:
  - Eq. 68 gives the Scully et al. photo-Carnot efficiency as η = η_Carnot − π cos(Φ). A correction term of magnitude up to π would allow η > 1 or η < 0, so this cannot be literally correct. I did not check it against [179].
  - The operator-sum paragraph (§4.1, p. 19) says a map Σ_μ K_μ ρ K_μ† "with Σ K_μ†K_μ = I is completely positive (but not necessarily trace preserving)". With that normalisation the map *is* trace preserving; the qualifier belongs to Σ K†K ≤ I.
  - The Diesel strokes (§6.4, p. 33) have inconsistent lengths: "from L2 to L3 > L1", then "from L3 to L1 > L3".
  - §4.3 says "close (in trace distance, see section 4)", but §4 never defines trace distance. It only mentions that contractivity "is also obeyed by trace distance".
- The dossier's other points check out:
  - Eqs. 2–3 and "process dependent … do not correspond to observables" (§2.1);
  - Jarzynski via Jensen giving ⟨W⟩ ≥ ΔF (Eqs. 19–21, §3.2);
  - the three open problems in §7: patchy work definitions, kinematic (typicality) vs dynamical (ETH) thermalisation, and statistics and non-thermal baths for machines;
  - the venue, Contemporary Physics 57(4) (arXiv DOI metadata 10.1080/00107514.2016.1201896).
