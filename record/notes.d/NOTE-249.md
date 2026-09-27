---
number: 249
status: Read
formerly:
- NOTE-tmppm8d2
paper: LIT-276
title: 'Measurement as Sheafification: Context, Logic, and Truth after Quantum Mechanics'
version: 1
history:
- version: 1
  date: '2026-09-27'
  note: >-
    Read in full (The full text of arXiv 2512.12249 v2 (16 Dec 2025), from
    the arXiv PDF, 23 pp.: the abstract, §§1–10 (with the unnumbered
    subsections "The EPR Argument and the Demand for Global Truth",
    "Intuitionistic Logic Inside Presheaves", "Contextual Multi-Valued
    Logic", "Measurement Reinterpreted" and "Quantum gravity and the
    sheafification of spacetime"), Appendix A (§11, including the v2
    subsection "A Čech-cohomological Obstruction to Contextuality"),
    Appendix B (§12), the acknowledgement and all 37 references. Nothing was
    skipped. The paper has no figures and no tables. `pdftotext` was not
    available in this session, so I extracted the text with PyMuPDF. I also
    downloaded v1 (13 Dec 2025, 23 pp.) and compared the two extracted texts
    word by word. The differences are listed under corrections. No journal
    version exists to compare (see corrections).). The first NOTE on this
    paper, which was seeded from its abstract alone.
date: '2026-09-27'
summary: >-
  A programmatic essay, with no theorem, model or computation of its own.
  It restates Abramsky & Brandenburger's criterion (contextuality and
  non-locality as the absence of a global section of a presheaf over
  measurement contexts) and adds three things. It declares measurement to
  be "sheafification" of that presheaf, without specifying a site, a
  topology or any sheafified object. It asserts that the Ghose–Patra
  seven-valued logic is a finite Heyting algebra, without giving an order
  or operations. It proposes that a quantum potential scaled by 0 ≤ λ ≤ 1
  (λ = 1 quantum, λ = 0 classical Hamilton–Jacobi) carries the presheaf
  continuously to a sheaf, which is asserted, not modelled. Its one worked
  formula, v2's Čech "obstruction class" [δs], is a coboundary and so is
  zero by construction.
---

<!-- inactive-ok-file: LIT-276 — Rejected: the paper this note reads, placed by this reading; the directive lapses when its status changes -->
<!-- inactive-ok-file: THEORY-017 — Proposed: named only to warn against reading this paper as support for it; the directive lapses when its status changes -->

# NOTE-249: Measurement as Sheafification: Context, Logic, and Truth after Quantum Mechanics

## Contribution

The paper contributes no new result. It is an interpretive essay. It argues that the measurement problem is a logical and not a dynamical problem: collapse is "a logical repair mechanism introduced to save a classical notion of truth" (§3, pp. 5–6).

It packages four existing pieces under one slogan:
- **Abramsky & Brandenburger's global-section criterion** ([LIT-016](../literature.d/LIT-016.md)), which the paper cites as "closely related" (§2, p. 5).
- **Abramsky, Mansfield & Barbosa's Čech-cohomological witness**, cited in v2 only.
- **The author's own earlier λ-interpolated Hamilton–Jacobi dynamics** (Ghose 2002, ref. [27]).
- **The Ghose–Patra seven-valued logic, from the Jaina *saptabhaṅgī*** (Ghose & Patra 2024, a book, ref. [24]).

The slogan joining them, "measurement is sheafification", is new, and so is the claim that the λ-dynamics drives the passage from presheaf to sheaf. Neither is given mathematical content.

## Key insight

The paper wants the reader to see the collapse postulate as a category mistake: demanding one global Boolean valuation of a theory whose truths are indexed by incompatible contexts. On this view a "measurement" is the point at which context-bound (presheaf) data must be rendered as globally communicable (sheaf) data. This is offered as a formal reading of Bohr's insistence on classical language (§6, p. 10).

As a *position*, it is Bohr plus Kochen–Specker, restated in Abramsky–Brandenburger vocabulary. As *mathematics*, the step that would make it more than a restatement is the identification of measurement with sheafification, and of classicality with the sheaf condition and with Boolean logic. That step is not carried out, and where it can be checked it does not hold (see Key results).

## Assumptions

- **The category of contexts C (§4, p. 7).** Its objects are "measurement contexts", described as "physically real experimental arrangement[s]". A morphism C → D is a "refinement or coarse-graining", e.g. "adding compatible observables". No arrow between two contexts "records physical incompatibility".
  - No concrete C is ever given: not for a Bell or KS scenario, and not the Isham–Butterfield context poset of commutative subalgebras.
  - The paper does not say whether C has intersections. The appendix uses Cᵢ ∩ Cⱼ.
  - The paper does not say whether C has an object covered by the maximal contexts. The appendix needs one.
