---
number: 282
status: Read
formerly:
- NOTE-tmp8r6cn
paper: LIT-305
title: 'On the Generalization of Equivariance and Convolution in Neural Networks to the Action of Compact Groups'
version: 1
history:
- version: 1
  date: '2026-09-29'
  note: >-
    Read in full (The full text of arXiv 1802.03690 v3 (10 Nov 2018; the PDF
    carries "Proceedings of the 35th International Conference on Machine
    Learning, Stockholm, Sweden, PMLR 80, 2018"), from the arXiv PDF, 14 pp.
    I read the abstract, §§1–7, Appendices A (group and representation
    theory), B (vector-valued convolution), C (proof of Prop. 1), D (proof
    of Prop. 2) and E (proof of Theorem 1, reverse direction, Lemmas 3–10),
    and the references. Nothing was skipped. The text was extracted with
    PyMuPDF. The three sparsity-pattern schematics in §4.2 survive only as
    labels, and I reconstructed them from Prop. 1 and its proof.). The first
    NOTE on this paper, which was seeded from its abstract alone.
date: '2026-09-29'
summary: >-
  Theorem 1 says that a feed-forward network whose layers are linear maps
  followed by pointwise nonlinearities, with every layer indexed by a
  homogeneous space G/H_ℓ of a compact group G, is G-equivariant (every
  layer transforming by the induced action) if and only if each linear map
  is a generalised convolution f ∗ χ with a filter on the double coset
  space H_{ℓ−1}\G/H_ℓ. The "if" direction is a short coset computation.
  The "only if" direction goes through the group Fourier transform:
  equivariant maps preserve isotypic components (Lemma 6) and act on each
  Fourier matrix by right multiplication, M ↦ MB (Lemma 10), which the
  convolution theorem (Prop. 2) turns back into a convolution.
---

# NOTE-282: On the Generalization of Equivariance and Convolution in Neural Networks to the Action of Compact Groups

## Contribution

It defines generalised convolution between functions on quotient spaces of a group:

- **Definition 4 (eq. 8).** (f ∗ g)(u) = Σ_{v∈G} f↑G(uv⁻¹) g↑G(v).
- **The three cases.** f on G, g on G/H (eq. 9); f on G/H, g on H\G (eq. 11); f on G/H, g on H\G/K (eq. 12).

It shows how quotient-space functions appear in Fourier space: their Fourier matrices are sparse in the columns and rows where the restricted irrep is non-trivial (Prop. 1). It proves the convolution theorem, the Fourier transform of f ∗ g at ρ equals f̂(ρ)ĝ(ρ) (Prop. 2), in all these combinations.

Its main result, Theorem 1, is that in a network whose layers live on homogeneous spaces of a compact group, equivariance holds exactly when every linear layer is such a convolution. It reads three existing architectures through this lens (§6):

- **Harmonic networks.** G = SO(2) on S¹ (Worrall et al.).
- **Spherical CNNs.** SO(3)/SO(2) = S². Only the middle column of each Wigner matrix survives, which gives the spherical harmonics.
- **Message-passing networks.** Receptive fields as S_n/(S_k × S_{n−k}), with irreps indexed by the two-row partitions (n−p, p).

No new architecture or experiment is presented (§1).

## Key insight

Equivariance is an intertwining condition, and Schur's lemma governs intertwiners. The steps are:

- **Isotypic preservation (Lemma 6).** A G-equivariant linear map between two representation spaces must send each isotypic component U_i (all copies of irrep ρ_i) into the matching isotypic component V_i.
- **Componentwise action (Lemma 7).** In Fourier coordinates it therefore acts separately on each matrix f̂(ρ_i).
- **Right multiplication (Lemmas 8–10).** By Schur's lemma II, the only allowable action on f̂(ρ_i) is right multiplication by an arbitrary matrix B_i. Left multiplication by B commutes with every ρ_i(g) only if B is scalar.
- **Back to convolution.** Right multiplication in every Fourier component is, by the convolution theorem, convolution with the filter whose Fourier transform is (B_1, B_2, …).

## Assumptions

- **Groups.** G is compact, so the Haar measure is unique, complete reducibility holds, the set of irreps R_G is countable and can be chosen unitary (App. A). The exposition and proofs take G finite or countable. ℝ², behind ordinary CNNs, is non-compact and is said to be "amenable … with small modifications" (footnote 1).
- **Field.** ℂ throughout, "because representation theory … is easiest to formulate over ℂ" (§4.1).
- **Network model.** An MFF-NN (Def. 1) is f_ℓ(x) = σ_ℓ(φ_ℓ(f_{ℓ−1})(x)), with φ_ℓ linear and σ_ℓ pointwise, and biases dropped.
- **Homogeneity.** Each index set X_ℓ is a transitive G-set, identified with G/H_ℓ by choosing an origin (boxed text, §4.1; App. A, Def. 6). The paper notes that the entries of an adjacency matrix are not a homogeneous space of S_n: the diagonal and off-diagonal parts are separate orbits (App. A).
- **Equivariance.** Def. 3 is layer-wise, with every layer f_ℓ transforming under the induced action T^ℓ.
- **Adapted irreps.** Prop. 1's proof takes the irreps of G "adapted" to H ≤ G, so that ρ|_H is block-diagonal with Q = I (App. C).

## Key results

- **Prop. 1 (sparsity).** For f: G/H → ℂ, [f̂(ρ)]_{*,j} = 0 unless column block j of ρ|_H is the trivial representation of H. The analogous row statement holds for H\G, and both hold for H\G/K. The proof (App. C) uses Lemma 2: Σ_{u∈G} ρ(u) = 0 for non-trivial irreducible ρ.
- **Prop. 2 (convolution theorem).** The Fourier transform of f ∗ g at ρ_i equals f̂(ρ_i)ĝ(ρ_i) for any combination of G, G/H, H\G and H\G/K (App. D, countable case).
- **Theorem 1.** For compact G and index sets X_ℓ = G/H_ℓ, the network N is G-equivariant iff it is a G-CNN, i.e. φ_ℓ(f) = f ∗ χ_ℓ with χ_ℓ on H_{ℓ−1}\G/H_ℓ. The forward direction is proved in §5 by the identity g⁻¹[uv⁻¹]_X = [g⁻¹uv⁻¹]_X. The reverse direction is in App. E.
- **Lemma 6 (isotypic preservation).** If φ is G-equivariant and U = ⊕U_i, V = ⊕V_i are the isotypic decompositions, then φ(U_i) ⊆ V_i.
- **Lemma 7.** The Fourier transform of f′ = φ(f) at ρ_i equals Φ_i(f̂(ρ_i)) for linear maps Φ_i.
- **Lemmas 8–10.** Φ_i is allowable iff Φ_i(M) = MB_i. Left multiplication by B is allowable only if B is scalar (Lemma 9, via Schur II).
- **§6.3 (message passing).** Permutation equivariance leaves one learnable scalar per Fourier component (n−p, p), 0 ≤ p ≤ ℓ. This is "a severe constraint" yet "richer than traditional MPNNs where the labels of the neighbors are simply summed".
- **§7, conclusion.** The authors "argue for Fourier space representations" for data with non-trivial symmetry.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Generalised convolution (Def. 4, Cases I–III) on quotient spaces yields G-equivariant layers | strong (proof) | §5 forward direction; short coset identity |
| C2 | Equivariance of such a network forces every linear layer to be a generalised convolution | moderate (proof sketch) | App. E; written for countable G and scalar channels; the pointwise-σ step is unjustified for non-injective σ; cross-reference slips |
| C3 | Convolution theorem f∗g ↦ f̂ĝ holds on groups and their quotient spaces | strong (proof) | Prop. 2, App. D (countable case); continuous case asserted |
| C4 | Fourier matrices of functions on G/H, H\G, H\G/K have fixed column/row sparsity patterns set by the trivial blocks of ρ|_H | strong (proof) | Prop. 1, App. C, assuming H-adapted irreps |
| C5 | Equivariant linear maps preserve isotypic components | strong (proof) | Lemma 6 via Schur's lemma I (Lemma 3) and Lemma 5 |
| C6 | Harmonic networks, spherical CNNs and MPNNs are instances of generalised convolution | informal argument | §6; the Worrall et al. nonlinearity is left "beyond the scope"; the S_n representation theory is "beyond the scope" |
| C7 | This is "the first time" the equivariance–convolution connection is stated at this generality | assertion | §1; Ravanbakhsh et al. 2017 (discrete groups) is named as close |
| C8 | Practitioners should use Fourier-space representations for symmetric data | informal argument | §7; no experiment |
| C9 | The results extend to continuous compact groups "straightforwardly" | assertion | §4.1, App. A, App. D |

## Method

This is pure theory, done in three steps:

- **Definitions.** Define lifting and projection between G and its quotients (boxed text, §4.1), then convolution on quotients.
- **Fourier transform.** Take the group Fourier transform with respect to a system of unitary irreps, and derive sparsity (Prop. 1) and the convolution theorem (Prop. 2).
- **Necessity.** For the reverse direction, combine Schur's lemmas I and II (Lemmas 3–4), irreducibility of images (Lemma 5), isotypic preservation (Lemma 6), componentwise action in Fourier space (Lemma 7) and the characterisation of allowable componentwise maps (Lemmas 8–10). Then invert the Fourier transform to get the filter.

## Concepts

- **Homogeneous space / quotient space.** X ≅ G/H once an origin x₀ is fixed; H is the stabiliser of x₀; [g]_X = g(x₀).
- **Lifting f↑G and projection f↓X.** These move functions between X and G.
- **Double coset space H\G/K.** It is where filters between G/H and G/K live.
- **Irreps, complete reducibility, multiplicity m_ρ(ρ′).** From App. A. The multiplicity is "a well-defined quantity" once R_G is fixed, and the paper compares R_G to "the primes in arithmetic".
- **Isotypic decomposition.** U = U₁ ⊕ U₂ ⊕ …, where U_i collects all copies of ρ_i (App. E).
- **Allowable map.** A componentwise Fourier map realised by some equivariant φ (App. E).
- **Group Fourier transform.** f̂(ρ_i) = Σ_u f(u)ρ_i(u), matrix-valued for non-commutative G. For commutative G all irreps are one-dimensional: SO(2) has ρ_j(θ) = e^{2πιjθ} (§6.1), and ℝ has the ordinary Fourier transform (App. A).

## Connections

- **Cohen & Welling ([LIT-314](../literature.d/LIT-314.md)).** It supplies the sufficiency direction for discrete plane groups in the regular representation. This paper generalises to compact groups and quotient spaces and adds necessity. It credits the term "equivariance" to Cohen & Welling 2016 (§1).
- **Bronstein et al. ([LIT-319](../literature.d/LIT-319.md)).** GDL §4.3 (p. 43) says "it is possible to show that any equivariant linear map f: X(Ω) → X(Ω′) … can be written as a generalised convolution", with no citation. This paper is the result that sentence rests on. GDL's bibliography cites other Kondor papers (Cormorant; the Lorentz-group network) but not this one (checked by search of the GDL bibliography).
- **Peter–Weyl ([LIT-329](../literature.d/LIT-329.md)).** Complete reducibility, the countable irrep system of a compact group and the completeness of matrix coefficients (needed for the inverse Fourier transform) are Peter–Weyl facts. This paper uses them without naming Peter–Weyl; it points to Serre (1977) and Terras (1999).
- **Pontryagin ([LIT-333](../literature.d/LIT-333.md)).** For abelian G the paper's Fourier transform reduces to characters, e.g. SO(2), §6.1. This is the Pontryagin-dual picture; the non-commutative generalisation is the paper's point.
- **Wedderburn ([LIT-309](../literature.d/LIT-309.md)) and Murota et al. ([LIT-352](../literature.d/LIT-352.md)).** Lemma 6's isotypic block structure of intertwiners is the representation-side version of the block decomposition that [LIT-352](../literature.d/LIT-352.md) computes numerically for a matrix *-algebra. In particular, the commutant of ρ(G) is ⊕ M_{m_i}(ℂ), acting on multiplicity spaces; that last statement is standard and my own, not in the paper.

## Bearing on the record

- **What the map's row 7 cites it for.** It is cited as the "closest owner of characters-and-irreps machinery in ML". The paper confirms half of that.
  - *Irreps: owned.* It is a good ML-facing source for irreducible representations, complete reducibility, multiplicity, **isotypic decomposition**, and Schur's lemmas I and II (Lemmas 3–4). Lemma 6 is the result §9.6's "sectors are isotypic components" needs: any operator intertwining the G-action maps each isotypic component into itself, so operators commuting with ρ(G) are block-diagonal on the isotypic sectors. The owner should cite Lemma 6 (or Serre) for that step.
  - *Characters: not owned.* The paper never uses characters. Its Fourier transform is matrix-valued, and the character-projection formula Π_t = (d_t/|G|) Σ_g χ_t(g)* ρ(g) that §9.6 displays is not here. The paper's Lemma 2 (Σ_u ρ(u) = 0 for non-trivial irreps) is the special case that projects onto the trivial isotypic component. For characters, cite a representation-theory text (Serre is the paper's own pointer), not this paper.
