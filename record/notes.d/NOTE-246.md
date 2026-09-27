---
number: 246
status: Read
formerly:
- NOTE-tmps11ei
paper: LIT-272
title: 'Reasoning about Meaning in Natural Language with Compact Closed Categories and Frobenius Algebras'
version: 1
history:
- version: 1
  date: '2026-09-27'
  note: >-
    Read in full (The full text of arXiv 1401.5980 v1 (the only version),
    from the arXiv PDF, 21 pp. I read the abstract, §§1–8, all eight tables
    and the 38 references. `pdftotext` was not available in this session, so
    I extracted the text with PyMuPDF. The string diagrams of §§5–6 do not
    survive text extraction, so I reconstructed each one from its stated
    linear-algebraic closed form, and I checked those forms numerically
    myself (random 5-d tensors). I did not read the published chapter
    (Cambridge University Press, 2016). The arXiv v1 footnote says it is the
    text "to appear" there, but I have not checked it against the print
    version. For comparison I also read the experimental sections and
    abstract of the authors' earlier COLING 2012 poster (Kartsaklis,
    Sadrzadeh & Pulman, "A Unified Sentence Space for Categorical
    Distributional-Compositional Semantics: Theory and Experiments", pp.
    549–558), because the chapter's results turned out to repeat it.). The
    first NOTE on this paper, which was seeded from its abstract alone.
date: '2026-09-27'
summary: >-
  The paper sets the sentence space equal to the noun space (F(s)=F(n)=W).
  It then uses the basis-copying map σ: v_i ↦ v_i⊗v_i of the Frobenius
  algebra fixed by W's basis to lift corpus-built verb matrices Σ_i
  sbj_i⊗obj_i into rank-3 tensors. So a transitive sentence becomes
  sbj⊙(verb·obj) ("copy-subject") or obj⊙(verbᵀ·sbj) ("copy-object"), a
  vector in W. On the Grefenstette–Sadrzadeh verb-disambiguation set,
  copy-object gets Spearman ρ=0.172, against 0.168 (Kron), 0.163 (Multp),
  0.143 (copy-subject), 0.050 (additive) and an inter-annotator bound of
  0.620. On a 112-term definition-matching task the best F1 is 0.21
  (nouns) and 0.27 (verbs). No significance test is reported. The
  disambiguation numbers are identical to the authors' COLING 2012 paper,
  and the definition numbers are the same data re-reported.
---

# NOTE-246: Reasoning about Meaning in Natural Language with Compact Closed Categories and Frobenius Algebras

## Contribution

The chapter restates the categorical compositional distributional ("DisCoCat") model of Coecke, Sadrzadeh & Clark (2010) in three steps.

- **A functor.** It replaces the earlier product category Preg × FVect with a strongly monoidal functor F from the free pregroup on {n, s} to FVect restricted to tensor powers of one distributional space W (§3.3).
- **Frobenius copying.** It uses the commutative special Frobenius algebra that a fixed basis induces on W to turn verb and adjective tensors, built from a corpus one rank too low, into tensors of the rank the grammar requires (§6).
- **Existing models as special cases.** It shows that Mitchell & Lapata's multiplicative model, and a diagonalised form of Grefenstette & Sadrzadeh's Kronecker model, are special cases of this recipe (§6.3).

It then reports three experiments: verb disambiguation, transitive against intransitive sentences, and term/definition matching (§7). Relative to the authors' COLING 2012 paper, the new material is the functorial framing, the MixCpDl and Kron encodings, and the §7.2 experiment. The constructions and the other results were already there.

## Key insight

The paper declares that sentences live in the same space as nouns (F(s)=W). A transitive verb then needs a tensor in W⊗W⊗W, but the corpus supplies only a matrix Σ_i sbj_i⊗obj_i. The copying map σ fills the extra wire by duplicating one index along the diagonal. Contracted with its arguments, the sentence becomes a pointwise (Hadamard) product in the fixed basis: sbj⊙(verb·obj) or obj⊙(verbᵀ·sbj).

So the whole "Frobenius" apparatus, once evaluated, is elementwise multiplication in the context-word basis. The string diagrams are a notation for choosing which index to duplicate.

## Assumptions

