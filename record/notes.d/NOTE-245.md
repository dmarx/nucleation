---
number: 245
status: Read
formerly:
- NOTE-tmp1umwm
paper: LIT-273
title: 'Mathematical Foundations for a Compositional Distributional Model of Meaning'
version: 1
history:
- version: 1
  date: '2026-09-27'
  note: >-
    Read in full (The full text of arXiv 1003.4394 v1 (the only version;
    submitted 23 Mar 2010, 118 KB), from the arXiv PDF, 34 pp. I read the
    abstract, §§1–7, the acknowledgements, footnotes 1–7 and the 41
    references. `pdftotext` was not available in this session, so I
    extracted the text with PyMuPDF. The string diagrams of §§2–4 (the
    reduction "under-links", the cups and caps, and the does/not diagrams)
    do not survive extraction. Each one sits next to its symbolic form, so I
    reconstructed them from the algebra; the one diagrammatic step I relied
    on, eq. (7), I checked through the paper's own symbolic computation (p.
    24). I checked the §5 similarity numbers and the basis-invariance of the
    ε/η composition numerically myself. I did not see the published
    Linguistic Analysis text. The arXiv record calls v1 "to appear", and I
    have not checked it against print.). The first NOTE on this paper, which
    was seeded from its abstract alone.
date: '2026-09-27'
summary: >-
  The paper builds DisCoCat as a product category FVect × P of vector
  spaces and a free pregroup. A sentence's meaning is f(w₁⊗…⊗wₙ), where f
  is the linear map got by putting vector spaces in place of the pregroup
  types in the reduction p₁…pₙ ≤ s. The ε maps become inner products and
  the η maps become Σᵢ eᵢ⊗eᵢ. So "John likes Mary" is Σ_ijk
  c_ijk⟨v|vᵢ⟩⟨w_k|w⟩ sⱼ ∈ S, and "not" is the 2×2 swap matrix placed on
  the sentence wire. There is no theorem and no experiment. The sentence
  space S is shown only as 1- or 2-dimensional truth values, over a toy
  model with one basis vector per individual, and the paper says how
  neither S nor the verb tensors are to be built from data. Its headline
  similarity numbers (3/4, 1/4, 3/8) are unnormalised inner products.
  Under its own Definition 5.1 they are 0.949, 0.316 and 0.6.
---

# NOTE-245: Mathematical Foundations for a Compositional Distributional Model of Meaning

## Contribution

The paper proposes the categorical compositional distributional model of meaning, later called DisCoCat. Lambek's pregroup grammars and finite-dimensional real vector spaces are both compact closed categories. So pair each word's distributional meaning space with its grammatical type in the product category FVect × P, and use the linear-map image of the pregroup reduction to compute a sentence vector from the tensor of word vectors (§3.4–3.5).

It works two constructions by hand: a positive transitive sentence (§4.1) and a negated one (§4.2), on toy truth-valued spaces. It defines sentence similarity as the normalised inner product in S (§5). And it notes that replacing ℝ by the Boolean semiring gives FRel × P and a Montague-style relational semantics (§6).

It is explicitly a framework paper. It says "we only set up our general mathematical framework and leave a practical implementation for future work" (§1, p. 3), and "the mathematical setting needs to be implemented and evaluated, by running experiments on real corpus data" (§7).

## Key insight

- **The shared structure.** A pregroup reduction such as n·(nʳ s nˡ)·n → s is a composite of the compact closed structure's ε maps (the cups). FVect has the same maps. There ε: V⊗V → ℝ is the inner product and η: ℝ → V⊗V is 1 ↦ Σᵢ eᵢ⊗eᵢ.
- **The recipe.** Replace each type by its word's vector space. The same diagram then becomes a linear map that contracts the verb's tensor against its arguments.
- **Where the verb's meaning goes.** The verb is not a vector alongside its arguments. It is a tensor in V⊗S⊗W, a "function" from subject and object to sentence (pp. 17–18).
- **Why the result is comparable.** Because the sentence wire always ends in S, any two sentences can be compared by inner product. This is the stated fix for Clark & Pulman's (2007) role-tensor proposal, whose sentence vectors live in structure-dependent spaces (§1, §3.6).

