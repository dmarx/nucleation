---
status: Deferred
status_note: seeded from the abstract and a skim on 2026-09-25; not read in full
title: 'two-level type theory [descriptive title: nLab wiki entry "two-level type theory"]'
version: 1
tags:
- mathematics
date: '2026-09-25'
published: '2018-04-16'
url: 'https://ncatlab.org/nlab/show/two-level+type+theory'
first_author: 'nLab'
keywords:
- 'two-level type theory'
- '2LTT'
- 'fibrant types'
- 'strict equality'
- 'semisimplicial types'
- 'Homotopy Type System'
implementations: []
summary: >-
  nLab (2018), <https://ncatlab.org/nlab/show/two-level+type+theory>. Two-level type theory pairs a homotopy (univalent, fibrant) type theory with an outer level having UIP "exact equality" (the internalised metatheory). This lets one reason explicitly about the presenting model category, e.g. to define semisimplicial types by induction on strict equalities. Whether this breaks the (∞,1) principle of equivalence, and how many natural-number types to have, are open design questions.
---

# LIT-tmp5pvvl: two-level type theory [descriptive title: nLab wiki entry "two-level type theory"]

nLab contributors (collaborative wiki; the page history does not name authors in the text I read) (2018), *nLab (collaborative wiki)* — <https://ncatlab.org/nlab/show/two-level+type+theory>

## Key takeaways

- Two-level type theory pairs a homotopy (univalent, fibrant) type theory with an outer level having UIP "exact equality" (the internalised metatheory). This lets one reason explicitly about the presenting model category, e.g. to define semisimplicial types by induction on strict equalities. Whether this breaks the (∞,1) principle of equivalence, and how many natural-number types to have, are open design questions.

*Seeded from the abstract and a skim, not a reading. What follows is what the work says about itself.*

The page describes 2LTT as versions of Martin-Löf type theory with two layers: an inner homotopy type theory (univalent universes, higher inductive types) and an outer traditional type theory satisfying uniqueness of identity proofs, which can be read as the internalised metatheory of the first. The inner types are called fibrant and the outer ones pretypes, following fibration-category and model-category semantics. The trade-off is explicit control over the presenting model category at the apparent cost of the (∞,1)-categorical principle of equivalence. The extent of that cost is an open question.

## Standing in the record

Filed from the survey of 2026-09-25 of work the anthology set aside as out of scope (tier C): 365 seconds of active reading over 1 session in the papers-feed tracker. `Deferred` because nobody has read it closely here yet, not on merit.

**Priority for a deeper reading: low — It is a short wiki page, read in full here (t=365, n=1). Any further reading should go to arXiv:1705.03307, not the page.**

What a deeper reading should check:

- The survey says "drop: a wiki page, not a work". If kept, the note should cite the canonical paper, Annenkov–Capriotti–Kraus–Sattler, arXiv:1705.03307, not the wiki. That is the preferred source under the record's arxiv > doi > url rule.
- It pairs directly with c22 (Riehl–Shulman), which names 2LTT as the "brute force" option it declines in favour of shapes and extension types.

Access when seeded: I fetched the live page HTML and read the whole body text (Idea, Type theories, Applications/Semisimplicial types, Variations/Natural numbers, See also, References). It was last revised 2024-02-23. The page history shows 10 revisions, with revision 1 on 2018-04-16 15:49:56. I use that as the date of first appearance. The wiki may predate that history (older nLab content was migrated), so the true creation date is unverified.