- **The grammar.** A free pregroup on basic types {n, s}. The types are n for nouns, nʳ·s for intransitive verbs, nʳ·s·nˡ for transitive verbs and n·nˡ for attributive adjectives (§3.1).
- **The functor.** F(n)=F(s)=W, F(xˡ)=F(xʳ)=F(xˡˡ)=F(xʳʳ)=W, and the ε-reductions go to inner products (§3.3). This uses W*≅W, which the paper notes "is not natural" and holds "by fixing a basis" (§2).
- **One distributional space.** W has a fixed orthonormal basis, and sentence meaning, noun meaning and word meaning all live in it (§3.2).
- **The Frobenius algebra.** It is the one determined by W's basis: σ: v_i ↦ v_i⊗v_i, ι: v_i ↦ 1, μ: v_i⊗v_i ↦ v_i, with σ†=μ for an orthonormal basis (§4). The unit is printed as "ζ :: 1 ↦ v_i". Correctly it is 1 ↦ Σ_i v_i, and μ should read v_i⊗v_j ↦ δ_ij v_i.
- **Relational verbs.** Relational verb and adjective tensors are sums of tensor products of their corpus arguments: an intransitive verb is Σ_i sbj_i, a transitive verb Σ_i sbj_i⊗obj_i, an adjective Σ_i noun_i (§6). In §7.3 a verb in a subjectless verb phrase is Σ_i obj_i.
- **Corpus and vectors.**
  - *Corpus.* The BNC (its size is stated garbled as "six million sentences and one million words, classified into a hundred million different lexical tokens").
  - *Basis and weights.* The basis is the 2000 most frequent lemmas. Weights are P(c|t)/P(c), i.e. exponentiated PMI without a floor.
  - *Similarity.* Cosine similarity, called "cosine distance" (§7).

## Key results

### Categorical

- **Compact structure is preserved (§2).** A strongly monoidal functor between compact closed categories sends adjoints to adjoints: F(Aˡ) is left adjoint to F(A). The argument is the standard one-paragraph uniqueness-of-adjoints argument. It is stated as equality where it holds up to isomorphism.
- **The functor F (§3.3).** It is asserted to be strongly monoidal. The paper gives F on objects and on two example reductions. It does not check functoriality on the free pregroup. That pregroup is a partial order, so any two parallel morphisms are equal and must have equal images. I did not find a counterexample, and whether this causes trouble is unverified.
- **Spider normal form (§5).** Every connected diagram of Frobenius maps equals a "spider" determined by its numbers of inputs and outputs. This is cited (Coecke–Pavlovic–Vicary, Coecke–Paquette), not proved.

### Closed forms (§6)

I checked each of the following numerically.

- **CpSbj.** σ copies the row (subject) index: Σ c_ij n_i⊗n_j ↦ Σ c_ij n_i⊗n_i⊗n_j. The sentence is sbj⊙(verb·obj) (eq. 1).
- **CpObj.** σ copies the column (object) index. The sentence is obj⊙(verbᵀ·sbj) (eq. 2).
- **MixCpDl.** μ merges one copy of each wire, which keeps only the verb matrix's diagonal. With verb = Σ_i sbj_i⊗obj_i, the sentence is sbj⊙(Σ_i sbj_i⊙obj_i)⊙obj. The paper states that this construction relates subject and object properties "on identical bases" only.
- **Multp.** Three σ's and one μ on the verb's context vector give sbj⊙verb⊙obj. This is Mitchell & Lapata's multiplicative model exactly.
- **Kron.** From verb⊗verb with σ, σ, μ, the sentence is sbj⊙verb⊙verb⊙obj (eq. 3). This is the diagonal of Grefenstette & Sadrzadeh's (verb⊗verb)⊙(sbj⊗obj) sentence matrix, not that model itself. So "representable in our setting" (§6.3) holds for Multp, and only for a collapsed variant of Kron.
- **Order of application.** For a fully populated rank-3 verb, (verb·obj)ᵀ·sbj = (verbᵀ·sbj)·obj, so "the order of application does not actually play a role" (§6.2). This is correct, but it undercuts the paper's own framing. CpSbj and CpObj are two different rank-3 tensors, not two orders of applying one tensor. The paper picks CpObj partly because applying "the verb to the subject then to the object seems to provide better experimental results" on the evaluation dataset (§6.2).

### Experiments (§7)

