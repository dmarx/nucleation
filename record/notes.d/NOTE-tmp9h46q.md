---
status: Skimmed
paper: LIT-2262
title: 'Leal, Bumpus, Nickel, García, Fairbanks and Dixon — Time-Varying Data as Sheaves: an Invitation to Narratives'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Skimmed on 2026-11-22 for LEAD-023 from the arXiv copy (2609.09056v1,
    8 September 2026, 42 pages, a book chapter): the abstract, introduction,
    Vignette 3 (temporal cellular sheaves for multi-agent systems with
    switching topologies, §3.3) and the conclusion read; §2's background,
    already read in Bumpus et al. (NOTE-tmpgeiy5), and Vignettes 1 and 2
    (rigidity of the persistence–accumulation adjunction; structured
    decompositions and temporal tree-width) read for their headings and
    conclusions only. Quotations checked by script.
date: '2026-11-22'
summary: >-
  An expository chapter on narratives with three research vignettes. The
  one the record cited it for models a multi-agent system with switching
  communication topology as a narrative valued in cellular sheaves, so that
  what persists and what accumulates across topology changes is recorded,
  not only a sequence of graphs. The dynamics on such temporal sheaves, and
  a stability theory for them, are announced as work in progress.
---
<!-- inactive-ok-file: NOTE-tmpgeiy5 — Skimmed; filed by LEAD-023 -->

# NOTE-tmp9h46q: Leal, Bumpus, Nickel, García, Fairbanks and Dixon — Time-Varying Data as Sheaves: an Invitation to Narratives

## Contribution

An invitation to the theory of narratives ([LIT-2238](../literature.d/LIT-2238.md)) through three
vignettes: rigidity classes of the persistence–accumulation adjunction,
structured decompositions of narratives, and temporal cellular sheaves for
switching multi-agent systems.

## Key results (parts read)

1. **Temporal cellular sheaves (§3.3, Definition 18).** Because the category
   of cellular sheaves has pullbacks and pushouts (Lemma 3.13, proved
   elsewhere), a narrative valued in it assigns to each interval a persistent
   and a cumulative cellular sheaf, so that "both the communication topology
   and the associated sensing and interaction maps evolve coherently through
   time."
2. **What it adds (§3.3.3).** "instead of viewing a switching multiagent
   system as a sequence of independent communication graphs, the narrative
   records how information persists and accumulates as the communication
   architecture evolves." Example 14: the persisting subsystem of two
   topologies is a pullback.
3. **Dynamics not yet (§3.3.3, conclusion).** "A natural next step is to
   endow temporal cellular sheaves with dynamical systems evolving on the
   vector spaces assigned to their cells"; a stability theory "is currently
   under development".
4. **Rigidity (conclusion).** Narratives sort into rigid, left-rigid,
   right-rigid and loose by whether the persistence–accumulation round trip
   loses information.

## Assumptions

Narratives as in Bumpus et al.; cellular sheaves as functors from a graph's
incidence category to vector spaces; topology changes given as data.

## Concepts

Narrative; persistence–accumulation adjunction and rigidity; structured
decomposition and temporal width; cellular sheaf as functor; temporal
cellular sheaf.

## Bearing on the record

- **[QUESTION-282](../questions.d/QUESTION-282.md).** A temporal cellular sheaf records a correspondence
  structure (the sheaf's maps) that changes over time, and what persists
  across the changes. The changes are given switching, not made by the
  agents' interactions, and the dynamics are future work, so it offers a
  way to describe change of the operator, not a condition for it.
- **[THEORY-1088](../theory.d/THEORY-1088.md)** (a parallel). The discourse sheaf's maps change here by
  exogenous switching rather than by learning; the chapter does not cite
  the learning dynamics.
- **[QUESTION-379](../questions.d/QUESTION-379.md)** (background). The same narrative language as
  [NOTE-tmpgeiy5](NOTE-tmpgeiy5.md); nothing on realizability.

## Limitations

Skimmed, and an expository chapter: the cellular-sheaf results are stated
with proofs deferred to a companion paper. No dynamics or stability theorem
yet.
