---
number: 47
status: Read
formerly:
- NOTE-tmpcpuvk
paper: LIT-040
title: 'nLab, two-level type theory'
version: 2
history:
- version: 2
  date: '2026-09-25'
  note: >-
    Read in full (two documents. (1) **The nLab page "two-level type
    theory"**, fetched live on 2026-09-26 (raw4/nlab-2ltt.html, text in
    raw4/nlab-2ltt.txt). The page says "Last revised on February 23, 2024".
    The history shows revision 1 on April 16, 2018 at 15:49:56 and "9 more"
    revisions, with no author named. I read the whole body: Idea, Type
    theories, Applications/Semisimplicial types, Variations/Natural numbers,
    See also, References. (2) **The paper it stands in for**: Annenkov,
    Capriotti, Kraus & Sattler, "Two-Level Type Theory and Applications",
    arXiv:1705.03307v5 (26 May 2026), 58 pp. Journal version: Math. Struct.
    in Comp. Sci., DOI 10.1017/S0960129523000130, per the arXiv "related
    DOI"; I did not open it. Extracted with PyMuPDF (raw4/1705.03307.txt).
    In full I read §1 (with §1.1–1.2), §2 (§2.1–2.8, including every example
    model in §2.5, conservativity in §2.6 and the no-fibrant-replacement
    theorem in §2.7), §3 (§3.1–3.4, through Lemma 3.25), §4.1–4.2, the
    opening of §4.3 (Defs 4.4–4.6), §4.7 from Def. 4.46 to its end, and §5.
    §4.3–4.6 (Theorem 4.8 onward, Reedy fibrant replacement, classifiers,
    exponents of diagrams) I read only at the level of statements. The
    commutative diagrams came through the extraction as flattened labels,
    and I read them against the prose.). Upgraded from `Skimmed` to `Read`:
    the claims table, assumptions and results are new, and the skim is
    corrected where the full text disagreed.
date: '2026-09-25'
summary: >-
  The nLab page is an accurate but thin gloss on two-level type theory. It
  says nothing about the result that makes 2LTT usable: basic 2LTT is
  **conservative over HoTT** (ACKS Prop. 2.18: an inner type provably
  inhabited in 2LTT is inhabited in HoTT), which answers much of the
  page's own "open question" about the principle of equivalence. It also
  omits that a fibrant-replacement type former would force UIP on the
  inner level (ACKS Thm 2.20). The paper it cites, ACKS arXiv:1705.03307,
  is the proper source: definitions via models, conservativity, the axiom
  menu (A1)–(A6)/(T1)–(T3), and internal Reedy-fibrant diagrams over
  inverse categories with a definition of univalent (∞,1)-category.
---

<!-- inactive-ok-file: LIT-040 — Deferred: the paper is placed by this reading; the directive lapses when its status changes -->

# NOTE-047: nLab, two-level type theory

## Contribution

**nLab page.** It adds a compact orientation and nothing beyond that:
- what 2LTT is (an inner HoTT level and an outer UIP level);
- its history (Voevodsky's HTS with undecidable type-checking, then ACK's UIP-only version, then cubical type theory as a non-fibrant layer);
- the motivating application (semisimplicial types);
- one design variation (one natural-numbers type or two).

**ACKS paper, which the note recommends citing instead.** It gives 2LTT a semantic definition: a model is two cwf hierarchies on a shared category of contexts with a conversion c from inner to outer (Defs 2.8–2.9). It proves 2LTT conservative over HoTT via a presheaf model over any model of HoTT (Cor. 2.14, Props 2.18–2.19). It separates the optional strengthenings into strictness conditions (T1–T3) and axioms (A1–A6), and checks them against simplicial, cubical and presheaf models. It then develops fibrations, cofibrations and Reedy fibrant diagrams over inverse categories internally (§§3–4), ending with a definition of univalent (∞,1)-category as a complete semi-Segal type (Def. 4.48). A Lean formalisation covers Theorem 4.8 (§5).

## Key insight

HoTT cannot quantify over the external natural numbers that index coherence towers, which is why "semisimplicial types of level n, for variable n" is not definable. 2LTT adds an outer, set-level type theory whose ℕ *is* the meta-level ℕ and whose equality is strict, so such constructions become internal. Because inner types only map into outer ones (c), and not back, anything proved about inner types without extra axioms holds in plain HoTT (conservativity). The price is paid only when an axiom such as (A1)/(A2) is added to relate the two ℕs, which is exactly what untruncated semisimplicial types need.