- **Disambiguation (Table 2).** The dataset is Grefenstette & Sadrzadeh (2011). The paper does not state its size. COLING 2012 gives 200 entries (400 sentences) and 25 annotators rating on a 1–7 scale.
  - *Spearman ρ.* Addtv 0.050, Multp 0.163, MixCpDl 0.000, Kron 0.168, CpSbj 0.143, CpObj 0.172. The inter-annotator upper bound is 0.620.
  - *Mean cosine (High / Low landmark).* Addtv 0.90/0.90, Multp 0.67/0.60, MixCpDl 0.75/0.77, Kron 0.31/0.21, CpSbj 0.95/0.95, CpObj 0.89/0.90. Humans: 4.80/2.49.
  - *What the numbers show.* CpSbj and CpObj separate high from low landmarks on average not at all, or in the wrong direction. Only Multp and Kron have a High > Low gap.
  - *Significance.* None is tested.
- **Transitive against intransitive (Table 3).** "For 100 target verbs", each transitive sentence s_tr is compared with intransitive versions made by dropping the object.
  - *Errors.* sim(s_tr,s_hi) > sim(s_tr,s_it) in 7 of 93 cases (7.5%). sim(s_tr,s_lo) > sim(s_tr,s_it) in 6 of 93 (printed as 5.6%; 6/93 is 6.5%). An unrelated intransitive sentence beats the sentence's own intransitive version in 36 of 9900 (0.4%).
  - *Unexplained.* The paper does not say why the denominator is 93 rather than 100, or which composition model was used.
  - *Missing.* There is no baseline. The four-way ordering the paper sets out (s_it > s_hi > s_lo > s_u) is tested only pairwise against s_it.
- **Term/definition classification (Tables 6–7).** There are 112 terms (72 nouns, 40 verbs), each with 3 definitions. Each definition is assigned to the most similar term, and F1 is macro-averaged over terms.
  - *Nouns (P/R/F1).* Addtv 0.21/0.17/0.16, Multp 0.21/0.22/0.19, Reltn 0.22/0.24/0.21.
  - *Verbs (P/R/F1).* Addtv 0.28/0.25/0.23, Multp 0.31/0.30/0.26, Reltn 0.32/0.28/0.27.
  - *Main definition ranked first.* Nouns: Multp 26/72 (36.1%), Reltn 25/72 (34.7%). Verbs: Multp 15/40 (37.5%), Reltn 8/40 (20.0%).
  - *Main definition in the top five.* Reltn nouns 47/72 (65%).
  - *Not reported.* MRR is computed but not reported ("very close for the two models"). There is no significance test.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | A strongly monoidal functor between compact closed categories preserves adjoints | strong (standard) | Short argument via uniqueness of adjoints, §2; correct up to isomorphism |
| C2 | DisCoCat can be recast as a strongly monoidal functor F: Preg_F → FVect_W with F(n)=F(s)=W | moderate (assertion with examples) | Object map and two morphism examples, §3.3; functoriality on the posetal Preg_F is not checked; identifying the adjoints with W uses a basis-dependent, non-natural isomorphism, which the paper acknowledges |
| C3 | Any vector space with a fixed basis carries a commutative special Frobenius algebra whose σ copies and μ "uncopies" the basis | strong (cited) | Coecke–Pavlovic–Vicary [9], §4; the unit ζ is misprinted |
| C4 | Copy-subject and copy-object give sentences sbj⊙(verb·obj) and obj⊙(verbᵀ·sbj) without building rank-3 tensors | strong (derivation) | Eqs. 1–2; I checked them numerically |
| C5 | Mitchell & Lapata's multiplicative model and Grefenstette & Sadrzadeh's Kronecker model are representable in the setting | strong for Multp; overstated for Kron | §6.3: Multp is exact; Kron is recovered only as its diagonal, sbj⊙verb⊙verb⊙obj (eq. 3) |
| C6 | The Frobenius algebras "enable us to work in a single space in which meanings of words, phrases, and sentences of any structure live" (abstract) | weak (stipulation) | The single space comes from the choice F(s)=W; Frobenius maps only fill tensors of the required rank; everything is relative to one fixed basis |
| C7 | The copy-object model is "the most successful" for verb disambiguation | weak | ρ=0.172 against 0.168 (Kron) and 0.163 (Multp), with no test; the same numbers were in COLING 2012, where CpObj's gap from the relational S=N⊗N model was called insignificant; CpObj's mean High and Low cosines are 0.89/0.90 |
| C8 | Objects matter more than subjects for disambiguating these verbs | weak (informal argument) | Inferred from CpObj (0.172) beating CpSbj (0.143), with an intuitive gloss on write/publish/spell; no ablation or test |
| C9 | MixCpDl's poor result "conforms to the predictions of the theory" | weak (post hoc) | ρ=0.000; §6 states no such prediction, only that the construction drops cross-basis interaction |
| C10 | Transitive and intransitive sentences can be meaningfully compared; results "follow indeed our expectations" | weak | Table 3 error rates 7.5%, 6.5% (printed 5.6%), 0.4%; model unstated, denominators unexplained, no baseline; the shared subject factor may give much of the ordering by construction |
| C11 | The relational model gives the best definition-classification performance | weak; contradicted in part by its own tables | F1 margins 0.02 (nouns) and 0.01 (verbs); Multp has higher verb recall and more first-rank main definitions (Table 7) |
| C12 | The experiments "verify the theoretical predictions" (abstract, §1) | assertion | No predictions are stated in advance; the results are modest correlations and small F1 margins with no significance testing |
| C13 | The setting is "a robust and scalable base" for implementing Coecke et al. 2010 (§8) | assertion | Scalability rests on avoiding rank-3 tensors via closed forms (§6.2); robustness is not measured |

