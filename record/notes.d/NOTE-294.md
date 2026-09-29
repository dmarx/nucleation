---
number: 294
status: Read
formerly:
- NOTE-tmpjm8we
paper: LIT-340
title: 'A theory of concepts and their combinations I: The structure of the sets of contexts and properties'
version: 1
history:
- version: 1
  date: '2026-09-29'
  note: >-
    Read in full (Full text of arXiv quant-ph/0402207 v1 (the only version,
    submitted 26 Feb 2004), from the arXiv PDF, 20 pp. The PDF is marked "To
    appear in Kybernetes, Summer 2004". I read the abstract, §1
    (introduction), §2 (the SCOP formalism and the 81-subject experiment,
    Tables 1–5), §3 (the lattices of contexts and properties, §§3.1–3.5), §4
    (summary and conclusions), the acknowledgments and all 73 references.
    Nothing was skipped. `pdftotext` was not available, so I extracted the
    text with PyMuPDF. The tables came through as columns of numbers, and I
    rebuilt them row by row. The closure bars in eqs. near (19), (22) and
    (31) did not survive extraction; I restored them from the surrounding
    sentences. I did not read the Kybernetes version of record (34(1/2),
    2005), and I have not checked it for changes.). The first NOTE on this
    paper, which was seeded from its abstract alone.
