---
number: 275
status: Read
formerly:
- NOTE-tmp39uqu
paper: LIT-306
title: 'The logic of quantum mechanics'
version: 2
history:
- version: 1
  date: '2026-09-29'
  note: >-
    Read in full (The full paper, *Annals of Mathematics* 37(4), October
    1936, pp. 823–843, from the Internet Archive's scan of the issue.
    *Annals* issues are renewed only from July 1945, and no contribution
    renewals were made before 1959, so the 1936 volume is in the US public
    domain. I read all 21 pages from page images: Part I, Physical
    Background (§§1–6); Part II, Algebraic Analysis (§§7–14); Part III,
    Conclusions (§§15–18); the Appendix (§§1–8); and footnotes 1–35. Nothing
    was skipped. I followed the Appendix's computation at the level of its
    steps (equations 1–29), not re-deriving each identity.). The first NOTE
    on this paper, which was seeded from its abstract alone.
- version: 2
  date: '2026-09-29'
  note: >-
    Correction added: Husimi 1937 uses the orthomodular law but does not
    isolate it, per its reading.
date: '2026-09-29'
summary: >-
  The paper argues heuristically that the experimental propositions of a
  quantum system correspond to closed linear subspaces of Hilbert space.
  Meet is intersection, join is closed linear span, and negation is
  orthogonal complement. The lattice satisfies L1–L4 and complementation
  L71–L73 but not the distributive law L6. The paper proposes the
  *modular* law L5 as its replacement. Under a finite-dimension
  assumption, it concludes that the propositional calculus of QM is an
  abstract projective geometry. The Appendix proves that
  orthocomplementations on P_{n−1}(F), n ≥ 4, are exactly the polarities
  of definite diagonal Hermitian forms with respect to an involutory
  anti-automorphism of F.
---

# NOTE-275: The logic of quantum mechanics

## Contribution

The paper asks "what logical structure one may hope to find in physical theories which, like quantum mechanics, do not conform to classical logic" (§1). Its "main conclusion, based on admittedly heuristic arguments", is a calculus of propositions formally indistinguishable from that of linear subspaces under set products, linear sums and orthogonal complements. This calculus resembles the classical calculus for and, or and not.

- **Part I.** It builds the dictionary. Observation-spaces lead to experimental propositions (subsets of observation-spaces), and these lead to subsets of phase-space. For classical mechanics that means Lebesgue-measurable sets modulo null sets, a Boolean algebra (§5). For QM it means closed subspaces spanned by joint eigenvectors (§6).
- **Part II.** It axiomatises: partial order (S1–S4), lattice (L1–L4), orthocomplementation (L71–L73), and the failure of distributivity (L6). It proposes modularity (L5), and derives projective geometry by adding finite dimension and irreducibility (§12). It then characterises orthocomplemented projective geometries algebraically (§§13–14 and the Appendix).
- **Part III.** It draws philosophical conclusions: QM has "greater logical coherence" than classical mechanics (§16), and it is distributivity, not negation, that is "the weakest link in the algebra of logic" (§17).

## Key insight

Compatible measurements have joint eigenspaces, so a proposition about one set of compatible readings picks out a closed subspace. The lattice of such subspaces keeps everything about and/or/not except distributivity. Distributivity fails precisely because incompatible propositions cannot be combined by independent observers (§10). Modularity is the natural weakening, since it follows from a dimension function, which the paper links to probability (§11). Modularity together with irreducibility turns the lattice into a projective geometry.

## Assumptions

- **Observation and phase space.** An observation of a system is the readings (x₁, …, x_n) of compatible measurements. Experimental propositions are subsets of observation-spaces. States are points of a phase-space Σ, Hilbert space for QM (§§2–3).
- **The Postulate (§6).** It is quoted in the corrections. Its motivation is the "not unnatural conjecture" that all Hermitian operators are observables, or those of a ring M (footnotes 12–13). Continuous spectra are "disregarded" (footnote 10).
- **Orthocomplementation.** Passage to the complement is "a dual automorphism of period two", and a implies a′ is absurd (§9).
- **Modularity (§11).** It is proposed as a postulate. It is motivated by the existence of a dimension function (D1: a > b ⇒ d(a) > d(b); D2: d(a) + d(b) = d(a∩b) + d(a∪b)), which "partially describe the formal properties of probability". The paper concedes "it would be desirable to interpret L5 by simpler phenomenological properties".
- **Finite dimension (§12).** Finite chain length is introduced "admitting frankly that the assumption is purely heuristic". Irreducibility (no "neutral" elements) is justified by the irreducibility of QM's operator ring, i.e. MM′ contains only 0 and 1 (footnote 28).

