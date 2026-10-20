---
number: 367
status: Active
formerly:
- THEORY-tmpbyiv8
title: "For SPJU relational queries, which Buneman, Khanna and Tan's tree model encodes, the minimal witnesses of an output tuple, the inclusion-minimal sets of source facts from which the query still derives it, are the minimal sets matched by single derivations and so are the same for every equivalent query, while where-provenance, the source location a value was copied from, can differ between equivalent queries"
version: 2
history:
- version: 2
  date: '2026-10-20'
  note: >-
    Narrowed and promoted, carrying out the promotion audit's decision
    for THEORY-367 (batch 053, ADR-047 v2). The dated note below proves
    that minimal witnesses are invariant for SPJU queries, the alternative
    the promote_when named. The rewrite-system clauses rest on rules the
    paper does not give, and "only for traceable queries" claims more than
    the paper shows. Both leave the title for QUESTION-tmpo255i.
tags:
- databases
- logic
date: '2026-10-15'
source:
- LIT-1104
summary: >-
  Buneman, Khanna and Tan (2001), [LIT-1104](../literature.d/LIT-1104.md), read in [NOTE-920](../notes.d/NOTE-920.md). Two
  meanings of the provenance of output data: why it is there (the witness
  basis, the source structures matched by each valuation that produces it)
  and where a value came from (the source paths bound to the output
  variable). The first is preserved by the paper's rewrite system and, cut
  down to minimal witnesses, agrees across equivalent queries with equality
  conditions; the second is shown by example to depend on how the query is
  written. Proofs are omitted. It is not a theory of revision: additions to
  the source, negation, aggregation and strengths of support are all outside it.
---

# THEORY-367: For SPJU relational queries, which Buneman, Khanna and Tan's tree model encodes, the minimal witnesses of an output tuple, the inclusion-minimal sets of source facts from which the query still derives it, are the minimal sets matched by single derivations and so are the same for every equivalent query, while where-provenance, the source location a value was copied from, can differ between equivalent queries

## Source

Buneman, Khanna and Tan (2001), [LIT-1104](../literature.d/LIT-1104.md) (ICDT 2001, LNCS 1973,
pp. 316–330), read in [NOTE-920](../notes.d/NOTE-920.md) from the authors' postprint: Definitions
6–9, Lemma 1, Theorems 1–4, Propositions 1–2 and the examples of Section 6.

## What was actually shown

**The setting.** Data are edge-labelled trees in which a node's out-edges
carry distinct labels, so every value has a unique path; relations are
encoded with keys on edges. Queries are well-formed, well-defined
where–collect expressions combined by deep union, with comparisons only
between variables and constants. "Restrictive as it may seem, DQL can
capture positive (SPJU) relational queries and positive nested relational
algebra". There is no negation and no aggregation.

**Why-provenance.** A witness for t is any s ⊑ D with t ⊑ Q(s). The witness
basis W_Q,D(t) keeps only the witnesses read off the query: for each
valuation that satisfies the where clause and produces t, the deep union of
the matched patterns. It is computed by a generated query (Theorem 2), is
preserved when the query is rewritten (Lemma 1), and composes through views
(Theorem 4). The witness basis itself is not invariant: "Observe that a
witness for a value is invariant under all equivalent queries but the
witness basis is not." Its members with no other member strictly inside
them, the minimal witness basis, are the same for equivalent well-formed
queries "with only equality conditions" (Theorem 3).

**Where-provenance.** The source paths bound to the output variable that
produced a value. The paper shows by pairs of equivalent queries that it is
not invariant: a value written as a constant in one query has no source
location, and a value copied from two variables forced equal is not
visible as such from syntax. Its conclusion: "for general queries,
where-provenance is not invariant over the space of equivalent queries".
For traceable queries (views sharing no variables with the outer query,
matched by sequences of distinct variables), the derivation basis is
preserved by rewriting (Proposition 2).

**What could have come out the other way.** Minimal witnesses could have
depended on the form of the query, as the full witness basis does; the
claim is that they do not, for equality conditions. That is the theorem the
record has not seen proved.

## What this does not say

- **That provenance supports revision.** The paper sets changes aside:
  "we are not asking how to reconstruct a view under a change to the
  source", and it is "not interested in what is not in the view". That a
  minimal witness basis decides whether an output survives deleting source
  facts is the record's reading, true in set semantics, not the paper's
  result.
- **That "minimal" means least retained.** A minimal witness is minimal by
  inclusion. Nothing measures the size of the witness basis or compares it
  with other retained states.
- **That why-provenance is one set of contributing inputs.** It is a set of
  witnesses. Flattening them into one set, as Green, Karvounarakis and
  Tannen's "why-provenance" does ([LIT-1110](../literature.d/LIT-1110.md)), loses which inputs suffice
  together.
- **That where-provenance is the provenance worth keeping.** It is the
  notion that depends on how the query was written.
- **Anything for nonmonotone queries.** The authors do not know whether a
  semantic characterization of why-provenance is "well behaved on anything
  beyond than SPJU queries".

## Connections

- [QUESTION-105](../questions.d/QUESTION-105.md) asks what an inquiry must retain to support a family of
  revisions. A minimal witness basis is one candidate for deletion of
  facts, and [THEORY-373](THEORY-373.md) gives the stronger, algebraic form of the same
  idea. Neither is the selection over remainders of [THEORY-353](THEORY-353.md) or the base
  of [THEORY-347](THEORY-347.md); neither chooses what to give up.
- [CASE-089](../cases.d/CASE-089.md) and [CLAIM-293](../claims.d/CLAIM-293.md): a witness basis records which supports suffice,
  not how strong they are, so it is the support topology [CLAIM-293](../claims.d/CLAIM-293.md) says
  does not fix revision.
- [CLAIM-303](../claims.d/CLAIM-303.md): why-provenance here is a query rerun on demand from Q and D,
  the reconstruct side of [CLAIM-303](../claims.d/CLAIM-303.md)'s trade.
- [CLAIM-306](../claims.d/CLAIM-306.md): both notions are defined only for what is in the output, so
  neither says anything about a conclusion of absence.

## Note of 2026-10-20: minimal witnesses, proved invariant

Proved for the promotion audit (batch 053, [ADR-047](../decisions.d/ADR-047.md) v2), for SPJU relational
queries.

1. **Witnesses are semantic.** A witness for an output tuple t is a
   subinstance J ⊆ D with t ∈ Q(J). Equivalent queries therefore have the
   same witnesses.
2. **The witness basis covers them.** A union of conjunctive queries with
   comparisons of variables to constants is monotone. If t ∈ Q(J), some
   valuation of one disjunct maps its body into J and produces t. Its image
   is a member of the witness basis and lies inside J. Conversely,
   monotonicity makes every member of the basis a witness.
3. **Minimal witnesses are the minimal basis members.** Every witness
   contains a basis member and every basis member is a witness. So the
   inclusion-minimal witnesses are exactly the inclusion-minimal members of
   the basis, and by step 1 they do not depend on how the query is written.
   This is the paper's Theorem 3. The proof uses only monotonicity.
4. **Where-provenance is not invariant.** The queries "select x from R(x)
   where x = 5" and "select 5 from R(x) where x = 5" are equivalent. In the
   first the output 5 is copied from R; in the second it is a constant with
   no source location.

The paper's rewrite-system results (Lemma 1, Proposition 2) are not
re-derived, since the rules are not given. Whether traceability is
necessary as well as sufficient is also left open. Both are
[QUESTION-tmpo255i](../questions.d/QUESTION-tmpo255i.md).
