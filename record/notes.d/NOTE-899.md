---
number: 899
status: Read
formerly:
- NOTE-tmpjk9xt
paper: LIT-1088
title: Reiter — On closed world data bases
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Read in full on 2026-10-15 from the author's own preprint, held by his department:
    Raymond Reiter, "On Closed World Data Bases", Technical Report 77-16, Department
    of Computer Science, University of British Columbia, October 1977, served by
    UBC's technical-report archive (www.cs.ubc.ca/sites/default/files/tr/1977/TR-77-16.pdf,
    listed at www.cs.ubc.ca/tr/1977/tr-77-16). It is a 2020 scan of the typescript,
    18 PDF pages (abstract page plus pp. 1–17), with an OCR text layer. Its abstract
    page says it was "Presented at the Workshop on Logic and Data Bases, Toulouse,
    France, November 16-18, 1977", the workshop whose proceedings are the Gallaire
    and Minker volume. The published Plenum chapter (pp. 55–76) was not seen, so
    this note reads the workshop version; its wording, numbering and any added material
    in the published chapter are unconfirmed. Text extracted with pdftotext -layout.
    The OCR mangles overbars (negation), turnstiles and set brackets, so the definition
    of EDB-bar (p. 7), the "no gaps" passage and Theorem 3.1 (p. 9), Theorem 4.2
    and Example 4.3 (p. 11) and Theorem 4.5 (p. 13) were checked against page images.
    Read: all six sections, every definition, theorem, corollary and example, and
    the reference list. Nothing skipped. The paper itself gives no proofs ("In the
    interest of brevity, we have ommitted all proofs of the results in this paper");
    they are in Reiter (1977a), a BBN technical report, which was not read. So the
    theorems below are as stated, not checked. Every quotation below was checked
    against the extracted text by script, with whitespace normalised; where the
    OCR garbles a quoted word, the page image was used and the discrepancy is listed
    here. OCR-only differences, where the quotation follows the page: "Q are" (OCR
    "Qare"), "representation" (OCR "represen t ation"), "gaps" in straight quotes
    (OCR "11 gaps 11"), "evaluation" (OCR "eiva.luation"), "EDB-bar" for the overbarred
    EDB (OCR "EDB"). "ommitted" and "never known" are the typescript's own spellings.
date: '2026-10-15'
summary: >-
  Reiter defines the closed-world assumption (CWA) for a function-free first-order
  database as reasoning from DB together with the negation of every ground atom
  that DB does not entail, and contrasts it with the open-world assumption (OWA),
  under which only what DB entails is an answer. He shows that, when DB with these
  added negations is consistent, closed-world evaluation of any existential query
  reduces to ordinary (open-world) evaluation of atomic queries combined by union,
  intersection, difference and projection, so the negations never need to be listed.
  The CWA can make a consistent database inconsistent (Pa ∨ Pb yields ¬Pa and ¬Pb);
  consistent Horn databases, and all definite databases, stay consistent. Nothing
  in the paper concerns how long a search takes: non-entailment is a fixed logical
  relation, and the CWA's justification is stated as an assumption of total knowledge
  of the domain, not proved as a soundness condition.
---

# NOTE-899: Reiter — On closed world data bases

## Contribution

The paper names and formalises the two assumptions under which deductive
question-answering systems evaluate queries. Under the open-world
assumption "the only answers to Q are those which obtain from proofs of Q
given DB as hypotheses". Under the closed-world assumption "certain answers
are admitted as a result of failure to find a proof. More specifically, if
no proof of a positive ground literal exists, then the negation of that
literal is assumed true." It then shows how closed-world answers can be
computed without ever writing the negative facts down, and which databases
the assumption leaves consistent.

## Key insight

Writing only positive facts and letting the absence of a fact stand for its
negation is a convention that "presumes total knowledge about the domain
being represented". In a database of ground facts it is harmless. Once
the database has general clauses, "absent" has to mean "not derivable", and
the convention becomes: add ¬Pc for every ground atom Pc that DB does not
entail. Because every ground atom is then decided one way or the other,
closed-world answers are always definite, and query evaluation splits into
atomic pieces. The price is that a database which knows a disjunction
without knowing which disjunct holds is made inconsistent.

## Assumptions

- **Function-free first-order language with typed variables.** A data base
  is "a set of clauses containing no function signs"; queries are
  existential, of the form ⟨x/τ | (∃y/θ) W(x, y)⟩ with W quantifier-free
  and function-free. Each type τ has a set |τ| of constant signs. The
  paper says function signs could be allowed "without significantly
  affecting the results", but presents only the constant-only theory.
- **Answers are sets of tuples of constants, judged by provability.** An
  OWA answer c(1) + … + c(r) requires DB ⊢ ∨ᵢ (∃y/θ) W(c(i), y). Minimal
  answers with one tuple are definite; minimal answers with several are
  indefinite (DB knows it is one of them, not which).
- **The CWA itself (p. 7).** EDB-bar = {¬Pc | P a predicate sign, c a tuple
  of constant signs, and DB ⊬ Pc}, and c(1) + … + c(r) is a CWA answer iff
  each c(i) is of the right types and DB ∪ EDB-bar ⊢ ∨ᵢ (∃y/θ) W(c(i), y).
  For a purely extensional database the condition is Pc ∉ DB; for a
  general one it is non-derivability. The definition is about entailment
  from DB, not about any procedure or the time it takes.
- **What justifies it is an assumption of complete knowledge, stated not
  proved.** "by adopting this convention, we are making an assumption about
  our knowledge about the domain, namely, that we know everything about each
  predicate of the domain. There are no gaps in our knowledge." "The
  implicit representation of negative facts presumes total knowledge about
  the domain being represented. Fortunately, in most applications, such an
  assumption is warranted." There is no semantics of the domain against
  which the CWA is shown sound or unsound; the formal results concern
  consistency and computation.
- **Proofs are omitted** and deferred to Reiter (1977a).

## Key results

- **Theorem 3.1 (no indefinite answers).** For Q = ⟨x/τ | (∃y/θ) W(x, y)⟩,
  every minimal CWA answer to Q is definite. Basis: for each P and c,
  "either DB ⊢ Pc or EDB-bar ⊢ ¬Pc" (from the page image), so "there can
  be no "gaps" in our knowledge about the domain".
- **Theorem 4.1 (connectives become set operations).** Under the CWA,
  ‖⟨x/τ | (∃y/θ) W₁ ∨ W₂⟩‖ = ‖⟨…W₁⟩‖ ∪ ‖⟨…W₂⟩‖, and for quantifier-free
  queries ‖⟨x/τ | W₁ ∧ W₂⟩‖ = ‖⟨…W₁⟩‖ ∩ ‖⟨…W₂⟩‖. *Conditions:* the ∧ case
  needs a quantifier-free query. Both identities fail under the OWA
  (Examples 4.1 and 4.2: DB = {Pa ∨ Ra} answers Px ∨ Rx with {a} but Px and
  Rx each with nothing).
- **Theorem 4.2 (negation becomes set difference).** If W, W₁, W₂ are
  quantifier-free and DB ∪ EDB-bar is consistent, then ‖⟨x/τ | ¬W⟩‖CWA =
  |τ| − ‖⟨x/τ | W⟩‖CWA and ‖⟨x/τ | W₁ ∧ ¬W₂⟩‖CWA = ‖⟨…W₁⟩‖CWA −
  ‖⟨…W₂⟩‖CWA. *Conditions:* quantifier-free and CWA-consistent; it fails
  for quantified queries (Example 4.3) and under the OWA.
- **Theorem 4.3 and Corollary 4.4 (projection).** An existential query is
  the projection of the corresponding quantifier-free query:
  ‖⟨x/τ | (∃y/θ) W⟩‖CWA = π_y ‖⟨x/τ, y/θ | W⟩‖CWA, and negations and
  conjunctions are taken before projecting.
- **Theorem 4.5 (the principal result of §4).** For an atomic query Q, if
  DB is consistent with the CWA (DB ∪ EDB-bar consistent), then
  ‖Q‖CWA = ‖Q‖OWA. With 4.1–4.4 this gives "a complete characterization of
  the CWA answers to an arbitrary existential query Q" from OWA answers to
  atomic queries: "CWA query evaluation has been reduced to OWA atomic query
  evaluation", and "we need never known [sic] the elements of EDB-bar". *Condition:* CWA-consistency.
  Example 4.5 works an inventory query through.
- **Example 5.1 (the CWA can create inconsistency).** "Not every consistent
  data base remains consistent under the CWA." DB = {Pa ∨ Pb}: DB entails
  neither Pa nor Pb, so EDB-bar = {¬Pa, ¬Pb}, and DB ∪ EDB-bar is
  inconsistent. Reiter knows of no characterisation of CWA-consistent
  databases.
- **Theorem 5.1 (Horn suffices).** If DB is Horn (every clause has at most
  one positive literal) and consistent, then DB ∪ EDB-bar is consistent.
  This is a sufficient condition only.
- **Theorem 5.2 (negative clauses are idle).** If DB is Horn and
  consistent, CWA answers to any existential query are the same with
  respect to DB and to Δ(DB), DB with its purely negative clauses removed:
  "negative clauses in DB have no influence on CWA query evaluation". It
  fails for non-Horn DBs (Example 5.2).
- **Theorem 5.3 and Corollary 5.4.** A definite database (every clause has
  exactly one positive literal) is consistent, and consistent with the CWA.
  Reiter calls 5.4 "a central result".
- **Relation to programming languages and semantics.** The CWA is
  "intimately related to the negation operators of PLANNER [Hewitt 1972] and
  PROLOG [van Emden and Kowalski 1976] since in these languages, negation
  means "not provable"". Van Emden's minimal-model condition (the
  intersection of all models is itself a model) is cited as a semantic
  criterion for CWA-consistency. The phrase "negation as failure" does not
  occur in this version.
