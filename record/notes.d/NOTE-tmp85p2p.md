---
status: Read
paper: LIT-tmptrcx3
title: 'Category-theoretic structure and radical ontic structural realism'
version: 1
history:
- version: 1
  date: '2026-09-26'
  note: >-
    Read in full (Full text of the published article, Synthese 190(9)
    (2013), pp. 1621–1635, from the typeset PDF on the author's own site (15
    pp.). Read all of it: the abstract; §1 Introduction; §2 "No relations
    without relata?" (2.1 set theory versus category theory, 2.2 elimination
    of relata in name only); §3 "An analogy from general relativity" (3.1
    asymptotic boundary conditions, 3.2 sheaves and relata, 3.3
    spatiotemporal structure sans relata); §4 "How to do category-theoretic
    physics"; §5 "What the category-theoretic radical ontic structural
    realist must do"; §6 Conclusion; footnotes 1–16; references. Nothing was
    skipped. The PhilSci-Archive preprint could not be reached (bot
    challenge), so any differences between it and the published version are
    unverified.). The first NOTE on this paper, which was seeded from its
    abstract alone.
date: '2026-09-26'
summary: >-
  Bain argues that the "relations without relata" objection to radical OSR
  depends on defining structure set-theoretically, where a relation is a
  subset of X × X. If a structure is instead "an object in a category",
  its elements (arrows 1 → A) are "not essential", because
  category-theoretic objects need not be structured sets. His examples are
  sheaves of Einstein algebras for GR with asymptotic boundary conditions,
  which may lack global sections (§3), and nCob and Hilb (§4). He
  concludes that ROSR "avoids the charge that it rests on an incoherent
  claim" (p. 1634). The paper never mentions the Yoneda lemma,
  representable functors or universal properties by name.
---

# NOTE-tmp85p2p: Category-theoretic structure and radical ontic structural realism

## Contribution

The paper is the first sustained argument that category theory, rather than set theory, gives radical ontic structural realism (ROSR) a coherent formulation. It identifies "structure" with "object in a category" and "relata" with elements (arrows 1 → A). It argues that such elements are inessential when objects are not structured sets. It then offers physics cases where this matters: sheaves of Einstein algebras for GR with boundary conditions, and nCob/Hilb for TQFT. It closes with a three-item agenda for the category-theoretic ROSRer.

## Key insight

Set-theoretic definitions of relation (subsets of X × X) mention elements ineliminably, whereas category-theoretic definitions (products by universal property, elements as arrows 1 → A) do not have to. So the incoherence charge against "relations without relata" may be an artefact of the set-theoretic framework. Whether the move is more than relabelling depends on finding physically relevant categories whose objects are not structured sets.

## Assumptions

- **Structure is "object in a category"** (p. 1623): "the intuitions of the ontic structural realist may be preserved by defining 'structure' in this context to be 'object in a category'".
- **Relata are elements**, meaning set-theoretic members or categorial arrows 1 → A (pp. 1623–1625).
- **The formalism is ontologically telling:** "semantic realism" and a "naturalistic approach to metaphysics" (p. 1634). How theories represent phenomena is to be taken "at face value".
- **Category theory can be specified without set theory** ("setting aside foundational issues for the moment", p. 1624). Bain concedes that this is still owed (§5(1)).
- **The internal/external distinction for toposes** gives "a formal means" of separating relata-laden set-theoretic discourse from relata-free categorial discourse (p. 1624). This is asserted, not shown.
- **The physics examples are physically relevant:** GR solutions with asymptotic boundary conditions (Heller & Sasin 1995), and nCob/Hilb as used in TQFT (Baez 2006).

## Key results

This is a philosophical argument; there are no theorems. What it argues:

