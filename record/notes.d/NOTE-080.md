---
number: 80
status: Read
formerly:
- NOTE-tmpx67yz
paper: LIT-086
title: 'Barandes, The Stochastic-Quantum Correspondence'
version: 2
history:
- version: 2
  date: '2026-09-25'
  note: >-
    Read in full (full text of arXiv:2302.10778v3 (the accepted Philosophy
    of Physics version, dated 30 June 2025 on p. 1, arXiv stamp 30 Jul
    2025), 38 pp. That covers §1–5 (pp. 1–32), the acknowledgments, the
    declarations and the 72-entry reference list (pp. 32–38). Nothing was
    skipped. Text was extracted with PyMuPDF from raw4/2302.10778.pdf (no
    pdftotext on this host). The extraction drops overbars and some inline
    symbols. Eqs. (12)–(15), (30)–(35), (43), (50) and (57) were re-derived
    by hand, and those checks are marked "(reader's check)". Read side by
    side with c18 (arXiv:1804.04807). Not read: v1/v2, and arXiv:2507.21192,
    which v3 says holds material removed since v1.). Upgraded from `Skimmed`
    to `Read`: the claims table, assumptions and results are new, and the
    skim is corrected where the full text disagreed.
date: '2026-09-25'
summary: >-
  Take any N×N stochastic transition matrix Γ(t←0) on a configuration
  space. Writing it entrywise as Γ_ij = |Θ_ij|² = tr(Θ†P_iΘP_j) (Eq. 15)
  is always possible, and the paper calls it the stochastic-quantum
  dictionary. Choosing Θ unitary (by Stinespring dilation to ≤N³
  configurations, §3.4) makes Γ unistochastic. The Born rule in the
  configuration basis (Eq. 23), the Schrödinger equation (Eq. 35, with H ≡
  iħ(∂U/∂t)U†) and interference (Eq. 43, the gap between Γ(t←0) and
  |U(t←t′)|²|U(t′←0)|²) then follow by definition or short algebra. The
  Born rule for non-diagonal observables (Eq. 78) is derived by reading a
  measuring device's configuration, given a composite unitary that
  produces Eq. (73).
---

<!-- inactive-ok-file: LIT-001 — Rejected; named in Connections as the Nelson-line paper this one disowns -->

# NOTE-080: Barandes, The Stochastic-Quantum Correspondence

## Contribution

The paper names and formalizes an *indivisible stochastic process*. It is a configuration space C = {1,…,N} plus transition matrices Γ(t←t0) that are specified only from a set of conditioning times, with no divisibility (Eq. 6) assumed and all higher-order conditionals left unspecified (§2). It then shows that the Hilbert-space formalism can be written *on top of* such a process as a representation. That rests on the entrywise factorization Γ_ij = |Θ_ij|² (Eq. 12), recast as the trace formula (15) with configuration projectors. The route runs Kraus decomposition (§3.3), then unitary dilation (§3.4), then the Schrödinger/von Neumann/Ehrenfest equations as definitions of H (Eqs. 33–36). The new material is the conceptual package. Interference is recast as non-divisibility (§3.5). "Division events" come from environmental correlation, and Markov chains follow as their coarse-grained limit (§3.7). Decoherence is a division event seen in the Hilbert picture (§3.8). A measurement model reads non-diagonal observables ("emergeables") off device configurations and yields the textbook Born rule and collapse-as-conditioning (§4). The reverse direction, quantum → stochastic via Γ = |U|² in a chosen basis, is credited in part to Korzekwa & Lostaglio 2021 (p. 12).

## Key insight

Γ_ij(t←0) = |Θ_ij(t←0)|² is an identity, and Θ is non-unique. So any time-dependent stochastic matrix can be given a Hilbert-space "potential". When that potential is chosen unitary, the unitary composes over intermediate times (Eq. 40) but its modulus-square does not (Eq. 43). "Interference" is precisely the cross-term Σ_{k≠l} U_ik Ψ_k conj(U_il Ψ_l) that separates the actual first-order transition probabilities from a pretend Markov factorization. On this reading, superposition and coherence mean only that the system is being examined *between* conditioning times. A division event, meaning perfect correlation with an environment that afterwards evolves separately (Eqs. 45–46), restores divisibility and makes the density matrix diagonal.

