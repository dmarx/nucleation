---
number: 389
status: Active
formerly:
- THEORY-tmpxw8fg
title: "For conjunctive queries and views without comparison predicates, a stored view can be used in an equivalent rewriting of a query exactly when the view's body maps homomorphically into the query's, a minimal rewriting needs no more literals than the query, and deciding whether a rewriting shorter than the query or one using only the views exists is NP-complete in the size of the query and view definitions; with comparisons in both, deciding whether any rewriting uses the views is Π2p-complete"
version: 1
tags:
- databases
- logic
date: '2026-10-15'
source:
- LIT-1100
- LIT-1111
answers:
- QUESTION-114
summary: >-
  Levy, Mendelzon, Sagiv and Srivastava (1995), [LIT-1100](../literature.d/LIT-1100.md), read in
  [NOTE-909](../notes.d/NOTE-909.md). Every use of a view in an equivalent rewriting comes from a
  containment mapping from the view into the query (Proposition 3.1);
  without comparisons a locally minimal complete rewriting has at most as
  many literals as the query (Lemma 3.5), which puts the problems in NP,
  and they are NP-complete (Theorems 3.7, 3.9, 3.10), with two independent
  sources of hardness. The results are worst case, in the size of the
  definitions rather than the stored data, for equivalent rewritings under
  set semantics only; they do not say recognizing reuse is costly in
  practice, and they do not cover contained (partial) rewritings.
supports:
- CLAIM-303
- CLAIM-314
---
<!-- inactive-ok-file: LIT-1111 LIT-1116 CLAIM-303 CLAIM-308 QUESTION-114 — read the same day, Proposed or open; named as works and claims this account bears on, not leaned on -->

# THEORY-389: For conjunctive queries and views without comparison predicates, a stored view can be used in an equivalent rewriting of a query exactly when the view's body maps homomorphically into the query's, a minimal rewriting needs no more literals than the query, and deciding whether a rewriting shorter than the query or one using only the views exists is NP-complete in the size of the query and view definitions; with comparisons in both, deciding whether any rewriting uses the views is Π2p-complete

## Source

Levy, Mendelzon, Sagiv and Srivastava (1995), [LIT-1100](../literature.d/LIT-1100.md), "Answering
queries using views (extended abstract)", PODS 1995, pp. 95–104, read in
full in [NOTE-909](../notes.d/NOTE-909.md) from the authors' camera-ready on Mendelzon's Toronto
page. It rests on Chandra and Merlin 1977 ([LIT-1111](../literature.d/LIT-1111.md), [THEORY-371](THEORY-371.md)).

## What was actually shown

**The problems.** A rewriting of Q using views V is a conjunctive query
equivalent to Q on every database that uses at least one view literal; a
complete rewriting uses only view literals and built-ins. The questions:
does some rewriting use V; is there one with fewer than k literals, or
fewer than k database literals; is there a complete one.

**Usability is containment (Proposition 3.1).** There is a rewriting of Q
using V iff the boolean projection of Q is contained in that of V, "If V is
empty for a given database, then so is Q", that is, iff V's body maps into
Q's body. Every use of a view is found among these mappings.

**The size bound (Lemma 3.5, Lemma 3.3).** Without comparisons, a locally
minimal complete rewriting has at most as many literals as Q, uses a subset
of Q's database literals and needs no new variables. The bound fails with
functional dependencies, and with comparisons a rewriting may need unions
or be exponentially long.

**Complexity.** Without comparisons, the shorter-rewriting problems and the
complete-rewriting problem are NP-complete (Theorem 3.7 (1)–(3)), also for
unions of conjunctive queries (Theorem 3.9). With comparisons in Q only,
existence of a rewriting using V is NP-complete; with comparisons in both,
Π2p-complete (Proposition 3.2); the shorter-rewriting problem is then in
Σ3p. Theorem 3.10: complete rewriting stays NP-complete when no rule
repeats a predicate, so each view maps into the query in at most one way;
the hardness then comes from combining views (exact cover by 3-sets). The
paper calls these "two independent sources" of complexity: "The first
source is the exponential number of possible containment mappings from the
views to the query"; the second is deciding which query literals become
redundant.

**A tractable step (Theorem 4.4).** Given one mapping, the needed literals
are computable in polynomial time; if the mapping is one-to-one on view
literals and Q is minimal, their complement is the unique maximal set of
redundant literals.

**What could have come out otherwise.** A usable view with no containment
mapping into the query would refute Proposition 3.1; a minimal complete
rewriting longer than the query, without comparisons or dependencies,
would refute Lemma 3.5.

## What this does not say

- **That recognizing reuse is expensive in practice.** Hardness is worst
  case, in the size of the query and view definitions; the stored data
  never enters. The authors expect the polynomial step to handle "many
  practical cases".
- **Anything about contained or partial answers.** Only equivalent
  rewritings are studied. Whether stored answers cover some cases of a
  question (maximally-contained rewritings) is [LIT-1116](../literature.d/LIT-1116.md)'s subject
  ([THEORY-374](THEORY-374.md)), with different complexity.
- **Which rewriting to use.** Minimality is counted in literals; choosing
  between rewritings by evaluation cost is, in the paper's words, "not
  addressed".
- **Anything about stored items without definitions or in prose.** Every
  result assumes each view carries a conjunctive definition over the
  query's schema. For a filed argument, there is no such definition, and
  coverage is not shown decidable.

## Connections

- [QUESTION-114](../questions.d/QUESTION-114.md): the stored-answer readings (THEORY on Harinarayan et al.,
  [LIT-1094](../literature.d/LIT-1094.md)) take answerability from a view as given by the lattice. This
  prices that step in general: NP-complete for conjunctive queries, so the
  joint cost model the question asks for has a recognition term besides
  storage, upkeep and saving.
- [CLAIM-303](../claims.d/CLAIM-303.md)'s c_a has a recognition term that varies with the question and
  with the set of filed items; [CLAIM-308](../claims.d/CLAIM-308.md) and [THEORY-348](THEORY-348.md) assume a fixed
  per-use price. This narrows where the 2-competitive rule applies; it
  does not refute it.
- [THEORY-371](THEORY-371.md) is the containment theory underneath; [THEORY-374](THEORY-374.md) places this
  result among contained rewritings and certain answers.