- **The presheaf.** It is F : C^op → Set (Appendix A, p. 18). F(C) is variously "the appropriate set of truth assignments, expectation values, or outcome structures" (§4), and "the set of observables, trajectories, or field-values accessible in context C", where a context "may be a measurement setting, coarse-graining scale, reference frame, or σ–λ diffusion regime" (p. 18). **No single presheaf is fixed.** In particular, the value-assignment presheaf (whose global sections are KS valuations) and the distribution presheaf (whose global sections are joint distributions) are never distinguished.
- **The sheaf condition (p. 18).** It is stated for "a cover {Uᵢ} of U" with the usual existence and uniqueness of gluing. **No Grothendieck topology on C is specified**, so it is undefined which families are covers.
- **Global sections.** "Γ(F) = ∅. This is the mathematical signature of contextuality" (p. 18).
- **Stochastic mechanics (§7, p. 11).** Nelson's ħ = mσ, with footnote 1: "More standardly one writes ν = ℏ/(2m) … the present notation absorbs numerical factors into σ". The Madelung form ψ = √ρ e^{iS/ħ} gives ∂S/∂t + (∇S)²/2m + V + Q = 0, with Q = −(ħ²/2m)∇²√ρ/√ρ.
- **Scope.** There is no Hilbert-space formalism beyond the Madelung equations. No Born rule, no outcome-selection rule and no multi-particle dynamics appear.

## Key results

The paper has no theorems, propositions or numbered equations. Its content, section by section, with my checks:

- **§§1–2 (pp. 1–5), the history of the claim.**
  - The Kantian "pact" between Newtonian physics and Boolean logic (§1).
  - Bohr's complementarity and Kochen–Specker as the failure of a "globally valid assignment of truth values".
  - Birkhoff–von Neumann quantum logic as keeping "a single overarching logical space", and Reichenbach's three-valued logic as treating indeterminacy probabilistically.
  - EPR as the demand for "a global truth function extending across all measurement contexts" (p. 4). Bohr's reply read as "one cannot form a single Boolean algebra of properties spanning all complementary setups" (p. 5).
  - "The 'nonlocality' that appears in the standard reading of Bell's theorem is thus a symptom of insisting on a global logical structure … rather than direct evidence for superluminal influences" (p. 5).
- **§5 (pp. 7–10), presheaves and logic.** "The internal logic of any category of presheaves is not Boolean but intuitionistic" (p. 9).
  - *My check.* This is true in general. A presheaf topos [C^op, Set] is Boolean iff C is a groupoid, which a context category with non-invertible refinements is not.
  - *The next step is wrong.* The paper then says Boolean logic is "recovered precisely when the presheaf data collapse to a single global section. In that regime the Heyting algebra of truth values becomes Boolean." But the logic of a topos is fixed by the base category (and the topology), not by whether one particular presheaf F has a global section. A classical, globally sectioned presheaf on the same C lives in the same non-Boolean topos, and its subobject lattices are Heyting in general.
- **§6 (p. 10), sheaves as classicality.** "Sheaves thus encode the logical structure presupposed by classical physics: context-independent truth and Boolean reasoning."
  - *My check: false as mathematics.* Sheaf toposes are not Boolean in general. The truth values of Sh(ℝ) are the open sets of ℝ, a non-Boolean Heyting algebra. The paper's own examples of sheaves, "classical EM fields (E, B)" (p. 20), live in exactly such toposes. Booleanness needs a special topology, such as the double-negation one, and the paper names none.
- **§6, "Measurement Reinterpreted" (p. 10), and Appendix A (p. 19): measurement as sheafification.**
  - *What is asserted.* Measurement is "a logical transition from contextual, presheaf-based descriptions to globally consistent, sheaf-like ones". Formally, "For any presheaf F, there is a canonical sheafification F♯, which forces gluing by construction."
  - *What is proved.* Nothing. F♯ depends on a Grothendieck topology J that is never given, and no F♯ is computed for any example.
  - *My checks.*
    - (i) Sheafification is a functor fixed by J. It applies identically to every presheaf, quantum or classical, at every λ. It is deterministic and so cannot select an outcome or produce Born weights, which the paper never addresses.
    - (ii) For the finest reading, where only maximal sieves cover (so every presheaf is a sheaf), F♯ = F and nothing changes.
    - (iii) On Abramsky–Brandenburger's own site (subsets of the measurement set X, with the maximal contexts covering X), consider sheafifying the distribution presheaf D_R ℰ by the plus-construction. It first identifies joint distributions that have the same context marginals, since D_R ℰ is not separated. It then adjoins, as formal elements of F♯(X), all compatible families, i.e. every empirical model, the contextual ones included. So a contextual model becomes a "global section" of F♯ only by being renamed one. It is still not a probability distribution on O^X, and whether it is contextual is unchanged. Sheafification does not create a joint distribution or a KS valuation. It either changes nothing or relabels the data. **"Measurement as sheafification" therefore has no content that would separate it from not measuring.** This is my sketch, not in the paper.
