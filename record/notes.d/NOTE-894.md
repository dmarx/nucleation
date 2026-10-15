---
number: 894
status: Read
formerly:
- NOTE-tmpa2jg6
paper: LIT-1087
title: Clark — Negation as failure
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Read in full on 2026-10-15 from the author's own copy, linked from Keith Clark's
    Imperial College page for the paper (www.doc.ic.ac.uk/~klc/neg.html, which says
    "First Published in: Logic and Data Bases, (eds Gallaire and Minker), 1978.")
    at www.doc.ic.ac.uk/~klc/NegAsFailure.pdf: a 29-page image-only scan of the
    typeset chapter (PDF dated 2004-06-09). Unpaywall, OpenAlex and Semantic Scholar
    all report the chapter closed. The scan's printed page numbers run 113–141,
    while Crossref gives 293–322 for the Plenum chapter; which printing was scanned
    is not identified, and wording could differ from the Plenum pages, which were
    not seen. Text was obtained by rendering each page at 300 dpi and running tesseract
    OCR; the OCR mangles logical symbols, so the proof rule, the completion schemas,
    Table 2 and Theorems 1–4 were read from the page images. Read: abstract, introduction,
    Query Evaluation for a Data Base of Clauses, Data Base Completion, Correctness
    of Query Evaluation (Lemma, Theorems 1–3 and the proof sketches), Completeness
    of Query Evaluation (Theorem 4), Final Remarks and the reference list. Nothing
    skipped. Reiter (1978, LIT-1088), which the paper names as the source of
    the closed world assumption, was not read here, so the relation between the
    two is stated as Clark states it. Every quotation of Clark below was checked
    by script against the OCR text, whitespace-normalised. Six that the OCR garbled
    (the proof rule, the two Case 2 sentences and Theorem 2, which contain logical
    symbols, and two sentences on p. 114 where the OCR ran words together) were
    checked against the page images instead; the "First Published in" line was checked
    against neg.html. Quotations of the record were checked against the record files.
date: '2026-10-15'
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

# NOTE-894: Clark — Negation as failure

## Contribution

PLANNER and PROLOG already treated negation operationally: "To show that P is false we do an exhaustive search for a proof of P. If every possible proof fails, ~ P is 'inferred'." Clark asks whether this "fail to prove" can be reconciled with negation's truth-functional meaning, "can we interpret a failure proof of ~ P as a valid first order inference that P is false." He answers yes, relative to a stated theory: a failure proof from the data base of clauses B is a first-order proof from the completed data base C(B). So negation as failure becomes "just a derived inference rule for deductions from C(B)".

## Key insight

A failed exhaustive search has the same structure as a first-order proof by cases from the only-if halves of the definitions: "The alternatives of the failed proof space become explicit disjunctions in the first order deduction, match failures of the former become false equalities of the latter." What makes the failure a proof is not that the search stopped but that it ran out of alternatives, each closed by a mismatch. The extra axioms needed to make this a deduction (the completion laws and the inequality schemas) are exactly the assumption that the data base says everything true about its relations and that its names are distinct.

## Assumptions

- **A data base of clauses**, each with one distinguished positive literal (the relation it is about); other positive literals appear as negated preconditions. Ground unit clauses are the extensional part, the rest are general rules.
- **Queries are conjunctions of literals**; an answer is a substitution making the query a logical consequence of the completed data base.
- **Evaluation** is linear resolution with a literal selection rule; each path can "SUCCEED, FAIL or not terminate". The selection rule "is constrained so that a negative literal is only selected if it contains no variables."
- **Negation as failure (Case 2).** For a ground negative literal ~P the evaluator recursively evaluates P: "If the evaluation of ←P SUCCEEDS, FAIL." "If the evaluation of ←P FAILS for every path of its nondeterministic evaluation, assume ~ P as a lemma." Failure proofs may nest.
- **The completed data base C(B).** For each relation R with k clauses, the general forms R(x1..xn) ← E1, ..., Ek give the definition ∀x [R(x) ↔ E1 ∨ ... ∨ Ek]; "The if-half of this definition is just the k general form clauses (7) grouped as a single implication. The only-if half is the completion law for R." A relation with no clauses is defined as ↔ false. Added to these is the identity theory: distinct constants are unequal (8), distinct functors are distinct constructors (9), constructed terms are equal only if their components are (10), constructors make new objects (11), no term equals a term containing it (12), and the usual equality axioms with a substitution schema. "The identity theory, together with the set of relation definitions implicitly given by a logic data base, constitute the completed data base."
- **Consistency** of the completed data base is assumed for Theorem 3 and for the completeness argument.

