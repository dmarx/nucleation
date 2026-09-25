---
status: Skimmed
paper: LIT-tmpngo4b
title: 'REST2 MD simulations of disordered proteins'
version: 1
date: '2026-09-25'
summary: >-
  A practical protocol for sampling IDP conformational ensembles with REST2 (Hamiltonian replica exchange that scales only solute interactions), covering setup, running and convergence checks in GROMACS with PLUMED, with a worked α-synuclein fragment example and public inputs.
---

<!-- inactive-ok-file: LIT-tmpngo4b — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-25 -->

# NOTE-tmpt46pj: REST2 MD simulations of disordered proteins

## Contribution

All-atom MD is valuable for characterizing the conformational ensembles of intrinsically disordered proteins. Those ensembles are heterogeneous and separated by large free-energy barriers, so explicit-solvent simulations need enhanced sampling to be statistically meaningful. Replica exchange with solute tempering runs coupled parallel replicas with selectively modified potential energies and samples IDP conformational space efficiently. The chapter shows how to set up, run and analyse such simulations.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- Theory (Introduction and REST theory): temperature replica exchange uses Metropolis swaps between temperature rungs to keep detailed balance, but continuous-time dynamics is lost. REST is a Hamiltonian replica exchange variant that heats only the solute, so it needs fewer replicas. REST2 is the widely used variant, implemented in GROMACS with PLUMED.
- Known pitfalls (Introduction): IDPs can collapse at high solute "temperature" in REST2. Two newer variants, REHT (which also heats the solvent on a gentler ladder) and REST3 (which scales solute–solvent interactions), address this.
- Workflow (Fig. 1): four stages (preparation, running, demultiplexed-replica analysis, convergence) before final analysis on the unscaled 300 K replica. Practical advice covers starting structures (linear vs. collapsed chains, ppII for prolines, trans ω, seeding known helices).
- Notes 1–10: installation and commands for GROMACS/PLUMED, box sizing, partial_tempering topology quirks, demultiplexing and PBC correction. Everything is in github.com/paulrobustelli/IDP_REST_tutorial.

## Open questions

- This is a methods tutorial in computational chemistry. Its link to probabilistic modeling is replica exchange as an MCMC or tempering sampler. The survey's note that it is not ML is correct, so it is not an anthology `biomolecular-modeling` document.
- It could be useful as a ground-truth-ensemble protocol if the owner looks at ML ensemble generators for IDPs. A deeper reading should check the convergence diagnostics section specifically.