- **§5, "Contextual Multi-Valued Logic" (p. 9); §9 (p. 14); Appendix B (p. 20): the seven-valued logic.** The seven GP values are "true", "false", "indeterminate" (*avaktavyam*, the predicate q) and four mixed cases. Appendix B writes them as (i) ∀x[φ→p], (ii) ∀x[φ→¬p], (iii) ∀x[φ→q], and (iv)–(vii), the conjunctions of these across pairwise non-equivalent conditions φ, φ′, φ″. That is, **the seven nonempty subsets of {p, ¬p, q}**.
  - *What is claimed.* "Formally, these seven values can be organised into a finite Heyting algebra" (p. 9). §9 adds that "they can be represented as subobjects in a presheaf topos … as argued earlier". No such argument appears earlier.
  - *My check.*
    - No order, meet, join, implication or pseudo-complement is given anywhere, so the claim cannot be verified from the paper. It is an assertion.
    - The structure the paper's own Appendix B suggests, nonempty subsets of a 3-set under inclusion, **is not a lattice**: {p} and {¬p} have no common lower bound. Adding a bottom gives the 8-element Boolean algebra 2³, which is Boolean, contrary to "do not collapse to a … Boolean structure".
    - Some 7-element Heyting algebras do exist (any finite distributive lattice is Heyting; e.g. the 7-chain). So a Heyting structure *could* be imposed, but the paper does not say which one. Nor does it say how the truth values would relate to the sieve-valued subobject classifier Ω(C) of a presheaf topos, which the "subobjects in a presheaf topos" remark requires.
