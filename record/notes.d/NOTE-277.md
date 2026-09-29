---
number: 277
status: Read
formerly:
- NOTE-tmp625ar
paper: LIT-343
title: 'A topos foundation for theories of physics: I. Formal languages for physics'
version: 1
history:
- version: 1
  date: '2026-09-29'
  note: >-
    Read in full (Full text of arXiv quant-ph/0703060 v1 (7 Mar 2007, the
    only arXiv version), from the arXiv PDF, 36 pp. I read the abstract,
    §§1–5, the acknowledgements, Appendix A (A.1 presheaves on a poset, A.2
    presheaves on a general category, sieves, the sub-object classifier,
    global elements) and all 33 references. Nothing was skipped. The paper
    has no theorems of its own; everything was read at the level of its
    definitions and arguments. I also read papers II–IV of the series in
    full (arXiv quant-ph/0703062, 0703064, 0703066), since this paper states
    the programme they carry out. `pdftotext` was not available, so I
    extracted the text with PyMuPDF; I checked eq. (3.4) against a render of
    the page. The published J. Math. Phys. text (paywalled) was not seen.
    Every arXiv listing shows v1 only, so any revision for the journal is
    unverified.). The first NOTE on this paper, which was seeded from its
    abstract alone.
date: '2026-09-29'
summary: >-
  The programme paper. Its contention is that a theory of a physical
  system S is a representation of a typed "local language" L(S) (ground
  types Σ and R, function symbols A : Σ → R) in a topos. Physical
  quantities become arrows Σ_φ → R_φ, and propositions become sub-objects
  of Σ_φ, which form a Heyting algebra. Classical physics is the
  representation in Sets. The paper proves nothing. Its one argument is
  that the axiom ¬(A ε Δ) ⇔ A ε ℝ∖Δ is not validated by non-Boolean
  Heyting representations (§3.2.1).
---

# NOTE-277: A topos foundation for theories of physics: I. Formal languages for physics

## Contribution

The paper states the Döring–Isham programme and fixes its vocabulary. The thesis (§2.2.2, §4) is this: for a given theory-type, each system S carries a topos τ_φ(S), and "constructing a theory of physics is equivalent to finding a representation in a topos of a certain formal language that is attached to the system" (abstract). The paper defines the two languages used in the rest of the series, a propositional language PL(S) and a higher-order typed local language L(S). It works out their representation for classical physics in Sets. It motivates the move from two directions: the a priori use of ℝ and [0,1] in quantum theory (§2.1), and the need for a realist rather than instrumentalist formalism for closed systems and quantum cosmology (§1).

## Key insight

Make every theory "look like classical physics" inside some topos. A classical theory has a state space S, real-valued functions S → ℝ for quantities, and the Boolean algebra of subsets of S for propositions. A topos theory has a state object Σ_φ, arrows A_φ : Σ_φ → R_φ, and the Heyting algebra Sub(Σ_φ) of sub-objects. Only the topos changes. The authors call the resulting stance "neo-realism": propositions get truth values, not just probabilities, but the truth values lie in a Heyting algebra (global elements of the sub-object classifier), and there may be no "microstates" at all.

## Assumptions

- **Realism, as physicists use the word (§1).** (1) "A property of the system" is meaningful. (2) Propositions are handled by Boolean logic. (3) There is a space of microstates that fixes the truth of every proposition. The paper keeps (1) and relaxes (2) to Heyting logic. It keeps a "state object" for (3) but gives up enough microstates to determine it.
- **Language before representation.** One local language L(S) is associated with each system (§4.1). Only the function symbols A : Σ → R depend on the system. The Hamiltonian and other dynamics live in the representation, not the language (§3.2.2, §4.1).
- **Intuitionistic deduction.** Both languages get intuitionistic logic, chosen "since it allows a larger class of representations" (§3.2.1).
- **Topos facts are imported from textbooks** (Bell, Goldblatt, Lambek–Scott, Mac Lane–Moerdijk), not proved: Sub(X) is a Heyting algebra in any topos; linguistic topoi; the internal language.

## Key results

The paper has no theorems. What it establishes is definitional or argued.

