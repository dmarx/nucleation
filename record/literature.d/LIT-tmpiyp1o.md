---
status: Active
status_note: >-
  Skimmed on 2026-11-12 ([NOTE-tmpyvjjb](../notes.d/NOTE-tmpyvjjb.md)): chapter 5 only, from the Association of Lisp Users' hypertext of chapters 5 and 6 mirrored at http://mop.lisp.se/www.alu.org/mop/concepts.html, made from TeX sources Xerox PARC distributed; the owner ruled on 2026-11-12 that the copy may be used ("the mirror is fine"). Part I (chapters 1 to 4) was not reached: the publisher's page (https://doi.org/10.7551/mitpress/1405.001.0001) showed a Cloudflare challenge, OpenAlex lists the book as closed, and the best neighbour for Part I, Kiczales, Ashley, Rodriguez, Vahdat and Bobrow, "Metaobject protocols: why we want them and what else they can do" (1993), is Unfetched (https://cseweb.ucsd.edu/~vahdat/papers/mop.pdf failed TLS verification on 2026-11-12). [LIT-tmpeg56k](LIT-tmpeg56k.md) stands in, weakly, for Part I.
title: 'The Art of the Metaobject Protocol'
version: 3
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Filed, not read. Identifier checked on 2026-11-12 with Crossref, and confirmed not held by DOI, exact title and first author in record/literature.d. `published:`: Crossref's date for the monograph. No email address was sent to any service. First application of ADR-tmppzz2h.
- version: 2
  date: '2026-11-12'
  note: >-
    Unavailable (ADR-041): no lawful copy reached; where it was sought is in the status note. The chapter-5 reading of a community mirror is not filed, at the lead's decision that the mirror's lawfulness is undetermined; the owner may rule otherwise. LIT-tmpeg56k registered and skimmed as a weak stand-in. Metadata unchanged.
- version: 3
  date: '2026-11-12'
  note: >-
    Active. The owner ruled on 2026-11-12, of the community hypertext of chapters 5 and 6: "the mirror is fine". Version 2's Unavailable, which followed the lead's earlier decision not to count that copy, is replaced by the reading: chapter 5 skimmed in NOTE-tmpyvjjb, account THEORY-tmph775l. LIT-tmpeg56k is kept as a stand-in for Part I, which was not reached. Metadata unchanged.
tags:
- software-engineering
date: '2026-11-12'
published: '1991-07-30'
doi: '10.7551/mitpress/1405.001.0001'
first_author: 'Kiczales'
keywords: []
implementations: []
summary: >-
  Gregor Kiczales, Jim des Rivières and Daniel G. Bobrow (1991), The MIT Press, DOI 10.7551/mitpress/1405.001.0001. Chapter 5, the only part read, specifies a metaobject protocol for CLOS: the language described as an extensible program whose metaobjects users may specialize, within explicit restrictions on users and implementors, with changes propagated to dependents. Read for the exchange "luria experiment design", where A cited it for a system that exposes its own behaviour to modification; it bears on [QUESTION-388](../questions.d/QUESTION-388.md) by placing such a system on the programmable side.
---
<!-- inactive-ok-file: ADR-tmppzz2h — Proposed; the decision this entry first applies -->
<!-- inactive-ok-file: NOTE-tmpyvjjb THEORY-tmph775l — Skimmed and Proposed; the reading of 2026-11-12 -->

# LIT-tmpiyp1o: The Art of the Metaobject Protocol

Gregor Kiczales, Jim des Rivières and Daniel G. Bobrow (1991), The MIT Press, DOI 10.7551/mitpress/1405.001.0001.

## Key takeaways

- Chapter 5 specifies the CLOS metaobject protocol as "a description of CLOS itself as an extensible CLOS program": users change the language by specializing its metaobjects.
- The extensions are bounded by explicit restrictions on users and on implementors.
- Redefinition propagates: discriminating functions are recomputed and registered dependents notified.
- A cited it for a system that exposes its own behaviour to modification through a meta-level interface, which is right for chapter 5; A's further remarks are A's.

## Standing in the record

Registered on 2026-11-12 from the exchange "luria experiment design" (https://chatgpt.com/share/6af35bfc-35f8-83e9-a63d-d594703eabda), at A50 (§12), once [ADR-tmppzz2h](../decisions.d/ADR-tmppzz2h.md) added `software-engineering`. Chapter 5 skimmed the same day ([NOTE-tmpyvjjb](../notes.d/NOTE-tmpyvjjb.md); [THEORY-tmph775l](../theory.d/THEORY-tmph775l.md)), from a copy the owner ruled usable. Part I, the book's argument for metaobject protocols, was not reached; [LIT-tmpeg56k](LIT-tmpeg56k.md) (Kiczales et al. 1997, aspect-oriented programming) stands in for it weakly, restating in one paragraph the idea of a meta-level controlling a language's own semantics.
