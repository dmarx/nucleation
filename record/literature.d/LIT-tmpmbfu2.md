---
status: Deferred
status_note: seeded from the abstract on 2026-09-26; not read in full
title: 'The epistemology of accurate credences'
version: 1
tags:
- epistemology
- probabilistic-modeling
- philosophy-of-science
date: '2026-09-26'
published: '2025-10-29'
url: 'https://philarchive.org/rec/PETTEO-44'
first_author: 'Pettigrew'
keywords:
- 'accuracy-first epistemology'
- 'epistemic utility theory'
- 'epistemic decision theory'
- 'Probabilism'
- 'Conditionalization'
- 'Principal Principle'
implementations: []
summary: >-
  Pettigrew (2025), <https://philpapers.org/rec/PETTEO-44>. Accuracy-first epistemology — scoring credences by their closeness to the truth (following Joyce 1999) — gives a purely epistemic foundation for Probabilism, Conditionalization and the Principal Principle, and extends to non-ideal agents, the value of inquiry, and collective credences.
---

# LIT-tmpmbfu2: The epistemology of accurate credences

Richard Pettigrew (2025), *PhilArchive preprint (listed as "In Preparation" on the author's homepage)* — <https://philpapers.org/rec/PETTEO-44>

## Key takeaways

- Accuracy-first epistemology — scoring credences by their closeness to the truth (following Joyce 1999) — gives a purely epistemic foundation for Probabilism, Conditionalization and the Principal Principle, and extends to non-ideal agents, the value of inquiry, and collective credences.

*Seeded from the abstract alone, not a reading. What follows is what the work says about itself.*

Pettigrew surveys the central ideas, arguments and results of accuracy-first epistemology, also called epistemic utility theory or epistemic decision theory, and adds a long technical appendix of core proofs. He starts from Bayesian epistemology's three central norms (Probabilism, Conditionalization and the Principal Principle) and asks why they are requirements of good reasoning. He briefly sets out the pragmatic answer of Ramsey and de Finetti, then develops the purely epistemic answer due to Joyce and others, on which credences are valued for their accuracy. He argues this answer grounds norms for both ideal and non-ideal agents, accounts for the goal and value of inquiry and for norms about what to learn, informs social epistemology about group opinions and epistemic communities, and fits naturally with the pragmatic approach.

## Standing in the record

Filed from the 2026-09-26 sweep of the papers-feed tracker for philosophy: 15 seconds of active reading over 1 session. `Deferred` because nobody has read it closely here yet, not on merit.

**Priority for a deeper reading: medium — only 15 s dwell and not reachable, but it is an authoritative, up-to-date survey whose formal core connects directly to proper scoring rules in ML. Worth fetching once PhilArchive is reachable.**

What a deeper reading should check:

- Accuracy measures are strictly proper scoring rules (Brier, log score) and Bregman divergences, the same objects that underlie ML's training losses and calibration metrics. This survey is the philosophical account of why proper scoring should be the standard.
- Check the technical appendix for which accuracy measures the dominance theorems require (additivity, strict propriety, continuity); these conditions are the bridge to loss-function choice. The author's companion "Divergences for Philosophers" covers the Bregman side.
- Check the treatment of group credences (linear vs geometric pooling), which bears on ensembling and forecast aggregation.

Access when seeded: philpapers.org and philarchive.org (record and PDF) are behind Cloudflare and returned 403. I found no other copy. The full abstract came from the author's homepage (richardpettigrew.com, "Papers – In Preparation", fetched with curl), whose PDF link points back to PhilArchive. `published:` 2025-10-29 comes from a web-search snippet saying the paper was added to PhilArchive on that date; I could not open the record to confirm it. OpenAlex and Semantic Scholar were rate-limited. No journal or DOI found. Keywords are drawn from the abstract.
