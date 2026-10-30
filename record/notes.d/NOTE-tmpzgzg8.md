---
status: Read
paper: LIT-1079
title: 'Mitra, Singhal & Buckley — Improving automatic query expansion'
version: 1
history:
- version: 1
  date: '2026-10-30'
  note: >-
    Read in full on 2026-10-30 from the SciSpace (typeset.io) copy
    (https://typeset.io/pdf/improving-automatic-query-expansion-cmfn0svc0j.pdf),
    which the owner ruled a lawful copy on 2026-10-30. It is the ACM
    proceedings text: nine pages numbered 206–214, the ACM permission
    line "SIGIR'98, Melbourne, Australia © 1998 ACM 1-58113-015-5", the
    three authors at Cornell, AT&T Labs–Research and Sabir Research. Its
    text layer is out of order, so every page was read from images
    rendered at 110 dpi: the abstract, all six sections, Tables 1–8,
    Figures 1–3 and the references. The bar charts of Figures 1–3 were
    read for their shape only; their values are not legible at that
    resolution, and Table 8 gives the counts. None of the cited works was
    read.
date: '2026-10-30'
summary: >-
  Pseudo-relevance feedback expands a short query with terms from its
  top-ranked documents, and hurts when those documents are off-topic:
  the authors name the harm query drift, "the alteration of the focus of
  a search topic caused by improper expansion". Reranking the top
  documents before feedback, by hand-made Boolean filters or by an
  automatic score that rewards matches on uncorrelated query terms,
  raises average precision over plain expansion on TREC 3–6, by 7–22%
  for the manual and 6–13% for the automatic method, and cuts the
  queries that expansion hurts from 64 of 199 to 43 or 50.
---
<!-- inactive-ok-file: CLAIM-301 — Proposed; the claim this reading bears on, cited as open -->

# NOTE-tmpzgzg8: Mitra, Singhal & Buckley — Improving automatic query expansion

## Contribution

It showed that query drift in blind feedback can be reduced without user
input by choosing better feedback documents, and that a cheap automatic
reranker does about as well as hand-written Boolean filters. It also
measured drift: Table 8 counts, by how many relevant documents a query
first retrieves, how many queries expansion hurts.

## Key insight

Blind feedback assumes the top documents are relevant, so the expansion
inherits whatever they are about. When most of them match only one
aspect of the query, the added terms pull the query toward that aspect
and away from the whole topic. Documents that cover all the query's
independent aspects make a better feedback set.

## Assumptions

- **Short queries.** TREC topics' "Description" field only (queries
  151–300), with "Title" added for TREC-6 (p. 209): the casual user's
  short query is the target.
- **The baseline.** SMART *Lnu.ltu* retrieval of 1,000 documents; the top
  20 assumed relevant, 501–1000 non-relevant; Rocchio with α = 8, β = 8,
  γ = 8, adding 25 words and 5 phrases (p. 209).
- **Aspects.** A query's aspects are disjunctions of words, conjoined
  (manual filters); or, automatically, each non-stop word is an aspect,
  discounted when it co-occurs with a rarer matching term in the top
  1,000 documents (Eqs. 2–3).

## Key results

