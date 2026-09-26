---
number: 195
status: Read
formerly:
- NOTE-tmpsyjjc
paper: LIT-221
title: 'Yoneda lemma'
version: 1
history:
- version: 1
  date: '2026-09-26'
  note: >-
    Read in full (The nLab page "Yoneda lemma" in full, in its current
    version (last revised 2026-08-17, the version after revision 88). I read
    it from the page source and checked it against the rendered page. Every
    section was read: Idea; Statement and proof (Classical: Definition,
    Remark, Proposition, Proof; In homotopy type theory: Theorem 9.5.4 with
    proof, Corollary 9.5.6 with proof); Corollaries I–III and
    Interpretation; Generalizations; Necessity of naturality; In
    semicategories; Applications; Related entries; References. I did not
    read the pages it links or transcludes (the context sidebars, Yoneda
    embedding, enriched Yoneda lemma, Yoneda lemma for (∞,1)-categories,
    regular semicategory). I did not check the HoTT book's own numbering
    against the book.). The first NOTE on this paper, which was seeded from
    its abstract alone.
date: '2026-09-26'
summary: >-
  The page states that for a locally small category C, every presheaf X
  and every object c, there is a canonical bijection
  Hom_{[C^op,Set]}(y(c), X) ≅ X(c), given by η ↦ η_c(id_c). It proves the
  bijection by chasing id_c around a naturality square. From it the page
  derives that the Yoneda embedding y: c ↦ Hom_C(−,c) is fully faithful
  and that y(c) ≅ y(d) ⇔ c ≅ d. It also shows by counterexample that the
  hypothesis doing the work is naturality: objects whose hom-sets are
  pointwise in bijection need not be isomorphic.
---

# NOTE-195: Yoneda lemma

## Contribution

A reference page that states the Yoneda lemma for presheaves on a locally small category and proves it. It derives three corollaries: the embedding is fully faithful, representing objects are unique, and representables are characterised by a terminal object in the category of elements. It also records the HoTT-book version (Thm. 9.5.4) and two things textbook treatments usually omit. First, counterexamples showing that pointwise bijection of hom-sets does not suffice without naturality, together with the Lovász (1967) and Pultr (1973) results where it does. Second, the failure of the lemma for semicategories.

## Key insight

A natural transformation out of a representable functor is determined by one element: η : Hom(−,c) ⇒ X is fixed by ξ = η_c(id_c). Naturality then forces η_b(f) = X(f)(ξ) for every f : b → c. So Hom(−,c) is the "free presheaf on one element at c". The embedding c ↦ Hom(−,c) loses nothing: morphisms c → d are exactly natural transformations y(c) ⇒ y(d), and so objects are determined up to isomorphism by how everything else maps into them. The determining data is the hom-functor with its action by composition, not a list of hom-sets.

## Assumptions

- **Local smallness:** each Hom_C(a,b) is a set, so y(c) = Hom_C(−,c) is a functor C^op → Set. (Definition, "For 𝒞 a locally small category".)
- **Identities exist.** The proof evaluates at id_c. The "In semicategories" section shows the lemma fails in general without identities: if it held in a semicategory 𝒢, 𝒢 would embed in PrSh(𝒢), which is a category, and so 𝒢 would already be one.
- **Naturality of η.** The proof uses it in one step, and "Necessity of naturality" shows that nothing weaker suffices in general.
- **HoTT section:** A is a precategory in the HoTT book's sense (the page's "category"), and F : A^op → Set is a functor into the category of sets (h-sets). Univalence is not needed for the statement.

## Key results

- **Definition (Yoneda embedding functor).** y : C → [C^op, Set], c ↦ Hom_C(−, c). **Remark:** y is the adjunct (currying) of Hom_C : C^op × C → Set, under Hom(C^op × C, Set) ≅ Hom(C, [C^op, Set]).
- **Proposition (Yoneda lemma), contravariant form as stated.** For C locally small, X ∈ [C^op, Set] and c ∈ C,
  Hom_{[C^op,Set]}(y(c), X) ≅ X(c), also written Nat(h_c, X) ≅ X(c).
  The map is η ↦ η_c(id_c): take the component at c, then evaluate at id_c. The inverse is ξ ↦ η^ξ with η^ξ_d(f) = X(f)(ξ) for f : d → c.
