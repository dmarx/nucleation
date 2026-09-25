---
number: 17
status: Read
formerly:
- NOTE-tmphgp0u
paper: LIT-003
title: 'A structure theorem for generalized-noncontextual ontological models'
version: 2
history:
- version: 2
  date: '2026-09-25'
  note: >-
    Read in full (full text of arXiv:2005.07161v3 (8 Mar 2024, the version
    accepted by Quantum on 2024-03-06), 41 pp. I read §1–6, the reference
    list [1]–[73], and Appendices A, B (proof of Theorem 4.1), C
    (Proposition 3.2), D (Proposition 4.4) and E.1–E.4. I extracted the text
    with PyMuPDF into raw4/2005.07161.txt. The string diagrams came through
    as scattered labels; I reconstructed them from the surrounding prose and
    the equation labels, and each proof step can be followed that way. I
    checked the ontic-state-count claim separately (scratchpad/check71.py,
    checkbits.py) by computing the real dimension spanned by stabilizer
    states and by epistricted states for (d, n) = (3, 1), (5, 1), (3, 2),
    and for d = 2 with n = 1, 2. I did not compare the published Quantum
    version (DOI 10.22331/q-2024-03-14-1283).). Upgraded from `Skimmed` to
    `Read`: the claims table, assumptions and results are new, and the skim
    is corrected where the full text disagreed.
date: '2026-09-25'
summary: >-
  Take a tomographically local GPT and any convex-linear, empirically
  adequate, diagram-preserving map M from it into FVect_R. Then M(T) = χ_B
  ∘ T ∘ χ_A⁻¹ for unique invertible linear maps χ_A (Thm 4.1).
  Consequences: - Every diagram-preserving quasiprobabilistic model is an
  exact (non-overcomplete) frame representation (Prop. 4.3). - Every
  diagram-preserving noncontextual ontological model has |Λ_A| = dim(A),
  the GPT dimension (Cor. 4.2, §4.3): exactly d² ontic states for a qudit
  and 4 for a qubit. - The paper also proves (Cor. 3.5) that three things
  are equivalent in arbitrary compositional scenarios, without needing
  tomographic locality: a noncontextual ontological model of the
  operational theory; an ontological model (simplex embedding) of its GPT;
  and a positive quasiprobabilistic model of its GPT.
---

# NOTE-017: A structure theorem for generalized-noncontextual ontological models

## Contribution

The paper gives the first process-theoretic definition of ontological models, quasiprobabilistic models and generalized noncontextuality for *arbitrary compositional* scenarios; earlier work covered prepare-measure or prepare-transform-measure scenarios. On that basis it does three things:
1. It extends the equivalence between noncontextual models, simplex embeddings and positive quasiprobability representations from prepare-measure scenarios [2, 4, 5] to all scenarios.
2. It proves a rigidity theorem. For tomographically local GPTs, every diagram-preserving linear representation is a change of basis, M(T) = χ_B T χ_A⁻¹. So diagram-preserving quasiprobability representations are exactly the non-overcomplete frame representations, and diagram-preserving noncontextual models have exactly GPT-dimension many ontic states.
3. It shows by example that tomographic locality cannot be dropped.

## Key insight

Once a representation must respect composition, and in particular must send the identity channel to the identity, it cannot add any dimensions. Tomographic locality lets every process be written as a real-linear combination of "effect-then-state" channels. Diagram preservation then fixes M on those channels by its action on states (χ) and on effects (φ). Empirical adequacy makes φ a left inverse of χ, and the identity makes it a right inverse. An invertible χ_A means dim V_A = dim A. For an ontological model V_A = R^{Λ_A}, so the number of ontic states is fixed at the GPT dimension. Overcomplete frames (the Q and P functions) and excess-baggage models are thereby not diagram-preserving. A classical explanation of a tomographically local theory, if one exists, is just a choice of basis for the GPT in which everything is positive.

## Assumptions

On the operational theory (§1.2):
- **Unique deterministic effect.** All "measure and discard" effects are operationally equivalent.
- **Arbitrary mixtures.** Coin-flip mixtures of procedures are procedures (convexity).
- **Finite dimension.** The GPT is finite-dimensional. The CV Wigner function is mentioned as satisfying the definition only after an unstated generalization to infinite dimensions (footnote 12).
- **Tomographic locality**, for the structure theorem, not for Cor. 3.5: processes are fixed by local preparations and local measurements (Eq. 26 ⇔ Eq. 49). The key technical form is Lemma 2.6: 1_A = Σ_ij [N⁻¹]_j^i E_i ∘ P_j.

