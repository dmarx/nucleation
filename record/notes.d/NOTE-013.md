---
number: 13
status: Read
formerly:
- NOTE-tmpf1zve
paper: LIT-007
title: 'Quasi-quantization'
version: 2
history:
- version: 2
  date: '2026-09-25'
  note: >-
    Read in full (full text of arXiv:1409.5041v1 (dated 16 Sept 2014), 35
    pp.: §I.A–D, §II.A–E, §III.A–B, §IV.A–B, Appendix A (Proposition 1) and
    the reference list. Figures 1–14 are pictures of phase-space grids that
    did not survive text extraction; I read their captions and the prose
    that describes them, not the images. Extracted with PyMuPDF from
    raw4/1409.5041.pdf (no pdftotext on this host). The later Springer
    chapter version (DOI 10.1007/978-94-017-7303-4_4) was not compared.).
    Upgraded from `Skimmed` to `Read`: the claims table, assumptions and
    results are new, and the skim is corrected where the full text
    disagreed.
date: '2026-09-25'
summary: >-
  Take a classical statistical theory over a phase space Ω = R^{2n} or
  (Z_d)^{2n}, and allow only uniform distributions over V^⊥ + v, where V
  is an isotropic subspace (a Poisson-commuting set of linear "quadrature"
  variables) and v ∈ V gives their values. The result is operationally
  identical to the quadrature quantum subtheory (the stabilizer formalism
  for odd prime d) for continuous variables and for odd prime d; the proof
  is that the Wigner functions of that subtheory are exactly these
  distributions (§IV.A). For d = 2 the two theories are isomorphic element
  by element but make different predictions, because the qubit stabilizer
  subtheory is contextual (§IV.B).
---


# NOTE-013: Quasi-quantization

## Contribution

The paper gives one formalism, stated independently of the underlying field, for "epistricted" theories over continuous (R) and prime-order discrete (Z_d) phase spaces. States are parametrized by pairs (V, v): V an isotropic subspace, v ∈ V a valuation vector. Reversible dynamics is the symplectic affine group m ↦ Sm + a. Sharp measurements are indexed by isotropic subspaces.

Beyond the overview, it adds several things:
- **Discrete Poisson bracket.** A finite-difference Poisson bracket for Z_d (Eq. 17, attributed to Barrett), which makes the bracket of two quadrature functionals equal the symplectic inner product in the discrete case as well.
- **Quantum side.** On the quantum side, quadrature observables are defined as PVMs rather than Hermitian operators, so that CV and discrete systems are handled alike (§III.A).
- **CV case.** "Quadrature epistricted mechanics" and a proof that it equals the "quadrature subtheory" of quantum mechanics (§IV.A).
- **Proposition 1.** Quadrature states coincide with stabilizer states, with M = (V^⊥)^C = JV (App. A).
- **Classification.** A proposal to call a quantum phenomenon *weakly* nonclassical if it arises in some epistricted theory and *strongly* nonclassical otherwise (§I.B).

## Key insight

For odd prime d and for continuous variables, the stabilizer/quadrature fragment of quantum theory is a classical statistical theory plus a rule about which distributions may be prepared. Its Wigner representation *is* that classical theory: states become uniform distributions on affine subspaces, Clifford unitaries become symplectic affine permutations of phase space, and quadrature measurements become deterministic indicator functions. So the fragment's phenomenology, entanglement included, needs no nonclassical explanation. The residue that does need one is what separates quantum theory from such models: contextuality and Bell nonlocality. The cleanest place to see that residue is the gap between qubits and bits, where the two theories agree on everything except the probability rule.

## Assumptions

