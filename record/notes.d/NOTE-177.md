---
number: 177
status: Read
formerly:
- NOTE-tmpxbdb6
paper: LIT-145
title: 'Turner — Ultrafilters as Propositional Theories'
version: 2
history:
- version: 2
  date: '2026-09-26'
  note: >-
    Read in full (full text of the author's preprint "Ultrafilters as
    Propositional Theories" (dated November 20, 2021; 22 pp., §§1–4 plus
    references), from the author's website, every page and every proof. The
    published Philosophy Compass version (2025, e70047) was not reachable
    (Wiley PDF and landing pages returned 403); I compared it only through
    its Crossref abstract, which differs from the preprint in at least one
    respect (see corrections). Claims below are about the preprint.).
    Upgraded from `Skimmed` to `Read`: the claims table, assumptions and
    results are new, and the skim is corrected where the full text
    disagreed.
date: '2026-09-26'
summary: >-
  An expository piece that redefines a filter over a set W as a
  "propositional theory" (a set of W-propositions closed under pairwise
  conjunction and implication, not containing ∅), proves maximal ⇔ prime ⇔
  ultra (Thm 2), the ultrafilter extension theorem as a propositional
  Lindenbaum's lemma (Thm 3, assuming choice), Łoś's theorem M_T,[A] ⊨ φ
  iff ⟦φ⟧_A ∈ T for ultraproducts of "intensional spaces" (Thm 9), and
  first-order compactness from it (Thm 12); "None of the results are
  novel" (p. 2).
---

# NOTE-177: Turner — Ultrafilters as Propositional Theories

## Contribution

Nothing new is proved. The contribution is a translation. The standard set-theoretic definition of a filter over I (a family of subsets closed under intersection and superset, excluding ∅) is recast as a propositional theory over a set of "worlds" W, where ∩ is conjunction, complement is negation and ⊆ is implication. The chain filter → ultrafilter → ultraproduct → Łoś → compactness is then worked through in that vocabulary, with each step paired with the syntactic proof philosophers already know: the extension theorem with Lindenbaum's lemma, and Łoś's theorem with Henkin's completeness proof.

## Key insight

A filter is a finitely consistent propositional theory, and an ultrafilter is a finitely consistent, negation-complete one. With that reading, Łoś's theorem is Henkin's construction done with propositions instead of sentences. You extend to a maximal (ultra) theory, then build a model whose domain is equivalence classes of world-to-object functions (W-individual concepts), where Henkin used constants. The model makes true exactly what the theory "says". Because the construction only needs *finite* conjunction closure, it turns finite satisfiability into satisfiability, which is compactness, with no detour through proof theory.

## Assumptions

- W is a non-empty set of indices ("worlds"; they need not be possible worlds). Each world is "classically logical": there is a model M_w with φ true at w iff M_w ⊨ φ (§1.1). §3.2 formalises this as an intensional space 𝒲 = ⟨W, i⟩ over a first-order language L, with i(w) = M_w = ⟨D_w, I_w⟩ and D_w non-empty.
- L has primitives ∼, ∧, ∃, =, a fixed stock of names and predicates, and infinitely many variables (§3.1).
- A filter over W is a set T ⊆ 𝒫(W) with (i) p, q ∈ T ⇒ p ∩ q ∈ T; (ii) p ∈ T and p ⊆ q ⊆ W ⇒ q ∈ T; (iii) ∅ ∉ T (§1.2.1). An ultrafilter also satisfies p ∈ T or W − p ∈ T for every p ⊆ W.
- **Axiom of choice**, which Turner flags explicitly: to well-order 𝒫(W) in Thm 3 (p. 7; needed whenever W is infinite, since 𝒫(W) is then uncountable); to choose witnesses g(w) in the ∃ step of Thm 9 (p. 20); and to pick one model M_w per finite subset in Thm 12 (p. 20).
- Names are interpreted as non-rigid individual concepts, following Carnap (1956) rather than Kripke (p. 11).

## Key results

