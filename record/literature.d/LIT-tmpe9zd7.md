---
status: Active
status_note: >-
  read in part 2026-11-04 ([NOTE-tmpxzaki](../notes.d/NOTE-tmpxzaki.md), Skimmed), the prose of §§5.4–5.5
  and §5.3.5 of the online edition posted by MIT; the equations, tables and
  figures there are images and were not seen. Worth reading as the
  authors' own textbook statement of the hypercube queueing model of urban
  emergency services: N distinguishable units, each busy or free, on the
  vertices of an N-cube; geographical atoms as Poisson sources;
  fixed-preference dispatch; the nine assumptions; and the unit
  workloads, inter-district dispatch fractions and travel times computed
  from the steady state, with Larson's N-equation approximation.
  Registered as the stand-in for Larson (1974), [LIT-tmpum63p](LIT-tmpum63p.md), whose model
  it restates and cites. Its main limits: the basic model evaluates the
  response areas a user supplies rather than optimizing them; priority
  dispatching is excluded; one unit is sent per call; exact computation
  grows as 2^N.
title: 'Urban Operations Research'
version: 1
history:
- version: 1
  date: '2026-11-04'
  note: >-
    Registered and read in part on 2026-11-04 as a stand-in for Larson
    (1974), LIT-tmpum63p, whose full text could not be found, at the
    owner's request; that paper is cited in the pasted bibliography on
    emergency readiness, written by another assistant (A) and pasted by
    the owner on 2026-11-04, which does not cite this book. A textbook by
    Richard C. Larson and Amedeo R. Odoni, "first published by
    Prentice-Hall, NJ, © 1981" according to the online edition's contents
    page, which also says "Massachusetts Institute of Technology © 1997-99,
    all rights reserved". No DOI; the ISBN was not checked; no Crossref or
    OpenAlex record was consulted. Only the year of first publication is
    known, so `published:` is 1981-01-01 under the first-of-the-month
    rule, the first of the year standing for a month and day not known.
    Not held before (no hit for the title, urban_or_book or Odoni). Copy:
    the online edition posted openly by MIT, the authors' institution, at
    http://web.mit.edu/urban_or_book/www/book/, chapter 5 sections fetched
    as HTML and converted to text; the equations and figures are images.
tags:
- operations-research
- probabilistic-modeling
date: '2026-11-04'
published: '1981-01-01'
url: 'http://web.mit.edu/urban_or_book/www/book/'
first_author: 'Larson'
keywords:
- 'urban operations research'
- 'spatially distributed queues'
- 'hypercube queueing model'
- 'emergency services'
- 'response areas'
- 'units of last resort'
implementations: []
summary: >-
  Larson & Odoni (1981), a textbook; only chapter 5, §§5.4–5.5, was read,
  in prose. The hypercube model represents an urban service with N
  distinguishable units over a city split into atoms, each an independent
  Poisson source of calls. Each unit is busy or free, so the state is a
  vertex of an N-cube; dispatch follows a fixed preference list per atom.
  From the steady state the authors compute each unit's workload, the
  fraction of dispatches sending each unit to each atom, the dispatches
  across response areas and the mean travel times. Workload sharing makes
  the units' workloads more even than those of their response areas.
  Exact solution needs 2^N equations; Larson's approximation needs N.
---
<!-- inactive-ok-file: NOTE-tmpxzaki THEORY-tmph4325 LIT-tmpum63p — Skimmed, Proposed or Unavailable, and new; the reading of this book, the account filed from it, and the unread original it stands in for, cited as open -->

# LIT-tmpe9zd7: Urban Operations Research

Larson, R. C. & Odoni, A. R. (1981). *Urban Operations Research*. Prentice-Hall, NJ. Online edition, MIT, http://web.mit.edu/urban_or_book/www/book/.

## Key takeaways

*From the reading, [NOTE-tmpxzaki](../notes.d/NOTE-tmpxzaki.md): chapter 5, §§5.4–5.5, prose only.*

- **The state space.** "The model's name derives from the state space
  describing the availabilities of servers" (§5.4): each server is busy
  or free.
- **Dispatch.** "This procedure is called a "fixed-preference" procedure
  since the ordered list of preferences does not change with the state of
  the system" (§5.4.2).
- **Workload sharing.** In the N = 3 example, backup dispatches make the
  units' workloads "more evenly distributed than the workloads of the
  primary response areas" (§5.4.4).
- **Units of last resort.** Units not used in routine assignment but
  "called upon during heavy workload conditions to avoid the formation of
  (or reduce the probability of) queues" (§5.4.1).
- **A decision aid, not an optimizer.** "the exact trade-off among the
  various factors must be determined by the user of the model, not by the
  model itself" (§5.4.1).

## Standing in the record

Registered as the stand-in for Larson (1974), [LIT-tmpum63p](LIT-tmpum63p.md), which the
pasted bibliography on emergency readiness cites and which could not be
found. Larson is the model's originator, and the book cites the 1974 paper
as [LARS 74a] for the model's generalizations and its computer-efficient
solution. It restates the model, not the paper: it does not give the
paper's solution algorithm, any location or redistricting search, or its
examples. The account filed from it is [THEORY-tmph4325](../theory.d/THEORY-tmph4325.md).
