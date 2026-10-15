---
status: Read
paper: LIT-tmpjckak
title: Green, Karvounarakis & Tannen — Provenance semirings
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Read in full on 2026-10-15 from the authors' postprint in the University of
    Pennsylvania's ScholarlyCommons repository (record repository.upenn.edu/handle/20.500.14332/8764,
    Database Research Group (CIS) 19; file pods07.pdf, fetched through the repository's
    API at repository.upenn.edu/server/api/core/bitstreams/b598c0a7-0d24-4162-8279-5f51a17d29c2/content).
    The repository labels it "Postprint version. Copyright ACM, 2007. This is the
    author's version of the work. It is posted here by permission of ACM". The PDF
    is 10 pages, generated on 21 March 2007, carries the PODS'07 copyright block
    on page 1 and no page numbers; the ACM version of record (pp. 31–40) was not
    compared. Text extracted with pdftotext, in reading order and in layout mode;
    the figures were checked against page images of pp. 2–3, and the figure values
    quoted below (Figures 3 and 5) were checked by hand against them. Read: all
    eleven sections, every definition, proposition, theorem, figure and both algorithms,
    and the reference list. Nothing skipped. Proofs: Propositions 5.2 and Theorem
    9.2 have sketches; Theorem 4.3 is derived in the text from Propositions 3.5
    and 4.2; the other propositions and Theorems 5.6, 6.4 and 6.5 are stated without
    proof. Buneman, Khanna and Tan (LIT-tmp8m5l3) was read the same day; the lineage
    papers of Cui and Widom and the cited work on c-tables, event tables and route-provenance
    were not. Every quotation of the paper below was checked against the extracted
    text by script, with whitespace normalised; quotations from record entries are
    copied from those entries.
date: '2026-10-15'
summary: >-
  Annotating each input tuple with an element of a commutative semiring, and computing
  union and projection with + and join with ·, gives one positive relational algebra
  (RA+) that is set semantics over the Booleans, bag semantics over the naturals,
  c-tables over positive Boolean expressions, event tables over sets of outcomes,
  and lineage over sets of tuple ids. The polynomials N[X] in the tuple ids are
  the most general such annotation: for any RA+ query and any commutative semiring
  K, the K-annotated answer is the provenance polynomial evaluated at the input's
  K-annotations (Theorem 4.3). For datalog the paper needs ω-continuous semirings
  and formal power series N∞[[X]], with the analogous factorization (Theorem 6.4)
  and a criterion for infinite coefficients (Theorem 6.5). Everything is positive:
  no negation, difference or aggregation, and revaluing inputs can only remove output
  tuples, never add them; trust and deletion propagation are not treated.
---

# NOTE-tmpc5ict: Green, Karvounarakis & Tannen — Provenance semirings

## Contribution

Four existing generalizations of relational algebra (Imielinski–Lipski c-tables, Fuhr–Rölleke–Zimányi event tables for probabilistic databases, lineage in data warehouses, and bag semantics) compute with annotations in "strikingly similar" ways. The paper unifies them: "We propose using commutative semirings for this purpose." It defines K-relations, gives RA+ on them, shows the semiring laws are exactly what the usual RA identities require, proposes polynomials with natural-number coefficients as the provenance annotation, extends the whole construction to datalog with fixed points and formal power series, gives algorithms to compute or test the resulting series, applies them to datalog on incomplete and probabilistic databases, and relates containment of queries across semirings.

## Key insight

A semiring annotation records only two ways of combining support: alternatives (+, from union and projection) and joint use (·, from join). The symbolic record of those combinations, a polynomial in the input tuple ids, is the free commutative semiring, so every other annotation is obtained from it by substituting values. Provenance is then not one more annotation beside counts, truth values and probabilities; it is the one they all factor through. "It seems that we need to know not just which input tuples contribute but also how they contribute." The paper's footnote names this: "In contrast to why-provenance, the notion of provenance we propose could justifiably be called how-provenance."

## Assumptions