- **Filter ⇔ filter\*** (§1.2.2, p. 4): T is a filter iff (i\*) p ∩ q ∈ T ⇔ p ∈ T and q ∈ T, and (ii\*) T ≠ 𝒫(W).
- **Theorem 2** (p. 5): for a filter T, maximal ⇔ prime (p ∪ q ∈ T iff p ∈ T or q ∈ T) ⇔ ultra (negation-complete).
- **Lemma 4** (p. 7): with the addition T + p = {q ⊆ W : ∃a ∈ T, a ∩ p ⊆ q}, T ⊆ T + p, p ∈ T + p, T + p is closed under conjunction and implication, and T + p is a filter iff −p ∉ T.
- **Theorem 3, Central Theorem on Ultrafilters** (p. 6, proof p. 8): every filter extends to an ultrafilter. The proof is transfinite recursion over an ordinal enumeration of 𝒫(W): T_{α+1} = T_α + p_α if that is a filter and T_α otherwise, with unions at limits. It is presented as the propositional analogue of Lindenbaum's lemma.
- **Propositions 5–7, Lemma 8** (pp. 13–15): ⟦·⟧_A commutes with the truth functions; φ ⊨ ψ implies ⟦φ⟧_A ⊆ ⟦ψ⟧_A, but not conversely, since W may omit countermodels (p. 13); ⟦φ⟧_{A[g▷x]} ⊆ ⟦∃xφ⟧_A; and a substitution lemma ⟦φ(x⃗)⟧_{A[⦇α⦈_A ▷ x⃗]} = ⟦φ(α⃗)⟧.
- **Ultraproduct** (p. 17): M_T = ⟨D_T, I_T⟩ with D_T the ≡_T-classes of W-individual concepts, where g ≡_T h iff T "says" g = h; I_T(α) = [⟦α⟧]; I_T(Π) = {[g⃗] : g⃗ T-satisfy Π}. This is ∏_{w∈W} M_w / T. Proposition 10 (well-definedness) needs only that T is a filter. For a mere filter the construction is a *reduced product* (p. 19).
- **Theorem 9, Łoś's theorem** (p. 18, proof pp. 19–20): for an ultrafilter T and any W-assignment A, M_T, [A] ⊨ φ iff ⟦φ⟧_A ∈ T. Only the negation step uses ultra-ness.
- **Theorem 12, Compactness** (pp. 20–21): if every finite subset of Γ has a model, Γ has one. Take W = the finite subsets of Γ, with M_w ⊨ w. The filter is T = {p ⊆ W : ⟦⋀Δ⟧ ⊆ p for some finite Δ ⊆ Γ}; extend it to an ultrafilter and apply Thm 9.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Filters over W are exactly the W-propositional theories closed under pairwise conjunction and implication and excluding the impossible proposition; the textbook definition and this one coincide | strong | definitional unpacking (p. 3) plus proof of equivalence with filter\* (p. 4) |
| C2 | For filters, maximality, primeness and ultra-ness are equivalent | moderate | Theorem 2 proof (p. 5); the maximal ⇒ prime step is gappy (see Limitations), though the result is standard |
| C3 | Every filter extends to an ultrafilter (given choice) | strong | Theorem 3 by transfinite recursion with Lemma 4 (pp. 7–8); standard result |
| C4 | The Central Theorem is "essentially the same" as Lindenbaum's lemma | moderate | informal argument comparing the two constructions (p. 6); an analogy, not a formal reduction |
| C5 | Łoś's theorem: M_T,[A] ⊨ φ iff ⟦φ⟧_A ∈ T for ultrafilters T | strong | proof by induction on formulas (pp. 19–20), resting on Lemma 11 and Prop. 10; standard result, with minor slips in the write-up |
| C6 | Łoś's theorem is the propositional counterpart of Henkin's completeness proof, with W-concepts in place of constants and no witness axiom needed | moderate | informal argument (pp. 16–17) |
| C7 | Compactness follows purely model-theoretically, with "no detour through proof theory" | strong | Theorem 12 proof (pp. 20–21); standard; contains a ∩/∪ slip |
| C8 | Ultrafilters are "a common gap" in philosophers' technical training and are skipped by the standard philosophy logic texts | weak | assertion backed by a footnote survey of six textbooks (fn. 1, p. 1) |
| C9 | Ultrafilters are "a powerful technical tool that philosophers can put to good use" | weak | assertion; no philosophical application is given in the paper |

