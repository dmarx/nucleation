---
status: Read
paper: LIT-tmpsu7u7
title: 'Topos Theory and Consistent Histories: The Internal Logic of the Set of All Consistent Sets'
version: 1
history:
- version: 1
  date: '2026-10-01'
  note: >-
    Read in full (Full text of arXiv gr-qc/9607069 v1 (28 Jul 1996, the only
    version; title page dated "26 July 1996", preprint
    Imperial/TP/95–96/55), from the arXiv PDF, 29 PDF pp. (title page plus
    printed pp. 1–28), text extracted with PyMuPDF. Read: abstract, §1
    (introduction), §2 (second-level propositions; sets through time; sets
    varying over a poset, sieves, Ω, characteristic morphisms), §3 (the
    orthoalgebra/decoherence-function formalism, Def. 3.1 and the Lemma on
    d-consistent Boolean subalgebras, the properties of the poset B of
    "windows", Def. 3.2 on sieves), §4 (Def. 4.1 d-realisability and why it
    fails to be a presheaf, Def. 4.2 d-accessibility, the valuation
    morphisms (4.6)–(4.10), Def. 4.3 and the semantic value (4.16) of ⟨α,
    p⟩), §5 (conclusions), Appendix A (Vietoris-style alternative), Appendix
    B (unrealisable propositions), all footnotes and all references. Nothing
    was skipped. Every displayed proof (the Lemma, the sieve and presheaf
    checks, (4.12), (4.17), (B.5)) was followed. The IJTP version of record
    was not read. No dossier existed. No entry for this paper exists in the
    Anthology of the SOTA (grep of record/literature.d for the arXiv id and
    title) or in nucleation.). The first NOTE on this paper, which was
    seeded from its abstract alone.
date: '2026-10-01'
summary: >-
  Isham takes the poset B of all Boolean subalgebras ("windows") of the
  history orthoalgebra UP, ordered by coarse-graining, and shows that the
  presheaf A_d(W) = {α | some d-consistent W′ ⊇ W contains α} is a
  subobject of the constant presheaf ΔUP, whereas the naive "realisable in
  W" assignment is not a presheaf at all (§4.1–4.2). The probability claim
  ⟨α, p⟩ then gets the sieve-valued semantic value {W ⊆ W₀ | ∃
  d-consistent W′ ⊇ W with α ∈ W′} if d(α, α) = p and ∅ otherwise (4.16),
  a global element 1 → Ω in Set^B, so the logic of "all consistent sets at
  once" is the distributive but non-Boolean Heyting algebra of sieves on
  B.
---

# NOTE-tmpbfy9n: Topos Theory and Consistent Histories: The Internal Logic of the Set of All Consistent Sets

## Contribution

The paper gives the first worked use of presheaves over a poset of Boolean contexts to assign generalised, context-relative truth values in quantum theory. Its setting is the consistent-histories formalism. It declines to select one consistent set and keeps them all ("many world-views", §1). Its main result is that the right notion to localise is *accessibility*, not *membership*. "α belongs to a d-consistent window W" is not a presheaf over B, because fine-graining adds propositions but destroys consistency (§4.2). "α lies in some d-consistent fine-graining of W" is a presheaf, a subobject of ΔUP. Its characteristic morphism therefore gives every probability claim ⟨α, p⟩ a sieve-valued semantic value at every window, consistent or not (Def. 4.3, (4.16)). What exists afterwards that did not before is the template the Kochen–Specker series uses: a base of Boolean contexts ordered by coarse-graining, with truth values that are sieves of coarse-grainings, read as "how far must the context be coarsened before this holds".

## Key insight

Coarse-graining a window plays the part of "later time" in Lawvere's sets-through-time (§2.2, p. 19). A proposition that is not yet meaningful at a fine window may become meaningful at a coarser one, and stays meaningful at every coarser one still. The set of coarsenings at which it holds is therefore an upper set, which is a sieve, and sieves form a Heyting algebra. Truth values in a theory with many incompatible Boolean contexts are thus naturally intuitionistic: distributive, but without excluded middle. The logic is fixed by the poset of contexts, not chosen.