## Assumptions

- **The grammar.** A free pregroup on basic types n (noun), s (declarative statement), j (infinitive) and σ ("glueing type"), from Preller's discourse work [30] (§2.2).
  - *Positive.* "John likes Mary" is n (nʳ s nˡ) n → s.
  - *Negative.* "John does not like Mary" is n (nʳ s jˡ σ)(σʳ j jˡ σ)(σʳ j nˡ) n → s.
  - *Lambek's switching lemma.* Cited in footnote 4, so that ε maps suffice for the reductions used.
- **The category.** FVect × P, taken strictly monoidal (justified by coherence, §3.1).
  - *Objects.* Pairs (V, p).
  - *Morphisms.* Pairs (f: V → W, p ≤ q), with none when p ≰ q.
  - *Compact closure.* Lifted "componentwise", stated as "easy to verify" (§3.4).
  - *Not a functor.* The paper does not use a functor, and there is no map sending each type to a space. Spaces are assigned per word (Definition 3.2 and step 2 of §3.5).
- **Self-duality of FVect.** Vˡ = Vʳ = V* = V. This is justified because "a fixed base canonically induces an inner-product" (p. 13). η is 1 ↦ Σᵢ eᵢ⊗eᵢ (eq. 4). ε is Σ c_ij vᵢ⊗wⱼ ↦ Σ c_ij⟨vᵢ|wⱼ⟩, which on a basis is the trace Σ cᵢᵢ (eq. 5). The text cites "equation 4" for ε; eq. 5 is meant.
- **Meaning spaces.** "We prefer to be flexible with the manner in which these vector spaces are built" (§3.5). Nouns get atomic distributional spaces and verbs get tensor spaces, but no construction is given for either the verb tensors or S.
- **The toy semantics of §§4–5.**
  - *Individuals as basis vectors.* V is spanned by men mᵢ and W by women fⱼ, one basis vector per individual. The paper itself calls this "a far too simple idealisation for practical purposes" (p. 19).
  - *S.* Either 1-dimensional (the vector 1 for true, the origin 0 for false; Example 1) or 2-dimensional ({|0⟩, |1⟩} for false/true; Example 1b).
  - *Verbs.* A verb is Σ_ij mᵢ ⊗ likes_ij ⊗ fⱼ with likes_ij ∈ {|0⟩, |1⟩}.
- **Function words.** They are set "manually and without consulting the document" (p. 21).
  - *"does".* S = J, and does = Σ_ij eᵢ⊗eⱼ⊗eⱼ⊗eᵢ = (1_V ⊗ η_J ⊗ 1_V) ∘ η_V, an identity built from η maps.
  - *"not".* not = Σᵢ eᵢ ⊗ (|01⟩+|10⟩) ⊗ eᵢ, the "name" of the swap matrix N = [[0,1],[1,0]]. This follows Preller & Sadrzadeh [31].
- **Semirings.** Matrices over any semiring form a compact closed category (§6, asserted). Footnote 7 defines a semiring as having "no additive nor multiplicative inverses". A semiring does not require them; it need not lack them, and ℝ is one.

## Key results

The paper states no theorem and gives no proof beyond worked calculations. Its results are definitions and worked examples.

### Definitions

- **Definition 3.1.** A meaning space is an object (W, p) of FVect × P.
- **Definition 3.2.** The meaning of a string is w₁⋯wₙ := f(w₁⊗⋯⊗wₙ). Here f = α[pᵢ \ Wᵢ] is the linear map "built by substituting each pᵢ in [p₁⋯pₙ ≤ x] with Wᵢ", and (f, ≤) is a morphism (W₁⊗⋯⊗Wₙ, p₁⋯pₙ) → (X, x). Because P is posetal, "[p₁⋯pₙ ≤ x]" names only *that* a reduction exists, not *which* one. The substitution is well defined only on a chosen reduction diagram. The paper does not remark on this.
- **Definition 5.1.** Two strings whose reductions reach the same type have degree of similarity m = ⟨f(w⃗)|f′(w⃗′)⟩ / (N·N′), the cosine.

