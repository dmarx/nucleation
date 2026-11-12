---
status: Active
status_note: >-
  Skimmed on 2026-11-12 ([NOTE-tmpds3ww](../notes.d/NOTE-tmpds3ww.md)) from the first author's own faculty page at the University of British Columbia (https://www.cs.ubc.ca/~gregor/papers/kiczales-ECOOP1997-AOP.pdf), the published text with Springer's notice, lawful under [ADR-074](../decisions.d/ADR-074.md). Registered as a stand-in for [LIT-tmpiyp1o](LIT-tmpiyp1o.md), The Art of the Metaobject Protocol, for its Part I, which was not reached; it stands in weakly, through one paragraph on metaobject protocols.
title: 'Aspect-oriented programming'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    (On the owner's ruling later the same day, "the mirror is fine", the book's chapter 5 was skimmed from that mirror, and this work now stands in for its Part I only.) Registered as a stand-in for LIT-tmpiyp1o, at the lead's decision that the only copy of that book's text reached, a community mirror of its chapters 5 and 6, was not shown lawful. Identifier checked on Crossref on 2026-11-12, no email address sent: Kiczales, Lamping, Mendhekar, Maeda, Lopes, Loingtier and Irwin, ECOOP'97, Lecture Notes in Computer Science 1241, pp. 220–242. Not held: no hit for the DOI, the title, "aspect-oriented" or Kiczales in record/literature.d. `published:`: Crossref gives the year only (online 2006-05-23); the copy's cover says "June 1997", so the first of that month is used. Skimmed in NOTE-tmpds3ww.
tags:
- software-engineering
date: '2026-11-12'
published: '1997-06-01'
doi: '10.1007/BFb0053381'
first_author: 'Kiczales'
keywords:
- aspect-oriented programming
- reflection
- metaobject protocols
implementations: []
summary: >-
  Gregor Kiczales, John Lamping, Anurag Mendhekar, Chris Maeda, Cristina Videira Lopes, Jean-Marc Loingtier and John Irwin (1997), ECOOP'97, LNCS 1241, DOI 10.1007/BFb0053381. Argues that some design decisions, which it calls aspects, cross-cut a system's functional decomposition and tangle procedural or object-oriented code, and that they are best written in separate aspect languages combined with the components by a weaver. Its §8.2 places reflection and metaobject protocols as one powerful tool for that goal, and §6.2 replaces raw reflective access, "so powerful that it can be dangerous or difficult to use", with a narrower aspect language. Here as a weak stand-in for Part I of The Art of the Metaobject Protocol (LIT-tmpiyp1o), which it cites.
---
<!-- inactive-ok-file: NOTE-tmpds3ww — Skimmed; the reading of this work -->

# LIT-tmpeg56k: Aspect-oriented programming

Gregor Kiczales, John Lamping, Anurag Mendhekar, Chris Maeda, Cristina Videira Lopes, Jean-Marc Loingtier and John Irwin (1997). "Aspect-oriented programming". ECOOP'97 — Object-Oriented Programming, LNCS 1241, Springer, pp. 220–242. DOI 10.1007/BFb0053381.

## Key takeaways

- Some design decisions cross-cut a system's basic functionality and cannot be captured cleanly in its functional decomposition (abstract, §3).
- Reflection gives "a base language and (one or more) meta-languages that provide control over the base language's semantics and implementation" (§8.2), and is a tool for AOP, not its goal.
- Unbounded reflective access is dangerous; the authors bound it with a purpose-built language (§6.2).

## Standing in the record

Registered on 2026-11-12 as a stand-in for [LIT-tmpiyp1o](LIT-tmpiyp1o.md). It restates the general idea of a meta-level that controls a language's own semantics, and cites the book as an instance; it does not restate the metaobject protocol for CLOS, its restrictions on users and implementors, or its dependent-maintenance protocol. It is by the book's first author and his group, and is otherwise about something else.