date: '2026-09-29'
summary: >-
  Aerts & Gabora model a concept as an entity with states that change
  under contexts, a "state context property system" (Σ, M, L, µ, ν). They
  report an 81-subject e-mail study in which 7 contexts shift the rated
  frequency of 14 exemplars of "pet" (for example dog 0.50 under "The pet
  is chewing a bone" against 0.12 in the unit context) and the
  applicability of 14 properties. They then *postulate* that contexts and
  properties each form a complete orthocomplemented lattice, and call the
  structure quantum-like because a state can be an eigenstate of e ∨ f
  without being one of e or of f (eq. 19). No theorem is proved, the
  lattice is not shown to be non-distributive or orthomodular, and the
  paper contains no Hilbert-space model and no treatment of combination;
  both are deferred to Part II.
---

# NOTE-294: A theory of concepts and their combinations I: The structure of the sets of contexts and properties

## Contribution

The paper sets up the vocabulary of the Brussels quantum-cognition programme for concepts. A concept is an entity that can be in *states*. *Contexts* change the state, and *properties* have state-dependent weights. Before this, prototype and exemplar theories gave each exemplar or property one typicality. Here a single exemplar's typicality and a single property's applicability are functions of the concept's state (§2.1).

- **Data.** It reports a questionnaire experiment with 81 subjects (§2.2). Seven contexts for "pet" (Table 1) produce significantly different frequency ratings for 14 exemplars (Table 2) and applicability ratings for 14 properties (Table 4), assessed by paired t-tests (Table 5).
- **Structure.** It then argues that the sets of contexts M and properties L each carry a complete orthocomplemented lattice (§§3.1–3.4). It is "quantum-like" in one precise sense: the eigenstates of a disjunction can exceed the union of the disjuncts' eigenstates (eq. 19).

Part I contains no Hilbert space, no numerical model and no combination of concepts; all three are deferred to Part II (its [21]).

## Key insight

Context-dependence is moved from the exemplar or property into the *state* of the concept, as a context acting on a physical system prepares a new state. Once contexts are "measurements" and the state is what they change, the partial order "stronger than" on contexts has meets ("and") and joins. The join is read as a "superposition context", "one of the contexts ei but we do not know which" (§3.1). Such a join can have eigenstates that are eigenstates of neither part. That surplus is the paper's whole mark of non-classicality.

## Assumptions

- **SCOP.** A concept is (Σ, M, L, µ, ν), with µ: Σ×M×Σ → [0,1] the transition probability that state p becomes q under context e, and ν: Σ×L → [0,1] the weight of a property in a state (§3). µ and ν are to be fixed by experiment, but neither is estimated here.
- **Contexts of the first kind (§3.2).** If e takes p to q, then q is an eigenstate of e, µ(q,e,q) = 1. The authors note that cognition has contexts that are not of the first kind and set them aside.
- **Order.** e ≤ f iff λ(e) ⊆ λ(f), where λ(e) = {p | µ(p,e,p) = 1} (eqs. 16–17). Likewise a ≤ b iff κ(a) ⊆ κ(b), where κ(a) = {p | ν(p,a) = 1} is the "Cartan map" (eqs. 28–30).
- **Completeness is assumed.** Every subset of M has an infimum and a supremum (§3.2, "We suppose").
- **Orthocomplementation is assumed.** It is given by axioms (20)–(22) and (32)–(34) and illustrated with "The pet does not run through the garden". That ⊥ is well defined on M, and that e ∧ e⊥ = 0 and e ∨ e⊥ = 1 hold, is asserted.
- **The model is a choice.** Whether a meet such as e1 ∧ e6 ("chewing a bone" and "is a fish") is 0 is a modelling decision, and different decisions give different SCOPs (§3.3).

## Key results

- **Experiment (§2.2, Tables 1–5).** There were 81 subjects, "friends and colleagues of the experimenters", answering by e-mail on 0–7 scales. Examples of the context shifts in relative frequency:

  | exemplar | e1 "chewing a bone" | unit context 1 | other |
  |---|---|---|---|
  | dog | 0.50 | 0.12 | — |
  | parrot | — | 0.07 | 0.63 under e5 "being taught to talk" |
  | goldfish | — | 0.10 | 0.48 under e6 "is a fish" |
  | guppy | — | 0.09 | 0.46 under e6 |

  Property weights shift too: "furry" is 0.66 under e1 and 0.23 under e4, and "feathered" is 0.08 under e1 and 0.84 under e5. The paper's example p-value is parrot e1/e2 = 6.30E-28. "In all but a few cases, the effect of context was highly significant." The full analysis is available only from the authors.
- **Complete lattice of contexts (§3.1).** It is motivated by examples (e7 = e9 ∧ e3), with the join defined as the "superposition context".
- **Quantum-like criterion (§3.2, eqs. 18–19).** λ(∧ᵢeᵢ) = ∩ᵢλ(eᵢ), but only ∪ᵢλ(eᵢ) ⊆ λ(∨ᵢeᵢ). The strict inclusion is argued from one example: the pet heard running and barking, for one of two reasons (p₁₁). λ(M) is said to be a closure space, "applying analogous techniques to those in [15] and [16]", and this is not proved here.
- **Orthocomplemented, not a complement (§3.3).** The ground state is an eigenstate of neither e3 nor e3⊥, so λ(e3) ∪ λ(e3⊥) ⊊ λ(e3 ∨ e3⊥). The logic is called "paracomplete".
- **Atoms (§3.3).** A worked toy lattice generated by e1, e2 and e6, with e1 ∧ e6 := 0, has 10 atomic contexts, which are listed.
- **Properties (§3.4).** The same structure for L. The "and" property is exact (eq. 24). The "or" property holds only one way (eq. 25), by the example "friendly or not friendly".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Context changes the rated frequency of a single exemplar and the applicability of a single property of "pet" | moderate (experiment) | §2.2, Tables 2, 4, 5. There are 81 convenience subjects and paired t-tests. Table 5 has p-values > 1 and four duplicated columns, and the full analysis is not published |
| C2 | The contexts of a concept form a complete lattice under "stronger than" | weak (assumption) | §3.1 motivates it by examples, and §3.2 "suppose[s]" it |
| C3 | The contexts and the properties each form a complete *orthocomplemented* lattice | weak (assumption) | §§3.3–3.4. The axioms (20)–(22) and (32)–(34) are stated and illustrated. Well-definedness of ⊥ on M is not shown |
| C4 | The structure is "quantum-like" because ∪λ(eᵢ) ⊊ λ(∨eᵢ) | moderate (one example) | §3.2, eq. 19 and the p₁₁ example. This establishes a non-classical *state space*, but not a non-distributive lattice (see Limitations) |
| C5 | λ(M) and κ(L) are closure spaces, and the closure adds exactly the superposition states | weak (cited or forward-referenced) | §§3.2, 3.4 cite [15], [16]. The superposition reading is deferred to [21] (Part II) |
| C6 | The theory resolves concept combination and the guppy effect | weak here (forward reference) | §§1, 2.1, 4. Nothing about combination is modelled in Part I |
| C7 | The structure is derived operationally "without any non-operational technical hypothesis" | unsupported | §4. It is contradicted by the "suppose" in §3.2 |

## Method

Operational-axiomatic, in the Geneva–Brussels quantum-logic tradition of Piron and Aerts (refs [1]–[7], [15]–[20], [50]–[57]). The method has three steps:

1. Collect the contexts, generate the states by applying every context to the ground state, and collect the properties (§3).
2. Order contexts by inclusion of eigenstate sets, and properties by inclusion of actuality sets.
3. Postulate completeness and an orthocomplement.

The experiment is a rating questionnaire (7 contexts × 14 exemplars, and 7 × 14 properties, on 0–7 scales), normalised to relative frequencies and weights and tested with paired two-sample t-tests.

## Concepts

- **State of a concept** — what a context changes. It is observed as the vector of exemplar frequencies and property weights. The **ground state** p̂ is the state under no particular context, operationalised as the unit context "The pet is just a pet".
- **Context** — "a goal or drive state, a previous lingering thought … or ones' physical surrounding". Here it is restricted to "aggregations of concepts", i.e. sentences.
- **Eigenstate / potentiality state** — p is an eigenstate of e iff µ(p,e,p) = 1. Otherwise p is a potentiality state for e, and e's action on it is "collapse".
- **Superposition context e ∨ f** — "one of the contexts … but we do not know which". It is the lattice join.
- **Weight ν(p,a)** — the renormalised applicability rating. A property is **actual** in p iff ν = 1.
- **Contextuality** — used in the sense that the state, and hence the statistics, depend on context. This is *not* Kochen–Specker contextuality, and the paper performs no test of it.

## Connections

- **Lineage.** Builds on Aerts's state–property systems and closure spaces ([5], [15]–[20]) and on Gabora & Aerts 2002 ([33], quant-ph/0205161, not read). It sets up Part II ([LIT-312](../literature.d/LIT-312.md)), which supplies the Hilbert-space model, the tensor-product combination and the pet-fish account.
- **The pet-fish problem.** It is Osherson & Smith 1981 ([48]). The paper cites the fuzzy-set failures ([72], [73], [49]) as motivation.
- **[LIT-270](../literature.d/LIT-270.md) (Aerts et al. 2025, Rejected).** The same group, twenty years on. The 2005 programme's "contextuality" is the state change context causes, which shows up as *shifting marginals*: "dog" goes from 0.12 to 0.50 when the context changes. [NOTE-243](NOTE-243.md) rejects [LIT-270](../literature.d/LIT-270.md) because its CHSH values come from tables whose marginals shift by up to 0.96 between contexts. Part I shows the lineage of that confusion. Here, marginal shift *is* the phenomenon the formalism is built to model, and it is called contextuality.
- **[THEORY-013](../theory.d/THEORY-013.md) / [LIT-264](../literature.d/LIT-264.md) (Contextuality-by-Default).** In Dzhafarov's terms, every effect in Part I's data is a context-dependent marginal, i.e. inconsistent connectedness or direct influence. That is exactly what Contextuality-by-Default separates *from* contextuality. So nothing in Part I is evidence of contextuality in [THEORY-012](../theory.d/THEORY-012.md)'s or [THEORY-013](../theory.d/THEORY-013.md)'s sense. Part I does not claim KS contextuality. Its word "contextual" means "state changes with context", and the two uses should not be conflated when the map lists this paper beside Abramsky–Brandenburger.
- **Van Rijsbergen ([LIT-262](../literature.d/LIT-262.md)).** Van Rijsbergen's IR book is contemporary (2004) and independent. There, relevance and predicates are projectors on a document space. Part I has no vector space at all.

## Bearing on the record

- **The map's role (§0, rows 1, 4; R1; must-cite).** The map names Aerts–Gabora 2005 as an owner of "concepts as states in Hilbert space, contexts as measurements, non-distributive concept combination". For Part I, the characterisation holds only in part.
  - *What it owns.* "Concepts as states, contexts as measurements": yes, this is where it is laid down for concepts (§2.1). The "orthocomplemented lattice of contexts/properties" as a proposal: yes, as an axiomatic proposal (§§3.3–3.4).
  - *What it does not own: a non-distributive or orthomodular concept lattice.* Part I never shows non-distributivity and never mentions orthomodularity. Its non-classicality criterion (eq. 19) is a property of the *state-to-eigenstate map λ*, not of the lattice. My check: in any Hilbert space, a set of mutually commuting projectors generates a *Boolean* lattice, yet the eigenstates of P ∨ Q strictly exceed those of P and of Q together (superpositions). Criterion (19) is therefore satisfied by Boolean lattices too, and cannot certify "non-Boolean concept logic".
  - *What it does not own: combination.* That, and "Hilbert space", are Part II.
  - *Suggested citation wording.* "Aerts & Gabora (2005, Part I) model a concept as an entity whose state is changed by context, and propose, by assumption, that its contexts and properties form complete orthocomplemented lattices."
- **The map's row 3 (FCA has no negation; the fix is an orthocomplement).** Part I is prior art for putting an orthocomplement on a *concept's* property set. But it only posits one, "not feathered", with no construction from data. For "the projector lattice is a cleaner resolution than weak-negation patches", Part I gives motivation, not machinery.
- **The map's §2 diagnosis ("the LRH is the single-context Boolean shadow").** Part I does not supply the multi-context non-Boolean object the diagnosis presupposes. It supplies the *idea* of contexts as measurements. Part II ([LIT-312](../literature.d/LIT-312.md)) is where the Hilbert model appears, and its fitted model turns out to be single-basis and Boolean (see pam-[LIT-312](../literature.d/LIT-312.md)).
- **[THEORY-012](../theory.d/THEORY-012.md).** No bearing. There is no global-section or Kochen–Specker content.
- **[THEORY-013](../theory.d/THEORY-013.md).** Consistent with it. Part I's data are exactly the context-dependent marginals Contextuality-by-Default excludes from contextuality. The paper makes no CHSH claim, so there is nothing for [THEORY-013](../theory.d/THEORY-013.md) to refute here.
- **ML practice.** It carries nothing. There is no instruction for practice, and it does not belong in the Anthology.

## Limitations

- **The lattice structure is posited, not derived.** Completeness is supposed, and the orthocomplement is postulated by axioms and illustrated by negated sentences. The paper does not show that the "not" of a context is itself in M with the required properties, nor that M is orthomodular or non-distributive.
- **The non-classicality criterion is weak.** "Quantum-like" rests on eq. (19), which Boolean projection lattices with superposed states also satisfy. The later distinctive quantum-logic property, the failure of distributivity or orthomodularity, is not addressed.
- **The empirical base is thin.** There were 81 convenience subjects, contacted by e-mail. Frequency and typicality are conflated by design ("rather than typicality values … we need frequency values", §2.1). The statistical analysis is not published ("can be obtained by contacting the authors"). Table 5 contains impossible p-values and duplicated columns, and the text misquotes Table 4.
- **Nothing is estimated.** µ and ν are to be "determined by means of well chosen experiments". The experiment measures only the ground and first-collapse states, and µ between arbitrary states is never measured.
- **The central claims are deferred to Part II.** Combination, the guppy effect and the Hilbert representation are all promised to [21].

## Open questions

- **Is the context lattice of a real concept orthomodular, or non-distributive?** What data would test it? Examples are e ∧ (f ∨ g) ≠ (e ∧ f) ∨ (e ∧ g) for sentence contexts, and order effects between non-commuting contexts. Later quantum-cognition work on conjunction and disjunction interference (Aerts 2009; Busemeyer & Bruza, [LIT-316](../literature.d/LIT-316.md); neither read here) is where such tests are said to appear.
- **Is the orthocomplement of a context well defined as a context at all?** "The pet does not run through the garden" has many instances. Why should it be the lattice complement of e3 rather than one of many pseudo-complements?
- **Does the corrected Table 5 support the significance claims?** Only a re-analysis of the raw data would settle it, and the raw data are not published.

## Corrections to the seeded skim

- Seeded from metadata; the text shows the summary is right in substance, with two precisions. (i) The seed says the paper "shows the sets of contexts and properties form a complete orthocomplemented lattice". The text motivates this by examples and then assumes it: "it is plausible to require" infima (§3.1), "We suppose that for any subset of contexts … there exists an infimum … and a supremum" (§3.2), and eqs. (20)–(22) and (32)–(34) state the orthocomplement axioms without deriving them. Nothing is proved. The closing claim that the derivation makes "no non-operational technical hypothesis" (§4) is contradicted by those "suppose" steps. (ii) The seed says the work shows how context changes typicality. That is the experiment's finding (§2.2), not a result of the formalism.
- Dates. arXiv v1 is 26 Feb 2004. The journal version is Kybernetes 34(1/2), pp. 167–191, 2005 (this journal reference is on the arXiv abstract page; the seed's DOI and pages were not checked against the publisher). Nucleation dates [LIT-270](../literature.d/LIT-270.md) by its first appearance ([ADR-002](../decisions.d/ADR-002.md)), so `published:` should arguably be 2004-02-26 rather than 2005-01-01. I left the seed's value below, and the owner should decide.
- Internal errors in the text. §3.4 gives the weight of a6 "can fly" as 0.57 in the ground state, 0.14 under e1 and 0.86 under e5, but Table 4 gives 0.52, 0.06 and 0.82. §3.4 says the weight of "property a4" falls under e4, where the table and the sense show a1 ("lives in and around the house", 0.94 → 0.42) is meant. §3.4 first glosses a15⊥ as "not feathered and able to swim" and then, correctly, as "not feathered or unable to swim". §2.2 says a high p-value means the difference "could be due to statistical fluctuations, hence a genuine effect of context"; the "hence" should be a negation.
- Table 5 (p-values). Three entries exceed 1 (spider e2/e3 5.96, hedgehog 3.48, guinea pig 1.31), which is impossible for a p-value. In the second block, the columns e2/1, e3/e4, e3/e5 and e3/e6 repeat the first block's e1/e5, e1/e6, e1/1 and e2/e3 entry for entry in every row (checked for all 14 exemplars), so at least four columns are copying errors. The significance claims in §2.2 cannot be checked from the table as printed.
- Table 2. The "freq" column is not a stated function of the "rate" column. In column e1 it is not even monotone in it: rabbit has rate 0.07 and freq 0.04, guppy has rate 0.14 and freq 0.01. So at least one entry is misprinted, or the normalisation is per subject and unstated.