- **§2.1:** set-theoretic structure, an isomorphism class of structured sets [{X, R_i}], makes "ineliminable reference to relata". Category-theoretic structure need not: elements become arrows x : 1 → X, "external" to X, and products are defined by an external probe (T, f1, f2, f) (pp. 1622–1624).
- **§2.2:** reply to "elimination in name only". Set-theoretic relata have categorial correlates, but "in many cases, these correlates are not essential to the articulation of the relevant structure", because "category-theoretic objects need not be structured sets" (p. 1625).
- **§3 (GR):** tensor models (M, g_ab) and Einstein-algebra models (C, g) correspond 1–1 (points ↔ maximal ideals), so moving to Einstein algebras is elimination in name only (p. 1626). With asymptotic boundary conditions, however, tensor models with and without boundary fall in different categories (Diff(M) versus Diff_c(M)). Sheaves of Einstein algebras over M′ = M ∪ ∂M put both in one category, Heller–Sasin's "Einstein structured spaces" (p. 1627). A sheaf "need not possess global sections, and even when it does, these fail to uniquely characterize it" (p. 1628). The conclusions: (1) point-correlates play no essential role in "global differentiable structure"; (2) EA models are more unifying (p. 1629). The analogy: (1′) categorial correlates of relata are inessential; (2′) this notion of structure does unifying work (p. 1629).
- **§4 (TQFT):** nCob and Hilb differ from Set in three ways: their objects are "not structured sets" because the morphisms are not structure-preserving functions; they are monoidal "but not Cartesian"; and they are *-categories. Their elements (manifold points, vectors) are therefore "not essential" (pp. 1630–1631).
- **§5 (agenda):** the ROSRer must (1) show that category theory is more fundamental than set theory, against Krause (2005), whom Bain cites as "Kraus"; (2) give more categorial reformulations of physics (Döring–Isham, Heunen et al., Baez); and (3) answer the worry that the physically relevant structures are the set-theoretic ones. On (3), whether measurement requires relata is "an empirical question". A "Jones underdetermination" argument follows: the tensor formulation supports objects, while the EA formulation "supports an ontology of structure devoid of objects" (p. 1634).
- **§6 conclusion:** "a definition of structure as an object in a category does not, in general, depend essentially on (set-theoretic) relata". Hence ROSR "avoids the charge that it rests on an incoherent claim" (p. 1634).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Set-theoretic definitions of relation and structure make ineliminable reference to elements | moderate | informal argument from the definition of ordered pairs and of ∈ as primitive (§2.1) |
| C2 | Category-theoretic definitions (elements as 1 → A, products by probes) do not refer to "internal" elements | weak | examples. Generalized elements T → A are ignored, and by Yoneda they determine A (see corrections) |
| C3 | "The notion of an element of an object only makes sense in ... categories with ... terminal objects" | weak | assertion (p. 1623). False for generalized elements, and yo3 §4 objects |
| C4 | Elements are "not essential" when objects are not structured sets | weak | assertion plus the examples of §§3–4. "Essential" is never defined, and yo3 §4 asks for exactly this |
| C5 | Tensor and EA models of GR correspond 1–1, so EA alone eliminates points in name only | strong | Geroch 1972, Heller–Sasin 1995 (points ↔ maximal ideals), cited |
| C6 | Sheaves of EAs unify spacetimes with and without asymptotic boundaries in one category | moderate | cited from Heller & Sasin (1995, p. 3647, 3657), not shown here. Physical relevance is disputed by yo3 §7 |
| C7 | Sheaves need not have global sections, so the objects of the relevant category need not have elements | moderate | a standard sheaf-theory fact, cited. The step "no global sections ⇒ no relata" is weak, since local sections remain (yo3 §7) |
| C8 | Sections of a sheaf of EAs are maximal ideals | false as stated | p. 1629. Sections are algebra elements; yo3 fn. 32 |
| C9 | nCob and Hilb are not Cartesian; their objects are not structured sets | weak / partly false | from Baez 2006. Hilb has direct-sum products; Hilbert spaces are structured sets whatever the morphisms (yo3 §6) |
| C10 | The EA formulation of GR "supports an ontology of structure devoid of objects" | weak | inference via Jones underdetermination plus face-value realism (§5). The paper's own §3 shows only that points are eliminated, not all relata (yo3 §7) |
| C11 | ROSR avoids the incoherence charge | weak | the conclusion (§6). It rests on C2–C4 and C10 |

## Concepts