- **PL(S) (§3.2).** Primitive propositions are strings "A ε Δ" (A a quantity name, Δ a Borel subset of ℝ, external to the language), closed under ¬, ∧, ∨, ⇒, with the axioms of intuitionistic propositional logic plus modus ponens. A representation π maps primitives into a Heyting algebra H and extends recursively (eqs. 3.5–3.8).
- **Optional axioms (§3.2.1).** A ε Δ₁ ∧ A ε Δ₂ ⇔ A ε Δ₁∩Δ₂ (3.1) and A ε Δ₁ ∨ A ε Δ₂ ⇔ A ε Δ₁∪Δ₂ (3.2) are "consistent with the intuitionistic logical structure". ¬(A ε Δ) ⇔ A ε ℝ∖Δ (3.3) is not recommended for non-Boolean targets, because it forces ¬¬α ⇔ α on primitives. Paper II later shows that the quantum representation validates (3.2) but not (3.1) ([LIT-335](../literature.d/LIT-335.md), §2.4.1).
- **Classical representation (§3.2.3, §4.3).** π_cl(A ε Δ) = Ă⁻¹(Δ) ⊆ S. H is the Boolean algebra of Borel subsets. (3.1)–(3.3) all hold, by eqs. (3.10)–(3.12). The truth value in state s is 1 iff Ă(s) ∈ Δ (3.13).
- **Failure in standard quantum theory (§3.2.4).** Represent "A ε Δ" by the spectral projector Ê[A ∈ Δ] in the lattice P(H). Distributivity (3.17) is derivable in PL(S) and fails in P(H) (3.15–3.16), so P(H) is not a representation of PL(S). A realist reading of quantum logic is thereby barred; the instrumentalist reading survives, giving Born probabilities rather than truth values.
- **L(S) (§4.1).** Type symbols are 1, Ω, Σ, R, closed under products and power types P. There are variables, and function symbols with signature T₁ → T₂; F(Σ,R) is non-empty and holds the physical quantities. Terms include A(s̃) ∈ Δ̃ (type Ω, with Δ̃ now an internal variable of type PR) and {s̃ | A(s̃) ∈ Δ̃} (type PΣ). Deduction is by sequents; footnote 23 lists the axioms (tautology, unity, equality, products, comprehension). Extra axioms, such as abelian-group axioms for R, are optional, and the paper says choosing them needs "physical insight".
- **Representation in a topos (§4.2).** Σ, R, Ω, 1 go to Σ_φ, R_φ, the sub-object classifier and the terminal object. A goes to A_φ : Σ_φ → R_φ, required to be faithful. The term A(s̃) ∈ Δ̃ goes to e ∘ (A_φ × id) : Σ_φ × PR_φ → Ω (4.3). The comprehension term goes to its power transpose PR_φ → PΣ_φ (4.4). Sentences go to global elements of Ω. For quantum theory the topos is named as Sets^{V(H)^op} with Σ_φ the spectral presheaf (§4.2, item 1), but nothing more is said here.
- **Theories as translations (§4.2).** A representation of L(S) in τ is equivalent to a translation of L(S) into the internal language L(τ), or equivalently a functor from the linguistic topos C(L(S)) to τ. This is textbook material, cited from Bell. It is the hook for paper IV's category of systems ([LIT-310](../literature.d/LIT-310.md)).
- **Extensions (§4.4).** Extra ground types, e.g. M (space-time, a poset object as a topos analogue of a causal set) or T (time), are floated as speculation.
- **Appendix.** A primer: presheaves on a poset and on a small category, sub-objects, sieves as lower sets, Ω as the presheaf of sieves with its Heyting operations (A.13–A.16), characteristic arrows (A.17), and global elements as matching families (A.19). In a presheaf topos over contexts, χ_K(x) is "the sieve of stages at which x lies in K". That is the sense in which "contextual, generalised truth values arise naturally" (p. 33).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Constructing a theory of a system is equivalent to finding a representation of its local language L(S) in a topos | assertion (programmatic definition) | §1, §4.4, abstract. It is stipulated, not derived. No theory is constructed this way that was not already known (classical physics here; quantum theory in II–III) |
| C2 | Classical physics is the representation of PL(S)/L(S) in Sets, with Borel subsets as propositions and axioms (3.1)–(3.3) valid | proof (elementary) | §3.2.3, §4.3; eqs. (3.9)–(3.13), (4.5)–(4.6) |
| C3 | P(H) cannot represent PL(S), because PL(S) proves distributivity and P(H) is non-distributive | proof (elementary) | §3.2.4, eqs. (3.15)–(3.17); the witness is the well-known three-rays-in-ℝ² example (footnote 19), not written out |
| C4 | Axiom (3.3) ¬(A ε Δ) ⇔ A ε ℝ∖Δ is not indicated for non-Boolean representations | informal argument (correct conclusion; eq. 3.4 misprinted) | §3.2.1. It forces ¬¬-stability of primitives, which a Heyting representation need not have |
| C5 | Every topos theory is "neo-realist": quantities are arrows Σ_φ → R_φ, propositions are sub-objects of Σ_φ, and truth values are global elements of Ω | assertion (conceptual gloss on the definitions) | §2.2.2, §5 |
| C6 | Physical quantity-values in a closed-system or quantum-gravity theory need not be real numbers, and probabilities need not lie in [0,1] or even be totally ordered | informal argument (philosophical) | §2.1 (rulers and pointers; relative frequency; "potentiality") |
| C7 | Quantum theory's topos is Sets^{V(H)^op} with the spectral presheaf as state object | assertion here; deferred | §4.2. Established in [LIT-335](../literature.d/LIT-335.md) and [LIT-299](../literature.d/LIT-299.md) |