## Assumptions

- **History orthoalgebra.** UP is an orthoalgebra of history propositions (fn. 17; Foulis–Greechie–Rüttimann). It has a partial sum ⊕ on orthogonal pairs and a negation with α ⊕ ¬α = 1, and it need not be a lattice. The concrete case kept in view is UP = P(V), the projectors on Hₜ₁ ⊗ … ⊗ Hₜₙ (HPO formalism, §3.1).
- **Decoherence function.** d : UP × UP → ℂ is Hermitian, positive on the diagonal, additive on orthogonal sums, and has d(1, 1) = 1 (§3.1). Only *strong* consistency is considered, d(α, β) = 0 itself rather than its real part (fn. 18).
- **Windows.** B is the set of all Boolean subalgebras of UP, ordered by W₁ ≤ W₂ iff W₁ ⊇ W₂, so that "up" means coarser (§3.2). Its top element is {0, 1}. It has no bottom element.
- **Propensity reading.** The probability in ⟨α, p⟩ is read as a propensity of the universe itself, not as knowledge or frequency (§2.1). This is a declared interpretive choice ("a temptation (to which I shall succumb)"), and none of the mathematics depends on it.
- **Finite sums.** Partitions of unity are finite, and countable sums are set aside (fn. 19).
- **Elementary topos only.** Only presheaves on a poset are used, and category language is kept to footnotes (fn. 5; §5).

## Key results

