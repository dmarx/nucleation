---
status: Unavailable
status_note: >-
  filed 2026-10-15, not read. Looked for a lawful full text on 2026-10-15; one exists,
  as the publisher's PDF in the ACM Digital Library (dl.acm.org/doi/pdf/10.1145/290941.290995),
  but it was found and could not be fetched, so no NOTE is filed and it is Unavailable
  until a copy is supplied, not on merit. Unpaywall and OpenAlex report it closed
  (oa_status closed, no OA or repository location); Semantic Scholar gives openAccessPdf
  status CLOSED. Direct requests to dl.acm.org, for both the landing page and the
  PDF, were refused with HTTP 403 by Cloudflare's bot challenge, by curl and by
  a web-fetch tool alike, so whether ACM now serves this item free could not be
  confirmed. The Wayback Machine reports a capture of that PDF URL (2023-12-04)
  and of the landing page (2024-08-13), but web.archive.org was unreachable from
  this environment throughout the session (connections reset, about twenty attempts
  over fifteen minutes). OpenAlex also lists two CiteSeerX records (10.1.1.12.1003,
  10.1.1.51.5102); CiteSeerX now redirects to the Wayback Machine, which was unreachable,
  and CiteSeerX is a crawler, not the authors' or an institution's copy. Mitra's
  pages (isical.ac.in/~mandar, mandarm.github.io) list no publications; Cornell
  eCommons holds Cornell SMART technical reports by Singhal and Mitra (e.g. 1813/7217,
  1813/7186) but none of this paper; Singhal's AT&T page of the time (research.att.com/~singhal/)
  survives only as a link; web searches found no author-posted, institutional or
  course-hosted copy. What was seen is the abstract, on the SIGIR '98 abstracts
  page that Moffat hosts at the University of Melbourne (people.eng.unimelb.edu.au/ammoffat/sigir98/abstracts/mitra.html),
  read through a web-fetch tool that paraphrases, so no quotation from it was checked
  by script. As paraphrased, the abstract says that adding terms to short queries
  by ad hoc feedback improves retrieval, that the authors refine the set of documents
  feedback is drawn from, first with manually formulated Boolean filters with proximity
  constraints and then with a fully automatic method based on term co-occurrence,
  and that this "often prevents the query drift caused by blind expansion", improving
  average precision and precision in the top twenty documents, with the automatic
  method competitive with the best manual one at little added cost. So the paper
  uses the term query drift and places its cause in blind (pseudo-relevance) expansion;
  that the mechanism is non-relevant documents in the top-ranked feedback set, the
  collections used and the sizes of the gains are not confirmed and need the full
  text. Nothing seen contradicts the entry's summary or what TERM-tmpywff6 and CLAIM-tmps7uw8
  cite it for: query drift with the information need held fixed.
title: Improving automatic query expansion
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Filed, not read. Citation checked against Crossref on 2026-10-15: Crossref gives
    August 1998, so `published:` is the first of the month. Not held in the Anthology
    of the SOTA: a grep of its record/ (clone of 2026-10-15, commit d1573d2) for
    the authors and the title found nothing. Set Unavailable the same day under
    ADR-041, the search having found no lawful copy that could be fetched.
tags:
- information-retrieval
date: '2026-10-15'
published: '1998-08-01'
doi: 10.1145/290941.290995
first_author: Mitra
keywords:
- query expansion
- pseudo-relevance feedback
- query drift
- information retrieval
implementations: []
summary: >-
  Mitra, Singhal and Buckley (1998), SIGIR. Studies why automatic query expansion
  by pseudo-relevance feedback sometimes hurts: when the top-ranked documents are
  off-topic, expansion drifts the query away from the information need. Proposes
  ways to keep expansion on the original query.
supports:
- CLAIM-tmps7uw8
---
<!-- inactive-ok-file: CLAIM-tmps7uw8 — Proposed; open claims and accounts cited as open, nothing here rests on their being settled -->

# LIT-tmpzz8jj: Improving automatic query expansion

Mitra, M., Singhal, A. and Buckley, C. (1998). Improving automatic query expansion. In *Proceedings of the 21st Annual International ACM SIGIR Conference on Research and Development in Information Retrieval*, 206–214. DOI 10.1145/290941.290995

Not read. The summary is drawn from the abstract or from what the work is
standardly cited for. A reading should check it first.

## Why this is here

The owner suspected at U21 that agent harnesses rediscover older information retrieval. A21 cited relevance feedback and the query-drift problem. This is a standard source for query drift, which [TERM-tmpywff6](../terms.d/TERM-tmpywff6.md) distinguishes from question drift and [CLAIM-tmps7uw8](../claims.d/CLAIM-tmps7uw8.md) builds on. Rocchio's relevance feedback (1971) is the older source and is not registered, having no DOI.
