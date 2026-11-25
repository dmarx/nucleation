---
status: Unavailable
status_note: >-
  no lawful copy found, 2026-11-22. Crossref and OpenAlex list the
  publisher's page and Project Euclid and no open copy (OpenAlex:
  oa_status closed, no repository full text). The Cambridge Core page,
  cambridge.org/core/journals/journal-of-symbolic-logic/article/on-the-interpretation-of-intuitionistic-number-theory/7218DF16E8159E56642409787E6E2CDA,
  redirects to the abstract and offers "Get access to the full version of
  this content"; the JSTOR record (doi:10.2307/2269016) is the same
  subscription copy. Two web searches for a course, faculty or author copy
  found none. Read in its stead: van Oosten's historical essay,
  [LIT-tmpegqz0](LIT-tmpegqz0.md), which states the 1945 definition clause by clause and its
  results.
title: 'On the interpretation of intuitionistic number theory'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed, not read, for LEAD-215. Citation checked against Crossref
    on 2026-11-22: S. C. Kleene, Journal of Symbolic Logic 10(4), 109–124,
    December 1945 (month only; the first of the month is `published:`,
    per ADR-002, by the record's convention for month-only dates).
    Searched record/literature.d for the DOI, the title, "Kleene" and
    "realizab" on 2026-11-22: nothing held (the record's `realizability`
    line and its "realizer" are other senses; see the curation entry).
    No lawful copy was found (status note); the stand-in LIT-tmpegqz0 was
    registered and read in NOTE-tmpajfia (ADR-114).
tags:
- logic
- mathematics
- philosophy-of-mathematics
date: '2026-11-22'
published: '1945-12-01'
doi: '10.2307/2269016'
first_author: 'Kleene'
keywords:
- 'realizability'
- 'intuitionistic arithmetic'
- 'recursive functions'
- 'Church''s rule'
summary: >-
  Kleene (1945) introduces recursive realizability: a definition, by
  induction on an arithmetical sentence, of what it is for a natural number
  to realize it, under which every theorem of intuitionistic arithmetic has
  a realizer. Registered for [LEAD-215](../leads.d/LEAD-215.md), to test [CLAIM-949](../claims.d/CLAIM-949.md)'s
  reading of Kleene's realizer as the record's realization with its witness
  kept, and the witness and certificate pair ([TERM-154](../terms.d/TERM-154.md),
  [TERM-153](../terms.d/TERM-153.md)). Unread; what is said of it here is van Oosten's account
  ([LIT-tmpegqz0](LIT-tmpegqz0.md), [THEORY-tmpqj2d4](../theory.d/THEORY-tmpqj2d4.md)), not verified against Kleene's text.
---
<!-- inactive-ok-file: CLAIM-949 TERM-154 TERM-153 THEORY-tmpqj2d4 — Proposed or Open; the claim, terms and lead this work was registered for, and the stand-in's reading -->

# LIT-tmp9cdlq: On the interpretation of intuitionistic number theory

S. C. Kleene (1945). *Journal of Symbolic Logic* 10(4): 109–124.
DOI-10.2307/2269016

## Key takeaways

*Not read.* By van Oosten's account ([NOTE-tmpajfia](../notes.d/NOTE-tmpajfia.md), pp. 3–7 of the author's
copy): the paper defines, by six inductive clauses, when a number n
realizes an arithmetical sentence. A true atomic sentence is realized by
0; a conjunction by a pair of realizers; a disjunction by a tagged realizer
of one disjunct; an implication or a universal by the index of a partial or
total recursive function carrying realizers to realizers; and an
existential ∃xφ(x) by a pair ⟨m, k⟩ with k realizing φ(m). Every theorem
of Heyting arithmetic is realized; from a minimal variant Kleene obtains a
weak Church's rule, and the paper shows double-negation shift underivable.
Kleene called the analysis "not ... more than a partial analysis of the
intuitionistic meaning of the statements" (§2, as van Oosten quotes it).

## Standing in the record

Registered on 2026-11-22 for [LEAD-215](../leads.d/LEAD-215.md). Unavailable; [LIT-tmpegqz0](LIT-tmpegqz0.md) stands
in for it. How far: van Oosten states all six clauses of the 1945
definition, the soundness theorem (in the "glued" form he gives it), the
weak Church's rule and the underivability of double-negation shift, and
says which later results are not in the paper (the existence and
disjunction properties). He quotes Kleene's 1945 text once, and Kleene's
motivation from the later retrospective (1973), not from 1945. What the
stand-in does not give: Kleene's own wording and notation, his formalized
realizability as he set it out, and the paper's argument for the
definition. A claim that leans on Kleene's own words needs this paper read.
