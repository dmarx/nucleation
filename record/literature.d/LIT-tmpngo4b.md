---
status: Deferred
status_note: seeded from the abstract and a skim on 2026-09-25; not read in full
title: 'Performing all-atom molecular dynamics simulations of intrinsically disordered proteins with replica exchange solute tempering'
version: 1
tags:
- natural-sciences
- probabilistic-modeling
date: '2026-09-25'
published: '2025-05-03'
arxiv: '2505.01860'
first_author: 'Koneru'
keywords:
- 'intrinsically disordered proteins'
- 'molecular dynamics'
- 'replica exchange'
- 'solute tempering'
- 'simulation convergence'
implementations: []
summary: >-
  Koneru et al. (2025), [ARXIV-2505.01860](https://arxiv.org/abs/2505.01860). A practical protocol for sampling IDP conformational ensembles with REST2 (Hamiltonian replica exchange that scales only solute interactions), covering setup, running and convergence checks in GROMACS with PLUMED, with a worked α-synuclein fragment example and public inputs.
---

# LIT-tmpngo4b: Performing all-atom molecular dynamics simulations of intrinsically disordered proteins with replica exchange solute tempering

Jaya Krishna Koneru, Korey M. Reid, Paul Robustelli (2025), *arXiv preprint (written as a book chapter; the host volume is not named in the text)* — [ARXIV-2505.01860](https://arxiv.org/abs/2505.01860)

## Key takeaways

- A practical protocol for sampling IDP conformational ensembles with REST2 (Hamiltonian replica exchange that scales only solute interactions), covering setup, running and convergence checks in GROMACS with PLUMED, with a worked α-synuclein fragment example and public inputs.

*Seeded from the abstract and a skim, not a reading. What follows is what the work says about itself.*

All-atom MD is valuable for characterizing the conformational ensembles of intrinsically disordered proteins. Those ensembles are heterogeneous and separated by large free-energy barriers, so explicit-solvent simulations need enhanced sampling to be statistically meaningful. Replica exchange with solute tempering runs coupled parallel replicas with selectively modified potential energies and samples IDP conformational space efficiently. The chapter shows how to set up, run and analyse such simulations.

## Standing in the record

Filed from the survey of 2026-09-25 of work the anthology set aside as out of scope (tier C): 480 seconds of active reading over 3 sessions in the papers-feed tracker. `Deferred` because nobody has read it closely here yet, not on merit.

**Priority for a deeper reading: low — A how-to chapter that the skim fully characterizes. High owner time (t=480 s over 3 sessions) suggests hands-on use rather than a reading need.**

What a deeper reading should check:

- This is a methods tutorial in computational chemistry. Its link to probabilistic modeling is replica exchange as an MCMC or tempering sampler. The survey's note that it is not ML is correct, so it is not an anthology `biomolecular-modeling` document.
- It could be useful as a ground-truth-ensemble protocol if the owner looks at ML ensemble generators for IDPs. A deeper reading should check the convergence diagnostics section specifically.

Access when seeded: I read the arXiv abstract page (v1 3 May 2025, physics.chem-ph) and the full PDF (30 pp.): Introduction, REST theory, Materials, the Methods/Analysis workflow (Fig. 1), Conclusion and the Notes. The batch title is truncated ("…with replica exchange"); the full published title ends "…replica exchange solute tempering". The text calls itself "this chapter" but does not name the book, so venue is unverified beyond arXiv.
