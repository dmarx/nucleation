---
status: Unfetched
status_note: >-
  not read. The publisher's page,
  https://www.sciencedirect.com/science/article/pii/S030439750600274X
  (reached from doi:10.1016/j.tcs.2006.03.022), returned HTTP 403 with a
  captcha (a robot check) on 2026-11-05; not retried. HAL
  (https://hal.science/hal-00150860) holds metadata and the abstract only,
  no full text; two web searches found no author-posted copy (the first
  author's Aalborg pages hold a one-page poster and talk slides, not the
  paper). Probably, not certainly, the ScienceDirect item the pasted
  synthesis cites. Raussen's 2023 paper on directed path spaces in PV
  programs (LIT-tmpjapuv) was read as its neighbour: it restates the PV
  model, executions as directed paths, dihomotopy, deadlocks and
  unreachable regions, but not this paper's general po-space theory,
  examples or cubical-set and two-phase-locking results.
title: 'Algebraic topology and concurrency'
version: 1
history:
- version: 1
  date: '2026-11-05'
  note: >-
    Registered on 2026-11-05 from the owner's pasted synthesis on
    resource-bounded realizability (written by another assistant, A, in
    the same exchange as the emergency-readiness bibliography, pasted
    2026-11-04), whose Response 3 §5 says "There is an established
    literature connecting directed homotopy theory with concurrent
    computation" and links "ScienceDirect+1", naming no work. The
    identification is plausible, not certain: this paper's HAL abstract
    matches A's description (directed homotopy of semaphore programs, "a
    “directed homotopy” that does not reverse the flow of time"), but "+1"
    means a second, unknown source, and the 2016 Springer book Directed
    Algebraic Topology and Concurrency (Fajstrup, Goubault, Haucourt,
    Mimram, Raussen; doi:10.1007/978-3-319-15398-8) is another candidate
    for the field's reference, though not on ScienceDirect. Citation
    checked against Crossref and HAL: Lisbeth Fajstrup, Eric Goubault and
    Martin Raussen (Crossref order Fajstrup, Raußen, Goubault),
    Theoretical Computer Science 357(1–3), 241–278, journal article, issue
    July 2006, doi:10.1016/j.tcs.2006.03.022. `published:` is 2006-04-27,
    HAL's citation_publication_date, presumably the online date, not
    confirmed from the publisher; it is the earliest date found. Not held
    before. Not read: no lawful full text reached (status note). The
    summary follows the HAL abstract and is unverified until read.
tags:
- mathematics
date: '2026-11-05'
published: '2006-04-27'
doi: '10.1016/j.tcs.2006.03.022'
first_author: 'Fajstrup'
keywords:
- 'directed homotopy'
- 'concurrency'
- 'semaphore programs'
- 'partially ordered spaces'
- 'deadlocks'
- 'cubical sets'
implementations: []
summary: >-
  Fajstrup, Goubault & Raussen (TCS 2006). From the HAL abstract,
  unverified until read: "We exhibit a natural semantics of semaphore
  programs, based on partially ordered topological spaces, which are
  studied up to “elastic deformation” or homotopy, giving information about
  important properties of the program, such as deadlocks, unreachables,
  serializability, essential schedules, etc." The homotopy is "a “directed
  homotopy” that does not reverse the flow of time"; the abstract adds
  examples of the difference from ordinary homotopy and a link to cubical
  sets. Registered as the probable source of the pasted synthesis's
  directed-homotopy citation; its neighbour LIT-tmpjapuv was read.
---
<!-- inactive-ok-file: NOTE-tmpdizof THEORY-tmpykyk4 — Skimmed, Proposed or new; the neighbour's reading, cited as open -->

# LIT-tmph2u8y: Algebraic topology and concurrency

Fajstrup, L., Goubault, E. & Raussen, M. (2006). Algebraic topology and concurrency. *Theoretical Computer Science* 357(1–3): 241–278. doi:10.1016/j.tcs.2006.03.022.

## Key takeaways

*Not read. From the HAL abstract, unverified until read.*

- Semaphore (PV) programs get a geometric semantics in partially ordered
  topological spaces, studied up to directed homotopy, which "does not
  reverse the flow of time".
- The homotopy classes carry deadlocks, unreachable states,
  serializability and essential schedules.
- A combinatorial view through cubical sets, closer to transition systems.
- An application to the safeness of a two-phase protocol from concurrent
  database theory, and a list of open problems.

## Standing in the record

Unfetched: the publisher's page stopped at a captcha and no open copy was
found (status note). The pasted synthesis on resource-bounded
realizability cites the directed-homotopy literature to ScienceDirect for
its point that "Ordinary topological connectivity is symmetric;
computational reachability need not be." This paper is the probable
source. Its neighbour, Raussen (2023; LIT-tmpjapuv, read in NOTE-tmpdizof,
THEORY-tmpykyk4), stands in for the model and its vocabulary: PV programs
whose shared resources have capacities, executions as directed paths,
d-homotopy, deadlocks and doomed regions. It does not stand in for this
paper's own constructions and results: po-spaces in general, its examples
separating directed from ordinary homotopy, cubical sets, or its
proof that a two-phase locking protocol is safe. On what the neighbour shows, A's
point is supported, and in this model directed reachability and resource
capacity are one structure, not the two levels A separates.
