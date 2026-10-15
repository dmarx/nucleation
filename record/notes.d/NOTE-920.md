---
number: 920
status: Read
formerly:
- NOTE-tmpxim6c
paper: LIT-1104
title: 'Buneman, Khanna & Tan — Why and where: a characterization of data provenance'
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Read in full on 2026-10-15 from the authors' postprint in the University of
    Pennsylvania's ScholarlyCommons repository (record repository.upenn.edu/handle/20.500.14332/6246,
    CIS Departmental Papers 210; file k50.pdf, fetched through the repository's
    API at repository.upenn.edu/server/api/core/bitstreams/e5dd7bf3-b63d-4c64-82ae-8d6dee22e5d1/content).
    The repository labels it "Postprint version. Published in Lecture Notes in Computer
    Science, Volume 1973 ... pages 316-330". The PDF is 15 pages numbered 1–15,
    generated from icdt01.dvi on 6 October 2000, so it is the authors' camera-ready
    text and does not carry the LNCS page numbers; the Springer version was not
    compared. Text extracted with pdftotext. The extraction drops the fi, ff and
    fl ligatures, renders braces as f and g, and loses the symbols ⊑, ⊔ and ⊏, so
    Definitions 6 and 7, the Why algorithm and Theorems 2 and 3 were checked against
    page images of pp. 9–10. Read: all seven sections, every definition, theorem,
    lemma, proposition and example, and the reference list. Nothing skipped. The
    paper gives no proofs: "We omit the details of R", and Theorems 1–4, Lemma 1
    and Propositions 1–2 are stated with at most a one-sentence indication of the
    proof, with details deferred to a full version that was not read. Cui and Widom's
    lineage, which the paper says its witness basis coincides with on SPJU queries,
    was not read. Every quotation of the paper below was checked against the extracted
    text by script, with whitespace normalised, running heads removed and ligatures
    restored; quotations from record entries are copied from those entries.
date: '2026-10-15'
summary: >-
  The paper separates two meanings of the provenance of a piece of output data.
  Why-provenance is the witness basis: for each valuation of the query that produces
  the value, the part of the source the query's patterns matched, one witness per
  derivation. Where-provenance is the location in the source a value was copied
  from. For a hierarchical data model and a query language that covers positive
  (SPJU) relational queries, the witness basis is preserved by the paper's query
  rewriting, and the minimal witness basis is the same for equivalent queries with
  equality conditions, while where-provenance is not invariant over equivalent queries
  in general and is preserved by rewriting only for a restricted class it calls
  traceable. Proofs are omitted, and nothing covers negation, aggregation, updates
  or additions to the source.
---

# NOTE-920: Buneman, Khanna & Tan — Why and where: a characterization of data provenance

## Contribution

Given a view V = Q(D) and a piece of data d in it, the paper asks what parts of D d came from, and answers in two ways. It works in a "deterministic" model of semistructured data, an edge-labelled tree in which the out-edges of each node carry distinct labels, so that every piece of data has a unique path, a location. Relations are encoded by putting each tuple's key on an edge. Queries are written in DQL, a where–collect language whose union is "deep union" (the union of the path representations, undefined if the result is not a partial function). The provenance of d is itself a query Q′ "completely determined by Q, D and d", computed by syntactic analysis of the query. The paper claims to be first to study where-provenance: "To our knowledge no-one has studied where-provenance."

## Key insight

Why is this here, and where did this value come from? These are different questions with different answers and different invariance. Why-provenance is about proof: a set of source structures from which the query derives the output, one per derivation. For queries with equality conditions it can be made independent of how the query is written by keeping only minimal witnesses. Where-provenance is about copying: which source location a value was taken from. It depends on how the query is written, because equivalent queries can copy a value from different places, or write it as a constant, so no purely syntactic account of it can be invariant.

## Assumptions

