---
status: Active
status_note: >-
  read in part 2026-11-05 (NOTE-tmplptka) from arXiv v1; registered as the
  open stand-in for formal concept analysis, whose canonical sources the
  record holds unread (LIT-344, Ganter & Wille, and LIT-337, Wille 2000,
  both Unavailable). Worth reading as a lawful, citable statement of the
  core of FCA, which its theory sections say they "mainly reproduce" from
  Ganter & Wille: formal contexts, derivation operators and their Galois
  property, closure operators, formal concepts, the concept lattice and the
  Basic Theorem, attribute implications, Armstrong rules and the
  Duquenne–Guigues base. It stands in for the first chapters of LIT-344,
  not for its structure theory, and for LIT-337 only for the FCA that paper
  extends, not for its Boolean concept logic. Its main limits: a tutorial,
  with exercises in place of proofs, a few typographical slips in the
  definitions, and some 80 pages of IR-oriented application surveys not
  read here.
title: 'Introduction to Formal Concept Analysis and Its Applications in Information Retrieval and Related Fields'
version: 1
history:
- version: 1
  date: '2026-11-05'
  note: >-
    Registered and read in part on 2026-11-05, at the owner's request, as
    a stand-in for the unread canonical sources of formal concept analysis.
    The owner's pasted synthesis on resource-bounded realizability (written
    by another assistant, A, in the same exchange as the
    emergency-readiness bibliography, pasted 2026-11-04) calls its
    demand–configuration Galois connection "an established construction in
    formal concept analysis" and cites only a link to moex.inria.fr, which
    could not be reached and is not identified. The canonical sources are
    held Unavailable (LIT-344, LIT-337); this tutorial was chosen as the
    open neighbour. A does not cite it. Citation checked against Crossref
    and the arXiv listing: Dmitry I. Ignatov, sole author (National
    Research University Higher School of Economics, Moscow), in Information
    Retrieval (RuSSIR 2014), Communications in Computer and Information
    Science 505 (volume from the arXiv journal reference; Crossref gives
    none), pp. 42–141, Springer, doi:10.1007/978-3-319-25485-2_3, book
    chapter online 2015-12-10, which is `published:`; arXiv:1703.02819, v1
    of 2017-03-08, the only version. Not held before. Copy: arXiv v1 PDF,
    https://arxiv.org/pdf/1703.02819v1, 102 pp., extracted with pdftotext
    -layout. Status set to Active.
tags:
- mathematics
date: '2026-11-05'
published: '2015-12-10'
arxiv: '1703.02819'
doi: '10.1007/978-3-319-25485-2_3'
first_author: 'Ignatov'
keywords:
- 'formal concept analysis'
- 'formal context'
- 'derivation operators'
- 'Galois connection'
- 'concept lattice'
- 'attribute implications'
- 'Duquenne-Guigues base'
- 'information retrieval'
implementations: []
summary: >-
  Ignatov (2015). Lecture notes for the RuSSIR 2014 summer school. The
  theory sections restate Ganter & Wille: a formal context is two sets and
  a relation between them; the derivation operators form an antitone Galois
  connection, A ⊆ B′ ⇔ B ⊆ A′ ⇔ A × B ⊆ I; their composites are closure
  operators; the closed pairs, formal concepts, form a complete lattice,
  and every complete lattice is a concept lattice (the Basic Theorem, after
  Wille 1982); an attribute implication A → B holds when each object with
  all of A has all of B, implications obey the Armstrong rules, and the
  Duquenne–Guigues base is a minimum base. Exercises replace proofs. The
  remainder surveys FCA in machine learning, data mining, information
  retrieval, text mining and ontologies.
---
<!-- inactive-ok-file: LIT-344 LIT-337 NOTE-tmplptka THEORY-tmp8atfa — Unavailable, or Skimmed or Proposed and new; the canonical sources this stands in for, and the account filed from it -->

# LIT-tmpnheem: Introduction to Formal Concept Analysis and Its Applications in Information Retrieval and Related Fields

Ignatov, D. I. (2015). Introduction to Formal Concept Analysis and Its Applications in Information Retrieval and Related Fields. In *Information Retrieval: 8th Russian Summer School, RuSSIR 2014*, Communications in Computer and Information Science 505, 42–141. Springer. doi:10.1007/978-3-319-25485-2_3. arXiv:1703.02819.

## Key takeaways

*From the reading, NOTE-tmplptka. Page numbers are the arXiv PDF's.*

- **A restatement.** "In this section, we mainly reproduce basic definitions
  from Ganter&Wille’s book on Formal Concept Analysis" (p. 3).
- **The context.** "A formal context K = (G, M, I) consists of two sets G and
  M and a relation I between G and M" (Definition 7, p. 6).
- **The Galois property.** For the derivation operators, A ⊆ B′ ⇔ B ⊆ A′ ⇔
  A × B ⊆ I (Proposition 1.5, p. 7), and both composites (·)′′ are closure
  operators (Exercise 4).
- **The Basic Theorem.** "Concept lattice B(G, M, I) is a complete lattice."
  and every complete lattice arises so: "In particular, L is isomorphic to
  B(L, L, ≤)." (Theorem 1, p. 9; stated, not proved).
- **Implications.** A → B holds when A′ ⊆ B′, "i.e., each object having all
  attributes from A also has all attributes from B." (Definition 17, p.
  15); "The Duquenne-Guigues base is a minimum (cardinality minimal)
  implication base." (p. 16).

## Standing in the record

Registered as a stand-in. The pasted synthesis on resource-bounded
realizability names formal concept analysis for its demand–configuration
Galois connection and cites an unreachable moex.inria.fr page; the
canonical works, LIT-344 (Ganter & Wille) and LIT-337 (Wille 2000), are held
Unavailable. This tutorial stands in for them this far: it states the
definitions and theorems of the first chapters of LIT-344 (contexts,
derivation operators, closures, concepts, the Basic Theorem, implications
and their bases, conceptual scaling) without proofs, and none of that
book's later structure theory (decompositions, morphisms, dimension). For
LIT-337 it gives only the base theory that paper extends; nothing on
negation, semiconcepts or protoconcepts. It is enough to check A's first
Galois connection, which is exactly the derivation-operator connection of
a formal context. Filed from it: THEORY-tmp8atfa.
