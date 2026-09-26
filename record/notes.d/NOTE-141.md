---
number: 141
status: Read
formerly:
- NOTE-tmpjtl4f
paper: LIT-115
title: 'Corfield — Duality as a category-theoretic concept'
version: 2
history:
- version: 2
  date: '2026-09-26'
  note: >-
    Read in full (full text of the published article (Studies in History and
    Philosophy of Modern Physics 59 (2017) 55–61, 7 pp. in journal layout
    with article history), from the author-hosted copy on David Corfield's
    ncatlab.org pages (ncatlab.org/davidcorfield/files/duality.pdf),
    extracted to text and read end to end. That covers the abstract, §§1–4,
    footnotes 1–4, acknowledgements and the reference list (checked for the
    works discussed, not item by item). ScienceDirect itself was not tried
    again; the copy carries the journal's pagination, which is what page
    references below use.). Upgraded from `Skimmed` to `Read`: the claims
    table, assumptions and results are new, and the skim is corrected where
    the full text disagreed.
date: '2026-09-26'
summary: >-
  A short programmatic paper. Its thesis is that category theory, not set
  theory, is the framework in which the scattered instances of
  mathematical duality can be drawn together. The constructions in §3
  (dual adjunctions restricting to dual equivalences on fixed points,
  truth-value-enriched Galois connections, Isbell conjugation, dualising
  objects "keeping summer and winter homes") all "revolve around"
  adjunction, though Corfield expects no "single monolithic account" (p.
  59–60). On his usage, 'duality' is reserved for "involution with some
  form of structural reversal" (p. 57), so several physicists' dualities
  (homological mirror symmetry as an A∞-equivalence, mirror symmetry's Z2
  on the Hodge diamond, S-duality as a vestige of SL(2,Z)) are better
  called equivalences or symmetries. He proposes, without argument beyond
  the examples, that philosophers of physics will need homotopy type
  theory rather than predicate logic for the sameness questions dualities
  raise.
---
<!-- inactive-ok-file: LIT-108 — Deferred: a related work named by a 2026-09-26 close reading on the identity tag; lapses when the cited work is read -->

# NOTE-141: Corfield — Duality as a category-theoretic concept

## Contribution

Corfield puts duality on the agenda of Anglophone philosophy of mathematics, where he finds it all but absent since Nagel (1939) (pp. 56–57). He surveys the category-theoretic machinery that covers most mathematical dualities, and draws a line between mathematicians' and physicists' uses of the word. After it, a philosopher of physics has a clear statement of why "duality" in string theory often means "equivalence" to a mathematician, and a sketch (not a development) of the formal tools the author thinks the sameness questions will need.

## Key insight

Most mathematical dualities are adjunctions between one category and the *opposite* of another, restricted to their fixed points, where they become dual equivalences (p. 58). What makes them dualities rather than equivalences is the arrow reversal. Equivalence is sameness for categories; C and C^op are not the same unless C is self-dual. So a physicist's "duality" that is an equivalence of theories is, in a mathematician's terms, a statement of sameness, not of reversal.

## Assumptions

Premises and authorities rather than formal conditions:
- Mathematical practice is evidence for philosophy of mathematics (from Nagel, and "the philosophy of mathematical practice", p. 56).
- Adjunction is central: "Adjunctions are almost everywhere in mathematics" (Mac Lane 1971, p. 103), and "Essentially everything that makes category theory nontrivial … can be derived from the concept of adjoint functors" (nLab, quoted p. 58).
- Naturalness and systematicity of formulation, not in-principle expressibility, are the right standard for comparing foundational languages (p. 60; cf. Corfield 2003 §9.8).
- 'Duality' should be reserved for involutions with structural reversal (a stated preference, p. 57).
- For the physics in §4, the author relies on Urs Schreiber (acknowledged for the final section) and nLab entries, not on a published physics analysis.

## Key results

