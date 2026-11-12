---
status: Unavailable
status_note: >-
  No lawful copy reached on 2026-11-12. The publisher's page (https://doi.org/10.7551/mitpress/1405.001.0001, redirecting to direct.mit.edu) showed a Cloudflare challenge; OpenAlex lists the book as closed, with the publisher's page its only location. Kiczales's faculty page at UBC (https://www.cs.ubc.ca/~gregor/) has no copy. A community hypertext of chapters 5 and 6 (the CLOS metaobject protocol specification) exists at http://mop.lisp.se/www.alu.org/mop/, made by Howard R. Stearns from TeX sources once distributed by Xerox PARC, with a second edition at http://metamodular.com/CLOS-MOP/; the reader read chapter 5 there, but whether that release is lawful could not be determined (PARC's terms are no longer visible, and it is a mirror, not the authors' or publisher's page), so the lead did not count it and nothing is filed from it. That judgement is left to the owner. Whole-book uploads were not sought. The best neighbour, Kiczales, Ashley, Rodriguez, Vahdat and Bobrow, "Metaobject protocols: why we want them and what else they can do" (1993), is Unfetched: https://cseweb.ucsd.edu/~vahdat/papers/mop.pdf failed TLS verification on 2026-11-12, and was not worked around. Stood in for, weakly, by LIT-tmpeg56k (Kiczales et al. 1997, aspect-oriented programming).
title: 'The Art of the Metaobject Protocol'
version: 2
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Filed, not read. Identifier checked on 2026-11-12 with Crossref, and confirmed not held by DOI, exact title and first author in record/literature.d. `published:`: Crossref's date for the monograph. No email address was sent to any service. First application of ADR-tmppzz2h.
- version: 2
  date: '2026-11-12'
  note: >-
    Unavailable (ADR-041): no lawful copy reached; where it was sought is in the status note. The chapter-5 reading of a community mirror is not filed, at the lead's decision that the mirror's lawfulness is undetermined; the owner may rule otherwise. LIT-tmpeg56k registered and skimmed as a weak stand-in. Metadata unchanged.
tags:
- software-engineering
date: '2026-11-12'
published: '1991-07-30'
doi: '10.7551/mitpress/1405.001.0001'
first_author: 'Kiczales'
keywords: []
implementations: []
summary: >-
  Gregor Kiczales, Jim des Rivières and Daniel G. Bobrow (1991), The MIT Press, DOI 10.7551/mitpress/1405.001.0001. Here because A cited it in the exchange "luria experiment design" at A50 (§12), for a programming system that makes aspects of its own behaviour explicit and modifiable through a meta-level interface, a predecessor A names for a collective that modifies its own working infrastructure; A adds that a record is not a universal reflective system, and that a changed rule counts only if it changes later behaviour. It bears on QUESTION-388 (what distinguishes a programmable system from one that governs its own reconfiguration) and CLAIM-469 (luria as an apparatus that revises its own distinctions). What A says of it is unverified until read.
---
<!-- inactive-ok-file: ADR-tmppzz2h — Proposed; the decision this entry first applies -->

# LIT-tmpiyp1o: The Art of the Metaobject Protocol

Gregor Kiczales, Jim des Rivières and Daniel G. Bobrow (1991), The MIT Press, DOI 10.7551/mitpress/1405.001.0001.

## Key takeaways

*Seeded from the exchange, not read.* A cites it for a programming system that makes aspects of its own behaviour explicit and modifiable through a meta-level interface, a predecessor A names for a collective that modifies its own working infrastructure; A adds that a record is not a universal reflective system, and that a changed rule counts only if it changes later behaviour. Unverified until read.

## Standing in the record

Unavailable since 2026-11-12. LIT-tmpeg56k stands in weakly: by the first author and his group, it restates in one paragraph (§8.2) the idea of a meta-level controlling a language's own semantics and cites this book, and restates nothing of the protocol itself, its restrictions or its dependent maintenance. The 1993 paper named in the status note would stand in better, if reached.


Registered on 2026-11-12 from the exchange "luria experiment design" (https://chatgpt.com/share/6af35bfc-35f8-83e9-a63d-d594703eabda), at A50 (§12), once ADR-tmppzz2h added `software-engineering`. It bears on QUESTION-388 (what distinguishes a programmable system from one that governs its own reconfiguration) and CLAIM-469 (luria as an apparatus that revises its own distinctions).