- **Lemma (§3.1, p. 13).** For a Boolean subalgebra W, d(α, β) = d(α ∧ β, α ∧ β) for all α, β ∈ W iff d(α, β) = 0 for all orthogonal α, β ∈ W. *Proof given* (decompose α = α₁ ⊕ γ, β = β₁ ⊕ γ with γ = α ∧ β and use additivity). This licenses Def. 3.1 (a d-consistent window) as the Boolean-algebra form of Gell-Mann–Hartle strong consistency. On a d-consistent window, d(·,·) restricted to the diagonal obeys the Kolmogorov rules.
- **Poset facts (§3.2).** The join of two windows is W₁ ∩ W₂ (3.8). A meet exists only if the two are Boolean-compatible. Coarse-graining preserves d-consistency, so the d-consistent windows B_d are an upper set. The meet of two d-consistent windows is "generally not" d-consistent, and there is generally no largest consistent coarse-graining of an inconsistent window. The last two are asserted, without an example.
- **Sieves on B (Def. 3.2; (3.9)–(3.13)).** Ω(W₀) is the set of upper sets of coarse-grainings of W₀. It is a Heyting algebra with ∧ = ∩, ∨ = ∪, (S₁ ⇒ S₂) = {W ⊆ W₀ | ∀W′ ⊆ W, W′ ∈ S₁ ⇒ W′ ∈ S₂}, and ¬S = {W ⊆ W₀ | ∀W′ ⊆ W, W′ ∉ S}. Restriction is S ↦ S ∩ ↑(W₂). These are standard facts, stated rather than proved.
- **Realisability fails (§4.1–4.2).** R_d(W) = W if W is d-consistent and ∅ otherwise (4.1). This is not a presheaf on B, because there is no natural map R_d(W₁) → R_d(W₂) for W₁ ≤ W₂. Correspondingly, the candidate value {W ⊆ W₀ | W ∈ B_d, α ∈ W} (4.2) is not a sieve.
- **Accessibility works (Def. 4.2, (4.3)–(4.7)).** A_d(W) = {α | ∃W′ ⊇ W, W′ ∈ B_d, α ∈ W′} satisfies W₁ ≤ W₂ ⇒ A_d(W₁) ⊆ A_d(W₂). It is therefore a subobject of ΔUP. Its characteristic morphism has components χ_W₀(α) = {W ⊆ W₀ | ∃W′ ⊇ W, W′ ∈ B_d, α ∈ W′} (4.6), and α is accessible from W iff χ_W(α) = ↑(W) (4.7). By the adjunction Δ ⊣ Γ (fn. 26), each α gives a global element 1 → Ω (4.8)–(4.10). Since a window contains α iff it contains ¬α, ⟨α, A_d⟩ and ⟨¬α, A_d⟩ are d-semantically equivalent (4.12).
- **Probability claims (Def. 4.3, (4.13)–(4.16)).** The semantic value of ⟨α, p⟩ at W₀ is the accessibility sieve of α if d(α, α) = p, and ∅ otherwise. ⟨α, p⟩ and ⟨¬α, 1 − p⟩ are d-semantically equivalent for all α and p (4.17). The semantic-equivalence classes generate a subalgebra of the Heyting algebra Hom(1, Ω) (p. 22).
- **Appendix A.** The trapping sets T_F(W₀) = {W ⊆ W₀ | W ∈ B_d, F ∩ W ≠ ∅} are used as a subbasis for a Vietoris-like topology τ_d on B. Its open sets form a Heyting algebra that does take the non-sieve values (4.2). This is only sketched and is said to need "a separate theory".
- **Appendix B.** U_d(W) = UP − W for d-consistent W (and ∅ otherwise) is a presheaf. Its Heyting negation is ¬U_d(W) = {0, 1} at every W (B.5), since {0, 1} is a d-consistent coarse-graining of every window. This is the paper's explicit example of a pseudo-complement that is far smaller than the set-theoretic complement.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | A d-consistent window is equivalently one on which d vanishes on orthogonal pairs, and d-consistency is preserved by coarse-graining | strong | Lemma with proof (§3.1); one-line argument (§3.2 item 4) |
| C2 | "α is d-realisable in W" (membership in a consistent window) does not define a presheaf over B, and its candidate semantic value is not a sieve | strong | direct argument (§4.1–4.2); easily checked |
| C3 | "α is d-accessible from W" defines a subobject A_d of ΔUP, with characteristic morphism (4.6) and α accessible iff χ_W(α) = ↑(W) | strong | direct verification (§4.2), plus the standard subobject-classifier correspondence |
| C4 | Each probability claim ⟨α, p⟩ receives a sieve-valued semantic value (4.16) at every window, assembled into a global element 1 → Ω of Set^B | strong | construction (Def. 4.3, fn. 26) |
| C5 | ⟨α, p⟩ ≡ ⟨¬α, 1 − p⟩ and ⟨α, A_d⟩ ≡ ⟨¬α, A_d⟩ semantically, for every d | strong | (4.12), (4.17), proof given |
| C6 | The sieves on any window form a Heyting algebra, so the logic of the many-world-views picture is distributive but not Boolean, an "intuitionistic" logic rather than quantum logic | moderate | standard topos theory, cited (Bell 1988, Mac Lane–Moerdijk), with the operations written out (3.10)–(3.12); non-Booleanness is not shown for B specifically, though it is immediate whenever B has a window with a proper coarse-graining |
| C7 | Topos theory is "the natural mathematical tool" for the internal logic of consistent histories when all consistent sets are kept | weak | motivation by analogy (sets through time, §2.2) and the success of C3–C4; no alternative is compared except Appendix A, which the author sets aside |
| C8 | The resulting interpretation is a "neo-realism", subtler than classical realism but stopping short of non-distributive quantum logic | weak | interpretive assertion (§5) |
| C9 | Accessibility between windows is an analogue of Kripke's relative possibility, so modal notions should have a natural home here | weak | remark, explicitly left to future work (§5) |
| C10 | The construction could be applied profitably to the Kochen–Specker theorem and to relational quantum theory | weak | one-sentence suggestion (§5); realised for KS by the later series, not here |

## Method

1. Classical warm-up (§2.1): for a measure μ on a Boolean algebra, second-level propositions ⟨α, p⟩ get {0, 1} valuations V^μ⟨α, p⟩ = [μ(α) = p]. Semantic equivalence is equality of valuations for all μ.
2. Sets through time (§2.2): with D(t) the dead at time t, the value of "x is mortal" at t₀ is {t ≥ t₀ | x ∈ D(t)}, an upper set. Upper sets form a Heyting algebra.
3. Generalise to presheaves on a poset P (§2.3): sieves, Ω, characteristic morphisms χ_p(x) = {q ≥ p | X_pq(x) ∈ A(q)}, and the negation of a subobject of a constant presheaf (2.17)–(2.18).
4. Specialise P to B (§3): define d-consistent windows, and record B's order structure.
5. Find the right subobject of ΔUP (§4): realisability fails, accessibility works. Take its characteristic morphism and transpose it to global elements of Ω. Add the probability filter d(α, α) = p.

