---
status: Active
status_note: >-
  read 2026-11-15 (NOTE-tmpbajuf) in full, from the accepted manuscript at
  Europe PMC (PMC8454901). The Supplemental Material was not read; the
  arXiv copy (2008.06093) may carry it. Worth reading here as a worked,
  physical instance of an effective boundary constraint with memory
  (TERM-090). Eliminating a network's interior leaves a response kernel
  that depends on the interior's state and differs from the connectivity.
title: "Nonequilibrium Green's Functions for Functional Connectivity in the Brain"
version: 1
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Registered and read on 2026-11-15 from the owner's pasted continuation
    of the ChatGPT exchange "Explain String Theory", in A's turn on waves
    in biological circuits (the owner meant transformer circuits, so this
    is a side reading). Identified from A's description ("time-dependent
    response functions for nonlinear neuronal networks, including
    illustrative calculations inspired by C. elegans"). Checked against
    the arXiv API and Crossref (no mailto): Francesco Randi and Andrew M.
    Leifer, Physical Review Letters 126, 118102 (2021-03-19),
    doi:10.1103/PhysRevLett.126.118102. `published:` is the arXiv v1 date,
    2020-08-13, the only version. No email address was sent to any
    service.
tags:
- neuroscience
- network-science
- complex-systems
date: '2026-11-15'
published: '2020-08-13'
arxiv: '2008.06093'
doi: '10.1103/PhysRevLett.126.118102'
first_author: 'Randi'
keywords:
- 'nonequilibrium Green''s functions'
- 'functional connectivity'
- 'response functions'
- 'nonlinear neuronal networks'
- 'Caenorhabditis elegans'
implementations: []
summary: >-
  Randi & Leifer (2021). They borrow two-time nonequilibrium Green's
  functions from many-body physics to describe how a perturbation of one
  neuron reaches another in a network of graded neurons with a few
  nonlinear edges. The measured, connected response equals the linear
  resolvent plus a correction carried through those edges. So one
  nonlinear, hub-like synapse can transiently gate effective connections
  elsewhere, or change their sign and kernel shape. Shown in simulated
  toy circuits inspired by C. elegans. A's description holds. The paper is
  linear-response bookkeeping, with no waves or interference. It is a
  neural instance of TERM-090's memory kernel and of its point that the
  relation is "effective, not fundamental".
---

# LIT-tmp0mf8t: Nonequilibrium Green's Functions for Functional Connectivity in the Brain

Randi, F. & Leifer, A. M. (2021). Nonequilibrium Green's Functions for Functional Connectivity in the Brain. *Physical Review Letters* 126: 118102. doi:10.1103/PhysRevLett.126.118102. [ARXIV-2008.06093](https://arxiv.org/abs/2008.06093).

## Key takeaways

*From the reading, NOTE-tmpbajuf.*

- **Response is not connectivity.** "In the linear and TTI case, F0,ij=G0,ijj,
  while they differ in a nonlinear system."
- **One edge, effects elsewhere.** "a time-dependent change of a single
  edge, due to a nonlinearity, can change effective connections and
  response functions elsewhere in the network".
- **Gating and change of kind.** An edge at the foot of its release sigmoid
  passes little until driven. Under moderate drive, an indirect path makes
  a connection's response "transiently acquires the shape of a
  fractional derivativelike kernel". Under strong drive the synapse saturates and the
  effect vanishes.
- **Measurable.** The responses "can be obtained experimentally as responses
  to impulsive perturbations", "even in subsampled networks".

## Standing in the record

A's description is accurate. The paper's object is a linear response
kernel around the current state, which is narrower than TERM-090's
set-theoretic projection of a behaviour. It is a demonstrated case of
both of that term's distinctions: memory, and a relation that changes
when the interior does with no change in any local coupling. A gated edge
that passes nothing at rest and transmits under drive may look like
masking (TERM-118). That analogy is the record's, not the authors'.