- **Classical ontology with symplectic structure.** Ontic states are points m ∈ Ω = R^{2n} or (Z_d)^{2n} with d prime, carrying the symplectic form ⟨f, g⟩ = f^T J g (Eqs. 14–15). Prime powers and other finite fields are explicitly excluded ("We shall consider here only the case where the order is itself a prime", p. 10).
- **Knowable variables are linear.** f = f^T z + c (Eqs. 8, 11, 16).
- **Joint knowability ⇔ Poisson commutation.** [f, g]_PB = ⟨f, g⟩ = 0 (Eq. 13). Closure under linear combination turns known sets into isotropic subspaces V ⊆ Ω, of dimension ≤ n (p. 12).
- **Maximum entropy given the constraints.** The valid state for (V, v) is µ_{V,v}(m) = N_V^{-1} δ_{V^⊥+v}(m), uniform over V^⊥ + v with V^⊥ the *Euclidean* complement (Eqs. 27–31). In the CV case uniformity is relative to the displacement-invariant measure.
- **Scope of the restriction.** It applies to knowledge from information wholly to the past or wholly to the future of the variables, not to pre/post-selection (p. 9).
- **Transformations supervene on ontic dynamics.** A map on epistemic states is valid only if it comes from a symplectic affine ontic map m ↦ Sm + a with S^T J S = J (Eqs. 32–33). Time reversal (q, p) ↦ (q, −p) preserves isotropy but is excluded (p. 14). Irreversible maps come from coupling to an ancilla in a valid state, then marginalizing.
- **Unsharp measurements** are sharp measurements on system plus valid ancilla after a symplectic affine coupling, the Naimark analogue (p. 15). Post-measurement update is not treated.
- **Quantum side.** Hilbert spaces L²(R^n) or C^{d^n}. Position and momentum eigenstates in the CV case are handled "informally", without rigged Hilbert space (p. 22). For qubits the character is χ(c) = e^{iπc/2}, a fourth root of unity rather than a second (Eq. 48).
- **The equivalence proof** needs a Wigner representation that is covariant under symplectic affine maps (Eq. 72), has orthogonal and complete phase-point operators (Eqs. 74–76), and represents position/momentum projectors as δ(q_i(m) − q) (Eq. 85). These hold for the standard CV Wigner function and for Gross's discrete one, which exists only for odd d (p. 31).

## Key results