## Assumptions

- **Kinematics.** A finite configuration space C = {1,…,N}. The system is always in exactly one configuration (p. 9). Footnote 3 asserts, without derivation, that everything extends to continuous C.
- **Dynamics.** Only first-order conditionals Γ_ij(t←t0) = p(i,t|j,t0) are laws. They are non-negative, columns sum to 1 (Eqs. 2–3), and Γ(t0←t0) = 1 (continuity, p. 4). Higher-order conditionals, and hence trajectory probabilities, are "left unspecified" and may vary run to run (p. 6). The paper asserts that first-order conditionals suffice for "all the empirical predictions of quantum theory" (p. 6). §4 supports this only for the measurement scheme it models.
- **Conditioning at a configuration.** The Hilbert-space objects are built from a diagonal initial distribution. ρ(0) = diag(p_j(0)) (Eq. 17), and Ψ(t) = Θ(t←0)e_j exists only for a pure *configuration* at 0 (Eq. 20). Coherent initial states arise only as states at later times.
- **Choice of representation.** Θ is restricted to complex entries (p. 7). Real, quaternionic or other algebras are named as equally available. Unitarity (Eq. 28) is adopted "without any real loss of generality" after dilation, with the dilated space ≤ N³ and ancilla N′ ≤ N² (p. 10).
- **Differentiability.** U(t←0) is differentiable in t, so H(t) ≡ iħ(∂U/∂t)U† is defined (Eq. 33).
- **Division-event idealization (§3.7).** A composite SE is unistochastic (Eq. 44). At t′ the joint distribution is perfectly correlated, p^{SE}_{i′e′}(t′) = p^S_{i′}(t′)δ_{e′e(i′)} (Eq. 45), with the e(i) distinct. Afterwards the relative unitary factorizes, U^{SE}(t←t′) = U^S ⊗ U^E (Eq. 46). The same is assumed for SDE in §4, via Eqs. (73)–(74).
- **Markov limit.** Division events recur at a fixed interval δt, and U^S is time-homogeneous (p. 19).
- **Measurement.** The composite SDE is unistochastic (Eq. 72), and some U^{SDE} produces the correlated wave function of Eq. (73). Footnote 21 gives one. The Born rule for the device is derived only "as long as there exists" such an evolution (p. 25).

## Key results

