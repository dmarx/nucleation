---
status: Active
status_note: 'read in full 2026-11-11 ([NOTE-tmpy1111](../notes.d/NOTE-tmpy1111.md)), from a course copy (University of Minnesota Duluth readings page).'
title: 'Reflections on trusting trust'
version: 1
history:
- version: 1
  date: '2026-11-11'
  note: >-
    Filed and read the same day, at the owner's filing of a related
    anecdote (LIT-tmp1lu07), as the documented original of the mechanism
    it tells. Metadata from Crossref (doi:10.1145/358198.358210):
    Communications of the ACM 27(8), 761-763, August 1984; Crossref gives
    the month only, so `published` is the first of the month. Read from a
    course copy of the journal pages (d.umn.edu), every page.
tags:
- epistemology
date: '2026-11-11'
published: '1984-08-01'
doi: '10.1145/358198.358210'
first_author: 'Thompson'
keywords:
- 'trojan-horse'
- 'self-reproducing-program'
- 'compiler'
- 'trust'
implementations: []
summary: >-
  Ken Thompson's Turing Award lecture. In three stages it builds a C
  compiler binary that miscompiles the login command to accept a known
  password and reinserts that change, and itself, whenever the compiler is
  rebuilt from clean source, so the Trojan horse lives in no source at
  all. Its moral: "No amount of source-level verification or scrutiny
  will protect you from using untrusted code." The record holds it as the
  documented form of a mechanism installed by one party and reproduced by
  the host's own process, bearing on [QUESTION-tmpmus93](../questions.d/QUESTION-tmpmus93.md).
---
<!-- inactive-ok-file: THEORY-tmpkzkpc — Proposed; the readings filed with this entry, cited with their standing -->

# LIT-tmpng40s: Reflections on trusting trust

Ken Thompson, Communications of the ACM 27(8), 761-763 (1984). Read in
full: [NOTE-tmpy1111](../notes.d/NOTE-tmpy1111.md). The record's account of it: [THEORY-tmpkzkpc](../theory.d/THEORY-tmpkzkpc.md).

## Standing in the record

The documented original of the compiler attack in [LIT-tmp1lu07](LIT-tmp1lu07.md)'s story,
and the mechanism [CASE-tmp4xp5m](../cases.d/CASE-tmp4xp5m.md) holds. It bears on [QUESTION-tmpmus93](../questions.d/QUESTION-tmpmus93.md).
