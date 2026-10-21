---
status: Unavailable
status_note: >-
  filed 2026-10-21; on 2026-10-21 a lawful full text was sought and none was reached, so no NOTE is filed. Open copies exist, so this failed on access, not availability. The authors' working paper is in the University of Michigan's Deep Blue repository (handle 2027.42/154046, files reputation-v11Submit.pdf and manipulation-final.pdf, by web search), but every Deep Blue URL tried (handle page, item page, bitstream and REST API) returned a Cloudflare browser check to this client, and WebFetch got HTTP 403. A copy on James Siderius's MIT LIDS site (siderius.lids.mit.edu/wp-content/uploads/sites/36/2021/09/manipulation.pdf, by web search) failed DNS resolution from this client, and Mohamed Mostagir's Michigan page (public.websites.umich.edu/~mosta) returned 403; mostagir.engin.umich.edu was refused by the proxy. CORE holds Deep Blue's copy (core.ac.uk/download/287611458.pdf), which returned 403 to curl and to WebFetch, and CORE's API withholds the full text from public users. SSRN (doi:10.2139/ssrn.3474643, which Unpaywall lists as the only open location) returned 403. Unpaywall and OpenAlex list the Management Science article as closed, Semantic Scholar had no record of its DOI, and arXiv has no copy. A copy the owner supplies would let it be read.
title: 'When Is Society Susceptible to Manipulation?'
version: 2
history:
- version: 1
  date: '2026-10-21'
  note: >-
    Filed, not read. Citation checked against Crossref, OpenAlex and arXiv on 2026-10-21. `published:` is the first of January 2019, from the SSRN working paper under the same title, which Crossref dates to 2019 with no month (doi:10.2139/ssrn.3474643), taking the earlier date per ADR-002. OpenAlex dates the journal article online to 21 January 2022; the issue is October 2022. The exchange's citation was right.
- version: 2
  date: '2026-10-21'
  note: >-
    Status Deferred → Unavailable under ADR-041. At the owner's request to read the proposed works, a lawful copy was sought on 2026-10-21 in Unpaywall, OpenAlex, Semantic Scholar, CORE, arXiv, SSRN, Deep Blue and the authors' pages. Copies exist in Deep Blue (mirrored by CORE) and on Siderius's site, but none could be fetched by this client (a Cloudflare check, 403s, a DNS failure); the status note lists every route. Failed on access, not availability.
tags:
- network-science
- game-theory
- social-science
date: '2026-10-21'
published: '2019-01-01'
doi: '10.1287/mnsc.2021.4265'
first_author: 'Mostagir'
keywords:
- 'social learning'
- 'manipulation'
- 'wisdom of the crowd'
- 'network centrality'
- 'misinformation'
implementations: []
summary: >-
  Mostagir, Ozdaglar & Siderius (2022). In a social-learning model a principal manipulates agents' beliefs by using the same forces that produce the wisdom of the crowd; characterizes the social norms and network structures susceptible to such manipulation, the conditions under which a network is impervious to it, and a new centrality measure.
---
<!-- inactive-ok-file: CLAIM-tmpjo2zr — Proposed; filed from the same exchange, named as the entry this work bears on -->
# LIT-tmp8x4zb: When Is Society Susceptible to Manipulation?

Mostagir, M., Ozdaglar, A. & Siderius, J. (2022). When Is Society Susceptible to Manipulation? *Management Science* 68(10): 7153–7175. doi:10.1287/mnsc.2021.4265. Earlier: SSRN working paper, 2019 (doi:10.2139/ssrn.3474643).

Not read: no copy was reached (see the status note). The summary is drawn
from the abstract or from what the work is standardly cited for. A
reading should check it first.

## Why this is here

A25 made it a first-priority reading and "possible novelty challenge": it "bears directly on whether our interpretation–authority model adds something beyond existing network influence models." Bears on [QUESTION-117](../questions.d/QUESTION-117.md) and [CLAIM-330](../claims.d/CLAIM-330.md), and on [CLAIM-tmpjo2zr](../claims.d/CLAIM-tmpjo2zr.md).