## Method

- **Build word vectors.** Noun vectors (and context vectors for all words) are BNC co-occurrence vectors over 2000 basis lemmas, weighted by P(c|t)/P(c).
- **Build relational tensors.** Tensors for verbs and adjectives are sums of tensor products of their observed arguments' vectors.
- **Lift to the grammatical rank.** Frobenius σ (and in some variants μ and ι) raises the relational tensor to the rank the pregroup type requires, choosing which index to copy.
- **Compose.** Apply the functor-image of the pregroup reduction, i.e. inner products (ε), and evaluate through the closed forms so that no rank-3 tensor is ever built.
- **Compare.** Take cosines between the resulting vectors in W, whatever the grammatical structure.

## Concepts

- **Strongly monoidal functor ("quantizing the grammar").** A structure-preserving map from grammatical types and reductions to vector spaces and linear maps. The paper likens it to Atiyah's definition of a TQFT as a monoidal functor Cob → FVect. The analogy is formal only.
- **Frobenius algebra on FVect.** (σ, ι, μ, ζ) as defined by the basis. The paper calls σ "copying" and μ "uncopying". For v ∈ W, σ(v) is the diagonal matrix of v. For z ∈ W⊗W, μ(z) is z's diagonal.
- **Relational matrix.** A verb's Σ_i sbj_i⊗obj_i over corpus occurrences. The paper treats it as a "weighted predicate", extending a Boolean relation to real weights (§6).
- **CpSbj / CpObj / MixCpDl / Kron / Multp / Reltn / Addtv.** Copy the subject index, copy the object index, keep the diagonal, diagonalised Kronecker, pointwise product of context vectors, relational (Σ obj_i for verb phrases), and vector sum (Table 1, §7.3).
- **Spider.** The normal form of a connected diagram of Frobenius maps.

## Connections