- **The spectral-degeneracy half of row 7 is not stated.**
  - *Available but unstated.* The paper does not say that a self-adjoint operator commuting with ρ(G) has eigenspaces that are G-subrepresentations, and so eigenvalue multiplicities that are sums of irrep dimensions. That fact is one step from Lemma 6 and Schur II, but it appears nowhere.
  - *The novelty consequence.* The owner's degeneracy-as-diagnostic is therefore not pre-empted by this paper. Nor is it new mathematics: it is the textbook Schur corollary, used as a symmetry detector in physics (standard, not verified against a source here).
  - *Precisions §9.6 needs.* Three follow from the machinery this paper does set out:
    - Symmetry implies degeneracy, not conversely. A degenerate eigenspace can be a sum of several irreps, or be accidental, so clump sizes "1, 1, 2, 3" identify no group.
    - An eigenspace dimension is a sum of irrep dimensions d_t, possibly with multiplicity. It is not "equal to d_t".
    - Abelian symmetries, including the Boolean cube's (ℤ/2)^n, give only one-dimensional irreps and so produce *no* degeneracy at all. The two halves of row 7 need different groups. See pam-[LIT-346](../literature.d/LIT-346.md) for a worked cube example.
- **The impose/detect contrast holds here.** G and its action on each layer's index set are inputs to Theorem 1. The theorem characterises architectures *constrained* to be equivariant. It never asks whether a trained, unconstrained network has become equivariant.
  - *Where the group acts.* As with [LIT-314](../literature.d/LIT-314.md), the group acts on the index sets of the layers, the input and feature *domains*. The owner's G acts on the representation space V itself and commutes with concept operators.
  - *The positioning sentence.* It should say this rather than only "they impose, we detect".