### Positive transitive sentence (§4.1)

- **The map.** f = ε_V ⊗ 1_S ⊗ ε_W : V⊗(V⊗S⊗W)⊗W → S.
- **The closed form.** With Ψ = Σ_ijk c_ijk vᵢ⊗sⱼ⊗w_k, the sentence is f(v⊗Ψ⊗w) = Σⱼ(Σ_ik c_ijk⟨v|vᵢ⟩⟨w_k|w⟩) sⱼ, which the diagrams simplify to (⟨v| ⊗ 1_S ⊗ ⟨w|)|Ψ⟩. The paper prints the second bra as ⟨v|, and the Dirac form as ⟨ε_V^r| ⊗ 1_S ⊗ ⟨ε_V^r|; W and w are meant.
- **Examples 1 and 1b.** With John = m₃ and Mary = f₄, f(m₃ ⊗ likes ⊗ f₄) = likes₃₄, the correct truth value, in both the 1-d and the 2-d S.

### Negated transitive sentence (§4.2)

- **The map.** f = (1_S ⊗ ε_J ⊗ ε_J) ∘ (ε_V ⊗ 1_S ⊗ 1_J* ⊗ ε_V ⊗ 1_J ⊗ 1_J* ⊗ ε_V ⊗ 1_J ⊗ ε_W).
- **What the diagram shows.** Yanking the η-built "does" and "not" wires reduces the sentence to (ε_V ⊗ N ⊗ ε_W)(v⊗Ψ⊗w), i.e. N applied to the positive sentence's value (eq. 7). This uses the fact that the cup–cap configuration around "not" transposes N, and N is symmetric.
- **The full symbolic calculation.** It is given on p. 24 for readers "suspicious of our graphical reasoning", and yields |0⟩⟨1|like₃₄⟩ + |1⟩⟨0|like₃₄⟩.
- **Example 2.** "John does not like Mary" is |1⟩ iff like₃₄ = |0⟩.
- **The analogy.** The pictures are those of teleportation and entanglement swapping, where η and ε are Bell states and Bell effects (p. 23).

### Similarity (§5)

- **Examples 3–4.** With likes = ¾ loves + ¼ hates, "John likes Mary" is ¾ loves₃₄ + ¼ hates₃₄. Its negation swaps the coefficients: ¼ loves₃₄ + ¾ hates₃₄.
- **Examples 5–7, as printed.** loves/likes 3/4; hates/likes 1/4; loves/hates 0; does-not-love/does-not-like 3/4; does-not-like/loves 1/4; does-not-like/hates 3/4; does-not-like/likes 3/8.
- **The same pairs as cosines (Definition 5.1), my computation in the case John loves Mary.** 0.949, 0.316, 0, 0.949, 0.316, 0.949 and 0.6. The printed values are unnormalised inner products.
- **The paper's reading.** Example 7, which compares sentences of different grammatical structure, shows the approach "does not limit us to the comparison of meanings of sentences that have the same grammatical structure" (p. 27).

### Relations (§6)

- **The Boolean case.** Over (𝔹, ∨, ∧), matrices give "an isomorphic copy" of FRel.
- **Superposition.** Subsets of X are superpositions of their elements, and their "inner product" is 1 if they intersect and 0 otherwise.
- **Example 1 revisited.** In FRel × P, likes ⊂ V × {∗} × W, and f({m₃} × likes × {f₄}) = ∗₃₄ ∈ {{∗}, ∅}.

### Experiments