- **Basis dependence against the Hilbert-space IR programme.** Commutative special Frobenius algebras on finite-dimensional spaces correspond to choices of orthonormal basis (Coecke–Pavlovic–Vicary). The paper cites this as copying/deleting "of the basis" (§1, §4) and calls W*≅W "not natural" (§2). It never draws the consequence: every Frobenius-built sentence vector is a Hadamard product, so it depends on the basis of W. §3.2 allows that basis to be SVD "topics" as well as context words, and the two choices give different sentence meanings. I checked that a random orthogonal change of basis changes the cosine between a CpSbj sentence and its subject (0.008 against −0.53 in one draw). Van Rijsbergen's Geometry of IR ([LIT-262](../literature.d/LIT-262.md)) is the contrast. [NOTE-239](NOTE-239.md) records that every quantity that book computes is a trace or inner product and so is invariant under a joint unitary change of basis. The two programmes share the Hilbert-space vocabulary but differ exactly here: this paper's composition treats the context-word basis as privileged, "classical" data.
- **Same formalism as the process-theory contextuality work.** Schmid et al. ([LIT-003](../literature.d/LIT-003.md)) study diagram-preserving maps from a process theory into FVect_ℝ. Structurally that is what F is here: a monoidal functor from a compositional syntax into FVect. The kinship is formal only. This paper uses the categorical quantum-mechanics toolkit as notation for linguistic composition and makes no claim about quantum theory. It is not evidence about contextuality, so it bears on none of [THEORY-010](../theory.d/THEORY-010.md)..016.
- **Not the quantum-cognition programme.** Unlike Aerts et al.'s claim of quantum structure in LLM language ([LIT-270](../literature.d/LIT-270.md)), the paper claims nothing non-classical about meaning. "Quantizing the grammar" is a metaphor for the functor. So the record's criticism of contextuality claims about word-meaning data ([THEORY-013](../theory.d/THEORY-013.md)) does not apply.
- **Distributional meaning.** The paper's "meaning-as-use" justification of distributional vectors (§3.2) is the view that Grindrod et al. ([LIT-208](../literature.d/LIT-208.md)) defend philosophically against the instability objection. Their differential, neighbourhood-based reading of meaning is basis-free, while this paper's composition is not.
- **ML practice.** The count vectors used here (exponentiated PMI over 2000 context words) are what Baroni et al.'s "Don't count, predict!" ([ANTH-LIT-608](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-608.md)) and Levy, Goldberg & Dagan ([ANTH-LIT-607](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-607.md)) later compared against predictive embeddings. Levy & Goldberg ([ANTH-LIT-612](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-612.md)) tied the two families through PMI factorisation. The additive composition that is the weak baseline here (ρ=0.050) is the composition word2vec's phrase paper advertises, e.g. Russian + river ≈ Volga River ([ANTH-LIT-603](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-603.md)).
- **What came after.** Verified by search, content not read:
  - *Frobenius extensions.* The Frobenius machinery was extended to relative pronouns by Sadrzadeh, Clark & Coecke ("The Frobenius anatomy of word meanings I", Journal of Logic and Computation 2013; arXiv 1404.5278).
  - *DisCoCirc.* Coecke's DisCoCirc ("The Mathematics of Text Structure", arXiv 1904.03478) moves the programme from sentences to text circuits.
  - *lambeq.* Kartsaklis et al.'s lambeq (arXiv 2110.04236, 2021) is a Python library turning DisCoCat-style string diagrams into tensor networks and quantum circuits for "quantum NLP".
  - *Unverified.* Whether any of these revisited the basis dependence noted above.

## Bearing on the record

- **Theories.** No THEORY in nucleation is supported or contradicted. The paper's quantum vocabulary (compact closure, Bell states as η maps, "classical data" as Frobenius algebras, TQFT analogies) is borrowed formalism. It says nothing about quantum foundations or contextuality.
- **What is worth recording.** Two points. First, the "single meaning space" of DisCoCat with Frobenius algebras is a stipulation, F(s)=F(n)=W, together with a choice of basis. Second, its compositions reduce to basis-dependent Hadamard products. Anyone citing DisCoCat as a principled, basis-free geometry of meaning should know this.
- **ML practice.** It carries nothing. The empirical content is a 2012–2014 comparison of count-vector composition functions on small datasets, with correlations ≤0.172 and no significance tests. It has been overtaken by learned sentence encoders. It does not belong in the Anthology.
- **For filing.**
  - *Tags proposed.* `linguistics` first: compositional semantics of natural language. `mathematics` for the category theory. `representation-learning` because it builds and compares sentence representations, though count-based and not learned. `logic` for type-logical (pregroup) grammar. `philosophy-of-language` for the meaning-as-use and Montague-style predicative framing.
  - *Tags not proposed.* `quantum-foundations`: the paper borrows the categorical quantum-mechanics formalism and is not about quantum theory. `anthology-candidate`.

## Limitations

- **The results are recycled.** The disambiguation results and the definition-classification data duplicate COLING 2012. The chapter drops that paper's significance statement and its CONT baseline, and renames CpObj to Reltn for the definition task.
- **No significance testing.** The model ranking in Table 2 rests on differences of 0.004–0.029 in ρ, with no test. The model order in §6.2 was chosen partly on the evaluation data.
- **"Verification" is not shown.** No prediction is registered before the experiments. The MixCpDl "confirmation" is post hoc.
- **§7.2 is underspecified.** It does not name the composition model or explain the denominator of 93. It has one arithmetic error (6/93 printed as 5.6%) and no baseline, such as additive composition or subject-overlap alone.
- **Basis dependence is never discussed.** The Frobenius algebras exist only relative to W's basis. The paper cites this but does not discuss what it means for the meaning of the sentence vectors, or for its own suggestion that SVD topics may serve as the basis.
- **The categorical claims are thin.** They are standard facts or assertions. Functoriality of F is illustrated, not verified, and the Frobenius unit is misstated.
- **A small corpus-era setting.** 2000-dimensional BNC count vectors, and datasets of 200 sentence pairs and 336 definitions.

