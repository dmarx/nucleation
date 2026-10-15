---
status: Active
status_note: >-
  read in full 2026-10-15 (NOTE for L39) from the author's own copy, a scan linked
  from Keith Clark's Imperial College page for the paper (www.doc.ic.ac.uk/~klc/NegAsFailure.pdf,
  via www.doc.ic.ac.uk/~klc/neg.html); the scan's printed pages run 113–141, not
  the 293–322 Crossref gives for the Plenum chapter, and which printing it is was
  not identified. Unpaywall, OpenAlex and Semantic Scholar report the chapter closed.
  Worth reading as the source of negation as failure and of the completed data base:
  a Horn clause evaluator that takes ~P as a lemma when every branch of the evaluation
  tree for P terminates in failure is sound for the clauses read as if-and-only-if
  definitions plus axioms that distinct names denote distinct objects (Theorem 2);
  a non-terminating search licenses nothing, the evaluator is in general incomplete,
  and it is complete for allowed queries on hierarchical data bases (Theorem 4).
  Clark identifies the assumption with Reiter's closed world assumption in one paragraph
  and makes no formal comparison. For [CLAIM-tmp3ejtf](../claims.d/CLAIM-tmp3ejtf.md) it confirms the record's gloss
  ("a finitely failed attempt ... sound with respect to the completion"), and it
  shows that a search cut off by a deadline is not a failure in Clark's sense: the
  rule needs the search exhausted, so the medic's rule in [CASE-085](../cases.d/CASE-085.md) is a stronger
  default than negation as failure, not negation as failure on a time bound; and
  since the EMT's own knowledge implied the item was stocked, negation as failure
  would have refused the conclusion.
title: Negation as Failure
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Filed, not read. Citation checked against Crossref on 2026-10-15: a chapter
    in Gallaire and Minker (eds.), Logic and Data Bases (Plenum, 1978); Crossref
    gives the year only, so `published:` is the first of January. Not held in the
    Anthology of the SOTA: a grep of its record/ (clone of 2026-10-15, commit d1573d2)
    for the author and the title found nothing. Read the same day (NOTE-tmpa2jg6).
tags:
- logic
date: '2026-10-15'
published: '1978-01-01'
doi: 10.1007/978-1-4684-3384-5_11
first_author: Clark
keywords: []
implementations: []
summary: >-
  Clark gives a query evaluator for a data base of clauses (a Horn clause prover
  in which a ground negated literal ~P is taken as a lemma when the recursive evaluation
  of P fails on every branch) and proves it sound with respect to the completed
  data base: the clauses read as the if-halves of if-and-only-if definitions, plus
  equality axioms saying distinct names denote distinct objects. Theorem 2: if for
  some selection rule every branch of the evaluation tree of Q terminates with failure,
  then not-(exists x)Q is a theorem of the completed data base. A branch that does
  not terminate licenses nothing; the rule requires the search to be exhausted,
  which the paper calls "the exhaustive but unsuccessful search for a proof of P".
  The evaluator is in general incomplete (non-ground negation, a single evaluation
  tree, no case analysis); it is complete for allowed queries on hierarchical data
  bases (Theorem 4).
---

# LIT-tmpix3rp: Negation as Failure

Clark, K. L. (1978). Negation as failure. In H. Gallaire and J. Minker (eds.), *Logic and Data Bases*, pp. 293–322. New York: Plenum. DOI 10.1007/978-1-4684-3384-5_11

## Key takeaways

Read in full ([NOTE-tmpa2jg6](../notes.d/NOTE-tmpa2jg6.md)), from the author's posted scan. Clark gives a query evaluator for a data base of clauses (a Horn clause prover in which a ground negated literal ~P is taken as a lemma when the recursive evaluation of P fails on every branch) and proves it sound with respect to the completed data base: the clauses read as the if-halves of if-and-only-if definitions, plus equality axioms saying distinct names denote distinct objects. Theorem 2: if for some selection rule every branch of the evaluation tree of Q terminates with failure, then not-(exists x)Q is a theorem of the completed data base. A branch that does not terminate licenses nothing; the rule requires the search to be exhausted, which the paper calls "the exhaustive but unsuccessful search for a proof of P". The evaluator is in general incomplete (non-ground negation, a single evaluation tree, no case analysis); it is complete for allowed queries on hierarchical data bases (Theorem 4).

## Why this is here

[CLAIM-tmp3ejtf](../claims.d/CLAIM-tmp3ejtf.md): the medic's "If I can't find it, it isn't there" ([CASE-085](../cases.d/CASE-085.md)) acts
on a failed search as if it showed absence. This is the inference, and
its soundness condition is the one [CLAIM-tmp3ejtf](../claims.d/CLAIM-tmp3ejtf.md) needs.