- **Structure of states (§II.B.1).** Valid epistemic states ↔ pairs (V, v), V isotropic, v ∈ V. Pure states are the convexly extremal *valid* states, i.e. V Lagrangian (dim V = n). "Maximal knowledge is always incomplete knowledge" (p. 13).
- **Single trit (§II.D).** Four inequivalent quadrature functionals q, p, q+p, q+2p, no two Poisson-commuting. That gives 12 pure states (4 × 3 values) and one mixed state (total ignorance). Two trits: a pure state whose known variables are single-system is a product state; one whose known variables are both joint (e.g. q1 − q2, p1 + p2) is entangled (Figs. 6–7).
- **Single bit (§II.E).** Three inequivalent functionals q, p, q+p give 6 pure states and 1 mixed. There are 6 symplectic 2×2 matrices over Z_2 (Eq. 43) and 4 displacements (Eq. 45), so 24 reversible maps: every permutation of the 4 ontic states is allowed. For n = 2 only a subset of permutations is allowed.
- **Quantum side (§III.A, p. 25).** Commuting quadrature observables ↔ Poisson-commuting functionals. The argument: a set is Poisson-commuting iff it is the image of {q_1, …, q_k} under some symplectic S, and unitary conjugation by V̂(S) preserves commutation of the position PVMs.
- **Quadrature subtheory (§III.B).** States ρ_{V,v} = N_V^{-1} Π̂_V(v) (Eq. 66). Reversible maps are the Clifford superoperators U(S, a), a *non-projective* representation of the symplectic affine group (p. 27). Irreversible maps and general measurements come by Stinespring/Naimark dilation with quadrature-state ancillas and Clifford couplings.
- **Equivalence (§IV.A).** Holds for Ω = R^{2n} and (Z_d)^{2n}, d odd prime:
  - W_{Π̂_{V'}(v')}(m) = ξ_{V'}(v'|m) (Eq. 87)
  - W_{ρ_{V,v}}(m) = µ_{V,v}(m) (Eq. 88)
  - W_{U(S,a)}(m|m') = δ(m − (Sm' + a)) = Γ_{S,a}(m|m') (Eqs. 89–90)

  So every prediction Tr[Π̂ E(ρ)] equals the classical law-of-total-probability expression (Eq. 40). *Holds when:* the Wigner representation has properties (72), (74)–(76), (85), which excludes d = 2.
- **Inequivalence for d = 2 (§IV.B).** States, sharp measurements and reversible transformations are in bijection between the bit and qubit theories (all indexed by (V, v), V′, (S, a) on (Z_2)^{2n}), yet Tr[Π̂_{V'}(v') U_{S,a}(ρ_{V,v})] ≠ Σ ξ Γ µ in general. No nonnegative quasiprobability representation of the qubit theory exists, since it contains Mermin-square and GHZ proofs of contextuality and, by [50], contextuality ⇒ negativity (p. 31).
- **Proposition 1 (App. A).** For every prime d including 2, ρ_{V,v} equals the stabilizer state ρ^{(stab)}_{M,v}: the joint eigenstate of {Ŵ(a) : a ∈ M} with eigenvalues χ(⟨v, a⟩), where M = (V^⊥)^C = JV. So the stabilizer formalism coincides with the quadrature subtheory for discrete systems. In the CV case the quadrature subtheory is a proper part of the Gaussian subtheory.
- **Classification (§I.B, Table II).** *Weak* nonclassicality: noncommutativity, coherent superposition, collapse, complementarity, no-cloning, no-broadcasting, interference, teleportation, remote steering, key distribution, dense coding, entanglement and its monogamy, Choi–Jamiołkowski, Naimark, Stinespring, ambiguity of mixtures, locally immeasurable and unextendible product bases, pre/post-selection effects, quantum eraser. *Strong*: Bell violations, noncontextuality-inequality violations, computational speed-up "(if it exists)", "certain aspects of items on the left". *Uncategorized*: quantization of energy and angular momentum, indistinguishable-particle statistics (p. 6).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | For CV and odd prime d, the quadrature epistricted theory and the quadrature quantum subtheory give identical operational predictions | strong | Derivation via Wigner representation, Eqs. 85–90 (§IV.A); CV delta functions handled informally |
| C2 | Quadrature states = stabilizer states for all prime d, via M = (V^⊥)^C = JV | moderate | Proof sketch of Proposition 1 (App. A): single-mode argument, then "by an argument similar" for n modes |
| C3 | Commuting quadrature observables ↔ Poisson-commuting quadrature functionals ↔ isotropic subspaces | moderate | Argument on p. 25; relies on "every Poisson-commuting set is obtainable from every other by a symplectic linear transformation" (p. 24), shown only in the direction that S preserves commutation, not that such an S always exists (unverified here, though standard) |
| C4 | For d = 2 the epistricted theory of bits and the qubit stabilizer subtheory are structurally isomorphic but predict differently | moderate | The isomorphism is asserted from the shared (V, v)/(S, a) parametrization. That predictions differ follows from C5; no explicit counterexample computation is given |
| C5 | No quasiprobability representation of the qubit quadrature subtheory is nonnegative | strong (as a citation chain) | Ref. [50] (contextuality ⇒ negativity) + Mermin square / GHZ, both using stabilizer resources only (p. 31) |
| C6 | Quadrature epistricted theory of bits = Spekkens 2007 toy theory | assertion | Stated on p. 4; not shown in this paper |
| C7 | For odd d, classical complementarity is inequivalent to knowledge balance, and only the former reproduces the stabilizer theory | assertion | Stated on p. 4, citing unpublished [7] |
| C8 | The phenomena in Table II's left column arise in epistricted theories | assertion | Table II and §I.B prose; none derived here. Teleportation is argued in prose (6 stabilizer states, 2 classical bits < log2 6); the rest rest on the cited literature |
| C9 | Phenomena should be graded weakly vs strongly nonclassical by whether an epistricted theory reproduces them | informal argument | §I.B: a classical account should be "maximally permissive", which includes epistemic states and not only ontic states. A definitional proposal, not a result |
| C10 | Epistricted theories are local and generalized-noncontextual "by construction" | informal argument | §I.B–C, §IV.B; follows from being ontological models with deterministic, outcome-indicator response functions, but no proof is given here |
| C11 | Epistricted theories lie outside the convex-operational (GPT) framework because their state spaces are non-convex, but inside process-theory frameworks | informal argument | §I.D, citing [45], [46] |
| C12 | Quasi-quantization could extend to electrodynamics and gravity via a Lagrangian scheme | assertion / speculation | §I.A, p. 5; explicitly open |

## Method

1. Fix a phase space Ω over a field (R or Z_d, d prime) with symplectic form J. Define quadrature functionals and the Poisson bracket (Eq. 6 for CV, the finite-difference Eq. 17 for discrete), with [f, g]_PB = f^T J g.
2. Epistemic states: for isotropic V and v ∈ V, µ_{V,v} is uniform on V^⊥ + v. Transformations: Γ_{S,a}(m|m′) = δ(m − Sm′ − a). Sharp measurements: response functions ξ_V(v|m) = δ_{V^⊥+v}(m). Operational statistics by the law of total probability (Eqs. 39–40).
3. Quantum side: Weyl operators Ŵ(a) built from shift and boost unitaries (Eqs. 49–52), a projective metaplectic-type representation V̂(S) (Eqs. 55–56), and quadrature observables O_f = V̂(S_f) O_q V̂(S_f)† (Eq. 60). States ρ_{V,v} ∝ Π̂_V(v). Clifford superoperators U(S, a).
4. Bridge: phase-point operators Â(m) = N_Ω^{-1} Σ χ(⟨m, m′⟩) Ŵ(m′) (Eq. 71). Covariance and orthogonality make each quantum object's Wigner function equal the matching epistricted object.

A caution on notation: Eqs. 51–53 write the Weyl phase as χ(2pq) and the product rule as χ(2⟨a, a′⟩). For the CV case the usual factor is ½ (for odd d, 2^{-1} mod d). These look like a typo or an unusual convention; unverified, and they do not affect the argument, which uses only covariance (Eq. 56). Eq. 87 indexes the product over V where V′ is meant, and the text refers to "the third equality in Eq. (90)" for Eq. (89).

## Concepts

- **Ontic / epistemic state.** A physical state (a point of Ω) versus an agent's state of knowledge (a distribution over Ω) (§I.A).
- **Epistricted theory.** An epistemically restricted statistical theory of a classical system (p. 2).
- **Quadrature variable/functional.** A linear functional f = f^T z + c on phase space, identified with its coefficient vector f ∈ Ω (Eqs. 8–12).
- **Classical complementarity.** The valid epistemic states are those in which an agent knows the values of a Poisson-commuting set of quadrature variables "and is maximally ignorant otherwise" (p. 9).
- **Isotropic / Lagrangian subspace.** V with ⟨f, g⟩ = 0 for all f, g ∈ V; Lagrangian when dim V = n. These index jointly knowable sets, and Lagrangian ones index maximal knowledge.
- **Valuation vector.** v ∈ V, with value assignment v(f) = f^T v. Ontic states m and m′ give the same valuation iff P_V m = P_V m′ (p. 12).
- **Possibilistic state.** An epistemic state that is uniform on its support, so it says only which ontic states are possible (p. 9).
- **Supervenience on an ontological transformation.** An epistemic map is valid only if some valid ontic map induces it (p. 14, following [2]).
- **Symplectic affine group.** Maps m ↦ Sm + a with S^T J S = J, composing as (S, b)(S′, b′) = (SS′, Sb′ + b) (Eq. 34).
- **Quadrature observable O_f.** The PVM V̂(S_f)-conjugate of the position PVM, where S_f q = f (Eq. 60). It is defined without a Hermitian operator so that CV and discrete systems are treated alike.
- **Quadrature quantum subtheory.** States ∝ Π̂_V(v), Clifford superoperators, PVMs of commuting quadrature observables, closed under dilation with quadrature ancillas (§III.B). For discrete d it equals the stabilizer formalism; for CV it is strictly inside the Gaussian subtheory.
- **Quasi-quantization.** Applying one epistemic restriction uniformly to classical statistical theories of arbitrary degrees of freedom. "Quasi" because it recovers only a subtheory, and for bits not even that (p. 4).
- **Weak / strong nonclassicality.** Reproducible or not by some epistricted theory (p. 7).
- **Foil.** A theory close to quantum theory that nature could have instantiated. The bit theory is a foil even to the stabilizer subtheory (§I.D).

## Connections

**Builds on.** Spekkens 2007 toy theory [1] (knowledge-balance principle, d = 2); Bartlett–Rudolph–Spekkens 2012 [2] (Gaussian epistricted mechanics = Gaussian quantum mechanics); Gross 2006 [6] (a nonnegative discrete Wigner function for odd-d stabilizer theory, and the "symplectic affine" terminology); Pusey 2012 [4] (stabilizer notation for the toy theory); van Enk 2007 [5]; and unpublished Schreiber–Spekkens 2008 [7] (classical complementarity for trits). Its new position relative to these: it replaces knowledge balance with a condition on symplectic structure, and argues that choice is better because it reproduces the odd-d stabilizer theory where knowledge balance does not (p. 4). It also reframes Gross's result: the stabilizer formalism is as naturally the discrete *quadrature* subtheory as the discrete *Gaussian* one (App. A, p. 33).

**Frame for "Why interference phenomena do not capture the essence of quantum theory" (Catani, Leifer, Schmid, Spekkens, arXiv:2111.13727).** What this paper supports:
- It places "Interference", "Coherent superposition", "Complementarity" and "Quantum eraser" in the *weakly* nonclassical column of Table II (p. 6). The later paper's thesis, that interference does not force wave–particle duality or retrocausation, is the detailed defence of that placement.
- Table I lists "quadrature epistricted optics = quadrature subtheory of quantum optics", and §I.A proposes extending quasi-quantization to field degrees of freedom (p. 4–5). A classical statistical theory of field modes with a restriction on jointly knowing conjugate variables is a natural instance of that programme.
- The present paper also states the stance the later one turns into a methodology (per its dossier): judge a phenomenon nonclassical only after being "maximally permissive" about classical explanations, allowing epistemic as well as ontic states (p. 7). It names generalized noncontextuality [25] as what epistricted theories satisfy and what the strongly nonclassical phenomena violate (p. 6).

What this paper does *not* support: any derivation of interference phenomenology. It never works through an interferometer. From the dossier, the later paper's toy field theory (binary occupation numbers and Z_2 phases per mode) looks close to a quadrature epistricted theory of bits applied to modes, but whether it is literally an instance of §II.E's formalism is not settled by this paper. Unverified; check it in the full read of item 17.

**Frame for "A structure theorem for generalized-noncontextual ontological models" (Schmid, Selby, Pusey, Spekkens, arXiv:2005.07161).** Four parts of this paper set up what the structure theorem formalizes:
1. **Classicality equivalence.** §IV.A's proof *is* an instance of the equivalence the structure theorem generalizes. A nonnegative quasiprobability (Wigner) representation of states, transformations and measurements, read through the law of total probability (Eqs. 83–84 against 39–40), is literally an ontological model of the subtheory, and "the quadrature epistricted theory is the hidden variable model" (p. 32). The structure paper's triple equivalence (noncontextual model ⇔ positive quasiprobability representation ⇔ ontological model of the GPT) generalizes this beyond prepare-measure scenarios and makes it rigorous.
2. **Contextuality ⇒ negativity.** §IV.B already uses Ref. [50] (contextuality ⇒ negativity) as the reason the bit/qubit gap cannot be closed by a better Wigner function. The structure theorem is the compositional successor of that tool.
3. **Ontic-state count.** The epistricted model of n odd-d qudits has |Ω| = d^{2n} ontic states, d² per qudit. Per its dossier, the structure theorem says a diagram-preserving noncontextual model of a tomographically local theory has exactly GPT-dimension many ontic states, d² for a qudit. The two agree. The structure paper's counterexample to tomographic locality (the real-amplitude qutrit stabilizer subtheory with Gross's model) is built on the Gross/epistricted model this paper presents. Both comparisons are drawn from the dossier, not checked here.
4. **Framework.** §I.D notes that epistricted theories have non-convex state spaces and so fall outside the convex GPT framework but inside category-theoretic process theories [44, 45]. The structure theorem is stated in process-theoretic terms (dossier), which is consistent with this remark, but this paper does not anticipate the theorem itself.

