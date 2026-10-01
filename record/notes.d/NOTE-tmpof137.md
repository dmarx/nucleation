---
status: Read
paper: LIT-tmpf4hde
title: 'A Topos Perspective on the Kochen-Specker Theorem: II. Conceptual Aspects, and Classical Analogues'
version: 1
history:
- version: 1
  date: '2026-10-01'
  note: >-
    Read in full (Full text of arXiv quant-ph/9808067 v2 (8 Nov 1998; v1 was
    31 Aug 1998, the arXiv comment on v2 being "Small changes and
    corrections"), from the arXiv PDF, 39 PDF pp. (title page plus printed
    pp. 1–38). The title page is dated "31 August 1998", with a footnote
    "Small corrections added in October 1998". I read the abstract, §1
    (introduction), §2 (review of Part I: §2.1 categories, presheaves and
    subobjects; §2.2 sieves, Ω, global and partial sections; §2.3 the
    applications to quantum physics, i.e. KS on O_d, partial → generalised
    valuations, the coarse-graining presheaf, valuations from states), §3
    (classical physics: §3.1 the category M and the value presheaf Υ,
    quantisation as a functor; §3.2 macrostates; §3.3 the classical
    generalised valuations), §4 (§4.1 generalised FUNC and Theorem 4.1; §4.2
    comparison functors and coarse-graining presheaves on any small
    category), §5 (§5.1 the intuitive argument from partial truth; §5.2 its
    assessment), §6 (conclusion), the acknowledgements and all 6 references.
    Nothing was skipped. The text was extracted with PyMuPDF; the
    commutative diagrams (2.2)–(2.3) were reconstructed from the surrounding
    text. I followed the one proof given (Theorem 4.1) and checked by hand
    several of the verifications the paper leaves to the reader (that ν^R of
    eq. 3.10 is a sieve and obeys FUNC, null and exclusivity; that ν^s of
    eq. 3.15 is principal iff Ā(s) ∈ Δ). The IJTP version of record was not
    read. Bibliographic data were checked against the arXiv abstract page
    and Crossref. There is no Anthology of the SOTA entry for this paper
    (searched the anthology's literature.d for the arXiv id and title). This
    is part II of the series whose part I is LIT-325, read as one series
    with Hamilton, Isham & Butterfield (2000, part III) and Butterfield &
    Isham (2002, part IV).). The first NOTE on this paper, which was seeded
    from its abstract alone.
date: '2026-10-01'
summary: >-
  Butterfield & Isham argue that the sieve-valued "generalised valuations"
  of part I are not a quantum peculiarity but the natural valuations for
  any presheaf of propositions on any small category. Three supports are
  offered. (1) Classical physics: the value presheaf Υ(Ā) = Ā(S) on the
  category M of measurable functions has global sections (one per
  microstate, eq. 3.7), yet a macrostate R ⊆ S yields a sieve-valued
  valuation ν^R(A ∈ Δ) = {f_M | B̄(R) ⊆ f(Δ)} (eq. 3.10) with the same
  FUNC property as the quantum ν^ρ. (2) A proof that a sieve-valued
  valuation on any presheaf G obeys generalised FUNC, ν(B, G(f)(d)) =
  f*(ν(A, d)), iff it is a natural transformation G → Ω, i.e. a subobject
  of G (Theorem 4.1). (3) An informal argument, explicitly "not a genuine
  deduction" (§5.2), that if partial truth is fixed by which weakenings of
  a proposition are totally true, the truth value is a sieve.
---

# NOTE-tmpof137: A Topos Perspective on the Kochen-Specker Theorem: II. Conceptual Aspects, and Classical Analogues

## Contribution

Part I built sieve-valued valuations for quantum theory, motivated by Kochen–Specker. This paper argues that they are the generic notion of valuation for any family of propositions indexed by a category of contexts, not a device invented to get around KS.

It does three things.

- **Classical analogue (§3).** It shows that the construction runs unchanged in classical physics, where KS does not apply. There, macrostates rather than no-go theorems motivate it.
- **General setting (§4).** It lifts the construction to an arbitrary presheaf of posets on an arbitrary small category. It proves (Theorem 4.1) that generalised FUNC is exactly the naturality condition that makes a sieve-valued valuation a subobject of the presheaf of propositions.
- **Partial truth (§5).** It gives an informal philosophical argument that sieves are the natural values of "partial truth" whenever partial truth is fixed by which consequences are totally true.

## Key insight

A sieve on A is exactly the set of "coarsenings at which the proposition becomes totally true". It is closed under further coarsening because weakenings of a total truth are total truths. So any context category with a coarse-graining action on propositions produces sieve values, whether or not global classical valuations exist.

The classical case shows this directly. The value presheaf has global sections, one per microstate (eq. 3.7). Even so, a macrostate, or a microstate evaluated through the sieve semantics, yields contextual, Heyting-valued truth values. What decides the logic of truth values is the base category, not the presence or absence of global sections.

## Assumptions

- **Presheaves on small categories.** No sheaf condition or Grothendieck topology is used (as in part I). Ω(A) is the set of sieves on A, with ∧ = ∩ and ∨ = ∪. Relative pseudo-complement and negation are written out in fn. 6: S₁ ⇒ S₂ = {f | ∀g, f∘g ∈ S₁ ⇒ f∘g ∈ S₂}, and ¬S = S ⇒ 0.
- **Quantum review (§2.3).** As in part I:
  - O_d is the category of discrete-spectrum operators, and KS is "equivalent to the statement that, if dim H > 2, there are no global elements of the spectral presheaf Σ: O_d^op → Set" (§2.3.1).
  - Continuous spectra are excluded from the KS statement "on the grounds that it is not physically meaningful to assign an exact value" in the continuous part (§2.3.1).
- **Classical setting (§3.1).** S is a state space and M is the category of real measurable functions on S. There is an arrow f_M: B̄ → Ā iff B̄ = f∘Ā with f measurable on S(Ā) := Ā(S). Measure-zero identifications are "ignored" (fn. 8). Constant functions are admitted; they are the analogue of multiples of 1̂ and can be removed (fn. 10).
- **General setting (§4.2).**
  - G is a presheaf of posets with 0 and 1 on a small category C.
  - A covariant **comparison functor** C has the same object map as G and pushes propositions forward.
  - A *coarse-graining* G with respect to C satisfies d ≤ C(f)[G(f)(d)] (4.5) and monotonicity. The *generalised retraction* G(f)[C(f)(d)] = d (4.6) of part I is dropped, because it forces C(f) to be injective.
- **Partial-truth premises (§5.1).**
  - (A) Arrows induce maps f† on propositions, with (id)† = id. The presheaf law is *not* assumed.
  - (B) [B, f†(d)] is logically weaker than [A, d].
  - (C) There is a distinguished "total truth". It is (a) inherited by weakenings; (b) partial truth is "more true" the more weakenings are totally true; (c) the truth value is determined by which weakenings are totally true.
- **The authors' own caveat.** The partial-truth conditions are "very reasonable" but not "obligatory", and partial truth is often rejected in the philosophical literature (Haack [6]) (§5).

## Key results

- **Classical value presheaf (§3.1).** Υ(Ā) = S(Ā) with Υ(f_M)(λ) = f(λ). A global section is exactly a FUNC-respecting classical valuation, and every microstate s gives one, γ^s_Ā = Ā(s) (eqs. 3.6–3.7). This is "the key difference from the situation in quantum theory".
- **Quantisation as a functor (§3.1.3).** A quantisation that respects functional relations is a covariant functor Q: M → O with Q(f_M) = f_O (3.8). This is a remark. No existence or non-existence result is given.
- **Classical sieve-valued valuations (§§3.2–3.3).**
  - *From a macrostate R:* ν^R(A ∈ Δ) := {f_M: B̄ → Ā | B̄(R) ⊆ f(Δ)} (3.10). This is set beside two simpler options: true iff Ā(R) ⊆ Δ, and the Boolean value R ∩ Ā⁻¹[Δ] (3.9).
  - *From a classical partial valuation:* V^R is defined on the functions constant on R (3.11–3.12). The general ν^V is eq. (3.13).
  - *From a microstate:* ν^s(A ∈ Δ) = {f_M | f(Ā(s)) ∈ f(Δ)} (3.15). It is the principal sieve iff Ā(s) ∈ Δ.
  - *From a classical mixed state ρ:* eq. (3.17).
  - *Status of the proofs.* The verifications are "not rehearse[d]" (§3.3); "one can check". I checked that (3.10) is a sieve and obeys FUNC, null and exclusivity for R ≠ ∅. The checks are routine and correct.
- **Theorem 4.1.** A sieve-valued valuation ν on any presheaf G obeys generalised FUNC, ν(B, G(f)(d)) = f*(ν(A, d)) (4.2), iff N^ν_A(d) := ν(A, d) defines a natural transformation G → Ω. Hence each such valuation is a subobject of G. The proof is the one-line naturality check (4.4), and it is correct.
- **Generalised valuations on a general coarse-graining presheaf (§4.2.3).**
  - *Definition.* A family of local valuations φ_A: G(A) → Ω(A) obeying null, monotonicity and exclusivity (4.7–4.9), and FUNC (4.10).
  - *Non-emptiness.* This is argued from part I's Theorem 5.1 on W. A classical counterpart is said to be provable "similarly". It is not given.
- **The partial-truth argument (§5.1).** (M): ν(A, d) = {f | [B, f†(d)] is totally true} (5.1). (T): total truth means ν(A, d) = ↓A (5.2). The paper says that (M) and (T) together yield (C)(a)–(b) and that ν(A, d) is a sieve.
  - *The authors' assessment (§5.2).* It is "not a genuine deduction". Even premises (D) "values are sets of morphisms" and (T) "do not imply (M)". The argument gives the special case of FUNC for f ∈ ν(A, d) (5.3–5.4), not FUNC in general (5.5). FUNC is motivated separately by Theorem 4.1.
  - *Precise version.* The argument is made precise by requiring posets with 0 and 1, the presheaf law, a comparison functor and generalised coarse-graining (5.6), with truth conditions (5.7a–c).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | For classical physics the value presheaf on M has global sections, one per microstate, and they are exactly FUNC-respecting valuations | proof (definitional) | §3.1.2, eqs. 3.6–3.7 |
| C2 | Macrostates (and classical partial valuations, microstates, mixed states) yield sieve-valued valuations with the same properties as the quantum ones | sketch; "one can check", verified by the reader for ν^R | §§3.2–3.3, eqs. 3.10, 3.13, 3.15, 3.17 |
| C3 | A sieve-valued valuation on any presheaf of propositions obeys generalised FUNC iff it is a natural transformation G → Ω, i.e. a subobject of G | proof (short, correct) | Theorem 4.1, eq. 4.4 |
| C4 | Part I's coarse-graining presheaves and generalised valuations extend to any small category with a comparison functor, dropping generalised retraction | definitions plus remark; non-emptiness by appeal to part I | §4.2, eqs. 4.5–4.10 |
| C5 | If partial truth is fixed by which weakenings are totally true, sieve values are "very natural" | informal argument, explicitly not a deduction | §5.1, assessed in §5.2 |
| C6 | Sieve-valued valuations obeying FUNC are "one of the most natural notions of valuation for any presheaf of propositions, no matter what their topic" | the abstract/introduction headline; rests on C2, C3 and C5, so on one short theorem plus an argument from naturalness | §1, §4 opening, §6 |
| C7 | Quantisation respecting functional relations is a functor M → O | assertion (definitional remark; existence not discussed) | eq. 3.8 |

## Method

Conceptual analysis supported by elementary presheaf theory. The paper restates part I's quantum constructions. It then substitutes a classical category, M with the value presheaf Υ, for O with the spectral presheaf Σ, and abstracts both to an arbitrary small category with a presheaf of posets and a comparison functor. The one formal result is a naturality check. The partial-truth argument is given first informally (assuming only the notion of a category) and then made precise in the §4.2 vocabulary.

## Concepts

- **Value presheaf Υ** — on M, Υ(Ā) = Ā(S), the "classical spectrum", with Υ(f_M)(λ) = f(λ). It is the classical analogue of part I's spectral presheaf.
- **Macrostate** — a Borel R ⊆ S. It induces the partial valuation V^R on the functions constant on R.
- **Morphism-valued / sieve-valued valuation** — any assignment ν(A, d) of a set of arrows into A (respectively, of a sieve on A) to each proposition [A, d] (§4.1).
- **Generalised FUNC** — ν(B, G(f)(d)) = f*(ν(A, d)) (4.2).
- **Comparison functor C** — a covariant functor with C(A) = G(A) that pushes a coarse-grained proposition back up for comparison of logical strength (§4.2.1).
- **Coarse-graining presheaf with respect to C** — d ≤ C(f)[G(f)(d)] plus monotonicity (4.5). The optional generalised retraction (4.6) is that of part I.
- **Total truth / partial truth** — total truth is the principal sieve ↓A. Partial truth is any other sieve, "more true" when larger (§5).

## Connections

- **Part I ([LIT-325](../literature.d/LIT-325.md), [NOTE-271](NOTE-271.md)).** This paper is part I's review (§2) plus three new motivations. Part I's §6 claim that the sieve Heyting algebra "is precisely fixed by the structure of the base category" gets a concrete gloss in §2.2: for the one-object category, "one gets just two truth-values". The coarse-graining presheaf G is restated on O (2.20–2.25), with part I's infimum definition for non-Borel f(Δ). The quantum category W is mentioned (§4.2) but not used.
- **Parts III and IV (Hamilton, Isham & Butterfield 2000; Butterfield & Isham 2002).** Reference [3] here promises an interval-valuation sequel; that became part IV, while part III moved the base to von Neumann algebras. Part III's §5 says the classical analogues and general motivations of this paper carry over to the base V "piece by piece", but does not spell them out. Part IV's §4 survey of relations R is the same "naturalness" style of argument as §5 here, applied to the interval/sieve correspondence.
- **Döring–Isham ([LIT-343](../literature.d/LIT-343.md), [NOTE-277](NOTE-277.md)).** Paper I of that series presents classical physics as the representation of the same formal language in Sets, and calls the stance "neo-realism". This paper's §3 is the earlier, more modest version: here the classical theory is not re-represented in Sets but given sieve-valued valuations over the context category M, exactly as in the quantum case. The Döring–Isham programme drops the "partial truth from weakenings" motivation in favour of formal languages and topos representations.
- **Kripke–Beth semantics (§1).** The paper names it as a further analogy (sieves on a poset of states of knowledge) and defers it to Butterfield & Isham "Philosophical implications of generalised valuations", in preparation. I did not check whether that paper appeared; part IV cites Butterfield's "Topos theory as a framework for partial truth" (PhilSci-Archive) in its place. Unverified.
- **Anthology of the SOTA.** No entry; nothing in this paper bears on ML practice.

## Bearing on the record

- **[THEORY-024](../theory.d/THEORY-024.md) (Rejected: "Boolean logic is restored when a presheaf acquires a global section").** This paper is the series' own counterexample to that claim, and it strengthens the refutation [THEORY-024](../theory.d/THEORY-024.md) records.
  - *Global sections, sieve truth anyway.* Classically the value presheaf Υ has global sections, one per microstate (§3.1). Yet the paper's classical valuations, even the one induced by a single microstate s (3.15), are sieve-valued in Ω(Ā) over M.
  - *Excluded middle fails at a microstate (my check).* With constants admitted, as in the main text, every constant arrow lies in ν^s(A ∈ Δ) for non-empty Δ. So every false proposition gets a non-empty, non-principal sieve, its pseudo-complement is ∅, and excluded middle fails at a classical microstate. This is the classical twin of part I's "minimally true" values and fn. 14.
  - *What decides the logic.* What makes truth values two-valued is a one-object base, as §2.2 notes, not a global section. [THEORY-024](../theory.d/THEORY-024.md) could cite [LIT-325](../literature.d/LIT-325.md) together with this paper.
- **[THEORY-020](../theory.d/THEORY-020.md) (Stone; one Boolean context always has two-valued valuations).** Consistent and mildly supportive. The classical context category has global sections because every classical "context" sits inside one Boolean algebra of Borel subsets of S (fn. 11 makes the classical W the Boolean subalgebras of that single algebra). So the overlap condition [THEORY-020](../theory.d/THEORY-020.md) locates the KS obstruction in is satisfied trivially. The paper does not invoke Stone, ultrafilters or this framing; the gloss is mine.
- **[THEORY-037](../theory.d/THEORY-037.md) (Proposed: the Heyting algebra of clopen sub-objects).** No direct bearing. Fn. 6 writes out the Heyting implication and negation, but for the sieves Ω(A), not for Sub_cl(Σ). It cannot meet [THEORY-037](../theory.d/THEORY-037.md)'s promote_when, which needs the implication on clopen sub-objects over the abelian von Neumann subalgebras.
- **The owner's map.** If the map leans on "contextual truth values over a context category" as a general device, this is the paper that argues for that generality, though only by naturalness arguments plus Theorem 4.1. It adds nothing on ultrafilters, Gelfand spectra or topes.
- **ML practice.** It carries nothing for ML practice and does not belong in the Anthology.
- **For filing.** `quantum-foundations` first. `logic` (partial truth, Heyting-valued semantics). `contextuality` (stage-dependent truth). `philosophy-of-science` (the conceptual status of valuations; the classical/quantum comparison). `mathematics` (presheaves). The paper is more philosophical than the other parts, which is why `philosophy-of-science` ranks above `mathematics` here.

## Limitations

- **Thin formal content.** The headline (C6), that these are among "the most natural" valuations for *any* presheaf of propositions, rests on Theorem 4.1 (naturality ⇔ FUNC, a one-line check) and the §5 argument, which the authors themselves say is not a deduction. That is appropriate for a conceptual paper, and the authors are candid about it, but the headline is a judgement of naturalness, not a theorem.
- **Classical verifications are left to the reader.** "We shall not rehearse all the definitions, and verifications" (§3.3). The checks I made were routine and correct.
- **A gap in §5.1 that §5.2 repairs.** The step "it follows immediately from (M) and (T) … that ν(A, d) is a sieve" needs (f∘g)† = g†∘f†, the presheaf law that assumption (A)(a) explicitly declines to require. Without it the composite weakening of a total truth need not be totally true. §5.2 imposes the presheaf law as "natural", which closes the gap.
- **Generality is partly nominal.** §4.2's comparison functor is assumed rather than constructed, and no example beyond O, W and M is given.
- **Quantisation remark (3.8).** It presupposes that functional relations should be preserved ("it is generally agreed"). Whether any functor M → O exists on all measurable functions is not discussed.
- **No probabilities.** The paper explicitly sets statistical physics aside (fn. 9), as part I set aside quantum probabilities.

## Open questions

- Is the partial-truth argument a deduction under some natural strengthening of (A)–(C)? The authors think it is not (§5.2).
- Which comparison functors and coarse-graining presheaves, beyond the identity-embedding cases of part I, give interesting valuations?
- Does a functorial quantisation M → O preserving all functional relations exist, and if so, what does it carry across from the classical global sections? The paper does not ask.

## Corrections to the seeded skim

- none (there was no seed or dossier)
- Title. [LIT-325](../literature.d/LIT-325.md)'s identification note gives part II as "Categorical preliminaries". The paper is "A Topos Perspective on the Kochen-Specker Theorem: II. Conceptual Aspects, and Classical Analogues" (title page, arXiv, Crossref). [NOTE-271](NOTE-271.md) already has the correct title.
- Author order. The batch instructions and the arXiv metadata list "Isham & Butterfield". The paper's title page lists **J. Butterfield first, then C.J. Isham**. Crossref has the same order (Butterfield, Isham), and parts III and IV cite it as "J. Butterfield and C.J. Isham". `first_author` is therefore Butterfield.
- The series plan changed. Reference [3] announces "A topos perspective on the Kochen-Specker theorem: III. Interval-valued generalised valuations" by Butterfield & Isham, "in preparation". The published part III is instead Hamilton, Isham & Butterfield on von Neumann algebras (it touches intervals only in §4). Interval valuations became part IV (2002).
- Reference [1] misprints part I's arXiv number as "quant-ph/980355" (it is quant-ph/9803055). [NOTE-271](NOTE-271.md) records the converse misprint in part I.