- **ROSR:** "structure exists independently of objects that may instantiate it"; structure "consists of relations devoid of relata" (p. 1622, citing French & Ladyman 2003).
- **Structure (categorial):** "object in a category" (p. 1623).
- **Element (categorial):** an arrow 1 → A from a terminal object (p. 1623). Bain does not use generalized elements.
- **Structured set:** a domain X with relations R_i. "Structure" set-theoretically is an isomorphism class [{X, R_i}] (p. 1622).
- **Internal vs external description:** framed in a category's internal language versus in set theory. It gains "traction" in toposes (p. 1624).
- **Global vs local differentiable structure:** the structure encoded in a sheaf of EAs over M′ versus Diff_c(M) on manifold points (p. 1629).
- **Jones underdetermination (after Pooley 2006):** one theory, several formulations whose realist readings give incompatible ontologies (p. 1633).

## Connections

The paper responds to the incoherence charge as put by Esfeld & Lam (2008), Stachel (2006), Wüthrich (2009), Dorato (2008) and Greaves (2009), and follows Chakravartty (2003) in allowing ROSR to deny the dependence. Its category theory draws on Awodey (2010), Bell (1988), Lawvere & Schanuel, and Mac Lane & Moerdijk. Its physics draws on Geroch (1972), Heller & Sasin (1995), Baez (2006), Döring & Isham (2011) and Heunen–Landsman–Spitters (2009). The direct responses are yo3 (Lam & Wüthrich 2013/2015) and Lal & Teh (arXiv:1404.3049, "Categorical Generalization and Physical Structuralism"), which I checked but did not read in full. Eva (2016, EJPS) defends Bain against both, but I could not reach it from a legitimate free source. None of the three names the Yoneda lemma: I searched the full texts of yo3 and of Lal & Teh for "Yoneda" and got no hits.

## Bearing on the record

- **The explicit Yoneda–OSR link is absent here.** This is the most-cited category-theoretic ROSR paper, and it does not invoke Yoneda. Any THEORY or NOTE saying "Bain uses Yoneda to support relations without relata" would be citing him for something he does not say.
- **What the paper does show:** the categorial vocabulary lets one state some structure without mentioning global elements. It does not show that relations can exist without relata, because morphisms have domains and codomains, and because the "structure" is itself an object of the category. Read with yo1: the best category-theoretic statement of "relata determined by relations" is Yoneda, and it presupposes the objects. It supports positions in a structure, not their elimination.
- **Whether it bears on [LIT-219](../literature.d/LIT-219.md) (Ladyman, Patterns All the Way Up): unverified.** I did not check that note's content.
- **ML practice:** none.

## Limitations

- "Essential" is never defined, and the argument turns on it (§2.2, §3.3, §4).
- The paper conflates elements of a C-object with C-objects as relata. Bain flags the terminology clash (fn. 2) but does not address the substantive issue: morphisms relate C-objects, and yo3 §5 presses this.
- It ignores generalized elements, and so Yoneda. That is the exact point where "no elements" fails.
- The GR case eliminates manifold points (or maximal ideals), not relata in general. The paper's closing claim ("structure devoid of objects", p. 1634) exceeds §3.
- There are technical errors in the definitions of maximal ideal and section, and in the claim that Hilb has no products (see corrections).
- By its own §5, the foundational claim it needs, that category theory is more fundamental than set theory, is left open.

## Open questions

- Is there a physically motivated category whose objects are not determined up to isomorphism by their generalized elements (their hom-functors), or where the hom-functor is not the natural candidate for "relations"? Yoneda says no category of the usual kind qualifies, so the question is whether ROSR needs a non-Yoneda setting: semicategories, or enriched or bicategorical settings with weaker statements.
- Could an arrows-only (single-sorted) presentation, together with a Yoneda-style reconstruction, give ROSR more than relabelling? yo3 §3 says that identifying objects with identity arrows is relabelling.
- Does Eva (2016) answer the generalized-element objection? This is unverified; the paper was not reachable.

## Corrections to the seeded skim