- **The problem (p. 206).** For TREC query 203 ("What is the economic
  impact of recycling tires?") only 4 of the top 20 documents are
  relevant; most discuss recycling of plastics and glass, so expansion
  adds 'plastic' and 'glass' and the query "begins to look more like a
  query about plastics and general recycling rather than tire
  recycling". Over 199 queries, plain expansion lowered performance for
  "about one-third". The aim is "to prevent query drift — the alteration
  of the focus of a search topic caused by improper expansion".
- **Baseline expansion (Table 2).** Average precision rises by 39.1%,
  32.3% and 21.2% on TREC 3, 4 and 5 and falls 0.3% on TREC 6.
- **Manual Boolean filters (§§2, 4.1, Tables 3–4).** Written by one of the
  authors. Reranking the top T documents by filter before feedback
  improves on the baseline expansion by 4.5% to 18.4% (binary filters)
  and about 7% to 24% (fuzzy filters). Proximity windows add little;
  reranking 200–500 documents is best.
- **Automatic reranking (§§3, 4.2, Tables 5–6).** With term correlations
  (Eq. 3), reranking only the top 50–100 is best, since the automatic
  filter admits non-relevant documents as T grows.
- **Comparison (Table 7).** Average precision over baseline expansion:
  fuzzy Boolean 18%, 7%, 8%, 22%; automatic with correlations 8%, 6%,
  9%, 13% (TREC 3–6). Precision at 20 is mixed: the automatic method
  loses 1% on TREC 5.
- **Drift measured (§5, Table 8, Figs. 1–3).** Queries binned by relevant
  documents in the initial top 20. Expansion hurts mainly where few are
  relevant: of 19 queries with two relevant in the top 20, baseline
  expansion hurts 12, manual reranking 6. Totals hurt by expansion: 64 of
  199 (baseline), 43 (manual), 50 (automatic). "The baseline histogram
  confirms that query drift is indeed a problem, but perhaps not as
  severe as feared" (p. 212). On TREC 4 the baseline matches Xu and
  Croft's local context analysis (11-pt precision 0.32 against 0.31).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Blind expansion causes query drift when the top-ranked documents are mostly non-relevant | moderate | the query 203 case; Table 8 and Figs. 2–3, harm concentrated in queries with few relevant documents initially |
| C2 | Reranking the feedback set with Boolean filters reduces drift and improves retrieval | moderate to strong | Tables 3–4 and 7, four TREC tasks; filters written by one author |
| C3 | A fully automatic reranker using term co-occurrence performs about as well as manual filters | moderate | Table 7; parameters chosen after the fact for good performance across tasks |
| C4 | Reranking alone does not raise precision; reranking followed by expansion does | moderate | Fig. 1 against Fig. 3 |

No significance tests are reported.

## Method

Retrieve with the user's query; rerank the top T (say 50) by a new score
from additional relevance indicators; take the top K (say 20) of the new
ranking as the feedback set for Rocchio expansion; retrieve with the
expanded query (p. 207). The new score is either the sum of maximum idf
per Boolean aspect, a fuzzy-Boolean form (Eq. 1), or the idf of matching
query terms down-weighted by their co-occurrence with rarer matched terms
(Eq. 3), optionally within the best w-word window.

## Concepts

- **Adhoc or blind feedback** — pseudo-relevance feedback: the top
  documents of the initial retrieval are assumed relevant "without any
  intervention by the user" and used to expand the query (p. 206).
- **Query drift** — "the alteration of the focus of a search topic caused
  by improper expansion" (p. 206). The search topic, the TREC statement of
  the information need, is fixed; it is the expanded query whose focus
  moves.
- **Query aspects** — the independent concepts a query needs a document
  to cover; a document matching several aspects is preferred to one
  matching many words of one aspect (pp. 207–208).

## Connections

It builds on Rocchio's relevance feedback, Buckley, Singhal and Mitra's
SMART runs at TREC, and Hearst's Boolean constraints for precision on
short queries, and compares itself with Xu and Croft's local context
analysis (SIGIR 1996).

## Bearing on the record

- **[TERM-056](../terms.d/TERM-056.md): fully.** The term cites this paper for query drift, "where
  the need stays fixed and the search leaves it". That is what the paper
  says. Its definition is "the alteration of the focus of a search topic
  caused by improper expansion" (p. 206). In its example the topic (tire
  recycling) stays as stated, and the expanded query comes to "look more
  like a query about plastics and general recycling". The paper never
  considers the need itself changing. So nothing here blurs the
  distinction [TERM-056](../terms.d/TERM-056.md) draws; the paper supplies one side of it.
- **[CLAIM-301](../claims.d/CLAIM-301.md): partly.** The claim's body cites this paper only for the
  term query drift, as "the IR literature's", and its note of 2026-10-29
  counts the source as Unavailable and unread. That much is now met: the
  term and its cause are here, and the record's earlier reading of the
  abstract holds. The paper has a mechanism close to the claim's own:
  documents retrieved under one aspect supply the terms that pull the
  query further toward that aspect. But it is a single round of feedback
  with the need held fixed, so it gives no evidence that the question
  being investigated drifts, which is [CLAIM-301](../claims.d/CLAIM-301.md)'s thesis. The claim's
  other open items, a filed CASE for the exchange's drift and the matched
  study its `defeated_if` names, are untouched.
- **[LIT-1079](../literature.d/LIT-1079.md)'s summary.** Its first half holds: expansion hurts when
  most of the top-ranked documents are off-topic. Its second half, "ways
  to keep expansion on the original query", is loose. The remedy is to
  refine the set of feedback documents by reranking, with the query's
  terms entering only as the aspects the reranker checks for. The LIT's
  summary is corrected on that point.
- No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- **One collection family and one system.** TREC 3–6 ad hoc tasks with
  SMART; no other retrieval model or user study.
- **Parameters chosen on the test queries.** Table 7's settings were
  picked as giving "reasonably good performance across different tasks",
  after the fact, and no significance tests are given.
- **Manual filters by an author**, not by users, so the manual numbers are
  an upper bound for what casual users would supply.
- **"Query drift"** is defined by its cause and measured by its effect:
  queries whose average precision falls after expansion. Drift that
  leaves precision unchanged is not counted.

## Open questions

- Does the reranking help with longer queries, or with feedback over
  several rounds, where drift could compound?
- Can the aspects of a query be identified more accurately than by term
  co-occurrence, as the authors propose (§6)?
