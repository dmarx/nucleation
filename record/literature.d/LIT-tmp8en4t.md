---
status: Active
status_note: >-
  read 2026-10-29 (NOTE-tmpwunhc) in full, from its first author's
  dissertation in the University of Chicago's repository (chapter 3,
  appendix included); worth reading as the result that, for symmetric
  competitive Lotka–Volterra communities, MacArthur's Lyapunov function
  orders every sub-community, so the assembly graph is acyclic, every
  feasible sub-community can be built by invasions without extinctions,
  and sequential and all-at-once assembly reach the same end-points.
  Read it knowing that the copy read is the dissertation chapter of
  August 2020, not the Ecology Letters version, which was not compared;
  that order-independence (a single end-point) needs the interaction
  matrix positive definite, and an indefinite one still has priority
  effects; and that the step from the Lyapunov function to acyclicity is
  asserted, not written out.
title: 'Tractable models of ecological assembly'
version: 2
history:
- version: 1
  date: '2026-10-29'
  note: >-
    Registered on 2026-10-29 from the triage of the day (curation entry
    of 20:59), File tier, for CLAIM-369, QUESTION-132 and QUESTION-083:
    CLAIM-369's note of 2026-10-29 leaves open whether its symmetric
    class rules out cyclic invasion graphs, and this paper's assembly
    graph for symmetric competitive Lotka–Volterra is the direct test;
    the owner ruled that it drops to Consider if it does not show the
    graph acyclic. Citation checked against Crossref, PubMed and the
    bioRxiv API: Carlos A. Serván and Stefano Allesina, "Tractable models
    of ecological assembly", Ecology Letters 24(5): 1029–1037 (2021),
    doi:10.1111/ele.13702; received 8 September 2020, accepted 12
    January 2021, online 26 March 2021. Its preprint is bioRxiv
    doi:10.1101/2020.09.02.279943, v1 posted 3 September 2020, the only
    version. `published:` is that bioRxiv date, the earliest full date of
    the article (ADR-002). The first author's dissertation, "Assembling
    large ecological communities: a theoretical exploration" (University
    of Chicago, August 2020, doi:10.6082/uchicago.2656), carries the same
    title as its chapter 3 with month precision only; it is a different
    document and was not used for the date. No arXiv deposit was found.
- version: 2
  date: '2026-10-29'
  note: >-
    Read in full (NOTE-tmpwunhc), from the dissertation's chapter 3 and
    its appendix. The bioRxiv PDF returned 429 (rate limit) on
    2026-10-29 and the journal version is closed, so neither was
    compared. Status Deferred → Active. THEORY-tmplmes0 filed (Active).
    The summary is written from the reading.
tags:
- ecology
- mathematics
date: '2026-10-29'
published: '2020-09-03'
doi: '10.1111/ele.13702'
first_author: 'Serván'
keywords:
- 'ecological assembly'
- 'top-down assembly'
- 'bottom-up assembly'
- 'assembly graph'
- 'assembly endpoints'
- 'priority effects'
- 'competitive Lotka-Volterra'
- 'Lyapunov function'
implementations: []
summary: >-
  Serván & Allesina (2021), Ecology Letters 24: 1029–1037. Represents
  assembly by rare, low-density, well-separated invasions as a directed
  graph on feasible sub-communities, and proves that sequential
  (bottom-up) and all-at-once (top-down) assembly reach the same
  end-points when the graph is acyclic and attractors are exactly the
  uninvadable sub-communities. For competitive Lotka–Volterra with
  A = D(v)BD(w), B symmetric with positive entries, MacArthur's Lyapunov
  function orders the sub-communities, so both hold: with B positive
  definite there is one end-point, the sub-community of greatest total
  biomass when r = v, reachable by invasions without extinctions; with B
  indefinite there are several, and order of arrival matters. A
  consumer–resource model whose consumers can exclude resources can
  have cycles.
---
<!-- inactive-ok-file: QUESTION-083 QUESTION-132 — Open; the questions this work bears on, cited as open -->

# LIT-tmp8en4t: Tractable models of ecological assembly

Serván, C. A. & Allesina, S. (2021). Tractable models of ecological
assembly. *Ecology Letters* 24(5), 1029–1037. doi:10.1111/ele.13702.
Preprint bioRxiv 2020.09.02.279943 (3 September 2020).

Read in full on 2026-10-29 (NOTE-tmpwunhc), in the first author's
dissertation version. One account was drawn from it: THEORY-tmplmes0.

## Why this is here

The triage of 2026-10-29 put it in the File tier for CLAIM-369. That
claim's note of 2026-10-29 said that in its symmetric class the
objective L decreases along every trajectory, "which should rule out
heteroclinic cycles and so cyclic invasion graphs", and that neither
Hofbauer and Schreiber (LIT-1233) nor the reading proved it. This paper
builds the assembly graph for symmetric competitive Lotka–Volterra
communities. It also bears on QUESTION-083's entrenchment by order of
arrival and on QUESTION-132's requirement that coexistence be judged by
invasion graphs, in the potential case.