## Concepts

- **Neo-realism.** The authors' coinage (fn. 6) for the structure in C5: a realist-looking formalism with Heyting-valued truth.
- **PL(S).** A propositional language over primitives "A ε Δ", with Δ external to the language.
- **L(S) (local language).** A typed higher-order language after Bell. Δ becomes an internal variable of type PR.
- **State object Σ_φ and quantity-value object R_φ.** The representations of the ground types Σ and R.
- **Representation φ.** An H-valuation (for PL(S)) or a model of L(S) in a topos. The authors avoid the word "interpretation" (fn. 25).
- **Sieve.** A lower set of stages. The sub-object classifier of a presheaf topos is the presheaf of sieves, and a sieve is a context-relative truth value.

## Connections

- **Isham–Butterfield 1998 ([LIT-325](../literature.d/LIT-325.md)).** The origin, cited as [21]–[24]. In that work "the crucial 'daseinisation' operation … was not known and, consequently, the discussion became convoluted in places" (§3.1). This paper restarts from the language side so as to place that work.
- **Döring–Isham II–IV ([LIT-335](../literature.d/LIT-335.md), [LIT-299](../literature.d/LIT-299.md), [LIT-310](../literature.d/LIT-310.md)).** They carry out, respectively, the PL(S) and truth-object part, the L(S) quantity-value part, and the category of systems.
- **Abramsky–Coecke categorical quantum mechanics.** Named in §1 as a rival strategy: categorical analogues of Hilbert-space structure versus the internal logic of a topos. Not in the record.
- **Dalla Chiara–Giuntini's first-order quantum logic.** Flagged for future comparison (fn. 18). The comparison is never made in the series.

## Bearing on the record

- **The map's role (§0 and row 8: "the Döring–Isham topos program (spectral presheaf) … owns §2.1").**
  - What this paper supplies is the programme's framing, not the machinery. There is no spectral presheaf construction, no Kochen–Specker statement beyond motivation, and no ultrafilters.
  - The step "no global ultrafilter → presheaf over contexts → Kochen–Specker" is owned by Isham–Butterfield 1998 ([LIT-325](../literature.d/LIT-325.md), §2.3). Its operator-algebraic form is in papers II–III ([LIT-335](../literature.d/LIT-335.md), [LIT-299](../literature.d/LIT-299.md)).
  - What paper I adds for the map is the frame in which "the LRH is one context" can be stated. A single Boolean context is exactly a classical representation in Sets (C2). The non-Boolean whole is a representation in a presheaf topos whose propositions form a Heyting algebra, not an orthomodular lattice.