This paper supports these links only as antecedents. It gives no general definition of an ontological model of a compositional theory, and its "local and noncontextual by construction" (C10) is not proved here.

## Bearing on the record

- **[LIT-007](../literature.d/LIT-007.md)** should move from `Deferred` once a `Read` note replaces NOTE-013. The [LIT-007](../literature.d/LIT-007.md) summary should be amended in two places. "Poisson-commuting quadrature variables" should include "and maximal ignorance otherwise". The equivalence should be stated as holding for CV and odd prime d with the *quadrature*, not Gaussian, subtheory.
- **[LIT-019](../literature.d/LIT-019.md)** (2111.13727) and **[LIT-003](../literature.d/LIT-003.md)** (2005.07161) can cite this paper as the source of the weak/strong nonclassicality classification and of the odd-d stabilizer ontological model. They should not cite it as demonstrating any Table II phenomenon.
- **THEORY documents.** None exist in this record yet (theory.d holds only the template). If one is filed, the natural candidate is: "the odd-prime stabilizer subtheory and the CV quadrature subtheory admit noncontextual ontological models given by their Wigner representations; the qubit stabilizer subtheory does not". Its source would be this paper, §IV, together with Gross 2006 and Spekkens 2008.
- **ML practice:** none. It carries no instruction for machine-learning practice and nothing for the Anthology of the SOTA. The dossier's loose analogy (a restriction on admissible distributions generating rich structure) is only an analogy, and this reading gives no reason to strengthen it.

