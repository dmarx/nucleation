---
status: Proposed
title: 'A repository''s documented machine interface to an open-access full text is a lawful route in its own right, and a bot check on the repository''s website does not bar it; Europe PMC''s REST API is the first such route'
version: 1
tags:
- record
date: '2026-11-17'
summary: >-
  On the owner's ruling of 2026-11-17 ("Europe PMC is fine"). ADR-074 and
  the read-and-file skill say to stop at any bot check and never work
  around one. On 2026-11-15 a reader met challenges at europepmc.org and
  PMC for a CC BY review, then fetched the same full text from Europe
  PMC's documented REST API on www.ebi.ac.uk. The lead accepted the route
  and left it to the owner, who confirmed it. This decision says why that
  is not a workaround: the API is the repository's own published route
  for machine access to the text, not a way past the check that guards
  its website. It adds the route to the skill's step 5. The bar on
  working around a check stands. A route counts only if the repository
  documents it for machine access and the text it serves is open access.
---
<!-- inactive-ok-file: LIT-tmp3d5f9 NOTE-tmpgrvfy — new; the first application, filed in the same pull request -->

# ADR-tmpukj8n: A repository's documented machine interface to an open-access full text is a lawful route in its own right, and a bot check on the repository's website does not bar it; Europe PMC's REST API is the first such route

## Context

ADR-074 fixes which copies count as lawful and how a blocked one is filed.
The read-and-file skill adds: "Stop at any bot check ... Never try to get
around one. Retrying the same host doesn't help either."

On 2026-11-15 a reader sought Márquez et al. (2023), a CC BY review in
Nanophotonics, as the stand-in for an unidentified source on holographic
multiplexing. Every web copy stopped the fetch:
- europepmc.org showed a Cloudflare challenge;
- PMC showed a reCAPTCHA;
- De Gruyter returned an empty HTTP 202;
- the Alicante repository timed out.

The reader then fetched the full text from Europe PMC's REST API,
`https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11501936/fullTextXML`.
The lead accepted the reading and set out the route in the curation entry
for the owner to overrule. On 2026-11-17 the owner confirmed it: "Europe
PMC is fine".

Without a decision, the next reader faces the same question and has only
the skill's flat rule to go on. That rule would make the work `Unfetched`.

## Decision

- **A documented machine interface is a route, not a workaround.** A
  repository that serves open-access full text may also publish an
  interface for programs to fetch it: an API, a bulk or OAI service, a
  documented download endpoint. Reading through that interface is lawful
  even when the repository's website shows a bot check. The check guards
  the website, and the interface is the repository's own answer to machine
  access. It does not get past that check.
- **Three conditions, all required:**
  - the repository documents the interface for machine access;
  - the text served is open access, or otherwise lawful under ADR-074;
  - the interface itself answers. If it shows a check, a rate limit or a
    refusal, stop there as the skill says, and the work is `Unfetched` at
    that address.
- **What stays barred.** Nothing here permits changing headers, using
  proxies or mirrors, scraping around a challenge, or using an
  undocumented endpoint. Those are workarounds, and they remain barred. A
  refusal by this session's own permission system or network policy is
  still an obstacle of this client (ADR-074, item 4).
- **The first named route is Europe PMC's REST API**, for articles with a
  PMCID that Europe PMC serves as open access. Others are added to the
  skill's step 5 as readers meet them, each with its documentation.
- **The NOTE's history names the route**, giving the API's address, the
  checks met on the way, and that this decision admitted it.

## First application

Márquez et al. (2023), LIT-tmp3d5f9, NOTE-tmpgrvfy (Skimmed), filed in the
same pull request. Its histories now cite this decision.

## Alternatives

- **Leave it to the owner each time.** That is what happened here. It
  makes every such reading wait on a ruling the owner has already given
  once.
- **Treat any route past a check as a workaround.** This is the skill's
  flat rule, read literally. It would file as `Unfetched` a text the
  repository itself serves to programs, and send the owner to click a link
  the record could already read.
- **Allow any other host that serves the same text.** That is too broad.
  It would admit mirrors and scrapers, which are exactly what the bar on
  workarounds exists to keep out. The line drawn here is the repository's
  own documented interface.