## Assumptions

These are the paper's; the nLab page states none formally.
- **Outer level:** a model of "set type theory" (Def. 2.6):
  - 1/Σ/Π with η;
  - identity, empty, coproduct and ℕ types;
  - UIP and funext.
- **Inner level:** a model of HoTT (Def. 2.7): the same formers, with univalent universes. HITs are optional (A6).
- **Judgmental η for Σ** (fn. 6 and Remark 2.12). Without it, Σ is "positive" and not preserved by c.
- **Conversion** c : Tyⁱ → Ty is a morphism of cwf hierarchies that preserves context extension (Def. 2.8). It is not assumed to be injective (T1), strict (T2) or replete (T3).
- **Semantics-first.** Syntax is notation for working in the initial model. The syntax/initial-model correspondence is not proved (Remark 2.1).

## Key results

From ACKS; the nLab has no results of its own.
- **Lemma 2.11.** c preserves 1, Σ and Π up to natural isomorphism (2.1)–(2.3). It gives only comparison maps for +, 0, ℕ, = and U (2.4)–(2.8), which are generally not invertible.
- **Prop. 2.13 / Cor. 2.14.** For any model C of HoTT (with size conditions), the presheaf category Ĉ is a model of 2LTT, and Yoneda is a weak morphism acting bijectively on types and terms.
- **Prop. 2.16.** A modified presheaf model satisfies (T1) and (T2). The construction is constructive only for finitary type formers.
- **Props 2.18–2.19.** 2LTT (respectively with (T1), (T2)) is conservative over HoTT, in the weak sense of Def. 2.17: inhabitation is reflected.
- **Theorem 2.20.** A fibrant-replacement type former implies UIP for inner types.
- **§3:**
  - fibrant types are closed under 1, Σ, Π (Lemma 3.5);
  - (trivial) fibrations are closed under pullback, finite composition and finite products (Lemma 3.10);
  - within fibrant types, trivial fibration ⇔ fibration + equivalence (Lemma 3.12), and trivial cofibration ⇔ cofibration + equivalence (Lemma 3.17);
  - fibrant types, finite types, finite coproducts/products and Σ of cofibrant types are cofibrant (Lemma 3.25).
- **§4 (statements only as read):**
  - fibrant limits of Reedy fibrant diagrams over finite inverse categories (Thm 4.8, after Shulman [Shu15b, Lemma 11.8], formalised in Lean);
  - Reedy fibrant replacement of pointwise fibrant diagrams (Cor. 4.27);
  - a fibrant type of strictly Reedy fibrant diagrams for admissible C (Lemma 4.38), which applies to semisimplicial types truncated at finite level;
  - univalent (∞,1)-category := complete semi-Segal type (Def. 4.48), with the nerve of a suitably fibrant category as an example (Lemma 4.51).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | 2LTT combines an inner HoTT level and an outer UIP level; the outer can be read as internalised metatheory | strong (definition) | nLab "Idea" = ACKS Defs 2.8–2.9 |
| C2 | HTS's reflection rule makes type-checking undecidable | assertion (nLab) | stated without citation. ACKS say only that HTS is 2LTT + (A1), (A4), (A5), (T1), (T2) and that (A5) as a base rule would lose decidability (p. 15) |
| C3 | Exact equality defined by induction solves the semisimplicial-types problem | moderate | nLab assertion. ACKS show it for finite truncations in basic 2LTT (Lemma 4.38) and need (A2) or similar for the untruncated type (§5) |
| C4 | Whether 2LTT breaks the principle of equivalence is open | overstated | ACKS Props 2.18–2.19 prove conservativity for basic 2LTT; only stronger forms and axiom-extended versions remain open |
| C5 | With two nats and no extra axiom, a fibrant type of untruncated semisimplicial types cannot be defined | informal | nLab argument (limit over the non-fibrant nat is not fibrant). ACKS §5 agree that such results need (A1)–(A3); it is not a theorem in either |
| C6 | Basic 2LTT is conservative over HoTT | strong | proof, ACKS Prop. 2.18 (Yoneda acts bijectively on terms in the presheaf model) |
| C7 | A fibrant-replacement type former forces inner UIP | strong | proof, ACKS Thm 2.20 |
| C8 | Stronger (bijective) conservativity holds under equality reflection | conjecture | ACKS p. 23; argument credited to Kovács 2022 |
| C9 | Whether every (∞,1)-topos has a presentation with fibrant ℕ is open | assertion (nLab) | no source given; not in ACKS |