On the representation (§1.2, Defs. 2.9–2.11):
- **Deterministic-effect preservation.** The discard effect maps to marginalization; this is Eq. 78, Σ_λ D_λ = discard.
- **Convex-linearity**, which also preserves coarse-graining.
- **Empirical adequacy.**
- **Diagram preservation.** The representation is a strong monoidal functor. Only three instances are used for Thm 4.1: Eqs. 76 and 112–114.

Definitions:
- **Noncontextual model** (Def. 3.1). T ≃ T′ ⇒ ξ(T) = ξ(T′); equivalently, ξ factors through the quotient map ∼.
- **Ontological model of a GPT** (Def. 2.10). A diagram-preserving map into SubStoch. Noncontextuality is a category mistake for such maps, since a GPT has no contexts (App. A).

## Key results

- **Theorem 2.8.** Every tomographically local GPT has a diagram-preserving representation in FVect_R: T ↦ M_T ∘ N_{1_A}, with M_T = N_{1_B}⁻¹ ∘ N_T ∘ N_{1_A}⁻¹ (Eqs. 59–60). Attributed to Hardy's duotensor work [31]; made explicit here.
- **Proposition 3.2 and Corollary 3.5 (no tomographic locality needed).** Noncontextual ontological models of Op correspond one-to-one with ontological models of the GPT, via ξ_nc = ξ̃ ∘ ∼ and ξ̃ = ξ_nc ∘ C, where C is any section of ∼. Existence of these is equivalent to existence of a positive quasiprobabilistic model (Prop. 3.4, "immediate from the definitions").
- **Theorem 4.1 (structure theorem).** Let M: GPT → FVect_R be convex-linear, empirically adequate and diagram-preserving, with the GPT tomographically local. Then M(T) = χ_B ∘ T ∘ χ_A⁻¹ with χ_A invertible and uniquely determined. Proof in App. B, Eqs. 120–135.
- **Corollary 4.2.** dim V_A = dim A.
- **Proposition 4.3.** Diagram-preserving quasiprobabilistic models: χ_A = Σ_λ |λ⟩⟨D_λ| with Σ_λ D_λ = discard. Also {F_λ} with tr F_λ = 1 in the quantum case, and ⟨D_λ′, F_λ⟩ = δ_λλ′ (Eq. 90). So ξ̂(T)(λ′|λ) = D_λ′ ∘ T ∘ F_λ, which is an *exact* frame / dual-frame pair (§4.1.1, Eqs. 93–95). Overcomplete-frame representations are not diagram-preserving.
- **Proposition 4.4.** For ontological models, additionally, each pair (χ_A⁻¹, χ_B) is a positive map from the GPT's transformation cone into the substochastic cone (App. D). In the quantum case this demands a frame and dual frame of positive operators, which do not exist [3]: a new one-line proof that quantum theory has no noncontextual model.
- **§4.3, dimension bound.** |Λ_A| = dim(A), so Hardy's excess-baggage factor is γ_A = |Λ_A|/dim(A) = 1 (Eq. 99). Consequences stated in the paper:
  - Qubit: exactly 4 ontic states.
  - Hardy's theorem (unbounded excess baggage for a qubit) combined with this gives a new proof that no noncontextual model exists for a qubit.
  - The 8-state Wallman–Bartlett model of the qubit stabilizer subtheory is contextual.
  - The simplex-embedding algorithm of [4] reduces to a single test at the GPT's own dimension, improving Gitton–Woods' d² bound [58].
  - With [59] (quadratic ontic-state scaling for qubit stabilizer), the qubit stabilizer subtheory is contextual.