## Concepts

- **Window.** Any Boolean subalgebra of UP, a possible "world-view" (§3.1, p. 13). A d-consistent window is Griffiths's "framework".
- **Coarse-graining / fine-graining.** W₂ is a coarse-graining of W₁ (W₁ ≤ W₂) iff W₂ ⊆ W₁. Each window counts as both a coarse- and a fine-graining of itself.
- **Second-level proposition ⟨α, p⟩.** "History proposition α is true with probability p", a proposition about the universe that contains a proposition of UP (§2.1).
- **Global proposition.** A second-level proposition that makes no reference to a window. It must be "localised" to windows before it can be evaluated (§4.2).
- **d-realisable / d-accessible / d-unrealisable.** α ∈ W with W d-consistent (Def. 4.1) / α in some d-consistent W′ ⊇ W (Def. 4.2) / α ∉ W with W d-consistent (App. B). Only the second is the paper's semantics. Accessibility implies that W itself is d-consistent (fn. 23).
- **Semantic value.** The sieve assigned at a stage, the author's preferred term for "truth value" (§1, p. 3).
- **d-semantic equivalence.** Two global propositions are equivalent when they map to the same global element of Ω for the given d. Only the equivalence classes carry the logic (§4.2).
- **Sieve.** Bell's convention: an upper set of coarse-grainings of W₀. Mac Lane–Moerdijk call this a cosieve (fn. 14).

## Connections

- **Kochen–Specker series, part I ([LIT-325](../literature.d/LIT-325.md), [NOTE-271](NOTE-271.md)).** KS I names this paper as a motivation. The two share their base: KS I's poset W of Boolean subalgebras of the projection lattice, ordered by coarse-graining, is B here with UP = P(H) and one time point. They also share the reading of a sieve as "the coarse-grainings at which the claim holds". They differ in three ways, and these are what the series adds.
  - *Propositions are coarse-grained, not only contexts.* Here the presheaves are subobjects of the *constant* presheaf ΔUP, so α is never changed as the window shrinks. KS I's coarse-graining presheaf G sends a proposition to its coarse-grained version at the coarser context (later called daseinisation, [NOTE-271](NOTE-271.md)).
  - *A state supplies the sieve.* Here d decides which windows are consistent, and the value of a claim is about meaningfulness. In KS I, ρ decides which coarse-grained propositions are certain, and the value is about truth.
  - *The no-go result.* KS I adds the dual presheaf Hom(W, {0,1}) and its lack of global sections. Nothing here corresponds to that.
- **Part II ([LIT-381](../literature.d/LIT-381.md), [NOTE-329](NOTE-329.md)).** Part II argues that sieve-valued valuations are generic to any presheaf of propositions, and that the logic is fixed by the base category. Both are already the stance here (§2.3, §5), argued here by analogy with sets through time instead of Theorem 4.1 of part II. This paper's App. B result ¬U_d = {0, 1} is a concrete instance of what [NOTE-329](NOTE-329.md) checks for classical microstates: a presheaf with plenty of global sections whose subobject logic is still non-Boolean.
- **Parts III–IV ([LIT-380](../literature.d/LIT-380.md), [LIT-382](../literature.d/LIT-382.md); [NOTE-327](NOTE-327.md), [NOTE-328](NOTE-328.md)).** No direct relation. The move to abelian von Neumann subalgebras, Gelfand spectra and interval valuations has no counterpart here. Part IV's "support ≤ coarse-grained proposition" form of the truth value is the state-based analogue of this paper's "some consistent fine-graining contains α".
- **Döring–Isham ([LIT-343](../literature.d/LIT-343.md), [LIT-335](../literature.d/LIT-335.md), [LIT-299](../literature.d/LIT-299.md), [LIT-310](../literature.d/LIT-310.md); [NOTE-277](NOTE-277.md), [NOTE-292](NOTE-292.md), [NOTE-290](NOTE-290.md), [NOTE-285](NOTE-285.md)).**
  - *Citation.* [LIT-343](../literature.d/LIT-343.md) cites this paper ("see also [20, 27]") alongside the KS series as earlier topos work.
  - *Neo-realism.* The term is first used here (§5), not in [LIT-343](../literature.d/LIT-343.md) (see corrections).
  - *Histories.* The later programme returns to histories only in passing. The one-volume version ([LIT-378](../literature.d/LIT-378.md), §3) remarks that a time-labelled PL(S) would suit the HPO consistent-histories formalism, and cites this paper as [40]. Nothing in [LIT-343](../literature.d/LIT-343.md), [LIT-335](../literature.d/LIT-335.md), [LIT-299](../literature.d/LIT-299.md) or [LIT-310](../literature.d/LIT-310.md) reconstructs the window poset B or the accessibility semantics.
  - *Context posets.* [LIT-378](../literature.d/LIT-378.md)'s Boolean-subalgebra base category (§5.5.3, per its status note) is the single-time W of KS I, not B.