- **Deterministic tree model.** Every node is identified by its path of edge labels. Relations are encoded with keys as edge labels; without a key, the whole tuple becomes the label. XML fits only through positions and attribute names, and its translation is deferred to the full version.
- **Query class.** Queries must be well-formed (Definition 3: no pattern is a single variable; generators are queries or query-free; comparisons are only between variables or variables and constants, the "conjunctive" fragment) and well-defined (not undefined on any input). Variables bind only to singular values (one path ending in a constant or variable). "Restrictive as it may seem, DQL can capture positive (SPJU) relational queries and positive nested relational algebra". No Kleene star in paths, no negation, no aggregation. The motivating query in the introduction, which compares salaries with an average, is outside DQL.
- **Witness.** A value s is a witness for t with respect to Q and D if t ⊑ Q(s) and s ⊑ D, where ⊑ is containment of path representations (Definition 1).
- **Syntactic approach.** Both notions are defined on the query's syntax and normal form, not semantically. The authors: "We do not know whether there is semantic characterization for where-provenance nor do we know whether there is a semantic characterization of why-provenance that is well behaved on anything beyond than SPJU queries."
- **Output only.** Why-provenance concerns what is in the view, not what could be added: "(a) that in why-provenance we are not interested in what is not in the view (view maintenance needs to account for additions to the database) and (b) that we are not asking how to reconstruct a view under a change to the source."

## Key results