- **K-relations (Definition 3.1).** A K-relation over attributes U is a function from U-tuples to K with finite support; tuples not in the relation get 0.
- **Positive relational algebra (Definition 3.2).** Empty relation (all 0), union (R₁ + R₂), projection (sum of the tags of the tuples that project to t), selection (multiply by a predicate that is 0 or 1), natural join (R₁(t₁) · R₂(t₂)) and renaming. No difference, no negation, no aggregation. Which 0/1 predicates are allowed in selection is "left unspecified".
- **Commutative semiring.** (K, +, 0) and (K, ·, 1) commutative monoids, · distributing over +, and 0 · a = a · 0 = 0; Definition 3.2 also assumes 0 ≠ 1.
- **Datalog (Section 5).** Pure datalog, all subgoals relational atoms, a countable domain. Semantics: the tag of an answer is the sum over all its derivation trees of the product of the tags of the leaves (Definition 5.1). This needs infinite sums, so K must be a commutative ω-continuous semiring: naturally ordered, ω-chains have least upper bounds, + and · continuous. B, N∞, PosBool(B) with B finite, P(Ω), the tropical semiring and the fuzzy semiring qualify; N and N[X] do not.
- **Idempotence is not assumed.** "Glaringly absent from the list of relational identities are the idempotence of union and of (self-)join. Indeed, these fail for the bag semantics".

## Key results

- **Proposition 3.4.** The RA identities (union associative, commutative, identity ∅; join associative, commutative and distributive over union; projections and selections commuting with each other and with unions and joins; σ_false(R) = ∅ and σ_true(R) = R) hold for RA+ on K-relations if and only if (K, +, ·, 0, 1) is a commutative semiring.
- **The examples as instances.** (B, ∨, ∧, false, true) gives RA+ under set semantics; (N, +, ·, 0, 1) bag semantics; (PosBool(B), ∨, ∧, false, true) "exactly the Imielinski-Lipski algebra" on c-tables; (P(Ω), ∪, ∩, ∅, Ω) the Fuhr–Rölleke–Zimányi algebra on event tables. Probabilities are then computed from the output events, outside the semiring.
- **Proposition 3.5.** For commutative semirings K and K′, applying a map h : K → K′ to the tags commutes with every RA+ query if and only if h is a semiring homomorphism. Under such a map "the support may shrink but never increase".
- **Why-provenance as a semiring (Section 4).** "Computing the why-provenance for queries in RA+ turns out to be exactly Definition 3.2 for the semiring (P(X), ∪, ∪, ∅, ∅)", X the input tuple ids. The paper's why-provenance is "the set of all contributing input tuples", which it attributes to Cui and Widom and to Buneman, Khanna and Tan. In the running example (Figure 5) the outputs (d, e) and (f, e) both get {r, s}, though "the query can also calculate (f, e) from s alone and (d, e) from r alone"; "this cannot be detected by why-provenance".
- **Definition 4.1 and Proposition 4.2.** The provenance semiring for RA+ is N[X], polynomials in the tuple ids with natural-number coefficients. For any commutative semiring K and any valuation v : X → K there is a unique semiring homomorphism Eval_v : N[X] → K extending v.
- **Theorem 4.3 (factorization).** For any RA+ query q, q(R) = Eval_v ∘ q(R̄), where R̄ tags each tuple in the support of R with its own id and v maps each id to that tuple's tag in R. In words, "the semantics of RA+ on K-relations for any semiring K factors through the semantics of the same in provenance semirings." Example: the polynomial of (d, e) in Figure 5(c) is 2r² + rs, and with p = 2, r = 5, s = 1 it gives 55, the multiplicity in the bag example (Figure 3). The polynomial of (f, e) is 2s² + rs, read as three derivations, two using s twice and one using r and s.
- **Datalog semantics (Definitions 5.1, 5.5; Propositions 5.2–5.4; Theorem 5.6).** The derivation-tree semantics gives finite support (5.2); agrees with RA+ on non-recursive translations of RA+ queries whose selections test only attribute equality (5.3); and over B gives ordinary datalog (5.4). Theorem 5.6: each nonzero tag equals the corresponding component of the least fixed point of the algebraic system Q̄ = T_q(R, Q̄) obtained from the immediate consequence operator. Proposition 5.7: ω-continuous semiring homomorphisms commute with datalog queries.
- **Formal power series (Definition 6.1, Proposition 6.3, Theorem 6.4).** "polynomials will not suffice for the provenance of tuples in the output of datalog queries because the semiring N[X] does not define infinite sums". The datalog provenance semiring is N∞[[X]], formal power series with coefficients in N extended by ∞; infinitely many distinct monomials give the series, infinitely many copies of one monomial give the ∞ coefficients. For any commutative ω-continuous K and valuation v there is a unique ω-continuous homomorphism Eval_v : N∞[[X]] → K (Proposition 6.3), and Theorem 6.4: "The semantics of datalog on K-relations for any commutative ω-continuous semiring K factors through the semantics of the same in provenance semirings (of formal power series)." Example: for transitive closure, the coefficient of rnps³ in the provenance of Q(a, d) is 5, five derivations using R(a, c), R(c, b), R(b, d) once and R(d, d) three times.
- **Theorem 6.5.** A tuple t's provenance series has no ∞ coefficient (is in N[[X]]) if and only if t is in the result and the instantiated program has no cycle of unit rules (rules whose body is a single idb atom) with t on the cycle.
- **Section 7 (algorithms).** All-Trees decides, for every output tuple, whether its series is a polynomial in N[X], and computes it if so; Theorem 6.5 then decides membership in N[[X]], and a cycle test decides N∞[X]. Monomial-Coefficient computes the coefficient of a given monomial, including ∞. Termination is argued; no complexity bounds are given.
- **Section 8.** For a finite distributive lattice K, a modified All-Trees, which keeps a derivation only if its monomial is smaller than any seen for that tuple, always returns polynomials, and evaluating them in K gives the K-relation answer. This yields datalog on Boolean c-tables ("new for incomplete databases") and on event tables over a finite domain.
- **Theorem 9.2.** If K is a distributive lattice, for unions of conjunctive queries q₁ ⊑_K q₂ if and only if q₁ ⊑_B q₂, so containment is decided as under set semantics.
- **Conclusion's own claim.** Coarser annotations, "even multisets", are coarser forms of provenance, while polynomials and power series are "the most general form of annotation possible with the boundaries of semiring structures". Open: negation, "which seems to require axiomatizing an additional operation akin to “proper subtraction” in N"; tropical datalog; and whether bag containment of (unions of) conjunctive queries implies containment under N[X].

