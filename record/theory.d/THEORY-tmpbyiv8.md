---
status: Proposed
promote_when: >-
  A read proof of the paper's Theorems 1–3 and Proposition 2 for its rewrite
  system, which this paper states without proof and without giving the rules
  (a full or journal version by the authors would do), or an independent
  proof that the minimal witnesses of a positive conjunctive query with
  equality conditions are the same for every equivalent query. More examples
  cannot settle it, and the where-provenance half does not wait on it: that
  where-provenance differs between equivalent queries is already shown by
  the paper's counterexamples.
title: "For positive queries over a tree data model that covers SPJU relational queries, why-provenance taken as the witness basis, one set of matched source facts per derivation, is preserved by query rewriting and its minimal witnesses are the same for equivalent queries with equality conditions, while where-provenance, the source location a value was copied from, can differ between equivalent queries and is preserved by rewriting only for traceable queries"
version: 1
tags:
- databases
- logic
date: '2026-10-15'
source:
- LIT-tmp8m5l3
summary: >-
  Buneman, Khanna and Tan (2001), [LIT-tmp8m5l3](../literature.d/LIT-tmp8m5l3.md), read in [NOTE-tmpxim6c](../notes.d/NOTE-tmpxim6c.md). Two
  meanings of the provenance of output data: why it is there (the witness
  basis, the source structures matched by each valuation that produces it)
  and where a value came from (the source paths bound to the output
  variable). The first is preserved by the paper's rewrite system and, cut
  down to minimal witnesses, agrees across equivalent queries with equality
  conditions; the second is shown by example to depend on how the query is
  written. Proofs are omitted. It is not a theory of revision: additions to
  the source, negation, aggregation and strengths of support are all outside it.
---

# THEORY-tmpbyiv8: For positive queries over a tree data model that covers SPJU relational queries, why-provenance taken as the witness basis, one set of matched source facts per derivation, is preserved by query rewriting and its minimal witnesses are the same for equivalent queries with equality conditions, while where-provenance, the source location a value was copied from, can differ between equivalent queries and is preserved by rewriting only for traceable queries

## Source

Buneman, Khanna and Tan (2001), [LIT-tmp8m5l3](../literature.d/LIT-tmp8m5l3.md) (ICDT 2001, LNCS 1973,
pp. 316–330), read in [NOTE-tmpxim6c](../notes.d/NOTE-tmpxim6c.md) from the authors' postprint: Definitions
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
  Tannen's "why-provenance" does ([LIT-tmpjckak](../literature.d/LIT-tmpjckak.md)), loses which inputs suffice
  together.
- **That where-provenance is the provenance worth keeping.** It is the
  notion that depends on how the query was written.
- **Anything for nonmonotone queries.** The authors do not know whether a
  semantic characterization of why-provenance is "well behaved on anything
  beyond than SPJU queries".

## Connections

- [QUESTION-105](../questions.d/QUESTION-105.md) asks what an inquiry must retain to support a family of
  revisions. A minimal witness basis is one candidate for deletion of
  facts, and [THEORY-tmpeqxfa](THEORY-tmpeqxfa.md) gives the stronger, algebraic form of the same
  idea. Neither is the selection over remainders of [THEORY-353](THEORY-353.md) or the base
  of [THEORY-347](THEORY-347.md); neither chooses what to give up.
- [CASE-089](../cases.d/CASE-089.md) and [CLAIM-293](../claims.d/CLAIM-293.md): a witness basis records which supports suffice,
  not how strong they are, so it is the support topology [CLAIM-293](../claims.d/CLAIM-293.md) says
  does not fix revision.
- [CLAIM-303](../claims.d/CLAIM-303.md): why-provenance here is a query rerun on demand from Q and D,
  the reconstruct side of [CLAIM-303](../claims.d/CLAIM-303.md)'s trade.
- [CLAIM-306](../claims.d/CLAIM-306.md): both notions are defined only for what is in the output, so
  neither says anything about a conclusion of absence.
