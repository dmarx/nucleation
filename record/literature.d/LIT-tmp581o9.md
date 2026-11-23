---
status: Active
status_note: >-
  read 2026-11-23 (NOTE-tmpfz1bj) from the arXiv PDF, v2 of 2 October 2012,
  text in full, figure captions read, figure images not; worth reading as
  the record's first measurement, in a construction of more than one
  staple, of a staple's melting temperature rising once a neighbouring
  staple has closed, which LEAD-183 asked for. In a three-strand "small
  origami" a staple's melting peak rises by 1.5 to 8.5 °C when its
  neighbour is folded, and a local-equilibrium model with neighbour-dependent
  crossover penalties reproduces the annealing–melting hysteresis of four
  rectangular origamis of about 200 staples. Its main limits: two staples
  per measured construction; misfolds and kinetics excluded by hypothesis;
  model parameters fitted to the small origamis.
title: 'Cooperativity in the annealing of DNA origamis'
version: 1
history:
- version: 1
  date: '2026-11-23'
  note: >-
    Registered and read on 2026-11-23 by the lead run of that date, found
    by an arXiv API search for multi-fold DNA origami melting data (the API
    then returned HTTP 429 on a later query, which was not retried). The
    citation was checked against Crossref (no mailto): Jean-Michel Arbona,
    Jean-Pierre Aimé and Juan Elezgaray (CBMN, UMR 5248, CNRS, Pessac),
    Journal of Chemical Physics 138, published online and in print
    7 January 2013, DOI 10.1063/1.4773405. arXiv:1111.7130, v1 submitted
    30 November 2011, which is `published:`. Read from the arXiv PDF
    (https://arxiv.org/pdf/1111.7130v2), v2. Status Active.
tags:
- natural-sciences
- thermodynamics
- complex-systems
date: '2026-11-23'
published: '2011-11-30'
arxiv: '1111.7130'
doi: '10.1063/1.4773405'
first_author: 'Arbona'
keywords:
- 'DNA origami'
- 'annealing'
- 'melting'
- 'hysteresis'
- 'cooperativity'
- 'crossover'
- 'UV absorption'
implementations: []
summary: >-
  Arbona, Aimé & Elezgaray (2013; arXiv 2011). UV-absorption melting of
  three-strand "small origamis", one 64-base scaffold and two staples:
  a staple's melting peak rises when the other staple is already folded,
  from 48.5 to 51.5 °C (outer position), 41.5 to 50 °C (inner) and 67 to
  72 °C (a second staple pair), and the inner position costs more than the
  outer. A local-equilibrium model, with a crossover penalty that depends
  on which neighbouring staples are bound and a strong-correlation
  closure, reproduces the annealing and melting curves and the hysteresis
  of four rectangular M13 origamis; misfolds and kinetics are excluded by
  hypothesis.
---
<!-- inactive-ok-file: NOTE-tmpfz1bj THEORY-tmp1pfm4 — new; the reading of this work and its account, filed with it -->

# LIT-tmp581o9: Cooperativity in the annealing of DNA origamis

Arbona, J.-M., Aimé, J.-P. & Elezgaray, J. (2013). Cooperativity in the annealing of DNA origamis. *Journal of Chemical Physics* 138. doi:10.1063/1.4773405. arXiv:1111.7130.

## Key takeaways

*From the reading, NOTE-tmpfz1bj (text and captions in full; figure images not read).*

- **A closed neighbour raises a staple's melting temperature.** With B2
  folded, B1 "folds at a temperature higher than when it is alone"; "the
  presence of B2 helps the folding of B1 whatever its location"; for the
  second pair, "a shift of the melting temperature from 67 ◦ C to 72 ◦ C".
- **Position in the connectivity matters.** The "inner" position, where the
  shortest path between a crossover's ends runs through the staple itself,
  costs more than the "outer", bulge-forming one: B1 inner melts at
  41.5 °C, outer at 48.5 °C.
- **Cooperativity is needed for the large origamis.** "We show that
  cooperativity between staples is critical to quantitatively explain the
  folding process of DNA origamis."
- **Nuclei set the order.** GC-rich staples "provide with initial nuclei
  that facilitate the folding of the neighbour staples", so AT-rich ones
  fold at a temperature "dependent on the distance to the set of these
  initial nuclei".
- **No traps by construction.** The model "disregard[s] misfolded
  configurations" and "does not consider any kinetic effect".

## Standing in the record

Filed for LEAD-183, which asked for "multi-fold origami data in which a
fold's melting temperature rises once a neighbour has closed". It supplies
the smallest such data, two staples on one scaffold, and a model of about
200 staples that needs the coupling to fit. It bears on QUESTION-380 as
evidence that a closed neighbour makes the next fold cheaper, the mechanism
Majikes et al. (LIT-2117; THEORY-1454) inferred and said needed "systems
with multiple folds", and on the nucleation-and-growth picture generally.
Because misfolds are excluded, its cooperativity can only help: it cannot
show a nucleus that lowers the chance of the target. Filed from it:
THEORY-tmp1pfm4. No instruction for machine-learning practice.
