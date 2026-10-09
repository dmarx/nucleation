---
number: 601
status: Skimmed
formerly:
- NOTE-tmp0fe8y
paper: 'LIT-803'
title: 'Seven Sketches in Compositionality'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Skimmed from arXiv v3 (12 October 2018, 353 PDF pages, text layer). Read
    closely: the preface and "How to read this book"; all of Chapter 1
    (generative effects, preorders, monotone maps, meets and joins, Galois
    connections, closure operators, level shifting, summary), exercises
    read but not worked; in Chapter 3, Section 3.1 ("What is a
    database?") to the first FQL listing, all of Section 3.4 (pulling back
    data, adjunctions, Σ and Π, single-set summaries), and the chapter
    summary. Read at their openings and summaries only: Chapters 2, 4, 5,
    6 and 7. Not read: the rest of Chapters 2–7 and the exercise
    solutions (one page looked at). The book's stated aims (preface) are
    an invitation to applied category theory through examples and a
    reference for monoidal categories; Chapter 1 is the chapter its own
    plan makes foundational, so it was the one read in full. The
    monoidal-category material of Chapters 2 and 4 was not read, so this
    note does not cover the second aim.
date: '2026-10-09'
summary: >-
  From Chapter 1 and Section 3.4: an observation is a monotone map, and a
  generative effect is its failure to preserve joins, Φ(a) ∨ Φ(b) < Φ(a ∨ b);
  left adjoints preserve joins, and out of a preorder with all joins a
  monotone map preserves joins iff it is a left adjoint. Database schemas
  are categories, instances functors to Set, and a schema map induces
  migrations Σ ⊣ Δ ⊣ Π. The other five chapters were seen only at their
  openings and summaries.
---

<!-- inactive-ok-file: LIT-344 — Deferred; named as the monograph whose order theory this overlaps, not leaned on -->
<!-- inactive-ok-file: CLAIM-119 — Proposed; named for the bearing reported, not edited -->

# NOTE-601: Seven Sketches in Compositionality

## Contribution

A textbook, not a research contribution: the results in the parts read are
standard order and category theory. What it adds is an organisation of
applied category theory around compositionality, with each chapter
pairing a modelling situation with one categorical idea, and an
introduction to monoidal categories written for readers outside
mathematics. Its first chapter makes "generative effect", from Elie Adam's
thesis, the motivating notion: what an observation of a whole shows that the
combined observations of its parts do not.

## Key insight

An observation of systems is a structure-preserving map, and the question
"what category are you working in?" is the question of which structure it
preserves. Observations that preserve order but not joins have generative
effects. Being a left adjoint is exactly the property that rules them out,
when the source has all joins. So "lossy observation" and "failure of
compositionality" become a precise statement about adjoints.

## Assumptions

- Preorders (reflexive, transitive) rather than partial orders; meets and
  joins defined up to equivalence.
- Theorem 1.115 needs the source of a join-preserving map to have all joins
  (dually, the source of a meet-preserving map all meets).
- In Chapter 3, schemas are finitely presented categories (graphs with path
  equations) and instances are Set-valued functors; Σ and Π are asserted to
  exist for every schema map, with details deferred to Spivak's other work.

## Key results

Chapter 1:

- **Definition 1.93 and Exercise 1.94.** For monotone f with the relevant
  joins, f(a) ∨ f(b) ≤ f(a ∨ b) always; f has a generative effect if the
  two sides differ for some a, b. Worked example: Φ on the five partitions
  of {•, ◦, ∗}, "is • connected to ∗?", is monotone, and joining two
  partitions in neither of which • and ∗ are connected can connect them.
- **Proposition 1.78.** Monotone maps P → Bool correspond to upper sets of
  P. **Exercise 1.66** is the Yoneda lemma for preorders: p ≤ p′ iff
  ↑p′ ⊆ ↑p.
- **Proposition 1.107.** f ⊣ g iff p ≤ g(f(p)) and f(g(q)) ≤ q for all p,
  q.
- **Proposition 1.111.** Right adjoints preserve meets; left adjoints
  preserve joins. Example 1.113: a right adjoint need not preserve joins.