## Open questions

- **Basis invariance.** Is there a basis-invariant version of the S=N construction, or a principled way to choose the basis (e.g. the one that maximises some corpus criterion)? How much do CpSbj and CpObj results change under an SVD or random-rotation basis on the same task?
- **Significance.** Do the reported model differences survive a paired significance test, e.g. bootstrap over items, on the disambiguation set? Do they survive on larger modern benchmarks for verb-sense and sentence similarity?
- **Full tensors.** Do fully learned rank-3 verb tensors, in which the copy-subject/copy-object choice disappears (§6.2), outperform the Frobenius-lifted matrices? The paper names this as work in progress.

## Corrections to the seeded skim

- none (there was no seed or dossier for this work)
- Identification note for filing: the arXiv abstract page lists only v1 (23 Jan 2014, 30 KB), with no journal-ref and no DOI other than the arXiv DataCite DOI 10.48550/arXiv.1401.5980. The v1 footnote says the paper is "To appear in Chubb, J., Eskandarian, A. and Harizanov, V., editors, Logic and Algebraic Structures in Quantum Computing and Information (2014), Cambridge University Press". Crossref and Cambridge Core both have it as chapter 9, pp. 199–222, of *Logic and Algebraic Structures in Quantum Computing*, the editors as above, Cambridge University Press, DOI 10.1017/CBO9781139519687.011. The print date is 2016-02-26 and the online date 2016-06-05. Retailer listings give the series as Lecture Notes in Logic 45. The printed title drops "and Information". One search-engine summary dated the book 2013, which is wrong. I read the arXiv v1, not the chapter.
- The abstract says the experiments "verify the theoretical predictions". The body states no prediction in advance. The one outcome called a confirmation is MixCpDl's ρ=0.000, said to conform "to the predictions of the theory, as these were expressed in Section 6" (§7.1). But §6 only notes that this construction discards cross-basis information. It does not predict failure. The measured correlations are small (best ρ=0.172 against a human bound of 0.620). The gaps between the top three models (0.004–0.009) are reported without a significance test.
- The experiments are not new. Table 2's ρ values (0.620, 0.050, 0.163, 0.143, 0.172) are identical to COLING 2012 Table 1. That paper also says the copy-object model's difference from Grefenstette & Sadrzadeh's original relational model (ρ=0.21, or 0.195 when recomputed) is "statistically insignificant". The chapter omits that comparison and that caveat. Table 6's Recall columns (Reltn 0.24/0.28, Multp 0.22/0.30, Addtv 0.17/0.25) equal COLING 2012's "accuracy" figures for the same dataset. There the best model was called copy-object, and there was a further baseline (CONT, 0.09/0.07) that the chapter drops. Only §7.2 (transitive against intransitive) is new.
- §7.3 says "The relational model delivers again the best performance". That holds for nouns on F1 (0.21 against 0.19) and on verbs only by F1 0.27 against 0.26. On verbs, Multp has the higher recall (0.30 against 0.28), and its main definition ranks first more often (15/40, 37.5%, against 8/40, 20.0%; Table 7). The COLING version said so: Multp was "slightly better for verbs".
- The task prompt expected constructions for relative pronouns, and names like "Frobenius additive/multiplicative". This paper has neither. Its models are CpSbj, CpObj, MixCpDl, Kron, Multp, Reltn and the Addtv baseline (Table 1, §7.3). Relative pronouns are the subject of Sadrzadeh, Clark & Coecke's "Frobenius anatomy of word meanings I" (arXiv 1404.5278), not this paper.
- The abstract says the Frobenius algebras "enable us to work in a single space". In the body the single space is stipulated by the functor, F(n)=F(s)=W (§3.3). The Frobenius maps only supply verb tensors of the rank that stipulation requires (§6). And those maps exist only relative to the fixed basis of W.
