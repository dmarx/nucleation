---
number: 383
status: Active
formerly:
- THEORY-tmprwm4f
title: 'On one Apache and Informix server answering cheap indexed selections over 1000 pages, a page whose query result was stored in the DBMS and refreshed on every update answered more slowly than one recomputed on each request at five or more updates per second, which the authors explain by reading the stored result costing about as much as recomputing it and its refresh loading the same DBMS, while a finished page stored at the web server and rewritten on every update answered 10 to 230 times faster than either'
version: 2
history:
- version: 2
  date: '2026-10-30'
  note: >-
    Narrowed first. 'whenever updates arrived' was contradicted by the
    authors' own conclusion that the DBMS-stored policy beat recomputation
    'only for a very limited number of cases': 100 pages, or under 5
    updates per second (NOTE-908). It is dropped as kind 3 of ADR-047's
    routing. The title now says five or more updates per second over 1000
    pages, attributes the causal clause to the authors, and the summary is
    corrected to match. Old title: "On one Apache and Informix server
    answering cheap indexed selections, a page whose query result was
    stored in the DBMS and refreshed on every update answered more slowly
    than one recomputed on each request whenever updates arrived, because
    reading the stored result cost about as much as recomputing it and its
    refresh loaded the same DBMS, while a finished page stored at the web
    server and rewritten on every update answered 10 to 230 times faster
    than either". Promoted to Active under ADR-065, at the status review's
    ruling (the owner delegated these rulings). The title reports what one
    study, read in full in NOTE-908, measured, with the study's hedges
    kept, and nothing in the record contradicts it. The old promote_when
    read: "A measurement on another database and web stack, with native
    materialized views and queries of graded cost, showing that a stored
    query result kept current on every update loses to recomputation
    exactly when reading the stored result costs about as much as
    recomputing it and the refresh runs on the resource that serves
    requests, and wins otherwise. More runs on one testbed with cheap
    indexed selections cannot settle it, since they only repeat the case
    held; nor can the paper's Eq. 9, whose values were never computed
    against measurement." Its demand for a measurement on another database
    and web stack asks for an independent test beyond the one testbed the
    title reports, and moves to QUESTION-347.
tags:
- databases
- operations-research
date: '2026-10-15'
source:
- LIT-1118
summary: >-
  Labrinidis and Roussopoulos (2000), [LIT-1118](../literature.d/LIT-1118.md), read in [NOTE-908](../notes.d/NOTE-908.md). Three
  ways to serve a database-generated page under online updates, with no stale
  reads allowed: compute on request, store the query result in the DBMS, or
  store the finished page at the web server. A cost model sums access and
  update costs by frequency; the per-page selection problem is stated and not
  solved. On their testbed the page stored at the web server won at every load,
  and the result stored in the DBMS lost to recomputation at five or
  more updates per second. The reading the evidence does not support: that storing an answer
  pays whenever it is reused enough. Where it is stored decided the outcome,
  and the generalization to other systems is the authors' expectation, not a
  measurement.
bears_on:
- QUESTION-114
---

# THEORY-383: On one Apache and Informix server answering cheap indexed selections over 1000 pages, a page whose query result was stored in the DBMS and refreshed on every update answered more slowly than one recomputed on each request at five or more updates per second, which the authors explain by reading the stored result costing about as much as recomputing it and its refresh loading the same DBMS, while a finished page stored at the web server and rewritten on every update answered 10 to 230 times faster than either

## Source

Labrinidis and Roussopoulos (2000), [LIT-1118](../literature.d/LIT-1118.md), SIGMOD 2000, read in full in
[NOTE-908](../notes.d/NOTE-908.md) from the authors' camera-ready copy. The cost model is Section 3,
the measurements Section 4.

## What was actually shown

**The setting.** A WebView is a page built from a query on base tables. Every
stored copy is refreshed on every update: "In this paper, we also assume a no
staleness requirement, i.e. the WebViews must always be up to date." There is
no storage limit and no cost for creating a stored copy.

**The measurements.** WebMat ran Apache 1.3.6 with mod_perl and Informix 9.14
on one Sun UltraSparc-5, with 1000 pages over 10 tables, each a selection on an
indexed attribute returning 10 tuples. Each run used one policy for every
page. Pages stored at the web server answered "consistently at least an order
of magnitude (10 - 230 times) less than those of the virt or matdb policies",
at 10 to 100 requests per second. With no updates, results stored in the DBMS
and recomputation were close, because "the cost of accessing them is about the
same as the cost of generating them from scratch". With updates the stored
results lost: at 25 requests per second and 5 updates per second recomputation
was 63.53% faster, and across 0 to 25 updates per second the "virt policy
gives 56% - 93% faster query response times compared to the matdb policy in
the presence of updates." The DBMS-stored policy won only with 100 pages, or
under 5 updates per second.

**Upkeep falls on others.** With 500 recomputed and 500 web-stored pages,
updates to the web-stored pages raised the recomputed pages' response time by
236%, against 27% when the same updates fell on the recomputed pages, because
rewriting stored pages runs queries in the shared DBMS.

## What this does not say

- **That storing in the DBMS loses in general.** The queries were cheap
  indexed selections. With 10% of pages made joins and 100 pages, the DBMS
  policy was 3.5 times faster than recomputation with no updates. The
  authors expect the same result on other products that store views as
  tables; that was not tested.
- **That the per-page choice was solved.** The selection problem is stated
  and no algorithm is given. Mixed plans were not chosen by the model.
- **Anything about staleness.** Stale reads are excluded. Minimum staleness,
  the delay from update to reply, is defined and sketched, never measured.
- **That the cost model predicts the numbers.** Eq. 9's terms were matched to
  the direction of the measured effects, never evaluated against them.
- **Anything about build cost or space**, both outside the model.

## Connections

- For [QUESTION-114](../questions.d/QUESTION-114.md) it has query savings and upkeep weighted by frequency, the
  shape of Gupta 1997 ([LIT-1091](../literature.d/LIT-1091.md)), plus where the copy lives; no staleness term,
  no build cost, no algorithm. [THEORY-332](THEORY-332.md) and [THEORY-350](THEORY-350.md) come nearer.
- The 236% result is a measured form of [THEORY-350](THEORY-350.md)'s finding that upkeep is
  not additive: here because stored and unstored items share a resource.
- For [CLAIM-303](../claims.d/CLAIM-303.md) it is a case where c_a ≈ c_r, so the claim's condition
  c_r > c_a + u fails whatever the reuse.
- Its successor, [LIT-1105](../literature.d/LIT-1105.md) ([THEORY-382](THEORY-382.md)), drops the no-staleness assumption
  and gives an online selection algorithm.