- **No Yoneda.** The owner asked for work connecting the Yoneda lemma to OSR. Bain, the first candidate named, does not mention the Yoneda lemma, the Yoneda embedding, representable functors or universal properties anywhere in the 15 pages. The two closest passages are these. (a) Footnote 4 (p. 1624) quotes Awodey (2010, p. 29): objects and arrows "are determined by the role they play in the category via their relations to other objects and arrows, that is, by their position in a structure and not by what they 'are' or 'are made of'". That is the informal content of Yoneda's Corollary II (yo1), stated without the lemma. Bain uses it only to contrast senses of "internal/external". (b) §2.1 (p. 1624) defines the product P = X × X by its universal property, through an "external 'probe' (T, f1, f2, f)". That is a representability statement, P representing T ↦ Hom(T,X) × Hom(T,X), and its uniqueness up to isomorphism is a Yoneda consequence. Bain presents it only as an example of defining things without elements. So the paper sits one step from Yoneda and does not take the step.
- **On the "determined up to isomorphism by its relations" inference.** Bain does not make this inference himself. If his position is reconstructed through Yoneda, the reconstruction works against him. Yoneda determines an object by its generalized elements, the arrows T → A from every object T, together with their functoriality (yo1, C3–C4, C6). Category theory therefore does not remove elements. It replaces global elements 1 → A with all probes T → A, and says those probes, taken with their composition, fix A up to isomorphism. Bain's claim (§2.1, p. 1623) that "the notion of an element of an object only makes sense in those categories with ... terminal objects" is false once generalized elements are admitted. yo3 (§4, p. 10) makes exactly this objection. And iso-determination presupposes the objects of the category, both as the index of the hom-functor and as the two ends of the isomorphism. At most it supports "objects are positions in a structure", which is non-eliminative OSR. It does not support eliminating objects.
- **Against [LIT-045](../literature.d/LIT-045.md) (SEP, Structural Realism):** the SEP entry presents "relations without relata" as ROSR's standing objection. Bain's answer grants the conceptual dependence of relations on relata in set theory, and denies it only for "structure as object in a category". In his own set-up the morphisms, which are the category's relations, still have domains and codomains. So the reply relocates the relata; it does not remove them. yo3 §5 presses the same point.
- **Against [LIT-196](../literature.d/LIT-196.md) (Chakravartty), [NOTE-149](NOTE-149.md):** Bain cites Chakravartty (2003, p. 871) for the claim that ROSR may deny the relation–relata dependence. [LIT-196](../literature.d/LIT-196.md) (2012) is the later paper, which targets the non-eliminative version. Bain explicitly rejects "thin" objects (fn. 16, p. 1633) and so takes the eliminativist horn that Chakravartty's 2012 argument says non-eliminative OSR collapses into.
- **Against [LIT-217](../literature.d/LIT-217.md) (Ladyman 2001) and [LIT-151](../literature.d/LIT-151.md) (Wallace):** Bain's ROSR is the eliminativist reading that [LIT-217](../literature.d/LIT-217.md) does not hold ("the phenomena have structure but they are not structure"). His appeal to "Jones underdetermination" between tensor and Einstein-algebra formulations of GR (§5, pp. 1633–1634) is the kind of formulation-dependence that [LIT-151](../literature.d/LIT-151.md)'s math-first view treats as a choice of presentation, not of ontology.
- **Technical errors in the paper (my reading, several shared with yo3):** (1) Fn. 6 defines a maximal ideal as "the largest subset of the ring closed under the ring product". That is wrong: a maximal ideal is a proper ideal contained in no larger proper ideal, and an ideal is closed under addition and under multiplication by arbitrary ring elements. (2) p. 1629 says a section of a sheaf of Einstein algebras over U "is a maximal ideal of that algebra". Sections are elements of the algebra over U, function-like, not maximal ideals, which correspond to points. yo3 fn. 32 corrects this. (3) The sheaf condition (i) (p. 1628) is misprinted as ρ_WV = ρ_VU ∘ ρ_WV; it should be ρ_WU = ρ_VU ∘ ρ_WV. (4) "A global section of S is an assignment of an element of S(U) to each open region U" (p. 1628) is loose: a global section is an element of S(X), equivalently a compatible family. (5) "In the category Set, the terminal object is the isomorphism class of singleton sets" (p. 1623): every singleton is a terminal object, and an isomorphism class is not an object of Set. (6) §4(ii) (p. 1630) says nCob and Hilb "admit a tensor product but not a Cartesian product". For Hilb (finite-dimensional, bounded linear maps) this is false: the direct sum H ⊕ K is a product, indeed a biproduct. The correct point, Baez's, is that the monoidal product ⊗ is not the Cartesian product. yo3 (p. 10) repeats the error.