## Two things the text gets wrong or leaves loose

- **The why-provenance structure is not a semiring as the paper defines one.** (P(X), ∪, ∪, ∅, ∅) has 0 = 1 = ∅, against Definition 3.2's 0 ≠ 1, and 0 · a = ∅ ∪ a = a, against the annihilation law the paper lists. Read literally, a join with an absent tuple would keep the other tuple's ids. This is the record's check of the paper's own definitions; repairing it needs a separate zero, which the paper does not supply.
- **"Why-provenance" here is not Buneman, Khanna and Tan's.** This paper's why-provenance is one set of contributing tuples per output. The witness basis of [LIT-tmp8m5l3](../literature.d/LIT-tmp8m5l3.md) is a set of witnesses, one per derivation, and on Figure 5 it would distinguish (d, e) (witnesses {r} and {r, s}) from (f, e) ({s} and {r, s}), which this paper says why-provenance cannot. So the limitation the paper shows belongs to the flattened set (lineage), not to the witness basis it cites as the same notion. (The witness sets for Figure 5 are the record's computation from the derivations the paper lists.)
- Minor: the datalog provenance semiring is written N∞[X] in the sentence before Proposition 6.2, where N∞[[X]] is meant.

## Bearing on the record

**[QUESTION-105](../questions.d/QUESTION-105.md).** This is the nearest thing in the record to a theorem of the question's form, and its limits are exact. Fix a positive query (RA+, or datalog with ω-continuous semirings) and take as the family of future revisions every re-annotation of the input facts in any commutative semiring: deleting a fact (tag 0), counting copies, attaching a condition, a probability event, a cost or a confidence level. Then retaining each output's provenance polynomial (or series) suffices for every revision in the family without rerunning the query: by Theorem 4.3 (6.4 for datalog) the revised output annotation is the polynomial evaluated at the revised input annotations. The retained state does look like provenance in the question's sense, a record of which inputs combine, jointly or alternatively, and in how many ways. Deletion propagation is the special case of evaluating with a deleted id set to 0 (the record's application of Theorem 4.3 to a valuation into N[X] or B; the paper does not discuss deletion). What it does not supply: (1) minimality. The "most general" annotation is the free object; the theorem says N[X] suffices for every semiring, not that it is the least state for a given family, and a narrower family needs less (for set-semantics deletion, which inputs occur in which monomial suffices, with coefficients and exponents dropped; this is the record's observation, not the paper's). The paper proves no lower bound and gives no size bounds. (2) Additions. Revaluing can only shrink the support, so a revision that adds a fact, or a conclusion that is not in the current output, is outside the family. (3) Nonmonotone revision. No negation, difference or defeat: AGM contraction and revision ([THEORY-353](../theory.d/THEORY-353.md)), belief bases ([THEORY-347](../theory.d/THEORY-347.md)) and the defeaters of [CASE-090](../cases.d/CASE-090.md) all need what the authors leave open. (4) Choosing what to give up. The polynomial tells you what happens to each output under a given deletion; it does not choose a deletion to remove a given output, which is where the AGM selection function lives.

