---
status: Active
status_note: 'read in full 2026-09-26 ([NOTE-tmpsyjjc](../notes.d/NOTE-tmpsyjjc.md)); Worth reading as a compact, correct statement and proof of the lemma with the embedding and the iso-determination corollary. It also has a "Necessity of naturality" section, which textbooks rarely include and which any structuralist reading of the lemma needs. Two caveats: its classical statement does not state naturality in c and X (the HoTT section does), and its finite counterexample is ill-formed as written.'
title: 'Yoneda lemma'
version: 2
history:
- version: 2
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
    against the book.); the first NOTE on it, since it was seeded from the
    abstract alone. Status set from the reading: Active.
tags:
- mathematics
- identity
date: '2026-09-26'
published: '2009-01-08'
url: 'https://ncatlab.org/nlab/show/Yoneda+lemma'
first_author: 'nLab'
keywords:
- 'Yoneda lemma'
- 'Yoneda embedding'
- 'representable presheaf'
- 'natural transformation'
- 'fully faithful functor'
- 'universal element'
implementations: []
summary: >-
  nLab (2009), <https://ncatlab.org/nlab/show/Yoneda+lemma>. The page
  states that for a locally small category C, every presheaf X and every
  object c, there is a canonical bijection Hom_{[C^op,Set]}(y(c), X) ≅
  X(c), given by η ↦ η_c(id_c). It proves the bijection by chasing id_c
  around a naturality square. From it the page derives that the Yoneda
  embedding y: c ↦ Hom_C(−,c) is fully faithful and that y(c) ≅ y(d) ⇔ c ≅
  d. It also shows by counterexample that the hypothesis doing the work is
  naturality: objects whose hom-sets are pointwise in bijection need not
  be isomorphic.
---

# LIT-tmpkwo0i: Yoneda lemma

nLab contributors (principal author Urs Schreiber) (2009), *nLab (ncatlab.org), a collaborative wiki for category theory and higher structures* — <https://ncatlab.org/nlab/show/Yoneda+lemma>

## Key takeaways

- The page states that for a locally small category C, every presheaf X and every object c, there is a canonical bijection Hom_{[C^op,Set]}(y(c), X) ≅ X(c), given by η ↦ η_c(id_c). It proves the bijection by chasing id_c around a naturality square. From it the page derives that the Yoneda embedding y: c ↦ Hom_C(−,c) is fully faithful and that y(c) ≅ y(d) ⇔ c ≅ d. It also shows by counterexample that the hypothesis doing the work is naturality: objects whose hom-sets are pointwise in bijection need not be isomorphic.

## Standing in the record

Filed at the owner's request on 2026-09-26, for an account of the Yoneda lemma, connected where the literature allows to ontic structural realism. It was filed `Deferred`, unread. [NOTE-tmpsyjjc](../notes.d/NOTE-tmpsyjjc.md) is the close reading of 2026-09-26, and it placed the work: **Active** — Worth reading as a compact, correct statement and proof of the lemma with the embedding and the iso-determination corollary. It also has a "Necessity of naturality" section, which textbooks rarely include and which any structuralist reading of the lemma needs. Two caveats: its classical statement does not state naturality in c and X (the HoTT section does), and its finite counterexample is ill-formed as written.
