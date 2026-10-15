---
status: Read
paper: LIT-tmp3l2ha
title: Levy, Mendelzon, Sagiv & Srivastava — Answering queries using views
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Read in full from the authors' camera-ready of the PODS 1995 extended abstract
    (10 pp., numbered 95–104 as in the proceedings; PostScript produced by dvips
    from a file named realfinal.dvi), linked from Alberto Mendelzon's University
    of Toronto publications page (www.cs.toronto.edu/~mendel/papers.html, which
    links ftp://ftp.db.toronto.edu/pub/papers/pods95LMSS.ps.Z). The FTP host timed
    out from this environment; the same file was fetched over HTTP from www.cs.toronto.edu/pub/papers/pods95LMSS.ps.Z
    on 2026-10-15, decompressed, and converted to PDF with Ghostscript (-dSAFER).
    ACM's open-access PDF (Unpaywall: gold) returned 403 here, and CiteSeerX (10.1.1.53.3114)
    reset the connection. Text extracted with pdftotext; the extraction drops the
    fi, fl and ff ligatures and the mathematical symbols (⊆, π∅, Σ, Π, ≤), so Proposition
    3.1, Proposition 3.2, Lemma 3.3, Lemma 3.5, Theorem 3.7, Corollary 3.8, Theorem
    3.9, Theorem 3.10 and Theorem 4.4 were read from page images (pp. 97–102). Read:
    all of §§1–5 and the reference list. Nothing skipped. It is an extended abstract;
    several proofs are deferred to a "full paper" that was not read. Every quotation
    below was checked by script against the extracted text, with whitespace, line-end
    hyphenation and the dropped ligatures normalised.
date: '2026-10-15'
summary: >-
  For conjunctive queries and views, a view can be used in an equivalent rewriting
  of a query exactly when there is a containment mapping (a homomorphism of bodies)
  from the view into the query, so every possible use of a stored view is found
  among those mappings. Without comparison predicates, a minimal rewriting needs
  no more literals than the query and no new variables, which puts the search in
  NP; deciding whether some rewriting uses a given set of views (with comparisons
  only in the query), whether a rewriting with fewer than k literals exists, and
  whether a rewriting using only the views exists are each NP-complete, and with
  comparisons in both query and views existence is Π2p-complete. The hardness has
  two independent sources, the number of mappings and the choice of which query
  literals to drop, and a polynomial algorithm removes the redundant literals for
  a given mapping, exactly under stated conditions. Only equivalent rewritings are
  studied; contained rewritings, the cost of the resulting plan and the size of
  view collections are outside it.
---

# NOTE-tmp7vihx: Levy, Mendelzon, Sagiv & Srivastava — Answering queries using views

## Contribution

The paper sets out the problem of computing a query from stored views, for
query optimization, mobile and global information systems and physical
data independence, and reduces it to query containment. Earlier work had
found uses of a view by syntactic or one-to-one matching. This paper shows
that every use of a view is given by a containment mapping from the view's
body into the query's body, which makes the space of rewritings well
defined. On that basis it classifies the complexity of finding a rewriting,
a minimal one and a complete one (one that uses nothing but the views),
and gives an algorithm for the step of deleting redundant query literals.
In the abstract's words: "We show that all the possible rewritings can be
obtained by considering containment mappings from the views to the query,
and that the problems we consider are NP-complete when both the query and
the views are conjunctive and don't involve built-in comparison
predicates."

## Key insight

Whether a stored answer can stand in for part of a new question is a
containment question in disguise. Adding a view literal to a query never
loses answers only if the view's body can be found inside the query's, and
Proposition 3.1 makes this exact: a rewriting of Q using V exists iff the
boolean projection of Q is contained in that of V, "If V is empty for a
given database, then so is Q." So recognizing reuse costs at least what
containment costs. Then a second search follows: once the view is added,
deciding which original literals it makes redundant is itself hard. The
paper shows the two searches are independent sources of hardness.

## Assumptions

- **Conjunctive queries and views** (select-project-join, Datalog rules
  without recursion), optionally with built-in comparisons (=, ≠, <, ≤).
  Unions of conjunctive queries are treated briefly (Theorem 3.9).
- **Set semantics.** Bag semantics, which the authors note restricts uses
  to one-to-one mappings (citing Chaudhuri et al. 1995), is outside.
- **Equivalent rewritings only.** A rewriting must give the same answer as
  the query on every database (Definition 2.1); a *complete* rewriting
  uses only views and built-ins (Definition 2.4). Contained or
  maximally-contained rewritings are not considered.
- **Cost is counted as literals.** Minimality means fewest literals, or
  fewest database-relation literals, ignoring built-ins (§2.1). The paper
  says the real cost of evaluation "depends on many factors", and it does
  not address choosing between rewritings by cost.
- **Views are given and materialized**; nothing is said about which to
  store, how many, or keeping them current.
- **Complexity is in the size of the query and view definitions.** The
  stored data does not enter any of the results.

## Key results

- **Containment mappings (§2.2).** Without built-in predicates, a
  containment mapping is necessary and sufficient for containment, "and is
  an NP-complete problem [CM77]"; this remains so when only the contained
  query has built-ins. When the containing query has built-ins, a mapping
  is only sufficient, and containment is Π2p-complete (van der Meyden
  1992).
- **Proposition 3.1.** For conjunctive Q and V with built-ins: there is a
  rewriting of Q using V iff π∅(Q) ⊆ π∅(V). The remark extends this to
  relational-calculus queries and views with conjunctive rewritings.
- **Proposition 3.2.** (1) If Q has built-ins and the views do not,
  deciding whether a rewriting of Q using V exists is NP-complete.
  (2) If both have built-ins, it is Π2p-complete.
- **Lemma 3.3.** Without built-ins: (1) the database-relation literals of a
  locally minimal rewriting are isomorphic to a subset of Q's literals;
  (2) any rewriting can be replaced by one that introduces no new
  variables; (3) with built-ins, the same holds if unions are allowed.
  Example 3.4 shows (2) fails for a single conjunctive rewriting when the
  view has a comparison.
- **Lemma 3.5 (the size bound).** Without built-ins, if Q's body has p
  literals, a locally minimal complete rewriting has at most p literals.
  Example 3.6: with functional dependencies the bound fails (a rewriting
  may need up to p + d literals, d the sum of the arities); with built-ins
  the rewriting may be exponential in the size of Q. The full paper, not
  read, is said to bound size in both cases.
- **Theorem 3.7.** For conjunctive Q and V without built-ins:
  (1) is there a rewriting with fewer than k literals (k below the
  number of Q's literals)? NP-complete; (2) the same counting only
  database-relation literals: NP-complete; (3) is there a complete
  rewriting? NP-complete; (4) with built-ins, problem 1 is in Σ3p.
  Membership in NP comes from the size bound: guess a rewriting no longer
  than the query and the containment mappings both ways.
- **Corollary 3.8.** Finding a globally minimal rewriting without built-ins
  is coNP-complete as the paper states it; with built-ins it is in Π3p.
- **Theorem 3.9.** For unions of conjunctive queries and views without
  built-ins, existence of a complete rewriting is NP-complete.
- **Theorem 3.10 (two independent sources).** "The complete rewriting
  problem is NP-complete for conjunctive queries and views without
  built-in predicates even when both the query and the views are defined
  by rules that do not contain repeated predicates in their body." Then
  each view maps into the query in at most one way and finding the
  mappings is easy, so the hardness comes from combining them, by
  reduction from exact cover by 3-sets. The paper's names for the two
  sources: "The first source is the exponential number of possible
  containment mappings from the views to the query"; the second is
  deciding which query literals are redundant given the mappings.
- **Theorem 4.4.** For one view and one mapping h, the set N of needed
  literals (Definition 4.2) is computable in polynomial time and q(X) :- N,
  v(Y) is always a rewriting. If h maps no two view literals to the same
  query literal and the query is minimal, the complement of N is the
  unique maximal set of redundant literals. Otherwise the algorithm may
  remove fewer than possible, never wrongly. With built-ins in the view,
  the needed sets are unioned over the mappings to each disjunct.

A small inconsistency in the text: the size bound is called Lemma 3.5 where
stated and "Proposition 3.5" two paragraphs later.

## Bearing on the record

**On [CLAIM-303](../claims.d/CLAIM-303.md), [CLAIM-308](../claims.d/CLAIM-308.md) and the owner's point that reuse requires
recognition.** If a filed argument is a stored answer and a new question is
a query, this paper prices the step that [CLAIM-303](../claims.d/CLAIM-303.md)'s c_a leaves implicit:
recognizing that a stored answer covers the new question, wholly or in
part. The exact statements, with their conditions:

- **The decision problems.** (a) Containment: is every answer of Q1 an
  answer of Q2? (b) Usability: is there an equivalent rewriting of Q that
  uses view V at all (Proposition 3.1)? (c) Minimal rewriting: is there an
  equivalent rewriting with fewer than k literals, or fewer than k
  database literals (Theorem 3.7 (1), (2))? (d) Complete rewriting: can Q
  be answered from the views alone (Theorem 3.7 (3), Theorems 3.9, 3.10)?
- **Their complexity.** For conjunctive queries and views without
  comparisons, (a) to (d) are NP-complete; minimal-rewriting verification
  as the paper states it is coNP-complete. With comparisons in the
  containing query or in both query and views, (a) and (b) are
  Π2p-complete and (c) is in Σ3p. Membership in NP rests on the size
  bound: a minimal rewriting is no longer than the query. That bound is for
  equivalent rewritings without comparisons or dependencies; it fails with
  functional dependencies (and, by Halevy's account, with access-pattern
  limits), and for maximally-contained rewritings, which this paper does
  not treat.
- **What this says about c_a.** Reuse is not a lookup. Even for the
  simplest query language with a stored definition attached to every
  stored answer, deciding that the answer covers the question, and how to
  combine several stored answers to cover it, is NP-complete in the size of
  the descriptions, with two independent sources of search. So c_a has a
  recognition term, it varies with the question and with the set of stored
  items (the number of candidate mappings grows with the views), and it is
  not bounded by a constant in the worst case. The rent-or-buy guarantee
  behind [CLAIM-308](../claims.d/CLAIM-308.md) ([THEORY-348](../theory.d/THEORY-348.md)) assumes a fixed, known per-use cost.
  [CLAIM-308](../claims.d/CLAIM-308.md) already excludes drifting costs; this result gives a specific
  reason the per-use cost drifts as more is filed. It does not overturn the
  2-competitive bound where c_a can be treated as fixed.
- **What it does not say.**
  - It does not say recognition is expensive in practice. The hardness is
    worst case and in the size of the query and view definitions, which
    are short; the stored data does not enter. The authors expect their
    polynomial redundancy algorithm to cover "many practical cases".
  - It does not cover arguments in prose. Containment here is decidable
    only because conjunctive queries are a small positive language; a
    filed argument has no conjunctive definition, and deciding that it
    answers a new question is not shown to be in NP or to be decidable.
  - It presupposes that each stored answer carries a definition of what it
    answers. Recognition cost is a function of those definitions. A filed
    item without a statement of the question it answers gives this
    analysis nothing to work on: recognition is then undefined, not merely
    hard. For the record, the title of a CLAIM or the QUESTION it answers
    plays the role of the view definition.
  - It treats only equivalent rewritings. Partial reuse, using a stored
    answer for part of a question and reconstructing the rest, is what
    Proposition 3.1's rewriting of Q using V allows (database literals may
    remain), but a stored answer that covers only some cases of the
    question (a contained rewriting) is outside it.
  - It says nothing about whether reuse is worth it once recognized. The
    authors leave choosing between rewritings by cost "not addressed".

**On [QUESTION-114](../questions.d/QUESTION-114.md).** The record's readings so far price storing answers and
reading them back, with the step of deciding that a stored answer serves a query
assumed free (Harinarayan et al., [LIT-1094](../literature.d/LIT-1094.md), takes a query to be answerable
from a view when the view is an ancestor in the cube lattice). This paper
is where that step has a price: NP-complete for conjunctive queries in
general, polynomial when the lattice structure or a unique mapping makes
it so. In the data-cube setting the containment is given by the lattice,
which is why it could be treated as free there.

## Limitations

- Extended abstract: proofs of several results (Theorem 3.7 (2)–(4),
  Theorem 3.9, the bounds with dependencies and built-ins) are sketched or
  deferred to a full paper.
- Equivalent rewritings under set semantics only; no maximally-contained
  rewritings, no bag semantics, no aggregation.
- Minimality is in literals, not in evaluation cost.
- Worst-case complexity in the size of the query and views; no measurement
  of the typical cost of finding rewritings.

## Connections

Built on Chandra and Merlin 1977 ([LIT-tmpkq8zv](../literature.d/LIT-tmpkq8zv.md)) for containment mappings,
their NP-completeness and the uniqueness of the core. Halevy 2001
([LIT-tmpu418n](../literature.d/LIT-tmpu418n.md)) surveys the field this paper opened and reports its size
bound and its two sources of hardness, with the second phrased as the
number of ways to combine the mappings of different views. Rajaraman,
Sagiv and Ullman 1995 extend it to views with binding patterns.