- **Covariant form (the form asked for, Nat(Hom(A,−), F) ≅ F(A)).** The page does not state it separately; it is the Proposition applied to C^op. For F : C → Set and A ∈ C, Nat(Hom_C(A, −), F) ≅ F(A), natural in A and in F. Forward: α ↦ α_A(1_A). Inverse: x ↦ (α^x)_B(f : A → B) = F(f)(x). Naturality in both variables is stated only in the HoTT theorem ("Moreover this is natural in both a and F", eq. 9.5.5), which is itself in contravariant form.
- **Proof sketch (as given).** Let η : C(−, c) ⇒ X and f : b → c. Naturality at f says X(f) ∘ η_c = η_b ∘ C(f, c). Apply both sides to id_c. Since C(f,c)(id_c) = id_c ∘ f = f, this gives η_b(f) = X(f)(η_c(id_c)). So η is determined by ξ = η_c(id_c). Conversely, every ξ gives a natural η^ξ by functoriality of X, and η^ξ_c(id_c) = X(id_c)(ξ) = ξ. The two maps are inverse.
- **Corollary 9.5.6 / Corollary I (the embedding).** y is fully faithful: [C^op, Set](C(−,c), C(−,d)) ≅ C(−,d)(c) = C(c,d). The HoTT version adds that this bijection is the action of y on hom-sets.
- **Corollary II (iso-determination).** y(c) ≅ y(d) ⇔ c ≅ d. The page's reason: y is fully faithful, so an iso of representables "must come from" an iso of objects. Fully faithful functors reflect isomorphisms. The page's gloss: "probes by objects of C are sufficient to distinguish objects of C: two objects of C are the same if they have the same probes".
- **Corollary III.** X is representable iff its category of elements el(X) has a terminal object (d, g ∈ X(d)), and then X ≅ y(d) with g the universal element.
- **Necessity of naturality.** (a) Take two objects A and B with Hom(A,A) = Hom(A,B) = Hom(B,B) = ℤ≥0, Hom(B,A) = ℤ≥1, and composition given by addition (identities are 0). Then Hom(A,−) ≅ Hom(B,−) pointwise, but A ≇ B, because any g : B → A has g ≥ 1 and so g ∘ f ≠ 0 = id_A. (b) A "finite" version of the same example is ill-formed as written; see corrections. (c) Where naturality is not needed: Lovász 1967, Thm 3.6(iv): finite relational structures A and B are isomorphic iff Hom(C,A) ≅ Hom(C,B) for every finite relational structure C. Pultr 1973, Thm 2.2, extends this to finitely well-powered, locally finite categories with an (extremal epi, mono) factorization system.
- **Semicategories:** the lemma fails in general. For regular semicategories it holds for "regular presheaves", the colimits of representables. The page gives this only as a pointer to "regular semicategory".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Nat(y(c), X) ≅ X(c) via η ↦ η_c(id_c), with inverse ξ ↦ (f ↦ X(f)(ξ)) | strong | proof (naturality-square chase), Proposition and Proof |
| C2 | The bijection is natural in c and X | moderate | stated in the HoTT theorem 9.5.4; asserted to "follow" and not proved; the classical statement omits it |
| C3 | y is fully faithful | strong | proof from C1 with X = y(d) (Corollary I and Cor. 9.5.6) |
| C4 | y(c) ≅ y(d) ⇔ c ≅ d | strong | from C3: fully faithful functors reflect isomorphisms (Corollary II; the step is stated, not spelled out) |
| C5 | X is representable iff el(X) has a terminal object | strong | short proof by unwinding hom-sets of el(X) (Corollary III) |
| C6 | Pointwise bijections Hom(A,−)(Z) ≅ Hom(B,−)(Z) for all Z do not imply A ≅ B | strong | explicit counterexample on ℤ≥0/ℤ≥1 (correct as written); the finite second example is ill-formed as written |
| C7 | In finite relational structures, and in Pultr's class of categories, counting homs does determine isomorphism | moderate | cited theorems (Lovász 1967 Thm 3.6(iv); Pultr 1973 Thm 2.2), not proved here |
| C8 | The lemma fails for semicategories in general | moderate | a one-sentence argument (validity would embed 𝒢 in a category) |
| C9 | "Probes by objects of C are sufficient to distinguish objects of C" | weak as worded | an informal gloss of C4: "the same" must mean "isomorphic" and "same probes" must mean "naturally isomorphic hom-functors", which C6 shows is not the same as having the same hom-sets |

