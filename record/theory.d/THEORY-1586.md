---
number: 1586
status: Active
formerly:
- THEORY-tmp8vjtt
title: 'Abramsky and Sadrzadeh model a basic discourse representation structure as a section of a presheaf of consistent literals, a choice of anaphoric resolution as a cover and a discourse''s meaning as the gluing, unique when it exists; in their linguistic examples the only obstruction to gluing is inconsistency of literals, which is not contextuality in Abramsky and Brandenburger''s sense'
version: 3
history:
- version: 1
  date: '2026-11-11'
  note: >-
    Filed from NOTE-644 (read 2026-10-09), at the read-and-file pass
    of 2026-11-11, which found the work read and no reading filed.
- version: 2
  date: '2026-11-11'
  note: >-
    Promoted at the status review's ruling (the owner delegated these
    rulings): ADR-065 §2, a reported title read in full in NOTE-644,
    nothing in the record contradicting it. The title already limits
    the claim about obstructions to the paper's linguistic examples,
    so the narrowing of that claim elsewhere in the record does not
    contradict it.
- version: 3
  date: '2026-11-11'
  note: >-
    corroborates CLAIM-044: its text says "Sharpened by Abramsky and
    Sadrzadeh". Defect sweep of 2026-11-11, at the status review's
    ruling (the owner delegated these rulings; ADR-058): the claim's LIT
    ground on this work is moved to corroboration by this reading, which
    the claim does not stand on. The quotation of QUESTION-026 in "What it bears on" now gives the question's wording as the same sweep narrowed it. No other change.
tags:
- linguistics
- contextuality
date: '2026-11-11'
source:
- LIT-841
summary: >-
  Abramsky and Sadrzadeh (2014), [LIT-841](../literature.d/LIT-841.md), read in [NOTE-644](../notes.d/NOTE-644.md) from the
  arXiv preprint. Basic DRS only, with no Grothendieck topology and no
  condition on overlaps. All the interpretive work is in choosing the
  cover. Its probabilistic section places a distribution on candidate
  global sections by summed corpus counts rather than gluing local
  distributions.
bears_on:
- QUESTION-026
corroborates:
- CLAIM-088
- CLAIM-044
---

# THEORY-1586: Abramsky and Sadrzadeh model a basic discourse representation structure as a section of a presheaf of consistent literals, a choice of anaphoric resolution as a cover and a discourse's meaning as the gluing, unique when it exists; in their linguistic examples the only obstruction to gluing is inconsistency of literals, which is not contextuality in Abramsky and Brandenburger's sense

## The account

Resolving anaphora is choosing how to identify the referents of separate
sentences; once that identification, the cover, is fixed, the global
meaning either exists, uniquely, or the identification is semantically
wrong (Proposition 1, §4.2). Interpretation lives in the cover, and the
gluing condition checks it. Ambiguity is a set of admissible covers.

## Evidence

- Proposition 1: for a cover and a family of sections, a gluing, if it
  exists, is the deductive closure of the pushed-forward literals; it is
  a gluing if consistent and if it restricts to each local section.
- "John owns a donkey. It is grey.": merging "it" with John is
  inconsistent, merging it with the donkey glues (§4.3).
- A non-linguistic example with shared vocabulary fails to glue without
  inconsistency, by over-determining a local section (§4.2); in every
  linguistic example the vocabularies are disjoint, so consistency is
  the only obstruction.
- The ranking of covers by summed counts gives weight to a reading with
  a zero-count pattern; 10/48 is printed as 0.205 (§5.1).

## What it bears on

[QUESTION-026](../questions.d/QUESTION-026.md) calls this paper the meeting point between categorical
semantics and the record's transport: "The meeting point already exists.
Abramsky and Sadrzadeh's Semantic Unification ([LIT-841](../literature.d/LIT-841.md), [NOTE-644](../notes.d/NOTE-644.md)) builds
a presheaf of discourse representations and glues sentence meanings over
a cover of anaphoric resolutions. ... In its linguistic examples the
obstruction to gluing is inconsistency of literals; its one
shared-vocabulary example fails by over-determining a local section.
Neither is contextuality, and it has no transport."
The reading is that premise, and it does not answer the question, which
asks about transport.

[CLAIM-088](../claims.d/CLAIM-088.md) says that by 2014 "sheaf-structured meaning for discourse
already existed: Abramsky and Sadrzadeh ([LIT-841](../literature.d/LIT-841.md)). Only the pragmatic
and transport use of it remains for the manuscript to claim, which
supports this claim's narrowing." The reading is independent evidence
for that narrowing, which the claim does not rest on.