What it argues (§ and page from the journal pagination):
- **§1 (pp. 55–56).** Instances: dual Platonic solids, De Morgan duality, Fourier transform, projective duality (Pascal–Brianchon), electric–magnetic duality from Faraday and Maxwell to Dirac's monopoles; these "broaden, deepen and merge" (Poincaré, Pontrjagin, Langlands). Philosophers of physics face apparently different theories with the same predictions; the Oxford Handbook (Shapiro 2005) shows duality "has made very little impression" on philosophy of mathematics. The Princeton Companion says no single definition covers duality. Later dualities relate different kinds of entity (theories–models, spaces–quantities), which some subsume under Isbell duality. String dualities resemble Morita equivalence (Okada 2009).
- **§2 (pp. 56–57).** Nagel (1939), a logical empiricist, read projective duality as freeing geometry from "absolute simples"; his third thesis (structure, isomorphism, invariance dominate research) is the one philosophers of mathematics failed to follow up. Lautman engaged contemporary mathematics; Corfield (2010) argued Lautman's high-level ideas need not live outside mathematics, and category theory is the language that emerged to state them.
- **§3 (pp. 57–59).** Physicists use 'duality', 'symmetry', 'reciprocity' loosely; HMS can be read "simply" as an equivalence of A∞-categories (Kontsevich 1995). The Langlands 'dual' group is arguably better called 'reciprocal' (Langlands 2014). "Indisputable" dualities come from a pairing A × B → C (Majid's representational duality); the nLab algebra–geometry table (observables/states, AQFT/FQFT, and higher versions; footnote 1 notes the full C*-deformation-quantisation side is not worked out). Then: adjunction (Hom_D(F x, y) ≅ Hom_C(x, G y)); fixed points of an adjunction give an adjoint equivalence; an adjunction into an opposite category gives a dual equivalence (Pontrjagin duality as an example); internal adjunctions in 2-categories and monoidal categories (finite-dimensional vector spaces and their duals; Coecke's cups and caps); profunctors, where C^op is each category's dual and C ↦ C^op is the only proper autoequivalence of the category of categories; the nucleus of a profunctor (Willerton 2015) as a "categorified Fourier transform"; enrichment in truth values giving six classic Galois-connection dualities, and in extended reals giving Fenchel–Legendre duality; Isbell conjugation; dualising objects (2 for Stone duality, R/Z for Pontrjagin, a ground field for Lefschetz); Forssell's (2008) first-order logical syntax–semantics duality; Lawvere & Rosebrugh's formal vs concrete duality; Morita equivalence; adjoint triples and cohesion.
- **§4 (pp. 59–61).** No monolithic account, but category theory covers most cases and set theory could not do so "naturally". Set is not self-dual (∅ and 1 behave asymmetrically), so taking Set as the default for "concrete" categories breaks the symmetry of the category of categories; Rel is self-dual, and physics' categories (Hilbert spaces, cobordisms) are monoidal but not cartesian (Baez 2004), which is "a central part of the appearance of genuine mathematical duality in physics". String dualities: topological T-duality relates to Fourier–Mukai but has extra choices; mirror symmetry is a genuine Z2 action on the Hodge diamond, but a Z2 action alone need not be called a duality; electric–magnetic duality is closer, but is a vestige of an SL(2,Z) action. The issue is sameness in moduli spaces of QFTs; predicate logic is expected to be "far from optimal"; action groupoids, not quotients; HoTT recommended; Schreiber's effective-epimorphism proposal and "dualities of dualities". Nagel's third thesis holds "every bit as true today".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Anglophone philosophy of mathematics has paid little attention to duality since Nagel (1939). | weak | one handbook search (Shapiro 2005) and the author's reading; no survey |
| C2 | Most mathematical dualities of interest are covered by category-theoretic constructions around adjunction (dual adjunctions, enrichment, Isbell conjugation, dualising objects). | moderate | worked exposition of standard constructions with named examples, §3; drawn from the literature (Willerton, Lawvere & Rosebrugh, Forssell), not proved here |
| C3 | There is unlikely to be a single monolithic account of duality. | assertion | stated, p. 59–60 |
| C4 | Set theory could express particular dualities in principle but not "naturally" or systematically. | informal argument | appeal to C ↦ C^op as the relevant autoequivalence, p. 60 |
| C5 | Sameness for categories is equivalence, and opposite categories are not to be identified unless self-dual. | moderate | standard category theory, stated p. 60 |
| C6 | 'Duality' is better reserved for involutions with structural reversal; many physicists' dualities are equivalences or symmetries. | informal argument | terminological preference (p. 57) plus case remarks on HMS, mirror symmetry, S-duality, T-duality (p. 60) |
| C7 | Set is not self-dual, and privileging it introduces symmetry-breaking; Rel and non-cartesian monoidal categories are more natively dual. | moderate | the ∅ / 1 asymmetry argument, p. 60; Baez 2004 |
| C8 | Predicate logic will be "far from optimal" for the sameness questions dualities raise; philosophers of physics may need homotopy type theory. | weak | expectation, supported only by the complexity of QFT moduli spaces and the Sym(X) quotient vs action-groupoid example, p. 60 |
| C9 | Nagel's thesis that structure, isomorphism and invariance dominate the sciences holds "every bit as true today". | assertion | p. 61 |