None. The paper reports no corpus, dataset, implementation or measurement. It defers all of them (§1, §4.1 p. 19, §7).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Pregroups and FVect are both compact closed, and a pregroup reduction is a composite of cups (ε maps) | strong (standard) | Standard facts, restated with the ε/η equations, §3.3; pregroup case "trivially satisfied" because the category is posetal |
| C2 | The compact closed structure lifts componentwise to FVect × P | moderate (assertion of a routine fact) | "It is easy to verify" (§3.4); the four structural morphisms are listed, not checked |
| C3 | The meaning of a sentence is f(w₁⊗⋯⊗wₙ), with f obtained by substituting spaces for types in the reduction | definition | Definition 3.2; well defined only relative to a chosen reduction diagram, which the posetal P does not record |
| C4 | For a transitive sentence, f(v⊗Ψ⊗w) = (⟨v| ⊗ 1_S ⊗ ⟨w|)\|Ψ⟩ | strong (derivation) | §4.1, p. 18; follows directly from eq. 5 (the paper's second bra is misprinted ⟨v\|) |
| C5 | Sentence meanings of any grammatical structure live in one space S and can be compared by inner product (abstract, §1) | holds by construction; stipulation | Every reduction to s ends in S; for negation this needs the stipulation S = J (§4.2); Definition 5.1 is restricted to same-type strings; how to build S from data is not given |
| C6 | "Not" built from η maps and the swap matrix negates the truth value of a transitive sentence | strong within the 2-d truth-value model | Diagrammatic argument (eq. 7) plus the full symbolic computation (p. 24); the paper itself says the matrix is "essentially two dimensional" and leaves a dimension-general negation open (§7) |
| C7 | "does" acts as an identity on the flow of information | strong (derivation) | does = (1_V ⊗ η_J ⊗ 1_V) ∘ η_V, and the snake equations remove it |
| C8 | "John loves Mary" and "John likes Mary" have degree of similarity 3/4; like/does-not-like 3/8, etc. | weak (arithmetic inconsistent with the paper's own Definition 5.1) | Values are unnormalised inner products; the cosines are 0.949 and 0.6; "always orthogonal" (loves₃₄ ⊥ hates₃₄) fails when neither relation holds |
| C9 | Restricting scalars to the Booleans gives a Montague-style Boolean semantics (abstract, §6) | weak (one example) | FRel is the Boolean-matrix category (standard); only Example 1 is redone; the representation theorem is future work (§7) |
| C10 | The categorical setting lets one "distinguish and reason about ambiguities" (§3, point 3) | unsupported; contradicted by the construction | P is posetal, so distinct reductions of one string are one morphism; no ambiguous example is worked |
| C11 | The approach overcomes Clark & Pulman's (2007) tensor proposal: it needs no role vectors, and sentences of different structure share a space | moderate (informal argument) | §1, §3.6; true of the design, but the price (unbuilt S and verb tensors) is not weighed |
| C12 | The same framework extends to ℕ or ℚ scalars ("degrees or probabilities of meaning") and to mixed states | assertion | §1 p. 3, §7; not developed |

## Method

- **Type the sentence.** Assign pregroup types to the words and find a reduction to s.
- **Assign spaces.** Give each word a vector space: atomic for nouns, a tensor product matching the type for verbs and function words.
- **Tensor.** Take the tensor of the word vectors.
- **Apply the reduction.** Apply the linear map obtained by reading the reduction diagram with ε ↦ inner product and identity wires ↦ identity maps. For function words, build their vectors from η maps and fixed small matrices.
- **Compare.** Take normalised inner products in S.

All computation in the paper is by hand, on toy truth-valued spaces.

## Concepts

- **Pregroup.** A partially ordered monoid in which every element has left and right adjoints: pˡ·p ≤ 1 ≤ p·pˡ and p·pʳ ≤ 1 ≤ pʳ·p (§2.2). Lambek's replacement for the Lambek calculus: p\q ↦ pʳ·q and p/q ↦ p·qˡ.
- **Compact closed category.** A monoidal category with ηˡ, εˡ, ηʳ, εʳ satisfying the four "yanking" equations (§3.3). FVect is the symmetric, self-dual case. A non-degenerate pregroup is "essentially non-commutative".
- **FVect × P.** The product category pairing meaning spaces with grammatical types. Grammar enters only as a proof that a morphism exists.
- **"From-meaning-of-words-to-meaning-of-a-sentence" map.** The linear map f of Definition 3.2.
- **Name of a linear map.** Ψ_f = Σᵢ eᵢ ⊗ f(eᵢ), the map-state duality used to encode "does" (the identity) and "not" (the swap) as vectors (p. 21).
- **Glueing type σ.** An extra basic type from Preller [30]. It lets the subject's information flow through the auxiliary and the negation to the verb.
- **Superposition in FRel.** A subset as the sum of its elements. Disjoint subsets are orthogonal (§6).

## Connections

- **Van Rijsbergen's Geometry of IR ([LIT-262](../literature.d/LIT-262.md), [NOTE-239](NOTE-239.md)).** The acknowledgements thank Keith van Rijsbergen, and the two works share the Hilbert-space vocabulary. The contrasts are exact.
  - *Negation.* Van Rijsbergen's negation is the orthocomplement in the subspace lattice, a non-truth-functional "choice negation" ([NOTE-239](NOTE-239.md), ch. 5). This paper's "not" is a fixed swap of two basis vectors of a 2-d truth space. The paper names orthogonal-subspace negation, via Widdows [41], as the candidate for a dimension-general version (§7), and does not adopt it.
  - *Basis.* [NOTE-239](NOTE-239.md) records that every quantity the book computes is invariant under a joint unitary change of basis. The ε/η composition here is too: I checked that orthogonal changes of V, S and W carry the sentence vector covariantly. That property is lost in the Frobenius-based sequel by Kartsaklis, Sadrzadeh, Pulman & Coecke (2014).
- **Categorical quantum mechanics, and the process-theory contextuality work.** The toolkit is Abramsky–Coecke categorical quantum mechanics [1, 7, 9], and §4.2 draws the teleportation analogy explicitly. Schmid et al. ([LIT-003](../literature.d/LIT-003.md)) study diagram-preserving maps from process theories into FVect_ℝ, which is structurally akin to reading a pregroup diagram in FVect. The kinship is formal only. The paper makes no claim about quantum theory and none about contextuality, so it bears on none of [THEORY-010](../theory.d/THEORY-010.md)..016. The quantum-cognition claims the record weighs (Aerts et al., [LIT-270](../literature.d/LIT-270.md); [THEORY-013](../theory.d/THEORY-013.md)) are a different programme: this paper asserts nothing non-classical about meaning.
- **Duality in category theory.** Corfield's survey ([LIT-115](../literature.d/LIT-115.md), [NOTE-141](NOTE-141.md)) places "Coecke's cups and caps", the internal adjunctions of finite-dimensional vector spaces with their duals, among the category-theoretic dualities. The ε/η maps here are exactly those cups and caps, and the pregroup adjoints pˡ, pʳ are the posetal instance.
- **Distributional meaning in philosophy of language.** §2.1's Firthian justification ("you shall know a word by the company it keeps") is the distributional hypothesis whose holism Grindrod et al. ([LIT-208](../literature.d/LIT-208.md), [NOTE-158](NOTE-158.md)) defend. Their "differential", rotation-surviving reading of similarity fits the orthogonal invariance of this paper's composition. It does not fit the toy semantics, where each basis vector is an individual.
- **Lattice and Boolean structure.** §6's move from vectors to relations (disjoint subsets orthogonal, inner product as non-empty intersection) is the Boolean end of the spectrum that the Lattice Representation Hypothesis reading ([LIT-267](../literature.d/LIT-267.md), [NOTE-240](NOTE-240.md)) examines for LLM concept geometry. The paper stops at the observation, and the representation theorem is future work.
- **The follow-up filed with it.** Kartsaklis, Sadrzadeh, Pulman & Coecke (2014) keep the ε-contraction and recast FVect × P as a strongly monoidal functor from the free pregroup to FVect, with F(n)=F(s)=W. They add Frobenius copying to build verb tensors from corpus data and supply experiments. From this paper they take the reduction-as-linear-map recipe, the verb-as-tensor typing, and the goal of one space for all sentences. The Grefenstette & Sadrzadeh (2011) work cited there supplied the first corpus construction of verbs and the first evaluation. I verified that by the sequel's own account and have not read it.
- **ML practice (ANTH).** §2.1's count vectors ("the vector for dog … is (6,5,7)", weighted per footnote 1) are the count models that Baroni et al.'s "Don't count, predict!" ([ANTH-LIT-608](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-608.md)) and Levy, Goldberg & Dagan ([ANTH-LIT-607](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-607.md)) later compared with predictive embeddings, and that Levy & Goldberg ([ANTH-LIT-612](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-612.md)) tied to them through PMI factorisation. The Clark–Pulman lineage cited here runs to Smolensky & Legendre's tensor-product representations [39]. The anthology holds no entry for those or for compositional distributional semantics (a grep for pregroup, DisCoCat, compositional semantics and tensor network in its literature, theory and practice directories found none).

## Bearing on the record

- **Theories.** No THEORY in nucleation is supported or contradicted. The quantum vocabulary (Bell states as η, teleportation pictures, "superposition" in FRel) is borrowed formalism. The paper is not about quantum theory, so `quantum-foundations` is not proposed.
- **What is worth recording.**
  - *The sentence space.* DisCoCat's "single sentence space" is a design stipulation, not a theorem. This first paper never says how S is built from data. Its only S's are truth-value spaces of dimension 1 or 2.
  - *Basis.* The original ε/η model is invariant under orthogonal changes of basis. The basis dependence that the df1 reading documents enters with the later Frobenius machinery. The record should not attribute it to DisCoCat as such.
  - *Ambiguity.* Pairing with a posetal pregroup loses the identity of the reduction. So the categorical "reasoning about ambiguity" promised in §3 is not delivered by this construction.
- **ML practice.** It carries nothing. It has no implementation or data, and the count-vector setting it presupposes has been overtaken. It does not belong in the Anthology.
- **For filing.**
  - *Tags proposed.* `linguistics` first: the compositional semantics of sentences, with pregroup syntax as linguists pose it. `mathematics` for compact closed categories and the diagrammatic calculus as the framework. `logic` for type-logical grammar, Montague-style Boolean semantics, and negation as a logical operator. `philosophy-of-language` for the symbolic-against-distributional theories of meaning and the Firthian meaning-as-use premise.
  - *Tags not proposed.*
    - `representation-learning`, which the df1 reading used: its gloss is how *learned* systems come to represent data, and this paper learns nothing.
    - `information-retrieval`: named only as a future application.
    - `quantum-foundations`.
    - `anthology-candidate`.

## Limitations

- **No theorem and no experiment.** Every result is a definition or a hand computation on a model where each individual is a basis vector.
- **The central objects are left unbuilt.** The verb tensors "would be obtained automatically from data using some suitable method" (p. 20). The sentence space S has no general construction and no dimension, except truth values.
- **The categorical framing is thin.** FVect × P does not constrain f to match the reduction: any pair (f, ≤) is a morphism. The pairing of meaning to grammar lives in the informal substitution of Definition 3.2, not in the category. Posetality erases which reduction was used.
- **Negation is two-dimensional and truth-functional.** It works only when S is the 2-d truth space. The authors say so (§7).
- **The §5 numbers are misreported** against Definition 5.1, as unnormalised inner products. The orthogonality of loves/hates rests on an unstated assumption that exactly one relation holds.
- **Typographical slips.** T for V⊗S⊗W (pp. 17, 19); the second bra ⟨v| for ⟨w| (p. 19); "equation 4" for eq. 5 (p. 13). The semiring footnote is wrong (footnote 7). "Pregorup" is misspelt (p. 5). The journal-ref reads "Festschirft".

## Open questions

- **Building S.** How should S be built from corpus data, and of what dimension, so that inner products in S track human sentence similarity? The sequel's S=N and Grefenstette & Sadrzadeh's relational S=N⊗N are two answers. Neither is derived from this paper's framework.
- **Negation in general.** Is there a dimension-general negation compatible with the ε/η composition? For example, Widdows-style orthogonal projection, which §7 names, or the orthocomplement of van Rijsbergen ([LIT-262](../literature.d/LIT-262.md)).
- **Keeping the reduction.** Replacing the posetal P with a free compact closed category (or 2-category) on the types would keep distinct reductions distinct and make Definition 3.2 a genuine functor. Does that deliver the promised treatment of syntactic ambiguity?
- **The Boolean case.** Does the claimed Boolean-semiring representation theorem hold, and which Montague "non-logical" axioms appear at that level (§7)? Unverified whether any later work proved it.

## Corrections to the seeded skim

- none (there was no seed or dossier for this work)
- Identification for filing. The arXiv abstract page lists only v1 (23 Mar 2010). Its comment is "to appear" and its journal-ref reads "Lambek Festschirft [sic], special issue of Linguistic Analysis, 2010". Primary class cs.CL; cross-lists cs.LO and math.CT. The only DOI is arXiv's DataCite 10.48550/arXiv.1003.4394, and a Crossref bibliographic search found no DOI for the published article, so none is given. The volume and pages, Linguistic Analysis 36, 345–384 (eds. J. van Benthem, M. Moortgat, W. Buszkowski), come from the authors' own later citation (ref. [10] of Kartsaklis, Sadrzadeh, Pulman & Coecke, arXiv 1401.5980), not from the journal itself. The issue number is unverified. That later citation, like several others, gives the title as "Mathematical Foundations for Distributed Compositional Model of Meaning". The arXiv title is "…for a Compositional Distributional Model of Meaning".
- The abstract says "meanings of whole sentences live in a single space, independent of the grammatical structure". That is true by construction, because every string that reduces to s is sent into the same S. But it is a design decision, not a finding. In the negative example it holds only because the paper stipulates S = J for "does" (§4.2). And Definition 5.1 compares only strings whose reductions end in the same type. Footnote 6's "common dummy space" for other types is not described.
- The abstract says a Montague-style Boolean semantics "results" from restricting scalars to the Booleans. The body shows one worked example (Example 1 revisited, §6). The representation theorem that would establish it is listed as future work (§7).
- §3 says the categorical setting "will, for instance, allow us to distinguish and reason about ambiguities in grammatical sentences". The framework as set up cannot. P is posetal (§3.3: "there can only be one morphism between any two objects"), so two different reductions of one string to s are the same morphism of FVect × P. The meaning map f of Definition 3.2 has to be read off a chosen reduction diagram, which is not part of the category.
- §5, Examples 5–7. The stated "degrees of similarity" are not the normalised quantity of Definition 5.1. like₃₄ = ¾|1⟩ + ¼|0⟩ has norm √10/4. So the cosines are 0.949 (loves/likes, printed 3/4), 0.316 (hates/likes, printed 1/4) and 0.6 (does-not-like/likes, printed 3/8). The paper says it "implicitly normalize[s]" but divides by |loves₃₄|² only. The claim that loves₃₄ and hates₃₄ "are always orthogonal" also holds only if exactly one of the two relations holds. If John neither loves nor hates Mary, both are |0⟩ and the two sentences have similarity 1.
- Compared with the df1 reading of Kartsaklis, Sadrzadeh, Pulman & Coecke (2014), df1 misstates nothing about this paper. Its "earlier product category Preg × FVect" is this paper's FVect × P with the factors swapped. Three scope points are worth adding. (1) Here S is a separate space from the noun spaces, and subject and object may even live in different spaces (V for men, W for women, §4.1). F(s)=F(n)=W is the later paper's stipulation. (2) This paper has no Frobenius algebras. Its composition uses only ε and η, which are invariant under an orthogonal change of basis applied consistently (checked numerically). So df1's point that DisCoCat compositions reduce to basis-dependent Hadamard products applies to the Frobenius variant, which is how df1 scopes it, not to the 2010 model. (3) df1's worry about functoriality on a posetal pregroup is already present here, in sharper form (previous bullet).
- The paper has no relative pronouns, adjectives or intransitive verbs. Its only constructions are the positive transitive sentence and the negated transitive sentence ("does not").