## Method

The method is a dictionary plus re-proof. Filter-theoretic notions are mapped onto propositional ones (∩ as conjunction, complement as negation, ⊆ as implication, ∅ as the impossible, W as the necessary). Then each theorem is proved in that vocabulary, alongside the familiar syntactic argument it mirrors: Lindenbaum for the extension theorem, and Henkin's term model (with identity handled by equivalence classes) for Łoś. The one new piece of apparatus is the intensional space ⟨W, i⟩. Every model in it interprets the same language L, so intensions of predicates and names, and "W-assignments" of individual concepts to variables, can be defined. Turner gives three interchangeable presentations of a W-assignment (§3.3, pp. 12–13). This machinery is what lets a propositional theory "say" that some individual concepts satisfy a formula (T-satisfaction, p. 16), from which the ultraproduct's extensions are read off.

## Concepts

- **W-proposition**: any subset of W. Conjunction is ∩, negation is complement in W, and p implies q iff p ⊆ q.
- **W-propositional theory**: any set of W-propositions.
- **Filter**: a theory closed under pairwise (hence finite) conjunction and implication that does not contain ∅. It is "something like" a consistent theory, but only finitely consistent (p. 3). What textbooks call a "proper filter" (fn. 2, Chang & Keisler).
- **Ultrafilter**: a negation-complete filter; equivalently maximal or prime.
- **Addition T + p**: {q : ∃a ∈ T, a ∩ p ⊆ q}, the closure of T ∪ {p} under conjunction and implication.
- **Intensional space**: ⟨W, i⟩, where i assigns each world a model of a fixed language L.
- **W-individual concept**: a function g with g(w) ∈ D_w. The domain of the ultraproduct is made of their equivalence classes.
- **T-satisfies**: g⃗ T-satisfy φ iff ⟦φ⟧_{A[g⃗▷x⃗]} ∈ T for any A. This is what theory T "says" about those concepts.
- **Ultraproduct / reduced product**: M_T built from an ultrafilter / a merely filter T.

## Connections

The logical question is how an algebraic, set-theoretic construction (filters, ultraproducts) relates to the logician's notions of consistent theory, maximal extension and model existence. The position taken is that it is the same construction in a different vocabulary. Ultrafilter extension is Lindenbaum's lemma for propositions, and Łoś's theorem is Henkin's completeness proof with individual concepts as the term model. This sits squarely in the `logic` tag's "propositional and model-theoretic structures, proof and consequence"; `logic` is justified and should lead. `mathematics` (set theory and model theory "read for itself") is also justified. The work does not carry and does not merit `philosophy-of-language`. It uses Carnapian intensions only as a device, disclaims modal semantics (p. 11), and treats the identification of ⟦φ⟧ with a genuine proposition as a "pretense" that helps with the model theory (p. 15).

Its sources are textbook: Chang & Keisler 1990 (the standard treatment it aims to make accessible), Henkin 1949, Carnap 1956, and Kripke 1972 (as the view it sets aside). On held works: nothing else in nucleation's literature.d mentions ultrafilters, ultraproducts, Lindenbaum, Łoś or compactness. The nearest held neighbour is [LIT-163](../literature.d/LIT-163.md) (philosophy of probability), which shares no content with it.

## Bearing on the record

It carries nothing for ML practice. It is a logic primer with no computational or learning content, and there is no Anthology of the SOTA document it bears on. Within nucleation it is a reference primer. It becomes useful if the record takes up works that use ultraproducts, non-standard models or compactness arguments in metaphysics, philosophy of mathematics or formal epistemology. The skim's framing, that without a `logic` topic the work was a candidate to drop as out of scope, no longer applies. No THEORY document is supported or contradicted.

## Limitations