## Concepts

- **Duality (Corfield's preferred sense)** — "kinds of involution with some form of structural reversal" (p. 57), e.g. subsets of a set and the reversal of inclusion along an injection. Contrasted with a "non-trivial equivalence".
- **Dual adjunction / dual equivalence** — an adjunction between C and D^op; restricted to fixed points (objects isomorphic to their round-trip image) it gives an equivalence C' ≃ D'^op (p. 58).
- **Representational duality** — Majid's term: a pairing A × B → C lets maps into C represent elements of either side (p. 57).
- **Dualising object** — an object V "keeping summer and winter homes" in two categories, giving a dual adjunction by maps into V in each (p. 59).
- **Formal vs concrete duality** — Lawvere & Rosebrugh: mere arrow reversal vs exponentiating by a dualising object (p. 59).
- **Action groupoid** — objects the points, morphisms the group elements relating them; keeps stabilisers that the quotient loses (p. 60).

## Connections

The contrast that matters for this record is with De Haro & Butterfield ([LIT-199](../literature.d/LIT-199.md)). Their Schema defines a duality as an *isomorphism* of model roots, so their dualities are, in Corfield's vocabulary, equivalences, not dualities; the two works use the word for different relations, and a reader moving between them has to translate. Corfield's §4 remarks on T-duality's "extra choices" and on "dualities of dualities" also bear on their geometric view of models as charts: Corfield independently sketches QFTs as an atlas with dualities as chart identifications (p. 60), from Schreiber, not from them. De Haro & Butterfield judge categorical equivalence "too weak" as a criterion of theoretical equivalence; Corfield takes equivalence as the right notion of sameness for categories, but does not apply it to theories, so there is no direct disagreement.

Le Bihan & Read ([LIT-113](../literature.d/LIT-113.md)) sort realist responses to dualities; Corfield offers nothing on actuality or underdetermination, and his text supplies none of the metaphysical principles they find missing.

Wallace ([LIT-151](../literature.d/LIT-151.md)) asks what notion of mathematical equivalence a math-first structural realism needs, rejecting set-theoretic isomorphism as too strict and finding categorical equivalence apparently too permissive. Corfield's answer is a direction (equivalence, groupoids rather than quotients, HoTT's "properly structuralist notion of sameness and difference"), not a criterion, so it does not settle Wallace's open question.

Leitgeb & Ladyman ([LIT-154](../literature.d/LIT-154.md)) argue, from graph theory, that identity of places is given by the structure and not by a criterion. Corfield's recommendation of HoTT (where identity is structure, e.g. the stabiliser kept in the action groupoid) points the same way, but he does not argue the metaphysical point. Riehl & Shulman's type theory for synthetic ∞-categories ([LIT-032](../literature.d/LIT-032.md)) is an instance of the "directed" HoTT variant Corfield says the philosopher of physics may need. The quasi-set theory of Holik et al. ([LIT-107](../literature.d/LIT-107.md)) is a different response to a different complaint about classical logic (non-individuals, not higher sameness), and the LIT's link to it should be weakened. Ladyman's SEP entry ([LIT-045](../literature.d/LIT-045.md)) is the background structural realism; Weyl ([LIT-108](../literature.d/LIT-108.md)) is a classic on symmetry, but not one Corfield cites.

On identity: Corfield holds a structuralist, univalent-style view of sameness for mathematical objects: things are the same when equivalent, sameness can itself carry structure (higher equivalences, "dualities of dualities"), and identifications should be kept as morphisms rather than collapsed. He gives no account of individuality or persistence. The `identity` tag is justified on the "across descriptions" clause of its blurb, as a secondary tag.

## Bearing on the record

It supports no THEORY document on its own. It is useful as a terminological check on any document in this record that uses "duality" from De Haro & Butterfield: in the mathematician's sense such a relation is an equivalence. It carries nothing for ML practice, and nothing in the Anthology of the SOTA depends on it (the category-theoretic ideas it surveys, such as Galois connections or Fenchel–Legendre duality, are standard mathematics, and the paper makes no claim about them outside mathematics and physics).

## Limitations

- Programmatic and short: §4's positive proposal (HoTT, action groupoids, effective epimorphisms, the T-duality 2-group) is a list of pointers to Schreiber and nLab, not an argued or worked account.
- The criterion for 'duality' is a stated preference, applied to physics cases in a paragraph each; none of the string dualities is analysed in detail, and AdS/CFT is not discussed.
- The claim of philosophical neglect rests on one handbook and the author's reading; Krömer & Corfield (2014), cited as the companion treatment, is not summarised.
- The case against predicate logic is an expectation; no sameness question is shown to be unstatable or mishandled in first-order terms.