- **Theorem 1.115 (adjoint functor theorem for preorders).** If Q has all
  meets, g : Q → P preserves meets iff it is a right adjoint, with left
  adjoint f(p) = ⋀{q | p ≤ g(q)}; dually for joins.
- **Section 1.4.2.** Any g : S → T induces g! ⊣ g* between partition
  preorders (push forward and take transitive closure; pull back).
- **Example 1.117.** For f : A → B, preimage f* has left adjoint the image
  f! and right adjoint f∗ (buckets all of whose apples are in the subset).
- **Section 1.4.4.** g∘f is a closure operator for any adjunction; every
  closure operator j arises from j ⊣ inclusion of its fixed points.
- **Section 1.4.5.** Reflexive–transitive closure is left adjoint to the
  inclusion of preorder relations into all relations.

Chapter 3 (sections read):

- **Definition 3.68.** Pulling back an instance I : D → Set along F : C → D
  is F ; I, giving Δ_F : D-Inst → C-Inst.
- **Definition 3.70 and Example 3.71.** Adjunctions as natural hom-set
  bijections; Galois connections are adjunctions between preorders.
- **Section 3.4.3–3.4.4.** Σ_F ⊣ Δ_F ⊣ Π_F; for ! : C → 1, Σ_! gives
  connected components and Π_! a selection (self-sent emails in the
  example). Σ-operations are built from colimits, Π-operations from limits
  (stated).

## Concepts

- **generative effect**: failure of a monotone map to preserve joins; "we
  see something when we observe the combined system that we could not
  expect by merely combining our observations of the pieces".
- **Galois connection / adjunction**: monotone f, g with f(p) ≤ q iff
  p ≤ g(q).
- **closure operator**: monotone j with p ≤ j(p) and j(j(p)) ≅ j(p).
- **data migration functors** Δ, Σ, Π: pullback along a schema map and its
  left and right adjoints.
- **coherence conditions**: the axioms that make structures "work well
  together"; the authors treat their choice as empirical.

## Connections

Chapter 1 follows Adam's thesis on generative effects (which goes on to
abelian categories and cohomology) and points to Galois connections in
program analysis. Chapter 3 descends from the categorical database work of
the mid-1990s and Rosebrugh's sketches, and from Spivak's functorial data
migration. The later chapters, seen only in summary, draw on Censi's
co-design, graphical linear algebra and Willems' behavioural approach,
Carboni–Walters and Fong's decorated cospans, and the topos-theory
literature.

## Bearing on the record

- **[CLAIM-119](../claims.d/CLAIM-119.md)** (communicative categories form a concept lattice).
  The book does not mention formal concept analysis. It supplies the order
  theory FCA rests on: the derivation operators of a formal context form an
  antitone Galois connection between subsets of objects and of attributes,
  and the formal concepts are the fixed points of the induced closure
  operators (Section 1.4.4's construction). That identification is my
  connection, not the book's; its Galois connections are covariant, and the
  antitone case is a short step. Bearing: it supports the claim's
  formal vocabulary, not the empirical claim about communicative categories.
- **Generative effects.** Definition 1.93 states precisely when an
  observation of a composite cannot be computed from observations of the
  parts. Whether a translation or reading of a combined text has such an
  effect is a question the definition makes precise; the book does not
  raise it, and no claim is made here.
- **[LIT-827](../literature.d/LIT-827.md)** (Backprop as Functor, same first two authors) is the
  research instance of the book's "functorial semantics" theme.
- No THEORY filed: the results read are textbook theorems the record has no
  use stating separately. No instruction for machine-learning practice.

## Limitations

- Skimmed: Chapters 2 and 4–7, including the book's own reference treatment
  of monoidal categories, were not read beyond openings and summaries; no
  claim here rests on them.
- The book proves only some of what it states; several equivalences (for
  instance g! ⊣ g* on partitions, and the existence of Σ and Π in general)
  are left to exercises or other sources.
- As an introduction it chooses examples "to our personal taste", by its own
  account, and does not survey applied category theory.

## Open questions

- Whether a full reading of Chapters 2 and 4 (monoidal preorders, enrichment,
  profunctors, monoidal categories) would support a THEORY on resource
  theories, which the record does not yet hold.