## Key results

- **The QM dictionary (§6).** (1) The mathematical representative of any experimental proposition is a closed linear subspace. (2) The representative of a negation is the orthogonal complement, "since all operators of quantum mechanics are Hermitian". (3) Three conditions are equivalent: (3a) P's representative ⊂ Q's; (3b) P implies Q (certainty of P gives certainty of Q); (3c) Prob(P) ≤ Prob(Q) in every ensemble. From the Postulate: "The set-product and closed linear sum of any two, and the orthogonal complement of any one closed linear subspace … itself represents an experimental proposition".
- **Classical case (§5).** "The experimental propositions concerning any system in classical mechanics, correspond to a 'field' of subsets of its phase-space. More precisely: To the 'quotient' of such a field by an ideal in it. At any rate they form a 'Boolean Algebra'." This cites Stone 1934 in footnote 9.
- **Distributivity (§10).** L6 is "a law in classical, but not in quantum mechanics". The witness: a is "wave-packet on one side of a plane", a′ the other side, and b "in a state symmetric about the plane". Then b ∩ (a ∪ a′) = b > 0 = (b ∩ a) ∪ (b ∩ a′). Also: "every 'field' of sets is isomorphic with a Boolean algebra, and conversely" (citing Stone). L6 follows from the compatibility of observables. The *generalised* distributive law fails in the measure algebra (the remark after §10).
- **The modular law (§11).** Products and closed sums of *finite-dimensional* subspaces satisfy L5. In Hilbert space, L5 fails. The counterexample: a is spanned by (ξ_{2n} + 10^{−n}ξ₁ + 10^{−2n}ξ_{2n+1}), b by the ξ_{2n}, and c by a and ξ₁. These generate the pentagon of Fig. 1 (Dedekind's criterion for non-modularity).
- **Relation to projective geometry (§12).** Citing Birkhoff 1935: "any lattice of finite dimensions satisfying L5 and L72 is the direct product of a finite number of abstract projective geometries … and a finite Boolean algebra, and conversely". A lattice with L5 and L71–L73 has independent basic elements (atoms) of which every element is a union iff it is Boolean (the Remark). The paper concludes that irreducibility forbids non-trivial "neutral" (central) elements in QM. Hence "*the propositional calculus of quantum mechanics has the same structure as an abstract projective geometry*" (§12, italic).
- **Skew fields (§13).** For n = 4, 5, …, every abstract (n−1)-dimensional projective geometry is P_{n−1}(F) for a (not necessarily commutative) field F. The full proof is deferred as "lengthy although elementary" (footnote 30).
- **§14 and Appendix, the main theorem proved in the paper.** P_{n−1}(F) admits an orthocomplementation satisfying L71–L73 iff F has an involutory antiautomorphism w (Q1–Q3) and a definite diagonal Hermitian form Σ w(x_i)γ_iξ_i with w(γ_i) = γ_i (Q4). Complement is then polarity with respect to that form. Sufficiency is in §14; necessity is in the Appendix, via a coordinate normalisation by collineations and functional equations (eqs. 1–29). §14 summary: "the above class of systems is exactly the class of irreducible lattices of finite dimensions > 3 satisfying L5 and L71–L73."
- **Models (§15).** Any such F gives models P_n(F): real, complex and quaternions (footnote 31, citing Kolmogoroff: locally compact projective geometries are over ℝ, ℂ or ℍ). Known criteria cannot distinguish these. Infinite-dimensional P_∞(F), made of *all* closed subspaces, is available, but "Hankel's principle of the 'perseverance of formal laws'" (to keep L5) favours a continuous-dimensional model P_c(F), i.e. von Neumann's continuous geometries (footnote 33).
- **Philosophy (§§16–17).**
  - QM calculi are irreducible, "of unbounded complexity", while classical ones decompose into independent constituents.
  - Footnote 34: "In quantum mechanics, dimensions but not complements are uniquely determined by the inclusion relation; in classical mechanics, the reverse is true!"
  - Mechanics points to L6 "as the weakest link in the algebra of logic", in contrast to intuitionist critiques of negation.
  - Footnote 35: given L1–L5 and L7, L6 is equivalent to "a′ ∪ b = 1 implies a ⊂ b".
- **Open questions (§18).** "What experimental meaning can one attach to the meet and join of two given experimental propositions? What simple and plausible physical motivation is there for condition L5?"

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | QM experimental propositions are represented by closed subspaces, negation by orthogonal complement, implication by inclusion | heuristic argument plus a Postulate | §6; rests on the Postulate and on "all Hermitian operators are observables" |
| C2 | Classical propositions form a Boolean algebra (a field of sets modulo an ideal) | argument, cites Stone | §5 |
| C3 | Distributivity fails in QM | example | §10, the half-space wave-packet example |
| C4 | Closed subspaces of infinite-dimensional Hilbert space are not modular | proof (explicit counterexample) | §11, Fig. 1 construction |
| C5 | QM propositions should satisfy the modular law L5 | heuristic / postulate | §11: dimension-function analogy with probability; §18 asks for a physical motivation |
| C6 | Under finite dimensions and irreducibility, the QM calculus is an abstract projective geometry | proof modulo cited results (Birkhoff 1935; Öre) | §12 |
| C7 | Orthocomplementations on P_{n−1}(F), n ≥ 4, are exactly polarities of definite diagonal Hermitian forms w.r.t. an involutory antiautomorphism | proof | §14 (sufficiency) and Appendix §§1–8 (necessity); I followed the steps, not every identity |
| C8 | Projective geometries of dimension ≥ 3 are coordinatised by skew fields | cited / deferred | §13, footnote 30: "we propose to publish it elsewhere" |
| C9 | QM has "greater logical coherence" than classical mechanics | philosophical interpretation | §16 |
| C10 | Distributivity, not negation, is logic's weakest link | philosophical interpretation | §17 |

## Method

Heuristic physical analysis (Part I), then lattice-theoretic axiomatics and classical projective-geometry coordinatisation (Part II), and functional equations for the orthocomplement (Appendix).

## Concepts

- **Observation-space, experimental proposition, physical quality.** A physical quality is an equivalence class of logically equivalent propositions (§7, footnote 14).
- **Mathematical representative (§6).** The closed subspace spanned by joint eigenfunctions f_k with (λ₁, …, λ_n) ∈ S.
- **L1–L4, L5, L6, L71–L74.** The lattice, modular, distributive and orthocomplementation laws.
- **Neutral element / irreducible.** A central element, and a lattice without non-trivial central elements (§12).
- **Dimension function.** d with D1–D2.

## Connections

- **[LIT-298](../literature.d/LIT-298.md) (Kochen–Specker).** KS criticise the non-partial approach implicitly. They define quantum propositions as a *partial* Boolean algebra, operating only on commeasurable pairs, which answers BvN's first §18 question ("what experimental meaning … meet and join") by declining to use meets of incompatible propositions as experimental propositions. BvN §9 note that meets and joins of incompatible propositions are only "physical qualities", not experimental ones (footnote 18 and §8 end).
- **[LIT-339](../literature.d/LIT-339.md) (Wick–Wightman–Wigner).** WWW superselection breaks BvN's irreducibility premise (§12). With superselection the lattice has neutral (central) elements, the sector projections, and it decomposes as a direct product. That is exactly the case BvN rule out by fiat (footnote 28, MM′ trivial).
- **[LIT-353](../literature.d/LIT-353.md) (Stone).** BvN's footnotes 9 and 21 cite the Stone 1934 PNAS announcement for "every field of sets is isomorphic with a Boolean algebra, and conversely".
- **[LIT-262](../literature.d/LIT-262.md) (van Rijsbergen).** It uses the Hilbert subspace lattice for IR and inherits the BvN dictionary. Van Rijsbergen's non-distributivity arguments are BvN §10's.
- **[THEORY-017](../theory.d/THEORY-017.md).** BvN's footnote 34 ("dimensions but not complements are uniquely determined by the inclusion relation") is a lattice-level analogue of [THEORY-017](../theory.d/THEORY-017.md): the orthocomplement, i.e. the inner product, is extra structure beyond inclusion. §15 notes that real, complex and quaternionic models "cannot be differentiated by known criteria".
- **[LIT-312](../literature.d/LIT-312.md), [LIT-340](../literature.d/LIT-340.md) (Aerts–Gabora).** Quantum-cognition works that rely on this lattice.

## Bearing on the record

- **Map row 1, "owner of the orthomodular subspace-lattice machinery (concept = projector, judgment = cut)".** BvN own the *idea*, not the orthomodular machinery.
  - *What they own.* The identification of propositions with closed subspaces or projectors, with meet, join and orthocomplement, and the non-distributivity point.
  - *What they do not own.* The axiom they propose is modularity. They show that the full closed-subspace lattice of infinite-dimensional Hilbert space *fails* it. So "the orthomodular lattice of closed subspaces" is not their object, and citing BvN for orthomodularity is a misattribution.
  - *What the owner's finite-dimensional embedding space gets.* The subspace lattice is modular (hence orthomodular), and BvN's §12 projective-geometry picture applies directly. That is good news for the owner, but the citation should be: BvN for the dictionary and non-distributivity, and a later source (e.g. Kalmbach, or the Husimi/Piron line) for orthomodularity.
- **"Judgment = cut".** BvN's implication = inclusion and probability ordering (3a–3c) is the nearest thing. There is no notion of a "cut" in the paper.
- **The single-context diagnosis.** It fits BvN §5 versus §6. A single compatible family generates a Boolean algebra (§§5, 10: L6 "is also a logical consequence of the compatibility of the observables occurring in a, b, and c"). Non-Boolean structure appears only across incompatible families. BvN say this in one paragraph (§10), and KS turn it into a theorem.
- **ML practice.** It carries nothing, and does not belong in the Anthology.

## Limitations

- **Heuristic by the authors' own description.** Every step from physics to lattice is a postulate or a heuristic, notably the §6 Postulate and modularity.
- **Infinite dimensions are unresolved.** The Hilbert-space lattice fails their own L5. They defer to continuous geometry, which later quantum logic did not generally adopt. Continuous spectra are disregarded.
- **The skew-field coordinatisation is deferred** to another paper. The Appendix proves only the orthocomplement characterisation.
- **Irreducibility is imposed,** which excludes superselection by assumption.

## Open questions

- The paper's own (§18): the experimental meaning of meet and join of incompatible propositions, and a physical motivation for L5. For the record: whether the owner's projector lattice is meant finite-dimensional, where BvN's modular picture applies, or infinite-dimensional, where only orthomodularity survives.

## Corrections to the seeded skim

- Seeded from metadata; the text shows the summary is right except on one load-bearing point. The paper does *not* propose an orthomodular lattice. The replacement for distributivity it proposes is the modular identity L5 (§11: "If a ⊂ c, then a ∪ (b ∩ c) = (a ∪ b) ∩ c"). It notes that L5 holds for closed subspaces only in finite dimensions, and gives an explicit infinite-dimensional counterexample (§11). It therefore prefers von Neumann's continuous geometries over Hilbert space in infinite dimensions (§15, footnote 33). The word "orthomodular" does not appear. That law was isolated later (Husimi 1937; unverified here).
  - *Correction (2026-09-29, from [NOTE-312](NOTE-312.md), the reading of Husimi 1937, [LIT-357](../literature.d/LIT-357.md)):* Husimi *uses* the orthomodular law as an unnamed proof step, justified as "traditional logic in any classical part" (p. 784). He never states or names it as an axiom, so "isolated" overstates him. The usual credit is a reading of his axioms.
- Its identification of propositions with closed subspaces is not a theorem. It rests on a stated Postulate (§6): "The set-theoretical product of any two mathematical representatives of experimental propositions concerning a quantum-mechanical system, is itself the mathematical representative of an experimental proposition". The Postulate is motivated by the conjecture that all Hermitian operators, or all operators of a suitable ring M, are observables. Footnote 14 adds that closed subspaces correspond one-many to experimental propositions, but one-one to "physical qualities" (equivalence classes).
- The paper was received 4 April 1936. The authors are Garrett Birkhoff (Society of Fellows, Harvard) and John von Neumann (Institute for Advanced Study). The seed's summary line calls him "Neumann", which is the Crossref sort form; the author is John von Neumann.
