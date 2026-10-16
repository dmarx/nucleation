---
number: 907
status: Read
formerly:
- NOTE-tmp5wypo
paper: LIT-1111
title: Chandra & Merlin — Optimal implementation of conjunctive queries in relational
  data bases
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Read in full from a scan of the published proceedings paper (Proc. STOC 1977,
    pp. 77–90, 14 pp.; the printed page numbers 77–90 are on the scan), hosted in
    the directory of UBC's course CPSC 504 (www.cs.ubc.ca/~laks/cpsc504/chandra-merlin-1977.pdf,
    PDF created 7 Sept 2000, fetched 2026-10-15). It is a course-hosted copy of
    the published article, not an author's preprint; the course's index page now
    returns 404, so the course context was not seen directly. ACM's open-access
    PDF (Unpaywall and OpenAlex: bronze, dl.acm.org/doi/pdf/10.1145/800105.803397)
    returned 403 to this environment. The PDF carries an OCR text layer; text was
    extracted with pdftotext. The OCR garbles symbols (≡, →, ∃, subscripts), so
    the statements of Theorems 6, 7, 8, 10, 11, 12 and 16 and Lemmas 13, 14 and
    15 were read from page images (pp. 81–83 and 85 rendered at 110 dpi). Read:
    §§1–7 (example, conjunctive queries, generalized join, complexity, query minimization,
    model and optimization, conclusions), the appendix (proofs of Lemmas 1 and 2),
    the reference list and Fig. 1. Nothing skipped. Every quotation below was checked
    by script against the extracted text, whitespace normalised; two ("Thus boolean
    first-order queries…" and "This algorithm runs…"), where the OCR layer drops
    or scrambles words, were checked against the page images of pp. 81 and 85 instead.
date: '2026-10-15'
summary: >-
  Defines conjunctive queries (existentially quantified conjunctions of atoms, no
  equality, constants naming distinct elements) and proves that two are equivalent
  exactly when there are homomorphisms each way between their natural models (Lemma
  13). Every conjunctive query has a minimal equivalent query, unique up to isomorphism,
  reached by folding (Theorem 12), and that minimal query yields an evaluation program
  within a constant factor of optimal in the paper's cost model (Theorem 16). The
  hardness results are that evaluating a boolean conjunctive query on a database
  is NP-complete when the query is part of the input (Theorem 7), and that deciding
  whether one query is a folding of another is NP-complete (Theorem 11). The paper
  does not state a containment theorem or the NP-completeness of containment or
  equivalence as such; both are standard corollaries of Lemma 13's proof and Theorem
  11's construction, and later papers cite them to it.
---

# NOTE-907: Chandra & Merlin — Optimal implementation of conjunctive queries in relational data bases

## Contribution

The paper names the class of conjunctive queries and makes three moves. It
shows that answering them is hard when the query is part of the input
(NP-complete, against PSPACE-complete for first-order queries). It shows
that equivalence between them has a finite, syntactic test: homomorphisms
between the queries themselves, read as small databases. And it uses that
test to get a canonical minimal form, which is the basis of an evaluation
program within a constant of optimal. The abstract: "It is shown that while
answering conjunctive queries is NP complete (general queries are PSPACE
complete), one can find an implementation that is within a constant of
optimal. The main lemma used to show this is that each conjunctive query
has a unique minimal equivalent query (much like minimal finite automata)."

## Key insight

A conjunctive query can be read as a database: its variables and constants
are the elements, its atoms the tuples (the "natural model" M_Q, with extra
unary relations marking the output variables and constants). Whether one
query's answers always include another's is then a question about two
finite structures, answered by looking for a structure-preserving map
between them. Semantic comparison over all possible databases reduces to a
search over maps between two small objects. That search is the cost: it is
the same kind of search as evaluating a query on a database, which is
NP-complete.

## Assumptions

- **Conjunctive queries only:** (x1,…,xk).∃x(k+1)…xm. A1 ∧ … ∧ Ar with
  each Ai an atom R(y1,…,yp) over variables and constants. No disjunction,
  negation, equality or comparison predicates. Unions of conjunctive
  queries are mentioned as handled by answering each disjunct separately;
  nothing is proved about them.
- **Constants stand for themselves and distinct constants are distinct
  elements**, a stated departure from ordinary logic. The appendix shows
  that with equality allowed, equivalence in this formalism would not even
  be transitive.
- **Set semantics.** Results are sets of tuples.
- **Atomic formulas are not repeated** within a query (assumed without loss
  of generality in §5).
- **The cost model** (§6.1) is a straight-line program over relations whose
  only charged step is the generalized join, costed as input and output
  sizes plus naive boolean matrix multiplication; a program is
  "near-optimal" if its running time is within a constant factor of every
  equivalent program on every database, i.e. its polynomial in the domain
  size n has minimal degree.

## Key results

- **Theorem 6 / 6'.** For first-order boolean queries, {(Q,B) | Q true in B}
  is logspace complete in PSPACE, and stays so for one fixed two-element
  database B0. Query complexity, not data complexity, drives it.
- **Theorem 7.** For conjunctive boolean queries, {(B,Q) | Q true in B} is
  logspace complete in NP (membership: guess an assignment; hardness: from
  clique). "Thus boolean first-order queries are PSPACE-complete whereas
  conjunctive queries are NP-complete. Note that the data base itself is
  part of the input." The authors draw the practical conclusion: "It pays,
  in such cases, to optimize the query as much as possible, even if such
  optimization takes a long time with respect to the size of the query (but
  independent of the data base)."
- **Theorem 8.** Isomorphism of conjunctive queries is logspace equivalent
  to graph isomorphism ("in a slightly different form" also shown by
  Kozen 1976).
- **Folding.** Q' is a folding of Q if M_Q' = h(M_Q) for an endomorphism h
  of M_Q that fixes a set V containing the output variables and constants
  and maps everything into V.
- **Theorem 10.** If Q2 is a folding of Q1 then Q1 ≡ Q2.
- **Theorem 11.** {(Q1,Q2) | Q2 is a folding of Q1} is NP-complete, also for
  boolean conjunctive queries; hardness by reduction from graph
  c-colouring, using one binary relation: Q1 is the graph's edges plus a
  c-clique on fresh variables, Q2 the c-clique alone.
- **Lemma 13 (the homomorphism theorem).** For conjunctive queries Q1, Q2:
  Q1 ≡ Q2 iff there are homomorphisms h1: M_Q1 → M_Q2 and
  h2: M_Q2 → M_Q1 (homomorphisms of the natural models, so they fix
  constants and send the i-th output variable to the i-th). The proof's
  "if" half shows one direction at a time: from h2: M_Q2 → M_Q1 it derives
  Res(Q1,B) ⊆ Res(Q2,B) for every compatible database B. That half is the
  containment criterion later papers call the containment mapping. The
  paper states only the equivalence form.
- **Theorem 12.** For every conjunctive query Q there is a folding Q0 such
  that every Q' ≡ Q has a folding isomorphic to Q0: a minimal equivalent
  query, unique up to isomorphism (the core), obtained by deleting atoms.
  Theorem 9: foldings are Church–Rosser up to isomorphism. §5 adds, without
  a separate theorem, that "minimizing a conjunctive query is NP-hard".
- **Theorem 16.** The algorithm that finds the minimal query Q1 ≡ Q and
  then, among all expressions equivalent to Q1, chooses the one whose
  running time is a polynomial of minimal degree, computes a near-optimal
  program. "This
  algorithm runs in time exponential in the length of the input query (but
  independent of the data base)." Lemma 15 is why minimizing first is safe:
  any expression for a query yields one for its folding that is no slower
  on any database.

What the paper does not contain, though it is often cited for it: a
theorem that containment of conjunctive queries is NP-complete. Membership
in NP follows from Lemma 13 (guess the homomorphism); NP-hardness of
equivalence, hence of containment, follows from the Theorem 11
construction, since there Q2 always maps into Q1 and Q1 maps into Q2 iff
the graph is c-colourable. Neither corollary is written down.

## Bearing on the record

**On [CLAIM-303](../claims.d/CLAIM-303.md) and its objection [CLAIM-308](../claims.d/CLAIM-308.md): the base cost of recognizing that
a stored answer covers a new question.**

- In [CLAIM-303](../claims.d/CLAIM-303.md)'s accounting, reuse costs c_a per use for access and
  verification. If filed items are stored answers and new questions are
  queries, then the judgement that a stored answer covers a question is containment,
  and this paper supplies its decision procedure: look for a homomorphism
  from one query to the other. The search is NP-complete in the worst case
  (Theorem 7's problem is the same search, with one query as the
  database). So recognition is a search problem with a known worst case,
  and c_a is not a constant once the questions vary.
- The hardness is in the size of the **queries**, not of the stored data.
  Theorem 7's hardness is for the query as input. Recognition compares two
  descriptions, a question and a stored answer's statement of what it
  answers, and its cost grows with their size and structure, not with the
  bulk of what was stored. The authors' own conclusion is that a
  query-size-exponential step is worth paying once to save on every
  evaluation. That is [CLAIM-303](../claims.d/CLAIM-303.md)'s trade applied to recognition: pay to put
  a question in canonical (minimal) form once.
- **What it does not say.** It says nothing about natural-language
  arguments. Containment is decidable here only because conjunctive queries
  are a small, positive language; Theorem 6 shows the first-order version is
  already PSPACE-complete to evaluate, and containment for full first-order
  queries is undecidable (not in this paper). The NP-completeness is a worst
  case over adversarial query shapes; it does not price the typical
  recognition. And it gives no algorithm for finding which of many stored
  answers cover a question: that is [LIT-1100](../literature.d/LIT-1100.md)'s problem.
- **For [CLAIM-308](../claims.d/CLAIM-308.md).** The rent-or-buy guarantee ([THEORY-348](../theory.d/THEORY-348.md)) assumes a fixed,
  known per-use cost. Recognition cost depends on the pair of descriptions
  compared, so it varies by use. [CLAIM-308](../claims.d/CLAIM-308.md) already sets drifting costs
  outside its claim; this paper is a concrete reason the costs drift, not a
  refutation.

**On [QUESTION-114](../questions.d/QUESTION-114.md).** Theorem 16 is an amortization of a different kind: an
exponential, data-independent cost paid once per query (minimization)
against a saving on every evaluation. It is a precedent for paying for search once, applied to the question rather than to the stored collection, with
the condition the authors state, that queries are much smaller than
databases.

## Limitations

- Conjunctive queries only, without equality, comparisons, negation or
  union; distinct constants denote distinct elements.
- The optimality result is in a stylized cost model (polynomial degree in
  domain size, naive matrix multiplication for joins), not a cost model of
  any real system.
- Several proofs are omitted or sketched (Lemmas 3, 5, 14; the labelled to
  unlabelled graph step in Theorem 8).
- The containment and equivalence complexity results that later work
  attributes to this paper are corollaries, not stated theorems.

## Connections

Levy, Mendelzon, Sagiv and Srivastava 1995 ([LIT-1100](../literature.d/LIT-1100.md)) build on Lemma 13
and Theorem 12, citing them for containment mappings, their NP-completeness
and the uniqueness of the core. Halevy 2001 ([LIT-1116](../literature.d/LIT-1116.md)) cites this paper
with Sagiv and Yannakakis 1981 for containment of select-project-join
queries and unions of them.
