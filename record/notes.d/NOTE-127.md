---
number: 127
status: Read
formerly:
- NOTE-tmpgb34d
paper: LIT-107
title: 'Holik et al. — Quasi-set theory for a quantum ontology'
version: 2
history:
- version: 2
  date: '2026-09-26'
  note: >-
    Read in full (full text of the authors' preprint "Quasi-set theory for a
    quantum ontology of properties" (dated September 24, 2021; 26 pp.),
    PhilSci-Archive 19725, file "QST for a quantum ontology of
    properties-final.pdf". Read all of it: §§1–7, footnotes 1–5 and the
    references. The Synthese version (200(5), art. 401, 2022, retitled
    "Quasi-set theory: a formal approach to a quantum ontology of
    properties") is paywalled and was not read; Springer's page shows "Open
    Access: N". It may differ from the preprint.). Upgraded from `Skimmed`
    to `Read`: the claims table, assumptions and results are new, and the
    skim is corrected where the full text disagreed.
date: '2026-09-26'
summary: >-
  The paper argues, with no new theorem, that the Lombardi–da Costa
  ontology of properties for quantum mechanics can be stated in Krause's
  quasi-set theory Q. On that ontology a system is a bundle of
  I-type-properties (instances of universal type-properties, represented
  by the algebra of observables) with no principle of individuality. For
  each property instance, the indiscernible instances form a qset U([Π]).
  An atomic bundle is any qset x with qc(x ∩ U) = 1 for each U; the Axiom
  of Choice in Q guarantees one exists. The bundle's kind is Q(B) = {x ∈
  P(Q) | R(x)}, whose members are all indiscernible. N particles are a
  subqset N(B) ⊂ Q(B) with qc = N, a definite number with no labels (§6,
  pp. 19–22).
---

# NOTE-127: Holik et al. — Quasi-set theory for a quantum ontology

## Contribution

The paper supplies a formal meta-language for an existing quantum ontology of properties (Lombardi & Castagnino 2008; da Costa et al. 2013; da Costa & Lombardi 2014; Lombardi & Dieks 2016). Standard logic and set theory presuppose individuals, and so cannot express "a bundle of property-instances that is not an individual". The authors show how quasi-set theory can: indiscernible property-instances become qsets, bundles are built by choice, and pluralities of indiscernible bundles get a definite quasi-cardinal without labels.

## Key insight

Quasi-set theory was built for indistinguishable particles understood as non-individuals, but it is purely formal. So it can be reinterpreted over any items whose logical behaviour matches it. Applied to property-instances, which the authors hold are only numerically distinct, it formalises bundles. Particle indistinguishability then becomes a derived relation, inherited by bundles from the indiscernibility of their components, rather than a primitive fact about particles.

## Assumptions

- **Algebraic priority.** Formalisms are not ontologically neutral. The algebraic formalism, where observables come first and states are functionals ω: A → ℂ, "evokes" an ontology of properties, while Hilbert space evokes individuals (pp. 2–3).
- **Universals, not tropes.** The elemental items are universal type-properties and their instances, which are indistinguishable, "only numerically different" (p. 5).
- **Bundles are not individuals.** No principle of individuality holds, and composition does not preserve component identity (p. 6).
- **Possibilism.** Possible case-properties are real; probabilities measure irreducible propensities (p. 6).
- **Q's axioms.** First-order logic without identity. Primitives m, M, Z, ∈, ≡, qc. Indiscernibility ≡ is an equivalence relation but not a congruence; substitutivity holds only for classical items (=). Extensional identity =_E is defined only for sets and M-atoms. The Weak Extensionality axiom holds, and a quasi-set version of Choice (pp. 12–19).
- **Galilean kinds.** Each irreducible representation of the Galilean group, labelled by (m, w, s) via the Casimir operators M = mI, W = wI, S = s(s+1)I, represents a kind of elementary particle (p. 20).
- **Spectral decomposition.** Without loss of generality, each I-type-property [A] is replaced by the projector-properties [Π_k^A] (p. 21).

## Key results

- **§3.1 (p. 7).** Kochen–Specker blocks value-definiteness for all I-type-properties, but a system is defined as a bundle of determinables. So "the proposed ontology of properties is immune to the challenge represented by the Kochen-Specker theorem".
- **§3.2 (pp. 7–8).** The components of a composite bundle do not keep their identity, so EPR correlations are "correlations between properties of a single item and, thus, the mystery of the original formulation vanishes".
- **§3.3 (pp. 8–10).** Indistinguishability holds primarily between I-type-properties of the same U-type with the same P-case-properties, and derivatively between bundles. PII "does not apply" because it concerns individuals. The Indistinguishability Principle follows if only symmetric observables are allowed.
- **§4 (pp. 10–11).** "An ontological domain populated exclusively by properties and non-individual bundles … cannot be adequately apprehended by any language that includes individual constants and variables" (p. 11). This agrees with French & Ladyman's complaint about logic and set theory. French (2020) notes the view is close to OSR.
- **§5 (pp. 11–19).** An exposition of Q: Definitions 1–5, including weak ordered pairs, quasi-relations and quasi-functions, which map indiscernibles to indiscernibles; axioms (≡1)–(=4), (∈1)–(∈11), (qc1)–(qc7) and Weak Extensionality (≡12); Theorem 7, invariance under permutations, with (x − `[[z]]_t`) ∪ `[[w]]_t` ≡ x; the Axiom of Choice in Q. Q does not prove the substitutivity of indiscernibles: Q ⊬ a ≡ b → ∀z(a ∈ z ↔ b ∈ z) (p. 18).
- **§6 (pp. 19–22).** An atomic bundle has (i) at most one I-type-property per U-type, (ii) always [M], [W], [S], and (iii) each of these with a single P-case-property. For each [Π] there is a qset U([Π]) of indiscernible instances, assumed to have denumerable quasi-cardinal. R(x) says qc(x ∩ U([M])) = qc(x ∩ U([W])) = qc(x ∩ U([S])) = 1 and ∀Π qc(x ∩ U([Π])) = 1. Then Q(B) := {x ∈ P(Q) | R(x)}, and Choice gives Q(B) ≠ ∅. Any x, y ∈ Q(B) satisfy x ≡ y. N indistinguishable particles are N(B) ⊂ Q(B) with qc(N(B)) = N.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Formalisms that are mathematically equivalent can suggest different ontologies (Peano vs Russell; Hilbert space vs algebraic) | weak | illustrative argument, pp. 2–3 |
| C2 | The ontology of properties is immune to Kochen–Specker | moderate (by definition) | §3.1. It follows from defining systems as bundles of determinables. The dissolution is definitional |
| C3 | Non-separability's "mystery vanishes" for non-individual composite bundles | weak | informal argument, §3.2. The correlations are relocated, not explained |
| C4 | The Indistinguishability Principle is a consequence, not an ad hoc postulate | weak | §3.3. It rests on restricting to symmetric observables, itself a postulate (Messiah & Greenberg 1964) |
| C5 | No language with individual constants or variables adequately describes a domain of non-individual bundles | weak–moderate | philosophical argument (Strawson, Wittgenstein Tractatus 4.1272), §4 |
| C6 | Q does not prove the substitutivity of indiscernibles | strong | a known metatheorem of Q, sketched p. 18 with reference to French & Krause 2006 |
| C7 | Permutation invariance: swapping indiscernibles yields an indiscernible qset | strong (as a theorem of Q) | Theorem 7, p. 19. The printed proof is garbled; see French & Krause 2006 ch. 7 |
| C8 | Atomic bundles are representable as qsets in Q(B), which is nonempty by Choice, and all its members are indiscernible | moderate | construction, §6, pp. 21–22. Existence is by the Q-version of AC; no independent consistency check is given |
| C9 | A definite number N of indistinguishable particles is representable without labels as N(B) with qc = N | moderate | construction, p. 22, using (qc3) |
| C10 | Quasi-set theory is an "appropriate meta-language" for the ontology of properties | moderate | the construction in §6 shows adequacy for kinds and multiplicities. States, actualisation and dynamics are not formalised |

## Method

The authors reinterpret an existing formal theory. Krause's Q (§5) is given a non-intended interpretation, with m-atoms read as property-instances rather than particles (p. 20). The construction is then made explicit for atomic bundles and for collections of them (§6).

## Concepts

- **U-type-property / I-type-property.** A universal determinable (e.g. energy H^U) and its instance in a particular bundle ([H]).
- **P-case-property / A-case-property.** A possible determinate value (an eigenvalue) of an I-type-property, and the single one that is actual.
- **Bundle.** A system: a collection of I-type-properties with no principle of individuality, and no set, because its members are not individuals (p. 11).
- **Atomic bundle.** The ontological correlate of an elementary particle: one instance per U-type, always including [M], [W], [S] with single values (p. 20).
- **Quasi-set (qset) / m-atom / M-atom.** Q's collections, its non-classical indiscernible atoms, and its classical (ZFA) atoms.
- **Quasi-cardinal qc(x).** A primitive cardinal attached to a qset with no ordinal or labelling (pp. 17–18).
- **Strong singleton `[[x]]_z`.** A subqset of [x]_z with qc = 1. That its element "is x" cannot be proved without identity (p. 16).
- **Non-reflexive logic.** A logic in which the standard theory of identity is restricted (pp. 12–13).

## Connections

The paper answers, formally, the complaint that structuralist and non-individual ontologies cannot be stated in standard logic, the same challenge Wallace's math-first structuralism takes up differently ([LIT-151](../literature.d/LIT-151.md)). It bears directly on Leitgeb & Ladyman ([LIT-154](../literature.d/LIT-154.md)). Leitgeb & Ladyman keep standard identity and accept primitive, non-weakly-discernible nodes. Holik et al. drop identity for the relevant items and replace it with indiscernibility. These are two opposite answers to the same graph-theoretic and quantum puzzle.

Its closeness to OSR (French 2020) links it to the record's structural-realism cluster: the Ladyman SEP entry ([LIT-045](../literature.d/LIT-045.md)), Morganti's coherentism ([LIT-173](../literature.d/LIT-173.md)), and effective OSR ([LIT-184](../literature.d/LIT-184.md)). The algebra-first motivation is shared with the C*-algebraic and sheaf-theoretic treatments of contextuality (e.g. [LIT-016](../literature.d/LIT-016.md)). The KS "immunity" claim should be read against that literature.

Gao ([LIT-121](../literature.d/LIT-121.md)) cites French & Krause 2006 for non-supervenient relations as an alternative reading of entanglement (p. 74). He takes the opposite, individualist line, with particles occupying one position per instant.

## Bearing on the record

- It is the record's formal anchor for "non-individuals" in quantum ontology, and a counterpart to [LIT-154](../literature.d/LIT-154.md).
- Metaphysics: the paper defends a bundle theory without individuals, universals over tropes, possibilism, and holism about composites. It presupposes that the algebraic formalism's order of priority is a guide to ontology.
- No ML-practice content. Nothing here bears on the Anthology of the SOTA.

## Limitations

- The new formal content (§6) covers only kinds and the counting of indistinguishable bundles. States, the actualisation of case-properties, and dynamics are not represented in Q, though the ontology gives them central roles (propensities, A-case-properties).
- The Kochen–Specker and non-separability "solutions" (§3) are recharacterisations, reached by definition or relocation, not arguments with new content. The Indistinguishability Principle is moved, not derived (C4).
- The printed formal material contains errors (Def. 6, Theorem 7's proof, notation on p. 18). A reader needs French & Krause 2006 to check it.
- The Galilean treatment is nonrelativistic. Kinds are labelled by (m, w, s) from Galilean irreducible representations, and there is no discussion of QFT, where particle number itself is not fixed.
- The metalanguage uses identity when it says variables x and y are different. The authors acknowledge this (Remark, p. 14) and argue by analogy with paraconsistent logics that it does not collapse the theory.

## Open questions

- Can states (functionals) and the actualisation of A-case-properties be formalised inside Q, e.g. as quasi-functions on qsets of projector-properties, without reintroducing labels?
- Does restricting to symmetric observables in this ontology select the bosonic and fermionic sectors, or leave parastatistical sectors open? The paper does not say.
- How does the bundle construction extend to relativistic QFT, where kinds come from Poincaré representations and number is indefinite?

## Corrections to the seeded skim

- Source: the dossier used this same preprint; both Springer and the PhilArchive copy were unreadable. Note the PhilSci file is titled "-final", but it predates the retitled Synthese version, and any changes are unverified.
- The dossier says the Indistinguishability Principle "falls out of the requirement that only symmetric observables are allowed (Messiah & Greenberg), so it no longer needs to be postulated ad hoc". That repeats the paper's claim (pp. 9–10) without noting that restricting to symmetric observables is itself a postulate. It is Messiah & Greenberg's alternative to symmetrising states, here re-motivated ontologically ("when two indistinguishable bundles merge … which … is taken first … does not matter"). The postulate is moved, not removed. The paper also does not discuss which symmetry sector (bosonic, fermionic, other) is then selected.
- More precise mapping (pp. 3–5): general physical magnitudes correspond to universal U-type-properties; observables to their instances, I-type-properties [A]; eigenvalues to possible P-case-properties aᵢ; the single realised value to an A-case-property [a_k]; the state to propensities to actualisation; and a system to a bundle of I-type-properties. A system is a bundle of *determinables*, not of determinate values. The "immunity" to Kochen–Specker (p. 7) depends on exactly this: contextuality restricts which case-properties become actual and never touches bundle membership.
- The dossier leaves out two stated metaphysical commitments. First, universals and their instances, which are "only numerically different", are preferred over tropes, because tropes are individuated by location or bearer and would reintroduce distinguishability (p. 5). Second, possibility is taken in non-actualist (possibilist) terms, with probabilities as irreducible propensities (p. 6).
- On the dossier's open question (does the Axiom of Choice quietly reintroduce selection?): the paper says the chosen qset picks one element from each U "no matter which one", and that all members of Q(B) are indiscernible (p. 22). Choice gives existence without identifying anything. The paper does not address the worry explicitly, and R(x) quantifies "∀Π" over T, the collection of projector-properties, treating that collection classically.
- Errors in the formal section: Def. 6(i) reads "z ≡ y" where "z ≡ w" is meant; "`[[n]]_z`" should be "`[[b]]_z`" (p. 18). Theorem 7's printed proof is garbled: Case 2 asserts "(x − `[[z]]_t`) ∪ `[[w]]_t` = ∅", then invokes (qc7) where (qc6) and Theorem (⋆) are presumably meant (p. 19). The paper defers to French & Krause 2006, ch. 7, for details. Whether the Synthese version corrects these is unverified.
- metaphysics tag: justified. The paper argues for a bundle theory without individuals, universals over tropes, possibilism about modality, a view on how identity and indiscernibility relate (PII "does not apply" to non-individuals, p. 9), and holism for composites.
- primary topic: metaphysics (keep). The paper's aim is a meta-language for an ontology. The formal apparatus is the means.
- Missing tags: `logic` should be added. Q is a first-order theory over a non-reflexive logic that restricts identity and substitutivity (pp. 12–14), and §4's argument is that any language with individual constants and variables is inadequate. `mathematics` is also justifiable: the topic's blurb names set theory, and quasi-set theory is a set theory applied to another field. `identity` is already present and apt.
