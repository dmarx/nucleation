---
status: Unavailable
status_note: >-
  not read; no lawful copy located as of 2026-11-04. Looked at: the
  publisher (INFORMS), paywalled; OpenAlex W2048267107 (oa_status closed,
  no repository full text); the TRID, RePEc and IDEAS listings, which link
  only to the DOI; web searches for an author, course or institutional
  copy, which found none; the University of Michigan pages of Mark Daskin,
  core.ac.uk and research.vu.nl, all Cloudflare challenges, not retried;
  arXiv searches for "maximum availability location" and "maximal
  availability location", which found nothing. The RAND page of Sorensen
  and Church (2010), a likely neighbour, was not tried, because rand.org
  had already returned a CloudFront block. Two neighbours stand in for it,
  on what the model maximizes and assumes only. De Oliveira, de Sá and
  Martins (2020), LIT-tmprtv5t, §2, state its aim (demand covered with
  reliability α), its assumptions (server independence, locally
  constrained service areas, availability not uniform), that it introduced
  area-specific busy fractions, and Sorensen and Church's objection to its
  α-reliability objective. Mukhopadhyay et al. (2020), LIT-tmpv1cro,
  §6.1, separate its first version, with equal busy probabilities, from
  its second, with busy fractions from local demand. Neither gives its
  zero–one formulation, how α becomes a count of servers, or the Baltimore
  results.
title: 'The Maximum Availability Location Problem'
version: 1
history:
- version: 1
  date: '2026-11-04'
  note: >-
    Registered on 2026-11-04 from the pasted bibliography on emergency
    readiness, written by another assistant (A) and pasted by the owner on
    2026-11-04, which cites it as locating emergency resources so that a
    sufficiently reliable response is available within a time standard,
    as reliability-constrained coverage rather than utilization
    maximization, mapping onto TERM-055. Citation checked against Crossref
    (api.crossref.org/works/10.1287/trsc.23.3.192) and OpenAlex
    (W2048267107): Charles ReVelle (Johns Hopkins University) and Kathleen
    Hogan (ICF), Transportation Science 23(3), 192–200, journal article.
    Crossref gives the print issue as 1989-08 and no online date, so
    `published:` is the first of that month. A's citation is correct. The
    summary follows the abstract Crossref holds. Not held before (no hit
    for the DOI, MALP, "maximum availability", ReVelle or Hogan). Searched
    for a lawful copy and found none (see the status note). At the owner's
    request two neighbouring works were read in its place: de Oliveira, de
    Sá and Martins (2020), LIT-tmprtv5t, and Mukhopadhyay et al. (2020),
    LIT-tmpv1cro.
tags:
- operations-research
- probabilistic-modeling
date: '2026-11-04'
published: '1989-08-01'
doi: '10.1287/trsc.23.3.192'
first_author: 'ReVelle'
keywords:
- 'maximum availability location problem'
- 'MALP'
- 'probabilistic location'
- 'maximal covering'
- 'reliability'
implementations: []
summary: >-
  ReVelle & Hogan (1989). Unverified until read; from the abstract on
  Crossref. A probabilistic version of the maximal covering location
  problem: "The maximum available location problem (MALP) positions p
  servers in such a way as to maximize the population which will find a
  server available within a time standard with α reliability." It stands
  to the probabilistic location set covering problem as maximal covering
  stands to location set covering, and is solved as a zero–one linear
  program on a network representing Baltimore City. The neighbours add
  that it estimates area-specific busy fractions from local demand and
  assumes independent servers.
---
<!-- inactive-ok-file: NOTE-tmpy7mc8 NOTE-tmpdnqqh — Skimmed and new; the readings of the neighbours that stand in for this work, cited as open -->

# LIT-tmpjzyct: The Maximum Availability Location Problem

ReVelle, C. & Hogan, K. (1989). The Maximum Availability Location Problem. *Transportation Science* 23(3): 192–200. doi:10.1287/trsc.23.3.192.

## Key takeaways

*Not read. From the abstract and from what two later works say of it,
unverified against the original.*

- **What it maximizes.** The population that "will find a server available
  within a time standard with α reliability" (abstract): reliability is a
  threshold per demand point, and the population above it is maximized.
- **Busy fractions.** "In MALP, ReVelle & Hogan (1989) introduce a method
  to compute an estimate of area-specific busy fractions associated with
  each demand point" (LIT-tmprtv5t, p. 10); the second version "removes"
  the assumption of equal busy probabilities (LIT-tmpv1cro, §6.1).
- **An objection.** "Sorensen & Church (2010) argue that the MALP's
  α-reliability objective function may not be appropriate in some EMS
  contexts and may lead to inferior results" (LIT-tmprtv5t, p. 11).

## Standing in the record

Registered from the pasted bibliography on emergency readiness, and not
read: no lawful copy was located. A's first sentence, that it locates
resources so that a sufficiently reliable response is available within a
time standard, matches the abstract. A's "rather than utilization
maximization" has no support: neither the abstract nor the neighbours set
the model against utilization maximization, and its stated foils are
deterministic maximal covering and probabilistic location set covering.
A's "reliability-constrained coverage" holds only if read as maximizing the
population for which α is met, not as constraining reliability across the
system. A leaves out the two versions, the independence and local-area
assumptions, and Sorensen and Church's objection.

A's "maps naturally onto Nucleation's TERM-055" is too strong. Both concern a chance
that a resource is deployed for a task within a deadline. But here
unavailability comes only from servers being busy elsewhere, with no
counterpart to the cue, retrieval or procedure that operational
availability, TERM-055, turns on; the quantity belongs to a demand node
under a whole siting plan and assumes independent servers, where TERM-055
is a chance for one resource, task and agent; and it is thresholded at α,
which TERM-055 is not. It is at most a special case of the term, not a
mapping onto it. A busy server is a formal case of present but not
deployable, CLAIM-296 and CLAIM-312. α-reliable coverage, enough servers
that one is free with probability α, is a redundancy standard the record
does not hold.

**The neighbours.** De Oliveira, de Sá and Martins (2020), LIT-tmprtv5t,
read Skimmed in NOTE-tmpy7mc8, and Mukhopadhyay et al. (2020),
LIT-tmpv1cro, read Skimmed in NOTE-tmpdnqqh, stand in for its aim, its
assumptions and its busy-fraction device, and for the distinction between
its two versions. Neither gives its formulation or results.