## Key results

- **The proof rule.** "⊢ ~⊢ P infer ⊢ ~P", "where the proof that P is not provable is always the exhaustive but unsuccessful search for a proof of P. Let us call it the negation as failure inference rule."
- **The closed world assumption.** "Note that to assume that a relation instance is false if it is not implied, is to assume that the data base gives complete information about the true instances of its relations. This is the closed world assumption referred to by Reiter [1978] and Nicolas and Gallaire [1978]. More precisely, it is the assumption that a relation instance is true only if it is given explicitly or else is implied by one of the general rules for the relation." With two Maths-course facts, concluding ~Maths-course(C) for another C "is to assume that C101 and C301 are the only Maths-courses, and that C is not an alternative name for either course" — the completion law plus inequality schemas. That is all the paper says about Reiter; it makes no formal comparison.
- **Lemma.** Using the identity theory, unification is emulated by inference about equalities: unifiable argument tuples have equalities equivalent to the m.g.u. bindings; non-unifiable ones have equalities provably equivalent to false.
- **Theorem 1.** If Q1..Qj are all the queries derivable from Q by resolving on a selected positive literal, with general forms G1..Gj, then Q ↔ G1 ∨ ... ∨ Gj is a theorem of the completed data base; if j = 0, Q ↔ false is.
- **Theorem 2 (soundness of negation as failure).** "If for some literal selection rule every branch of the evaluation tree of a query ←Q terminates with failure, then ~(∃x1,...,xk)Q where x1,...,xk are the free variables of Q, is a theorem of the completed data base." Proved by induction on the number of nested failure proofs and on the structure of the failure tree. The proof is constructive: a failure tree can be lifted into a first-order proof (worked for ~Non-maths-major(D.Smith)).
- **Finiteness.** Remark (6): if every branch terminates with SUCCESS or FAIL, then "By Konig's Lemma ... the evaluation tree contains a finite number of queries." So a failure tree in Theorem 2 is a finite tree — later literature's "finite failure". The paper's own words are "terminates with failure" and "every possible proof fails". A non-terminating path ("an infinite sequence of queries") yields no conclusion: in Figure 7a the PROLOG rule gives "an evaluation tree with a single infinite branch" for P(a), so ~P(a) cannot be inferred, though another selection rule gives "a finite failure tree".
- **Theorem 3 (answers are exhaustive).** If, for some selection rule, every branch ends in success or failure, with answers θ1..θj, then ∀x [Q ↔ θ1 ∨ ... ∨ θj] (general forms) is a theorem of the completed data base, assuming it is consistent. In the Final Remarks: "an exhaustive search for solutions to a query, if it returns a finite set of solutions, is a proof that these are exactly the set of solutions."
- **Incompleteness.** "Will we still be able to infer every answer to the query implied by the completed data base? With certain restrictions on the data base and its queries, yes. In general, no." Three gaps: negation applies only to ground literals; the search grows only one evaluation tree, so "to grow just one evaluation tree is to risk 'missing' a failure proof"; and no case analysis — "Like intuistionist logic, the query evaluator does not countenance the law of the excluded middle" (example (13): R(a,b) follows from the completed data base but no evaluation of ←R(a,b) terminates, because P(a) can be neither proved nor failure-proved).
- **Completeness conditions.** For "allowed" queries (every variable of a negated literal ranged by an unnegated one) and a selection rule giving finite evaluation trees, query evaluation is complete given consistency ("and I think that the finiteness of every evaluation tree guarantees this, although I have not checked it out"). A sufficient condition is "the condition of computable finite extensions". **Theorem 4:** "For a data base satisfying the hierarchical constraint the evaluation process for allowed queries is complete." The hierarchical constraint rules out recursive definitions, "unfortunately, a very strong constraint."
- **Relation to Kramosil.** Clark's rule is "relatively weak rule, for the unprovability condition is so strong", and it extends a Horn clause prover that is not complete for first-order logic, which is why it can add conclusions.