- **Butterfield & Isham, "Some possible roles for topos theory" (this batch, Isham & Butterfield 1999).** That essay's §3.6 discusses consistent histories, but only the continuous-time history algebra and synthetic differential geometry. It neither cites nor summarises this paper.
- **Kripke semantics.** §5's "relative possibility" remark is the same analogy part II defers to a planned paper on Kripke–Beth semantics ([NOTE-329](NOTE-329.md), Connections).
- **Anthology of the SOTA.** No entry. Nothing in this paper bears on ML practice.

## Bearing on the record

- **[THEORY-024](../theory.d/THEORY-024.md) (Rejected: Boolean logic restored when a presheaf acquires a global section).** This paper is the earliest source in the record against that claim, and the cleanest.
  - *Global sections, non-Boolean logic.* ΔUP is a constant presheaf with a global section for every α. Yet its subobjects A_d and U_d receive non-trivial sieve values. The general negation of a subobject of a constant presheaf (2.17) satisfies A ⊆ ¬¬A, with equality failing (2.18). Appendix B's ¬U_d(W) = {0, 1} is an explicit failure of excluded middle.
  - *What decides the logic.* The paper says the Heyting algebra's "structure is determined by the space B" (abstract). It also states the criterion that a Heyting algebra is Boolean iff a = ¬¬a for all a (§2.2).
  - *Suggestion.* [THEORY-024](../theory.d/THEORY-024.md) could add this paper to its refuting readings, beside [LIT-325](../literature.d/LIT-325.md) §6.
- **[THEORY-020](../theory.d/THEORY-020.md) (Stone; a single Boolean context is classical, and the obstruction lies in how contexts overlap).** Consistent, and a probabilistic analogue.
  - *Each context alone.* Every d-consistent window carries ordinary Kolmogorov probability (§3.1, p. 11).
  - *Where non-classicality sits.* It sits entirely in the fact that windows cannot all be combined: B has no least element, and the meet of two consistent windows need not be consistent (§3.2).
  - *The gap.* The paper never mentions Stone, two-valued homomorphisms or ultrafilters, and its obstruction is to *joint consistency*, not to joint valuations. It shows the pattern of [THEORY-020](../theory.d/THEORY-020.md) in a different setting; it is not a source for the Stone claim.
- **[THEORY-037](../theory.d/THEORY-037.md) (Proposed: Sub_cl(Σ) is Heyting with pseudo-complement negation).** No direct bearing. The paper writes out implication and negation in full, but for sieves on B ((3.11)–(3.12)) and for subobjects of a constant presheaf ((2.17)), not for clopen sub-objects of a spectral presheaf. It cannot meet the promote_when. It does pre-date and support the THEORY's contrast between a distributive, intuitionistic logic and quantum logic proper (§1, p. 2; §5).
- **ML practice.** It carries nothing for ML practice and does not belong in the Anthology.
- **For filing.**
  - `quantum-foundations` first: consistent histories, interpretation.
  - `logic`: Heyting-valued semantics.
  - `contextuality`: context-relative truth over a poset of Boolean contexts, though not Kochen–Specker contextuality.
  - `mathematics`: presheaves on a poset.
  - `philosophy-of-science`: the many-world-views and neo-realism discussion, and the propensity reading.