## Concepts

- **Inner / outer types** (ACKS). Other names: fibrant/pretypes (ACK), strict/exo types (ANST21), "fibrant/non-fibrant" (nLab).
- **Conversion** c (ACKS Def. 2.8): inner → outer, bijective on terms (Lemma 2.10).
- **Fibrant type** (ACKS Def. 3.4): an outer type with a chosen isomorphism to an inner type. This is structure, not a property.
- **Fibration** (Def. 3.7): a map whose fibres are fibrant. **Cofibration** (Def. 3.13): its pullback exponential preserves (trivial) fibrations. A **cofibrant type** is one whose exponentials preserve fibrancy (Cor. 3.20).
- **(A1)–(A6), (T1)–(T3)** (ACKS §2.4): optional strengthenings, relating the two ℕ, 0 and + (A1–A3), outer universes (A4), equality reflection (A5), extra type formers (A6), and strictness of c (T1–T3).
- **Conservative** (ACKS Def. 2.17): reflects inhabitation of types. This is weaker than the functor being conservative.

## Connections

**Against Riehl–Shulman, [LIT-032](../literature.d/LIT-032.md) (reads/c22.md).** Riehl & Shulman (pp. 5–6 of v5) name two-level type theory, citing "[Voe13, ACK17]", i.e. an early three-author version of ACKS, as the "brute force" way to internalise the Reedy argument. It would define hom_A(x, y) with strict equalities and "assert axiomatically that it is fibrant, since in general it would not be". They choose instead:
- all types fibrant;
- cofibrations as a separate judgmental layer (shapes and topes);
- extension types.

ACKS return the compliment. §1.1 describes RS17 as "using additional context layers to express structure that, in 2LTT, would be expressed via the outer equality type". Remark 3.14(i) says ACKS's characterisation of cofibrations (the type of diagonal fillers against fibrations is fibrant) is worth "comparing with the extension types by Riehl and Shulman". So the two are alternative answers to the same question, "question 2" in ACKS: how to extend HoTT so that coherence towers become internal. On that question:
- RS trade expressiveness for keeping every type homotopy-invariant.
- ACKS keep strict equality and recover homotopy invariance by conservativity.

That is why the nLab page's "See also: type theory with shapes" points at [LIT-032](../literature.d/LIT-032.md). A reader of [LIT-032](../literature.d/LIT-032.md) wanting the alternative should go to ACKS, not the nLab.

**Other lineage.**
- Voevodsky's HTS (2013), the first 2LTT.
- ACK at CSL'16 (arXiv:1604.03799).
- Capriotti's thesis [Cap16], the source of conservativity.
- Maietti's minimalist two-level foundation.
- Downstream uses listed by ACKS §1.1: ANST's *Univalence Principle*, Kovács's staging, Barras–Maestracci in Dedukti, Agda's SSet universe.

## Bearing on the record

- **[LIT-040](../literature.d/LIT-040.md) should be retired as Superseded by a LIT for ACKS** (arXiv:1705.03307). This is the one concrete action. A note on [LIT-032](../literature.d/LIT-032.md) that mentions 2LTT should name ACKS, not the wiki.
- No THEORY document is affected.
- **No bearing on ML practice.** Kovács's use of 2LTT for staged compilation is the nearest thing to engineering, and it is outside the Anthology's scope. Nothing here carries an instruction for the Anthology of the SOTA.

## Limitations

- **nLab page:**
  - no proofs;
  - two unattributed claims (C2's decidability remark has a plausible source in Voevodsky's note, but none is given; C9 has none);
  - no mention of conservativity or Theorem 2.20;
  - terminology that differs from its main reference;
  - an unstable document (last revised 2024-02-23; any later edit changes what [LIT-040](../literature.d/LIT-040.md) cites);
  - no named authorship.