- **Theorem 1 (strong normalization).** The rewrite system R, which is not given, is strongly normalizing: every well-formed query reaches a normal form (Definition 5, a deep union of where–collect blocks whose generators are database constants and whose patterns and output expressions are singular) in finitely many steps.
- **Definition 6 (witness basis).** For a normal-form query and a singular output value t, W_Q,D(t) is the set of deep unions ⟦p₀⟧ψ ⊔ … ⊔ ⟦pₙ⟧ψ over the valuations ψ that satisfy the where clause and produce t (⟦e⟧ψ = t), unioned across the blocks of the query. For a nested query the witnesses of the inner query are combined by product. For a compound t it is the product of the bases of its singular parts. A witness that is the deep union of the leaves of some proof tree is a member; a larger witness that merely contains one (the paper's example adds an unrelated Mozart tuple) is a witness but not a member.
- **Lemma 1.** If Q rewrites to Q′ under R, then W_Q,D(t) = W_Q′,D(t) for every t in Q(D).
- **Theorem 2 (soundness and completeness).** For Q in normal form and singular t in Q(D), W_Q,D(t) = Why(t, Q, D)(D): the witness basis is obtained by running a generated query whose where clause is Q's and whose output is the instantiated patterns.
- **Comparison.** "our notion of witness basis coincides with the derivation of a tuple in [7] for SPJU queries where the general case of theta-join is considered." Details deferred.
- **Definition 7 and Theorem 3 (minimal witness basis).** s is a minimal witness for t if no proper substructure s′ ⊏ s has t ⊑ Q(s′). The minimal witness basis M_Q,D(t) is the subset of W_Q,D(t) of members with no other member strictly inside them. "Observe that a witness for a value is invariant under all equivalent queries but the witness basis is not." Theorem 3: if Q and Q′ are equivalent well-formed queries "with only equality conditions" and t is in both outputs, M_Q,D(t) = M_Q′,D(t). The proof is said to rest on a homomorphism theorem for containment in this class, and to extend, following Klug, to "certain subclasses of queries with inequalities".
- **Theorem 4 (unnesting of witnesses).** For a query Q over sources D and a view V(D), computing witnesses against D and V and then replacing each view part by its own witnesses from D gives the same basis as composing the view into the query first and computing witnesses against D.
- **Where-provenance is not invariant (Section 6, by example).** Q1 writes $50K as a constant in its output and Q2 copies it from a variable; the queries are equivalent, but only Q2's value has a source location, and Q1's is ascribed to the query. Q3 and Q4 are equivalent, but Q4's value comes from two variables forced equal, which syntax alone does not reveal. Nested queries make tracking harder. Conclusion: "for general queries, where-provenance is not invariant over the space of equivalent queries, and that a purely syntactic characterization of where-provenance is unlikely to yield a complete description of the where-provenance."
- **Definition 8 (derivation basis).** For an atomic output value at path l, the set of pairs (witness, set of source paths bound to the output variable that produced it), over the valuations that produce it.
- **Definition 9 and Propositions 1–2 (traceable queries).** A query is traceable if each pattern matches a database constant or a subquery, every subquery is a view sharing no variables with the outer scope, only a singular pattern matches a subquery, and that pattern and the subquery's output are equal-length sequences of distinct variables. Traceability is preserved by R (Proposition 1), and for traceable queries the derivation basis is preserved by R (Proposition 2).
- **Conclusion's own summary.** "why-provenance is preserved over the class of well-defined queries and where-provenance is preserved over the class of traceable queries", both under the rewrite rules. Open: necessary and sufficient conditions for well-definedness, and whether constraints such as functional dependencies give a fuller where-provenance.

## Bearing on the record

**[QUESTION-105](../questions.d/QUESTION-105.md).** The paper supplies a precise candidate for one kind of retained state and a precise statement of which part of it is independent of how a conclusion was derived. For a positive query, the minimal witness basis of an output is a set of alternative sufficient supports, each a set of source facts. That is what a revision by deletion of source facts needs in set semantics: an output survives the deletion of some facts exactly when some witness avoids them all. This consequence is the record's reading; the paper does not discuss deletion and explicitly sets aside changes to the source ("we are not asking how to reconstruct a view under a change to the source"). The paper's split also bears on the question's phrasing. "Provenance" is two things here: why-provenance is support, where-provenance is the origin of a copied value, and only the first is invariant. A retained state that records where each value came from is the non-invariant one. What the paper does not supply: any account of revisions that add facts (it excludes "what is not in the view"), any nonmonotone query (no negation, no aggregation), any weights or strengths of support, and any measure of how small the retained state is. Its "minimal" is set-inclusion minimality of each witness, not minimal information retained, so it does not answer the question's optimization. Against the record's AGM and belief-base THEORYs ([THEORY-353](../theory.d/THEORY-353.md), [THEORY-347](../theory.d/THEORY-347.md)) it is a different object: those fix a revision by a selection over remainders or by a base; this keeps the derivations of each conclusion from a base of source facts, which is nearest to the base side and to Doyle-style dependency records, and says nothing about choosing what to give up.

**[CLAIM-303](../claims.d/CLAIM-303.md).** The paper defines provenance as a query computed from Q, D and d, so it is reconstructed on demand rather than filed, provided the query and the source are kept. That is one side of [CLAIM-303](../claims.d/CLAIM-303.md)'s trade made concrete: dependency tracking for positive queries need not be stored if the derivation can be rerun. The paper prices nothing and gives no complexity bounds.

**[CLAIM-306](../claims.d/CLAIM-306.md).** Neither notion applies to a conclusion of absence. Both are defined for positive queries and for values present in the output; the paper's opening example, where a nonmonotone query makes "every tuple" relevant, is informal and outside DQL. So the paper supports [CLAIM-306](../claims.d/CLAIM-306.md)'s asymmetry only by its silence: provenance as defined here is a structure for presence, and the provenance of "it isn't there" would have to range over the whole collection, which the paper does not define.

**The workbench entry of 2026-10-15 (U12–U13).** A12's "independent support survives invalidation" is the witness-basis structure: two witnesses, delete a fact in one, the output survives by the other. The record's [CASE-089](../cases.d/CASE-089.md) adds that the strength of the survivor matters, which a witness basis does not carry.

**[LIT-1104](../literature.d/LIT-1104.md)'s own entry.** Its "Why this is here" gloss of why-provenance as "which inputs justify it" is right in spirit but loses the structure that matters: the paper's why-provenance is a set of witnesses, one per derivation, not a single set of contributing inputs. A flattened set of contributing inputs, which is what Green, Karvounarakis and Tannen compute under the name "why-provenance" and attribute partly to this paper ([LIT-1110](../literature.d/LIT-1110.md)), cannot say whether an output survives a deletion; the witness basis can.