- **§7 (pp. 11–12): σ–λ dynamics.**
  - *The equation.* ∂S/∂t + (∇S)²/2m + V + λQ = 0, with 0 ≤ λ ≤ 1 (from Ghose 2002 [27], after Rosen 1964's "classical Schrödinger equation", which has no Q).
  - *λ as a function of σ.* "λ can be regarded as a function of the underlying diffusion, λ = λ(σ)." Large diffusion supports λ ≈ 1, and as diffusion weakens λ → 0. No functional form is given and nothing is derived. With ħ = mσ held fixed, the paper does not say what varies.
  - *The claimed link to logic.* "In the limit λ → 0, the cohomological obstructions vanish, a global section emerges, and classical Boolean logic is effectively restored" (p. 12). This is asserted. No empirical model, presheaf or cohomology group is computed at any λ.
  - *Scope.* The dynamics is single-particle and written in Madelung form. Bell scenarios need entangled multi-particle states, and a λ-scaled quantum potential makes the Schrödinger equation nonlinear. The paper does not discuss what that does to no-signalling. A standard concern is that deterministic nonlinear modifications of quantum mechanics generally allow signalling (Gisin 1990, not held, not read), so this is a gap in the argument, not a result.
  - *Experiment and prediction.* There is none in v2. v1's one empirical pointer (micellar surfactants) was removed, and §10 lists "whether intermediate regimes admit experimental signatures" as future work (p. 16).
- **§8 (pp. 12–13).** Von Neumann's two processes are "reinterpreted as two regimes of description". The measurement problem is "not so much solved as dissolved".
- **§9 (p. 14).** The Jaina *saptabhaṅgī* as a historical analogue. It explicitly disclaims being "a 'source' of quantum logic".
- **§10 (pp. 15–16).** The summary, and v2's quantum-gravity paragraph. Classical GR's recovery from Wheeler–DeWitt is read as "restoration of descent … tied to a continuous classicalization controlled by the σ–λ dynamics", which is asserted.
- **Appendix A (pp. 16–20).** A textbook introduction to categories, functors, natural transformations, adjunctions, presheaves and the sheaf condition. v2 adds the Čech subsection:
  - *The construction.* It takes a cover {Cᵢ → C}, the free abelian presheaf ℤ[F], a 0-cochain s = (sᵢ), and (δs)ᵢⱼ := sⱼ|Cᵢⱼ − sᵢ|Cᵢⱼ. The claims: "Since δ¹∘δ⁰ = 0, the cochain δs is automatically a 1-cocycle, and its cohomology class [δs] ∈ Ȟ¹({Cᵢ}, ℤ[F]) is the obstruction class: if [δs] ≠ 0 then there is no global section".
  - *My check: this is wrong.* δs = δ⁰s is a coboundary, so its class in Ȟ¹ = Z¹/B¹ is **zero for every s**. The criterion "[δs] ≠ 0" can never be met.
  - *δs ≠ 0 does not show contextuality either.* It says only that *this* choice of local sections fails to agree. Another choice might agree.
  - *δs = 0 does not give gluing.* "δs = 0 … in which case the family {sᵢ} pastes to a global section s ∈ F(C)" is true only if F is already a sheaf, which is what is in question.
  - *The cover itself.* The maximal contexts of a contextual scenario cover no context C, because a context containing all of them would be a joint context. So the object C that the example ("e.g. the maximal compatible measurement contexts") needs is not in the category of contexts. Abramsky–Brandenburger avoid this by working over the subsets of the measurement set X, which is not itself a context.
  - *The prose and AMB.* The next paragraph correctly describes AMB: "an obstruction class (built from an abelian presheaf derived from the support of the model) which vanishes whenever a global section exists; hence non-vanishing provides a robust sufficient witness of contextuality [34, 35]". AMB's class is a different object. It is the image of a local section under the connecting homomorphism of a relative-cohomology sequence, not the class of a 0-coboundary. **The paper's displayed construction is not AMB's, and it is trivial.** The AMB characterisation is from general knowledge of [34]; that paper is not held, and I did not read it for this note.
  - *"(a) Classical Physics … Ȟ¹(C, F) = 0 … Examples: classical EM fields, classical trajectories, classical probability distributions" (p. 20).* This is also wrong in two ways.
    - Ȟ¹ of a Set-valued F is not defined. And for an abelian sheaf, H¹ ≠ 0 does not mean failure of gluing (gluing is the H⁰/sheaf condition): nonzero H¹ is about locally trivial but globally twisted data, e.g. line bundles.
    - Classical probability distributions do *not* behave as sheaves. Uniqueness fails: two fair bits that are independent, and two that are perfectly correlated, have the same one-variable marginals. Existence fails too: three bits pairwise perfectly anticorrelated on the cover {a,b}, {b,c}, {a,c} have consistent uniform marginals but no joint distribution, since a ≠ b, b ≠ c, a ≠ c is impossible for bits. This is the classical marginal problem. Both are my checks.
  - *"(b) Quantum or Contextual Physics: Ȟ¹ ≠ 0 … signals … interference phenomena … An example is the Kochen-Specker obstruction [36, 37]" (p. 20).* This is asserted. Interference is not a failure of gluing in any presheaf the paper defines. The KS example is by citation to Isham–Butterfield 1998, which frames KS as no global section of the spectral presheaf, which is an H⁰ statement, not an Ȟ¹ one.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Locality/completeness (EPR) and non-contextuality amount to the existence of a global section of a presheaf of value assignments over measurement contexts | weak (restatement by citation) | §2 p. 5, citing Abramsky & Brandenburger [18]. It is proved there ([LIT-016](../literature.d/LIT-016.md) Thm 8.1), not here. The paper never fixes which presheaf, so it conflates the KS value presheaf and the distribution presheaf |
| C2 | The internal logic of a presheaf topos is intuitionistic | strong (standard fact, asserted) | §5 p. 9, no proof or citation. True: a presheaf topos is Boolean iff the base is a groupoid |
| C3 | Classical physics is the sheaf case, where "Boolean logic is effectively restored"; Boolean logic returns when a presheaf has a global section | unsupported (assertion; false as stated) | §§5–6, 10. A sheaf topos is not Boolean in general (Sh(ℝ)), and the logic of a topos does not depend on one presheaf's global sections |
| C4 | Measurement is the sheafification of presheaf-valued truth | unsupported (assertion) | §6 p. 10, App. A p. 19. No site, topology or F♯ is specified. By my check, sheafification either leaves the data unchanged or adjoins the empirical model itself as a formal section, and it never selects an outcome |
| C5 | Čech cohomology measures the obstruction; [δs] ∈ Ȟ¹({Cᵢ}, ℤ[F]) is the obstruction class | unsupported (the displayed construction is trivial) | App. A p. 19. [δ⁰s] = 0 identically. The correct AMB witness is described in one sentence by citation [34, 35] and not constructed |
| C6 | Classical fields, trajectories and probability distributions satisfy Ȟ¹ = 0 / behave as sheaves | unsupported (partly false) | App. A pp. 18, 20, as a bullet list. Classical distributions violate both gluing axioms (my counterexamples) |
| C7 | The Ghose–Patra seven-valued logic is a finite Heyting algebra, representable by subobjects in a presheaf topos | unsupported (assertion) | Abstract; §5 p. 9; §9 p. 14. No order or operations are given. The subset structure App. B suggests is not a lattice, and completing it gives Boolean 2³ |
| C8 | The σ–λ dynamics (∂S/∂t + (∇S)²/2m + V + λQ = 0, 0 ≤ λ ≤ 1, λ = λ(σ)) continuously carries the presheaf of truth values to a sheaf, making the cohomological obstructions vanish as λ → 0 | unsupported (assertion) | §7 pp. 11–12. The equation is from Ghose 2002 [27]. λ(σ) is not specified, and no presheaf or cohomology group is computed at any λ. There is no multi-particle or Bell-scenario treatment, and no experiment or prediction |
| C9 | Measurement paradoxes (Schrödinger's cat, Wigner's friend) and "nonlocality" are artefacts of an illegitimate demand for global truth, and "the dissolution of the measurement problem and the disappearance of 'nonlocality' … coincide" | weak (interpretive argument) | §§2–3, 8, 10. It is a reading of Bohr, not a derivation. No Bell-violating model is shown to gain a global section, and the Born rule and outcome definiteness are not addressed |
| C10 | Recovery of classical GR from Wheeler–DeWitt is a "restoration of descent" controlled by the σ–λ dynamics | unsupported (assertion) | §10 pp. 15–16, v2 only. It cites Isham–Butterfield 2000 and Raptis 2000 for the gluing idea |
| C11 | The Jaina *saptabhaṅgī* is formally a contextual logic of the same pattern | weak (analogy, explicitly hedged) | §9 p. 14, citing Burch 1964. It disclaims any claim of anticipation |

## Method

A conceptual essay. It reads the history of the measurement problem (Kant, Bohr, EPR, Schrödinger, von Neumann) as a demand for global Boolean truth. It maps that demand onto the existence of global sections, and maps classicality onto the sheaf condition. It then attaches the author's λ-interpolated Hamilton–Jacobi dynamics as the physical carrier of the transition. The mathematics is confined to the appendices, which give definitions only: category, functor, presheaf, sheaf, sheafification and Čech cochains. No computation is made on any example.

## Concepts

- **Measurement context** — "a physically real experimental arrangement: a choice of observables, an arrangement of apparatus, a temporal ordering of interventions, and an environment" (§4, p. 7). Elsewhere it is also a "coarse-graining scale, reference frame, or σ–λ diffusion regime" (p. 18).
- **Refinement morphism** — C → D "by adding compatible observables, increasing resolution, or otherwise sharpening the description". The absence of an arrow means incompatibility (§4).
- **Global truth / global section** — a context-independent valuation. Γ(F) = ∅ is called "the mathematical signature of contextuality" (p. 18).
- **Sheafification** — used in the paper as a name for the passage from contextual to "globally communicable" description, i.e. measurement. It is never constructed.
- **GP seven-valued logic** — the seven *saptabhaṅgī* predications, recast as patterns of truth (p), falsity (¬p) and indescribability (q, *avaktavyam*) across mutually exclusive conditions (App. B). The paper glosses "true-and-false" as "true in some context C₁ and false in another, incompatible context C₂" (p. 20).
- **σ–λ dynamics** — Nelson's diffusion σ (ħ = mσ) together with the scaled Hamilton–Jacobi equation with λQ. λ = 1 is quantum and λ = 0 is classical (§7).

## Connections

- **Abramsky & Brandenburger ([LIT-016](../literature.d/LIT-016.md)), cited as [18].** The paper's formal core *is* [LIT-016](../literature.d/LIT-016.md)'s criterion. The paper acknowledges this only as "closely related" (§2, p. 5) and as a one-sentence summary (p. 19).
  - *What [LIT-016](../literature.d/LIT-016.md) has that this paper lacks.* [LIT-016](../literature.d/LIT-016.md) defines the site precisely: the measurement set X, its subsets, the event sheaf ℰ and the distribution presheaf D_R ℰ. It builds no-signalling into the definition of an empirical model (§2.5). It proves that a global section exists iff a factorizable hidden-variable model does (Thm 8.1). Ghose uses none of this machinery, and in places contradicts it. His cover of "a given context C" by the maximal contexts has no counterpart in [LIT-016](../literature.d/LIT-016.md), where X is not a context. His "classical probability distributions behave as sheaves" conflicts with the fact that D_R ℰ fails gluing even for classical data.
  - *Non-locality.* The paper's reading, that "nonlocality" is "a symptom of insisting on a global logical structure … rather than direct evidence for superluminal influences" (p. 5), does **not** conflict with [LIT-016](../literature.d/LIT-016.md)'s theorems. In [LIT-016](../literature.d/LIT-016.md), non-locality simply *is* the absence of a (nonnegative) global section for a Bell-type cover, a property of the observed statistics. [LIT-016](../literature.d/LIT-016.md) does not attribute it to superluminal influence, and it proves quantum no-signalling for commuting families (Prop 9.2).
  - *Where the paper overreaches.* The conflict is with the paper's own later language, "dissolving … apparent nonlocality" and "the disappearance of 'nonlocality'" (abstract, §10). Under [LIT-016](../literature.d/LIT-016.md)'s definitions, absence of a global section is not dissolved by changing the logic: it is an empirical fact about the data. The paper renames the non-locality without removing it, and it shows no model in which it disappears.
- **Abramsky, Mansfield & Barbosa 2012 [34] and Abramsky et al. 2015 [35], "Contextuality, cohomology and paradox".** These are cited in v2 only, with an accurate one-sentence description, but the construction displayed is not theirs and is trivial (Key results). Neither is held in this record. The contextual fraction ([LIT-265](../literature.d/LIT-265.md)) is not cited.
- **Isham & Butterfield 1998 [36] and 2000 [32]; Döring & Isham.** Isham–Butterfield 1998 (KS as no global section of the spectral presheaf over the context category) is cited only for "an example is the Kochen-Specker obstruction". Isham–Butterfield 2000 is cited only in the quantum-gravity paragraph.
  - *Not cited.* Döring & Isham's topos programme and Heunen, Landsman & Spitters's "Bohrification" (not held, not read here), which is an explicitly Bohrian topos reading of the same idea, are not cited. The latter is the closest prior work to "Bohr's cut as passage from presheaf to classical description", and it constructs its site and internal logic.
  - *Where the record has them.* [LIT-102](../literature.d/LIT-102.md)'s reading already points a reader to Döring & Isham as "a worked formal-language approach". Nothing in this paper goes beyond Isham–Butterfield on KS as a no-global-section theorem.
- **Kochen–Specker contextuality ([LIT-263](../literature.d/LIT-263.md)) and Spekkens contextuality ([LIT-266](../literature.d/LIT-266.md)).** The paper's notion is KS contextuality only, in the Bohrian "truth is context-indexed" gloss. Spekkens's generalized notion is not mentioned.
- **Van Rijsbergen ([LIT-262](../literature.d/LIT-262.md)).** Van Rijsbergen's orthomodular subspace logic is one instance of what the paper dismisses in the Birkhoff–von Neumann programme, which "preserved a global, context-independent logical structure" (§2, p. 4). There is no engagement beyond that remark. [LIT-262](../literature.d/LIT-262.md) is not cited.
- **Knowledge sheaves ([LIT-232](../literature.d/LIT-232.md)), Yoneda ([LIT-221](../literature.d/LIT-221.md)).** There is no connection. The paper uses no cellular sheaves and no Yoneda argument.
- **Arsiwalla et al. ([LIT-102](../literature.d/LIT-102.md)).** A comparable case. Both are programmatic essays that invoke topos and sheaf language for foundations of physics without a construction of their own. Both were read and placed as not worth a reader's time for the formal claim.
- **Anthology.** No ANTH- citation is warranted. The paper has no machine-learning content.

## Bearing on the record

- **[THEORY-012](../theory.d/THEORY-012.md) (Active).** This paper neither supports nor contradicts it. It restates the global-section criterion by citation to [LIT-016](../literature.d/LIT-016.md). It adds no proof, no new scenario and no quantitative content. Nothing in it should be cited as a source for [THEORY-012](../theory.d/THEORY-012.md).
  - *A point [THEORY-012](../theory.d/THEORY-012.md)'s reader should keep.* This paper's slogan "classical = sheaf" is not [THEORY-012](../theory.d/THEORY-012.md)'s claim. [THEORY-012](../theory.d/THEORY-012.md) concerns whether a *particular* compatible family glues to a nonnegative global distribution. It does not say that classical data form a sheaf, which they do not (the marginal-problem counterexample above).
- **[THEORY-014](../theory.d/THEORY-014.md) (Proposed).** There is no bearing. The paper never discusses signed or real-valued sections, or negativity.
- **[THEORY-010](../theory.d/THEORY-010.md) (Proposed), on Grangier & Auffèves's contextual objectivity.** There is a family resemblance: both are ontological or interpretive postulates that "truth/reality is relative to context", motivated by Bohr and KS. [THEORY-010](../theory.d/THEORY-010.md)'s diagnosis applies here too. The paper uses the formal notion ([LIT-016](../literature.d/LIT-016.md)) as motivation and vocabulary, but its own argued consequences (dissolution of collapse, disappearance of nonlocality) are not consequences of contextuality in [LIT-016](../literature.d/LIT-016.md)'s sense. That placement is the record's inference, not the paper's claim, and it does not require filing a new THEORY.
- **[THEORY-011](../theory.d/THEORY-011.md), [THEORY-013](../theory.d/THEORY-013.md), [THEORY-015](../theory.d/THEORY-015.md), [THEORY-016](../theory.d/THEORY-016.md).** There is no bearing. The paper does not engage generalized contextuality, CbD or GPTs.
- **[THEORY-017](../theory.d/THEORY-017.md) (Proposed), its two marked inferences.**
  - *"Contextuality needs more than one basis."* It is consistent with this paper, which says there is "no single experimental context in which both descriptions can be jointly applied" (§2, p. 3). But the paper works without Hilbert spaces or bases and adds no support.
  - *"Boolean structure needs a basis."* The paper asserts the parallel slogan, "Boolean structure needs a global section / a sheaf", and that slogan is false as stated (C3). A reader of [THEORY-017](../theory.d/THEORY-017.md) should not take this paper as corroboration. The correct nearby statement is [THEORY-017](../theory.d/THEORY-017.md)'s own: the projections diagonal in one basis form a Boolean algebra, and the subspace lattice is orthomodular. It is about the base of the lattice, not about gluing.
- **No THEORY should be produced from this paper.** Its only novel claims (C4, C5 as displayed, C7, C8, C10) are unsupported or wrong.
- **ML practice.** It carries nothing. There is no Anthology relevance.
- **For filing.**
  - *Tags proposed.* `quantum-foundations` first. `contextuality` second. `logic` third, for the intuitionistic and multi-valued-logic claims and Birkhoff–von Neumann. `philosophy-of-science` for the Kantian and Bohrian interpretive argument. `mathematics` last, since the formal apparatus is presheaves, sheaves and Čech cohomology, even though it is not used correctly.
  - *Tags not proposed.* `religion` and `metaphysics`: the Jaina section (§9) is about *saptabhaṅgī* as a logic and is one page. `epistemology`: arguable, not chosen.
  - *Status.* Rejected, following [LIT-102](../literature.d/LIT-102.md)'s precedent.

## Limitations

- **No site, no topology, no presheaf.** Every formal claim floats free of a fixed category, Grothendieck topology or presheaf. So "sheafification", "global section" and "Ȟ¹" have no definite referent. Where a referent can be supplied ([LIT-016](../literature.d/LIT-016.md)'s site), the claims either reduce to [LIT-016](../literature.d/LIT-016.md) or fail.
- **The one displayed computation is wrong.** [δs] is zero in Ȟ¹ by construction, and "δs = 0 ⇒ pastes to a global section" presupposes the sheaf property.
- **The Boolean claims confuse two levels.** "Sheaf ⇒ Boolean" and "global section ⇒ Boolean internal logic" conflate the logic of a topos, fixed by site and topology, with a property of one object in it. Both are false in general.
- **The Heyting-algebra claim is asserted, not exhibited.** The natural reading of Appendix B contradicts it.
- **The σ–λ link to contextuality is asserted.** λ(σ) is unspecified. The treatment is single-particle and not applied to any Bell or KS scenario. The paper does not discuss how nonlinearity for λ ≠ 1 bears on no-signalling. There is no experiment or prediction, and v2 removed v1's only empirical pointer.
- **The measurement problem is not addressed at its hard points.** No account is given of which outcome occurs, of the Born weights, or of why and when "globalisation" happens. Calling collapse "a logical projection" (§8) relabels the postulate without replacing it.
- **Bibliographic slips.** Refs [1]–[8] are uncited in v2 (a residue of v1's deleted introduction). The arXiv comment has "om" for "on", describes the v2 change as only "a short section on cohomology", and omits the quantum-gravity addition and the deletions.
- **Disclosed LLM assistance.** The acknowledgement discloses ChatGPT use for language and LaTeX. This is noted, not held against the content.

## Open questions

- **Is there a site (C, J) on a context category for which the ¬¬-style sheafification of the KS value presheaf has global sections, and do they mean anything physically?** The paper would need that computation, not the slogan, to make "measurement as sheafification" a claim. My guess is that any such J either leaves Γ empty or adds only formal sections, but this is unverified.
- **Which 7-element Heyting algebra is the GP logic, if any?** How would it relate to the subobject classifier Ω of a presheaf topos over a concrete context category, for example the Isham–Butterfield poset for a qutrit?
- **What does the λ-scaled, nonlinear Madelung dynamics do to a two-particle Bell scenario?** Does the empirical model at λ < 1 remain no-signalling? Does its contextual fraction ([LIT-265](../literature.d/LIT-265.md)) decrease monotonically as λ → 0? Either computation would give the σ–λ claim testable content.
- **Does the AMB cohomological witness (the real one) track λ?** The paper's own outlook proposes refining "the cohomological analysis of contextuality" and relating it to σ–λ (§10, p. 16). That is not attempted.

## Corrections to the seeded skim

- none (there was no seed or dossier)
- **Identification.** The arXiv abs page lists v1 (Sat 13 Dec 2025, 26 KB) and v2 (Tue 16 Dec 2025, 25 KB). There is no v3. The comment reads "23 pages, no figures; a short section om [sic] cohomology added to Appendix A for completeness", and the category is quant-ph. The only DOI is the arXiv-issued DataCite DOI 10.48550/arXiv.2512.12249. A web search and a Crossref title query found no journal version, so no `doi:` is given. The affiliation is Tagore Centre for Natural Sciences and Philosophy, Kolkata.
- **What v2 changed from v1 (word-level diff of the extracted texts).** The arXiv comment names only the cohomology section. The actual changes go further:
  - *(a) v1's §1 was deleted.* This was "Introduction: Why the Measurement Problem Refuses to Go Away" (~1 p.): von Neumann's two processes, the interpretations (Bohm, Everett, Omnès, Rovelli, QBism) and Wigner's friend. Refs [1]–[8] survive in v2's bibliography but are no longer cited anywhere in the text (v2 cites [9]–[37] only). Sections were renumbered as a result.
  - *(b) v1's §7 claim about Davidson was deleted.* It said that "Davidson has argued that variational formulations of stochastic mechanics allow non-unique (even variable) diffusion, which dovetails with treating σ as a tunable 'quantumness' parameter [28]".
  - *(c) v1's §10 empirical claim was deleted.* It said that "micellar aqueous surfactant systems have been reported to exhibit oscillatory behaviour between quantum-like and classical-like regimes … providing suggestive evidence for a smooth quantum–classical passage", citing Ghose & Mirgorod 2024 (Physics of Wave Phenomena 32, 34–42). **v2 therefore contains no empirical support of any kind.**
  - *(d) A new §10 paragraph was added, "Quantum gravity and the sheafification of spacetime".* It covers Wheeler–DeWitt, the WKB/Born–Oppenheimer route to classical GR, and "restoration of descent", and adds refs [29]–[33] (DeWitt, Kiefer, Kiefer–Wichmann, Isham–Butterfield 2000, Raptis).
  - *(e) The Appendix A subsection "A Čech-cohomological Obstruction to Contextuality" was added.* It adds refs [34] (Abramsky–Mansfield–Barbosa 2012) and [35] (Abramsky et al. 2015). v1 cited neither.
  - *(f) Other changes.* The keyword "Saptabhaṅgī" was added, "proposed by Ghose and Patra" became "Ghose–Patra", most DOIs were stripped from the references, and the acknowledgement was reworded. It still discloses ChatGPT use "for language polishing and assistance with LaTeX formatting".
- **Where the abstract says more than the body.**
  - *"the Ghose–Patra seven-valued contextual logic is exhibited as a finite Heyting algebra."* Nothing is exhibited. The body asserts it (§5 p. 9, §9 p. 14, §10 p. 15), and Appendix B gives only seven first-order formulas, with no order, meet, join or implication.
  - *"Čech cohomology measures the resulting obstruction."* The paper's own cochain construction yields a class that is identically zero (Appendix A, p. 19). AMB's non-trivial construction is only described in one sentence, by citation.
  - *"Measurement is therefore reinterpreted as sheafification."* No site, Grothendieck topology or sheafified presheaf is ever specified. The appendix has one line: "For any presheaf F, there is a canonical sheafification F♯ … presheaf (quantum-like) → sheaf (classical)" (p. 19).
  - *"dissolving … apparent nonlocality."* No Bell-violating model is shown to acquire a global section, at any λ.
  - *"a σ–λ dynamics … provides a continuous interpolation between strongly contextual and approximately classical regimes."* The interpolation is between two Hamilton–Jacobi equations (Ghose 2002, cited). That it interpolates between *contextuality* regimes is asserted (§7, p. 12).