## Open questions

- Does the structural-reversal criterion sort the physicists' dualities (T-, S-, mirror, gauge–gravity) cleanly, once each is stated precisely? A case-by-case analysis in De Haro & Butterfield's Schema, with each checked for arrow reversal, would settle it.
- Can homotopy type theory actually state a criterion of physical equivalence that disagrees usefully with isomorphism of model roots or with categorical equivalence? A worked HoTT formalisation of one duality, compared with the Schema, would show whether the recommendation earns its place.

## Corrections to the seeded skim

- The dossier and the LIT summary say predicate logic "is ill-suited" to the sameness questions dualities raise, as if argued. The paper states it as an expectation: "We should have every expectation then that the resources provided by natural language or the philosopher's traditional tool, predicate logic, are far from optimal" (p. 60). The only support is the complexity of QFT moduli spaces and one worked contrast (quotient vs action groupoid of Sym(X) on a finite set X). No failure of predicate logic is exhibited.
- The LIT summary says duality "is best understood category-theoretically as structural reversal organised around adjunction". Corfield claims less. The category-theoretic constructions "cover most examples of interest" and all involve adjunction, "and yet there is unlikely to be a single monolithic account of duality" (pp. 59–60). The comparative claim is against set theory, and is about naturalness: it would be "hopelessly implausible" that set theory handles duality "in anything like as 'natural' … and systematic a way" (p. 60), while conceding set theory can do it "in principle". The restriction of 'duality' to structural reversal is a terminological preference ("In my view it is preferable", p. 57), not a result.
- The dossier leaves out the paper's core formal point about sameness (p. 60): what is "fundamentally at stake in many cases of mathematical duality" is the one nontrivial autoequivalence of the (∞,1)-category of categories, C ↦ C^op; "the right way to treat 'sameness' between categories is the notion of equivalence", and opposite categories are not to be identified because they are not equivalent unless self-dual. It also leaves out the positive proposal of §4: the action groupoid, not the quotient, as the configuration space of a generally covariant theory; charts on an atlas of the space of QFTs, with dualities as chart identifications; the smooth T-duality 2-group (credited to Nikolaus); Schreiber's proposal that QFT duality is a "homotopified" equivalence relation (an effective epimorphism) on Lagrangian data, with "dualities of dualities".
- The dossier says T-duality "relates to Fourier–Mukai". It adds (p. 60) that T-duality involves "extra choices", so a string background may have "none, one or more than one 'T-duals'". That is the paper's reason for doubting it is a duality in the strict sense.
- The dossier's question "whether Corfield's structural-reversal criterion excludes gauge–gravity duality" has no answer in the text: AdS/CFT and gauge–gravity duality are not mentioned. Applying his criterion, it would count as an equivalence, not a duality, but that is inference, not his claim (unverified).
- The LIT's link to quasi-set theory ([LIT-107](../literature.d/LIT-107.md)) as an echo of the predicate-logic claim is loose. Corfield's alternative to predicate logic is homotopy type theory and its "cohesive, linear and directed" variants (p. 60), a structuralist-sameness formalism, not a logic of non-individuals. The link to Riehl & Shulman's type theory for synthetic ∞-categories ([LIT-032](../literature.d/LIT-032.md)) is closer.
- Minor: the six Galois-connection examples (§3, p. 59, after Willerton 2013) come from enriching in truth values, i.e. from a relation between two sets inducing an adjunction between their power sets. The dossier lists them without saying where they come from.
- identity tag: justified, narrowly. The work concerns sameness across descriptions (when two categories, or two Lagrangian presentations of a QFT, are "the same"), and its answer is a structuralist one: sameness is equivalence, identifications are kept as structure (groupoids) rather than quotiented away. It says nothing about individuality or persistence, and the sameness material is about a page of §4. It belongs on the tag last.
- philosophy-of-mathematics tag ([ADR-007](../decisions.d/ADR-007.md)): justified, and strongly. The paper is written by a philosopher of mathematics, framed by Nagel (1939) and Lautman, placed in "the philosophy of mathematical practice" (p. 56), and argues about which foundational language best captures a mathematical concept.
- primary topic: philosophy-of-mathematics. The thesis is philosophical (category theory vs set theory as the language for a thematic concept; what "duality" should mean; what philosophers of physics should learn). The mathematics in §3 is exposition in service of it, not mathematics "read for itself". Suggested order: philosophy-of-mathematics, mathematics, philosophy-of-science, identity.