- **Proposition 4.6.** Diagram preservation forces χ_AB = χ_A ⊗ χ_B. Hence Λ_AB = Λ_A × Λ_B (ontic separability), the frame is a product basis, and PBR's preparation independence follows (Eq. 105).
- **Theorem 4.7 (categorical).** Every such M is naturally isomorphic to the canonical representation R of Thm 2.8, via a unique monoidal natural isomorphism.
- **§5.2, necessity of tomographic locality.** Take the real-amplitude qutrit stabilizer subtheory with Gross's model restricted to it. It is still noncontextual, since restricting procedures adds no operational equivalences, yet it uses 9^n ontic states, more than the GPT dimension. Conversely, if an ontological model has |Λ| = dim for every system, the GPT is tomographically local: transformations inject into d×d substochastic matrices, which have dimension d², and effect-prepare channels already span d².

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Noncontextual ontological models of Op ↔ ontological models of its GPT ↔ positive quasiprobabilistic models of its GPT, in arbitrary compositional scenarios | strong | Prop. 3.2 (sketch in the main text; completed in App. C) and Prop. 3.4 (by definition). Tomographic locality is not needed |
| C2 | Every convex-linear, empirically adequate, diagram-preserving representation of a tomographically local GPT in FVect_R is T ↦ χ_B T χ_A⁻¹, with unique invertible χ | strong | Thm 4.1, full proof App. B. Uses Lemma 2.6 (proved App. E.3) and the linear extension of a convex-linear map (App. B, footnote 14) |
| C3 | Diagram-preserving quasiprobability representations are exactly the non-overcomplete frame representations | strong | Prop. 4.3 and §4.1.1; converse in §4.5 |
| C4 | A diagram-preserving noncontextual model of a tomographically local theory has exactly dim(A) ontic states (d² for a qudit) | strong | Cor. 4.2 + Prop. 3.2. Stated as "bound" / "largest number" in the abstract but proved as equality |
| C5 | The odd-d stabilizer subtheory's noncontextual model (Gross / epistricted) meets the count exactly | strong for d = 3 (stated, p. 25); my own check for general odd d | The paper checks it for qutrits only and cites [19] for uniqueness. I verified d^{2n} = GPT dimension for (3,1), (5,1), (3,2) and by the Weyl-basis argument (corrections) |
| C6 | Tomographic locality is necessary for the dimension bound | strong (for the general converse); moderate (for the worked example) | The general argument at the end of §5.2 is sound. The example's dimension figures (45, 36, ½3^n(3^n+1)) appear to be real-quantum-theory numbers; by my count they are 21, 16 and 4 for the real stabilizer subtheory. The conclusion is unaffected |
| C7 | Diagram preservation "does not restrict the scope of applicability"; it is a prescription for how to apply the formalism | assertion | §1.2, p. 5. Defended only for three instances (§5.1); the full defence is deferred to [35] |
| C8 | Diagram preservation implies ontic separability and PBR preparation independence | strong (as derivation) | Prop. 4.6; Eqs. 100–107 |
| C9 | Noncontextual ontological models are "essentially unique" | moderate | Thm 4.7 gives uniqueness up to an invertible real linear map. The authors themselves say that up to permutations of ontic states there are "likely" many (p. 24) |
| C10 | New proofs of quantum contextuality (Hardy excess baggage; no positive exact frame; 8-state model; qubit stabilizer via [59]) | strong (as corollaries) | §4.2–4.3; each combines the bound with a cited result |
| C11 | Theories that are not tomographically local "likely" violate Leibniz's principle | speculation | §6, p. 26 |
| C12 | The Wigner representation satisfies the definition; Q and P do not | informal argument | §5.1, p. 24. Wigner qualifies only after an unstated extension to infinite-dimensional GPTs (footnote 12) |

## Method

1. Model operational theories as process theories (symmetric monoidal categories). Quotient by operational equivalence to get the GPT; the quotient map ∼ is diagram-preserving (App. E.1).
2. Represent the GPT concretely: fiducial testers give finite real vectors (Eqs. 37–39). Composition is bilinear (Lemma 2.5, App. E.2). Under tomographic locality, the transition-matrix decomposition of the identity (Lemma 2.6) embeds the GPT into FVect_R (Thm 2.8).
3. Define ontological, quasiprobabilistic and noncontextual models as diagram-preserving maps into SubStoch or QuasiSubStoch (Defs. 2.9–2.11, 3.1).
4. Prove rigidity (App. B):
   - expand any process into effect-state channels (Cor. 2.7);
   - extend M linearly;
   - read off χ from states and φ from effects;
   - use empirical adequacy for φχ = 1 on the GPT;
   - use the identity for χφ = 1.
5. Specialize the codomain: QuasiSubStoch gives exact frames, and SubStoch adds positivity (App. D, via ordered vector spaces and cones).

## Concepts