## Concepts

- **Presheaf:** a functor C^op → Set. **Representable presheaf:** one isomorphic to y(c) = Hom_C(−, c) for some c, the "presheaf represented by c".
- **Yoneda embedding:** y : C → [C^op, Set]. It is called an embedding because it is fully faithful (Corollary I).
- **Probe (Interpretation):** a map c → X from a representable into a presheaf, which by the lemma is an element of X(c). Presheaves are "generalized objects probeable by objects c of C".
- **Category of elements el(X):** objects are pairs (c, f ∈ X(c)); morphisms (c,f) → (d,g) are the u : c → d with X(u)(g) = f.
- **Universal element:** the g ∈ X(d) of a terminal object (d, g) of el(X). It gives X ≅ y(d).

## Connections

The page credits the name to Mac Lane, from a 1954 conversation with Nobuo Yoneda at the Gare du Nord (Kinoshita's obituary and Mac Lane's note, Math. Japonica 47 (1998)). It cites Grothendieck's 1960 Bourbaki exposé as an early source. For exposition it points to Mac Lane (CWM §III.2), Leinster, Riehl (*Category Theory in Context*, ch. 2), Perrone (arXiv:1912.10642, ch. 2), Reyes, Reyes & Zolfaghari (2004) and Pratt's "Yoneda lemma without category theory". The generalisations it lists are the enriched Yoneda lemma, Yoneda reduction (ends and coends), bicategories, tricategories, (∞,1)-categories, internal higher categories (Martini, arXiv:2103.17141) and formal category theory in a 2-category (Street 1974). Its applications are Tannaka reconstruction and Isbell duality. It links to a type-theoretic Yoneda lemma, and to Escardó's "Using Yoneda rather than J to present the identity type". These are the bridge to [LIT-032](../literature.d/LIT-032.md)'s directed type theory.

## Bearing on the record