**[CLAIM-293](../claims.d/CLAIM-293.md) and [CASE-089](../cases.d/CASE-089.md).** The paper sharpens [CLAIM-293](../claims.d/CLAIM-293.md) rather than contradicting it. A provenance polynomial is more than support-graph topology (it separates joint from alternative support and counts derivations), but it is still the same in [CASE-089](../cases.d/CASE-089.md)'s two worlds (e₁ + e₂ if the two pieces of evidence are alternative supports for H): the difference between 20:1 and 1.1:1 lives in the valuation, which the polynomial deliberately leaves out. Whether combining independent evidence by multiplying Bayes factors is a semiring evaluation of that polynomial at all is outside the paper; probabilities here come from event tables, computed after the semiring calculation.

**[CLAIM-303](../claims.d/CLAIM-303.md).** The paper's choice is to file: compute the polynomial once and evaluate it under each revision, instead of rerunning the query, which is the trade [CLAIM-303](../claims.d/CLAIM-303.md) describes, with dependency tracking taking the specific form of a polynomial per output. For recursive derivations the filed object may be an infinite series, held finitely only as a system of fixed-point equations or as a test for finiteness (Section 7). The paper gives no costs, so it settles nothing about when filing pays.

**[CLAIM-306](../claims.d/CLAIM-306.md).** Negation as failure is exactly what the paper leaves out: no negation, and the authors expect it to need a proper subtraction. Provenance here is for presence. A tuple tagged 0 has the zero polynomial, which records nothing about why it is absent.

**The workbench entry of 2026-10-15 (U13).** A13 brought provenance semirings to cache invalidation; the factorization theorem is what makes that natural, since invalidating an input is revaluing it and the outputs' new tags follow by evaluation. A12's "independent support survives invalidation" is the + of the semiring: an output whose polynomial has a monomial without the invalidated id survives. Its "Changes to epistemic grounds should propagate obligations to review, not automatically propagate changes of belief" is about policy, which the algebra does not touch.

**[LIT-tmpjckak](../literature.d/LIT-tmpjckak.md)'s own entry.** Its "Why this is here" says the algebra "specializes to counting derivations, lineage and deletion propagation". Counting derivations (N, N∞) and lineage (the P(X) structure, with the defect above) are in the paper. Deletion propagation is not: the paper never mentions deletion. It follows from Theorem 4.3, but the entry should say it is the record's application, not the paper's result. Trust is mentioned once, as a motive ("one of r or s is perhaps less trusted"), not as a semiring.
