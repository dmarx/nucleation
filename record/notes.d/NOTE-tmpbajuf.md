---
status: Read
paper: 'LIT-tmp0mf8t'
title: "Randi and Leifer — Nonequilibrium Green's functions for functional connectivity"
version: 1
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Read in full on 2026-11-15 from the Europe PMC full-text XML of the
    accepted manuscript (PMC8454901,
    https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8454901/fullTextXML):
    the whole letter, with equations in linear form. Not read: the
    Supplemental Material (derivations, a third example, validity of the
    linearization, subsampling). A side reading, so kept compact. The
    filer rechecked every quote below against that copy.
date: '2026-11-15'
summary: >-
  Two-time nonequilibrium Green's functions describe functional
  connectivity in nonlinear graded networks. The measured connected
  response equals the linear resolvent plus a correction through the few
  nonlinear edges. So one nonlinear hub synapse can gate, or change the
  sign and kernel of, effective connections elsewhere. Shown in toy
  simulations inspired by C. elegans.
---
<!-- inactive-ok-file: TERM-118 — Proposed; a term the reading is set against -->

# NOTE-tmpbajuf: Randi and Leifer — Nonequilibrium Green's functions for functional connectivity

## Contribution

A formal bridge from the local couplings of a biophysical model to the
measurable responses, which include indirect paths, extended to
nonlinear, time-dependent regimes.

## Key insight

What an experiment measures between two neurons is the interior of the
network summed out. In a nonlinear network that sum depends on the
network's current state, so it is not the connectivity.

## Assumptions

Graded activity. Sparse nonlinear edges, the rest linear about
equilibrium. Small perturbations on the current state. Toy networks of
three or four neurons.

## Key results

- **Connected Green's function** (Eq. 2): obtained "by recursively
  inserting contributions of all neurons", "the resolvent kernel in
  Volterra integral equations".
- **Response ≠ connectivity**: "In the linear and TTI case, F0,ij=G0,ijj,
  while they differ in a nonlinear system."
- **One edge, effects elsewhere** (Eq. 5): "a time-dependent change of a
  single edge, due to a nonlinearity, can change effective connections and
  response functions elsewhere in the network".
- **Gating** (example 1): an edge at the foot of its sigmoid passes little
  until its neuron is driven; then the response function and the explicit
  simulation agree ("The two calculations closely agree").
- **Change of kind** (example 2): under moderate drive the response
  "transiently acquires the shape of a fractional derivativelike kernel";
  at saturation the effect vanishes.
- **Measurement**: responses "can be obtained experimentally as responses
  to impulsive perturbations", "even in subsampled networks"; recovering
  the local couplings is "experimentally impractical for larger animals".

## Concepts

Green's function; connected and direct response; resolvent kernel;
two-time response; gating; hub nonlinearity.

## Bearing on the record

- **[TERM-090](../terms.d/TERM-090.md)**: a worked instance of the "by memory" axis. Eliminating the
  interior leaves a kernel over the boundary's histories, and here it
  changes with the interior's state while no local coupling changes, which
  is the term's "effective, not fundamental". The paper's object is a
  linear response kernel, narrower than the term's projection of a
  behaviour.
- **[TERM-118](../terms.d/TERM-118.md)**: an edge with transmissive capacity unexpressed at rest and
  expressed under drive may suggest masking. That analogy is the
  record's, not the authors', and the paper shows a state-dependent
  response, not a blocked manifestation.

## Limitations

Supplement unread. Toy circuits only; no C. elegans data analysed.
