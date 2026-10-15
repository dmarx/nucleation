---
status: Active
status_note: >-
  read in full 2026-10-15 from the authors' camera-ready of the PODS 1995 extended
  abstract (pp. 95–104), linked from Alberto Mendelzon's University of Toronto publications
  page and fetched from www.cs.toronto.edu/pub/papers/pods95LMSS.ps.Z, because ACM's
  open-access PDF refused requests from this environment. Worth reading as the paper
  that reduces reuse of stored views to query containment: a view can be used in
  an equivalent rewriting exactly when its body maps homomorphically into the query's,
  a minimal rewriting is no longer than the query, and finding a rewriting, a shorter
  one or one using only the views is NP-complete for conjunctive queries without
  comparisons (Π2p-complete for existence with comparisons in both), with two independent
  sources of hardness ([THEORY-tmpxw8fg](../theory.d/THEORY-tmpxw8fg.md)). For [CLAIM-303](../claims.d/CLAIM-303.md) and [CLAIM-308](../claims.d/CLAIM-308.md) it shows that recognizing
  that stored answers cover a new question is a worst-case NP-complete search in
  the size of the question and the stored items' definitions, not in the stored
  data, so the per-use cost c_a has a recognition term that varies with the question
  and the store; it says nothing about prose arguments, contained (partial) reuse,
  or whether recognized reuse pays.
title: Answering Queries Using Views
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Filed, not read. Citation checked on 2026-10-15: PODS 1995. Crossref gives 22
    May 1995. Not held in the Anthology of the SOTA: a grep of its record/ (clone
    of 2026-10-15, commit d1573d2) for the title and authors found nothing. Read
    the same day (NOTE-tmp7vihx).
tags:
- databases
- logic
date: '2026-10-15'
published: '1995-05-22'
doi: 10.1145/212433.220198
first_author: Levy
keywords: []
implementations: []
summary: >-
  Levy et al. (1995), PODS 1995. For conjunctive queries and views, a view can be
  used in an equivalent rewriting of a query exactly when there is a containment
  mapping (a homomorphism of bodies) from the view into the query, so every possible
  use of a stored view is found among those mappings. Without comparison predicates,
  a minimal rewriting needs no more literals than the query and no new variables,
  which puts the search in NP; deciding whether some rewriting uses a given set
  of views (with comparisons only in the query), whether a rewriting with fewer
  than k literals exists, and whether a rewriting using only the views exists are
  each NP-complete, and with comparisons in both query and views existence is Π2p-complete.
  The hardness has two independent sources, the number of mappings and the choice
  of which query literals to drop, and a polynomial algorithm removes the redundant
  literals for a given mapping, exactly under stated conditions. Only equivalent
  rewritings are studied; contained rewritings, the cost of the resulting plan and
  the size of view collections are outside it.
---

# LIT-tmp3l2ha: Answering Queries Using Views

Levy, A. Y., Mendelzon, A. O., Sagiv, Y. and Srivastava, D. (1995). Answering queries using views (extended abstract). In *Proc. PODS 1995*, pp. 95–104. DOI 10.1145/212433.220198

## Key takeaways

Read in full ([NOTE-tmp7vihx](../notes.d/NOTE-tmp7vihx.md)). For conjunctive queries and views, a view can be used in an equivalent rewriting of a query exactly when there is a containment mapping (a homomorphism of bodies) from the view into the query, so every possible use of a stored view is found among those mappings. Without comparison predicates, a minimal rewriting needs no more literals than the query and no new variables, which puts the search in NP; deciding whether some rewriting uses a given set of views (with comparisons only in the query), whether a rewriting with fewer than k literals exists, and whether a rewriting using only the views exists are each NP-complete, and with comparisons in both query and views existence is Π2p-complete. The hardness has two independent sources, the number of mappings and the choice of which query literals to drop, and a polynomial algorithm removes the redundant literals for a given mapping, exactly under stated conditions. Only equivalent rewritings are studied; contained rewritings, the cost of the resulting plan and the size of view collections are outside it.

## Why this is here

[CLAIM-303](../claims.d/CLAIM-303.md) and [CLAIM-308](../claims.d/CLAIM-308.md) price reuse of a filed argument as access plus verification. This paper gives the complexity of recognizing that stored views answer a new query exactly: NP-complete for conjunctive queries, growing with the query and view definitions, not the stored data.
