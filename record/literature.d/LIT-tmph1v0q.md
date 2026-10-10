---
status: Deferred
status_note: 'registered 2026-10-10 from its Crossref record, not read, to ground the record''s use of the do-operator in [CLAIM-127](../claims.d/CLAIM-127.md) (version 2) and [CLAIM-tmp2i7yj](../claims.d/CLAIM-tmp2i7yj.md). No full text was sought; the book is in print with Cambridge University Press. No NOTE is filed. It stays Deferred until it is read, not on merit.'
title: 'Causality: Models, Reasoning, and Inference'
version: 1
history:
- version: 1
  date: '2026-10-10'
  note: >-
    Registered, not read. The exchange's do() move is the owner's (U41,
    2026-10-09: "this feels to me like an opportunity for Judea Pearl's
    `do()` notation"), and A129 §1 formalized it, citing only unresolved
    search handles, so which of Pearl's works A129 drew on cannot be
    checked. This, the second edition of the book, is filed as the
    standard statement of the calculus. Details checked against Crossref
    on 2026-10-10 (DOI 10.1017/CBO9780511803161, monograph, Cambridge
    University Press, edition 2, sole author Judea Pearl; print
    publication 14 September 2009, online 5 March 2013; ISBNs
    9780511803161, 9780521895606 and 9780521749190). `published:` is the
    print date, the earliest full date Crossref gives (ADR-002). Not held
    in the Anthology of the SOTA: a grep of its record/ (clone of
    2026-10-09, commit d8b5ba5) for "Pearl" found nothing.
tags:
- causality
- probabilistic-modeling
date: '2026-10-10'
published: '2009-09-14'
doi: '10.1017/CBO9780511803161'
first_author: 'Pearl'
keywords: []
implementations: []
summary: >-
  Pearl (2009), second edition, Cambridge University Press. The standard
  statement of structural causal models and the do-operator, which
  separates conditioning on an observed value from setting a variable by
  replacing its structural equation. Registered unread, as the source the
  record's causal layer cites.
supports:
- CLAIM-127
- CLAIM-tmp2i7yj
---

<!-- inactive-ok-file: CLAIM-127 CLAIM-tmp2i7yj — Proposed; the claims this registration grounds, cited as open -->

# LIT-tmph1v0q: Causality: Models, Reasoning, and Inference

Judea Pearl (2009), 2nd edition, Cambridge: Cambridge University Press —
DOI-10.1017/CBO9780511803161

## Key takeaways

*Registered, not read.* Nothing below is from the book's text. It records
only what the record uses the book for.

- **The do-operator.** P(Y | do(X = x)) is the distribution of Y when X is
  set to x by replacing X's structural equation, the other equations left
  in place. It differs in general from P(Y | X = x), which conditions on
  the cases where X happens to be x. A129 §1 uses the distinction in these
  terms.

## Standing in the record

Registered on 2026-10-10 so that the record's causal claims name a source.
[CLAIM-127](../claims.d/CLAIM-127.md) (version 2) separates conditioning on a communicative situation,
intervening on it and intervening on what the interpreter is told.
[CLAIM-tmp2i7yj](../claims.d/CLAIM-tmp2i7yj.md) draws the experimental consequence of the last two. Both
rest on the calculus only for the definition of do(); neither uses an
identification result. A reading would say which of the book's results
bear on A129's schematic, one-step and unidentified model of the
interpreter, and what it offers for sequential framing, which needs
time-indexed states that A129 does not write.
