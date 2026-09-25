---
number: 18
status: Read
formerly:
- NOTE-tmphvs2x
paper: LIT-019
title: 'Why interference phenomena do not capture the essence of quantum theory'
version: 2
history:
- version: 2
  date: '2026-09-25'
  note: >-
    Read in full (full text of arXiv:2111.13727v7 (18 Sep 2023, the version
    accepted by Quantum on 2023-09-01), 61 pp. I read §1–5, the
    acknowledgements, the reference list [1]–[109], and Appendices A.1–A.3,
    B and C.1–C.6. I extracted the text with PyMuPDF into
    raw4/2111.13727.txt (pdftotext is not on this host). Figures 1–11 are
    box-grid diagrams, and their images did not survive extraction; I read
    the captions and the formal expressions that accompany them (Eqs. 26–53,
    56–57). I checked the arithmetic of the TRAP account in a short script
    (scratchpad/check17.py): the Eq. 13 beamsplitter and Eq. 22 CNOT are
    symplectic over Z_2; the beamsplitter is its own inverse; and the
    phase-shifter, which-way and eraser statistics come out as the paper
    states. I did not compare the published Quantum version (DOI
    10.22331/q-2023-09-25-1119) with this arXiv version.). Upgraded from
    `Skimmed` to `Read`: the claims table, assumptions and results are new,
    and the skim is corrected where the full text disagreed.