- **Two logics, not one.** The map's rows 1 and 3 use the orthomodular subspace lattice with orthocomplement as negation. §3.2.4 here argues that P(H) with orthocomplement cannot serve as the logic of propositions if distributive deduction is kept. The topos programme's answer is to change the logic to an intuitionistic one, where excluded middle fails and ¬ is a pseudo-complement.
  - So the map's "logical face" (topos) and "operator face" (projector lattice) are not one logic seen twice.
  - They are related by a lossy map, daseinisation, which paper II shows preserves ∨ but not ∧ or ¬ ([LIT-335](../literature.d/LIT-335.md)).
  - A document that uses orthocomplement for negation and cites this programme for its logic should say which one it means.
- **Contextuality entries.** No direct relation to [THEORY-012](../theory.d/THEORY-012.md), [LIT-016](../literature.d/LIT-016.md), [LIT-277](../literature.d/LIT-277.md) or [LIT-278](../literature.d/LIT-278.md): this paper has no probabilities, empirical models or obstructions. The sieve-valued truth of the Appendix is the context-relative truth value that [LIT-016](../literature.d/LIT-016.md)'s authors credit to the Isham school and then set aside ([NOTE-016](NOTE-016.md), Connections).
- **ML practice.** It carries nothing for ML practice. The one ML-adjacent monograph in the Anthology, [ANTH-LIT-698](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-698.md) (Belfiore & Bennequin), does not cite Isham, according to the full-text search reported in [NOTE-016](NOTE-016.md), so there is no link to record.
- **For filing.** Tags as above. `anthology-candidate` is not proposed.

## Limitations

- **No results.** The paper consists of definitions, a classical worked example and argument. "Constructing a theory = representing a language" is a stipulation whose payoff (new theories without continuum quantities) is not demonstrated anywhere in the series; paper III's conclusion concedes it is "an important challenge for future work".
- **Choosing axioms is left open.** Which extra axioms go into L(S) (abelian group, ordering, reals) is explicitly left to "physical insight" (§4.1). The series later shows that the natural quantum R_φ is only a monoid ([LIT-299](../literature.d/LIT-299.md)).
- **Motivations are philosophical.** §2.1 on why values are real and probabilities lie in [0,1] is a philosophical position, not an argument with premises that could be checked.
- **Misprint.** Eq. (3.4) is misprinted (see corrections).

## Open questions

- Is there any system for which a representation of L(S) in a non-Sets, non-quantum topos yields a physically new, testable theory? The series offers none. Paper III §6 suggests presheaves over a non-Hilbert context category C and M-sets as places to look.
- Which axioms on R are physically forced? The quantum case ([LIT-299](../literature.d/LIT-299.md)) rules out field and ring axioms and leaves a monoid, or a group after Grothendieck completion.
- How does this higher-order intuitionistic setting compare with first-order quantum logics (fn. 18)? The comparison was promised and never made.

## Corrections to the seeded skim

- Seeded from metadata; the text agrees with the seed's summary. Two things to add. First, the paper contains no theorem and no quantum-theoretic construction: the spectral presheaf is named once (§4.2) and deferred to papers II–III. Second, the propositional language PL(S) is introduced, by the authors' own account, mainly to link to the earlier Isham–Butterfield work ([LIT-325](../literature.d/LIT-325.md)); the programme runs on L(S).
- Eq. (3.4) is misprinted in the arXiv text. It reads "¬¬(A ε Δ) ⇔ A ε ℝ", where the surrounding argument needs "A ε Δ". The argument is also weaker than stated. Axiom (3.3) forces every primitive proposition to be ¬¬-stable; that is not inconsistent with intuitionistic logic, it is just not satisfied in every Heyting-algebra representation. "Could be false in a Heyting-algebra representation" (p. 13) is the accurate phrasing, and it is what the paper concludes.
- Identifiers check against the arXiv listing: journal-ref J. Math. Phys. 49:053515 (2008); DOI 10.1063/1.2883740; comment "36 pages, no figures". The PDF is dated 6 March 2007 and arXiv v1 is 7 Mar 2007. The seed's `published: 2008-05-01` is the journal issue; if the record dates works by first public appearance, it should be 2007-03-07. This is flagged, not changed.
- Tag proposal: add `philosophy-of-science`. §§1–3 are an argument about realist versus instrumentalist readings of physical theories, which is that topic's blurb. Keep `contextuality`: the Appendix defines sieve-valued, context-relative truth values, and the series is the reference someone browsing contextuality would expect. The primary tag stays `quantum-foundations`.