## Limitations

- **Overview, not a paper of new theorems.** It says so itself (abstract). Key discrete results are credited to unpublished work [7]. The bit-theory = toy-theory identification (C6) and the claim that knowledge balance fails for odd d (C7) are asserted, not shown.
- **Table II does most of the rhetorical work and none of the technical work.** Its left column is supported only by citation and one prose argument about teleportation. The paper concedes that "if one looks hard enough" each left-column phenomenon has features an epistricted theory cannot reproduce, and puts those under "certain aspects of items on the left" (p. 5). That makes the weak/strong split depend on a judgement about which feature is "the mystery".
- **Measurement update is left out** (§II.B.3), though collapse, steering, key distribution and teleportation all use post-measurement states.
- **The CV quadrature subtheory is entirely idealized.** The pure states are joint eigenstates of quadrature operators (infinitely squeezed, not normalizable), and even the no-knowledge state is uniform over R^{2n}. The paper treats these "informally" (p. 22). This is my observation, not the paper's. The consequence is that the CV equivalence is between two idealized theories, and the physically preparable Gaussian subtheory is covered by the *different* restriction of [2].
- **Only prime d is treated.** Composite dimensions and prime powers are not.
- **Proof gaps.** The n-mode step of Proposition 1 and the CV equivalence are sketched rather than proved in full. There are notational inconsistencies in the Weyl phases (Eqs. 51–53) and in the equation references (Eq. 87, Eq. 89/90).
- **"Local and noncontextual by construction"** (C10) is stated but not proved for the general quadrature epistricted theory. It is plausible, since the theory is an ontological model with deterministic, outcome-indicator response functions, but checking it against the definitions of generalized noncontextuality in [25] is left to the reader.