- **Summary formula.** The CWA "says, in effect, "everything that you don't
  know to be true may be assumed false"".

## Bearing on the record

**On [CLAIM-306](../claims.d/CLAIM-306.md): Reiter supplies the closed-world assumption and its
standing condition, but not a soundness theorem, and nothing about time.**

- **The definition matches, as entailment.** The claim and [LIT-1088](../literature.d/LIT-1088.md)
  gloss the CWA as "in a database taken to be complete, a fact that cannot
  be derived is taken to be false". That is right: EDB-bar is the set of
  negated ground atoms DB does not entail, and Reiter says the convention
  presumes the database knows everything about each predicate.
- **"Sound only relative to a completeness assumption" is a fair gloss of
  his framing, not of a result.** Reiter states, in prose, that the
  convention "presumes total knowledge about the domain" and says this is
  usually warranted. He proves nothing about soundness relative to the
  world; his theorems are about consistency and computation. The record's
  words "standardly described as sound only relative to a completeness
  assumption" should cite Reiter for the assumption, and should not
  attribute to him a soundness condition. If a formal soundness statement
  is wanted (negation as failure is sound with respect to the completed
  database), that is Clark's ([LIT-1087](../literature.d/LIT-1087.md), unread), not Reiter's.
- **Reiter's CWA is not about a search procedure or a deadline.** The
  abstract does say "as a result of failure to find a proof", and the
  airline illustration is close to the medic's rule: "If I fail to find an
  entry indicating that Air Canada flight 103 connects Vancouver with
  Toulouse I will conclude that it does not." But the formal definition is
  DB ⊬ Pc, a fixed relation. For the paper's function-free databases with
  finite type extensions it is decidable, and nothing in the paper bounds
  the time spent deciding it. "Not found within τ" is a different and
  weaker relation: it includes atoms DB does entail but that the search did
  not reach. So "a closed-world assumption taken on a time bound" is the
  record's extension, not Reiter's notion, and the paper gives no result
  about it.