- **Connections to nucleation entries.** [THEORY-017](../theory.d/THEORY-017.md): the isotypic decomposition is intrinsic once ρ is given, but ρ itself is extra data supplied from outside the space. The bases within an isotypic component, which is how the paper picks a "system of irreps", are unique only up to the unitary freedom it states (App. A, "far from unique"). That matches [THEORY-017](../theory.d/THEORY-017.md). [LIT-329](../literature.d/LIT-329.md), [LIT-333](../literature.d/LIT-333.md), [LIT-309](../literature.d/LIT-309.md) and [LIT-352](../literature.d/LIT-352.md) are covered under Connections.
- **ML practice.** It carries a design prescription (use generalised convolution and Fourier-space features for symmetric data) but no evidence. It is a theory reference for the anthology, not a practice source. If filed there, it belongs beside, not under, the equivariance practices.

## Limitations

- **Scope of the theorem.** It covers only linear-then-pointwise architectures on transitive index sets. It says nothing about attention, gated or bilinear layers, or non-transitive domains (a general graph's adjacency; the paper itself notes the diagonal/off-diagonal split).
- **Proof coverage.** The necessity proof is for countable groups and scalar channels, and has the pointwise-σ gap and reference slips listed under corrections.
- **Continuous groups.** They are handled by assertion.
- **Examples.** The MPNN example needs S_n representation theory that the paper declares out of scope, and the Worrall et al. nonlinearity is not analysed.

## Open questions

- **ReLU.** Does the "only if" direction survive for non-injective pointwise nonlinearities, with equivariance imposed on post-activation layers only? A proof or a counterexample would settle whether "necessary" holds for ReLU networks.
- **Detecting approximate equivariance.** For an unconstrained trained network, how would one test whether some layer is approximately G-equivariant for an unknown G? The isotypic and Schur machinery here says what signatures an exact G-action leaves (block structure, and degeneracy for non-abelian G). It says nothing about estimating them from noisy weights, which is the owner's empirical problem.

## Corrections to the seeded skim

- Seeded from metadata and the abstract; the text agrees with the seed's summary. Venue and authors verified: Risi Kondor (Statistics and Computer Science, University of Chicago) and Shubhendu Trivedi (TTI-Chicago), ICML 2018, PMLR 80.
- The abstract's "(given some natural constraints)" hides four hypotheses:
  - *Transitive index sets.* Every layer's index set is a homogeneous space G/H_ℓ (Def. 5, Thm 1).
  - *Linear-then-pointwise layers.* Each layer is a linear map followed by a pointwise nonlinearity (Def. 1).
  - *Layer-wise equivariance.* Equivariance is required of every layer, each under its own induced action (Def. 3), not only input to output.
  - *Scope of the proofs.* They are for finite or countable G. The compact and continuous case is "straightforward" (§4.1, App. A, App. D), asserted and not shown.
- The "only if" proof (App. E) has gaps that the headline "necessary as well as sufficient" does not show.
  - *Scalar channels only.* It is written for scalar channels ("assuming Y_ℓ = ℂ"). The vector-valued case is called "straightforward".
  - *A circular opening.* It begins "Since N is a G-CNN", where "Since N is G-equivariant" is meant; as written it assumes the conclusion.
  - *The nonlinearity step.* It asserts that because σ_ℓ is pointwise, equivariance of σ_ℓ∘φ_ℓ "is equivalent to" equivariance of φ_ℓ. That holds when σ_ℓ is injective. For ReLU, σ(φ(T f)) = σ(T′φ(f)) does not let σ be cancelled, so the step needs another argument (my own observation).
  - *Cross-references.* It cites "Lemma 8" where Lemma 7 (Fourier components map componentwise) is meant, and the proof of Lemma 7 refers to "Section ??".
  - *Lemma 5.* It states that φ(W) is irreducible for irreducible W, which fails when φ(W) = 0. That case is harmless.
  - *Lemma 10.* Its proof is an informal composition argument.
- The paper uses matrix-valued irreps and Fourier matrices throughout. The word "character" occurs once, as "characteristic sparsity patterns" (§4.2). Characters, class functions and the character-projection formula for isotypic projectors do not appear. For row 7 this matters: the paper owns the *isotypic* machinery but not the *character* machinery (see Bearing).
- Identification: the map says bare "Kondor". This paper fits row 7's role well, because it is where Kondor ties equivariance to irreps, isotypic decomposition and Schur's lemma in an ML setting. The seed's alternatives (Kondor's 2008 thesis; Kondor, Lin & Trivedi 2018, Clebsch–Gordan nets, cited here as its ref. "Kondor, Lin, and Trivedi 2018") were not read, and the choice remains the owner's.
