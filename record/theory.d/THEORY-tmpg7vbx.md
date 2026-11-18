---
status: Proposed
promote_when: >-
  The Supplemental derivation of Eq. 5 is read and checked, or an
  independent calculation reproduces it. Or a measurement of impulse
  responses in a graded-potential network (for example in C. elegans)
  shows the response between two neurons changing with the state of a
  third neuron on an indirect, nonlinear path, gating or changing sign or
  kernel shape, while the direct synapses stay unchanged.
title: "Randi and Leifer show that in a network of graded neurons with a few nonlinear edges, the measured response between two neurons is a state- and time-dependent nonequilibrium Green's function that differs from the connectivity, so one nonlinear hub synapse can gate, or change the sign and kernel of, effective connections elsewhere"
version: 1
tags:
- neuroscience
- network-science
- complex-systems
date: '2026-11-15'
source:
- LIT-tmp0mf8t
summary: >-
  Randi & Leifer (2021), read in [NOTE-tmpbajuf](../notes.d/NOTE-tmpbajuf.md). The connected response
  F_ij(t,t′) equals the linear resolvent plus a correction through the
  nonlinear edges (Eq. 5). In toy circuits inspired by C. elegans, a
  sigmoidal edge gates transmission, and moderate drive turns a connection
  into a fractional-derivative-like kernel, while saturation removes the
  effect. Simulation only; the supplement is unread. A neural instance of
  [TERM-090](../terms.d/TERM-090.md)'s memory kernel. The wording is the reader's; adopting it is
  the owner's call.
---

# THEORY-tmpg7vbx: Randi and Leifer show that in a network of graded neurons with a few nonlinear edges, the measured response between two neurons is a state- and time-dependent nonequilibrium Green's function that differs from the connectivity, so one nonlinear hub synapse can gate, or change the sign and kernel of, effective connections elsewhere

## Source

Randi & Leifer (2021), [LIT-tmp0mf8t](../literature.d/LIT-tmp0mf8t.md); read in [NOTE-tmpbajuf](../notes.d/NOTE-tmpbajuf.md).

## The result

Summing the network's interior between neurons j and i gives the connected
Green's function, "the resolvent kernel in Volterra integral equations".
"In the linear and TTI case, F0,ij=G0,ijj, while they differ in a nonlinear
system". With a few nonlinear edges, Eq. 5 writes the measured response as
the linear one plus a two-time correction through those edges, so "a
time-dependent change of a single edge, due to a nonlinearity, can change
effective connections and response functions elsewhere in the network". In
example 1 an edge at rest passes little and opens under drive. The
response-function prediction and the explicit simulation "closely agree".
In example 2 moderate drive changes a connection's kernel; low and high
drive do not.

## What it does not show

- Any measured C. elegans response; the examples are toy simulations.
- That the linearization holds beyond small perturbations (that is in the
  unread supplement).
- Waves, scattering or interference.
- That the local couplings can be recovered in larger animals, which the
  authors call "experimentally impractical".
