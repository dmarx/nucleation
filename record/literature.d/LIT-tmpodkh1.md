---
status: Unavailable
status_note: >-
  not read; no lawful copy located as of 2026-11-04. Looked at: the
  locations OpenAlex lists (W2011786610: only the publisher's DOI landing
  page, oa_status closed, no repository full text); Ward Whitt's Columbia
  papers index, https://www.columbia.edu/~ww2040/allpapers.html, which
  returned HTTP 403 Forbidden once and was not retried, so whether Whitt's
  site holds a copy is unresolved and a visit by hand to
  columbia.edu/~ww2040/ may find one; web searches for an author or course
  copy, which found only bibliographic records (RePEc/IDEAS, EconBiz,
  researchr) and later papers on the Halfin–Whitt regime; the publisher,
  not fetched because OpenAlex marks it closed. Unpaywall not used, since
  it requires an email address. The tutorial of van Leeuwaarden, Mathijsen
  and Zwart (2019), [LIT-tmpf2bau](LIT-tmpf2bau.md), stands in for it on the M/M/s results
  (the square-root scaling, the condition for a non-degenerate delay
  probability and its limit, the diffusion limit and its stationary
  distribution), stated and attributed but not proved; it does not stand
  in for the original's proofs, its other models, its numerical work or
  its own framing.
title: 'Heavy-Traffic Limits for Queues with Many Exponential Servers'
version: 1
history:
- version: 1
  date: '2026-11-04'
  note: >-
    Registered on 2026-11-04 from the pasted bibliography on emergency
    readiness, written by another assistant (A) and pasted by the owner on
    2026-11-04, which cites it as formalizing why capacity must be
    considered relative to stochastic fluctuations, not merely average
    demand. Citation checked against Crossref
    (api.crossref.org/works/10.1287/opre.29.3.567) and OpenAlex
    (W2011786610): Shlomo Halfin and Ward Whitt, Operations Research 29(3),
    567–588, journal article. Crossref gives the print issue as 1981-06 and
    no online date; OpenAlex gives 1981-06-01, which is `published:`. A's
    citation is correct. Not held before (no hit for the DOI or "Halfin").
    Searched for a lawful copy and found none (see the status note). At the
    owner's request a neighbouring work was read in its place: van
    Leeuwaarden, Mathijsen and Zwart (2019), LIT-tmpf2bau.
tags:
- operations-research
- probabilistic-modeling
date: '2026-11-04'
published: '1981-06-01'
doi: '10.1287/opre.29.3.567'
first_author: 'Halfin'
keywords:
- 'heavy traffic'
- 'many-server queue'
- 'M/M/s'
- 'diffusion approximation'
implementations: []
summary: >-
  Halfin & Whitt (1981). Unverified until read: no copy and no abstract
  were reached. As the tutorial of van Leeuwaarden, Mathijsen and Zwart
  (2019), [LIT-tmpf2bau](LIT-tmpf2bau.md), reports it, the paper shows that in the M/M/s queue
  the probability of delay tends to a limit strictly between zero and one
  exactly when the number of servers exceeds the offered load by a multiple
  of its square root, identifies that limit, and proves a diffusion limit
  for the scaled number in system. The pasted bibliography on emergency
  readiness cites it for sizing capacity against fluctuations rather than
  mean demand, which the tutorial bears out in substance, though not the
  "must".
---
<!-- inactive-ok-file: NOTE-tmpbp6yl THEORY-tmppfbrx — Skimmed or Proposed and new; the reading of the tutorial that stands in for Halfin and Whitt (1981) and the account filed from it, cited as open -->

# LIT-tmpodkh1: Heavy-Traffic Limits for Queues with Many Exponential Servers

Halfin, S. & Whitt, W. (1981). Heavy-Traffic Limits for Queues with Many Exponential Servers. *Operations Research* 29(3): 567–588. doi:10.1287/opre.29.3.567.

## Key takeaways

*Not read. What follows is what a later tutorial says of it, unverified
against the original.*

- **The square-root regime.** With s = λ + β√λ servers, the M/M/s delay
  probability tends to a non-degenerate limit, and the tutorial says
  Halfin and Whitt "showed that this is in fact the only scaling regime in
  which such a non-degenerate limit exists and identified" its value
  ([LIT-tmpf2bau](LIT-tmpf2bau.md), §2.1).
- **The diffusion limit.** The centred, scaled number in system tends to a
  diffusion that "is a combination of a negative-drift Brownian motion"
  above full occupancy and an Ornstein–Uhlenbeck process below it
  ([LIT-tmpf2bau](LIT-tmpf2bau.md), §2.1, Thm 2.2).
- **In its own words**, as the tutorial quotes it: "The balance between
  service and economy usually dictates that the probability of delay be
  kept away from both zero and one" ([LIT-tmpf2bau](LIT-tmpf2bau.md), §1). Checked against the
  tutorial's text only.

## Standing in the record

Registered from the pasted bibliography on emergency readiness, and not
read: no lawful copy was located, though Whitt's own site was not reached
(HTTP 403) and may hold one. A's gloss, that it formalizes why capacity
must be considered relative to stochastic fluctuations and not merely
average demand, is right in substance by the tutorial's account: the
headroom term is of the order of the load's fluctuations. The "must" is A's:
the result is asymptotic, and the efficiency-driven and quality-driven
regimes are legitimate operating choices too. A also leaves out the
economies of scale, utilization tending to one while service stays good,
which tells against reading this work as being about idle reserve kept for
rare events.

**The neighbour.** The tutorial of van Leeuwaarden, Mathijsen and Zwart
(2019), [LIT-tmpf2bau](LIT-tmpf2bau.md), read Skimmed in [NOTE-tmpbp6yl](../notes.d/NOTE-tmpbp6yl.md), stands in for it on
the M/M/s results, which it states in formulas and attributes to this
paper. It does not give the proofs (it says only that the proof "relies on
Stone's Theorem"), the original's other arrival models, its numerical work
or its own statement of scope. The account filed from the tutorial,
[THEORY-tmppfbrx](../theory.d/THEORY-tmppfbrx.md), names this paper as the original and asks for it to be
read before promotion.