- Expository by design: "None of the results are novel" (p. 2). No philosophical application is shown, although the introduction says ultrafilters are a tool "philosophers can put to good use" (C9).
- Only the 2021 preprint was read. The published 2025 abstract omits compactness, so the published text may differ in scope. Unverified.
- Slips in the preprint's proofs (the results are standard and correct; the write-up is not flawless):
  - Thm 2, maximal ⇒ prime (p. 5): the argument that one of p, q "could be added to T" because p ∪ q is non-empty does not establish it. The needed step is Lemma 4(iii): if neither T + p nor T + q is a filter, then −p, −q ∈ T, so −(p ∪ q) ∈ T alongside p ∪ q, which is a contradiction. That lemma is only proved later.
  - Thm 3 (p. 8): Tγ is called "the union of all the T_α's", but the recursion defines it that way only if γ is a limit ordinal. Harmless, but unstated.
  - Thm 9, conjunction step (p. 19): it cites "condition (ii\*)" where the conjunction-completeness condition (i\*) is meant.
  - Thm 9, ∃ direction (p. 20): g is defined only on ⟦∃xψ⟧_A and must be extended arbitrarily elsewhere (domains are non-empty). The step from "each w ∈ ⟦∃xψ⟧_A is in ⟦ψ⟧_{A[g▷x]}" to "⟦ψ⟧_{A[g▷x]} ∈ T" needs closure under implication, which is left implicit.
  - Thm 12 (p. 21): "Δ ∩ Σ is also finite, so ⟦⋀(Δ ∩ Σ)⟧ = ⟦⋀Δ⟧ ∩ ⟦⋀Σ⟧" should read Δ ∪ Σ. The last paragraph also writes M_T and "∈ T" where the ultrafilter T′ is meant.
  - Minor typos: "ultrafilter" for "filter" (p. 3), "W + p" for "T + p" (p. 7), "r is also in T" for "T + p" (p. 7), the intension of a name defined as "⟦Π⟧(w) = I_w(α)" where ⟦α⟧ is meant (p. 11).
- The "propositions" are sets of indices, not propositions in any metaphysically serious sense, and the author says so (p. 15). The philosophical accessibility is pedagogical, not a thesis about propositions.

## Open questions

- Does the published 2025 version keep §4.2 (compactness), and does it correct the proof slips listed above? A reading of the Wiley version of record would settle it.
- Which philosophical uses of ultrafilters does Turner have in mind? The paper names none. A companion application (e.g. non-standard models in philosophy of mathematics, or ultraproduct constructions in modal or formal epistemology) would show whether the propositional reading does work beyond teaching.

## Corrections to the seeded skim

- The skim says "The closed vocabulary has no logic topic … the vocabulary wants `logic`". Stale: `logic` now exists ("propositional and model-theoretic structures, proof and consequence") and is the work's first tag.
- Page ranges in the skim are off: §3 "Intensional Spaces" runs pp. 9–16, not 9–18; §4 (Łoś's theorem) begins on p. 16, not p. 18 (proof §4.1 pp. 18–20, compactness §4.2 pp. 20–21).
- The skim and the LIT say the published abstract presents compactness as an application. The Crossref abstract of the 2025 version does not mention compactness; it ends with Łoś's theorem ("the ultraproduct of an ultrafilter makes true all and only the sentences which express propositions in the ultrafilter"). Whether §4.2 survives into the published version is unverified. Compactness is an application in the 2021 preprint.
- The LIT's summary reads a filter as "consistent … and, for an ultrafilter, negation-complete". Right, but the paper stresses (p. 3) that a filter is only *finitely* consistent: it can contain an "essentially infinite contradiction" (at least n Fs for every n, plus "only finitely many Fs"). That is the point of the notion, and "consistent" should be read as "contains no ∅ and closed under finite conjunction".
- The skim says Łoś's theorem applies to "each world agreeing with some classical model". In §3 this becomes a definition, the *intensional space* ⟨W, i⟩, with i(w) a model of a fixed first-order language L. Names get non-rigid Carnapian individual concepts, explicitly not Kripkean rigid designators (p. 11).
- philosophy-of-language tag: not carried and correctly so. §3's intensions and what a theory "says" borrow the apparatus, but Turner disclaims modal semantics ("we're doing logic here, not modal semantics", p. 11) and calls the reading of ⟦φ⟧ as a proposition a "pretense" (p. 15).
- logic tag: justified. mathematics tag: justified. Primary topic `logic` is right.
