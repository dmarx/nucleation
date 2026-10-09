---
status: Active
status_note: 'read in full 2026-10-09 ([NOTE-tmp3cvly](../notes.d/NOTE-tmp3cvly.md)); worth reading as the first paper to model discourse meaning as sheaf-theoretic gluing, and as the record''s earliest bridge between the Abramsky–Brandenburger framework and natural-language semantics. A basic Discourse Representation Structure is a section of a presheaf of consistent literals; a choice of anaphoric resolution is a cover, a jointly surjective family of variable maps; and the meaning of the discourse is the gluing, which is unique when it exists (Proposition 1, its only result). Its "contextuality" is context dependence, not the failure of a compatible family to glue: the only obstruction it exhibits is inconsistency of literals. Its probabilistic section ranks candidate covers by summed corpus counts rather than gluing distributions. Short and preliminary by its own account.'
title: 'Semantic Unification: A Sheaf Theoretic Approach to Natural Language'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Filed at the owner's request on 2026-10-09 and read in full the same
    day (NOTE-tmp3cvly) from the arXiv PDF (v1, the only version).
    Bibliography checked against the arXiv abstract page (v1 submitted 13
    March 2014, 12 pages, "Dedicated to Jim Lambek on the occasion of his
    90th birthday"), Crossref (DOI 10.1007/978-3-642-54789-8_1, pp. 1–13
    of Categories and Types in Logic, Language, and Physics: Essays
    Dedicated to Jim Lambek on the Occasion of His 90th Birthday, eds.
    Casadio, Coecke, Moortgat and Scott, Springer 2014; Crossref gives no
    volume number and only the year) and the Springer chapter page, which
    gives Lecture Notes in Computer Science volume 8222. `published:` is
    the arXiv v1 date. Not held in the Anthology of the SOTA: a grep of its
    record/ (clone pulled 2026-10-09, commit d8b5ba5) for the arXiv id,
    the title and Sadrzadeh found nothing; Abramsky appears there only
    as the co-author of LIT-016.
tags:
- linguistics
- contextuality
- compositionality
- pragmatics
- mathematics
- logic
- philosophy-of-language
- probabilistic-modeling
date: '2026-10-09'
published: '2014-03-13'
arxiv: '1403.3351'
doi: '10.1007/978-3-642-54789-8_1'
first_author: 'Abramsky'
keywords:
- 'sheaf theory'
- 'gluing'
- 'semantic unification'
- 'Discourse Representation Theory'
- 'anaphora resolution'
- 'distribution functor'
implementations: []
summary: >-
  Abramsky & Sadrzadeh (2014), [ARXIV-1403.3351](https://arxiv.org/abs/1403.3351), in the Lambek Festschrift
  (LNCS 8222, pp. 1–13). Models basic Discourse Representation Structures
  as sections of a presheaf of consistent literals over (vocabulary,
  variables), an anaphoric resolution as a cover by variable maps, and the
  meaning of a discourse as the gluing of its sentences' sections, unique
  when it exists. Failure to glue is inconsistency, not contextuality in
  the Abramsky–Brandenburger sense; competing resolutions are competing
  covers, ranked in the probabilistic section by corpus counts.
extends:
- LIT-016
supports:
- CLAIM-044
---

# LIT-tmph7en9: Semantic Unification: A Sheaf Theoretic Approach to Natural Language

Samson Abramsky and Mehrnoosh Sadrzadeh (2014), in C. Casadio, B. Coecke,
M. Moortgat and P. Scott (eds.), *Categories and Types in Logic, Language,
and Physics*, LNCS 8222, Springer, pp. 1–13 — [ARXIV-1403.3351](https://arxiv.org/abs/1403.3351),
DOI-10.1007/978-3-642-54789-8_1

## Key takeaways

- **The construction.** Objects are pairs (L, X) of a finite vocabulary of
  relation symbols and a finite set of variables; a morphism is an
  inclusion of vocabularies with any function on variables, so it can
  include, relabel or identify referents. F(L, X) is the set of deductive
  closures of consistent finite sets of literals over X in L, and
  restriction along f pulls a literal ±A(x) back exactly when ±A(f(x))
  holds. A basic DRS is a section.
- **Semantic unification is gluing.** A cover is a jointly surjective
  family fᵢ : (Lᵢ, Xᵢ) → (L, X) with L the union of the Lᵢ; a gluing is a
  section s over (L, X) restricting to each sᵢ. Proposition 1: if a
  gluing exists it is unique (the deductive closure of the pushed-forward
  literals). So "the intelligence of the semantic unification operation is
  in the choice of cover": DRT's merging of referents is the cover, and the
  gluing condition checks that the merge is semantically correct.
- **What blocks a gluing.** With disjoint vocabularies, as in all the
  linguistic examples, only inconsistency: "John owns a donkey. It is
  grey" fails to glue on the cover that merges "it" with John (Man(x)
  against ¬Man(y)) and glues on the one that merges it with the donkey.
  With shared vocabulary the gluing can also fail because the merged
  section says more about a local referent than its local section did
  (the R, S example after Proposition 1). Neither is a compatible family
  without a global section: the paper defines no overlap condition and
  exhibits no contextuality in the sense of [LIT-016](LIT-016.md).
- **Ambiguity is a choice among covers.** "John put the cup on the plate.
  He broke it" has two covers, each with its unique gluing. The
  probabilistic section composes F with a distribution functor D_R over a
  commutative semiring, invokes maximum entropy without using it, and in
  its worked example ("John gave the bananas to the monkeys. They were
  ripe. They were cheeky.") ranks the four candidate covers by summed
  British News corpus counts of "ripe banana", "cheeky monkey" and so on
  (14/48, 24/48, 0, 10/48), choosing bananas-ripe, monkeys-cheeky.

## Standing in the record

Filed on 2026-10-09 at the owner's request, as the paper that first carried
the sheaf-theoretic treatment of contextuality ([LIT-016](LIT-016.md), [NOTE-016](../notes.d/NOTE-016.md)) into
natural-language semantics. It sits between the record's contextuality line
([LIT-016](LIT-016.md), [LIT-277](LIT-277.md), [LIT-265](LIT-265.md); [THEORY-012](../theory.d/THEORY-012.md)) and its compositional
distributional semantics ([LIT-273](LIT-273.md), [LIT-272](LIT-272.md)), and beside Heim's file change
semantics ([LIT-838](LIT-838.md)), DRT's sister theory. It bears on the sheaf vocabulary
of the manuscript *What Survives Translation?* (line
`pragmatic-transport`); [NOTE-tmp3cvly](../notes.d/NOTE-tmp3cvly.md) says how.