## Limitations

- **The Heyting values carry no probabilistic information.** The decoherence function assigns α one number d(α, α) regardless of window, so (4.16) factorises as [d(α, α) = p] ∧ (accessibility sieve of α). The probability part is two-valued. What is contextual and many-valued is only whether α can be placed in some consistent set. The abstract's phrase that the truth values "of such contextual predictions" lie in a Heyting algebra is accurate, but readers may hear more in it than is there.
- **The motivating problem is not engaged.** The motivation is the plethora of mutually incompatible consistent sets, and Kent's "consistent sets contradict" is cited (§1). Nothing in the construction addresses retrodictions that are certain in one consistent set and contrary in another. The semantics tells you where α is meaningful, not how to reconcile what different windows say about it.
- **"Natural" is argued by analogy.** The naturalness of the topos framework (C7) rests on the sets-through-time analogy and on accessibility being the first candidate that forms a presheaf. Appendix A shows a non-presheaf alternative exists and is set aside without comparison.
- **Several claims are asserted without example or proof.** These are the claims about meets of consistent windows (§3.2), the Heyting structure of Ω(W₀) (cited as standard), and the Zorn's-lemma remark on descending chains. The last is not needed: an ascending chain of Boolean subalgebras has its union as a lower bound. None of these affects the main construction.
- **Small slips that do not affect the results.**
  - On p. 9, "(2.21) simplifies to" should read "(2.20) simplifies to".
  - Appendix B's definition is numbered "Definition 2.1".
  - The fn. 22 phrase "this does affect" should read "does not affect".
- **No concrete computation.** No example system, decoherence function or window poset is computed. The conclusion says analysing B for UP = P(V) "is a viable concrete task" (p. 22) and leaves it undone.

## Open questions

- Is there a semantics in which the *probabilities themselves* vary with the window? This would need something other than a single decoherence function, or a value object other than [0, 1]. Butterfield–Isham 1999 §1.3 later raises non-real-valued probabilities, and the Döring–Isham programme's later work on probabilities would be the place to look; it is not in the record.
- What is the logic of B for the HPO case UP = P(Hₜ₁ ⊗ … ⊗ Hₜₙ)? For example, does Ω(W₀) have atoms, and how does accessibility interact with the tensor structure? Not attempted.
- Can the Kripke-style accessibility between windows (§5) be turned into a modal logic of consistent histories with stated frame conditions? Posed, not settled.
- Does a Kochen–Specker-type obstruction exist for history propositions, i.e. no global section of Hom(W, {0,1}) over B? The paper's final remark points toward the question but does not pose it in this form. A proof or counterexample over B would settle it.

## Corrections to the seeded skim

- none (there was no seed or dossier)
- The batch description ("the series' stated motivation (KS I cites it as [13])") is confirmed. KS I §1 says its procedure "was partly motivated" by this paper, which showed "how a topos framework fits naturally with the multi-branched, coarse-graining operations" of consistent sets. The paper itself mentions Kochen–Specker only once, as future work, in its last paragraph (p. 23): "the well-known contextuality of truth values in standard quantum theory (i.e., the Kochen–Specker theorem) could be explored profitably from this perspective". It contains no spectral or dual presheaf, no valuation of UP, and no no-global-section statement.
- The record attributes the coining of "neo-realism" to Döring–Isham: [LIT-343](../literature.d/LIT-343.md) fn. 6 says "We coin the term 'neo-realist'", and [NOTE-277](NOTE-277.md) reports that the paper "calls the stance 'neo-realism'". The term is already here, with the same meaning, in 1996: the many-windows interpretation "corresponds to a type of neo-realism" that is more subtle than classical realism but stops short of the non-distributive structure of quantum logic (§5, p. 23). The record's notes do not claim priority for [LIT-343](../literature.d/LIT-343.md), but anything that does should cite this paper.