- **Operational theory / GPT.** Unquotiented vs quotiented process theories. A procedure is (equivalence class, context). The GPT has no contexts, so "contextual" is not a predicate of its representations (App. A).
- **Generalized noncontextuality** (Def. 3.1). Operationally equivalent procedures, which agree on all testers, get identical ontological representations. It is defined here for arbitrary processes, not only preparations and measurements.
- **Tester.** A "clamp" (state, effect, auxiliary system) that closes any process into a scalar. Needed for operational equivalence when the theory is not tomographically local (footnote 5).
- **Tomographic locality.** Processes are determined by local state inputs and local effect outputs. Examples: quantum theory, classical theory, the Spekkens toy model, and the stabilizer subtheory in any dimension. Non-examples: real quantum theory and the real stabilizer subtheory (p. 13).
- **Diagram-preserving map.** Sequential and parallel composition, wirings and identities commute with the map; a strong monoidal functor (Remark 2.1).
- **Exact frame representation.** A quasiprobability representation built from a frame {F_λ} and dual {D_λ} that are bases, not overcomplete, with ⟨D_λ′, F_λ⟩ = δ.
- **Simplex embedding.** Another name for an ontological model of a GPT (§2.3.1; [4]).
- **Ontological excess baggage** γ_A = |Λ_A|/dim(A). Hardy's term (Eq. 99). Forced to 1 here.
- **Ontic separability.** Λ_AB = Λ_A × Λ_B: composites have no holistic properties (§4.4).

## Connections

**Quasi-quantization, [LIT-007](../literature.d/LIT-007.md) (Spekkens, arXiv 1409.5041).** [LIT-007](../literature.d/LIT-007.md) §IV.A is a concrete instance of what this paper proves in general. There, a nonnegative Wigner representation of states, Clifford transformations and quadrature measurements, read through the law of total probability, *is* an ontological model of the odd-d stabilizer / quadrature subtheory. Here that becomes Cor. 3.5, (iii) ⇔ (ii) ⇔ (i), for arbitrary compositional scenarios. And the structure theorem adds that such a model can only be an exact-frame change of basis.

The full read confirms the 14-reading's ontic-state conjecture (see corrections): |Ω| = d^{2n} = GPT dimension of the n-qudit stabilizer subtheory. Gross's phase-point operators ([LIT-007](../literature.d/LIT-007.md) Eq. 71) are the exact product frame that Props. 4.3 and 4.6 require. The paper cites [LIT-007](../literature.d/LIT-007.md) itself as [60], as the source showing Gross's model "can be reconstructed from an 'epistemic restriction'" (p. 25).

[LIT-007](../literature.d/LIT-007.md) left one claim unproved: "local and noncontextual by construction" (its C10). This paper does not prove it for epistricted theories as such either, but it supplies the route. For odd d the model is a positive diagram-preserving quasiprobability representation, so by Cor. 3.5 it is a noncontextual model of the stabilizer subtheory. For d = 2 the same machinery explains [LIT-007](../literature.d/LIT-007.md) §IV.B's bit/qubit gap:
- The qubit stabilizer subtheory is tomographically local with GPT dimension 4^n.
- Any noncontextual model would need exactly 4^n ontic states.
- Karanjai–Wallman–Bartlett [59] show quadratically many bits are needed, so none exists (§4.3).

The epistricted bit theory has exactly 4 ontic states per bit (and its own valid states span R^4 and R^16 for n = 1, 2, by my check). So it has the right *count* for a qubit but is a model of a different GPT.

**Why interference phenomena do not capture the essence of quantum theory, [LIT-019](../literature.d/LIT-019.md) (arXiv 2111.13727).** That paper cites this one ([47] there) for "classicality is intimately related to the positivity of quasi-probability representations". Its claim that the toy field theory is a noncontextual model of the TRAP interference fragment is asserted there, not proved (see NOTE for item 17, C5). This paper provides the test that would settle it: exhibit a positive exact frame representation of the TRAP fragment's GPT with 4 ontic states per mode.

**Abramsky & Brandenburger, [LIT-016](../literature.d/LIT-016.md).** Different notion, and the paper does not cite it. [LIT-016](../literature.d/LIT-016.md) formalizes Kochen–Specker/Bell-type contextuality as the non-existence of a global section of an empirical model over a measurement cover. Here, generalized noncontextuality is a constraint on ontological representations of an operational theory with respect to its operational equivalences. Both papers do share the move of casting classicality as the existence of a structure-preserving map (a global section; a strong monoidal functor into SubStoch), and both are categorical. App. A explains why KS-style contexts (measurement-outcome pairs) are invisible to a representation whose domain is the GPT. That explanation marks the formal boundary between the two notions. The paper does not attempt any formal comparison, such as whether a sheaf-theoretic non-contextual empirical model yields a diagram-preserving ontological model.

