---
number: 291
status: Skimmed
formerly:
- NOTE-tmpgnu6w
paper: LIT-346
title: 'Analysis of Boolean Functions'
version: 1
history:
- version: 1
  date: '2026-09-29'
  note: >-
    Read in part (The author's free arXiv edition, arXiv 2105.10386 v1 ("May
    2021 arXiv Edition", cs.DM, 21 May 2021; "Originally published April
    2014 by Cambridge University Press"), from the arXiv PDF, 419 PDF pages.
    Page numbers below are the book's own, which match the PDF pages.
    Book-length, so this is a partial reading. I read closely: the front
    matter and list of notation; all of Chapter 1 (Boolean functions and the
    Fourier expansion, §§1.1–1.7 with all exercises and notes, pp. 19–41);
    all of Chapter 2 (basic concepts and social choice: influences, total
    influence, noise stability and the noise operator T_ρ, the Laplacian L,
    Arrow's Theorem via Kalai, exercises and notes, pp. 43–68); §3.1 and the
    opening of §3.2 (spectral concentration; characters indexed by F̂₂ⁿ as a
    group, pp. 69–72); the Chapter 3 notes (p. 91, the Pontryagin-duality
    remark); and §8.5 on characters of finite abelian groups (Def. 8.51–Fact
    8.58 and Exercise 8.35, pp. 227–229, 241). The rest of the book
    (Chapters 3–11 otherwise: learning, DNF, majority and the CLT,
    pseudorandomness, property testing, generalised domains,
    hypercontractivity, invariance principle, Gaussian space) I did not
    read. I searched the whole text for irreducible, nonabelian, Schur,
    isotypic, multiplicit* and degenera*. The only hit was one
    "nondegenerate intervals" (p. 345, Gaussian surface area), which is
    unrelated.). The first NOTE on this paper, which was seeded from its
    abstract alone.
date: '2026-09-29'
summary: >-
  Every f: {−1,1}ⁿ → ℝ has a unique multilinear (Fourier–Walsh) expansion
  f = Σ_S f̂(S)χ_S over the parities χ_S(x) = ∏_{i∈S} x_i, which are an
  orthonormal basis (Thm 1.1, Thm 1.5) and are the characters of the group
  F₂ⁿ, χ_S(x+y) = χ_S(x)χ_S(y) (eq. 1.5; §3.2; §8.5). The central
  operators are all diagonal in this basis with eigenvalues depending only
  on |S|: the noise operator T_ρχ_S = ρ^{|S|}χ_S (Prop. 2.47) and the
  Laplacian Lχ_S = |S|χ_S (Prop. 2.37). Influence, noise stability and
  Arrow's Theorem (via Stab_{−1/3}) become statements about the Fourier
  weight at each level (Thms 2.20, 2.38, 2.49, 2.56).
---

# NOTE-291: Analysis of Boolean Functions

## Contribution

It is a graduate text built on one move. A function on the Hamming cube is expanded in the orthonormal basis of parity functions χ_S, and its combinatorial properties are "read off" from its Fourier coefficients (p. 26). Chapters 1–2 set up the basis and the basic formulas:

- **Plancherel and Parseval.** Parseval: ‖f‖₂² = Σ f̂(S)².
- **Convolution.** f̂∗g = f̂·ĝ (Thm 1.27).
- **Influences.** Inf_i[f] = Σ_{S∋i} f̂(S)² (Thm 2.20).
- **Total influence.** I[f] = Σ|S|f̂(S)² (Thm 2.38).
- **Noise stability.** Stab_ρ[f] = Σ ρ^{|S|}f̂(S)² (Thm 2.49).
- **Two applications.** The BLR linearity test (Thm 1.30) and Kalai's Fourier proof of Arrow's Theorem (Thm 2.56 and corollary).

## Key insight

The parity functions are simultaneously three things:

- **Monomials.** They are the monomials of the unique multilinear representation (§1.2).
- **An orthonormal basis.** They are orthonormal under the uniform measure, because χ_Sχ_T = χ_{S△T} and E[χ_S] = 0 for S ≠ ∅ (Facts 1.6–1.7).
- **Characters.** They are the characters of the group F₂ⁿ, and form a group isomorphic to it (eq. 3.1; the Chapter 3 notes call this "a special case of the theory of Pontryagin duality").

Operators that respect the cube's structure are therefore diagonal in this basis. For T_ρ and L the eigenvalue depends only on the *level* |S|, so every analytic quantity decomposes by degree.

## Assumptions

- **Domain and measure.** The domain is {−1,1}ⁿ ≅ F₂ⁿ with the **uniform** measure (Notation 1.4). Biased product measures and general product domains come in Chapter 8, which was not read beyond §8.5.
- **Scalars.** Real-valued functions (complex-valued in §8.5). Exercise 2.58 invites vector-valued f: {−1,1}ⁿ → V but does not develop them.
- **Encoding.** False/True ↔ +1/−1, chosen for the character property χ(b) = (−1)^b (p. 22).

## Key results

- **Thm 1.1.** Unique multilinear expansion f = Σ_S f̂(S)x^S.
- **Thm 1.5.** The 2ⁿ parities form an orthonormal basis of L²({−1,1}ⁿ) under ⟨f,g⟩ = E[fg].
- **Prop. 1.8.** f̂(S) = ⟨f, χ_S⟩.
- **Parseval and Plancherel.** Parseval ‖f‖₂² = Σ f̂(S)², so a Boolean-valued f has spectral sample S_f with P[S] = f̂(S)² (Def. 1.18).
- **Eq. 1.5.** χ_S(x+y) = χ_S(x)χ_S(y).
- **Thm 1.27.** The Fourier transform of f∗g at S is f̂(S)ĝ(S).
- **Thm 1.30 (BLR).** If the 3-query test accepts with probability 1−ε, then f is ε-close to a character.
- **Prop. 2.19.** D_i f = Σ_{S∋i} f̂(S)x^{S∖{i}}, and Thm 2.20: Inf_i[f] = Σ_{S∋i} f̂(S)².
- **Prop. 2.37.** Lf = Σ_S |S| f̂(S)χ_S. The Laplacian of the cube is diagonal in the characters with eigenvalue |S|. Thm 2.38 gives I[f] = Σ_k k·W^k[f]. The Poincaré inequality Var[f] ≤ I[f] is "equivalent to the spectral gap for the discrete cube graph" (notes, p. 68).
- **Prop. 2.47.** T_ρχ_S = ρ^{|S|}χ_S, so T_ρ f = Σ_k ρ^k f^{=k}. Thm 2.49 gives Stab_ρ[f] = Σ_k ρ^k W^k[f].
- **Ex. 2.32.** Semigroup property, T_{ρ₁}T_{ρ₂} = T_{ρ₁ρ₂}.
- **Prop. 2.50.** For unbiased f, Stab_ρ[f] ≤ ρ, with equality iff f = ±χ_i.
- **Thm 2.56 (Kalai).** P[Condorcet winner] = ¾ − ¾·Stab_{−1/3}[f]. This yields Arrow's Theorem, Guilbaud's ≈ 91.2%, the bound 7/9 + 2/9·W¹[f] (Cor. 2.59), and a robust Arrow via FKN (Cor. 2.60).
- **Ex. 1.30 (a).** The Fourier transform of f^π at S is f̂(π⁻¹(S)). Coordinate permutations permute characters *within a level*. Part (e) extends isomorphism to signed permutations g(x) = h(±x_{π(1)}, …, ±x_{π(n)}).
- **Prop. 2.22.** Transitive symmetry forces equal degree-1 coefficients, so a monotone transitive-symmetric f has Inf_i ≤ 1/√n.
- **§8.5 (Def. 8.52–Fact 8.58, Ex. 8.35).** For any finite abelian G the characters form an orthonormal Fourier basis of L²(G), exactly |G| of them, and they form the dual group Ĝ ≅ G.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The parities χ_S are an orthonormal basis of real functions on {−1,1}ⁿ, and every f has a unique Fourier expansion | strong (proof) | Thms 1.1, 1.5; Facts 1.6–1.7 |
| C2 | The parities are the characters of F₂ⁿ and form a group ≅ F₂ⁿ; this is a case of Pontryagin duality | strong (proof; cited framing) | eq. 1.5, eq. 3.1, p. 91 notes; the Walsh-functions-as-characters viewpoint is credited to Vilenkin (1947) and Fine (1949) (p. 40) |
| C3 | The noise operator and the cube Laplacian are diagonal in the characters, with eigenvalues ρ^{|S|} and |S| | strong (proof) | Props 2.47, 2.37 |
| C4 | Influence, total influence and noise stability are the level-weighted Fourier weights | strong (proof) | Thms 2.20, 2.38, 2.49 |
| C5 | A unanimous 3-candidate Condorcet rule that always has a winner is a dictatorship (Arrow) | strong (proof) | Thm 2.56 and its corollary |
| C6 | For all finite abelian G, characters give a Fourier basis and Ĝ ≅ G | strong (proof, part as exercise) | §8.5, Props 8.54–8.55, Fact 8.58, Ex. 8.35 |

## Method

Mathematical exposition. The methods are orthogonal expansion, probabilistic identities under the uniform measure, and operator diagonalisation. Proofs are complete for the results listed from Chapters 1–2. Several are left as exercises, e.g. Props 1.15, 2.24, 2.26, 2.37 and Ex. 8.35.

## Concepts

- **Character χ_S / χ_γ.** χ_γ(x) = (−1)^{γ·x}; a homomorphism F₂ⁿ → {±1}.
- **Fourier weight at degree k.** W^k[f]. The **degree-k part** is f^{=k}.
- **Influence, total influence, sensitivity.**
- **Noise operator T_ρ; noise stability; noise sensitivity.**
- **Laplacian L = Σ L_i.** Here Lf = Σ|S|f̂(S)χ_S.
- **Symmetric vs transitive-symmetric functions.** Invariant under all of S_n, or under a subgroup acting transitively on coordinates (Defs 2.8, 2.10); Aut(f) is the permutation-automorphism group (Ex. 1.30).
- **Spectral sample S_f.**

## Connections

- **Walsh 1923 ([LIT-300](../literature.d/LIT-300.md)).** The book's notes (pp. 39–40) trace the basis to Walsh's orthonormal ±1 system on [0,1] with Paley's ordering. They credit the character viewpoint on ℤ₂ⁿ to Vilenkin (1947) and Fine (1949), and the level-ordering by |S| to Bonami and Kiener. That confirms [LIT-300](../literature.d/LIT-300.md)'s seed claim that Walsh functions are the characters of (ℤ/2)ⁿ, with the attribution that the *character* reading is Vilenkin's and Fine's, not Walsh's.
- **Pontryagin ([LIT-333](../literature.d/LIT-333.md)).** The book explicitly places F̂₂ⁿ ≅ F₂ⁿ and Ĝ ≅ G as special cases of Pontryagin duality (p. 91 notes; §8.5).
- **Peter–Weyl ([LIT-329](../literature.d/LIT-329.md)).** It is not used. The book stays abelian, where Peter–Weyl reduces to the character basis.
- **Kondor & Trivedi ([LIT-305](../literature.d/LIT-305.md)).** Their App. A notes that abelian groups have one-dimensional irreps, so the matrix Fourier transform reduces to characters. This book is that reduced case, fully worked for the cube.
- **Stone ([LIT-353](../literature.d/LIT-353.md)) and the map's "tripod".** The Boolean *algebra* of subsets and the Boolean *cube* as a group are different structures. This book is about the second, harmonic analysis over F₂ⁿ. Stone duality is about the first. The map's §2.1 tripod joins them through "the concept/predicate duality", but nothing in the chapters read connects Stone representation to Fourier–Walsh analysis.

## Bearing on the record

- **What the map's row 7 cites it for.** It is cited as the "Boolean-Fourier/character machinery for predicate harmonics". The book owns exactly that, and the half of row 7 it supports should be marked `KNOWN`, not `SYNTHESIS`:
  - *The cube.* The Walsh–Hadamard basis is the characters of (ℤ/2)ⁿ (eq. 1.5, §3.2, notes p. 40).
  - *General finite abelian groups.* The same holds for them (§8.5).
- **What "predicate harmonics = characters" can mean, precisely.** In this book the characters are functions on the **input cube**, predicates of n binary attributes. In learning theory a Boolean function is "a 'concept' with n binary attributes" (p. 20).
  - *The Boolean reading.* The projector-lattice document §9.6 cites the Walsh expansion f = Σ f̂(S)χ_S from its own earlier chat. If "predicate harmonics" means the Fourier–Walsh expansion of predicates as Boolean functions of binary features, the identification is exactly this book, and it is textbook.
  - *The operator reading.* If "predicate harmonics" means the SVD/Mercer harmonics of concept *operators* on a representation space V (as §9.6 then uses them), the identification needs a group acting on V. For the cube that means V ≅ L²(F₂ⁿ) with the translation action, or some other realisation. That action is not supplied by the book or by the map.
- **The two halves of row 7 need different groups.** This is the book's most useful lesson for the owner, and I checked it myself.
  - *Abelian groups give no multiplets.* The cube's group F₂ⁿ is abelian, so every irrep is one-dimensional (a character). Under F₂ⁿ alone, each level-k space span{χ_S : |S| = k} splits into C(n,k) *distinct* one-dimensional characters. My numeric check, n = 4, gives ⟨χ,χ⟩ = C(n,k) on each level. **Abelian characters produce no multiplets, so they cannot be detected by degeneracy.**
  - *The book does exhibit degeneracies.* The eigenvalue ρ^k of T_ρ and k of L each have multiplicity C(n,k) (Props 2.47, 2.37).
  - *They come from a nonabelian group.* T_ρ and L also commute with coordinate permutations, and the full symmetry group is the hyperoctahedral group (ℤ/2)ⁿ ⋊ S_n: sign flips and permutations, the "signed permutations" of Ex. 1.30(e). My own check, n = 4, character inner product: each level-k space is an **irreducible** representation of this group, ⟨χ,χ⟩ = 1 for k = 0…4, of dimension C(n,k). So the cube's Laplacian degeneracies are a clean worked example of "degenerate multiplet = irrep of the full symmetry group". The example is mine; the book states the eigenvalues, not the representation theory.
  - *A subgroup gives the wrong count.* Under S_n alone the same level-k space is reducible (⟨χ,χ⟩ = min(k, n−k) + 1: 1, 2, 3, 2, 1 for n = 4), yet the eigenvalue is still C(n,k)-fold degenerate. Degeneracy multiplicities equal irrep dimensions only for the *full* symmetry group. Measured against a subgroup, or with accidental degeneracy, they are sums of irrep dimensions. The §9.6 phrase "multiplicities equal the d_t", and the reading "clumps of sizes 1, 1, 2, 3 are irrep dimensions", need this qualification.
- **For the positioning against equivariance.**
  - *Detection is intrinsic, but for level-structure, not characters.* The degeneracy-detection idea is well served by this example. The level structure (C(n,k)-fold degeneracy) is visible in the spectrum of T_ρ or L alone, with no basis chosen, and the spectrum is unitarily invariant ([THEORY-017](../theory.d/THEORY-017.md)'s intrinsic data). The individual characters inside a level are not: they are one of many bases of the eigenspace.
  - *What the test finds.* A degeneracy test would find the levels (the nonabelian irreps) and could never find the individual Walsh characters. Row 7's two slogans should not be presented as one mechanism: the characters are what degeneracy *cannot* see.
- **Other nucleation connections.** [THEORY-017](../theory.d/THEORY-017.md): the parity basis is intrinsic only relative to the cube's group structure, which is extra data. On the bare Hilbert space ℝ^{2ⁿ} it is one orthonormal basis among many, singled out by the translation action (Ex. 1.12's Hadamard matrix is the change of basis). [LIT-300](../literature.d/LIT-300.md) and [LIT-333](../literature.d/LIT-333.md) are under Connections.
- **ML practice.** It carries nothing directly for the anthology. Its learning-theory chapter (low-degree and Kushilevitz–Mansour algorithms, §3.4–3.5) is PAC-style theory about Boolean concepts, and was not read here.

## Limitations

- **Coverage of this reading.** It is partial (see `read:`). Statements about Chapters 3–11 rest on the table of contents, §3.1–3.2's opening, §8.5 and keyword search.
- **Abelian only.** The book is about abelian harmonic analysis on product spaces. It offers nothing on nonabelian representation theory, which is what "irrep multiplets" require.
- **Uniform measure.** Results are for the uniform measure in Chapters 1–2. Biased measures change the basis (Chapter 8, not read).

## Open questions

- **Which group?** For a trained model's concept operators, which group, if any, plays the role of (ℤ/2)ⁿ ⋊ S_n? That is, is there a natural "signed permutation of binary features" symmetry whose irreps (the levels) would show up as degenerate clusters, while the individual features (the characters) stay invisible to spectral methods?
- **Vector-valued harmonics.** Ex. 2.58 asks how much of the theory extends to vector-valued f: {−1,1}ⁿ → V. That is the natural setting for predicates whose "value" is an embedding. How much of Chapters 1–2 survives there is unverified here.

## Corrections to the seeded skim

- Seeded from metadata. The text agrees with the seed's summary: Fourier analysis of f: {−1,1}ⁿ → ℝ, influences, noise stability, hypercontractivity, and applications to learning, social choice, complexity and property testing (contents, pp. v–viii).
- Date: the arXiv front matter says "Originally published April 2014 by Cambridge University Press". The seed's 2014-06-05 may be the online or DOI date (unverified). The arXiv edition is dated May 2021 (v1, 21 May 2021).
- The seed tag `information-theory` is not supported by the chapters read (1–2). Whether later chapters (hypercontractivity, pseudorandomness) justify it is unverified. I have left the seed's tags unchanged.
- For row 7: the book's "characters" are the characters of *abelian* groups only. These are F₂ⁿ throughout, and ℤ_mⁿ and general finite abelian G in §8.5 (Def. 8.52: "a homomorphism … G → ℂ^×"). The book does not use irreducible representations of nonabelian groups, character tables, or degeneracy of spectra. The symmetric group appears only as coordinate permutations of functions (Ex. 1.30, Def. 2.8 "symmetric", Def. 2.10 "transitive-symmetric"), never through its representations.