## Bearing on the record

**On [CLAIM-306](../claims.d/CLAIM-306.md): the record's gloss of Clark holds; the analogy it draws from him does not.**

- **The gloss.** The LIT summary says negation as failure is "inferring not-p from a finitely failed attempt to prove p, sound with respect to the completion of the program". That is accurate, with three precisions. The completion is the if-halves read as if-and-only-if definitions plus an identity theory (distinct names denote distinct objects, constructors are free); without the equality axioms the result fails. "Finitely failed" is later terminology; Clark's condition is that for some selection rule every branch of the evaluation tree terminates with failure, which by König's lemma is a finite tree. And "sound" means the conclusion is a theorem of the completed data base, not that it is true of the world: it is true of the world only if the completion is.
- **Two completeness assumptions, which the claim runs together.** The claim says both CWA and NAF are sound "only relative to a completeness assumption: that whatever is true would have been found". In Clark there are two different things. (a) The data base is complete about its relations — the closed world assumption, the only-if halves. That is what makes NAF's conclusions true. (b) The search has been completed — every alternative explored and closed. That is what makes the inference a proof at all. Clark's rule demands (b) outright as its premise; it is not an assumption about the search but a precondition that the search actually finished. "Whatever is true would have been found" mixes (a) with a search-completeness (b′: the procedure would find a proof if there is one), which Clark shows is not guaranteed and is the subject of his incompleteness section.
- **A deadline-cut search is not a finite failure.** A search stopped at τ has unexplored branches. In Clark's terms it is neither a failure tree nor a success; it is like the evaluation that has not terminated, from which nothing follows. Theorem 2 gives it no licence. So "If I can't find it, it isn't there" under a deadline is not negation as failure. It is a stronger default: it takes the closed world assumption and also treats the unsearched remainder as if it had failed. That supports the claim's main point (absence is not shown under a deadline) and contradicts its label ("is negation as failure ... taken on a time bound"): NAF has no time-bound form; a time bound removes the condition that makes NAF sound.
- **[CASE-085](../cases.d/CASE-085.md) is not even a closed world.** Clark's CWA says what is not implied by the data base is false. The EMT's own data base implied presence ("the unit was stocked and the EMT knew it"). With that fact in the clauses, a query for the item would succeed, and negation as failure would refuse ~present. So the medic's rule overrides the agent's own information; it is a decision to stop, as the claim itself says in its last paragraph, not a closed-world inference. The owner's "may as well not be there" ([CASE-094](../cases.d/CASE-094.md)) is closer: a statement of practical equivalence, not of absence.
- **What does carry over.** Clark's completeness conditions are about termination: the condition of computable finite extensions, and hierarchical (non-recursive) data bases, guarantee that every evaluation tree is finite, so that failure is always reached and NAF always decides. The record's "an arrangement that makes retrieval complete within the deadline" is the resource-bounded analogue of that: an arrangement in which the exhaustive pass is short enough to finish before τ. Only then does the failed search become a failure in Clark's sense, and only then (with a closed world) does absence follow. In the claim's formula this is h = 1 because the search was exhaustive, not merely likely to succeed.
- **Suggested correction to [CLAIM-306](../claims.d/CLAIM-306.md).** Replace "is negation as failure, a closed-world assumption taken on a time bound" with something like: "acts on an unfinished search as negation as failure acts on a finished one. Negation as failure (Clark 1978) infers not-p only when the search for p has been exhausted — every branch of the evaluation tree ends in failure — and then not-p is a theorem of the completed data base (the clauses read as complete definitions, with distinct names for distinct things); an unfinished or non-terminating search licenses nothing. Under a deadline the search is cut before it is exhausted, so the medic's rule is a stronger default than negation as failure: it assumes both that the collection holds only what it should (the closed world) and that the unsearched part would have failed. It is safe when the arrangement makes the exhaustive pass finish within the deadline." The summary's "Both are sound only relative to a completeness assumption" should name the two assumptions separately. Reiter ([LIT-1088](../literature.d/LIT-1088.md)) is cited by Clark as the source of the CWA but its content is not given here; the claim should not lean on this paper for what Reiter proved.
- Nothing in the paper supports the Bayesian part of the claim; it is a deductive result with no probabilities.