**Other lineage.**
- Spekkens 2005 [1]: definition of generalized noncontextuality.
- Spekkens 2008 [2]: contextuality ⇔ negativity in prepare-measure scenarios; corrected here (footnote 1) for conflating the operational theory with the GPT.
- Schmid et al. 2021 [4] and Shahandeh [5]: simplex embedding.
- Ferrie–Emerson [3, 38]: frame representations.
- Hardy [31, 39]: duotensors; excess baggage.
- Schmid–Du–Selby–Pusey [19]: uniqueness for odd-d stabilizer; the state-injection application.

## Bearing on the record

- **[LIT-003](../literature.d/LIT-003.md)** can move from `Deferred` to `Active`, with this note replacing the skim. Its summary is accurate; it could say "equal to" rather than rely on the abstract's "largest number". It should add that tomographic locality is necessary (§5.2).
- **[LIT-007](../literature.d/LIT-007.md) / [NOTE-013](NOTE-013.md).** This reading closes the 14-reading's "unverified" comparison in its favour, and supplies the general result (Cor. 3.5) of which [LIT-007](../literature.d/LIT-007.md) §IV.A is an instance. [NOTE-013](NOTE-013.md)'s Connections can cite this reading for the ontic-state match instead of the dossier.
- **[LIT-019](../literature.d/LIT-019.md).** Its classicality claim should be marked as resting on an unproved step. This paper gives the criterion for proving it (see the item-17 note).
- **THEORY.** A candidate [LIT-007](../literature.d/LIT-007.md)'s reading proposed can now be sourced properly: "Odd-prime stabilizer subtheories admit a noncontextual ontological model, unique and with exactly d^{2n} ontic states, given by Gross's Wigner function; the qubit stabilizer subtheory admits none." Sources would be this paper (§4.3, §5.1, §5.2), Gross 2006 and [19].
- **ML practice: none.** It carries no instruction for machine-learning practice and nothing for the Anthology of the SOTA. The formal shape is "a structure-preserving linear representation of a compositional theory is a change of basis; nonnegativity in some basis is the classicality test". That resembles questions about positive or nonnegative factorizations, but any such link is analogy only, and this reading gives no reason to pursue it.

## Limitations

- **Tomographic locality is essential, and the authors call it "the key limitation"** (§6). Real quantum theory and real stabilizer theories fall outside, and for them the dimension bound provably fails.
- **Diagram preservation is the substantive assumption on models.** It excludes overcomplete frames (the Q and P functions) and all excess-baggage models by fiat. The measure-and-reprepare instance is, by the authors' account, new. The full defence lives in another paper [35]. A reader who rejects diagram preservation keeps Cor. 3.5, which does not use it, but loses the rigidity and the count.
- **The abstract understates the result.** It says "largest number"; the theorem gives equality.
- **The §5.2 example's dimensions appear to be misstated** (see corrections). The argument for necessity is unaffected, and its general converse is correct.
- **Uniqueness is weaker than it sounds.** It holds up to invertible real linear maps, not up to permutations of ontic states (p. 24).
- **Finite dimension only.** Continuous-variable Wigner representations are covered only by an unstated extension (footnote 12). So [LIT-007](../literature.d/LIT-007.md)'s CV quadrature equivalence is not strictly in scope.
- **No new existence results.** The theorem constrains models that exist. Deciding existence (positivity of some χ) remains a nontrivial check: "one must check the condition for every χ_B" (§4.5).

## Open questions

- **Dropping tomographic locality.** Is there a structure theorem, perhaps with a weaker bound using testers with side channels, for theories that are not tomographically local? Alternatively, a principled argument (the suggested Leibnizian one, §6) that such theories are unphysical would close this.
- **Experimental tests of tomographic locality**, independent of quantum theory, by extending [73] to composite systems (§6).
- **Other nonclassicality algorithms.** Can the algorithms of [70, 71] be extended to compositional scenarios using this framework (§6)?
- **Stricter uniqueness.** When is the ontological model unique up to permutation of ontic states? This is known for odd-d stabilizer [19]; the general case is open (p. 24).
- **Relation to Kochen–Specker/sheaf contextuality** ([LIT-016](../literature.d/LIT-016.md)). Not addressed.