- **What the lemma licenses philosophically, stated from this page's content.** Inside a given category, an object's isomorphism class is fixed by its hom-functor, meaning its hom-sets from every object together with the action of every morphism by composition. This is the precise sense of "an object is determined by its relations". Three things are presupposed. (i) The objects of the category. The hom-functor is indexed by them and the conclusion is an isomorphism between two of them. (ii) The composition structure, not just which relations hold. The necessity-of-naturality counterexample is two non-isomorphic objects with pointwise-bijective hom-sets. (iii) Identity arrows. So the lemma is a relational criterion of identity up to isomorphism for objects that are already there. It is not a construction of objects from relations that lack relata. At most it supports "objects are positions in a structure" (non-eliminative OSR, as in [LIT-217](../literature.d/LIT-217.md)'s 2001 position). It does not support eliminating objects (radical OSR). This is the relevant control for yo2 and yo3.
- **Identity.** The criterion is up to isomorphism. For objects with non-trivial automorphisms, or distinct isomorphic copies, it is silent on numerical identity. This matches the limit [LIT-154](../literature.d/LIT-154.md) found for weak discernibility, and it is the precise place where a structuralist must either adopt identity = isomorphism (univalence) or grant relata a primitive identity.
- **No THEORY in nucleation depends on the page.** If one is written (for example "Yoneda formalises structuralism"), cite C3 and C4 for the mathematics and C6 for the caveat, and flag C9 as a gloss.
- **ML practice:** none. The lemma has been invoked in ML-adjacent category-theory papers (for example arXiv:2207.02917 on causal inference), but this page carries no instruction for ML practice.

## Limitations

- It is a wiki page: anonymous edits are possible and content moves between revisions. Cite the revision date.
- The classical statement omits naturality, and neither version proves it.
- One of the two counterexamples is ill-formed as written (see corrections).
- Corollary II's step ("must come from") uses, without stating it, that fully faithful functors reflect isomorphisms.
- It states only the presheaf (contravariant) form. The covariant Nat(Hom(A,−), F) ≅ F(A) is left to duality.
- The HoTT theorem numbers (9.5.3–9.5.6) are the page's, not checked against the book.
- It makes no philosophical claim, and the structuralist reading is not the page's. The "Interpretation" gloss for Corollary II is looser than the corollary.

## Open questions

- Which categories arising in physics satisfy a Lovász–Pultr-type theorem, so that bare hom-set counts, rather than natural isomorphism, determine objects? This is where a "relations as bare data" reading would be literally correct.
- Is there a Yoneda-style reconstruction of objects from morphism data alone, in an arrows-only presentation, that is not a relabelling of identities as objects? This is the question yo3 (§3, fn. 11) raises.

## Corrections to the seeded skim

- Against [LIT-032](../literature.d/LIT-032.md) (Riehl & Shulman) and [NOTE-069](NOTE-069.md): no conflict. The note reads RS Thm. 9.1 as "just the usual proof" of Yoneda. This page gives that usual proof: evaluate at the identity and extend by functoriality. Its HoTT section is the HoTT book's 1-categorical lemma (Thm. 9.5.4, for precategories). That is not RS's directed, dependent Yoneda for covariant families (RS Thm. 9.5), and the record should not confuse the two. The page lists "Yoneda lemma for (∞,1)-categories" only as a link.
- Against [LIT-154](../literature.d/LIT-154.md) (Leitgeb & Ladyman) and [NOTE-133](NOTE-133.md): the lemma is the category-theoretic counterpart of a structural identity criterion, and it has the same limit. Corollary II gives y(c) ≅ y(d) ⇔ c ≅ d, which is identity only up to isomorphism. Distinct but isomorphic objects, for example two different one-element sets in Set, have isomorphic relational profiles, and the lemma cannot tell them apart. This is the categorical analogue of the non-discernible nodes of LL's graph G′. Category theory's answer is to deny that the distinction matters (identity = isomorphism, as in univalent foundations). It does not answer by discerning them.
- Against [LIT-196](../literature.d/LIT-196.md) (Chakravartty) and its [NOTE-149](NOTE-149.md) gloss that relations cannot fix relata's identity without intrinsic features: inside a category the lemma is a precise counterexample, but only a partial one. An object has no intrinsic features beyond its identity arrow, and its isomorphism class is fixed entirely by its hom-functor. Numerical identity within an isomorphism class is not fixed relationally, and the objects are presupposed throughout. This supports a determination thesis ("relations fix identity up to isomorphism"), not an elimination thesis.
- Against [LIT-045](../literature.d/LIT-045.md) (SEP, Structural Realism): the entry's "relations without relata" objection is not answered by Yoneda. The lemma is stated for a category that already has objects. The relational profile y(c) is a functor indexed by all the objects of C. The iso is between two objects of C. Nothing in the page claims otherwise. The claim that "Yoneda formalises structuralism" belongs to other pages, such as the nLab "structuralism" entry, not to this one.
- On the page itself: (1) the classical Proposition says "canonical isomorphism" and does not state naturality in c and X. The Idea section says "natural bijection", and only the HoTT theorem states "natural in both a and F". Neither version proves naturality: the HoTT proof says it "follows from this". (2) The finite counterexample in "Necessity of naturality" (Hom(A,A) = Hom(A,B) = Hom(B,B) = {0,1}, Hom(B,A) = {0,2}, "composition is multiplication modulo 2") violates the identity law as written: for g = 2 : B → A, g ∘ 1_B = 2·1 mod 2 = 0 ≠ 2. The intended example needs composites landing in Hom(B,A) to keep the value 2 (2∘1 = 1∘2 = 2). My own check, not the page's: with that repair every composite through a B→A arrow into the {0,1} hom-sets is 0, and the example works. The infinite counterexample (hom-sets ℤ≥0 and ℤ≥1 under addition) is correct as written. (3) The HoTT proof has a misplaced parenthesis ("F_{a,a'}(f(α_a(1_a))" for F_{a,a'}(f)(α_a(1_a))). It computes only one of the two composites and then asserts both are identities. (4) The classical inverse is written η^ξ_d := X(−)(ξ). It means f ↦ X(f)(ξ).