date: '2026-09-25'
summary: >-
  The paper models each mode of the interferometer as a classical bit pair
  (occupation N ∈ Z_2, phase Φ ∈ Z_2). The agent may know only one of N, Φ
  or N⊕Φ and must be maximally ignorant of the rest. Under that
  restriction, local and deterministic dynamics (beamsplitter: swap N_L
  with Φ_L⊕Φ_R) reproduce exactly the 50-50, ϕ ∈ {0, π} Mach–Zehnder
  statistics (output port L with probability 1 or 0; ½/½ with a which-way
  detector). The same holds for the Elitzur–Vaidman bomb tester (success
  probability ¼), delayed choice and the quantum eraser (interference
  within each P_A outcome class, none within each Q_A class). So this
  "TRAP" slice of interference phenomenology cannot, on its own, force
  wave–particle complementarity, observer-dependence or
  nonlocal/retrocausal influence. The paper leaves aside the phenomenology
  it concedes is nonclassical (unbalanced beamsplitters, the functional
  form of the duality relation, Hardy's interferometer).
---

# NOTE-018: Why interference phenomena do not capture the essence of quantum theory

## Contribution

The paper builds an explicit classical statistical model of a discrete field, which it calls the "toy field theory". It shows that the model reproduces exactly the part of Mach–Zehnder phenomenology that the standard arguments for three interpretational claims actually use. The three claims are wave–particle complementarity, observer-dependence of reality, and the failure of local causal explanation. The model does this with local, deterministic, reversible dynamics and an epistemic restriction. It does the same for the Elitzur–Vaidman bomb tester, Wheeler's delayed choice and the Scully–Englert–Walther quantum eraser.

Two further contributions:
- **Second quantization matters.** A local account exists in the second-quantized (mode) description but is not manifest in the first-quantized one, because the first-quantized toy theory is a coarse-graining of the mode theory (Eq. 14).
- **Methodology.** Interpretational claims should be backed by a no-go theorem against an explicitly formalized notion of classicality. The paper's own notion implies generalized noncontextuality.

The model is credited to 2005 work with Elliot Martin (footnote 40; Acknowledgements).

## Key insight

The quantum vacuum in the unused arm is read as a *state of incomplete knowledge*, not a state of reality. An unoccupied mode still carries a physical phase bit, and a detector on that arm can flip it (with probability ½) without the arm being occupied. That flip reaches the second beamsplitter along the empty arm by local propagation. The beamsplitter's Swap Rule then makes the relative phase decide the output port. So "which-way detection destroys interference" is a local disturbance of a phase the agent cannot see. The dependence on later or distant choices (delayed choice, eraser) is *inference*: Bayesian updating about properties that were there all along. It is not influence. What makes this work is ψ-epistemicity: the pure-state analogue has support on several ontic states (§5.2.1). A ψ-ontic reading of the vacuum rules the account out from the start.

## Assumptions

- **Scope of phenomenology ("TRAP").** Only balanced (50-50) beamsplitters and phase shifts ϕ ∈ {0, π}. A single excitation (N_L⊕N_R = 1 throughout). Photon injected at input port L. No free-space phase. The unbalanced and continuous-phase predictions are explicitly excluded (§2.1, §5.2.4).
- **Ontology.** Each mode j has a physical state (N_j, Φ_j) ∈ Z_2 × Z_2. N is a binary occupation, and N ↦ N⊕1 is the analogue of Pauli X within {|0⟩, |1⟩}, not a creation operator (footnote 20). Φ ∈ {0, π} is encoded mod 2.
- **Epistemic restriction, one mode** (p. 12). At most one of N, Φ, N⊕Φ is known, and the agent is maximally ignorant otherwise, so every valid state is uniform on its support (App. A.1, p. 40). The restriction applies to knowledge from data wholly in the causal past or wholly in the causal future (footnote 21).
- **Epistemic restriction, two modes.** Only certain pairs of variables are jointly knowable; the examples are (N_L, N_R) and (N_L⊕N_R, Φ_L⊕Φ_R) (p. 12). The general rule is deferred to [9, 10].
- **Dynamics.** Local and deterministic. The beamsplitter is Eq. 13, equivalently the Swap Rule "swap N_L and Φ_L⊕Φ_R; keep Φ_R and N_L⊕N_R" (Eq. 31). The π phase shift is Φ ↦ Φ⊕1 (Eq. 34). The eraser CNOT is Eq. 22: N_R′ = N_R, Φ_R′ = Φ_R⊕P̄_A, Q̄_A′ = Q̄_A⊕N_R, P̄_A′ = P̄_A.
- **Measurement update** (p. 14; Eqs. 41–50). A nondestructive, repeatable measurement of N conditions on the outcome and then randomizes that mode's Φ. Footnote 22 says this randomness is deterministic at the level of the apparatus's unknown variables, but only by reference to a continuous-variable discussion in [3]. A destructive measurement randomly resets Φ to 0 or 1 and sets N = 0 (App. C.3).
- **Probabilities are credences.** App. C.1–C.2 argue this does not weaken testability, via i.i.d./de Finetti, and recast the account in terms of ensembles.

## Key results

- **Phase shifter** (§3.1.2; App. A.1).
  - After the first beamsplitter: N_L, N_R uniform, Φ_L⊕Φ_R = 1 with certainty, Φ_R uniform (Eq. 32).
  - ϕ = 0 gives output L with probability 1; ϕ = π gives output R with probability 1 (Eqs. 26, 39).
- **Which-way detector on R** (§3.1.3; Eqs. 46–53). The detector fires with probability ½. Whether or not it fires, Φ_R is randomized, so Φ_L⊕Φ_R becomes uniform and the outputs are ½/½.
- **Bomb tester** (§4.1). A functional bomb that does not explode is certified with probability ½ × ½ = ¼. The "interaction-free" certification is carried by a local phase flip of the *unoccupied* mode R.
- **Delayed choice** (§4.2). Both N and the relative phase have values throughout. The late choice fixes only which one can be inferred.
- **Quantum eraser** (§4.3; App. A.3, Eq. 57).
  - Measuring Q_A sorts runs by N_R: no interference in either subset.
  - Measuring P_A sorts runs by the back-action on Φ_R, and hence by Φ_L⊕Φ_R: complete interference in each subset.
  - The choice made at A changes nothing about modes L and R.
  - App. B: every ψ-ontic model (Bohm, collapse, Blasiak) needs nonlocality for the eraser, because it is an EPR-type scenario [80]. The toy field theory does not.
- **First vs second quantization** (§3.3; Eq. 14). W and Θ are the coarse-grainings (N_L, N_R) ↦ W and Φ_L⊕Φ_R ↦ Θ. A joint phase flip on both modes acts as the identity at the coarse-grained level. Locality is manifest only in the fine-grained description.
- **Robustness extensions.**
  - Destructive detectors: a random reset gives the same stochastic map on Φ_R as a random flip (App. C.3).
  - Mirror removed: the R input is replaced by the vacuum mode R′ (App. C.4).
  - Spatially localized cellular-automaton model (App. C.6, Eqs. 58–63).
- **What is conceded to be nonclassical** (p. 5; §5.1.3; §5.2.4):
  - Hardy's overlapping-interferometer Bell argument [23].
  - The functional form of the wave–particle duality relation, and experiments with non-50-50 beamsplitters: shown to admit no generalized-noncontextual model in [24].
  - Coherence/contextuality in a Mach–Zehnder interferometer [72].

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The toy field theory reproduces the quantum statistics of the balanced, ϕ ∈ {0, π} Mach–Zehnder with phase shifter or which-way detector | strong | Explicit calculation, §3.1 and App. A.1 (Eqs. 26–53); re-derived in check17.py |
| C2 | It reproduces the bomb tester (¼ success), delayed choice and the quantum eraser | strong | §4.1–4.3 and App. A.3 (Eq. 57); eraser statistics re-derived. The main-text port labels on p. 26 are reversed (see corrections) |
| C3 | The model's dynamics are local and deterministic, with kinematical locality as well | strong | Maps act only on contiguous modes (Eqs. 13, 22, 34); cellular-automaton recasting in App. C.6 |
| C4 | Therefore the three interpretational claims are not forced by TRAP phenomenology | strong (as a logical point) | An existence proof by counter-model. It is as strong as C1–C3, relative to the TRAP scope |
| C5 | The toy field theory satisfies the authors' preferred notion of classicality, (i) sets/functions, (ii) Bayesian/Boolean inference, (iii) Leibnizianity, and hence generalized noncontextuality | assertion | (i) and (ii) are argued in one paragraph each (p. 28). (iii) is "for the same reason that other epistemically restricted ... theories do [9, 10]". No proof that the model is noncontextual with respect to the quantum TRAP operational equivalences |
| C6 | Feynman's claim that interference is "impossible, absolutely impossible, to explain in any classical way" is "proven to be simply false" (§5.1.1) | moderate | Follows from C1–C4 for the TRAP slice only. As a verdict on "the only mystery" it rests on C5 and on a reading of what Feynman meant |
| C7 | A local account is manifest only in the second-quantized description; the first-quantized toy theory is a coarse-graining | informal argument | §3.3, Eq. 14. The joint-phase-flip example shows the coarse-graining loses information. That no local first-quantized account exists is argued, not proved |
| C8 | Every ψ-ontic model needs nonlocality for the quantum eraser | moderate (citation) | App. B, via "the eraser is an EPR scenario" + [80] (Harrigan–Spekkens) |
| C9 | Only the toy field theory, among realist accounts, preserves both sets-and-functions kinematics and Leibnizianity | informal argument | App. B end: the alternatives are ψ-ontic, and ψ-ontic models are preparation contextual [45] |
| C10 | The toy field theory is not ad hoc | informal argument | §5.2.3: the vacuum-as-knowledge feature is forced by the epistemic restriction, which independently reproduces [LIT-007](../literature.d/LIT-007.md)'s Table II. Leans on Table II, which [LIT-007](../literature.d/LIT-007.md) asserts rather than derives |
| C11 | Unbalanced beamsplitters suffice for a noncontextuality no-go | citation | §5.2.4, attributed to [24]; not shown here |

## Method

1. Fix the scope. Isolate the TRAP phenomenology: only the predictions that the three interpretational arguments use (§2.1–2.2).
2. Pass from the first-quantized (one photon, path qubit) to the second-quantized (two modes, qubit Fock spaces) description, via |L⟩ ↦ |1⟩_L|0⟩_R (Eq. 7). The beamsplitter becomes an entangling map on modes (Eq. 9).
3. Build the classical counterpart by [LIT-007](../literature.d/LIT-007.md)'s three steps:
   - classical kinematics and dynamics (Z_2 × Z_2 per mode, symplectic maps);
   - the statistical theory over it;
   - an epistemic restriction.

   Map each quantum state, unitary and measurement in the circuit to a uniform distribution, a permutation of ontic states, and a conditioning-plus-randomization rule.
4. Propagate distributions through each circuit (App. A). Compare the output statistics with the quantum ones. Read each interpretational claim against the model's ontology.

## Concepts

- **TRAP phenomenology.** "The phenomenology that is traditionally regarded as problematic": exactly those aspects of interference that appear in the arguments for the three interpretational claims (§2.1). A deliberately narrow set.
- **Toy field theory** (= second-quantized toy theory). An epistemically restricted statistical theory of discrete field modes, each with a binary occupation number and a binary phase.
- **Swap Rule.** The 50-50 beamsplitter swaps N_L and Φ_L⊕Φ_R and preserves Φ_R and N_L⊕N_R (§3.1.1).
- **Epistemic restriction** (here). A limit on which distributions over ontic states an agent may hold; for one mode, knowledge of at most one of N, Φ, N⊕Φ.
- **Wave–particle complementarity** (strong sense). The denial that particle-like and wave-like properties can be *jointly well-defined*. The paper separates this from the weak sense, which denies joint measurability, and argues the weak does not imply the strong (footnote 4).
- **Global but non-holistic property.** A property defined from the parts but belonging to the pair, such as the relative phase Θ = Φ_R⊕Φ_L. The paper's analogy is a centre of mass (p. 18).
- **Leibnizianity.** Empirically indiscernible situations should be ontologically identical, generalized to probabilistic theories in [35]. It implies generalized noncontextuality.
- **Kinematical vs dynamical locality.** Localized systems vs local interactions (App. C.6, citing [108]).
- **Ontic indifference principle** (Hardy [83]). If a pure state is invariant under a transformation, so is every ontic state in its support. Footnote 37 argues epistricted theories make this principle implausible, since a phase flip leaves the vacuum distribution invariant but changes the ontic state.

## Connections

**Quasi-quantization, [LIT-007](../literature.d/LIT-007.md) (Spekkens, arXiv 1409.5041).** This paper is a direct application of [LIT-007](../literature.d/LIT-007.md)'s quasi-quantization scheme, and it says so (pp. 4, 11). The full read settles the question the item-14 reading left open. For the parts the paper states, the toy field theory is the quadrature epistricted theory of bits ([LIT-007](../literature.d/LIT-007.md) §II.E), with modes as systems and (q, p) = (N, Φ). The Mach–Zehnder maps are symplectic affine maps on (Z_2)^{2n}; see corrections for the details and the three places where the paper goes beyond [LIT-007](../literature.d/LIT-007.md).

[LIT-007](../literature.d/LIT-007.md) placed "interference", "coherent superposition", "complementarity" and "quantum eraser" in its weakly nonclassical column (Table II), mostly by citation. This paper is the detailed derivation that Table II lacked for those four entries, and only for them. The rest of the column is still undemonstrated. The paper's own gloss on Table II is still that it lists phenomena these theories "can also reproduce" (p. 32).

The paper also inherits [LIT-007](../literature.d/LIT-007.md)'s d = 2 caveat without discussing it. [LIT-007](../literature.d/LIT-007.md) §IV.B shows the bit theory and the qubit stabilizer theory make different predictions, because the latter is contextual. The paper's "qubit field theory" for two modes is, by its own footnote 14, the two-qubit stabilizer subtheory, and that subtheory already contains the Peres–Mermin contextuality proof. So the toy field theory is a classical model of the TRAP *fragment*, not of the subtheory in which the fragment is described. This is consistent with the paper's scope statement (p. 5: the toy theory "cannot reproduce the full scope of quantum phenomenology"), but a reader should not infer the stronger claim.

**Structure theorem, [LIT-003](../literature.d/LIT-003.md) (Schmid, Selby, Pusey, Spekkens, arXiv 2005.07161; reference [47] here).** Cited as the source of "classicality ⇔ positive quasiprobability representation" (p. 27). A structure-theorem check of the toy field theory as a model of the quantum TRAP fragment would make C5 rigorous: ask whether a positive exact frame representation of the fragment's GPT exists. The paper does not attempt it. One point is suggestive but unchecked: the toy field theory uses exactly 4 ontic states per mode, which equals the GPT dimension of a qubit, and that is the count [LIT-003](../literature.d/LIT-003.md)'s corollary requires of any diagram-preserving noncontextual model of a tomographically local qubit theory.

**Abramsky & Brandenburger, [LIT-016](../literature.d/LIT-016.md).** No direct connection. That framework treats contextuality as the absence of a global section over measurement contexts: Kochen–Specker-type, possibilistic/probabilistic. The notion here is generalized (Spekkens) noncontextuality. Interference experiments with one single-photon setting per run do not have the compatibility structure the sheaf approach needs. This matches the paper's remark that most interference experiments lack the causal structure for a Bell-type theorem (p. 28).

**Other lineage.**
- Spekkens 2007 toy theory [9]: the knowledge-balance principle and the measurement update rule.
- Bartlett–Rudolph–Spekkens 2012 [3]: Gaussian epistricted mechanics, and the deterministic apparatus account in footnote 22.
- Catani–Leifer–Scala–Schmid–Spekkens [24]: the companion paper that identifies which interference phenomena *are* nonclassical.
- Hance & Hossenfelder [92]: a comment on an earlier draft, answered in App. C.3–C.4.

## Bearing on the record

- **[LIT-019](../literature.d/LIT-019.md)** can move from `Deferred` to `Active`, with this note replacing the skim. Its summary is accurate as far as it goes. It should add that the reproduction covers only balanced beamsplitters and ϕ ∈ {0, π}, and that the paper concedes the unbalanced/duality-relation phenomenology is nonclassical [24].
- **[LIT-007](../literature.d/LIT-007.md) ([NOTE-013](NOTE-013.md) bearing).** This reading supplies the missing derivation for four Table II entries: interference, coherent superposition (in the interferometer sense), complementarity and quantum eraser. It supplies nothing for the rest of that column.
- **THEORY.** The record has no theory documents yet. A candidate this paper would *support* is: "The TRAP phenomenology of two-path interference admits a local, ψ-epistemic classical statistical model; interference as such is not a witness of nonclassicality." A candidate it would *not* support as stated is anything claiming a proved noncontextual model (C5).
- **ML practice: none.** It carries no instruction for machine-learning practice and nothing for the Anthology of the SOTA. The methodological point applies in general: do not infer "no classical explanation" from failing to find one; state the criterion and prove a no-go. But it is epistemology of science, not an ML recommendation, and dressing it as one would be an analogy.

## Limitations

- **The scope is deliberately narrow, and the headline is broader than the body.** The body reproduces 50-50, ϕ ∈ {0, π}, single-excitation experiments. The title and §5.1.1 speak of "interference phenomena" and "the only mystery", and the abstract of "basic interference phenomena". The paper itself concedes that unbalanced beamsplitters already give a noncontextuality no-go [24], and so do Hardy's interferometer and the duality relation.
- **Classicality is asserted, not proved (C5).** The argument that TRAP phenomenology is classical *by the authors' preferred notion* needs the toy field theory to be a generalized-noncontextual model of the quantum operational theory for those experiments. That step rests on citation to [9, 10], and neither of those (nor [LIT-007](../literature.d/LIT-007.md)) proves it for this setting. That the three interpretational claims are *not forced* (C4) does not depend on C5: C1–C3 suffice for local realism without complementarity.
- **The two-mode epistemic restriction is not stated in general.** It is given only by example (p. 12). A reader must supply [LIT-007](../literature.d/LIT-007.md)'s Poisson-commutation rule.
- **The single-excitation constraint.** N_L⊕N_R = 1 is imposed on all states and transformations (p. 12). The eraser's CNOT, when A is itself a mode, breaks number conservation (footnote 30).
- **The measurement model needs outside support.** The randomization in measurement update is said to be deterministic at the apparatus level. The paper gives this only by analogy to a continuous-variable discussion elsewhere (footnote 22). The destructive-measurement reset maps (App. C.3) are chosen to reproduce the statistics; that they arise from an ancilla-swap dynamics is not shown.
- **Typographical and labelling errors.** The p. 26 port labels are reversed; the p. 22 relative phase should be 1, not 0; the p. 23 normalizations read "1/2" for 1/√2; and Eq. 21's text reference is reversed. None affects a conclusion.

## Open questions

- **Which interference phenomena are genuinely nonclassical, and by how much?** [24] and [72] begin this. A full characterization of the boundary between noncontextually modelable and non-modelable two-path experiments, as a function of beamsplitter reflectivity and phase, would settle it.
- **Fermions.** Aharonov's objection (footnote 42) is that the account works for bosons but not for fermions. A toy field theory with fermionic (anticommuting) mode structure, or a proof that none exists, would close it.
- **A proof of C5.** Show that the toy field theory is a diagram-preserving noncontextual model of the quantum TRAP fragment, for instance by exhibiting it as a positive exact frame representation of that fragment's GPT in [LIT-003](../literature.d/LIT-003.md)'s sense.
- **Continuous phases.** Can a continuous-variable epistricted field theory (Gaussian or quadrature, per [3] and [LIT-007](../literature.d/LIT-007.md)) reproduce balanced interference for arbitrary ϕ? If not, where exactly does it fail?

## Corrections to the seeded skim

- The dossier says the toy theory's classicality under the preferred criterion is established in §5.1.2–5.1.3. The paper *asserts* it. Criterion (iii), Leibnizianity and hence generalized noncontextuality, is said to hold "for the same reason that other epistemically restricted classical statistical theories do [9, 10]" (p. 28). The implication "criteria (i)–(iii) ⇒ generalized-noncontextual model" is a citation to [45]. No argument in this paper shows that the toy field theory is a generalized-noncontextual model *of the quantum TRAP operational theory*: quantum procedures that are operationally equivalent within the TRAP fragment would need to receive the same toy distribution. [LIT-007](../literature.d/LIT-007.md) did not prove its analogous claim either (its C10), so the chain is unproved at both links.
- Two internal inconsistencies the skim could not see, both confirmed by direct computation (check17.py):
  - **Eraser port labels.** In the toy account of the eraser, §4.3 (p. 26) says the a+ data set always has the photon at the **R** output port and a− at **L**. The quantum account (p. 23) and the formal toy account (App. A.3, Eq. 57: the a+ branch has Φ_L⊕Φ_R = 1, so the Swap Rule gives N_L = 1) both put a+ at **L**. The p. 26 sentence has the labels reversed.
  - **Relative phase.** §4.2 (p. 22) says "one knows the relative phase to be zero inside the interferometer". By §3.1.1 (p. 13) and Eq. 32 it is Φ_L⊕Φ_R = 1 with certainty after the first beamsplitter. Only the fact that it is *known* matters to the argument, so neither slip changes a conclusion.
- The dossier's list of experiments is incomplete. Appendices C.3 and C.4 add two cases that Hance & Hossenfelder's comment [92] speculated would resist classical explanation: destructive measurement (a brick or photodetector in arm R, modelled by a random reset-to-0/reset-to-1 of the phase), and the interferometer with the R mirror removed. Appendix C.6 recasts the model as a Margolus-partitioned cellular automaton of spatially localized cells, to secure kinematical as well as dynamical locality.
- The question left open by the item-14 reading was whether the toy field theory is literally an instance of [LIT-007](../literature.d/LIT-007.md) §II.E. It is, in its kinematics and dynamics:
  - Each mode is one bit of the quadrature epistricted theory with q = N and p = Φ.
  - N, Φ, N⊕Φ are exactly the three nonzero functionals on Z_2².
  - "Maximally ignorant otherwise" is stated verbatim (p. 12).
  - Every dynamical map given is symplectic affine over Z_2: the beamsplitter (Eq. 13), the phase flip (Eq. 34), the CNOT (Eq. 22) and free propagation (Eq. 58). Footnote 32 says so, and I checked the matrices.

  The paper goes beyond [LIT-007](../literature.d/LIT-007.md) in three places:
  - The rule for jointly knowable two-mode variables is given only by example: (N_L, N_R), or (N_L⊕N_R, Φ_L⊕Φ_R), whose Poisson bracket I checked is 0 mod 2. It is not stated as the Poisson-commutation condition.
  - The measurement update rule, "Bayesian conditioning, then randomize the conjugate variable", comes from the 2007 toy theory [9]. [LIT-007](../literature.d/LIT-007.md) explicitly sets measurement update aside.
  - The constraint N_L⊕N_R = 1 and the destructive-measurement reset maps are not bijections. They are obtainable by swapping in a fresh vacuum mode, which is [LIT-007](../literature.d/LIT-007.md)'s ancilla route, but the paper does not say so.