- **Reiter's guarantees do not carry over to the time-bounded version.**
  Theorem 5.1's consistency guarantee for Horn databases depends on adding
  ¬Pc only when DB ⊬ Pc. A time-bounded rule that adds ¬Pc for an
  entailed but unfound Pc makes even a Horn database inconsistent. The
  claim's Bayesian condition (h → 1, retrieval complete within the deadline)
  is what would make the time-bounded set coincide with Reiter's EDB-bar;
  that identification is the record's argument and is not in the paper.
- **The medic's situation is Reiter's Example 5.1, which tells against the
  CWA there, not for it.** In [CASE-085](../cases.d/CASE-085.md) the EMT knew the unit was stocked:
  the item is in one of its compartments, he cannot say which. That is a
  disjunction without a known disjunct, the non-Horn case. Applied to each
  "it is in compartment k", the CWA adds every negation and contradicts
  "it is stocked", exactly as {Pa ∨ Pb} becomes inconsistent. On
  Reiter's terms, then, the CWA is unavailable to a searcher who knows the
  item is present, and "it isn't there" in [CASE-085](../cases.d/CASE-085.md) cannot be a
  closed-world inference from what the medic knew. This supports the
  claim's own conclusion that the medic's statement "was a decision to stop
  searching, not a finding", and narrows its framing: the medic's rule is a
  closed-world assumption only for a searcher who does not already know
  the item is there.
- **What the paper does support.** It is the right source for the
  open/closed-world distinction, for the CWA as an implicit addition of
  negated atoms licensed by an assumption of complete knowledge, and for
  the observation that the convention is safe (consistent) for Horn and
  definite databases and can fail for disjunctive ones. It is evidence for
  none of the claim's empirical or decision-theoretic content, and it
  neither supports nor weakens the search asymmetry or the Bayesian
  formula.