## Open questions

- **A single restriction for all cases (p. 4).** Is there one epistemic restriction that gives the Gaussian subtheory for CV and the stabilizer subtheory for qudits? A restriction with both outputs would close it.
- **Conceptual meaning of the bit/qubit gap (p. 32).** The paper calls it "perhaps the most interesting product". It suggests the quantum innovation must be statable in possibilistic terms, but gives no candidate.
- **Quasi-quantization of electrodynamics and gravity** via a Lagrangian scheme (p. 5), with the epistemic restriction applied to matter and field alike.
- **Uncategorized phenomena.** Where do quantization of energy and angular momentum and indistinguishable-particle statistics fall in Table II (p. 6)? An epistricted theory reproducing, or provably failing to reproduce, them would settle it.
- **Beyond ontological models (§I.C).** The programme is framed as a first step toward rejecting classical probability theory for epistemic states while keeping the quantum state epistemic. What would replace it is left open.

## Corrections to the seeded skim

- The dossier and NOTE-013 skim say the CV/odd-prime equivalence is with "the quadrature (stabilizer/Gaussian) quantum subtheory". This is wrong for continuous variables. The paper separates the quadrature subtheory from the Gaussian subtheory, which strictly contains it (App. A, p. 33). The equivalence proved here is between *quadrature* epistricted mechanics and the *quadrature* subtheory. Gaussian epistricted mechanics comes from a different restriction, the classical uncertainty principle of Bartlett–Rudolph–Spekkens 2012, and the classical-complementarity restriction admits a *smaller* set of states than that one (p. 4). The paper leaves open whether any single restriction yields the Gaussian subtheory for CV and the stabilizer subtheory for qudits (p. 4).
- "Classical complementarity" is more than "you may only jointly know Poisson-commuting quadrature variables" (the [LIT-007](../literature.d/LIT-007.md) summary). It has three parts: (i) only *linear* functionals f = Σ(a_i q_i + b_i p_i) + c can be known; (ii) a jointly known set must Poisson-commute; (iii) the agent is *maximally ignorant otherwise*, i.e. holds the uniform distribution on the consistent region (§II.A, p. 9). Part (iii) makes every state possibilistic and the state space non-convex (§I.D). The restriction also applies only to knowledge from wholly past or wholly future information, not to pre- and post-selection (p. 9).
- The skim says qubit/bit inequivalence holds "because qubit Wigner functions go negative". The paper makes a stronger claim: *no* quasiprobability representation of the qubit quadrature subtheory can be nonnegative. It argues this from Ref. [50] (Spekkens 2008: a proof of contextuality forces negativity) plus Mermin's square and GHZ, both of which use only stabilizer resources (p. 31). The Gibbons–Hoffman–Wootters Wigner function going negative is just one instance of this.
- Table II is not demonstrated anywhere in this paper. No phenomenon on its left-hand list (teleportation, key distribution, entanglement monogamy, etc.) is derived in §II–IV. The placements rest on earlier work, mainly the 2007 toy theory [1]. The paper also sets aside measurement update ("we will not discuss the transformative aspect of measurements", §II.B.3), so "collapse" in Table II gets no support from the formalism given here.
- The paper calls itself an overview ("This article provides an overview", abstract). The trit/odd-d results are credited to unpublished 2008 work with Olaf Schreiber [7] (Acknowledgments: "Much of the work presented here summarizes unpublished results"). The dossier's question of what is new is answered in "Contribution" below.