- **Dictionary (Eq. 15).** Γ_ij(t←0) = tr(Θ†(t←0) P_i Θ(t←0) P_j), with Σ_i |Θ_ij|² = 1 (Eq. 13). This is an identity: Θ_ij = √Γ_ij always works (reader's check).
- **Hilbert-space recasting (§3.2).** p_i(t) = tr(P_i ρ(t)) with ρ(t) = Θ diag(p_j(0)) Θ† (Eqs. 16–17). ⟨A⟩ = tr(Aρ) for diagonal A (Eq. 18). For a configuration start, p_i(t) = |Ψ_i(t)|² (Eq. 23), where Ψ is the j-th column of Θ.
- **Kraus form (Eqs. 25–27).** K_β = ΘP_β satisfies Σ_β K_β†K_β = 1, and Γ_ij = Σ_β |K_β,ij|².
- **Unistochastic form (Eqs. 30–32).** Γ_ij = |U_ij|². Such Γ is doubly stochastic. Permutation matrices are the deterministic special case. Footnote 11: |(Σ^{t/δt})_ij|² interpolates a discrete permutation dynamics smoothly.
- **"Schrödinger equation" (Eqs. 33–36).** With H ≡ iħ(∂U/∂t)U†: iħ∂ρ/∂t = [H,ρ], iħ∂Ψ/∂t = HΨ, and the Ehrenfest equation. Reader's check: Eq. (35) is Eq. (33) applied to Ψ = Ue_j. It has no content beyond the choice of U, and H is whatever that U makes it.
- **Non-divisibility (Eqs. 37–38).** Γ(t←0)Γ^{-1}(t′←0) is generically not stochastic, because a stochastic matrix has a stochastic inverse only if it is a permutation matrix (standard result, cited as elementary).
- **Interference (Eq. 43).** Γ_ij(t←0) − [|U(t←t′)|²|U(t′←0)|²]_ij = Σ_{k≠l} U_ik(t←t′)Ψ_k(t′) conj(U_il(t←t′)Ψ_l(t′)). The reader's check confirms the algebra.
- **Division event ⇒ divisibility (Eqs. 50–56).** Under Eqs. (45)–(46): p^S_i(t) = Σ_{i′} |U^S_{ii′}(t←t′)|² p^S_{i′}(t′). So Γ^S(t←0) = Γ^S(t←t′)Γ^S(t′←0). The cross terms vanish because Σ_e U^E_{e e(i1)} conj(U^E_{e e(i2)}) = δ_{i1 i2} needs e(i1) ≠ e(i2) whenever i1 ≠ i2 (reader's check).
- **Markov chain (Eqs. 57–58).** Regular division events plus homogeneity give Γ^S(nδt←0) = (Γ^S)^n, with Γ^S_ij = |U^S_ij(δt←0)|².
- **Decoherence (Eqs. 59–62).** After a division event, ρ^S(t′) = diag(p^S_{i′}(t′)). Without one, ρ^S(t′) = U diag(p(0)) U†.
- **Entanglement (Eqs. 63–66).** An interaction is defined as the failure of Γ^{AB}(t←0) to tensor-factorize. A later division event restores factorization of the *relative* matrix. Locality and causation are "treated in detail in future work" (p. 22).
- **Measurement (Eqs. 72–78).** Given Eq. (73), p^D_{d(α)}(t′) = |Ψ̃^S_α(t′)|² (Eq. 78), the textbook Born rule for any self-adjoint Ã^S. The subject system has *no* division event at t′ if Ã^S is non-diagonal (p. 25).
- **Collapse as conditioning (Eqs. 89–94).** Γ^{SD}_{i,d(α)}(t←t′) = tr(U^{S†}P^S_i U^S P̃^S_α). The conditional state is U(t←t′)ẽ_α (Eq. 94), and the unconditioned ρ^S is their mixture (Eq. 93).
- **Uncertainty (Eq. 95).** The Robertson inequality follows "from any of the standard proofs" once the Born rule and collapse are in hand.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Every stochastic matrix can be written Γ_ij = |Θ_ij|² = tr(Θ†P_iΘP_j) | strong | Identity, Eqs. (12)–(15). Trivially true (entrywise square root) |
| C2 | Eq. (15) "is a new result" (p. 7) | weak | Assertion. The trace form is a one-line rewriting of (12), and footnote 7 itself notes similar formulas in Auffèves & Grangier 2017 |
| C3 | Unitary Θ is available "without any real loss of generality", and this "establishes the inevitability of unitary time evolution in quantum theory" (p. 10) | weak | Informal argument by citation of Stinespring dilation. The dilation is not constructed, and the ancilla "need not be regarded as physical". The headline "inevitability" is stronger than a representability claim supports |
| C4 | The Schrödinger, von Neumann and Ehrenfest equations "emerge" from a stochastic model, "a surprising new result" (p. 13) | weak | Eq. (35) follows from the *definition* (33) of H. There is no dynamical content (reader's check) |
| C5 | Interference is the discrepancy between indivisible dynamics and a would-be Markov division (Eq. 43) | moderate | The algebra is correct (reader's check). The decomposition is representation-relative: the "divisible part" |U(t←t′)|²|U(t′←0)|² changes under footnote 6's phase freedom, and an ontology other than C can be divisible (see Connections) |
| C6 | The example 2×2 matrices of Eq. (7) are "provably indivisible" | moderate | Asserted. Reader's check for f = e^{−t²/τ²}: the would-be divisor has eigenvalue (2f(t)−1)/(2f(t′)−1), which exceeds 1 in modulus as f(t′) → ½, so it is not stochastic for some (t, t′) |
| C7 | A perfectly correlating environment makes t′ a conditioning time (a "division event"), and regular division events yield a Markov chain | strong (given Eqs. 45–46) | Derivation, Eqs. (48)–(58). The idealized correlation and later factorization are assumed. Footnote 18 asserts that the approximate case follows "for precisely the same reasons" as decoherence |
| C8 | This "provides a theoretical explanation for the ubiquity of Markovian stochastic dynamics" (p. 19) | weak | Only the ideal case (C7) is shown. No approximation bound or real-system example is given |
| C9 | Non-diagonal self-adjoint matrices are genuine observables obeying the Born rule "without the need to introduce any new fundamental axioms" (p. 22) | moderate | Derivation, Eqs. (73)–(78), *given* that a unistochastic U^{SDE} produces Eq. (73). The Born rule used is the configuration-basis one of Eq. (23), which holds by definition |
| C10 | Collapse is conditioning on the device configuration | moderate | Derivation, Eqs. (86)–(94), under the same assumptions as C9 |
| C11 | The picture "arguably has the resources to solve the measurement problem" (p. 27) | weak | Informal argument. Hedged by the paper itself |
| C12 | Every quantum system can be understood as an indivisible stochastic process (abstract, §5.1) | moderate | For a finite system with a *chosen* configuration basis, Γ = |U|² gives a stochastic matrix (standard; Korzekwa–Lostaglio cited). The paper does not say which basis is physical for a general system. Continuous C is asserted (fn. 3). Multi-time statistics beyond the §4 measurement model are unaddressed |
| C13 | Entrywise phase changes of Θ are a new gauge invariance under which "all empirical results remain unchanged" (fn. 6) | weak | Assertion ("Due to space limitations, nothing more…"). Configuration-level Γ is invariant by construction. Unitarity, and the relative U(t←t′) used in §3.5–4, are not (reader's check) |
| C14 | The theory lies outside the Harrigan–Spekkens ontological-models framework, so PBR does not apply; the wave function is nomic | moderate | Argument, §5.3 and fn. 23 citing Harrigan & Spekkens 2010, §6 |
| C15 | Canonical quantization can be implemented by making deterministic dynamics stochastic (§5.1) | weak | One-sentence assertion with no construction. Footnote 11's permutation interpolation is the only related example |
| C16 | The indivisible interpretation "resolves the category problem" (§5.2) | weak | Philosophical argument |

## Method

1. Posit (C, Γ(t←t0)), with Γ stochastic, Γ(t0←t0) = 1, and no divisibility assumed.
2. Choose Θ with |Θ_ij|² = Γ_ij and complex entries. Define ρ(t) = Θ diag(p(0)) Θ†, and Ψ = Θe_j for a configuration start.
3. Rewrite Θ as Kraus operators K_β = ΘP_β, then dilate to a unitary Ũ on C × C′ with |C′| ≤ N². Work with U from then on.
4. Define H ≡ iħ(∂U/∂t)U†. The Schrödinger, von Neumann and Ehrenfest equations follow.
5. Model environment and device as further configuration spaces. Impose idealized correlation at t′ plus later factorization. Marginalize to obtain divisibility (a division event), decoherence, and device Born probabilities for arbitrary PVMs.

## Concepts

- **Indivisible stochastic process.** A configuration space plus transition maps Γ(t←t0) from a set of conditioning times to target times, with no requirement that Γ(t←t0) = Γ̃(t←t′)Γ(t′←t0) for a stochastic Γ̃ (§2.1, Eq. 6).
- **Conditioning time vs target time.** Times one may condition on, versus times at which one gets probabilities. Only the former are points of divisibility (p. 3).
- **Divisible.** In the sense of Wolf & Cirac 2008, not infinite divisibility (fn. 4). A divisible process is "generically" Markovian here (p. 4). The paper does not separate divisibility from Markovianity carefully.
- **Dictionary.** Eq. (15).
- **Unistochastic process.** An indivisible process whose Γ is |U|² for a unitary U (p. 12). Orthostochastic means U is real orthogonal. Unistochastic ⊋ orthostochastic, which is why complex numbers "generically play a necessary role" (p. 11).
- **Division event.** A time t′ at which environmental correlation (Eq. 45) plus later factorization (Eq. 46) makes Γ(t←0) divisible at t′ (p. 19). It is described as a spontaneous breaking of time-translation symmetry.
- **Beable / emergeable.** A beable is a diagonal random variable on C (after Bell). An emergeable is a non-diagonal self-adjoint matrix whose "values" appear only as device configurations (§4.1).
- **Category problem.** Textbook axioms predict only measurement-outcome probabilities, never "happening probabilities" (§5.2).
- **Indivisible interpretation / indivisible quantum theory.** Systems always occupy a configuration. Hilbert-space objects are "mathematical appurtenances" (§5.1).

## Connections

- **c18, Grangier & Auffèves, *What is quantum in quantum randomness?* ([LIT-077](../literature.d/LIT-077.md)).** This paper cites c18's source paper, Auffèves & Grangier, Sci. Rep. 7:43365 (2017) (its ref. [1]), in footnote 7, for "similar-looking formulas" in that paper's Eqs. (3)–(6). Footnote 7 spells the second author "Gragnier". It separates itself on purpose ("conceptually different purposes"), and the texts bear that out.
  - **Role of unistochasticity.** Here it is a chosen representation of a given Γ. In CSM it is the claimed output of physical postulates (i)–(iii).
  - **What the matrix relates.** Here, configurations at two times. In CSM, modalities of two contexts. The CSM-shaped object in this paper is the hybrid matrix of Eq. (89), which at t → t′ is |ẽ^S_{α,i}|²: a change-of-basis unistochastic matrix between an emergeable's eigenbasis and the configuration basis (reader's check).
  - **Complex numbers.** Here they are a convenience, with reals, quaternions or "a more general algebra" all admissible for Θ (p. 7). In c18 they are "a consequence of the quantization of exclusive modalities" (c18 p. 5, asserted and cited).
  - **Contextuality.** Both call their theory contextual. This paper does so in the Bell–Kochen–Specker sense, with beables tied to one measurement context and emergeables to others (§5.3). c18 makes contexts ontologically primitive.
  - **Continuity.** Both lean on it at different points. Here it is Γ(t0←t0) = 1 and differentiability of U. In CSM, condition (iii), "the state of the context can change continuously", is said to be what makes the matrix unistochastic.

  The seed's "same unistochastic transition matrices" is therefore true of the algebra and false of the argument. See corrections.
- **Quasi-quantization, Spekkens ([LIT-007](../literature.d/LIT-007.md); reading reads/14.md).** No citation between the two. The paper cites Harrigan & Spekkens 2010, not the epistricted programme. Two points of contact are supported by the texts.
  - **Framework.** [LIT-007](../literature.d/LIT-007.md)'s epistricted theories are ontological models whose transformations are stochastic maps on Ω, specifically symplectic affine permutations Γ_{S,a}(m|m′) = δ(m − Sm′ − a), which compose sequentially. §5.3 places indivisible quantum theory *outside* that framework because it is non-Markovian. The two are the divisible and indivisible answers to "what classical stochastic structure underlies (part of) quantum theory?".
  - **Interference relative to an ontology.** Per the reading of [LIT-007](../literature.d/LIT-007.md), the odd-d quadrature epistricted theory is operationally identical to the odd-d stabilizer subtheory, with d² ontic states per qudit and divisible (deterministic) ontic dynamics. Take a stabilizer circuit with a Fourier gate applied twice in the computational basis. By Eq. (43) of this paper, measured on the N = d computational configurations, it shows "interference", yet it has a divisible model on a larger ontic space (reader's inference joining the two texts). So "interference is a direct consequence of the stochastic dynamics not generally being divisible" (p. 14) holds *relative to the chosen configuration space*. It is not a theorem that interference needs indivisible dynamics on any ontology. For d = 2 and in general, [LIT-007](../literature.d/LIT-007.md) locates the unavoidable residue in contextuality and Bell violations, which this paper leaves to future work.
- **Lindgren & Liukkonen, *Quantum Mechanics can be understood through stochastic optimization on spacetimes* ([LIT-001](../literature.d/LIT-001.md), Rejected; reading reads/35.md).** No citation. Both reach a Schrödinger equation from a stochastic starting point, and they fail in instructive opposite ways.
  - **[LIT-001](../literature.d/LIT-001.md)** is in the Nelson/stochastic-mechanics line. Per its reading, it needs a complex noise variance σ² = i/m and an i-valued volume factor, which "leaves no real stochastic process" behind.
  - **This paper** says explicitly that it "is not continuous with" the Bopp–Fényes–Nelson approaches (p. 2). Its Γ stays a real stochastic matrix throughout, and i enters only in the chosen representation Θ and in the definition (33) of H.

  The price is the reverse of [LIT-001](../literature.d/LIT-001.md)'s. The stochastic process is kept, but the Schrödinger equation carries no dynamical content of its own (C4). Neither paper explains where a *particular* H comes from.
- **Other lineage named by the paper:**
  - Divisibility: Wolf & Cirac 2008. Quantum non-Markovianity: Milz & Modi 2021.
  - The reverse direction: Korzekwa & Lostaglio 2021.
  - Classical-to-classical channels as a proper subclass: Wilde 2017, fn. 12.
  - Latent measurement: Dicke 1989, Glick & Adami 2020.
  - Contrasts: Bohmian mechanics, Everett, GRW/CSL, modal interpretations (§5.3), and Bedingham 2018 as a nomic-wave-function collapse model.

## Bearing on the record

- The nucleation record has no THEORY documents yet (theory.d holds only the README stub). This reading would support one: the claim that a quantum Hilbert-space model is a non-unique representation of first-order transition probabilities on a chosen configuration space. It should be filed with C1, C5 and C9 as its support and C3, C4 and C13 as its caveats. A THEORY that cites this paper for "quantum dynamics derived from stochastic processes" would be citing C4, which is definitional.
- [LIT-086](../literature.d/LIT-086.md)'s summary ("every quantum system can be represented…, and the reverse also holds") is fair as a description of the paper's claims. It should add that the quantum→stochastic direction needs a chosen configuration basis, and that the unitary representation on the original space exists only for doubly stochastic Γ (Eq. 32).
- **ML practice: nothing for the Anthology of the SOTA.** The paper gives no estimator, parameterization, algorithm or experiment for non-Markovian time-series modelling. The one practical constraint it does surface cuts against casual reuse. A unitary Θ on the original state space forces Γ to be doubly stochastic, which excludes, e.g., absorbing states. So general Γ needs a dilated state space of up to N³ configurations. The dossier's "touches sequence and time-series modelling" should not travel into the anthology.

## Limitations

- Most "new result" labels mark definitions or identities (C2, C4). The substantive content is the division-event and measurement analysis of §3.7–4, and there only under idealized perfect correlation and factorization.
- The dilation (§3.4) is cited, not constructed. "At least some choices of the ancilla's configuration j′" leaves open how the ancilla's initial configuration is to be understood physically.
- Which basis counts as the configuration basis is never fixed for a given quantum system. The quantum→stochastic direction is only as physical as that choice.
- Higher-order conditionals and trajectory probabilities are left unspecified (p. 6). No principle picks them, so the "physical trajectory" in C (p. 2) has no probability law beyond two-time marginals.
- Continuous configuration spaces (fn. 3), locality and causation (§3.9, §5.4), and the gauge freedom (fn. 6) are all deferred. Bell-type questions are not addressed in this version at all.
- There is no worked quantum example beyond 2×2 matrices and footnote examples. No numerical check is given.

## Open questions

- Does the footnote-6 phase freedom leave any empirical prediction invariant beyond configuration-level Γ of the whole composite? That needs an explicit treatment of how subsystem unitaries and emergeables transform.
- Is there a principled choice of configuration basis (a "beable" basis) for a given Hamiltonian system? Without one, C12 is a representation theorem, not an ontology.
- What fixes the higher-order conditionals, if anything, and are they ever empirically accessible? §4's device-mediated multi-time statistics suggest not, but the paper does not prove it.
- Can the ideal division event of Eqs. (45)–(46) be made quantitative, bounding the deviation from Markovianity for approximate correlation? Footnote 18 only asserts it.
- The locality/causation analysis is deferred to later work (per the v3 note, arXiv:2507.21192, unread here). It would be needed before any claim about Bell nonlocality can be attributed to this programme.

## Corrections to the seeded skim

- **Seed (joint with c18): "both reach the Born rule through the same unistochastic transition matrices."** The mathematical object is the same, a matrix of |U_ij|² for a unitary U. Its role and its physical reading are opposite in the two papers. Here, unistochasticity is *assumed*: a representational choice justified by a dilation argument ("without any real loss of generality", p. 11). The configuration-basis Born rule p_i = |Ψ_i|² is then *definitional*, because Ψ is defined as a column of Θ (Eqs. 20–23). In c18, unistochasticity is claimed as a *conclusion* of physical postulates plus continuity, and c18 cites the proof without giving it. Here, Γ is a transition matrix between configurations at two *times*. In c18, the matrix relates the modalities of two *contexts*, i.e. two measurement bases. The object closest to c18's matrix is this paper's hybrid device-to-subject matrix, Eq. (89), which at t → t′ reduces to |ẽ^S_{α,i}|², a change-of-basis unistochastic matrix (reader's check). The paper flags the kinship itself: footnote 7 (p. 7) says "similar-looking formulas" appear in Eqs. (3)–(6) of Auffèves & Grangier 2017 (its ref. [1]; c18's ref. [14]) "as an intermediate step in proving a lemma" used "for conceptually different purposes".
- The dossier says the dictionary "yields the Hilbert-space representation (§3.2)". It does yield it, but with no constraint on Θ beyond the column-sum condition (13). Unitarity enters only in §3.4, and not every stochastic matrix is unistochastic (unistochastic ⇒ doubly stochastic, Eq. 32). The Hilbert-space representation on the *original* N configurations is therefore unitary only for doubly stochastic Γ. The general case needs the dilated space. The dossier does not mention this restriction.
- The dossier asked whether anything besides stipulation selects unitary Θ. The full text answers: nothing but the dilation argument and convenience. The dilation is asserted from the Stinespring theorem (p. 10), with "at least some choices" of the ancilla's initial configuration, and not worked out. Footnote 6's claimed "gauge invariance", entrywise phases Θ_ij ↦ e^{iθ_ij(t)}Θ_ij (the i is missing in the extracted text), does not preserve unitarity in general. Reader's check: multiplying one entry of the 2×2 Hadamard by e^{iφ} makes its columns non-orthogonal unless φ = 0. So the choice of a unitary representative is itself not gauge-invariant.
- The dossier calls §5.1 a proposal that canonical quantization is the move from deterministic to stochastic dynamics. That is accurate, but it is one sentence with "(when mathematically feasible)" and no construction (p. 29).
- The dossier says §5.4 "touches sequence and time-series modelling". That is the dossier's own extrapolation. The paper names biology and finance (p. 32) and turbulence and finance (p. 2), and gives no method, algorithm or worked example beyond the 2×2 matrices of Eq. (7).
- Minor: the v3 PDF is dated 30 June 2025 on p. 1, while the arXiv stamp reads 30 Jul 2025. The footnote says material "removed since Version 1" went into arXiv:2507.21192, which matches the dossier.