- **ACKS, as read:**
  - the syntax is not proved to present the initial model (Remark 2.1);
  - conservativity is the weak, inhabitation-reflecting kind;
  - results needing (A1)–(A3) are not known to transfer to HoTT (§5);
  - the (∞,1)-category theory is "the very beginning" (§5), with no limits, colimits or Yoneda.
- **My reading.** I did not read §4.3–4.6 proofs in full.

## Open questions

- **Bijective conservativity** of 2LTT with equality reflection over HoTT (ACKS p. 23). Kovács's staging argument is offered as a route.
- **Whether results using (A2)/(A3)** (e.g. the untruncated type of semisimplicial types, [Kra15b, Thm 8.8.5]) can be expressed in plain HoTT.
- **Whether every (∞,1)-topos admits a model presentation with fibrant ℕ** (nLab; unsourced). A positive answer would justify the one-nat variant semantically.

## Corrections to the seeded skim

- **The record should cite ACKS, not the wiki; the seed only flagged this.** The page is a summary of ACK (arXiv:1604.03799) and ACKS (arXiv:1705.03307) plus nLab context. It contains no result, argument or citation not traceable to those papers, except two unattributed claims:
  1. "It is an open question whether any (∞,1)-topos can be presented by a model category in which the natural numbers object is fibrant".
  2. The use of "local model structure on simplicial presheaves" as the example where ℕ is not fibrant.

  I could not source either in ACKS.
  - **Filing options.** Under the record's source rule (arxiv > doi > url), the natural move is to file ACKS as its own LIT (arxiv 1705.03307, doi 10.1017/S0960129523000130), with [LIT-040](../literature.d/LIT-040.md) marked Superseded by it. Re-pointing [LIT-040](../literature.d/LIT-040.md)'s `url:` to an `arxiv:` would change which document the LIT is, which the record's retire-by-status rule argues against.
- **The page's "open question" is partly answered by its own cited paper.** The nLab says it is "an open question to what extent the principle of equivalence is actually broken, i.e. whether results proven in two-level type theory can be transferred". ACKS §2.6 proves:
  - **Prop. 2.18:** the unique morphism 0_HoTT → (0_2LTT)ⁱ is conservative, in the sense that inhabitation of an inner type over a HoTT context is reflected. This stays true with any outer type former validated by the presheaf model, including equality reflection (A5).
  - **Prop. 2.19:** the same holds for 2LTT with (T1) and (T2).

  What stays open (ACKS p. 23 and §5) is two things. First, a stronger, bijective conservativity (conjectured, with a concrete argument credited to Kovács 2022, Cor. 5.5). Second, the status of results that use (A1)–(A3).
- **"Fibrant" means something different in the paper.** The seed and the nLab say inner types "are called fibrant". ACKS deliberately reserve "fibrant" for an *outer* type isomorphic to an inner one (Def. 3.4 and p. 3). Fibrancy is then proof-relevant structure, not a property (p. 26). They also do not assume inner types are a subset of outer ones: there is only a conversion c from inner to outer (Def. 2.8), which is what makes the conservativity proof work. Readers moving from the nLab to the paper will trip on both points.
- **The nLab's "one nat or two" discussion is the paper's axiom menu, not an open design question.** The "weaker axiom" (fibrant types closed under limits of towers indexed by the outer nat) is ACKS (A2). "Non-fibrant nat is cofibrant" is (A3), attributed to Shulman. Two nats with an isomorphism is (A1). ACKS §2.5 then says which models validate which:
  - simplicial and cubical sets validate (A1)–(A4);
  - the presheaf model over a model of HoTT validates none of (A1)–(A4) in general;
  - (A2) holds there if C has ω-ary dependent sums (Remark after Prop. 2.14).
  
  HTS is identified precisely as basic 2LTT + (A1), (A4), (A5), (T1), (T2) in their strongest forms (p. 15).
- **Omitted by the page:** Theorem 2.20. An internal fibrant-replacement type former (rules form-R … comp-R) forces UIP on the inner level, so it cannot be added while keeping homotopical models. Any reader wanting "make an outer type fibrant" inside 2LTT needs this.
- **Dossier detail:** the seed says the page history shows "10 revisions". The history page lists Revisions 1–9 plus the current version, i.e. 10 states, so this is consistent. There are no named authors.