## Corrections to the seeded skim

- **The claim the 14-reading could not check holds.** The claim: the odd-d epistricted (Gross/Wigner) model has as many ontic states as the structure theorem requires.
  - The epistricted model of n qudits (odd prime d) has |Ω| = |(Z_d)^{2n}| = d^{2n}.
  - The GPT of the (convexified, complex) stabilizer subtheory spans the full Hermitian operator space, so its dimension is d^{2n}. Each Weyl operator W(a) is a linear combination of eigenprojectors of W(a), which are (mixed) stabilizer states, and the d^{2n} Weyl operators form a basis.
  - Computed directly: the stabilizer-state span has dimension 9, 25 and 81 for (d, n) = (3, 1), (5, 1), (3, 2). The epistricted valid states span R^{|Ω|}: 9 and 81 for d = 3; also 4 and 16 for d = 2.
  - So the count is exactly the Corollary 4.2 value, not merely within a bound.

  The paper itself makes the check only for qutrits: "the representation of n qutrits uses 9^n ontic states, matching the dimension of the relevant space of density matrices" (§5.2, p. 25). For general odd d it supports the claim only by citation: Gross's Wigner function is the unique noncontextual model of odd-d stabilizer subtheories, per [19] (§5.1, p. 24).

  The model meets the structure theorem's other requirements as well. Its phase-point operators are d^{2n} in number, orthogonal and tensor-product ([LIT-007](../literature.d/LIT-007.md) Eqs. 71, 74–76). So they form an exact frame that factorizes over subsystems, as Prop. 4.3 and Prop. 4.6 demand, and Ω_AB = Ω_A × Ω_B gives ontic separability (§4.4).
- **The §5.2 numbers look wrong, though the conclusion stands.** The dimension counts given for the real-amplitude qutrit stabilizer subtheory are those of real quantum theory, not of the real stabilizer subtheory. The paper says two such qutrits "are described by 45 parameters, whereas only 6² = 36 parameters are available from local measurements", and that the density matrices live in a ½·3^n(3^n+1)-dimensional space (p. 25). ½·3(3+1) = 6 and 45 are the dimensions of real symmetric 3×3 and 9×9 matrices.

  By direct enumeration the numbers are smaller:
  - **n = 1.** Only 4 single-qutrit stabilizer states are real up to phase (|0⟩, |1⟩, |2⟩, (|0⟩+|1⟩+|2⟩)/√3). They span 4 dimensions.
  - **n = 2.** 22 pure and 39 pure-or-mixed two-qutrit stabilizer states are real. They span 21 dimensions.

  The qualitative conclusion survives, and more strongly:
  - The theory is still not tomographically local (21 > 4² = 16).
  - Gross's model still overshoots the GPT dimension: 9 > 4 per qutrit, and 81 > 21 for two.

  This is my computation (check71.py), not the paper's. It assumes the subtheory's GPT dimension is the span of its real states, which follows from the paper's own definition of the GPT as the quotiented theory.
- **The abstract and the results say different things.** The abstract says the ontic-state number is "no larger than" / "the largest number possible" is the GPT dimension. The results (§1.1 item 3, §4.3) prove *equality*, |Λ_A| = dim(A), because χ_A is invertible. The dossier's "equals" is right, and the abstract understates it.
- **Diagram preservation is less assumed than the dossier suggests.** The dossier points to "diagram preservation (§5.1, App. B)" as the load-bearing assumption to scrutinize. App. B is the proof of Theorem 4.1, not a defence of diagram preservation; the full defence is deferred to Ref. [35] (Schmid–Selby–Spekkens, App. B there). The theorem uses only three instances of diagram preservation (Eqs. 76, 112–114):
  - prepare-measure factorization;
  - measure-and-reprepare factorization, which the authors say they are "not aware of ... having been made in previous works" (p. 24);
  - identity ↦ identity.
- **The skim's "essentially unique" needs qualifying.** Ontological models are unique up to a unique natural isomorphism in FVect_R, i.e. up to an invertible real linear map (Thm 4.7). The paper notes that under the stricter SubStoch notion (a permutation of ontic states) "it is likely that ... there are many different ontological models for a given GPT" (p. 24). Stronger uniqueness is proved only in special cases, such as odd-d stabilizer [19].
