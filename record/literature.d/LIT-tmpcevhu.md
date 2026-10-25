---
status: Unavailable
status_note: >-
  filed 2026-10-25 from the owner's exchange of 2026-10-24/25, not read. A
  lawful full text was sought on 2026-10-25 and not reached: it failed on
  access, not availability. The publisher's copy at Project Euclid is free
  to read (Unpaywall and OpenAlex both list it, bronze), but Project
  Euclid's bot check (Incapsula) answered every request from this client,
  by curl and by WebFetch, with a challenge page and no PDF. The Internet
  Archive holds captures of that PDF (2026-09-17 and 2026-02-17, per its
  availability API), but web.archive.org reset every connection from this
  environment that day. Semantic Scholar was rate-limited; CORE returned
  no usable result; DTIC refused (403) and a search found no deposit of
  the OSRD report (no. 1998) the Annals text was reprinted as. The
  Springer reprint in Kotz and Johnson's Breakthroughs in Statistics is
  paywalled. It stays Unavailable until a copy is supplied, and is among
  the quickest to clear by hand: the Project Euclid PDF opens in a
  browser. No NOTE is filed.
title: 'Sequential Tests of Statistical Hypotheses'
version: 2
history:
- version: 1
  date: '2026-10-25'
  note: >-
    Filed, not read. Registered unread from the owner's exchange of
    2026-10-24/25 (the continuation of "Review PR 327 Improvements"),
    shared at
    https://chatgpt.com/share/6add7ae3-1a38-83ea-ac83-4f490e399824. At
    turn U35 the reply cites "the sequential probability ratio test" as "a
    classical connection between accumulated likelihood evidence and
    binary drift–diffusion dynamics", by search reference only and with no
    author or title; this is the paper that introduced the test. Citation
    checked against Crossref on 2026-10-25: A. Wald, The Annals of
    Mathematical Statistics 16(2), 117–186, issue June 1945 with no day,
    so `published:` is 1945-06-01, meaning June 1945 (ADR-002). OpenAlex
    lists a free copy at Project Euclid. It is distinct from Wald's book
    Sequential Analysis (1947). Crossref and OpenAlex carry no abstract,
    so the summary states what the paper is standardly cited for.
- version: 2
  date: '2026-10-25'
  note: >-
    Status Deferred → Unavailable under ADR-041, the case of a lawful copy
    this client could not fetch. On 2026-10-25 the free Project Euclid PDF
    (listed by Unpaywall and OpenAlex) returned only an Incapsula
    challenge page to curl and to WebFetch; its Internet Archive captures
    exist but web.archive.org reset every connection; Semantic Scholar,
    CORE and DTIC gave nothing usable, and no other lawful copy was found
    by search. No NOTE is filed.
tags:
- mathematical-statistics
date: '2026-10-25'
published: '1945-06-01'
doi: '10.1214/aoms/1177731118'
first_author: 'Wald'
keywords:
- 'sequential probability ratio test'
- 'sequential analysis'
- 'operating characteristic'
- 'average sample number'
implementations: []
summary: >-
  Wald (1945). Introduces the sequential probability ratio test:
  observations are taken one at a time, the log-likelihood ratio of two
  simple hypotheses is accumulated, and sampling stops when it leaves an
  interval whose bounds are set approximately from the desired error
  probabilities. The paper derives the test's operating characteristic and
  its expected number of observations, which for given error rates is
  substantially smaller than the fixed sample a test of the same strength
  needs (as standardly cited; no abstract on Crossref).
---
<!-- inactive-ok-file: CLAIM-262 — Proposed; the owner's earlier statement of the hypothesis, named, nothing here rests on it -->
# LIT-tmpcevhu: Sequential Tests of Statistical Hypotheses

Wald, A. (1945). Sequential tests of statistical hypotheses. *The Annals
of Mathematical Statistics* 16(2): 117–186. doi:10.1214/aoms/1177731118.

Not read. The summary is drawn from the abstract or from what the work
is standardly cited for. A reading should check it first.

## Why this is here

At U34 the owner hypothesized that when the perspectives advocate one of n
= 2 interpretations, a properly set-up simulation should show
drift–diffusion dynamics, and at U35 the reply cited the sequential
probability ratio test as the classical link between accumulated
likelihood evidence and binary drift–diffusion. The record already held
the link only as restated: Bogacz et al. ([LIT-569](LIT-569.md)) state that the SPRT "of
Barnard and Wald" is the fastest test for a given error rate and that its
continuum limit is the drift–diffusion model, and [THEORY-068](../theory.d/THEORY-068.md) reads it.
[CASE-155](../cases.d/CASE-155.md) part 4 shows that the replicator in log-odds form with no
feedback term is the SPRT walk. The claim [CLAIM-tmpfd9lk](../claims.d/CLAIM-tmpfd9lk.md) and the
construction [CASE-tmpvmjgd](../cases.d/CASE-tmpvmjgd.md) rest on that limit; [CLAIM-262](../claims.d/CLAIM-262.md) is the owner's
earlier, continuous statement of the hypothesis. This is the primary
source.
